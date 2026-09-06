---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_IdentityCenterOptionsInput.html
---

# IdentityCenterOptionsInput
<a name="API_IdentityCenterOptionsInput"></a>

Configuration settings for enabling and managing IAM Identity Center.

## Contents
<a name="API_IdentityCenterOptionsInput_Contents"></a>

 ** EnabledAPIAccess **   <a name="opensearchservice-Type-IdentityCenterOptionsInput-EnabledAPIAccess"></a>
Indicates whether IAM Identity Center is enabled for API access in Amazon OpenSearch Service.
Type: Boolean
Required: No

 ** IdentityCenterInstanceARN **   <a name="opensearchservice-Type-IdentityCenterOptionsInput-IdentityCenterInstanceARN"></a>
The ARN of the IAM Identity Center instance used to create an OpenSearch UI application that uses IAM Identity Center for authentication.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^arn:aws[a-z\\-]*:[a-z]+:[a-z0-9\\-]*:[0-9]*:[a-z0-9\\-]+\/[a-z0-9\\-]+`
Required: No

 ** IdentityCenterInstanceRegion **   <a name="opensearchservice-Type-IdentityCenterOptionsInput-IdentityCenterInstanceRegion"></a>
The Region of the IAM Identity Center instance.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 30.
Pattern: `[a-z][a-z0-9\-]+`
Required: No

 ** RolesKey **   <a name="opensearchservice-Type-IdentityCenterOptionsInput-RolesKey"></a>
Specifies the attribute that contains the backend role identifier (such as group name or group ID) in IAM Identity Center.
Type: String
Valid Values: `GroupName | GroupId`
Required: No

 ** SubjectKey **   <a name="opensearchservice-Type-IdentityCenterOptionsInput-SubjectKey"></a>
Specifies the attribute that contains the subject identifier (such as username, user ID, or email) in IAM Identity Center.
Type: String
Valid Values: `UserName | UserId | Email`
Required: No

## See Also
<a name="API_IdentityCenterOptionsInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/IdentityCenterOptionsInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/IdentityCenterOptionsInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/IdentityCenterOptionsInput)
