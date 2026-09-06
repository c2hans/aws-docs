---
source_url: https://docs.aws.amazon.com/tnb/latest/APIReference/API_GetSolNetworkPackage.html
---

# GetSolNetworkPackage
<a name="API_GetSolNetworkPackage"></a>

Gets the details of a network package.

A network package is a .zip file in CSAR (Cloud Service Archive) format defines the function packages you want to deploy and the AWS infrastructure you want to deploy them on.

## Request Syntax
<a name="API_GetSolNetworkPackage_RequestSyntax"></a>

```
GET /sol/nsd/v1/ns_descriptors/{{nsdInfoId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetSolNetworkPackage_RequestParameters"></a>

The request uses the following URI parameters.

 ** [nsdInfoId](#API_GetSolNetworkPackage_RequestSyntax) **   <a name="TNB-GetSolNetworkPackage-request-uri-nsdInfoId"></a>
ID of the network service descriptor in the network package.
Pattern: `np-[a-f0-9]{17}`
Required: Yes

## Request Body
<a name="API_GetSolNetworkPackage_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetSolNetworkPackage_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "id": "string",
   "metadata": {
      "createdAt": "string",
      "lastModified": "string",
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
   "nsdOnboardingState": "string",
   "nsdOperationalState": "string",
   "nsdUsageState": "string",
   "nsdVersion": "string",
   "tags": {
      "string" : "string"
   },
   "vnfPkgIds": [ "string" ]
}
```

## Response Elements
<a name="API_GetSolNetworkPackage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_GetSolNetworkPackage_ResponseSyntax) **   <a name="TNB-GetSolNetworkPackage-response-arn"></a>
Network package ARN.
Type: String
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-b|aws-us-gov):tnb:([a-z]{2}(-(gov|isob|iso))?-(east|west|north|south|central){1,2}-[0-9]):\d{12}:(network-package/np-[a-f0-9]{17})`

 ** [id](#API_GetSolNetworkPackage_ResponseSyntax) **   <a name="TNB-GetSolNetworkPackage-response-id"></a>
Network package ID.
Type: String
Pattern: `np-[a-f0-9]{17}`

 ** [metadata](#API_GetSolNetworkPackage_ResponseSyntax) **   <a name="TNB-GetSolNetworkPackage-response-metadata"></a>
Metadata associated with a network package.
A network package is a .zip file in CSAR (Cloud Service Archive) format defines the function packages you want to deploy and the AWS infrastructure you want to deploy them on.
Type: [GetSolNetworkPackageMetadata](API_GetSolNetworkPackageMetadata.md) object

 ** [nsdId](#API_GetSolNetworkPackage_ResponseSyntax) **   <a name="TNB-GetSolNetworkPackage-response-nsdId"></a>
Network service descriptor ID.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

 ** [nsdName](#API_GetSolNetworkPackage_ResponseSyntax) **   <a name="TNB-GetSolNetworkPackage-response-nsdName"></a>
Network service descriptor name.
Type: String

 ** [nsdOnboardingState](#API_GetSolNetworkPackage_ResponseSyntax) **   <a name="TNB-GetSolNetworkPackage-response-nsdOnboardingState"></a>
Network service descriptor onboarding state.
Type: String
Valid Values: `CREATED | ONBOARDED | ERROR`

 ** [nsdOperationalState](#API_GetSolNetworkPackage_ResponseSyntax) **   <a name="TNB-GetSolNetworkPackage-response-nsdOperationalState"></a>
Network service descriptor operational state.
Type: String
Valid Values: `ENABLED | DISABLED`

 ** [nsdUsageState](#API_GetSolNetworkPackage_ResponseSyntax) **   <a name="TNB-GetSolNetworkPackage-response-nsdUsageState"></a>
Network service descriptor usage state.
Type: String
Valid Values: `IN_USE | NOT_IN_USE`

 ** [nsdVersion](#API_GetSolNetworkPackage_ResponseSyntax) **   <a name="TNB-GetSolNetworkPackage-response-nsdVersion"></a>
Network service descriptor version.
Type: String

 ** [tags](#API_GetSolNetworkPackage_ResponseSyntax) **   <a name="TNB-GetSolNetworkPackage-response-tags"></a>
A tag is a label that you assign to an AWS resource. Each tag consists of a key and an optional value. You can use tags to search and filter your resources or track your AWS costs.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Pattern: `(?!aws:).{1,128}`
Value Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [vnfPkgIds](#API_GetSolNetworkPackage_ResponseSyntax) **   <a name="TNB-GetSolNetworkPackage-response-vnfPkgIds"></a>
Identifies the function package for the function package descriptor referenced by the onboarded network package.
Type: Array of strings
Pattern: `fp-[a-f0-9]{17}`

## Errors
<a name="API_GetSolNetworkPackage_Errors"></a>

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
<a name="API_GetSolNetworkPackage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/tnb-2008-10-21/GetSolNetworkPackage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/tnb-2008-10-21/GetSolNetworkPackage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/tnb-2008-10-21/GetSolNetworkPackage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/tnb-2008-10-21/GetSolNetworkPackage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/tnb-2008-10-21/GetSolNetworkPackage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/tnb-2008-10-21/GetSolNetworkPackage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/tnb-2008-10-21/GetSolNetworkPackage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/tnb-2008-10-21/GetSolNetworkPackage)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/tnb-2008-10-21/GetSolNetworkPackage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/tnb-2008-10-21/GetSolNetworkPackage)
