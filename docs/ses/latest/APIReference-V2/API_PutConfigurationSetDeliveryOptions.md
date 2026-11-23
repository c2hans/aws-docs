---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_PutConfigurationSetDeliveryOptions.html
---

# PutConfigurationSetDeliveryOptions

Associate a configuration set with a dedicated IP pool. You can use dedicated IP pools to create groups of dedicated IP addresses for sending specific types of email.

## Request Syntax
<a name="API_PutConfigurationSetDeliveryOptions_RequestSyntax"></a>

```
PUT /v2/email/configuration-sets/{{ConfigurationSetName}}/delivery-options HTTP/1.1
Content-type: application/json

{
   "MaxDeliverySeconds": {{number}},
   "SendingPoolName": "{{string}}",
   "SharedPoolDeliveryMode": "{{string}}",
   "TlsPolicy": "{{string}}"
}
```

## URI Request Parameters
<a name="API_PutConfigurationSetDeliveryOptions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ConfigurationSetName](#API_PutConfigurationSetDeliveryOptions_RequestSyntax) **   <a name="SES-PutConfigurationSetDeliveryOptions-request-uri-ConfigurationSetName"></a>
The name of the configuration set to associate with a dedicated IP pool.
Required: Yes

## Request Body
<a name="API_PutConfigurationSetDeliveryOptions_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [MaxDeliverySeconds](#API_PutConfigurationSetDeliveryOptions_RequestSyntax) **   <a name="SES-PutConfigurationSetDeliveryOptions-request-MaxDeliverySeconds"></a>
The maximum amount of time, in seconds, that Amazon SES API v2 will attempt delivery of email. If specified, the value must greater than or equal to 300 seconds (5 minutes) and less than or equal to 50400 seconds (840 minutes).
Type: Long
Valid Range: Minimum value of 300. Maximum value of 50400.
Required: No

 ** [SendingPoolName](#API_PutConfigurationSetDeliveryOptions_RequestSyntax) **   <a name="SES-PutConfigurationSetDeliveryOptions-request-SendingPoolName"></a>
The name of the dedicated IP pool to associate with the configuration set.
Type: String
Required: No

 ** [SharedPoolDeliveryMode](#API_PutConfigurationSetDeliveryOptions_RequestSyntax) **   <a name="SES-PutConfigurationSetDeliveryOptions-request-SharedPoolDeliveryMode"></a>
The shared pool delivery mode for email that you send with the configuration set from shared IP addresses. This setting overrides the shared pool delivery mode of your account. Can be one of the following:
+  `GLOBAL` – Amazon SES delivers from your sending Region first and, when it improves your deliverability, also uses Amazon SES shared IP addresses with established sending history in other AWS Regions within the same AWS partition.
+  `REGIONAL` – Amazon SES delivers your email only from shared IP addresses in your sending Region.
+  `ACCOUNT` – The configuration set uses the shared pool delivery mode of your account.
If you don't specify a value, the current value doesn't change.
Type: String
Valid Values: `GLOBAL | REGIONAL | ACCOUNT`
Required: No

 ** [TlsPolicy](#API_PutConfigurationSetDeliveryOptions_RequestSyntax) **   <a name="SES-PutConfigurationSetDeliveryOptions-request-TlsPolicy"></a>
Specifies whether messages that use the configuration set are required to use Transport Layer Security (TLS). If the value is `REQUIRE`, messages are only delivered if a TLS connection can be established. If the value is `OPTIONAL`, messages can be delivered in plain text if a TLS connection can't be established.
Type: String
Valid Values: `REQUIRE | OPTIONAL`
Required: No

## Response Syntax
<a name="API_PutConfigurationSetDeliveryOptions_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_PutConfigurationSetDeliveryOptions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_PutConfigurationSetDeliveryOptions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
The input you provided is invalid.
HTTP Status Code: 400

 ** NotFoundException **
The resource you attempted to access doesn't exist.
HTTP Status Code: 404

 ** TooManyRequestsException **
Too many requests have been made to the operation.
HTTP Status Code: 429

## See Also
<a name="API_PutConfigurationSetDeliveryOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sesv2-2019-09-27/PutConfigurationSetDeliveryOptions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sesv2-2019-09-27/PutConfigurationSetDeliveryOptions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/PutConfigurationSetDeliveryOptions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sesv2-2019-09-27/PutConfigurationSetDeliveryOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/PutConfigurationSetDeliveryOptions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sesv2-2019-09-27/PutConfigurationSetDeliveryOptions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sesv2-2019-09-27/PutConfigurationSetDeliveryOptions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sesv2-2019-09-27/PutConfigurationSetDeliveryOptions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sesv2-2019-09-27/PutConfigurationSetDeliveryOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/PutConfigurationSetDeliveryOptions)
