---
source_url: https://docs.aws.amazon.com/tnb/latest/APIReference/API_GetSolNetworkInstance.html
---

# GetSolNetworkInstance
<a name="API_GetSolNetworkInstance"></a>

Gets the details of the network instance.

A network instance is a single network created in AWS TNB that can be deployed and on which life-cycle operations (like terminate, update, and delete) can be performed.

## Request Syntax
<a name="API_GetSolNetworkInstance_RequestSyntax"></a>

```
GET /sol/nslcm/v1/ns_instances/{{nsInstanceId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetSolNetworkInstance_RequestParameters"></a>

The request uses the following URI parameters.

 ** [nsInstanceId](#API_GetSolNetworkInstance_RequestSyntax) **   <a name="TNB-GetSolNetworkInstance-request-uri-nsInstanceId"></a>
ID of the network instance.
Pattern: `ni-[a-f0-9]{17}`
Required: Yes

## Request Body
<a name="API_GetSolNetworkInstance_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetSolNetworkInstance_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "id": "string",
   "lcmOpInfo": {
      "nsLcmOpOccId": "string"
   },
   "metadata": {
      "createdAt": "string",
      "lastModified": "string"
   },
   "nsdId": "string",
   "nsdInfoId": "string",
   "nsInstanceDescription": "string",
   "nsInstanceName": "string",
   "nsState": "string",
   "tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_GetSolNetworkInstance_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_GetSolNetworkInstance_ResponseSyntax) **   <a name="TNB-GetSolNetworkInstance-response-arn"></a>
Network instance ARN.
Type: String
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-b|aws-us-gov):tnb:([a-z]{2}(-(gov|isob|iso))?-(east|west|north|south|central){1,2}-[0-9]):\d{12}:(network-instance/ni-[a-f0-9]{17})`

 ** [id](#API_GetSolNetworkInstance_ResponseSyntax) **   <a name="TNB-GetSolNetworkInstance-response-id"></a>
Network instance ID.
Type: String
Pattern: `ni-[a-f0-9]{17}`

 ** [lcmOpInfo](#API_GetSolNetworkInstance_ResponseSyntax) **   <a name="TNB-GetSolNetworkInstance-response-lcmOpInfo"></a>
Lifecycle management operation details on the network instance.
Lifecycle management operations are deploy, update, or delete operations.
Type: [LcmOperationInfo](API_LcmOperationInfo.md) object

 ** [metadata](#API_GetSolNetworkInstance_ResponseSyntax) **   <a name="TNB-GetSolNetworkInstance-response-metadata"></a>
The metadata of a network instance.
A network instance is a single network created in AWS TNB that can be deployed and on which life-cycle operations (like terminate, update, and delete) can be performed.
Type: [GetSolNetworkInstanceMetadata](API_GetSolNetworkInstanceMetadata.md) object

 ** [nsdId](#API_GetSolNetworkInstance_ResponseSyntax) **   <a name="TNB-GetSolNetworkInstance-response-nsdId"></a>
Network service descriptor ID.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

 ** [nsdInfoId](#API_GetSolNetworkInstance_ResponseSyntax) **   <a name="TNB-GetSolNetworkInstance-response-nsdInfoId"></a>
Network service descriptor info ID.
Type: String
Pattern: `np-[a-f0-9]{17}`

 ** [nsInstanceDescription](#API_GetSolNetworkInstance_ResponseSyntax) **   <a name="TNB-GetSolNetworkInstance-response-nsInstanceDescription"></a>
Network instance description.
Type: String

 ** [nsInstanceName](#API_GetSolNetworkInstance_ResponseSyntax) **   <a name="TNB-GetSolNetworkInstance-response-nsInstanceName"></a>
Network instance name.
Type: String

 ** [nsState](#API_GetSolNetworkInstance_ResponseSyntax) **   <a name="TNB-GetSolNetworkInstance-response-nsState"></a>
Network instance state.
Type: String
Valid Values: `INSTANTIATED | NOT_INSTANTIATED | UPDATED | IMPAIRED | UPDATE_FAILED | STOPPED | DELETED | INSTANTIATE_IN_PROGRESS | INTENT_TO_UPDATE_IN_PROGRESS | UPDATE_IN_PROGRESS | TERMINATE_IN_PROGRESS`

 ** [tags](#API_GetSolNetworkInstance_ResponseSyntax) **   <a name="TNB-GetSolNetworkInstance-response-tags"></a>
A tag is a label that you assign to an AWS resource. Each tag consists of a key and an optional value. You can use tags to search and filter your resources or track your AWS costs.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Pattern: `(?!aws:).{1,128}`
Value Length Constraints: Minimum length of 0. Maximum length of 256.

## Errors
<a name="API_GetSolNetworkInstance_Errors"></a>

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
<a name="API_GetSolNetworkInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/tnb-2008-10-21/GetSolNetworkInstance)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/tnb-2008-10-21/GetSolNetworkInstance)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/tnb-2008-10-21/GetSolNetworkInstance)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/tnb-2008-10-21/GetSolNetworkInstance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/tnb-2008-10-21/GetSolNetworkInstance)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/tnb-2008-10-21/GetSolNetworkInstance)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/tnb-2008-10-21/GetSolNetworkInstance)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/tnb-2008-10-21/GetSolNetworkInstance)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/tnb-2008-10-21/GetSolNetworkInstance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/tnb-2008-10-21/GetSolNetworkInstance)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Telco Network Builder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query tnb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
