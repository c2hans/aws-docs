---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_ProfileSummary.html
---

# ProfileSummary
<a name="API_route53profiles_ProfileSummary"></a>

 Summary information about a Route 53 Profile.

## Contents
<a name="API_route53profiles_ProfileSummary_Contents"></a>

 ** Arn **   <a name="Route53Profiles-Type-route53profiles_ProfileSummary-Arn"></a>
 The Amazon Resource Name (ARN) of the Profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** Id **   <a name="Route53Profiles-Type-route53profiles_ProfileSummary-Id"></a>
 ID of the Profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** Name **   <a name="Route53Profiles-Type-route53profiles_ProfileSummary-Name"></a>
 Name of the Profile.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `(?!^[0-9]+$)([a-zA-Z0-9\-_' ']+)`
Required: No

 ** ShareStatus **   <a name="Route53Profiles-Type-route53profiles_ProfileSummary-ShareStatus"></a>
 Share status of the Profile.
Type: String
Valid Values: `NOT_SHARED | SHARED_WITH_ME | SHARED_BY_ME`
Required: No

## See Also
<a name="API_route53profiles_ProfileSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53profiles-2018-05-10/ProfileSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53profiles-2018-05-10/ProfileSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53profiles-2018-05-10/ProfileSummary)
