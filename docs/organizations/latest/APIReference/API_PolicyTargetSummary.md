---
source_url: https://docs.aws.amazon.com/organizations/latest/APIReference/API_PolicyTargetSummary.html
---

# PolicyTargetSummary
<a name="API_PolicyTargetSummary"></a>

Contains information about a root, OU, or account that a policy is attached to.

## Contents
<a name="API_PolicyTargetSummary_Contents"></a>

 ** Arn **   <a name="organizations-Type-PolicyTargetSummary-Arn"></a>
The Amazon Resource Name (ARN) of the policy target.
For more information about ARNs in Organizations, see [ARN Formats Supported by Organizations](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsorganizations.html#awsorganizations-resources-for-iam-policies) in the * AWS Service Authorization Reference*.
Type: String
Pattern: `^arn:aws:organizations::.+:.+`
Required: No

 ** Name **   <a name="organizations-Type-PolicyTargetSummary-Name"></a>
The friendly name of the policy target.
The [regex pattern](http://wikipedia.org/wiki/regex) that is used to validate this parameter is a string of any of the characters in the ASCII character range.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** TargetId **   <a name="organizations-Type-PolicyTargetSummary-TargetId"></a>
The unique identifier (ID) of the policy target.
The [regex pattern](http://wikipedia.org/wiki/regex) for a target ID string requires one of the following:
+  **Root** - A string that begins with "r-" followed by from 4 to 32 lowercase letters or digits.
+  **Account** - A string that consists of exactly 12 digits.
+  **Organizational unit (OU)** - A string that begins with "ou-" followed by from 4 to 32 lowercase letters or digits (the ID of the root that the OU is in). This string is followed by a second "-" dash and from 8 to 32 additional lowercase letters or digits.
Type: String
Length Constraints: Maximum length of 100.
Pattern: `^(r-[0-9a-z]{4,32})|(\d{12})|(ou-[0-9a-z]{4,32}-[a-z0-9]{8,32})$`
Required: No

 ** Type **   <a name="organizations-Type-PolicyTargetSummary-Type"></a>
The type of the policy target.
Type: String
Valid Values: `ACCOUNT | ORGANIZATIONAL_UNIT | ROOT`
Required: No

## See Also
<a name="API_PolicyTargetSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/organizations-2016-11-28/PolicyTargetSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/organizations-2016-11-28/PolicyTargetSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/organizations-2016-11-28/PolicyTargetSummary)
