---
source_url: https://docs.aws.amazon.com/organizations/latest/APIReference/API_Child.html
---

# Child
<a name="API_Child"></a>

Contains a list of child entities, either OUs or accounts.

## Contents
<a name="API_Child_Contents"></a>

 ** Id **   <a name="organizations-Type-Child-Id"></a>
The unique identifier (ID) of this child entity.
The [regex pattern](http://wikipedia.org/wiki/regex) for a child ID string requires one of the following:
+  **Account** - A string that consists of exactly 12 digits.
+  **Organizational unit (OU)** - A string that begins with "ou-" followed by from 4 to 32 lowercase letters or digits (the ID of the root that contains the OU). This string is followed by a second "-" dash and from 8 to 32 additional lowercase letters or digits.
Type: String
Length Constraints: Maximum length of 100.
Pattern: `^(\d{12})|(ou-[0-9a-z]{4,32}-[a-z0-9]{8,32})$`
Required: No

 ** Type **   <a name="organizations-Type-Child-Type"></a>
The type of this child entity.
Type: String
Valid Values: `ACCOUNT | ORGANIZATIONAL_UNIT`
Required: No

## See Also
<a name="API_Child_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/organizations-2016-11-28/Child)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/organizations-2016-11-28/Child)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/organizations-2016-11-28/Child)
