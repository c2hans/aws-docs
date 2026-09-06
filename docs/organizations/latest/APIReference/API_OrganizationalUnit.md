---
source_url: https://docs.aws.amazon.com/organizations/latest/APIReference/API_OrganizationalUnit.html
---

# OrganizationalUnit
<a name="API_OrganizationalUnit"></a>

Contains details about an organizational unit (OU). An OU is a container of AWS accounts within a root of an organization. Policies that are attached to an OU apply to all accounts contained in that OU and in any child OUs.

## Contents
<a name="API_OrganizationalUnit_Contents"></a>

 ** Arn **   <a name="organizations-Type-OrganizationalUnit-Arn"></a>
The Amazon Resource Name (ARN) of this OU.
For more information about ARNs in Organizations, see [ARN Formats Supported by Organizations](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsorganizations.html#awsorganizations-resources-for-iam-policies) in the * AWS Service Authorization Reference*.
Type: String
Pattern: `^arn:aws:organizations::\d{12}:ou\/o-[a-z0-9]{10,32}\/ou-[0-9a-z]{4,32}-[0-9a-z]{8,32}`
Required: No

 ** Id **   <a name="organizations-Type-OrganizationalUnit-Id"></a>
The unique identifier (ID) associated with this OU. The ID is unique to the organization only.
The [regex pattern](http://wikipedia.org/wiki/regex) for an organizational unit ID string requires "ou-" followed by from 4 to 32 lowercase letters or digits (the ID of the root that contains the OU). This string is followed by a second "-" dash and from 8 to 32 additional lowercase letters or digits.
Type: String
Length Constraints: Maximum length of 68.
Pattern: `^ou-[0-9a-z]{4,32}-[a-z0-9]{8,32}$`
Required: No

 ** Name **   <a name="organizations-Type-OrganizationalUnit-Name"></a>
The friendly name of this OU.
The [regex pattern](http://wikipedia.org/wiki/regex) that is used to validate this parameter is a string of any of the characters in the ASCII character range.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\s\S]*`
Required: No

 ** Path **   <a name="organizations-Type-OrganizationalUnit-Path"></a>
The path in the organization where this OU exists.
Type: String
Pattern: `^(o-[a-z0-9]{10,32}\/r-[0-9a-z]{4,32}(\/ou\-[0-9a-z]{4,32}-[a-z0-9]{8,32})*(\/\d{12})*)\/`
Required: No

## See Also
<a name="API_OrganizationalUnit_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/organizations-2016-11-28/OrganizationalUnit)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/organizations-2016-11-28/OrganizationalUnit)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/organizations-2016-11-28/OrganizationalUnit)
