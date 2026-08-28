---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_CreateAttendeeError.html
---

# CreateAttendeeError
<a name="API_meeting-chime_CreateAttendeeError"></a>

The list of errors returned when errors are encountered during the BatchCreateAttendee and CreateAttendee actions. This includes external user IDs, error codes, and error messages.

## Contents
<a name="API_meeting-chime_CreateAttendeeError_Contents"></a>

 ** ErrorCode **   <a name="chimesdk-Type-meeting-chime_CreateAttendeeError-ErrorCode"></a>
The error code.
Type: String
Length Constraints: Maximum length of 4096.
Required: No

 ** ErrorMessage **   <a name="chimesdk-Type-meeting-chime_CreateAttendeeError-ErrorMessage"></a>
The error message.
Type: String
Length Constraints: Maximum length of 4096.
Required: No

 ** ExternalUserId **   <a name="chimesdk-Type-meeting-chime_CreateAttendeeError-ExternalUserId"></a>
The Amazon Chime SDK external user ID. An idempotency token. Links the attendee to an identity managed by a builder application.
Pattern: `[-_&@+=,(){}\[\]\/«».:|'"#a-zA-Z0-9À-ÿ\s]*`
Values that begin with `aws:` are reserved. You can't configure a value that uses this prefix. Case insensitive.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 64.
Required: No

## See Also
<a name="API_meeting-chime_CreateAttendeeError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-meetings-2021-07-15/CreateAttendeeError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-meetings-2021-07-15/CreateAttendeeError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-meetings-2021-07-15/CreateAttendeeError)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
