---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAclGroup.html
---

# DocumentAclGroup
<a name="API_DocumentAclGroup"></a>

Represents a group in the document's ACL, used to define access permissions for multiple users collectively.

## Contents
<a name="API_DocumentAclGroup_Contents"></a>

 ** name **   <a name="qbusiness-Type-DocumentAclGroup-name"></a>
The name of the group in the document's ACL. This is used to identify the group when applying access rules.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `\P{C}*`
Required: No

 ** type **   <a name="qbusiness-Type-DocumentAclGroup-type"></a>
The type of the group. This indicates the scope of the group's applicability in access control.
Type: String
Valid Values: `INDEX | DATASOURCE`
Required: No

## See Also
<a name="API_DocumentAclGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/DocumentAclGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/DocumentAclGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/DocumentAclGroup)
