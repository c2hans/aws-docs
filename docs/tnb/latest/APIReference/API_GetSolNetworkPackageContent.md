---
source_url: https://docs.aws.amazon.com/tnb/latest/APIReference/API_GetSolNetworkPackageContent.html
---

# GetSolNetworkPackageContent
<a name="API_GetSolNetworkPackageContent"></a>

Gets the contents of a network package.

A network package is a .zip file in CSAR (Cloud Service Archive) format defines the function packages you want to deploy and the AWS infrastructure you want to deploy them on.

## Request Syntax
<a name="API_GetSolNetworkPackageContent_RequestSyntax"></a>

```
GET /sol/nsd/v1/ns_descriptors/{{nsdInfoId}}/nsd_content HTTP/1.1
Accept: {{accept}}
```

## URI Request Parameters
<a name="API_GetSolNetworkPackageContent_RequestParameters"></a>

The request uses the following URI parameters.

 ** [accept](#API_GetSolNetworkPackageContent_RequestSyntax) **   <a name="TNB-GetSolNetworkPackageContent-request-accept"></a>
The format of the package you want to download from the network package.
Valid Values: `application/zip`
Required: Yes

 ** [nsdInfoId](#API_GetSolNetworkPackageContent_RequestSyntax) **   <a name="TNB-GetSolNetworkPackageContent-request-uri-nsdInfoId"></a>
ID of the network service descriptor in the network package.
Pattern: `np-[a-f0-9]{17}`
Required: Yes

## Request Body
<a name="API_GetSolNetworkPackageContent_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetSolNetworkPackageContent_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-Type: {{contentType}}

{{nsdContent}}
```

## Response Elements
<a name="API_GetSolNetworkPackageContent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The response returns the following HTTP headers.

 ** [contentType](#API_GetSolNetworkPackageContent_ResponseSyntax) **   <a name="TNB-GetSolNetworkPackageContent-response-contentType"></a>
Indicates the media type of the resource.
Valid Values: `application/zip`

The response returns the following as the HTTP body.

 ** [nsdContent](#API_GetSolNetworkPackageContent_ResponseSyntax) **   <a name="TNB-GetSolNetworkPackageContent-response-nsdContent"></a>
Content of the network service descriptor in the network package.

## Errors
<a name="API_GetSolNetworkPackageContent_Errors"></a>

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
<a name="API_GetSolNetworkPackageContent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/tnb-2008-10-21/GetSolNetworkPackageContent)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/tnb-2008-10-21/GetSolNetworkPackageContent)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/tnb-2008-10-21/GetSolNetworkPackageContent)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/tnb-2008-10-21/GetSolNetworkPackageContent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/tnb-2008-10-21/GetSolNetworkPackageContent)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/tnb-2008-10-21/GetSolNetworkPackageContent)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/tnb-2008-10-21/GetSolNetworkPackageContent)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/tnb-2008-10-21/GetSolNetworkPackageContent)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/tnb-2008-10-21/GetSolNetworkPackageContent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/tnb-2008-10-21/GetSolNetworkPackageContent)
