---
source_url: https://docs.aws.amazon.com/b2bi/latest/APIReference/API_ProfileSummary.html
---

# ProfileSummary
<a name="API_ProfileSummary"></a>

Contains the details for a profile. A profile is the mechanism used to create the concept of a private network.

## Contents
<a name="API_ProfileSummary_Contents"></a>

 ** businessName **   <a name="b2bi-Type-ProfileSummary-businessName"></a>
Returns the name for the business associated with this profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 254.
Required: Yes

 ** createdAt **   <a name="b2bi-Type-ProfileSummary-createdAt"></a>
Returns the timestamp for creation date and time of the profile.
Type: Timestamp
Required: Yes

 ** name **   <a name="b2bi-Type-ProfileSummary-name"></a>
Returns the display name for profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 254.
Required: Yes

 ** profileId **   <a name="b2bi-Type-ProfileSummary-profileId"></a>
Returns the unique, system-generated identifier for the profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** logging **   <a name="b2bi-Type-ProfileSummary-logging"></a>
Specifies whether or not logging is enabled for this profile.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** logGroupName **   <a name="b2bi-Type-ProfileSummary-logGroupName"></a>
Returns the name of the logging group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** modifiedAt **   <a name="b2bi-Type-ProfileSummary-modifiedAt"></a>
Returns the timestamp that identifies the most recent date and time that the profile was modified.
Type: Timestamp
Required: No

## See Also
<a name="API_ProfileSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/b2bi-2022-06-23/ProfileSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/b2bi-2022-06-23/ProfileSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/b2bi-2022-06-23/ProfileSummary)
