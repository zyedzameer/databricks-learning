# DAG (Directed Acyclic Graph) in Spark

# What is DAG?

DAG stands for:

**Directed Acyclic Graph**

It represents the execution flow of Spark transformations.

Spark does not execute transformations immediately.
Instead, it builds a logical execution graph first and executes it only when an action is triggered.

---

# Why Spark Uses DAG

Traditional execution model:

```text
Step 1 → Execute
Step 2 → Execute
Step 3 → Execute
```

Spark model:

```text
Build full execution plan first
        ↓
Optimize globally
        ↓
Execute efficiently
```

This is possible because Spark follows:

# Lazy Evaluation

Transformations are only recorded until an action is called.

Example:

```python
df.filter(col("age") > 30) \
  .groupBy("city") \
  .count()
```

No execution happens yet.

Execution starts only after actions like:

```python
count()
collect()
write()
show()
```

---

# Benefits of DAG

## 1. Optimization

Spark gets complete visibility of the query.

This allows Catalyst Optimizer to:

* reorder filters
* push predicates
* prune columns
* optimize joins
* reduce shuffles

Without DAG:

* Spark would execute blindly step-by-step
* performance would be much worse

---

## 2. Fault Tolerance

Spark maintains lineage information.

If a partition is lost:

* Spark can recompute only required partitions
* instead of rerunning entire job

Spark remembers:

```text
How was this data derived?
```

This lineage-based recovery is core to Spark architecture.

---

# Important Clarification

DAG lineage is NOT same as checkpointing.

| Concept       | Meaning                           |
| ------------- | --------------------------------- |
| DAG Lineage   | Recompute lost partitions         |
| Cache/Persist | Store intermediate data           |
| Checkpoint    | Persist stable intermediate state |

---

# DAG and Spark Internals

Spark internally creates multiple plans.

## 1. Logical Plan

What user requested.

Example:

```python
df.filter(...).groupBy(...).count()
```

---

## 2. Optimized Logical Plan

Catalyst applies optimization rules.

Examples:

* predicate pushdown
* column pruning
* constant folding

---

## 3. Physical Plan

Spark decides:

* join strategy
* shuffle plan
* partitioning strategy

---

## 4. DAG of Stages and Tasks

Actual distributed execution plan.

---

# DAG and Shuffle

Wide transformations create shuffle boundaries.

Examples:

* groupBy
* join
* distinct
* orderBy

Why?

Because data must move across executors.

Example:

```python
df.groupBy("city").count()
```

Spark must ensure:

* all same city records end up together

This causes:

* network transfer
* disk spill
* serialization overhead

---

# Narrow vs Wide Transformations

| Type    | Shuffle Required? |
| ------- | ----------------- |
| filter  | No                |
| map     | No                |
| select  | No                |
| groupBy | Yes               |
| join    | Yes               |
| orderBy | Yes               |

---

# Why Shuffle Is Expensive

Shuffle causes:

* network I/O
* serialization/deserialization
* disk spill
* stage synchronization
* skew problems

In Databricks:

* shuffle-heavy jobs increase runtime
* inefficient jobs consume more DBUs

---

# DAG and Catalyst Optimizer

Catalyst relies on DAG visibility.

Spark can optimize entire query before execution.

Examples:

## Column Pruning

Read only required columns.

```python
df.select("name", "city")
```

---

## Predicate Pushdown

Push filters to storage layer.

```python
df.filter(col("age") > 30)
```

Parquet/Delta may skip unnecessary data blocks.

---

## Partition Pruning

Skip unnecessary partition directories.

Example:

```text
/year=2024/
/year=2025/
```

Query:

```sql
WHERE year = 2025
```

Spark skips irrelevant partitions completely.

---

# DAG and Databricks

Databricks still uses Spark underneath.

Advanced optimizations rely heavily on DAG analysis:

* AQE (Adaptive Query Execution)
* Photon
* Delta statistics
* Broadcast joins
* Dynamic partition pruning

Databricks performance improvements depend on:

* runtime statistics
* metadata
* DAG visibility

---

# Important Databricks Mindset

Spark optimization is often:

# "How do we reduce shuffle?"

Because shuffle:

* slows execution
* increases cloud cost
* increases DBU usage

---

# Real-World Example

```python
df.filter(col("status") == "SUCCESS") \
  .groupBy("customer") \
  .sum("amount")
```

Spark internally builds DAG first:

```text
Read Data
   ↓
Filter SUCCESS
   ↓
Shuffle by customer
   ↓
Aggregate amount
   ↓
Return result
```

Then:

* Catalyst optimizes
* AQE may adapt at runtime
* physical execution begins

---

# Key Takeaways

* Spark builds DAG before execution
* DAG enables optimization
* DAG enables fault tolerance
* Spark uses lazy evaluation
* Wide transformations create shuffle
* Shuffle is one of biggest Spark costs
* Catalyst depends on DAG visibility
* Databricks optimizations heavily rely on DAG analysis

---

# Senior-Level Insight

Good Spark engineers do not think only in APIs.

They think in:

* execution plans
* shuffle behavior
* partition movement
* runtime cost
* cluster efficiency

Understanding DAG deeply is foundation for:

* Spark tuning
* Delta Lake optimization
* Databricks performance engineering
* cloud cost optimization
