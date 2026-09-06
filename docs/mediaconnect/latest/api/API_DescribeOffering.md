---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_DescribeOffering.html
---

# DescribeOffering
<a name="API_DescribeOffering"></a>

 Displays the details of an offering. The response includes the offering description, duration, outbound bandwidth, price, and Amazon Resource Name (ARN).

## Request Syntax
<a name="API_DescribeOffering_RequestSyntax"></a>

```
GET /v1/offerings/{{offeringArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeOffering_RequestParameters"></a>

The request uses the following URI parameters.

 ** [offeringArn](#API_DescribeOffering_RequestSyntax) **   <a name="mediaconnect-DescribeOffering-request-uri-offeringArn"></a>
 The ARN of the offering.
Required: Yes

## Request Body
<a name="API_DescribeOffering_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeOffering_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "offering": {
      "currencyCode": "string",
      "duration": number,
      "durationUnits": "string",
      "offeringArn": "string",
      "offeringDescription": "string",
      "pricePerUnit": "string",
      "priceUnits": "string",
      "resourceSpecification": {
         "reservedBitrate": number,
         "resourceType": "string"
      }
   }
}
```

## Response Elements
<a name="API_DescribeOffering_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [offering](#API_DescribeOffering_ResponseSyntax) **   <a name="mediaconnect-DescribeOffering-response-offering"></a>
The offering that you requested a description of.
Type: [Offering](API_Offering.md) object

## Errors
<a name="API_DescribeOffering_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message.
HTTP Status Code: 400

 ** InternalServerErrorException **
The server encountered an internal error and is unable to complete the request.
HTTP Status Code: 500

 ** NotFoundException **
One or more of the resources in the request does not exist in the system.
HTTP Status Code: 404

 ** ServiceUnavailableException **
The service is currently unavailable or busy.
HTTP Status Code: 503

 ** TooManyRequestsException **
The request was denied due to request throttling.
HTTP Status Code: 429

## See Also
<a name="API_DescribeOffering_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mediaconnect-2018-11-14/DescribeOffering)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mediaconnect-2018-11-14/DescribeOffering)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/DescribeOffering)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mediaconnect-2018-11-14/DescribeOffering)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/DescribeOffering)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mediaconnect-2018-11-14/DescribeOffering)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mediaconnect-2018-11-14/DescribeOffering)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mediaconnect-2018-11-14/DescribeOffering)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mediaconnect-2018-11-14/DescribeOffering)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/DescribeOffering)
