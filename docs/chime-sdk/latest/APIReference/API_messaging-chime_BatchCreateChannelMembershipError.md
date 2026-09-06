---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_BatchCreateChannelMembershipError.html
---

# BatchCreateChannelMembershipError
<a name="API_messaging-chime_BatchCreateChannelMembershipError"></a>

A list of failed member ARNs, error codes, and error messages.

## Contents
<a name="API_messaging-chime_BatchCreateChannelMembershipError_Contents"></a>

 ** ErrorCode **   <a name="chimesdk-Type-messaging-chime_BatchCreateChannelMembershipError-ErrorCode"></a>
The error code.
Type: String
Valid Values: `BadRequest | Conflict | Forbidden | NotFound | PreconditionFailed | ResourceLimitExceeded | ServiceFailure | AccessDenied | ServiceUnavailable | Throttled | Throttling | Unauthorized | Unprocessable | VoiceConnectorGroupAssociationsExist | PhoneNumberAssociationsExist`
Required: No

 ** ErrorMessage **   <a name="chimesdk-Type-messaging-chime_BatchCreateChannelMembershipError-ErrorMessage"></a>
The error message.
Type: String
Required: No

 ** MemberArn **   <a name="chimesdk-Type-messaging-chime_BatchCreateChannelMembershipError-MemberArn"></a>
The `AppInstanceUserArn` of the member that the service couldn't add.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 1600.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: No

## See Also
<a name="API_messaging-chime_BatchCreateChannelMembershipError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-messaging-2021-05-15/BatchCreateChannelMembershipError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-messaging-2021-05-15/BatchCreateChannelMembershipError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-messaging-2021-05-15/BatchCreateChannelMembershipError)
