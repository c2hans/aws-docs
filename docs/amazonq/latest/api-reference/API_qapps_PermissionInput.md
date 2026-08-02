---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_PermissionInput.html
---

# PermissionInput
<a name="API_qapps_PermissionInput"></a>

The permission to grant or revoke for a Amazon Q App.

## Contents
<a name="API_qapps_PermissionInput_Contents"></a>

 ** action **   <a name="qbusiness-Type-qapps_PermissionInput-action"></a>
The action associated with the permission.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Valid Values: `read | write`
Required: Yes

 ** principal **   <a name="qbusiness-Type-qapps_PermissionInput-principal"></a>
The principal user to which the permission applies.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## See Also
<a name="API_qapps_PermissionInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qapps-2023-11-27/PermissionInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qapps-2023-11-27/PermissionInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qapps-2023-11-27/PermissionInput)
