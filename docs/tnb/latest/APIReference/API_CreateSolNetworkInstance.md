---
source_url: https://docs.aws.amazon.com/tnb/latest/APIReference/API_CreateSolNetworkInstance.html
---

# CreateSolNetworkInstance
<a name="API_CreateSolNetworkInstance"></a>

Creates a network instance.

A network instance is a single network created in AWS TNB that can be deployed and on which life-cycle operations (like terminate, update, and delete) can be performed. Creating a network instance is the third step after creating a network package. For more information about network instances, [Network instances](https://docs.aws.amazon.com/tnb/latest/ug/network-instances.html) in the * AWS Telco Network Builder User Guide*.

Once you create a network instance, you can instantiate it. To instantiate a network, see [InstantiateSolNetworkInstance](https://docs.aws.amazon.com/tnb/latest/APIReference/API_InstantiateSolNetworkInstance.html).

## Request Syntax
<a name="API_CreateSolNetworkInstance_RequestSyntax"></a>

```
POST /sol/nslcm/v1/ns_instances HTTP/1.1
Content-type: application/json

{
   "nsDescription": "{{string}}",
   "nsdInfoId": "{{string}}",
   "nsName": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateSolNetworkInstance_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateSolNetworkInstance_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [nsDescription](#API_CreateSolNetworkInstance_RequestSyntax) **   <a name="TNB-CreateSolNetworkInstance-request-nsDescription"></a>
Network instance description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Required: No

 ** [nsdInfoId](#API_CreateSolNetworkInstance_RequestSyntax) **   <a name="TNB-CreateSolNetworkInstance-request-nsdInfoId"></a>
ID for network service descriptor.
Type: String
Pattern: `np-[a-f0-9]{17}`
Required: Yes

 ** [nsName](#API_CreateSolNetworkInstance_RequestSyntax) **   <a name="TNB-CreateSolNetworkInstance-request-nsName"></a>
Network instance name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [tags](#API_CreateSolNetworkInstance_RequestSyntax) **   <a name="TNB-CreateSolNetworkInstance-request-tags"></a>
A tag is a label that you assign to an AWS resource. Each tag consists of a key and an optional value. You can use tags to search and filter your resources or track your AWS costs.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Pattern: `(?!aws:).{1,128}`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateSolNetworkInstance_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "arn": "string",
   "id": "string",
   "nsdInfoId": "string",
   "nsInstanceName": "string",
   "tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_CreateSolNetworkInstance_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_CreateSolNetworkInstance_ResponseSyntax) **   <a name="TNB-CreateSolNetworkInstance-response-arn"></a>
Network instance ARN.
Type: String
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-b|aws-us-gov):tnb:([a-z]{2}(-(gov|isob|iso))?-(east|west|north|south|central){1,2}-[0-9]):\d{12}:(network-instance/ni-[a-f0-9]{17})`

 ** [id](#API_CreateSolNetworkInstance_ResponseSyntax) **   <a name="TNB-CreateSolNetworkInstance-response-id"></a>
Network instance ID.
Type: String
Pattern: `ni-[a-f0-9]{17}`

 ** [nsdInfoId](#API_CreateSolNetworkInstance_ResponseSyntax) **   <a name="TNB-CreateSolNetworkInstance-response-nsdInfoId"></a>
Network service descriptor ID.
Type: String
Pattern: `np-[a-f0-9]{17}`

 ** [nsInstanceName](#API_CreateSolNetworkInstance_ResponseSyntax) **   <a name="TNB-CreateSolNetworkInstance-response-nsInstanceName"></a>
Network instance name.
Type: String

 ** [tags](#API_CreateSolNetworkInstance_ResponseSyntax) **   <a name="TNB-CreateSolNetworkInstance-response-tags"></a>
A tag is a label that you assign to an AWS resource. Each tag consists of a key and an optional value. You can use tags to search and filter your resources or track your AWS costs.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Pattern: `(?!aws:).{1,128}`
Value Length Constraints: Minimum length of 0. Maximum length of 256.

## Errors
<a name="API_CreateSolNetworkInstance_Errors"></a>

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
<a name="API_CreateSolNetworkInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/tnb-2008-10-21/CreateSolNetworkInstance)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/tnb-2008-10-21/CreateSolNetworkInstance)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/tnb-2008-10-21/CreateSolNetworkInstance)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/tnb-2008-10-21/CreateSolNetworkInstance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/tnb-2008-10-21/CreateSolNetworkInstance)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/tnb-2008-10-21/CreateSolNetworkInstance)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/tnb-2008-10-21/CreateSolNetworkInstance)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/tnb-2008-10-21/CreateSolNetworkInstance)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/tnb-2008-10-21/CreateSolNetworkInstance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/tnb-2008-10-21/CreateSolNetworkInstance)
