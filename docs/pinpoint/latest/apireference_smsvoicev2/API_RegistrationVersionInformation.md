---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_RegistrationVersionInformation.html
---

# RegistrationVersionInformation
<a name="API_RegistrationVersionInformation"></a>

Provides information about the specified version of the registration.

## Contents
<a name="API_RegistrationVersionInformation_Contents"></a>

 ** RegistrationVersionStatus **   <a name="pinpoint-Type-RegistrationVersionInformation-RegistrationVersionStatus"></a>
The status of the registration.
+  `APPROVED`: Your registration has been approved.
+  `ARCHIVED`: Your previously approved registration version moves into this status when a more recently submitted version is approved.
+  `DENIED`: You must fix your registration and resubmit it.
+  `DISCARDED`: You've abandon this version of their registration to start over with a new version.
+  `DRAFT`: The initial status of a registration version after it’s created.
+  `REQUIRES_AUTHENTICATION`: You need to complete email authentication.
+  `REVIEWING`: Your registration has been accepted and is being reviewed.
+  `REVOKED`: Your previously approved registration has been revoked.
+  `SUBMITTED`: Your registration has been submitted.
Type: String
Valid Values: `DRAFT | SUBMITTED | AWS_REVIEWING | REVIEWING | REQUIRES_AUTHENTICATION | APPROVED | DISCARDED | DENIED | REVOKED | ARCHIVED | REQUIRES_OFFLINE_REVIEW`
Required: Yes

 ** RegistrationVersionStatusHistory **   <a name="pinpoint-Type-RegistrationVersionInformation-RegistrationVersionStatusHistory"></a>
The **RegistrationVersionStatusHistory** object contains the time stamps for when the reservations status changes.
Type: [RegistrationVersionStatusHistory](API_RegistrationVersionStatusHistory.md) object
Required: Yes

 ** VersionNumber **   <a name="pinpoint-Type-RegistrationVersionInformation-VersionNumber"></a>
The version number of the registration.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 100000.
Required: Yes

 ** DeniedReasons **   <a name="pinpoint-Type-RegistrationVersionInformation-DeniedReasons"></a>
An array of RegistrationDeniedReasonInformation objects.
Type: Array of [RegistrationDeniedReasonInformation](API_RegistrationDeniedReasonInformation.md) objects
Required: No

 ** Feedback **   <a name="pinpoint-Type-RegistrationVersionInformation-Feedback"></a>
Generative AI feedback information provided during the registration review process. This includes comments, suggestions, or additional requirements.
Type: String
Required: No

## See Also
<a name="API_RegistrationVersionInformation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/RegistrationVersionInformation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/RegistrationVersionInformation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/RegistrationVersionInformation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging SMS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pinpoint` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
