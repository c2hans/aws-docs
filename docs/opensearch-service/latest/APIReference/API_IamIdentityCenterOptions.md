---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_IamIdentityCenterOptions.html
---

# IamIdentityCenterOptions
<a name="API_IamIdentityCenterOptions"></a>

Configuration settings for IAM Identity Center in an OpenSearch application.

## Contents
<a name="API_IamIdentityCenterOptions_Contents"></a>

 ** enabled **   <a name="opensearchservice-Type-IamIdentityCenterOptions-enabled"></a>
Indicates whether IAM Identity Center is enabled for the OpenSearch application.
Type: Boolean
Required: No

 ** iamIdentityCenterApplicationArn **   <a name="opensearchservice-Type-IamIdentityCenterOptions-iamIdentityCenterApplicationArn"></a>
The Amazon Resource Name (ARN) of the domain. See [Identifiers for IAM Entities ](https://docs.aws.amazon.com/IAM/latest/UserGuide/index.html) in *Using AWS Identity and Access Management* for more information.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `.*`
Required: No

 ** iamIdentityCenterInstanceArn **   <a name="opensearchservice-Type-IamIdentityCenterOptions-iamIdentityCenterInstanceArn"></a>
The Amazon Resource Name (ARN) of the domain. See [Identifiers for IAM Entities ](https://docs.aws.amazon.com/IAM/latest/UserGuide/index.html) in *Using AWS Identity and Access Management* for more information.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `.*`
Required: No

 ** iamRoleForIdentityCenterApplicationArn **   <a name="opensearchservice-Type-IamIdentityCenterOptions-iamRoleForIdentityCenterApplicationArn"></a>
The Amazon Resource Name (ARN) of the IAM role assigned to the IAM Identity Center application for the OpenSearch application.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(aws|aws\-cn|aws\-us\-gov|aws\-iso|aws\-iso\-b):iam::[0-9]+:role\/.*`
Required: No

## See Also
<a name="API_IamIdentityCenterOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/IamIdentityCenterOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/IamIdentityCenterOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/IamIdentityCenterOptions)
