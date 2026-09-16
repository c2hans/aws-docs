---
source_url: https://docs.aws.amazon.com/tnb/latest/APIReference/API_UpdateSolNetworkPackage.html
---

# UpdateSolNetworkPackage
<a name="API_UpdateSolNetworkPackage"></a>

Updates the operational state of a network package.

A network package is a .zip file in CSAR (Cloud Service Archive) format defines the function packages you want to deploy and the AWS infrastructure you want to deploy them on.

A network service descriptor is a .yaml file in a network package that uses the TOSCA standard to describe the network functions you want to deploy and the AWS infrastructure you want to deploy the network functions on.

## Request Syntax
<a name="API_UpdateSolNetworkPackage_RequestSyntax"></a>

```
PATCH /sol/nsd/v1/ns_descriptors/{{nsdInfoId}} HTTP/1.1
Content-type: application/json

{
   "nsdOperationalState": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateSolNetworkPackage_RequestParameters"></a>

The request uses the following URI parameters.

 ** [nsdInfoId](#API_UpdateSolNetworkPackage_RequestSyntax) **   <a name="TNB-UpdateSolNetworkPackage-request-uri-nsdInfoId"></a>
ID of the network service descriptor in the network package.
Pattern: `np-[a-f0-9]{17}`
Required: Yes

## Request Body
<a name="API_UpdateSolNetworkPackage_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [nsdOperationalState](#API_UpdateSolNetworkPackage_RequestSyntax) **   <a name="TNB-UpdateSolNetworkPackage-request-nsdOperationalState"></a>
Operational state of the network service descriptor in the network package.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: Yes

## Response Syntax
<a name="API_UpdateSolNetworkPackage_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nsdOperationalState": "string"
}
```

## Response Elements
<a name="API_UpdateSolNetworkPackage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nsdOperationalState](#API_UpdateSolNetworkPackage_ResponseSyntax) **   <a name="TNB-UpdateSolNetworkPackage-response-nsdOperationalState"></a>
Operational state of the network service descriptor in the network package.
Type: String
Valid Values: `ENABLED | DISABLED`

## Errors
<a name="API_UpdateSolNetworkPackage_Errors"></a>

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
<a name="API_UpdateSolNetworkPackage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/tnb-2008-10-21/UpdateSolNetworkPackage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/tnb-2008-10-21/UpdateSolNetworkPackage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/tnb-2008-10-21/UpdateSolNetworkPackage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/tnb-2008-10-21/UpdateSolNetworkPackage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/tnb-2008-10-21/UpdateSolNetworkPackage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/tnb-2008-10-21/UpdateSolNetworkPackage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/tnb-2008-10-21/UpdateSolNetworkPackage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/tnb-2008-10-21/UpdateSolNetworkPackage)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/tnb-2008-10-21/UpdateSolNetworkPackage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/tnb-2008-10-21/UpdateSolNetworkPackage)
