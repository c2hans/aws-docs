---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_NullableAdditionalRecipients.html
---

# NullableAdditionalRecipients
<a name="API_NullableAdditionalRecipients"></a>

The additional recipients of an outbound email that you can update. An empty list of `CcEmailAddresses` clears the existing CC recipients.

## Contents
<a name="API_NullableAdditionalRecipients_Contents"></a>

 ** CcEmailAddresses **   <a name="connect-Type-NullableAdditionalRecipients-CcEmailAddresses"></a>
The additional CC email address recipients. You can specify up to 50 addresses. Provide an empty list to clear the existing CC recipients.
Type: Array of [EmailAddressInfo](API_EmailAddressInfo.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## See Also
<a name="API_NullableAdditionalRecipients_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/NullableAdditionalRecipients)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/NullableAdditionalRecipients)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/NullableAdditionalRecipients)
