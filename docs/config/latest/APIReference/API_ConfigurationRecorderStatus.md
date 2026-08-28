---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_ConfigurationRecorderStatus.html
---

# ConfigurationRecorderStatus
<a name="API_ConfigurationRecorderStatus"></a>

The current status of the configuration recorder.

For a detailed status of recording events over time, add your AWS Config events to CloudWatch metrics and use CloudWatch metrics.

## Contents
<a name="API_ConfigurationRecorderStatus_Contents"></a>

 ** arn **   <a name="config-Type-ConfigurationRecorderStatus-arn"></a>
The Amazon Resource Name (ARN) of the configuration recorder.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: No

 ** lastErrorCode **   <a name="config-Type-ConfigurationRecorderStatus-lastErrorCode"></a>
The latest error code from when the recorder last failed.
Type: String
Required: No

 ** lastErrorMessage **   <a name="config-Type-ConfigurationRecorderStatus-lastErrorMessage"></a>
The latest error message from when the recorder last failed.
Type: String
Required: No

 ** lastStartTime **   <a name="config-Type-ConfigurationRecorderStatus-lastStartTime"></a>
The time the recorder was last started.
Type: Timestamp
Required: No

 ** lastStatus **   <a name="config-Type-ConfigurationRecorderStatus-lastStatus"></a>
The status of the latest recording event processed by the recorder.
Type: String
Valid Values: `Pending | Success | Failure | NotApplicable`
Required: No

 ** lastStatusChangeTime **   <a name="config-Type-ConfigurationRecorderStatus-lastStatusChangeTime"></a>
The time of the latest change in status of an recording event processed by the recorder.
Type: Timestamp
Required: No

 ** lastStopTime **   <a name="config-Type-ConfigurationRecorderStatus-lastStopTime"></a>
The time the recorder was last stopped.
Type: Timestamp
Required: No

 ** name **   <a name="config-Type-ConfigurationRecorderStatus-name"></a>
The name of the configuration recorder.
Type: String
Required: No

 ** recording **   <a name="config-Type-ConfigurationRecorderStatus-recording"></a>
Specifies whether or not the recorder is currently recording.
Type: Boolean
Required: No

 ** servicePrincipal **   <a name="config-Type-ConfigurationRecorderStatus-servicePrincipal"></a>
For service-linked configuration recorders, the service principal of the linked AWS service.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w+=,.@-]+`
Required: No

## See Also
<a name="API_ConfigurationRecorderStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/ConfigurationRecorderStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/ConfigurationRecorderStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/ConfigurationRecorderStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
