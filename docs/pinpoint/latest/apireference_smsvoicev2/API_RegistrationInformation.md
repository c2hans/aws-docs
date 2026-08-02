---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_RegistrationInformation.html
---

# RegistrationInformation
<a name="API_RegistrationInformation"></a>

Provides information about the requested registration.

## Contents
<a name="API_RegistrationInformation_Contents"></a>

 ** CreatedTimestamp **   <a name="pinpoint-Type-RegistrationInformation-CreatedTimestamp"></a>
The time when the registration was created, in [UNIX epoch time](https://www.epochconverter.com/) format.
Type: Timestamp
Required: Yes

 ** CurrentVersionNumber **   <a name="pinpoint-Type-RegistrationInformation-CurrentVersionNumber"></a>
The current version number of the registration.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 100000.
Required: Yes

 ** RegistrationArn **   <a name="pinpoint-Type-RegistrationInformation-RegistrationArn"></a>
The Amazon Resource Name (ARN) for the registration.
Type: String
Required: Yes

 ** RegistrationId **   <a name="pinpoint-Type-RegistrationInformation-RegistrationId"></a>
The unique identifier for the registration.
Type: String
Required: Yes

 ** RegistrationStatus **   <a name="pinpoint-Type-RegistrationInformation-RegistrationStatus"></a>
The status of the registration.
+  `CLOSED`: The phone number or sender ID has been deleted and you must also delete the registration for the number.
+  `CREATED`: Your registration is created but not submitted.
+  `COMPLETE`: Your registration has been approved and your origination identity has been created.
+  `DELETED`: The registration has been deleted.
+  `PROVISIONING`: Your registration has been approved and your origination identity is being created.
+  `REQUIRES_AUTHENTICATION`: You need to complete email authentication.
+  `REQUIRES_UPDATES`: You must fix your registration and resubmit it.
+  `REVIEWING`: Your registration has been accepted and is being reviewed.
+  `SUBMITTED`: Your registration has been submitted and is awaiting review.
Type: String
Valid Values: `CREATED | SUBMITTED | AWS_REVIEWING | REVIEWING | REQUIRES_AUTHENTICATION | PROVISIONING | COMPLETE | REQUIRES_UPDATES | CLOSED | DELETED`
Required: Yes

 ** RegistrationType **   <a name="pinpoint-Type-RegistrationInformation-RegistrationType"></a>
The type of registration form. The list of **RegistrationTypes** can be found using the [DescribeRegistrationTypeDefinitions](API_DescribeRegistrationTypeDefinitions.md) action.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_]+`
Required: Yes

 ** AdditionalAttributes **   <a name="pinpoint-Type-RegistrationInformation-AdditionalAttributes"></a>
Metadata about a given registration which is specific to that registration type.
Type: String to string map
Required: No

 ** ApprovedVersionNumber **   <a name="pinpoint-Type-RegistrationInformation-ApprovedVersionNumber"></a>
The version number of the registration that was approved.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 100000.
Required: No

 ** LatestDeniedVersionNumber **   <a name="pinpoint-Type-RegistrationInformation-LatestDeniedVersionNumber"></a>
The latest version number of the registration that was denied.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 100000.
Required: No

## See Also
<a name="API_RegistrationInformation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/RegistrationInformation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/RegistrationInformation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/RegistrationInformation)
