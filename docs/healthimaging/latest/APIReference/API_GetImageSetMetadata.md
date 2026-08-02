---
source_url: https://docs.aws.amazon.com/healthimaging/latest/APIReference/API_GetImageSetMetadata.html
---

# GetImageSetMetadata
<a name="API_GetImageSetMetadata"></a>

Get metadata attributes for an image set.

## Request Syntax
<a name="API_GetImageSetMetadata_RequestSyntax"></a>

```
POST /datastore/{{datastoreId}}/imageSet/{{imageSetId}}/getImageSetMetadata?version={{versionId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetImageSetMetadata_RequestParameters"></a>

The request uses the following URI parameters.

 ** [datastoreId](#API_GetImageSetMetadata_RequestSyntax) **   <a name="healthimaging-GetImageSetMetadata-request-uri-datastoreId"></a>
The data store identifier.
Pattern: `[0-9a-z]{32}`
Required: Yes

 ** [imageSetId](#API_GetImageSetMetadata_RequestSyntax) **   <a name="healthimaging-GetImageSetMetadata-request-uri-imageSetId"></a>
The image set identifier.
Pattern: `[0-9a-z]{32}`
Required: Yes

 ** [versionId](#API_GetImageSetMetadata_RequestSyntax) **   <a name="healthimaging-GetImageSetMetadata-request-uri-versionId"></a>
The image set version identifier.
Pattern: `\d+`

## Request Body
<a name="API_GetImageSetMetadata_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetImageSetMetadata_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-Type: {{contentType}}
Content-Encoding: {{contentEncoding}}

{{imageSetMetadataBlob}}
```

## Response Elements
<a name="API_GetImageSetMetadata_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The response returns the following HTTP headers.

 ** [contentEncoding](#API_GetImageSetMetadata_ResponseSyntax) **   <a name="healthimaging-GetImageSetMetadata-response-contentEncoding"></a>
The compression format in which image set metadata attributes are returned.

 ** [contentType](#API_GetImageSetMetadata_ResponseSyntax) **   <a name="healthimaging-GetImageSetMetadata-response-contentType"></a>
The format in which the study metadata is returned to the customer. Default is `text/plain`.

The response returns the following as the HTTP body.

 ** [imageSetMetadataBlob](#API_GetImageSetMetadata_ResponseSyntax) **   <a name="healthimaging-GetImageSetMetadata-response-imageSetMetadataBlob"></a>
The blob containing the aggregated metadata information for the image set.

## Errors
<a name="API_GetImageSetMetadata_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The user does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
Updating or deleting a resource can cause an inconsistent state.
HTTP Status Code: 409

 ** InternalServerException **
An unexpected error occurred during processing of the request.
HTTP Status Code: 500

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
<a name="API_GetImageSetMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/medical-imaging-2023-07-19/GetImageSetMetadata)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/medical-imaging-2023-07-19/GetImageSetMetadata)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/medical-imaging-2023-07-19/GetImageSetMetadata)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/medical-imaging-2023-07-19/GetImageSetMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/medical-imaging-2023-07-19/GetImageSetMetadata)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/medical-imaging-2023-07-19/GetImageSetMetadata)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/medical-imaging-2023-07-19/GetImageSetMetadata)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/medical-imaging-2023-07-19/GetImageSetMetadata)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/medical-imaging-2023-07-19/GetImageSetMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/medical-imaging-2023-07-19/GetImageSetMetadata)
