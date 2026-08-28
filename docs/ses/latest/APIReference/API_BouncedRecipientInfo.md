---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference/API_BouncedRecipientInfo.html
---

# BouncedRecipientInfo
<a name="API_BouncedRecipientInfo"></a>

Recipient-related information to include in the Delivery Status Notification (DSN) when an email that Amazon SES receives on your behalf bounces.

For information about receiving email through Amazon SES, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/dg/receiving-email.html).

## Contents
<a name="API_BouncedRecipientInfo_Contents"></a>

 ** Recipient **
The email address of the recipient of the bounced email.
Type: String
Required: Yes

 ** BounceType **
The reason for the bounce. You must provide either this parameter or `RecipientDsnFields`.
Type: String
Valid Values: `DoesNotExist | MessageTooLarge | ExceededQuota | ContentRejected | Undefined | TemporaryFailure`
Required: No

 ** RecipientArn **
This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to receive email for the recipient of the bounced email. For more information about sending authorization, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/dg/sending-authorization.html).
Type: String
Required: No

 ** RecipientDsnFields **
Recipient-related DSN fields, most of which would normally be filled in automatically when provided with a `BounceType`. You must provide either this parameter or `BounceType`.
Type: [RecipientDsnFields](API_RecipientDsnFields.md) object
Required: No

## See Also
<a name="API_BouncedRecipientInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/email-2010-12-01/BouncedRecipientInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/email-2010-12-01/BouncedRecipientInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/email-2010-12-01/BouncedRecipientInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ses` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
