---
source_url: https://docs.aws.amazon.com/healthimaging/latest/APIReference/API_GetImageFrame.html
---

# GetImageFrame
<a name="API_GetImageFrame"></a>

Get an image frame (pixel data) for an image set.

## Request Syntax
<a name="API_GetImageFrame_RequestSyntax"></a>

```
POST /datastore/{{datastoreId}}/imageSet/{{imageSetId}}/getImageFrame HTTP/1.1
Content-type: application/json

{
   "imageFrameId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetImageFrame_RequestParameters"></a>

The request uses the following URI parameters.

 ** [datastoreId](#API_GetImageFrame_RequestSyntax) **   <a name="healthimaging-GetImageFrame-request-uri-datastoreId"></a>
The data store identifier.
Pattern: `[0-9a-z]{32}`
Required: Yes

 ** [imageSetId](#API_GetImageFrame_RequestSyntax) **   <a name="healthimaging-GetImageFrame-request-uri-imageSetId"></a>
The image set identifier.
Pattern: `[0-9a-z]{32}`
Required: Yes

## Request Body
<a name="API_GetImageFrame_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [imageFrameId](#API_GetImageFrame_RequestSyntax) **   <a name="healthimaging-GetImageFrame-request-imageFrameId"></a>
The image frame (pixel data) identifier.
Type: String
Pattern: `[0-9a-z]{32}`
Required: Yes

## Response Syntax
<a name="API_GetImageFrame_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-Type: {{contentType}}

{{imageFrameBlob}}
```

## Response Elements
<a name="API_GetImageFrame_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The response returns the following HTTP headers.

 ** [contentType](#API_GetImageFrame_ResponseSyntax) **   <a name="healthimaging-GetImageFrame-response-contentType"></a>
The format in which the image frame information is returned to the customer. Default is `application/octet-stream`.
+ If the stored transfer syntax is `1.2.840.10008.1.2.1`, the returned `contentType` is `application/octet-stream`.
+ If the stored transfer syntax is `1.2.840.10008.1.2.4.50`, the returned `contentType` is `image/jpeg`.
+ If the stored transfer syntax is `1.2.840.10008.1.2.4.91`, the returned `contentType` is `image/j2c`.
+ If the stored transfer syntax is MPEG2, `1.2.840.10008.1.2.4.100`, `1.2.840.10008.1.2.4.100.1`, `1.2.840.10008.1.2.4.101`, or `1.2.840.10008.1.2.4.101.1`, the returned `contentType` is `video/mpeg`.
+ If the stored transfer syntax is MPEG-4 AVC/H.264, UID `1.2.840.10008.1.2.4.102`, `1.2.840.10008.1.2.4.102.1`, `1.2.840.10008.1.2.4.103`, `1.2.840.10008.1.2.4.103.1`, `1.2.840.10008.1.2.4.104`, `1.2.840.10008.1.2.4.104.1`, `1.2.840.10008.1.2.4.105`, `1.2.840.10008.1.2.4.105.1`, `1.2.840.10008.1.2.4.106`, or `1.2.840.10008.1.2.4.106.1`, the returned `contentType` is `video/mp4`.
+ If the stored transfer syntax is HEVC/H.265, UID `1.2.840.10008.1.2.4.107` or `1.2.840.10008.1.2.4.108`, the returned `contentType` is `video/H256`.
+ If the stored transfer syntax is `1.2.840.10008.1.2.4.202` or if the stored transfer syntax is *missing*, the returned `contentType` is `image/jph`.
+ If the stored transfer syntax is `1.2.840.10008.1.2.4.203`, the returned contentType is `image/jphc`.
+ If the stored transfer syntax is `1.2.840.10008.1.2.4.112` the returned `contentType` is `image/jxl`.

The response returns the following as the HTTP body.

 ** [imageFrameBlob](#API_GetImageFrame_ResponseSyntax) **   <a name="healthimaging-GetImageFrame-response-imageFrameBlob"></a>
The blob containing the aggregated image frame information.

## Errors
<a name="API_GetImageFrame_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The user does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** BadRequestException **
The request is invalid or malformed.
HTTP Status Code: 400

 ** ConflictException **
Updating or deleting a resource can cause an inconsistent state.
HTTP Status Code: 409

 ** InternalServerException **
An unexpected error occurred during processing of the request.
HTTP Status Code: 500

 ** NotAcceptableException **
The request content type or accept header is not supported.
HTTP Status Code: 406

 ** ResourceNotFoundException **
The request references a resource which does not exist.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints set by the service.
HTTP Status Code: 400

## See Also
<a name="API_GetImageFrame_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/medical-imaging-2023-07-19/GetImageFrame)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/medical-imaging-2023-07-19/GetImageFrame)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/medical-imaging-2023-07-19/GetImageFrame)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/medical-imaging-2023-07-19/GetImageFrame)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/medical-imaging-2023-07-19/GetImageFrame)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/medical-imaging-2023-07-19/GetImageFrame)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/medical-imaging-2023-07-19/GetImageFrame)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/medical-imaging-2023-07-19/GetImageFrame)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/medical-imaging-2023-07-19/GetImageFrame)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/medical-imaging-2023-07-19/GetImageFrame)
