---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_Profile.html
---

# Profile
<a name="API_route53profiles_Profile"></a>

 A complex type that includes settings for a Route 53 Profile.

## Contents
<a name="API_route53profiles_Profile_Contents"></a>

 ** Arn **   <a name="Route53Profiles-Type-route53profiles_Profile-Arn"></a>
 The Amazon Resource Name (ARN) of the Profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** ClientToken **   <a name="Route53Profiles-Type-route53profiles_Profile-ClientToken"></a>
 The `ClientToken` value that was assigned when the Profile was created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** CreationTime **   <a name="Route53Profiles-Type-route53profiles_Profile-CreationTime"></a>
 The date and time that the Profile was created, in Unix time format and Coordinated Universal Time (UTC).
Type: Timestamp
Required: No

 ** Id **   <a name="Route53Profiles-Type-route53profiles_Profile-Id"></a>
 ID of the Profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** ModificationTime **   <a name="Route53Profiles-Type-route53profiles_Profile-ModificationTime"></a>
 The date and time that the Profile was modified, in Unix time format and Coordinated Universal Time (UTC).
Type: Timestamp
Required: No

 ** Name **   <a name="Route53Profiles-Type-route53profiles_Profile-Name"></a>
 Name of the Profile.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `(?!^[0-9]+$)([a-zA-Z0-9\-_' ']+)`
Required: No

 ** OwnerId **   <a name="Route53Profiles-Type-route53profiles_Profile-OwnerId"></a>
 AWS account ID of the Profile owner.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 32.
Required: No

 ** ShareStatus **   <a name="Route53Profiles-Type-route53profiles_Profile-ShareStatus"></a>
 Sharing status for the Profile.
Type: String
Valid Values: `NOT_SHARED | SHARED_WITH_ME | SHARED_BY_ME`
Required: No

 ** Status **   <a name="Route53Profiles-Type-route53profiles_Profile-Status"></a>
 The status for the Profile.
Type: String
Valid Values: `COMPLETE | DELETING | UPDATING | CREATING | DELETED | FAILED`
Required: No

 ** StatusMessage **   <a name="Route53Profiles-Type-route53profiles_Profile-StatusMessage"></a>
 Status message that includes additiona information about the Profile.
Type: String
Required: No

## See Also
<a name="API_route53profiles_Profile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53profiles-2018-05-10/Profile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53profiles-2018-05-10/Profile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53profiles-2018-05-10/Profile)
