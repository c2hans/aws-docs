---
source_url: https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_CloudFormationHealth.html
---

# CloudFormationHealth
<a name="API_CloudFormationHealth"></a>

 Information about the health of AWS resources in your account that are specified by an AWS CloudFormation stack.

## Contents
<a name="API_CloudFormationHealth_Contents"></a>

 ** AnalyzedResourceCount **   <a name="DevOpsGuru-Type-CloudFormationHealth-AnalyzedResourceCount"></a>
 Number of resources that DevOps Guru is monitoring in your account that are specified by an AWS CloudFormation stack.
Type: Long
Required: No

 ** Insight **   <a name="DevOpsGuru-Type-CloudFormationHealth-Insight"></a>
 Information about the health of the AWS resources in your account that are specified by an AWS CloudFormation stack, including the number of open proactive, open reactive insights, and the Mean Time to Recover (MTTR) of closed insights.
Type: [InsightHealth](API_InsightHealth.md) object
Required: No

 ** StackName **   <a name="DevOpsGuru-Type-CloudFormationHealth-StackName"></a>
 The name of the CloudFormation stack.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[a-zA-Z*]+[a-zA-Z0-9-]*$`
Required: No

## See Also
<a name="API_CloudFormationHealth_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-guru-2020-12-01/CloudFormationHealth)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-guru-2020-12-01/CloudFormationHealth)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-guru-2020-12-01/CloudFormationHealth)
