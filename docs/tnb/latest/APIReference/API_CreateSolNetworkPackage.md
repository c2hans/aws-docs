---
source_url: https://docs.aws.amazon.com/tnb/latest/APIReference/API_CreateSolNetworkPackage.html
---

# CreateSolNetworkPackage
<a name="API_CreateSolNetworkPackage"></a>

Creates a network package.

A network package is a .zip file in CSAR (Cloud Service Archive) format defines the function packages you want to deploy and the AWS infrastructure you want to deploy them on. For more information, see [Network instances](https://docs.aws.amazon.com/tnb/latest/ug/network-instances.html) in the * AWS Telco Network Builder User Guide*.

A network package consists of a network service descriptor (NSD) file (required) and any additional files (optional), such as scripts specific to your needs. For example, if you have multiple function packages in your network package, you can use the NSD to define which network functions should run in certain VPCs, subnets, or EKS clusters.

This request creates an empty network package container with an ID. Once you create a network package, you can upload the network package content using [PutSolNetworkPackageContent](https://docs.aws.amazon.com/tnb/latest/APIReference/API_PutSolNetworkPackageContent.html).

## Request Syntax
<a name="API_CreateSolNetworkPackage_RequestSyntax"></a>

```
POST /sol/nsd/v1/ns_descriptors HTTP/1.1
Content-type: application/json

{
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateSolNetworkPackage_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateSolNetworkPackage_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [tags](#API_CreateSolNetworkPackage_RequestSyntax) **   <a name="TNB-CreateSolNetworkPackage-request-tags"></a>
A tag is a label that you assign to an AWS resource. Each tag consists of a key and an optional value. You can use tags to search and filter your resources or track your AWS costs.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Pattern: `(?!aws:).{1,128}`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateSolNetworkPackage_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "arn": "string",
   "id": "string",
   "nsdOnboardingState": "string",
   "nsdOperationalState": "string",
   "nsdUsageState": "string",
   "tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_CreateSolNetworkPackage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_CreateSolNetworkPackage_ResponseSyntax) **   <a name="TNB-CreateSolNetworkPackage-response-arn"></a>
Network package ARN.
Type: String
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-b|aws-us-gov):tnb:([a-z]{2}(-(gov|isob|iso))?-(east|west|north|south|central){1,2}-[0-9]):\d{12}:(network-package/np-[a-f0-9]{17})`

 ** [id](#API_CreateSolNetworkPackage_ResponseSyntax) **   <a name="TNB-CreateSolNetworkPackage-response-id"></a>
ID of the network package.
Type: String
Pattern: `np-[a-f0-9]{17}`

 ** [nsdOnboardingState](#API_CreateSolNetworkPackage_ResponseSyntax) **   <a name="TNB-CreateSolNetworkPackage-response-nsdOnboardingState"></a>
Onboarding state of the network service descriptor in the network package.
Type: String
Valid Values: `CREATED | ONBOARDED | ERROR`

 ** [nsdOperationalState](#API_CreateSolNetworkPackage_ResponseSyntax) **   <a name="TNB-CreateSolNetworkPackage-response-nsdOperationalState"></a>
Operational state of the network service descriptor in the network package.
Type: String
Valid Values: `ENABLED | DISABLED`

 ** [nsdUsageState](#API_CreateSolNetworkPackage_ResponseSyntax) **   <a name="TNB-CreateSolNetworkPackage-response-nsdUsageState"></a>
Usage state of the network service descriptor in the network package.
Type: String
Valid Values: `IN_USE | NOT_IN_USE`

 ** [tags](#API_CreateSolNetworkPackage_ResponseSyntax) **   <a name="TNB-CreateSolNetworkPackage-response-tags"></a>
A tag is a label that you assign to an AWS resource. Each tag consists of a key and an optional value. You can use tags to search and filter your resources or track your AWS costs.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Pattern: `(?!aws:).{1,128}`
Value Length Constraints: Minimum length of 0. Maximum length of 256.

## Errors
<a name="API_CreateSolNetworkPackage_Errors"></a>

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
<a name="API_CreateSolNetworkPackage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/tnb-2008-10-21/CreateSolNetworkPackage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/tnb-2008-10-21/CreateSolNetworkPackage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/tnb-2008-10-21/CreateSolNetworkPackage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/tnb-2008-10-21/CreateSolNetworkPackage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/tnb-2008-10-21/CreateSolNetworkPackage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/tnb-2008-10-21/CreateSolNetworkPackage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/tnb-2008-10-21/CreateSolNetworkPackage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/tnb-2008-10-21/CreateSolNetworkPackage)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/tnb-2008-10-21/CreateSolNetworkPackage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/tnb-2008-10-21/CreateSolNetworkPackage)
