---
source_url: https://docs.aws.amazon.com/chime/latest/APIReference/API_CreatePhoneNumberOrder.html
---

**End of support notice**: On February 20, 2026, AWS will end support for the Amazon Chime service. After February 20, 2026, you will no longer be able to access the Amazon Chime console or Amazon Chime application resources. For more information, visit the [blog post](https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/). **Note:** This does not impact the availability of the [Amazon Chime SDK service](https://aws.amazon.com/chime/chime-sdk/).

# CreatePhoneNumberOrder
<a name="API_CreatePhoneNumberOrder"></a>

Creates an order for phone numbers to be provisioned. For toll-free numbers, you cannot use the Amazon Chime Business Calling product type. For numbers outside the U.S., you must use the Amazon Chime SIP Media Application Dial-In product type.

## Request Syntax
<a name="API_CreatePhoneNumberOrder_RequestSyntax"></a>

```
POST /phone-number-orders HTTP/1.1
Content-type: application/json

{
   "E164PhoneNumbers": [ "{{string}}" ],
   "ProductType": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreatePhoneNumberOrder_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreatePhoneNumberOrder_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [E164PhoneNumbers](#API_CreatePhoneNumberOrder_RequestSyntax) **   <a name="chime-CreatePhoneNumberOrder-request-E164PhoneNumbers"></a>
List of phone numbers, in E.164 format.
Type: Array of strings
Pattern: `^\+?[1-9]\d{1,14}$`
Required: Yes

 ** [ProductType](#API_CreatePhoneNumberOrder_RequestSyntax) **   <a name="chime-CreatePhoneNumberOrder-request-ProductType"></a>
The phone number product type.
Type: String
Valid Values: `BusinessCalling | VoiceConnector | SipMediaApplicationDialIn`
Required: Yes

## Response Syntax
<a name="API_CreatePhoneNumberOrder_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "PhoneNumberOrder": {
      "CreatedTimestamp": "string",
      "OrderedPhoneNumbers": [
         {
            "E164PhoneNumber": "string",
            "Status": "string"
         }
      ],
      "PhoneNumberOrderId": "string",
      "ProductType": "string",
      "Status": "string",
      "UpdatedTimestamp": "string"
   }
}
```

## Response Elements
<a name="API_CreatePhoneNumberOrder_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [PhoneNumberOrder](#API_CreatePhoneNumberOrder_ResponseSyntax) **   <a name="chime-CreatePhoneNumberOrder-response-PhoneNumberOrder"></a>
The phone number order details.
Type: [PhoneNumberOrder](API_PhoneNumberOrder.md) object

## Errors
<a name="API_CreatePhoneNumberOrder_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permissions to perform the requested operation.
HTTP Status Code: 403

 ** BadRequestException **
The input parameters don't match the service's restrictions.
HTTP Status Code: 400

 ** ForbiddenException **
The client is permanently forbidden from making the request.
HTTP Status Code: 403

 ** ResourceLimitExceededException **
The request exceeds the resource limit.
HTTP Status Code: 400

 ** ServiceFailureException **
The service encountered an unexpected error.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The service is currently unavailable.
HTTP Status Code: 503

 ** ThrottledClientException **
The client exceeded its request rate limit.
HTTP Status Code: 429

 ** UnauthorizedClientException **
The client is not currently authorized to make the request.
HTTP Status Code: 401

## Examples
<a name="API_CreatePhoneNumberOrder_Examples"></a>

In the following example or examples, the Authorization header contents( `AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the *AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_CreatePhoneNumberOrder_Example_1"></a>

This example creates an order for phone numbers to be provisioned.

#### Sample Request
<a name="API_CreatePhoneNumberOrder_Example_1_Request"></a>

```
POST /phone-number-orders HTTP/1.1 Host: service.chime.aws.amazon.com Accept-Encoding: identity User-Agent: aws-cli/1.16.170 Python/3.6.0 Windows/10 botocore/1.12.160 X-Amz-Date: 20190918T175735Z Authorization: AUTHPARAMS Content-Length: 88 {"ProductType": "BusinessCalling", "E164PhoneNumbers": ["+12065550100", "+12065550101"]}
```

#### Sample Response
<a name="API_CreatePhoneNumberOrder_Example_1_Response"></a>

```
HTTP/1.1 201 Created x-amzn-RequestId: 7ac7b213-6e5d-4b2a-a142-ce9a7bb7e455 Content-Type: application/json Content-Length: 366 Date: Wed, 18 Sep 2019 17:57:43 GMT Connection: keep-alive {"PhoneNumberOrder":{"CreatedTimestamp":"2019-09-18T17:57:36.280Z","OrderedPhoneNumbers":[{"E164PhoneNumber":"+12065550100","Status":"Processing"},{"E164PhoneNumber":"+12065550101","Status":"Processing"}],"PhoneNumberOrderId":"abc12345-de67-89f0-123g-h45i678j9012","ProductType":"BusinessCalling","Status":"Processing","UpdatedTimestamp":"2019-09-18T17:57:43.110Z"}}
```

## See Also
<a name="API_CreatePhoneNumberOrder_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-2018-05-01/CreatePhoneNumberOrder)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-2018-05-01/CreatePhoneNumberOrder)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-2018-05-01/CreatePhoneNumberOrder)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-2018-05-01/CreatePhoneNumberOrder)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-2018-05-01/CreatePhoneNumberOrder)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-2018-05-01/CreatePhoneNumberOrder)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-2018-05-01/CreatePhoneNumberOrder)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-2018-05-01/CreatePhoneNumberOrder)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/chime-2018-05-01/CreatePhoneNumberOrder)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-2018-05-01/CreatePhoneNumberOrder)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
