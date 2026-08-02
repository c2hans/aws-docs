---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_MemberUser.html
---

# MemberUser
<a name="API_MemberUser"></a>

The users that belong to a group.

## Contents
<a name="API_MemberUser_Contents"></a>

 ** userId **   <a name="qbusiness-Type-MemberUser-userId"></a>
The identifier of the user you want to map to a group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `\P{C}*`
Required: Yes

 ** type **   <a name="qbusiness-Type-MemberUser-type"></a>
The type of the user.
Type: String
Valid Values: `INDEX | DATASOURCE`
Required: No

## See Also
<a name="API_MemberUser_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/MemberUser)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/MemberUser)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/MemberUser)
