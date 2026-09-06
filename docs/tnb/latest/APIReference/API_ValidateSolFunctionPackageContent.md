---
source_url: https://docs.aws.amazon.com/tnb/latest/APIReference/API_ValidateSolFunctionPackageContent.html
---

# ValidateSolFunctionPackageContent
<a name="API_ValidateSolFunctionPackageContent"></a>

Validates function package content. This can be used as a dry run before uploading function package content with [PutSolFunctionPackageContent](https://docs.aws.amazon.com/tnb/latest/APIReference/API_PutSolFunctionPackageContent.html).

A function package is a .zip file in CSAR (Cloud Service Archive) format that contains a network function (an ETSI standard telecommunication application) and function package descriptor that uses the TOSCA standard to describe how the network functions should run on your network.

## Request Syntax
<a name="API_ValidateSolFunctionPackageContent_RequestSyntax"></a>

```
PUT /sol/vnfpkgm/v1/vnf_packages/{{vnfPkgId}}/package_content/validate HTTP/1.1
Content-Type: {{contentType}}

{{file}}
```

## URI Request Parameters
<a name="API_ValidateSolFunctionPackageContent_RequestParameters"></a>

The request uses the following URI parameters.

 ** [contentType](#API_ValidateSolFunctionPackageContent_RequestSyntax) **   <a name="TNB-ValidateSolFunctionPackageContent-request-contentType"></a>
Function package content type.
Valid Values: `application/zip`

 ** [vnfPkgId](#API_ValidateSolFunctionPackageContent_RequestSyntax) **   <a name="TNB-ValidateSolFunctionPackageContent-request-uri-vnfPkgId"></a>
Function package ID.
Pattern: `fp-[a-f0-9]{17}`
Required: Yes

## Request Body
<a name="API_ValidateSolFunctionPackageContent_RequestBody"></a>

The request accepts the following binary data.

 ** [file](#API_ValidateSolFunctionPackageContent_RequestSyntax) **   <a name="TNB-ValidateSolFunctionPackageContent-request-file"></a>
Function package file.
Required: Yes

## Response Syntax
<a name="API_ValidateSolFunctionPackageContent_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "id": "string",
   "metadata": {
      "vnfd": {
         "overrides": [
            {
               "defaultValue": "string",
               "name": "string"
            }
         ]
      }
   },
   "vnfdId": "string",
   "vnfdVersion": "string",
   "vnfProductName": "string",
   "vnfProvider": "string"
}
```

## Response Elements
<a name="API_ValidateSolFunctionPackageContent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [id](#API_ValidateSolFunctionPackageContent_ResponseSyntax) **   <a name="TNB-ValidateSolFunctionPackageContent-response-id"></a>
Function package ID.
Type: String
Pattern: `fp-[a-f0-9]{17}`

 ** [metadata](#API_ValidateSolFunctionPackageContent_ResponseSyntax) **   <a name="TNB-ValidateSolFunctionPackageContent-response-metadata"></a>
Function package metadata.
Type: [ValidateSolFunctionPackageContentMetadata](API_ValidateSolFunctionPackageContentMetadata.md) object

 ** [vnfdId](#API_ValidateSolFunctionPackageContent_ResponseSyntax) **   <a name="TNB-ValidateSolFunctionPackageContent-response-vnfdId"></a>
Function package descriptor ID.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

 ** [vnfdVersion](#API_ValidateSolFunctionPackageContent_ResponseSyntax) **   <a name="TNB-ValidateSolFunctionPackageContent-response-vnfdVersion"></a>
Function package descriptor version.
Type: String

 ** [vnfProductName](#API_ValidateSolFunctionPackageContent_ResponseSyntax) **   <a name="TNB-ValidateSolFunctionPackageContent-response-vnfProductName"></a>
Network function product name.
Type: String

 ** [vnfProvider](#API_ValidateSolFunctionPackageContent_ResponseSyntax) **   <a name="TNB-ValidateSolFunctionPackageContent-response-vnfProvider"></a>
Network function provider.
Type: String

## Errors
<a name="API_ValidateSolFunctionPackageContent_Errors"></a>

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
<a name="API_ValidateSolFunctionPackageContent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/tnb-2008-10-21/ValidateSolFunctionPackageContent)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/tnb-2008-10-21/ValidateSolFunctionPackageContent)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/tnb-2008-10-21/ValidateSolFunctionPackageContent)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/tnb-2008-10-21/ValidateSolFunctionPackageContent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/tnb-2008-10-21/ValidateSolFunctionPackageContent)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/tnb-2008-10-21/ValidateSolFunctionPackageContent)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/tnb-2008-10-21/ValidateSolFunctionPackageContent)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/tnb-2008-10-21/ValidateSolFunctionPackageContent)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/tnb-2008-10-21/ValidateSolFunctionPackageContent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/tnb-2008-10-21/ValidateSolFunctionPackageContent)
