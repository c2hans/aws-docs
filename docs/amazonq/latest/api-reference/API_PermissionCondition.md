---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_PermissionCondition.html
---

# PermissionCondition
<a name="API_PermissionCondition"></a>

Defines a condition that restricts when a permission is effective. Conditions allow you to control access based on specific attributes of the request.

## Contents
<a name="API_PermissionCondition_Contents"></a>

 ** conditionKey **   <a name="qbusiness-Type-PermissionCondition-conditionKey"></a>
The key for the condition. This identifies the attribute that the condition applies to.
Type: String
Pattern: `aws:PrincipalTag/qbusiness-dataaccessor:[a-zA-Z]+.*`
Required: Yes

 ** conditionOperator **   <a name="qbusiness-Type-PermissionCondition-conditionOperator"></a>
The operator to use for the condition evaluation. This determines how the condition values are compared.
Type: String
Valid Values: `StringEquals`
Required: Yes

 ** conditionValues **   <a name="qbusiness-Type-PermissionCondition-conditionValues"></a>
The values to compare against using the specified condition operator.
Type: Array of strings
Array Members: Fixed number of 1 item.
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_-]*`
Required: Yes

## See Also
<a name="API_PermissionCondition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/PermissionCondition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/PermissionCondition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/PermissionCondition)
