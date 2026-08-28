---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_CloudwatchLogsAction.html
---

# CloudwatchLogsAction
<a name="API_CloudwatchLogsAction"></a>

Describes an action that sends data to CloudWatch Logs.

## Contents
<a name="API_CloudwatchLogsAction_Contents"></a>

 ** logGroupName **   <a name="iot-Type-CloudwatchLogsAction-logGroupName"></a>
The CloudWatch log group to which the action sends data.
Type: String
Required: Yes

 ** roleArn **   <a name="iot-Type-CloudwatchLogsAction-roleArn"></a>
The IAM role that allows access to the CloudWatch log.
Type: String
Required: Yes

 ** batchMode **   <a name="iot-Type-CloudwatchLogsAction-batchMode"></a>
Indicates whether batches of log records will be extracted and uploaded into CloudWatch. Values include `true` or `false` *(default)*.
Type: Boolean
Required: No

## See Also
<a name="API_CloudwatchLogsAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/CloudwatchLogsAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/CloudwatchLogsAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/CloudwatchLogsAction)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
