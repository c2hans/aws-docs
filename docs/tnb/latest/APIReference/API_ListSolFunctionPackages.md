---
source_url: https://docs.aws.amazon.com/tnb/latest/APIReference/API_ListSolFunctionPackages.html
---

# ListSolFunctionPackages
<a name="API_ListSolFunctionPackages"></a>

Lists information about function packages.

A function package is a .zip file in CSAR (Cloud Service Archive) format that contains a network function (an ETSI standard telecommunication application) and function package descriptor that uses the TOSCA standard to describe how the network functions should run on your network.

## Request Syntax
<a name="API_ListSolFunctionPackages_RequestSyntax"></a>

```
GET /sol/vnfpkgm/v1/vnf_packages?max_results={{maxResults}}&nextpage_opaque_marker={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListSolFunctionPackages_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListSolFunctionPackages_RequestSyntax) **   <a name="TNB-ListSolFunctionPackages-request-uri-maxResults"></a>
The maximum number of results to include in the response.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListSolFunctionPackages_RequestSyntax) **   <a name="TNB-ListSolFunctionPackages-request-uri-nextToken"></a>
The token for the next page of results.

## Request Body
<a name="API_ListSolFunctionPackages_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListSolFunctionPackages_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "functionPackages": [
      {
         "arn": "string",
         "id": "string",
         "metadata": {
            "createdAt": "string",
            "lastModified": "string"
         },
         "onboardingState": "string",
         "operationalState": "string",
         "usageState": "string",
         "vnfdId": "string",
         "vnfdVersion": "string",
         "vnfProductName": "string",
         "vnfProvider": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListSolFunctionPackages_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [functionPackages](#API_ListSolFunctionPackages_ResponseSyntax) **   <a name="TNB-ListSolFunctionPackages-response-functionPackages"></a>
Function packages. A function package is a .zip file in CSAR (Cloud Service Archive) format that contains a network function (an ETSI standard telecommunication application) and function package descriptor that uses the TOSCA standard to describe how the network functions should run on your network.
Type: Array of [ListSolFunctionPackageInfo](API_ListSolFunctionPackageInfo.md) objects

 ** [nextToken](#API_ListSolFunctionPackages_ResponseSyntax) **   <a name="TNB-ListSolFunctionPackages-response-nextToken"></a>
The token to use to retrieve the next page of results. This value is `null` when there are no more results to return.
Type: String

## Errors
<a name="API_ListSolFunctionPackages_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Insufficient permissions to make request.
HTTP Status Code: 403

 ** InternalServerException **
Unexpected error occurred. Problem on the server.
HTTP Status Code: 500

 ** ThrottlingException **
Exception caused by throttling.
HTTP Status Code: 429

 ** ValidationException **
Unable to process the request because the client provided input failed to satisfy request constraints.
HTTP Status Code: 400

## See Also
<a name="API_ListSolFunctionPackages_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/tnb-2008-10-21/ListSolFunctionPackages)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/tnb-2008-10-21/ListSolFunctionPackages)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/tnb-2008-10-21/ListSolFunctionPackages)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/tnb-2008-10-21/ListSolFunctionPackages)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/tnb-2008-10-21/ListSolFunctionPackages)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/tnb-2008-10-21/ListSolFunctionPackages)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/tnb-2008-10-21/ListSolFunctionPackages)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/tnb-2008-10-21/ListSolFunctionPackages)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/tnb-2008-10-21/ListSolFunctionPackages)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/tnb-2008-10-21/ListSolFunctionPackages)
