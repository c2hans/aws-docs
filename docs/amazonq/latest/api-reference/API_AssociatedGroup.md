---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_AssociatedGroup.html
---

# AssociatedGroup
<a name="API_AssociatedGroup"></a>

Represents a group associated with a given user in the access control system.

## Contents
<a name="API_AssociatedGroup_Contents"></a>

 ** name **   <a name="qbusiness-Type-AssociatedGroup-name"></a>
The name of the group associated with the user. This is used to identify the group in access control decisions.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `\P{C}*`
Required: No

 ** type **   <a name="qbusiness-Type-AssociatedGroup-type"></a>
The type of the associated group. This indicates the scope of the group's applicability.
Type: String
Valid Values: `INDEX | DATASOURCE`
Required: No

## See Also
<a name="API_AssociatedGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/AssociatedGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/AssociatedGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/AssociatedGroup)
