---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_PrincipalGroup.html
---

# PrincipalGroup
<a name="API_PrincipalGroup"></a>

Provides information about a group associated with the principal.

## Contents
<a name="API_PrincipalGroup_Contents"></a>

 ** access **   <a name="qbusiness-Type-PrincipalGroup-access"></a>
Provides information about whether to allow or deny access to the principal.
Type: String
Valid Values: `ALLOW | DENY`
Required: Yes

 ** membershipType **   <a name="qbusiness-Type-PrincipalGroup-membershipType"></a>
The type of group.
Type: String
Valid Values: `INDEX | DATASOURCE`
Required: No

 ** name **   <a name="qbusiness-Type-PrincipalGroup-name"></a>
The name of the group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `\P{C}*`
Required: No

## See Also
<a name="API_PrincipalGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/PrincipalGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/PrincipalGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/PrincipalGroup)
