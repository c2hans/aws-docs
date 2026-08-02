---
source_url: https://docs.aws.amazon.com/tnb/latest/APIReference/API_GetSolNetworkOperation.html
---

# GetSolNetworkOperation
<a name="API_GetSolNetworkOperation"></a>

Gets the details of a network operation, including the tasks involved in the network operation and the status of the tasks.

A network operation is any operation that is done to your network, such as network instance instantiation or termination.

## Request Syntax
<a name="API_GetSolNetworkOperation_RequestSyntax"></a>

```
GET /sol/nslcm/v1/ns_lcm_op_occs/{{nsLcmOpOccId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetSolNetworkOperation_RequestParameters"></a>

The request uses the following URI parameters.

 ** [nsLcmOpOccId](#API_GetSolNetworkOperation_RequestSyntax) **   <a name="TNB-GetSolNetworkOperation-request-uri-nsLcmOpOccId"></a>
The identifier of the network operation.
Pattern: `no-[a-f0-9]{17}`
Required: Yes

## Request Body
<a name="API_GetSolNetworkOperation_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetSolNetworkOperation_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "error": {
      "detail": "string",
      "title": "string"
   },
   "id": "string",
   "lcmOperationType": "string",
   "metadata": {
      "createdAt": "string",
      "instantiateMetadata": {
         "additionalParamsForNs": JSON value,
         "nsdInfoId": "string"
      },
      "lastModified": "string",
      "modifyVnfInfoMetadata": {
         "vnfConfigurableProperties": JSON value,
         "vnfInstanceId": "string"
      },
      "updateNsMetadata": {
         "additionalParamsForNs": JSON value,
         "nsdInfoId": "string"
      }
   },
   "nsInstanceId": "string",
   "operationState": "string",
   "tags": {
      "string" : "string"
   },
   "tasks": [
      {
         "taskContext": {
            "string" : "string"
         },
         "taskEndTime": "string",
         "taskErrorDetails": {
            "cause": "string",
            "details": "string"
         },
         "taskName": "string",
         "taskStartTime": "string",
         "taskStatus": "string"
      }
   ],
   "updateType": "string"
}
```

## Response Elements
<a name="API_GetSolNetworkOperation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_GetSolNetworkOperation_ResponseSyntax) **   <a name="TNB-GetSolNetworkOperation-response-arn"></a>
Network operation ARN.
Type: String
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-b|aws-us-gov):tnb:([a-z]{2}(-(gov|isob|iso))?-(east|west|north|south|central){1,2}-[0-9]):\d{12}:(network-operation/no-[a-f0-9]{17})`

 ** [error](#API_GetSolNetworkOperation_ResponseSyntax) **   <a name="TNB-GetSolNetworkOperation-response-error"></a>
Error related to this specific network operation occurrence.
Type: [ProblemDetails](API_ProblemDetails.md) object

 ** [id](#API_GetSolNetworkOperation_ResponseSyntax) **   <a name="TNB-GetSolNetworkOperation-response-id"></a>
ID of this network operation occurrence.
Type: String
Pattern: `no-[a-f0-9]{17}`

 ** [lcmOperationType](#API_GetSolNetworkOperation_ResponseSyntax) **   <a name="TNB-GetSolNetworkOperation-response-lcmOperationType"></a>
Type of the operation represented by this occurrence.
Type: String
Valid Values: `INSTANTIATE | UPDATE | TERMINATE`

 ** [metadata](#API_GetSolNetworkOperation_ResponseSyntax) **   <a name="TNB-GetSolNetworkOperation-response-metadata"></a>
Metadata of this network operation occurrence.
Type: [GetSolNetworkOperationMetadata](API_GetSolNetworkOperationMetadata.md) object

 ** [nsInstanceId](#API_GetSolNetworkOperation_ResponseSyntax) **   <a name="TNB-GetSolNetworkOperation-response-nsInstanceId"></a>
ID of the network operation instance.
Type: String
Pattern: `ni-[a-f0-9]{17}`

 ** [operationState](#API_GetSolNetworkOperation_ResponseSyntax) **   <a name="TNB-GetSolNetworkOperation-response-operationState"></a>
The state of the network operation.
Type: String
Valid Values: `PROCESSING | COMPLETED | FAILED | CANCELLING | CANCELLED`

 ** [tags](#API_GetSolNetworkOperation_ResponseSyntax) **   <a name="TNB-GetSolNetworkOperation-response-tags"></a>
A tag is a label that you assign to an AWS resource. Each tag consists of a key and an optional value. You can use tags to search and filter your resources or track your AWS costs.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Pattern: `(?!aws:).{1,128}`
Value Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [tasks](#API_GetSolNetworkOperation_ResponseSyntax) **   <a name="TNB-GetSolNetworkOperation-response-tasks"></a>
All tasks associated with this operation occurrence.
Type: Array of [GetSolNetworkOperationTaskDetails](API_GetSolNetworkOperationTaskDetails.md) objects

 ** [updateType](#API_GetSolNetworkOperation_ResponseSyntax) **   <a name="TNB-GetSolNetworkOperation-response-updateType"></a>
Type of the update. Only present if the network operation lcmOperationType is `UPDATE`.
Type: String
Valid Values: `MODIFY_VNF_INFORMATION | UPDATE_NS`

## Errors
<a name="API_GetSolNetworkOperation_Errors"></a>

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
<a name="API_GetSolNetworkOperation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/tnb-2008-10-21/GetSolNetworkOperation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/tnb-2008-10-21/GetSolNetworkOperation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/tnb-2008-10-21/GetSolNetworkOperation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/tnb-2008-10-21/GetSolNetworkOperation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/tnb-2008-10-21/GetSolNetworkOperation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/tnb-2008-10-21/GetSolNetworkOperation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/tnb-2008-10-21/GetSolNetworkOperation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/tnb-2008-10-21/GetSolNetworkOperation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/tnb-2008-10-21/GetSolNetworkOperation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/tnb-2008-10-21/GetSolNetworkOperation)
