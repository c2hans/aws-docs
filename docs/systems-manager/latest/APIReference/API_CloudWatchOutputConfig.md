---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_CloudWatchOutputConfig.html
---

# CloudWatchOutputConfig
<a name="API_CloudWatchOutputConfig"></a>

Configuration options for sending command output to Amazon CloudWatch Logs.

## Contents
<a name="API_CloudWatchOutputConfig_Contents"></a>

 ** CloudWatchLogGroupName **   <a name="systemsmanager-Type-CloudWatchOutputConfig-CloudWatchLogGroupName"></a>
The name of the CloudWatch Logs log group where you want to send command output. If you don't specify a group name, AWS Systems Manager automatically creates a log group for you. The log group uses the following naming format:
 `aws/ssm/SystemsManagerDocumentName `
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** CloudWatchOutputEnabled **   <a name="systemsmanager-Type-CloudWatchOutputConfig-CloudWatchOutputEnabled"></a>
Enables Systems Manager to send command output to CloudWatch Logs.
Type: Boolean
Required: No

## See Also
<a name="API_CloudWatchOutputConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/CloudWatchOutputConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/CloudWatchOutputConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/CloudWatchOutputConfig)
