---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_PhoneNumberError.html
---

# PhoneNumberError
<a name="API_voice-chime_PhoneNumberError"></a>

If a phone number action fails for one or more of the phone numbers in a request, a list of the failed phone numbers is returned, along with error codes and error messages.

## Contents
<a name="API_voice-chime_PhoneNumberError_Contents"></a>

 ** ErrorCode **   <a name="chimesdk-Type-voice-chime_PhoneNumberError-ErrorCode"></a>
The error code.
Type: String
Valid Values: `BadRequest | Conflict | Forbidden | NotFound | PreconditionFailed | ResourceLimitExceeded | ServiceFailure | AccessDenied | ServiceUnavailable | Throttled | Throttling | Unauthorized | Unprocessable | VoiceConnectorGroupAssociationsExist | PhoneNumberAssociationsExist | Gone`
Required: No

 ** ErrorMessage **   <a name="chimesdk-Type-voice-chime_PhoneNumberError-ErrorMessage"></a>
The error message.
Type: String
Required: No

 ** PhoneNumberId **   <a name="chimesdk-Type-voice-chime_PhoneNumberError-PhoneNumberId"></a>
The phone number ID for which the action failed.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_voice-chime_PhoneNumberError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-voice-2022-08-03/PhoneNumberError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-voice-2022-08-03/PhoneNumberError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-voice-2022-08-03/PhoneNumberError)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
