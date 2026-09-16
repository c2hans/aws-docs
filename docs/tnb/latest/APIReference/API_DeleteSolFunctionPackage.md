---
source_url: https://docs.aws.amazon.com/tnb/latest/APIReference/API_DeleteSolFunctionPackage.html
---

# DeleteSolFunctionPackage
<a name="API_DeleteSolFunctionPackage"></a>

Deletes a function package.

A function package is a .zip file in CSAR (Cloud Service Archive) format that contains a network function (an ETSI standard telecommunication application) and function package descriptor that uses the TOSCA standard to describe how the network functions should run on your network.

To delete a function package, the package must be in a disabled state. To disable a function package, see [UpdateSolFunctionPackage](https://docs.aws.amazon.com/tnb/latest/APIReference/API_UpdateSolFunctionPackage.html).

## Request Syntax
<a name="API_DeleteSolFunctionPackage_RequestSyntax"></a>

```
DELETE /sol/vnfpkgm/v1/vnf_packages/{{vnfPkgId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteSolFunctionPackage_RequestParameters"></a>

The request uses the following URI parameters.

 ** [vnfPkgId](#API_DeleteSolFunctionPackage_RequestSyntax) **   <a name="TNB-DeleteSolFunctionPackage-request-uri-vnfPkgId"></a>
ID of the function package.
Pattern: `fp-[a-f0-9]{17}`
Required: Yes

## Request Body
<a name="API_DeleteSolFunctionPackage_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteSolFunctionPackage_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_DeleteSolFunctionPackage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_DeleteSolFunctionPackage_Errors"></a>

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
<a name="API_DeleteSolFunctionPackage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/tnb-2008-10-21/DeleteSolFunctionPackage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/tnb-2008-10-21/DeleteSolFunctionPackage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/tnb-2008-10-21/DeleteSolFunctionPackage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/tnb-2008-10-21/DeleteSolFunctionPackage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/tnb-2008-10-21/DeleteSolFunctionPackage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/tnb-2008-10-21/DeleteSolFunctionPackage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/tnb-2008-10-21/DeleteSolFunctionPackage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/tnb-2008-10-21/DeleteSolFunctionPackage)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/tnb-2008-10-21/DeleteSolFunctionPackage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/tnb-2008-10-21/DeleteSolFunctionPackage)
