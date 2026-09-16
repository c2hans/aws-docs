---
source_url: https://docs.aws.amazon.com/tnb/latest/APIReference/API_TerminateSolNetworkInstance.html
---

# TerminateSolNetworkInstance
<a name="API_TerminateSolNetworkInstance"></a>

Terminates a network instance.

A network instance is a single network created in AWS TNB that can be deployed and on which life-cycle operations (like terminate, update, and delete) can be performed.

You must terminate a network instance before you can delete it.

## Request Syntax
<a name="API_TerminateSolNetworkInstance_RequestSyntax"></a>

```
POST /sol/nslcm/v1/ns_instances/{{nsInstanceId}}/terminate HTTP/1.1
Content-type: application/json

{
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_TerminateSolNetworkInstance_RequestParameters"></a>

The request uses the following URI parameters.

 ** [nsInstanceId](#API_TerminateSolNetworkInstance_RequestSyntax) **   <a name="TNB-TerminateSolNetworkInstance-request-uri-nsInstanceId"></a>
ID of the network instance.
Pattern: `ni-[a-f0-9]{17}`
Required: Yes

## Request Body
<a name="API_TerminateSolNetworkInstance_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [tags](#API_TerminateSolNetworkInstance_RequestSyntax) **   <a name="TNB-TerminateSolNetworkInstance-request-tags"></a>
A tag is a label that you assign to an AWS resource. Each tag consists of a key and an optional value. When you use this API, the tags are only applied to the network operation that is created. These tags are not applied to the network instance. Use tags to search and filter your resources or track your AWS costs.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Pattern: `(?!aws:).{1,128}`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_TerminateSolNetworkInstance_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "nsLcmOpOccId": "string",
   "tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_TerminateSolNetworkInstance_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [nsLcmOpOccId](#API_TerminateSolNetworkInstance_ResponseSyntax) **   <a name="TNB-TerminateSolNetworkInstance-response-nsLcmOpOccId"></a>
The identifier of the network operation.
Type: String
Pattern: `no-[a-f0-9]{17}`

 ** [tags](#API_TerminateSolNetworkInstance_ResponseSyntax) **   <a name="TNB-TerminateSolNetworkInstance-response-tags"></a>
A tag is a label that you assign to an AWS resource. Each tag consists of a key and an optional value. When you use this API, the tags are only applied to the network operation that is created. These tags are not applied to the network instance. Use tags to search and filter your resources or track your AWS costs.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Pattern: `(?!aws:).{1,128}`
Value Length Constraints: Minimum length of 0. Maximum length of 256.

## Errors
<a name="API_TerminateSolNetworkInstance_Errors"></a>

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
<a name="API_TerminateSolNetworkInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/tnb-2008-10-21/TerminateSolNetworkInstance)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/tnb-2008-10-21/TerminateSolNetworkInstance)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/tnb-2008-10-21/TerminateSolNetworkInstance)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/tnb-2008-10-21/TerminateSolNetworkInstance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/tnb-2008-10-21/TerminateSolNetworkInstance)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/tnb-2008-10-21/TerminateSolNetworkInstance)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/tnb-2008-10-21/TerminateSolNetworkInstance)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/tnb-2008-10-21/TerminateSolNetworkInstance)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/tnb-2008-10-21/TerminateSolNetworkInstance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/tnb-2008-10-21/TerminateSolNetworkInstance)
