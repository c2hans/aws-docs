---
source_url: https://docs.aws.amazon.com/emr/latest/ReleaseGuide/spark-troubleshooting-agent-troubleshooting.html
---

# Common errors and FAQs for the Apache Spark agents
<a name="spark-troubleshooting-agent-troubleshooting"></a>

## Common errors
<a name="spark-troubleshooting-common-issues"></a>

The error message from the Apache Spark agents is available in different ways for different MCP clients. This section lists general guidance for common issues that you might see when you use the Apache Spark agents for Amazon EMR and AWS Glue.

**General errors**
+ [Error: MCP server failed to load](#mcp-server-failed-to-load)
+ [Observation: Slow tool loading](#slow-tool-loading)
+ [Error: Tool invocation failed with throttling error](#throttling-error)
+ [Error: Tool responds with user error](#user-error)
+ [Error: The agent can't access your job](#spark-agents-error-access)
+ [Error: Tool responds with internal error](#internal-error)

**Troubleshooting Agent errors**
+ [Observation: Degraded tool response quality](#spark-agents-error-degraded)

**Optimization Agent errors**
+ [Error: Optimization fails because Spark event data can't be read](#spark-agents-error-event-data)
+ [Error: Optimization isn't supported for the platform, version, or run state](#spark-agents-error-unsupported)
+ [Observation: Optimization recommendations on EMR Serverless miss application-level settings](#spark-agents-error-app-settings)
+ [Observation: Baseline comparison falls back to single-run analysis](#spark-agents-error-baseline-fallback)

### Error: MCP server failed to load
<a name="mcp-server-failed-to-load"></a>
+ Verify that your MCP configurations are properly configured.
+ **Validate JSON syntax**:
  + Ensure your JSON is valid with no syntax errors.
  + Check for missing commas, quotes, or brackets.
+ Verify your local AWS credentials, and verify that the policy for the MCP IAM role is properly configured.
+ Run `/mcp` to verify MCP server availability for the Kiro CLI case.

### Observation: Slow tool loading
<a name="slow-tool-loading"></a>
+ Tools might take a few seconds to load on the first attempt to launch the server.
+ If tools don't appear, try restarting the chat.
+ Run the `/tools` command to verify tool availability.
+ Run `/mcp` to verify whether the server launched without error.

### Error: Tool invocation failed with throttling error
<a name="throttling-error"></a>
+ If you reach your service limit, wait a few seconds before you issue another tool invocation when you see the throttling exception.

### Error: Tool responds with user error
<a name="user-error"></a>
+ `AccessDeniedException` – Check the error message and fix the permission issue.
+ `InvalidInputException` – Check the error message and correct the tool input parameters.
+ `ResourceNotFoundException` – Check the error message and fix the input parameter for the resource reference.

### Error: The agent can't access your job
<a name="spark-agents-error-access"></a>

If the role that the agent uses doesn't have permission to read your job's basic details, the agent fails and can't start the analysis. You see an error message similar to the following:

```
... An error occurred (AccessDeniedException) when calling the GetJobRun operation: User: ... is not authorized to perform: glue:GetJobRun ...
```

This happens when the role lacks the describe or get permission for your platform. Grant the relevant permission for your platform from the following table, and then run the analysis again.

**Permissions to read basic job details**

| Platform | Permission |
| --- | --- |
| EMR on EC2 | elasticmapreduce:DescribeCluster, elasticmapreduce:DescribeStep |
| AWS Glue | glue:GetJob, glue:GetJobRun |
| EMR Serverless | emr-serverless:GetJobRun |
| EMR on EKS | emr-containers:DescribeVirtualCluster, emr-containers:DescribeJobRun |

### Error: Tool responds with internal error
<a name="internal-error"></a>
+ If you see `The service is handling high-volume requests`, retry the tool invocation in a few seconds.
+ If you see `INTERNAL SERVICE EXCEPTION`, document the analysis ID, tool name, any error message available from the MCP log or tool response, and optional sanitized conversation history, and contact AWS Support.

### Observation: Degraded tool response quality
<a name="spark-agents-error-degraded"></a>

The Troubleshooting Agent is designed to fail gracefully when certain signals are unavailable. If the agent can't read one of your job's signals (for example, execution logs, Spark event logs, or Spark History Server data), it still returns an analysis based on what it could read. A missing permission therefore usually appears as a less complete or lower-quality analysis rather than a hard error.

To check whether the agent was able to read everything that you expect it to, look at the `artifacts_analyzed` field in the raw tool response for your analysis. Each artifact that the agent couldn't analyze appears as `{"analyzed": false, "failure_reason": "<reason>"}`. This information isn't shown by default. In Kiro CLI, ask the agent to relay the `artifacts_analyzed` field from the most recent tool response.

The `failure_reason` often names the missing permission. For example, it might include an `AccessDeniedException`, an "is not authorized to perform" message, or an "Unauthorized access" message. Sometimes the error is more generic. Whenever an artifact shows `analyzed: false`, make sure that the role that the agent uses has the corresponding permission from [IAM permissions for the Apache Spark agents](spark-troubleshooting-agent-iam-setup.md). The following table shows some common scenarios.

**Artifacts and the permissions required to analyze them**

| Artifact (`artifacts_analyzed` key) | What it provides | If it shows `analyzed: false`, add this permission to the role |
| --- | --- | --- |
| `execution_logs`<br />`exception_stack_trace` | Driver and executor log timeline and the parsed error | Logs in Amazon S3 (EMR on EC2, EMR Serverless): `s3:GetObject`, `s3:ListBucket`.<br />Logs in CloudWatch Logs (AWS Glue): `logs:GetLogEvents`, `logs:FilterLogEvents`.<br />Logs in CloudWatch Logs (EMR on EKS): `logs:GetLogEvents`, `logs:DescribeLogGroups`, `logs:DescribeLogStreams`.<br />Encrypted logs: add `kms:Decrypt` and `kms:DescribeKey` for the customer managed key. |
| spark\_configuration | Spark environment and configuration | AWS Glue: glue:GetEnvironment, plus iam:PassRole for your AWS Glue job execution role. |
| spark\_events | Jobs, stages, and executor metrics | AWS Glue: glue:GetStages, glue:GetStage, glue:GetStageAttempt, glue:GetStageAttemptTaskList, glue:GetStageAttemptTaskSummary, glue:GetExecutors, glue:GetExecutorsThreads, glue:GetStorage, glue:GetStorageUnit, plus iam:PassRole for your AWS Glue job execution role. |
| spark\_query\_plan | SQL executions and query plans | AWS Glue: glue:GetQueries, glue:GetQuery, plus iam:PassRole for your AWS Glue job execution role. |
| spark\_history\_server | Connection to your platform's Spark UI. Appears with analyzed: false when the agent can't reach the Spark UI, or can't read any Spark UI data. | EMR on EC2 and EMR on EKS: `elasticmapreduce:CreatePersistentAppUI`, `elasticmapreduce:DescribePersistentAppUI`, `elasticmapreduce:GetPersistentAppUIPresignedURL`.<br />EMR Serverless: `emr-serverless:GetDashboardForJobRun`.<br />AWS Glue: the Spark UI permissions in the `spark_events` and `spark_query_plan` rows, plus `iam:PassRole`. Also confirm that the job run has the Spark UI turned on. |

### Error: Optimization fails because Spark event data can't be read
<a name="spark-agents-error-event-data"></a>

The Optimization Agent requires the run's Spark event data. If it can't read that data, it stops and returns an error.

**EMR Serverless**

The Optimization Agent reads Spark event data from the EMR Serverless Spark History Server, which relies on managed log storage. The analysis fails if managed log storage is turned off for the run, or if the run's logs are past the 30-day retention period. The agent returns a message similar to the following:

```
I encountered the following issue while analyzing your workload: An error occurred (ValidationException) when calling the GetDashboardForJobRun operation: Dashboard for completed job is not available as no logs are present.
```

The same message also appears right after a run finishes, before its logs are available. The message doesn't distinguish logs that expired from logs that were never present. The agent retries for about a minute before it returns this error. If you just ran the job, wait and retry. Otherwise, turn on managed log storage and analyze a more recent run whose logs are still within the 30-day window.

**AWS Glue**

The Optimization Agent reads the Spark event logs that an AWS Glue run wrote to Amazon S3 through the Glue Studio Spark UI. The run must have the Spark UI turned on: set `--enable-spark-ui` to `true` and set `--spark-event-logs-path`. The maximum supported Spark event log size is 512 MB, and 1 GB for rolling logs. Runs that wrote event logs only to the legacy path (`--enable-spark-ui-legacy-path`) aren't supported.

If the run didn't have the Spark UI turned on, or didn't write event logs to a supported path, the agent returns a message similar to the following:

```
I encountered the following issue while analyzing your workload: Spark UI (event logs) is required to read Spark event data for this Glue job run. Enable --enable-spark-ui with --spark-event-logs-path and re-run.
```

If the run wrote only legacy-format event logs, the agent returns a message similar to the following:

```
I encountered the following issue while analyzing your workload: This Glue job run wrote only legacy-format Spark event logs (--enable-spark-ui-legacy-path=true with --enable-spark-ui=false). The analysis service only supports standard-format Spark event logs. Update the job to write standard logs by setting --enable-spark-ui=true, then re-run the job and analyze the new run.
```

To fix either case, run the job again with the Spark UI turned on, and then analyze the new run.

**Permissions**

If the role can't read your run's Spark UI data, the `AccessDenied` message is passed through in the error. Grant the permission that your platform needs to read Spark data, and then run the analysis again:
+ EMR Serverless: `emr-serverless:GetDashboardForJobRun`
+ AWS Glue: the AWS Glue Spark UI permissions (`glue:RequestLogParsing`, `glue:GetLogParsingStatus`, `glue:GetEnvironment`, `glue:GetStage`, `glue:GetStages`, `glue:GetStageFiles`, `glue:BatchGetStageFiles`, `glue:GetStageAttempt`, `glue:GetStageAttemptTaskList`, `glue:GetStageAttemptTaskSummary`, `glue:GetExecutors`, `glue:GetExecutorsThreads`, `glue:GetStorage`, `glue:GetStorageUnit`, `glue:GetQueries`, `glue:GetQuery`, `glue:GetDashboardUrl`) and `iam:PassRole`

For more information, see [IAM permissions for the Apache Spark agents](spark-troubleshooting-agent-iam-setup.md).

### Error: Optimization isn't supported for the platform, version, or run state
<a name="spark-agents-error-unsupported"></a>

The Optimization Agent refuses a run that it can't optimize and returns the reason.
+ **Platform** – Optimization is available for EMR Serverless and AWS Glue only. A run on EMR on EC2 or EMR on EKS returns a message similar to the following:

  ```
  Optimization Agent is not yet supported for Amazon EMR on EC2
  ```

  ```
  Optimization Agent is not yet supported for Amazon EMR on EKS
  ```
+ **Version** – Optimization requires AWS Glue 4.0 or later and EMR Serverless `emr-7.6.0` or later. A run on an earlier version returns a message such as the following, where {{version}} and {{release}} are the run's current labels:

  ```
  Optimization Agent is not yet supported for AWS Glue {{version}}. Please upgrade to 4.0
  ```

  ```
  Optimization Agent is not yet supported for Amazon EMR Serverless {{release}}. Please upgrade to emr-7.6.0
  ```
+ **Run state** – The Optimization Agent analyzes successful runs only. A run that was stopped, canceled, or timed out returns a message similar to the following, where {{STATE}} is the run's state:

  ```
  Optimization Agent is not yet supported for {{STATE}}
  ```

  A run in any other state, such as a run that's still in progress, returns a message similar to the following:

  ```
  Analysis is only supported for succeeded/failed Spark workloads.
  ```

### Observation: Optimization recommendations on EMR Serverless miss application-level settings
<a name="spark-agents-error-app-settings"></a>

If the Optimization Agent's recommendations don't account for your EMR Serverless application's settings, the role might lack `emr-serverless:GetApplication`. The agent completes the analysis without those settings and doesn't indicate that they were missing. For recommendations that account for your application's settings, grant `emr-serverless:GetApplication` to the role. For more information, see [IAM permissions for the Apache Spark agents](spark-troubleshooting-agent-iam-setup.md).

### Observation: Baseline comparison falls back to single-run analysis
<a name="spark-agents-error-baseline-fallback"></a>

You can name one baseline run per request. If you request a baseline comparison but the Optimization Agent can't use the baseline that you named, the analysis still completes as a single-run analysis.

To tell whether this happened, check the `baseline` entry in the `artifacts_analyzed` field of the raw tool response. A dropped baseline appears as `{"analyzed": false, "failure_reason": "<reason>"}`, the same way that other artifacts appear in [Observation: Degraded tool response quality](#spark-agents-error-degraded). Also check the start of the analysis summary.

The following are common reasons that a baseline isn't used, with how to fix each one:
+ **Run ID not found** – Check the baseline run ID. The baseline must be a run of the same job (AWS Glue) or application (EMR Serverless).
+ **The baseline is the run being analyzed** – Name a different, earlier run.
+ **The baseline didn't succeed** – Choose a baseline run that succeeded.
+ **The baseline is below the supported version** – Choose a baseline on a supported version (AWS Glue 4.0 or later, or EMR Serverless `emr-7.6.0` or later).
+ **The baseline's run details couldn't be read** – Retry. If the problem persists, choose a different baseline run. Run details are the job run record, for example the AWS Glue job run details.
+ **Access denied** – Grant the missing permission to the role. For more information, see [IAM permissions for the Apache Spark agents](spark-troubleshooting-agent-iam-setup.md).
+ **The baseline's Spark event data couldn't be read** – This includes the baseline's Spark configuration. The baseline has the same Spark event data requirements as the run that you're analyzing. For these requirements, see [Error: Optimization fails because Spark event data can't be read](#spark-agents-error-event-data). For an expired EMR Serverless baseline, the `baseline` entry shows `analyzed: false`, and the summary states why the baseline wasn't used.
+ **The run didn't regress against the baseline** – The runtime or cost differences were insignificant and attributable to noise rather than a setup regression.

For more information, see [Optimization features and capabilities](spark-optimization-features.md).

## FAQs
<a name="spark-troubleshooting-qa"></a>

### Should I turn on the "trust" setting for the tools by default?
<a name="qa-trust-setting"></a>

Don't turn on the "trust" setting by default for all tool calls initially, and work in a git-versioned build environment when you accept code recommendations. Review each tool execution to understand what changes are being made.

### Does the agent change my job or apply recommendations for me?
<a name="spark-agents-qa-no-changes"></a>

No. Neither agent modifies, starts, or stops your jobs. They also don't change your job scripts, infrastructure, or other AWS resources. The agents read your job run data and return recommendations. You decide which changes to make.
+ **Troubleshooting Agent** – Returns the root cause and recommended fixes. For a code issue, it might call the code recommendation tool, which suggests a code change for you to review and apply.
+ **Optimization Agent** – Recommends configuration, infrastructure, and data changes. You apply the changes to your job or application, and then run the job again.

Review each recommendation before you apply it. As with any tuning change, test the changes in a non-production run before you apply them to production jobs, and then analyze the new run to confirm the effect.

### What are the common example prompts to use with the agents?
<a name="qa-example-prompts"></a>

For example prompts, see [Troubleshooting prompt examples](spark-troubleshooting-agent-prompt-examples.md) and [Optimization prompt examples](spark-optimization-prompt-examples.md).

### What data is transmitted to the LLM, and how is it handled?
<a name="qa-data-transmitted-to-llm"></a>

Customer data and files remain within your chosen AWS Region and aren't transmitted cross-Region. When an agent operates in a Region that uses global cross-Region inference from Amazon Bedrock, the service might route requests to the nearest Region with available capacity, depending on demand. In such cases, only extracted metadata from customer logs and processed inference results are transmitted, not the underlying customer data or files. All data is PII-masked before it's sent to the LLM for processing, whether the inference occurs within the same Region or is routed to another Region. For more information about how cross-Region inference works and which Regions are affected, see [Cross-Region processing for the Apache Spark agents](spark-troubleshooting-cross-region-processing.md).

### How can I get more fine-grained control over the agents' permissions?
<a name="spark-agents-qa-fine-grained"></a>

Because the agents run as your IAM identity, you control what they can reach. You choose which identity they use and what that identity can do. There are two ways to tighten this access.

**Option 1: Restrict your existing role with condition keys**

If you keep using your own identity, you can limit what the agents can do compared with what you can do yourself, without creating a new role. This is the quickest option. The SMUS MCP server adds two condition keys to every request, which you can reference in your IAM policies to scope down the agents' access. For more information, see [Condition keys for MCP server requests](spark-troubleshooting-agent-iam-setup.md#spark-troubleshooting-agent-mcp-permissions-change).

**Option 2: Give the agents a dedicated role**

For the tightest control, create a dedicated IAM role that's scoped to only the access that you want the agents to have, and point the MCP client at a profile that assumes it. For the complete set of permissions that the agents need at full capability, see [IAM permissions for the Apache Spark agents](spark-troubleshooting-agent-iam-setup.md).

The following AWS CloudFormation template is a quick way to create the role and its assume-role profile. The template is a sample. Modify it to meet your requirements.

**Note**
The template doesn't grant `iam:PassRole` on the AWS Glue job execution role, which both agents need for AWS Glue. Add `iam:PassRole` to the role as described in [Option B: AWS Glue](spark-troubleshooting-agent-iam-setup.md#spark-troubleshooting-agent-iam-glue).

The template creates an IAM role that has permissions to call the MCP server and the permissions required for the selected platform.

Choose one of the **Launch Stack** buttons in the following table. This launches the stack on the AWS CloudFormation console in the respective Region.

| Region | Launch |
| --- | --- |
| US East (Ohio) |  [![Launch Stack button with information icon.](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/images/cloudformation-launch-stack-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-2#/stacks/new?templateURL=https%3A%2F%2Fsmus-mcp-cfn-template-prod-us-east-2.s3.us-east-2.amazonaws.com%2Fcloudformation%2Fspark-troubleshooting-mcp-setup.yaml&stackName=spark-troubleshooting-mcp-setup)  |
| US East (N. Virginia) |  [![Launch Stack button with information icon.](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/images/cloudformation-launch-stack-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?templateURL=https%3A%2F%2Fsmus-mcp-cfn-template-prod-us-east-1.s3.us-east-1.amazonaws.com%2Fcloudformation%2Fspark-troubleshooting-mcp-setup.yaml&stackName=spark-troubleshooting-mcp-setup)  |
| US West (Oregon) |  [![Launch Stack button with information icon.](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/images/cloudformation-launch-stack-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-west-2#/stacks/new?templateURL=https%3A%2F%2Fsmus-mcp-cfn-template-prod-us-west-2.s3.us-west-2.amazonaws.com%2Fcloudformation%2Fspark-troubleshooting-mcp-setup.yaml&stackName=spark-troubleshooting-mcp-setup)  |
| Asia Pacific (Tokyo) |  [![Launch Stack button with information icon.](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/images/cloudformation-launch-stack-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/new?templateURL=https%3A%2F%2Fsmus-mcp-cfn-template-prod-ap-northeast-1.s3.ap-northeast-1.amazonaws.com%2Fcloudformation%2Fspark-troubleshooting-mcp-setup.yaml&stackName=spark-troubleshooting-mcp-setup)  |
| Europe (Ireland) |  [![Launch Stack button with information icon.](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/images/cloudformation-launch-stack-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-west-1#/stacks/new?templateURL=https%3A%2F%2Fsmus-mcp-cfn-template-prod-eu-west-1.s3.eu-west-1.amazonaws.com%2Fcloudformation%2Fspark-troubleshooting-mcp-setup.yaml&stackName=spark-troubleshooting-mcp-setup)  |
| Asia Pacific (Singapore) |  [![Launch Stack button with information icon.](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/images/cloudformation-launch-stack-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-southeast-1#/stacks/new?templateURL=https%3A%2F%2Fsmus-mcp-cfn-template-prod-ap-southeast-1.s3.ap-southeast-1.amazonaws.com%2Fcloudformation%2Fspark-troubleshooting-mcp-setup.yaml&stackName=spark-troubleshooting-mcp-setup)  |
| Asia Pacific (Sydney) |  [![Launch Stack button with information icon.](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/images/cloudformation-launch-stack-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-southeast-2#/stacks/new?templateURL=https%3A%2F%2Fsmus-mcp-cfn-template-prod-ap-southeast-2.s3.ap-southeast-2.amazonaws.com%2Fcloudformation%2Fspark-troubleshooting-mcp-setup.yaml&stackName=spark-troubleshooting-mcp-setup)  |
| Canada (Central) |  [![Launch Stack button with information icon.](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/images/cloudformation-launch-stack-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ca-central-1#/stacks/new?templateURL=https%3A%2F%2Fsmus-mcp-cfn-template-prod-ca-central-1.s3.ca-central-1.amazonaws.com%2Fcloudformation%2Fspark-troubleshooting-mcp-setup.yaml&stackName=spark-troubleshooting-mcp-setup)  |
| South America (São Paulo) |  [![Launch Stack button with information icon.](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/images/cloudformation-launch-stack-button.png)](https://console.aws.amazon.com/cloudformation/home?region=sa-east-1#/stacks/new?templateURL=https%3A%2F%2Fsmus-mcp-cfn-template-prod-sa-east-1.s3.sa-east-1.amazonaws.com%2Fcloudformation%2Fspark-troubleshooting-mcp-setup.yaml&stackName=spark-troubleshooting-mcp-setup)  |
| Europe (Frankfurt) |  [![Launch Stack button with information icon.](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/images/cloudformation-launch-stack-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-central-1#/stacks/new?templateURL=https%3A%2F%2Fsmus-mcp-cfn-template-prod-eu-central-1.s3.eu-central-1.amazonaws.com%2Fcloudformation%2Fspark-troubleshooting-mcp-setup.yaml&stackName=spark-troubleshooting-mcp-setup)  |
| Europe (Stockholm) |  [![Launch Stack button with information icon.](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/images/cloudformation-launch-stack-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-north-1#/stacks/new?templateURL=https%3A%2F%2Fsmus-mcp-cfn-template-prod-eu-north-1.s3.eu-north-1.amazonaws.com%2Fcloudformation%2Fspark-troubleshooting-mcp-setup.yaml&stackName=spark-troubleshooting-mcp-setup)  |
| Europe (London) |  [![Launch Stack button with information icon.](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/images/cloudformation-launch-stack-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-west-2#/stacks/new?templateURL=https%3A%2F%2Fsmus-mcp-cfn-template-prod-eu-west-2.s3.eu-west-2.amazonaws.com%2Fcloudformation%2Fspark-troubleshooting-mcp-setup.yaml&stackName=spark-troubleshooting-mcp-setup)  |
| Europe (Paris) |  [![Launch Stack button with information icon.](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/images/cloudformation-launch-stack-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-west-3#/stacks/new?templateURL=https%3A%2F%2Fsmus-mcp-cfn-template-prod-eu-west-3.s3.eu-west-3.amazonaws.com%2Fcloudformation%2Fspark-troubleshooting-mcp-setup.yaml&stackName=spark-troubleshooting-mcp-setup)  |
| Asia Pacific (Seoul) |  [![Launch Stack button with information icon.](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/images/cloudformation-launch-stack-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-2#/stacks/new?templateURL=https%3A%2F%2Fsmus-mcp-cfn-template-prod-ap-northeast-2.s3.ap-northeast-2.amazonaws.com%2Fcloudformation%2Fspark-troubleshooting-mcp-setup.yaml&stackName=spark-troubleshooting-mcp-setup)  |
| Asia Pacific (Mumbai) |  [![Launch Stack button with information icon.](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/images/cloudformation-launch-stack-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-south-1#/stacks/new?templateURL=https%3A%2F%2Fsmus-mcp-cfn-template-prod-ap-south-1.s3.ap-south-1.amazonaws.com%2Fcloudformation%2Fspark-troubleshooting-mcp-setup.yaml&stackName=spark-troubleshooting-mcp-setup)  |

Proceed to the **Specify stack details** page and enter the **Stack name**. Enter additional information under **Parameters**. Provide the following information, and then create the stack.
+ **TroubleshootingRoleName** – Name of the agent IAM role to create.
+ **EnableEMREC2** – Enable EMR on EC2 permissions (default: true).
+ **EnableEMRServerless** – Enable EMR Serverless permissions (default: true).
+ **EnableEMREKS** – Enable EMR on EKS permissions (default: true).
+ **EnableGlue** – Enable AWS Glue permissions (default: true).
+ **CloudWatchKmsKeyArn** – (Optional) ARN of an existing KMS key for CloudWatch Logs encryption (EMR Serverless only; leave empty for default encryption).

You can also download and review [the CloudFormation template](https://github.com/aws-samples/aws-emr-utilities/blob/03c20fece616de23ec0ea5389f0113a5bc65fc3a/utilities/apache-spark-agents/spark-troubleshooting-agent-cloudformation/spark-troubleshooting-mcp-setup.yaml), specify the preceding options, and launch the template yourself with AWS CloudFormation CLI commands. The following is an example:

```
# deploy the stack with CloudFormation CLI commands
aws cloudformation deploy \
  --template-file spark-troubleshooting-mcp-setup.yaml \
  --stack-name spark-troubleshooting-mcp-setup \
  --region <your Spark MCP server launch region> \
  --capabilities CAPABILITY_NAMED_IAM \
  --parameter-overrides \
    TroubleshootingRoleName=spark-troubleshooting-role

# retrieve the 1-line instruction to set the local environment variables, which will be used for the following MCP server configuration
aws cloudformation describe-stacks \
  --stack-name spark-troubleshooting-mcp-setup \
  --region <your Spark MCP server launch region> \
  --query "Stacks[0].Outputs[?OutputKey=='ExportCommand'].OutputValue" \
  --output text
```

Open the **Outputs** tab (or retrieve the value from the preceding `describe-stacks` command) and copy the one-line instruction from the CloudFormation output to set your environment variables. Then run it in your local environment. The following is an example one-line instruction:

```
export SMUS_MCP_REGION=<your mcp server launch region> && export IAM_ROLE=arn:aws:iam::111122223333:role/spark-troubleshooting-role-xxxxxx
```

Then run the following commands locally to set up the IAM profile and MCP server configuration. This creates a profile (`smus-mcp-profile`) that assumes the dedicated role:

```
# Step 1: Configure AWS CLI Profile
aws configure set profile.smus-mcp-profile.role_arn ${IAM_ROLE}
aws configure set profile.smus-mcp-profile.source_profile <AWS CLI Profile to assume the IAM role - ex: default>
aws configure set profile.smus-mcp-profile.region ${SMUS_MCP_REGION}

# Step 2: if you are using kiro CLI, use the following command to add the MCP configuration
# Add Spark Troubleshooting MCP Server
kiro-cli-chat mcp add \
    --name "sagemaker-unified-studio-mcp-troubleshooting" \
    --command "uvx" \
    --args "[\"mcp-proxy-for-aws@latest\",\"https://sagemaker-unified-studio-mcp.${SMUS_MCP_REGION}.api.aws/spark-troubleshooting/mcp\", \"--service\", \"sagemaker-unified-studio-mcp\", \"--profile\", \"smus-mcp-profile\", \"--region\", \"${SMUS_MCP_REGION}\", \"--read-timeout\", \"180\"]" \
    --timeout 180000 \
    --scope global

# Add Spark Code Recommendation MCP Server
kiro-cli-chat mcp add \
    --name "sagemaker-unified-studio-mcp-code-rec" \
    --command "uvx" \
    --args "[\"mcp-proxy-for-aws@latest\",\"https://sagemaker-unified-studio-mcp.${SMUS_MCP_REGION}.api.aws/spark-code-recommendation/mcp\", \"--service\", \"sagemaker-unified-studio-mcp\", \"--profile\", \"smus-mcp-profile\", \"--region\", \"${SMUS_MCP_REGION}\", \"--read-timeout\", \"180\"]" \
    --timeout 180000 \
    --scope global
```

This updates `~/.kiro/settings/mcp.json` to include the MCP server configuration as follows.

```
{
  "mcpServers": {
    "sagemaker-unified-studio-mcp-troubleshooting": {
      "type": "stdio",
      "command": "uvx",
      "args": [
        "mcp-proxy-for-aws@latest",
        "https://sagemaker-unified-studio-mcp.us-east-1.api.aws/spark-troubleshooting/mcp",
        "--service",
        "sagemaker-unified-studio-mcp",
        "--profile",
        "smus-mcp-profile",
        "--region",
        "us-east-1",
        "--read-timeout",
        "180"
      ],
      "timeout": 180000,
      "disabled": false
    },
    "sagemaker-unified-studio-mcp-code-rec": {
      "type": "stdio",
      "command": "uvx",
      "args": [
        "mcp-proxy-for-aws@latest",
        "https://sagemaker-unified-studio-mcp.us-east-1.api.aws/spark-code-recommendation/mcp",
        "--service",
        "sagemaker-unified-studio-mcp",
        "--profile",
        "smus-mcp-profile",
        "--region",
        "us-east-1",
        "--read-timeout",
        "180"
      ],
      "timeout": 180000,
      "disabled": false
    }
  }
}
```
