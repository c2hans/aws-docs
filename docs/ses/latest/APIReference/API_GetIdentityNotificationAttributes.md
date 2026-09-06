---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference/API_GetIdentityNotificationAttributes.html
---

# GetIdentityNotificationAttributes
<a name="API_GetIdentityNotificationAttributes"></a>

Given a list of verified identities (email addresses and/or domains), returns a structure describing identity notification attributes.

This operation is throttled at one request per second and can only get notification attributes for up to 100 identities at a time.

For more information about using notifications with Amazon SES, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/dg/monitor-sending-activity-using-notifications.html).

## Request Parameters
<a name="API_GetIdentityNotificationAttributes_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 **Identities.member.N**
A list of one or more identities. You can specify an identity by using its name or by using its Amazon Resource Name (ARN). Examples: `user@example.com`, `example.com`, `arn:aws:ses:us-east-1:123456789012:identity/example.com`.
Type: Array of strings
Required: Yes

## Response Elements
<a name="API_GetIdentityNotificationAttributes_ResponseElements"></a>

The following element is returned by the service.

 **NotificationAttributes** NotificationAttributes.entry.N.key (key)NotificationAttributes.entry.N.value (value)
A map of Identity to IdentityNotificationAttributes.
Type: String to [IdentityNotificationAttributes](API_IdentityNotificationAttributes.md) object map

## Errors
<a name="API_GetIdentityNotificationAttributes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_GetIdentityNotificationAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/email-2010-12-01/GetIdentityNotificationAttributes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/email-2010-12-01/GetIdentityNotificationAttributes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/email-2010-12-01/GetIdentityNotificationAttributes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/email-2010-12-01/GetIdentityNotificationAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/email-2010-12-01/GetIdentityNotificationAttributes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/email-2010-12-01/GetIdentityNotificationAttributes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/email-2010-12-01/GetIdentityNotificationAttributes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/email-2010-12-01/GetIdentityNotificationAttributes)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/email-2010-12-01/GetIdentityNotificationAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/email-2010-12-01/GetIdentityNotificationAttributes)
