---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_DescribeFlowSourceThumbnail.html
---

# DescribeFlowSourceThumbnail
<a name="API_DescribeFlowSourceThumbnail"></a>

 Describes the thumbnail for the flow source.

## Request Syntax
<a name="API_DescribeFlowSourceThumbnail_RequestSyntax"></a>

```
GET /v1/flows/{{flowArn}}/source-thumbnail HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeFlowSourceThumbnail_RequestParameters"></a>

The request uses the following URI parameters.

 ** [flowArn](#API_DescribeFlowSourceThumbnail_RequestSyntax) **   <a name="mediaconnect-DescribeFlowSourceThumbnail-request-uri-flowArn"></a>
 The Amazon Resource Name (ARN) of the flow.
Pattern: `arn:(aws[a-zA-Z-]*):mediaconnect:[a-z0-9-]+:[0-9]{12}:flow:[a-zA-Z0-9-]+:[a-zA-Z0-9_-]+`
Required: Yes

## Request Body
<a name="API_DescribeFlowSourceThumbnail_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeFlowSourceThumbnail_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "thumbnailDetails": {
      "flowArn": "string",
      "thumbnail": "string",
      "thumbnailMessages": [
         {
            "code": "string",
            "message": "string",
            "resourceName": "string"
         }
      ],
      "timecode": "string",
      "timestamp": "string"
   }
}
```

## Response Elements
<a name="API_DescribeFlowSourceThumbnail_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [thumbnailDetails](#API_DescribeFlowSourceThumbnail_ResponseSyntax) **   <a name="mediaconnect-DescribeFlowSourceThumbnail-response-thumbnailDetails"></a>
The details of the thumbnail, including thumbnail base64 string, timecode and the time when thumbnail was generated.
Type: [ThumbnailDetails](API_ThumbnailDetails.md) object

## Errors
<a name="API_DescribeFlowSourceThumbnail_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message.
HTTP Status Code: 400

 ** ForbiddenException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

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
<a name="API_DescribeFlowSourceThumbnail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mediaconnect-2018-11-14/DescribeFlowSourceThumbnail)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mediaconnect-2018-11-14/DescribeFlowSourceThumbnail)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/DescribeFlowSourceThumbnail)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mediaconnect-2018-11-14/DescribeFlowSourceThumbnail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/DescribeFlowSourceThumbnail)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mediaconnect-2018-11-14/DescribeFlowSourceThumbnail)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mediaconnect-2018-11-14/DescribeFlowSourceThumbnail)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mediaconnect-2018-11-14/DescribeFlowSourceThumbnail)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/mediaconnect-2018-11-14/DescribeFlowSourceThumbnail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/DescribeFlowSourceThumbnail)
