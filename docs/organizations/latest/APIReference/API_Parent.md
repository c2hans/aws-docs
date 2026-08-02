---
source_url: https://docs.aws.amazon.com/organizations/latest/APIReference/API_Parent.html
---

# Parent
<a name="API_Parent"></a>

Contains information about either a root or an organizational unit (OU) that can contain OUs or accounts in an organization.

## Contents
<a name="API_Parent_Contents"></a>

 ** Id **   <a name="organizations-Type-Parent-Id"></a>
The unique identifier (ID) of the parent entity.
The [regex pattern](http://wikipedia.org/wiki/regex) for a parent ID string requires one of the following:
+  **Root** - A string that begins with "r-" followed by from 4 to 32 lowercase letters or digits.
+  **Organizational unit (OU)** - A string that begins with "ou-" followed by from 4 to 32 lowercase letters or digits (the ID of the root that the OU is in). This string is followed by a second "-" dash and from 8 to 32 additional lowercase letters or digits.
Type: String
Length Constraints: Maximum length of 100.
Pattern: `^(r-[0-9a-z]{4,32})|(ou-[0-9a-z]{4,32}-[a-z0-9]{8,32})$`
Required: No

 ** Type **   <a name="organizations-Type-Parent-Type"></a>
The type of the parent entity.
Type: String
Valid Values: `ROOT | ORGANIZATIONAL_UNIT`
Required: No

## See Also
<a name="API_Parent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/organizations-2016-11-28/Parent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/organizations-2016-11-28/Parent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/organizations-2016-11-28/Parent)
