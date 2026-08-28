---
source_url: https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_PutConfigurationSetDeliveryOptions.html
---

# PutConfigurationSetDeliveryOptions
<a name="API_PutConfigurationSetDeliveryOptions"></a>

Associate a configuration set with a dedicated IP pool. You can use dedicated IP pools to create groups of dedicated IP addresses for sending specific types of email.

## Request Syntax
<a name="API_PutConfigurationSetDeliveryOptions_RequestSyntax"></a>

```
PUT /v1/email/configuration-sets/{{ConfigurationSetName}}/delivery-options HTTP/1.1
Content-type: application/json

{
   "SendingPoolName": "{{string}}",
   "TlsPolicy": "{{string}}"
}
```

## URI Request Parameters
<a name="API_PutConfigurationSetDeliveryOptions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ConfigurationSetName](#API_PutConfigurationSetDeliveryOptions_RequestSyntax) **   <a name="pinpoint-PutConfigurationSetDeliveryOptions-request-uri-ConfigurationSetName"></a>
The name of the configuration set that you want to associate with a dedicated IP pool.
Required: Yes

## Request Body
<a name="API_PutConfigurationSetDeliveryOptions_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [SendingPoolName](#API_PutConfigurationSetDeliveryOptions_RequestSyntax) **   <a name="pinpoint-PutConfigurationSetDeliveryOptions-request-SendingPoolName"></a>
The name of the dedicated IP pool that you want to associate with the configuration set.
Type: String
Required: No

 ** [TlsPolicy](#API_PutConfigurationSetDeliveryOptions_RequestSyntax) **   <a name="pinpoint-PutConfigurationSetDeliveryOptions-request-TlsPolicy"></a>
Specifies whether messages that use the configuration set are required to use Transport Layer Security (TLS). If the value is `Require`, messages are only delivered if a TLS connection can be established. If the value is `Optional`, messages can be delivered in plain text if a TLS connection can't be established.
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
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pinpoint-email-2018-07-26/PutConfigurationSetDeliveryOptions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pinpoint-email-2018-07-26/PutConfigurationSetDeliveryOptions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-email-2018-07-26/PutConfigurationSetDeliveryOptions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pinpoint-email-2018-07-26/PutConfigurationSetDeliveryOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-email-2018-07-26/PutConfigurationSetDeliveryOptions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pinpoint-email-2018-07-26/PutConfigurationSetDeliveryOptions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pinpoint-email-2018-07-26/PutConfigurationSetDeliveryOptions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pinpoint-email-2018-07-26/PutConfigurationSetDeliveryOptions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/pinpoint-email-2018-07-26/PutConfigurationSetDeliveryOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-email-2018-07-26/PutConfigurationSetDeliveryOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Pinpoint Email. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pinpoint-email` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
