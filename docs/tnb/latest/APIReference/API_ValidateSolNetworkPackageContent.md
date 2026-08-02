---
source_url: https://docs.aws.amazon.com/tnb/latest/APIReference/API_ValidateSolNetworkPackageContent.html
---

# ValidateSolNetworkPackageContent
<a name="API_ValidateSolNetworkPackageContent"></a>

Validates network package content. This can be used as a dry run before uploading network package content with [PutSolNetworkPackageContent](https://docs.aws.amazon.com/tnb/latest/APIReference/API_PutSolNetworkPackageContent.html).

A network package is a .zip file in CSAR (Cloud Service Archive) format defines the function packages you want to deploy and the AWS infrastructure you want to deploy them on.

## Request Syntax
<a name="API_ValidateSolNetworkPackageContent_RequestSyntax"></a>

```
PUT /sol/nsd/v1/ns_descriptors/{{nsdInfoId}}/nsd_content/validate HTTP/1.1
Content-Type: {{contentType}}

{{file}}
```

## URI Request Parameters
<a name="API_ValidateSolNetworkPackageContent_RequestParameters"></a>

The request uses the following URI parameters.

 ** [contentType](#API_ValidateSolNetworkPackageContent_RequestSyntax) **   <a name="TNB-ValidateSolNetworkPackageContent-request-contentType"></a>
Network package content type.
Valid Values: `application/zip`

 ** [nsdInfoId](#API_ValidateSolNetworkPackageContent_RequestSyntax) **   <a name="TNB-ValidateSolNetworkPackageContent-request-uri-nsdInfoId"></a>
Network service descriptor file.
Pattern: `np-[a-f0-9]{17}`
Required: Yes

## Request Body
<a name="API_ValidateSolNetworkPackageContent_RequestBody"></a>

The request accepts the following binary data.

 ** [file](#API_ValidateSolNetworkPackageContent_RequestSyntax) **   <a name="TNB-ValidateSolNetworkPackageContent-request-file"></a>
Network package file.
Required: Yes

## Response Syntax
<a name="API_ValidateSolNetworkPackageContent_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "id": "string",
   "metadata": {
      "nsd": {
         "overrides": [
            {
               "defaultValue": "string",
               "name": "string"
            }
         ]
      }
   },
   "nsdId": "string",
   "nsdName": "string",
   "nsdVersion": "string",
   "vnfPkgIds": [ "string" ]
}
```

## Response Elements
<a name="API_ValidateSolNetworkPackageContent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_ValidateSolNetworkPackageContent_ResponseSyntax) **   <a name="TNB-ValidateSolNetworkPackageContent-response-arn"></a>
Network package ARN.
Type: String
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-b|aws-us-gov):tnb:([a-z]{2}(-(gov|isob|iso))?-(east|west|north|south|central){1,2}-[0-9]):\d{12}:(network-package/np-[a-f0-9]{17})`

 ** [id](#API_ValidateSolNetworkPackageContent_ResponseSyntax) **   <a name="TNB-ValidateSolNetworkPackageContent-response-id"></a>
Network package ID.
Type: String
Pattern: `np-[a-f0-9]{17}`

 ** [metadata](#API_ValidateSolNetworkPackageContent_ResponseSyntax) **   <a name="TNB-ValidateSolNetworkPackageContent-response-metadata"></a>
Network package metadata.
Type: [ValidateSolNetworkPackageContentMetadata](API_ValidateSolNetworkPackageContentMetadata.md) object

 ** [nsdId](#API_ValidateSolNetworkPackageContent_ResponseSyntax) **   <a name="TNB-ValidateSolNetworkPackageContent-response-nsdId"></a>
Network service descriptor ID.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

 ** [nsdName](#API_ValidateSolNetworkPackageContent_ResponseSyntax) **   <a name="TNB-ValidateSolNetworkPackageContent-response-nsdName"></a>
Network service descriptor name.
Type: String

 ** [nsdVersion](#API_ValidateSolNetworkPackageContent_ResponseSyntax) **   <a name="TNB-ValidateSolNetworkPackageContent-response-nsdVersion"></a>
Network service descriptor version.
Type: String

 ** [vnfPkgIds](#API_ValidateSolNetworkPackageContent_ResponseSyntax) **   <a name="TNB-ValidateSolNetworkPackageContent-response-vnfPkgIds"></a>
Function package IDs.
Type: Array of strings
Pattern: `fp-[a-f0-9]{17}`

## Errors
<a name="API_ValidateSolNetworkPackageContent_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Insufficient permissions to make request.
HTTP Status Code: 403

 ** InternalServerException **
Unexpected error occurred. Problem on the server.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Request references a resource that doesn't exist.
HTTP Status Code: 404

 ** ThrottlingException **
Exception caused by throttling.
HTTP Status Code: 429

 ** ValidationException **
Unable to process the request because the client provided input failed to satisfy request constraints.
HTTP Status Code: 400

## See Also
<a name="API_ValidateSolNetworkPackageContent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/tnb-2008-10-21/ValidateSolNetworkPackageContent)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/tnb-2008-10-21/ValidateSolNetworkPackageContent)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/tnb-2008-10-21/ValidateSolNetworkPackageContent)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/tnb-2008-10-21/ValidateSolNetworkPackageContent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/tnb-2008-10-21/ValidateSolNetworkPackageContent)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/tnb-2008-10-21/ValidateSolNetworkPackageContent)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/tnb-2008-10-21/ValidateSolNetworkPackageContent)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/tnb-2008-10-21/ValidateSolNetworkPackageContent)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/tnb-2008-10-21/ValidateSolNetworkPackageContent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/tnb-2008-10-21/ValidateSolNetworkPackageContent)
