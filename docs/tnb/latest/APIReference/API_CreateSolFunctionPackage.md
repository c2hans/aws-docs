---
source_url: https://docs.aws.amazon.com/tnb/latest/APIReference/API_CreateSolFunctionPackage.html
---

# CreateSolFunctionPackage
<a name="API_CreateSolFunctionPackage"></a>

Creates a function package.

A function package is a .zip file in CSAR (Cloud Service Archive) format that contains a network function (an ETSI standard telecommunication application) and function package descriptor that uses the TOSCA standard to describe how the network functions should run on your network. For more information, see [Function packages](https://docs.aws.amazon.com/tnb/latest/ug/function-packages.html) in the * AWS Telco Network Builder User Guide*.

Creating a function package is the first step for creating a network in AWS TNB. This request creates an empty container with an ID. The next step is to upload the actual CSAR zip file into that empty container. To upload function package content, see [PutSolFunctionPackageContent](https://docs.aws.amazon.com/tnb/latest/APIReference/API_PutSolFunctionPackageContent.html).

## Request Syntax
<a name="API_CreateSolFunctionPackage_RequestSyntax"></a>

```
POST /sol/vnfpkgm/v1/vnf_packages HTTP/1.1
Content-type: application/json

{
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateSolFunctionPackage_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateSolFunctionPackage_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [tags](#API_CreateSolFunctionPackage_RequestSyntax) **   <a name="TNB-CreateSolFunctionPackage-request-tags"></a>
A tag is a label that you assign to an AWS resource. Each tag consists of a key and an optional value. You can use tags to search and filter your resources or track your AWS costs.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Pattern: `(?!aws:).{1,128}`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateSolFunctionPackage_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "arn": "string",
   "id": "string",
   "onboardingState": "string",
   "operationalState": "string",
   "tags": {
      "string" : "string"
   },
   "usageState": "string"
}
```

## Response Elements
<a name="API_CreateSolFunctionPackage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_CreateSolFunctionPackage_ResponseSyntax) **   <a name="TNB-CreateSolFunctionPackage-response-arn"></a>
Function package ARN.
Type: String
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-b|aws-us-gov):tnb:([a-z]{2}(-(gov|isob|iso))?-(east|west|north|south|central){1,2}-[0-9]):\d{12}:(function-package/fp-[a-f0-9]{17})`

 ** [id](#API_CreateSolFunctionPackage_ResponseSyntax) **   <a name="TNB-CreateSolFunctionPackage-response-id"></a>
ID of the function package.
Type: String
Pattern: `fp-[a-f0-9]{17}`

 ** [onboardingState](#API_CreateSolFunctionPackage_ResponseSyntax) **   <a name="TNB-CreateSolFunctionPackage-response-onboardingState"></a>
Onboarding state of the function package.
Type: String
Valid Values: `CREATED | ONBOARDED | ERROR`

 ** [operationalState](#API_CreateSolFunctionPackage_ResponseSyntax) **   <a name="TNB-CreateSolFunctionPackage-response-operationalState"></a>
Operational state of the function package.
Type: String
Valid Values: `ENABLED | DISABLED`

 ** [tags](#API_CreateSolFunctionPackage_ResponseSyntax) **   <a name="TNB-CreateSolFunctionPackage-response-tags"></a>
A tag is a label that you assign to an AWS resource. Each tag consists of a key and an optional value. You can use tags to search and filter your resources or track your AWS costs.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Pattern: `(?!aws:).{1,128}`
Value Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [usageState](#API_CreateSolFunctionPackage_ResponseSyntax) **   <a name="TNB-CreateSolFunctionPackage-response-usageState"></a>
Usage state of the function package.
Type: String
Valid Values: `IN_USE | NOT_IN_USE`

## Errors
<a name="API_CreateSolFunctionPackage_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Insufficient permissions to make request.
HTTP Status Code: 403

 ** InternalServerException **
Unexpected error occurred. Problem on the server.
HTTP Status Code: 500

 ** ServiceQuotaExceededException **
Service quotas have been exceeded.
HTTP Status Code: 402

 ** ThrottlingException **
Exception caused by throttling.
HTTP Status Code: 429

 ** ValidationException **
Unable to process the request because the client provided input failed to satisfy request constraints.
HTTP Status Code: 400

## See Also
<a name="API_CreateSolFunctionPackage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/tnb-2008-10-21/CreateSolFunctionPackage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/tnb-2008-10-21/CreateSolFunctionPackage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/tnb-2008-10-21/CreateSolFunctionPackage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/tnb-2008-10-21/CreateSolFunctionPackage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/tnb-2008-10-21/CreateSolFunctionPackage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/tnb-2008-10-21/CreateSolFunctionPackage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/tnb-2008-10-21/CreateSolFunctionPackage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/tnb-2008-10-21/CreateSolFunctionPackage)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/tnb-2008-10-21/CreateSolFunctionPackage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/tnb-2008-10-21/CreateSolFunctionPackage)
