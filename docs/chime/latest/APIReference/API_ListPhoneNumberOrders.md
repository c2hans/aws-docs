---
source_url: https://docs.aws.amazon.com/chime/latest/APIReference/API_ListPhoneNumberOrders.html
---

**End of support notice**: On February 20, 2026, AWS will end support for the Amazon Chime service. After February 20, 2026, you will no longer be able to access the Amazon Chime console or Amazon Chime application resources. For more information, visit the [blog post](https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/). **Note:** This does not impact the availability of the [Amazon Chime SDK service](https://aws.amazon.com/chime/chime-sdk/).

# ListPhoneNumberOrders
<a name="API_ListPhoneNumberOrders"></a>

Lists the phone number orders for the administrator's Amazon Chime account.

## Request Syntax
<a name="API_ListPhoneNumberOrders_RequestSyntax"></a>

```
GET /phone-number-orders?max-results={{MaxResults}}&next-token={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListPhoneNumberOrders_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_ListPhoneNumberOrders_RequestSyntax) **   <a name="chime-ListPhoneNumberOrders-request-uri-MaxResults"></a>
The maximum number of results to return in a single call.
Valid Range: Minimum value of 1. Maximum value of 99.

 ** [NextToken](#API_ListPhoneNumberOrders_RequestSyntax) **   <a name="chime-ListPhoneNumberOrders-request-uri-NextToken"></a>
The token to use to retrieve the next page of results.

## Request Body
<a name="API_ListPhoneNumberOrders_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListPhoneNumberOrders_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "PhoneNumberOrders": [
      {
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
   ]
}
```

## Response Elements
<a name="API_ListPhoneNumberOrders_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListPhoneNumberOrders_ResponseSyntax) **   <a name="chime-ListPhoneNumberOrders-response-NextToken"></a>
The token to use to retrieve the next page of results.
Type: String

 ** [PhoneNumberOrders](#API_ListPhoneNumberOrders_ResponseSyntax) **   <a name="chime-ListPhoneNumberOrders-response-PhoneNumberOrders"></a>
The phone number order details.
Type: Array of [PhoneNumberOrder](API_PhoneNumberOrder.md) objects

## Errors
<a name="API_ListPhoneNumberOrders_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
The input parameters don't match the service's restrictions.
HTTP Status Code: 400

 ** ForbiddenException **
The client is permanently forbidden from making the request.
HTTP Status Code: 403

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
<a name="API_ListPhoneNumberOrders_Examples"></a>

In the following example or examples, the Authorization header contents( `AUTHPARAMS` ) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the *AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_ListPhoneNumberOrders_Example_1"></a>

This example lists the phone number orders for the administrator's Amazon Chime account.

#### Sample Request
<a name="API_ListPhoneNumberOrders_Example_1_Request"></a>

```
GET /phone-number-orders HTTP/1.1 Host: service.chime.aws.amazon.com Accept-Encoding: identity User-Agent: aws-cli/1.16.170 Python/3.6.0 Windows/10 botocore/1.12.160 X-Amz-Date: 20190918T175325Z Authorization: AUTHPARAMS
```

#### Sample Response
<a name="API_ListPhoneNumberOrders_Example_1_Response"></a>

```
HTTP/1.1 200 OK x-amzn-RequestId: 6e79c3b2-a0e4-443e-a280-9057b0edd4e8 Content-Type: application/json Content-Length: 770 Date: Wed, 18 Sep 2019 17:53:26 GMT Connection: keep-alive {"NextToken":null,"PhoneNumberOrders":[{"CreatedTimestamp":"2019-08-12T22:10:20.504Z","OrderedPhoneNumbers":[{"E164PhoneNumber":"+12065550100","Status":"Acquired"},{"E164PhoneNumber":"+12065550101","Status":"Acquired"}],"PhoneNumberOrderId":"abc12345-de67-89f0-123g-h45i678j9012","ProductType":"Voice Connector","Status":"Successful","UpdatedTimestamp":"2019-08-12T22:10:31.186Z"}]}
```

## See Also
<a name="API_ListPhoneNumberOrders_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-2018-05-01/ListPhoneNumberOrders)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-2018-05-01/ListPhoneNumberOrders)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-2018-05-01/ListPhoneNumberOrders)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-2018-05-01/ListPhoneNumberOrders)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-2018-05-01/ListPhoneNumberOrders)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-2018-05-01/ListPhoneNumberOrders)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-2018-05-01/ListPhoneNumberOrders)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-2018-05-01/ListPhoneNumberOrders)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/chime-2018-05-01/ListPhoneNumberOrders)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-2018-05-01/ListPhoneNumberOrders)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
