---
source_url: https://docs.aws.amazon.com/tnb/latest/APIReference/API_GetSolFunctionPackage.html
---

# GetSolFunctionPackage
<a name="API_GetSolFunctionPackage"></a>

Gets the details of an individual function package, such as the operational state and whether the package is in use.

A function package is a .zip file in CSAR (Cloud Service Archive) format that contains a network function (an ETSI standard telecommunication application) and function package descriptor that uses the TOSCA standard to describe how the network functions should run on your network..

## Request Syntax
<a name="API_GetSolFunctionPackage_RequestSyntax"></a>

```
GET /sol/vnfpkgm/v1/vnf_packages/{{vnfPkgId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetSolFunctionPackage_RequestParameters"></a>

The request uses the following URI parameters.

 ** [vnfPkgId](#API_GetSolFunctionPackage_RequestSyntax) **   <a name="TNB-GetSolFunctionPackage-request-uri-vnfPkgId"></a>
ID of the function package.
Pattern: `fp-[a-f0-9]{17}`
Required: Yes

## Request Body
<a name="API_GetSolFunctionPackage_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetSolFunctionPackage_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "id": "string",
   "metadata": {
      "createdAt": "string",
      "lastModified": "string",
      "vnfd": {
         "overrides": [
            {
               "defaultValue": "string",
               "name": "string"
            }
         ]
      }
   },
   "onboardingState": "string",
   "operationalState": "string",
   "tags": {
      "string" : "string"
   },
   "usageState": "string",
   "vnfdId": "string",
   "vnfdVersion": "string",
   "vnfProductName": "string",
   "vnfProvider": "string"
}
```

## Response Elements
<a name="API_GetSolFunctionPackage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_GetSolFunctionPackage_ResponseSyntax) **   <a name="TNB-GetSolFunctionPackage-response-arn"></a>
Function package ARN.
Type: String
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-b|aws-us-gov):tnb:([a-z]{2}(-(gov|isob|iso))?-(east|west|north|south|central){1,2}-[0-9]):\d{12}:(function-package/fp-[a-f0-9]{17})`

 ** [id](#API_GetSolFunctionPackage_ResponseSyntax) **   <a name="TNB-GetSolFunctionPackage-response-id"></a>
Function package ID.
Type: String
Pattern: `fp-[a-f0-9]{17}`

 ** [metadata](#API_GetSolFunctionPackage_ResponseSyntax) **   <a name="TNB-GetSolFunctionPackage-response-metadata"></a>
Metadata related to the function package.
A function package is a .zip file in CSAR (Cloud Service Archive) format that contains a network function (an ETSI standard telecommunication application) and function package descriptor that uses the TOSCA standard to describe how the network functions should run on your network.
Type: [GetSolFunctionPackageMetadata](API_GetSolFunctionPackageMetadata.md) object

 ** [onboardingState](#API_GetSolFunctionPackage_ResponseSyntax) **   <a name="TNB-GetSolFunctionPackage-response-onboardingState"></a>
Function package onboarding state.
Type: String
Valid Values: `CREATED | ONBOARDED | ERROR`

 ** [operationalState](#API_GetSolFunctionPackage_ResponseSyntax) **   <a name="TNB-GetSolFunctionPackage-response-operationalState"></a>
Function package operational state.
Type: String
Valid Values: `ENABLED | DISABLED`

 ** [tags](#API_GetSolFunctionPackage_ResponseSyntax) **   <a name="TNB-GetSolFunctionPackage-response-tags"></a>
A tag is a label that you assign to an AWS resource. Each tag consists of a key and an optional value. You can use tags to search and filter your resources or track your AWS costs.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Pattern: `(?!aws:).{1,128}`
Value Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [usageState](#API_GetSolFunctionPackage_ResponseSyntax) **   <a name="TNB-GetSolFunctionPackage-response-usageState"></a>
Function package usage state.
Type: String
Valid Values: `IN_USE | NOT_IN_USE`

 ** [vnfdId](#API_GetSolFunctionPackage_ResponseSyntax) **   <a name="TNB-GetSolFunctionPackage-response-vnfdId"></a>
Function package descriptor ID.
Type: String

 ** [vnfdVersion](#API_GetSolFunctionPackage_ResponseSyntax) **   <a name="TNB-GetSolFunctionPackage-response-vnfdVersion"></a>
Function package descriptor version.
Type: String

 ** [vnfProductName](#API_GetSolFunctionPackage_ResponseSyntax) **   <a name="TNB-GetSolFunctionPackage-response-vnfProductName"></a>
Network function product name.
Type: String

 ** [vnfProvider](#API_GetSolFunctionPackage_ResponseSyntax) **   <a name="TNB-GetSolFunctionPackage-response-vnfProvider"></a>
Network function provider.
Type: String

## Errors
<a name="API_GetSolFunctionPackage_Errors"></a>

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
<a name="API_GetSolFunctionPackage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/tnb-2008-10-21/GetSolFunctionPackage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/tnb-2008-10-21/GetSolFunctionPackage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/tnb-2008-10-21/GetSolFunctionPackage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/tnb-2008-10-21/GetSolFunctionPackage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/tnb-2008-10-21/GetSolFunctionPackage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/tnb-2008-10-21/GetSolFunctionPackage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/tnb-2008-10-21/GetSolFunctionPackage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/tnb-2008-10-21/GetSolFunctionPackage)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/tnb-2008-10-21/GetSolFunctionPackage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/tnb-2008-10-21/GetSolFunctionPackage)
