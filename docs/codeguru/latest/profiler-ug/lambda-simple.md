---
source_url: https://docs.aws.amazon.com/codeguru/latest/profiler-ug/lambda-simple.html
---

# Easier option for Java 8 on Amazon Linux 2 and Java 11 and Java 17 (Corretto) runtimes
<a name="lambda-simple"></a>

You can enable CodeGuru Profiler from the AWS console by setting environment variables and updating configuration for your AWS Lambda function. This method works for Java 8 on Amazon Linux 2 and Java 11 and Java 17 (Corretto) runtimes.

If you're profiling applications that run on Lambda, set the following environment variables to your Lambda function.
+ `AWS_CODEGURU_PROFILER_GROUP_NAME` – Identifies the profiling group name.
+ `AWS_CODEGURU_PROFILER_TARGET_REGION` – Identifies the target region of the profiling group.
+ `AWS_CODEGURU_PROFILER_HEAP_SUMMARY_ENABLED` – Optional. Set this variable to `true` to enable heap summary. The default is `false`.
+ `JAVA_TOOL_OPTIONS` – Set this variable to `-javaagent:/opt/codeguru-profiler-java-agent-standalone.jar`.

For information about setting environment variables in the AWS Lambda console, see [Using AWS Lambda environment variables](https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html).

Add a layer to your Lambda function using the following layer ARN. For more information on Lambda layers, see [AWS Lambda Layers](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html#configuration-layers-using).

```
arn:aws:lambda:{{LAMBDA-FUNCTION-REGION-CODE}}:157417159150:layer:AWSCodeGuruProfilerJavaAgentLayer:12
```

For example, if your Lambda function is in Region `us-east-1`, then the ARN would be the following.

```
arn:aws:lambda:us-east-1:157417159150:layer:AWSCodeGuruProfilerJavaAgentLayer:12
```

The CodeGuru Profiler heap summary is an optional feature that shows your application's heap usage over time. For more information on the heap summary, see [Understanding the heap summary](working-with-visualizations-heap-summary.md).

Your Lambda function runs normally with the CodeGuru Profiler agent running in parallel. The agent submits your first profile after running for a total of 5 minutes. Processing can take up to 15 minutes.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeGuru. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codeguru` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
