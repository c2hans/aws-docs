---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_ResourceStatus.html
---

# ResourceStatus
<a name="API_ResourceStatus"></a>

Details the status of Amazon Inspector for each resource type Amazon Inspector scans.

## Contents
<a name="API_ResourceStatus_Contents"></a>

 ** ec2 **   <a name="inspector2-Type-ResourceStatus-ec2"></a>
The status of Amazon Inspector scanning for Amazon EC2 resources.
Type: String
Valid Values: `ENABLING | ENABLED | DISABLING | DISABLED | SUSPENDING | SUSPENDED`
Required: Yes

 ** ecr **   <a name="inspector2-Type-ResourceStatus-ecr"></a>
The status of Amazon Inspector scanning for Amazon ECR resources.
Type: String
Valid Values: `ENABLING | ENABLED | DISABLING | DISABLED | SUSPENDING | SUSPENDED`
Required: Yes

 ** codeRepository **   <a name="inspector2-Type-ResourceStatus-codeRepository"></a>
The status of Amazon Inspector scanning for code repositories.
Type: String
Valid Values: `ENABLING | ENABLED | DISABLING | DISABLED | SUSPENDING | SUSPENDED`
Required: No

 ** lambda **   <a name="inspector2-Type-ResourceStatus-lambda"></a>
The status of Amazon Inspector scanning for AWS Lambda function.
Type: String
Valid Values: `ENABLING | ENABLED | DISABLING | DISABLED | SUSPENDING | SUSPENDED`
Required: No

 ** lambdaCode **   <a name="inspector2-Type-ResourceStatus-lambdaCode"></a>
The status of Amazon Inspector scanning for custom application code for AWS Lambda functions.
Type: String
Valid Values: `ENABLING | ENABLED | DISABLING | DISABLED | SUSPENDING | SUSPENDED`
Required: No

## See Also
<a name="API_ResourceStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/ResourceStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/ResourceStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/ResourceStatus)
