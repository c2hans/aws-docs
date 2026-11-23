---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_PutAccountDeliveryAttributes.html
---

# PutAccountDeliveryAttributes

Set the shared pool delivery mode for your Amazon SES account in the current AWS Region. The mode controls whether Amazon SES can deliver your email from shared IP addresses in other AWS Regions within the same AWS partition.

A change may take a few minutes to take effect. Messages that are already queued for delivery keep the mode that they were sent with.

## Request Syntax
<a name="API_PutAccountDeliveryAttributes_RequestSyntax"></a>

```
POST /v2/email/account/delivery HTTP/1.1
Content-type: application/json

{
   "SharedPoolDeliveryMode": "{{string}}"
}
```

## URI Request Parameters
<a name="API_PutAccountDeliveryAttributes_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_PutAccountDeliveryAttributes_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [SharedPoolDeliveryMode](#API_PutAccountDeliveryAttributes_RequestSyntax) **   <a name="SES-PutAccountDeliveryAttributes-request-SharedPoolDeliveryMode"></a>
The shared pool delivery mode for your Amazon SES account in the current AWS Region. This mode applies to email that you send from shared IP addresses. Can be one of the following:
+  `GLOBAL` – Amazon SES delivers from your sending Region first and, when it improves your deliverability, also uses Amazon SES shared IP addresses with established sending history in other AWS Regions within the same AWS partition.
+  `REGIONAL` – Amazon SES delivers your email only from shared IP addresses in your sending Region.
Type: String
Valid Values: `GLOBAL | REGIONAL`
Required: Yes

## Response Syntax
<a name="API_PutAccountDeliveryAttributes_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_PutAccountDeliveryAttributes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_PutAccountDeliveryAttributes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
The input you provided is invalid.
HTTP Status Code: 400

 ** TooManyRequestsException **
Too many requests have been made to the operation.
HTTP Status Code: 429

## See Also
<a name="API_PutAccountDeliveryAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sesv2-2019-09-27/PutAccountDeliveryAttributes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sesv2-2019-09-27/PutAccountDeliveryAttributes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/PutAccountDeliveryAttributes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sesv2-2019-09-27/PutAccountDeliveryAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/PutAccountDeliveryAttributes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sesv2-2019-09-27/PutAccountDeliveryAttributes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sesv2-2019-09-27/PutAccountDeliveryAttributes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sesv2-2019-09-27/PutAccountDeliveryAttributes)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sesv2-2019-09-27/PutAccountDeliveryAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/PutAccountDeliveryAttributes)
