---
source_url: https://docs.aws.amazon.com/frauddetector/latest/api/API_AllowDenyList.html
---

Amazon Fraud Detector is no longer be open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker AI, AutoGluon, and AWS WAF.

# AllowDenyList
<a name="API_AllowDenyList"></a>

 The metadata of a list.

## Contents
<a name="API_AllowDenyList_Contents"></a>

 ** name **   <a name="FraudDetector-Type-AllowDenyList-name"></a>
 The name of the list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[0-9a-z_]+$`
Required: Yes

 ** arn **   <a name="FraudDetector-Type-AllowDenyList-arn"></a>
 The ARN of the list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^arn\:aws[a-z-]{0,15}\:frauddetector\:[a-z0-9-]{3,20}\:[0-9]{12}\:[^\s]{2,128}$`
Required: No

 ** createdTime **   <a name="FraudDetector-Type-AllowDenyList-createdTime"></a>
 The time the list was created.
Type: String
Length Constraints: Minimum length of 11. Maximum length of 30.
Required: No

 ** description **   <a name="FraudDetector-Type-AllowDenyList-description"></a>
 The description of the list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** updatedTime **   <a name="FraudDetector-Type-AllowDenyList-updatedTime"></a>
 The time the list was last updated.
Type: String
Length Constraints: Minimum length of 11. Maximum length of 30.
Required: No

 ** variableType **   <a name="FraudDetector-Type-AllowDenyList-variableType"></a>
 The variable type of the list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[A-Z_]{1,64}$`
Required: No

## See Also
<a name="API_AllowDenyList_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/frauddetector-2019-11-15/AllowDenyList)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/frauddetector-2019-11-15/AllowDenyList)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/frauddetector-2019-11-15/AllowDenyList)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Fraud Detector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query frauddetector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
