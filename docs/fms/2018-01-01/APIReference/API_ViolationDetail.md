---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_ViolationDetail.html
---

# ViolationDetail
<a name="API_ViolationDetail"></a>

Violations for a resource based on the specified AWS Firewall Manager policy and AWS account.

## Contents
<a name="API_ViolationDetail_Contents"></a>

 ** MemberAccount **   <a name="fms-Type-ViolationDetail-MemberAccount"></a>
The AWS account that the violation details were requested for.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^[0-9]+$`
Required: Yes

 ** PolicyId **   <a name="fms-Type-ViolationDetail-PolicyId"></a>
The ID of the AWS Firewall Manager policy that the violation details were requested for.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[a-z0-9A-Z-]{36}$`
Required: Yes

 ** ResourceId **   <a name="fms-Type-ViolationDetail-ResourceId"></a>
The resource ID that the violation details were requested for.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: Yes

 ** ResourceType **   <a name="fms-Type-ViolationDetail-ResourceType"></a>
The resource type that the violation details were requested for.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: Yes

 ** ResourceViolations **   <a name="fms-Type-ViolationDetail-ResourceViolations"></a>
List of violations for the requested resource.
Type: Array of [ResourceViolation](API_ResourceViolation.md) objects
Required: Yes

 ** ResourceDescription **   <a name="fms-Type-ViolationDetail-ResourceDescription"></a>
Brief description for the requested resource.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** ResourceTags **   <a name="fms-Type-ViolationDetail-ResourceTags"></a>
The `ResourceTag` objects associated with the resource.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

## See Also
<a name="API_ViolationDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/ViolationDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/ViolationDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/ViolationDetail)
