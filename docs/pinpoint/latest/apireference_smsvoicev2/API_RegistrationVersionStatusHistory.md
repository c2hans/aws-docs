---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_RegistrationVersionStatusHistory.html
---

# RegistrationVersionStatusHistory
<a name="API_RegistrationVersionStatusHistory"></a>

The **RegistrationVersionStatusHistory** object contains the time stamps for when the reservations status changes.

## Contents
<a name="API_RegistrationVersionStatusHistory_Contents"></a>

 ** DraftTimestamp **   <a name="pinpoint-Type-RegistrationVersionStatusHistory-DraftTimestamp"></a>
The time when the registration was in the draft state, in [UNIX epoch time](https://www.epochconverter.com/) format.
Type: Timestamp
Required: Yes

 ** ApprovedTimestamp **   <a name="pinpoint-Type-RegistrationVersionStatusHistory-ApprovedTimestamp"></a>
The time when the registration was in the approved state, in [UNIX epoch time](https://www.epochconverter.com/) format.
Type: Timestamp
Required: No

 ** ArchivedTimestamp **   <a name="pinpoint-Type-RegistrationVersionStatusHistory-ArchivedTimestamp"></a>
The time when the registration was in the archived state, in [UNIX epoch time](https://www.epochconverter.com/) format.
Type: Timestamp
Required: No

 ** AwsReviewingTimestamp **   <a name="pinpoint-Type-RegistrationVersionStatusHistory-AwsReviewingTimestamp"></a>
The time when the registration was in the AWS reviewing state, in [UNIX epoch time](https://www.epochconverter.com/) format.
Type: Timestamp
Required: No

 ** DeniedTimestamp **   <a name="pinpoint-Type-RegistrationVersionStatusHistory-DeniedTimestamp"></a>
The time when the registration was in the denied state, in [UNIX epoch time](https://www.epochconverter.com/) format.
Type: Timestamp
Required: No

 ** DiscardedTimestamp **   <a name="pinpoint-Type-RegistrationVersionStatusHistory-DiscardedTimestamp"></a>
The time when the registration was in the discarded state, in [UNIX epoch time](https://www.epochconverter.com/) format.
Type: Timestamp
Required: No

 ** RequiresAuthenticationTimestamp **   <a name="pinpoint-Type-RegistrationVersionStatusHistory-RequiresAuthenticationTimestamp"></a>
The time when the registration was in the requires authentication state, in [UNIX epoch time](https://www.epochconverter.com/) format.
Type: Timestamp
Required: No

 ** ReviewingTimestamp **   <a name="pinpoint-Type-RegistrationVersionStatusHistory-ReviewingTimestamp"></a>
The time when the registration was in the reviewing state, in [UNIX epoch time](https://www.epochconverter.com/) format.
Type: Timestamp
Required: No

 ** RevokedTimestamp **   <a name="pinpoint-Type-RegistrationVersionStatusHistory-RevokedTimestamp"></a>
The time when the registration was in the revoked state, in [UNIX epoch time](https://www.epochconverter.com/) format.
Type: Timestamp
Required: No

 ** SubmittedTimestamp **   <a name="pinpoint-Type-RegistrationVersionStatusHistory-SubmittedTimestamp"></a>
The time when the registration was in the submitted state, in [UNIX epoch time](https://www.epochconverter.com/) format.
Type: Timestamp
Required: No

## See Also
<a name="API_RegistrationVersionStatusHistory_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/RegistrationVersionStatusHistory)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/RegistrationVersionStatusHistory)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/RegistrationVersionStatusHistory)
