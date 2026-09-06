---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_HttpAction.html
---

# HttpAction
<a name="API_HttpAction"></a>

Send data to an HTTPS endpoint.

## Contents
<a name="API_HttpAction_Contents"></a>

 ** url **   <a name="iot-Type-HttpAction-url"></a>
The endpoint URL. If substitution templates are used in the URL, you must also specify a `confirmationUrl`. If this is a new destination, a new `TopicRuleDestination` is created if possible.
Type: String
Length Constraints: Maximum length of 2000.
Required: Yes

 ** auth **   <a name="iot-Type-HttpAction-auth"></a>
The authentication method to use when sending data to an HTTPS endpoint.
Type: [HttpAuthorization](API_HttpAuthorization.md) object
Required: No

 ** batchConfig **   <a name="iot-Type-HttpAction-batchConfig"></a>
The configuration settings for batching. For more information, see [ Batching HTTP action messages](https://docs.aws.amazon.com/iot/latest/developerguide/http_batching.html).
Type: [BatchConfig](API_BatchConfig.md) object
Required: No

 ** confirmationUrl **   <a name="iot-Type-HttpAction-confirmationUrl"></a>
The URL to which AWS IoT sends a confirmation message. The value of the confirmation URL must be a prefix of the endpoint URL. If you do not specify a confirmation URL AWS IoT uses the endpoint URL as the confirmation URL. If you use substitution templates in the confirmationUrl, you must create and enable topic rule destinations that match each possible value of the substitution template before traffic is allowed to your endpoint URL.
Type: String
Length Constraints: Maximum length of 2000.
Required: No

 ** enableBatching **   <a name="iot-Type-HttpAction-enableBatching"></a>
Whether to process the HTTP action messages into a single request. Value can be true or false.
Type: Boolean
Required: No

 ** headers **   <a name="iot-Type-HttpAction-headers"></a>
The HTTP headers to send with the message data.
Type: Array of [HttpActionHeader](API_HttpActionHeader.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: No

## See Also
<a name="API_HttpAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/HttpAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/HttpAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/HttpAction)
