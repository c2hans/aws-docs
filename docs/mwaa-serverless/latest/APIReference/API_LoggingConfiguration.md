---
source_url: https://docs.aws.amazon.com/mwaa-serverless/latest/APIReference/API_LoggingConfiguration.html
---

# LoggingConfiguration
<a name="API_LoggingConfiguration"></a>

Configuration for workflow logging that specifies where you should store your workflow execution logs. Amazon Managed Workflows for Apache Airflow Serverless provides comprehensive logging capabilities that capture workflow execution details, task-level information, and system events. Logs are automatically exported to your specified CloudWatch log group using remote logging functionality, providing centralized observability across the distributed, multi-tenant execution environment. This enables effective debugging, monitoring, and compliance auditing of workflow executions.

## Contents
<a name="API_LoggingConfiguration_Contents"></a>

 ** LogGroupName **   <a name="mwaaserverless-Type-LoggingConfiguration-LogGroupName"></a>
The name of the CloudWatch log group where workflow execution logs are stored.
Type: String
Required: Yes

## See Also
<a name="API_LoggingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mwaa-serverless-2024-07-26/LoggingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mwaa-serverless-2024-07-26/LoggingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mwaa-serverless-2024-07-26/LoggingConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Workflows for Apache Airflow Serverless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mwaa-serverless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
