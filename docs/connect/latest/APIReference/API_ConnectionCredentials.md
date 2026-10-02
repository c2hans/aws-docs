---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ConnectionCredentials.html
---

# ConnectionCredentials
<a name="API_ConnectionCredentials"></a>

The credentials that a chat participant uses to connect to the Connect Customer Participant Service.

## Contents
<a name="API_ConnectionCredentials_Contents"></a>

 ** ConnectionToken **   <a name="connect-Type-ConnectionCredentials-ConnectionToken"></a>
The connection token used by the chat participant to call the Connect Customer Participant Service.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: No

 ** Expiry **   <a name="connect-Type-ConnectionCredentials-Expiry"></a>
The expiration of the token. It's specified in ISO 8601 format: yyyy-MM-ddThh:mm:ss.SSSZ. For example, 2019-11-08T02:41:28.172Z.
Type: String
Required: No

## See Also
<a name="API_ConnectionCredentials_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ConnectionCredentials)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ConnectionCredentials)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ConnectionCredentials)
