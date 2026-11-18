---
source_url: https://docs.aws.amazon.com/emr/latest/ReleaseGuide/spark-optimization-agent.html
---

# Apache Spark Optimization Agent for Amazon EMR and AWS Glue
<a name="spark-optimization-agent"></a>

The Apache Spark Optimization Agent analyzes successful Spark runs on EMR Serverless and AWS Glue and returns prioritized recommendations that reduce cost or runtime.

When you ask about a successful run, the `analyze_spark_workload` tool uses the Optimization Agent. You can use the Optimization Agent from MCP clients or from the console. For setup, pricing, and architecture, see [Spark Troubleshooting and Optimization Agents](spark-troubleshoot.md).

## Types of optimization analysis
<a name="spark-optimization-agent-types"></a>

The Optimization Agent supports two kinds of analysis.
+ **Single-run optimization** – The agent analyzes one successful run for common sources of inefficiency, such as idle or underused capacity, data skew, memory pressure, and inefficient reads.
+ **Baseline comparison (regression analysis)** – The agent compares a less performant run against an earlier, better-performing baseline run. It looks at configuration, run metrics, stage and task behavior, shuffle, and capacity to isolate what changed.

For how to run each kind of analysis, see [Optimization features and capabilities](spark-optimization-features.md).

## How the Optimization Agent works
<a name="spark-optimization-agent-how"></a>

To start an optimization analysis, you need the identifiers of a successful run on EMR Serverless or AWS Glue. You then submit a prompt such as the following:

```
Analyze EMR Serverless job run {{job-run-id}} in application {{application-id}} and recommend optimizations
```

The workflow follows these steps:

1. **Feature extraction and context building** – The agent reads the run's configuration and Spark event data, and measures where time went, how evenly data was distributed, and how much capacity sat idle. This step also incorporates the optional baseline run and the cost or runtime intent.

1. **Analysis and optimization recommendations** – The agent uses AI models and knowledge of how each platform allocates capacity to turn the measurements into prioritized recommendations. You receive the following:
   + **Summary** – A short description of how the run behaved.
   + **Recommendations** – Prioritized changes, each tagged as one of the following:
     + An infrastructure change (`[infra]`), such as application capacity or worker type and count
     + A Spark configuration change (`[config]`)
     + A data layout change (`[data]`), such as repartitioning or compacting small files
   + **Recommended Spark properties (when applicable)** – The current and proposed value of each Spark property that the agent suggests changing.
   + **Comparison (baseline comparison only)** – What changed between the two runs.

The optimization process is iterative. You can continue the conversation to ask about a specific recommendation, or request a cost-focused analysis instead of a runtime-focused one. Test recommended changes in a non-production run before you apply them to production jobs.

**Topics**
+ [Types of optimization analysis](#spark-optimization-agent-types)
+ [How the Optimization Agent works](#spark-optimization-agent-how)
+ [Using the Optimization Agent](spark-optimization-using.md)
+ [Optimization features and capabilities](spark-optimization-features.md)
+ [Optimization prompt examples](spark-optimization-prompt-examples.md)
