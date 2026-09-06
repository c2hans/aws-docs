---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_CreateAttendeeRequestItem.html
---

# CreateAttendeeRequestItem
<a name="API_meeting-chime_CreateAttendeeRequestItem"></a>

The Amazon Chime SDK attendee fields to create, used with the BatchCreateAttendee action.

## Contents
<a name="API_meeting-chime_CreateAttendeeRequestItem_Contents"></a>

 ** ExternalUserId **   <a name="chimesdk-Type-meeting-chime_CreateAttendeeRequestItem-ExternalUserId"></a>
The Amazon Chime SDK external user ID. An idempotency token. Links the attendee to an identity managed by a builder application.
Pattern: `[-_&@+=,(){}\[\]\/«».:|'"#a-zA-Z0-9À-ÿ\s]*`
Values that begin with `aws:` are reserved. You can't configure a value that uses this prefix. Case insensitive.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 64.
Required: Yes

 ** Capabilities **   <a name="chimesdk-Type-meeting-chime_CreateAttendeeRequestItem-Capabilities"></a>
A list of one or more capabilities.
Type: [AttendeeCapabilities](API_meeting-chime_AttendeeCapabilities.md) object
Required: No

## See Also
<a name="API_meeting-chime_CreateAttendeeRequestItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-meetings-2021-07-15/CreateAttendeeRequestItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-meetings-2021-07-15/CreateAttendeeRequestItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-meetings-2021-07-15/CreateAttendeeRequestItem)
