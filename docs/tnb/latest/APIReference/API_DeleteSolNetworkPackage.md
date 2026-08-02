---
source_url: https://docs.aws.amazon.com/tnb/latest/APIReference/API_DeleteSolNetworkPackage.html
---

# DeleteSolNetworkPackage
<a name="API_DeleteSolNetworkPackage"></a>

Deletes network package.

A network package is a .zip file in CSAR (Cloud Service Archive) format defines the function packages you want to deploy and the AWS infrastructure you want to deploy them on.

To delete a network package, the package must be in a disable state. To disable a network package, see [UpdateSolNetworkPackage](https://docs.aws.amazon.com/tnb/latest/APIReference/API_UpdateSolNetworkPackage.html).

## Request Syntax
<a name="API_DeleteSolNetworkPackage_RequestSyntax"></a>

```
DELETE /sol/nsd/v1/ns_descriptors/{{nsdInfoId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteSolNetworkPackage_RequestParameters"></a>

The request uses the following URI parameters.

 ** [nsdInfoId](#API_DeleteSolNetworkPackage_RequestSyntax) **   <a name="TNB-DeleteSolNetworkPackage-request-uri-nsdInfoId"></a>
ID of the network service descriptor in the network package.
Pattern: `np-[a-f0-9]{17}`
Required: Yes

## Request Body
<a name="API_DeleteSolNetworkPackage_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteSolNetworkPackage_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_DeleteSolNetworkPackage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_DeleteSolNetworkPackage_Errors"></a>

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
<a name="API_DeleteSolNetworkPackage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/tnb-2008-10-21/DeleteSolNetworkPackage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/tnb-2008-10-21/DeleteSolNetworkPackage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/tnb-2008-10-21/DeleteSolNetworkPackage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/tnb-2008-10-21/DeleteSolNetworkPackage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/tnb-2008-10-21/DeleteSolNetworkPackage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/tnb-2008-10-21/DeleteSolNetworkPackage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/tnb-2008-10-21/DeleteSolNetworkPackage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/tnb-2008-10-21/DeleteSolNetworkPackage)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/tnb-2008-10-21/DeleteSolNetworkPackage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/tnb-2008-10-21/DeleteSolNetworkPackage)
