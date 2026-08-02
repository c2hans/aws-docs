---
source_url: https://docs.aws.amazon.com/chime/latest/APIReference/API_UserError.html
---

**End of support notice**: On February 20, 2026, AWS will end support for the Amazon Chime service. After February 20, 2026, you will no longer be able to access the Amazon Chime console or Amazon Chime application resources. For more information, visit the [blog post](https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/). **Note:** This does not impact the availability of the [Amazon Chime SDK service](https://aws.amazon.com/chime/chime-sdk/).

# UserError
<a name="API_UserError"></a>

The list of errors returned when errors are encountered during the [BatchSuspendUser](API_BatchSuspendUser.md), [BatchUnsuspendUser](API_BatchUnsuspendUser.md), or [BatchUpdateUser](API_BatchUpdateUser.md) actions. This includes user IDs, error codes, and error messages.

## Contents
<a name="API_UserError_Contents"></a>

 ** ErrorCode **   <a name="chime-Type-UserError-ErrorCode"></a>
The error code.
Type: String
Valid Values: `BadRequest | Conflict | Forbidden | NotFound | PreconditionFailed | ResourceLimitExceeded | ServiceFailure | AccessDenied | ServiceUnavailable | Throttled | Throttling | Unauthorized | Unprocessable | VoiceConnectorGroupAssociationsExist | PhoneNumberAssociationsExist`
Required: No

 ** ErrorMessage **   <a name="chime-Type-UserError-ErrorMessage"></a>
The error message.
Type: String
Required: No

 ** UserId **   <a name="chime-Type-UserError-UserId"></a>
The user ID for which the action failed.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_UserError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-2018-05-01/UserError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-2018-05-01/UserError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-2018-05-01/UserError)
