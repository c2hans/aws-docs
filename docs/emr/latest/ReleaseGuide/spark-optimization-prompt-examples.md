---
source_url: https://docs.aws.amazon.com/emr/latest/ReleaseGuide/spark-optimization-prompt-examples.html
---

# Optimization prompt examples
<a name="spark-optimization-prompt-examples"></a>

You can use the following prompt examples with the Optimization Agent. Replace the placeholders with your own values.

## Optimize a run for runtime
<a name="spark-optimization-prompt-runtime"></a>

EMR Serverless:

```
How can I make my EMR Serverless job run {{job-run-id}} in application {{application-id}} faster?
```

AWS Glue:

```
Optimize my Glue job {{job-name}} run {{job-run-id}} for runtime performance and speed
```

## Optimize a run for cost
<a name="spark-optimization-prompt-cost"></a>

EMR Serverless:

```
Optimize my EMR Serverless job run {{job-run-id}} in application {{application-id}} for cost. How can I make it cheaper?
```

AWS Glue:

```
How can I reduce the cost of my Glue job {{job-name}} run {{job-run-id}}?
```

## Compare a run against a baseline
<a name="spark-optimization-prompt-baseline"></a>

EMR Serverless:

```
My EMR Serverless job run {{job-run-id}} in application {{application-id}} got slower than run {{baseline-job-run-id}}. Tell me why and how to fix it.
```

AWS Glue:

```
Compare Glue job run {{job-run-id}} against baseline run {{baseline-job-run-id}} of job {{job-name}} and tell me what regressed
```
