---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/tuning-aws-glue-for-apache-spark/optimize-user-defined-functions.html
---

# Optimize user-defined functions
<a name="optimize-user-defined-functions"></a>

User-defined functions (UDFs) and `RDD.map` in PySpark often degrade performance significantly. This is because of the overhead required to accurately represent your Python code in Spark's underlying Scala implementation.

The following diagram shows the architecture of PySpark jobs. When you use PySpark, the Spark driver uses the Py4j library to call Java methods from Python. When calling Spark SQL or DataFrame built-in functions, there is little performance difference between Python and Scala because the functions run on each executor's JVM using an optimized execution plan.

![Spark context connects to Spark driver using Py4J, and driver connects to the worker nodes.](http://docs.aws.amazon.com/prescriptive-guidance/latest/tuning-aws-glue-for-apache-spark/images/guide-img/ee14755c-1401-4ea5-afc7-732eb483b047/images/46526efc-3ccc-4c96-816f-88cbf018f0e3.png)

If you use your own Python logic, such as using `map/ mapPartitions/ udf`, the task will run in a Python runtime environment. Managing two environments creates an overhead cost. Additionally, your data in memory must be transformed for use by the JVM runtime environment's built-in functions. *Pickle* is a serialization format used by default for the exchange between the JVM and Python runtimes. However, the cost of this serialization and deserialization cost is very high, so UDFs written in Java or Scala are faster than Python UDFs.

To avoid serialization and deserialization overhead in PySpark, consider the following:
+ **Use the built-in Spark SQL functions** – Consider replacing your own UDF or map function with Spark SQL or DataFrame built-in functions. When running Spark SQL or DataFrame built-in functions, there is little performance difference between Python and Scala because the tasks are handled on each executor's JVM .
+ **Implement UDFs in Scala or Java** – Consider using a UDF which is written in Java or Scala, because they run on the JVM.
+ **Use Apache Arrow-based UDFs for vectorized workloads** – Consider using Arrow-based UDFs. This feature is also known as Vectorized UDF (Pandas UDF). [Apache Arrow](https://arrow.apache.org/) is a language-agnostic in-memory data format that AWS Glue can use to efficiently transfer data between JVM and Python processes. This is currently most beneficial to Python users that work with Pandas or NumPy data.

  Arrow is a columnar (vectorized) format. Its usage is not automatic and might require some minor changes to configuration or code to take full advantage and ensure compatibility. For more detail and limitations see [Apache Arrow in PySpark](https://spark.apache.org/docs/latest/api/python/tutorial/sql/arrow_pandas.html).

  The following example compares a basic incremental UDF in standard Python, as a Vectorized UDF, and in Spark SQL.

## Standard Python UDF
<a name="python-udf"></a>

Example time is 3.20 (sec).

**Example code**

```
# DataSet
df = spark.range(10000000).selectExpr("id AS a","id AS b")

# UDF Example
def plus(a,b):
    return a+b
spark.udf.register("plus",plus)

df.selectExpr("count(plus(a,b))").collect()
```

**Execution plan**

```
== Physical Plan ==
AdaptiveSparkPlan isFinalPlan=false
+- HashAggregate(keys=[], functions=[count(pythonUDF0#124)])
+- Exchange SinglePartition, ENSURE_REQUIREMENTS, [id=#580]
+- HashAggregate(keys=[], functions=[partial_count(pythonUDF0#124)])
+- Project [pythonUDF0#124]
+- BatchEvalPython [plus(a#116L, b#117L)], [pythonUDF0#124]
+- Project [id#114L AS a#116L, id#114L AS b#117L]
+- Range (0, 10000000, step=1, splits=16)
```

## Vectorized UDF
<a name="vectorized-udf"></a>

Example time is 0.59 (sec).

The Vectorized UDF is 5 times faster than the previous UDF example. Checking `Physical Plan`, you can see `ArrowEvalPython`, which shows this application is vectorized by Apache Arrow. To enable Vectorized UDF, you must specify `spark.sql.execution.arrow.pyspark.enabled = true` in your code.

**Example code**

```
# Vectorized UDF
from pyspark.sql.types import LongType
from pyspark.sql.functions import count, pandas_udf

# Enable Apache Arrow Support
spark.conf.set("spark.sql.execution.arrow.pyspark.enabled", "true")

# DataSet
df = spark.range(10000000).selectExpr("id AS a","id AS b")

# Annotate pandas_udf to use Vectorized UDF
@pandas_udf(LongType())
def pandas_plus(a,b):
    return a+b
spark.udf.register("pandas_plus",pandas_plus)

df.selectExpr("count(pandas_plus(a,b))").collect()
```

**Execution plan**

```
== Physical Plan ==
AdaptiveSparkPlan isFinalPlan=false
+- HashAggregate(keys=[], functions=[count(pythonUDF0#1082L)], output=[count(pandas_plus(a, b))#1080L])
+- Exchange SinglePartition, ENSURE_REQUIREMENTS, [id=#5985]
+- HashAggregate(keys=[], functions=[partial_count(pythonUDF0#1082L)], output=[count#1084L])
+- Project [pythonUDF0#1082L]
+- ArrowEvalPython [pandas_plus(a#1074L, b#1075L)], [pythonUDF0#1082L], 200
+- Project [id#1072L AS a#1074L, id#1072L AS b#1075L]
+- Range (0, 10000000, step=1, splits=16)
```

## Spark SQL
<a name="spark-sql"></a>

Example time is 0.087 (sec).

Spark SQL is much faster than Vectorized UDF, because the tasks are run on each executor's JVM without a Python runtime . If you can replace your UDF with a built-in function, we recommend doing so.

**Example code**

```
df.createOrReplaceTempView("test")
spark.sql("select count(a+b) from test").collect()
```

## Using pandas for big data
<a name="pandas"></a>

If you are already familiar with [pandas](https://pandas.pydata.org/docs/) and want to use Spark for big data, you can use the pandas API on Spark. AWS Glue 4.0 and later support it. To get started, you can use the official notebook[ Quickstart: Pandas API on Spark](https://spark.apache.org/docs/latest/api/python/getting_started/quickstart_ps.html). For more information, see the [PySpark documentation](https://spark.apache.org/docs/latest/api/python/index.html).
