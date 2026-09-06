---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_AssociatedUser.html
---

# AssociatedUser
<a name="API_AssociatedUser"></a>

Represents an associated user in the access control system.

## Contents
<a name="API_AssociatedUser_Contents"></a>

 ** id **   <a name="qbusiness-Type-AssociatedUser-id"></a>
The unique identifier of the associated user. This is used to identify the user in access control decisions.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** type **   <a name="qbusiness-Type-AssociatedUser-type"></a>
The type of the associated user. This indicates the scope of the user's association.
Type: String
Valid Values: `INDEX | DATASOURCE`
Required: No

## See Also
<a name="API_AssociatedUser_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/AssociatedUser)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/AssociatedUser)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/AssociatedUser)
