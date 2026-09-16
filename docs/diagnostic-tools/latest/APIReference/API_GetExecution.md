---
source_url: https://docs.aws.amazon.com/diagnostic-tools/latest/APIReference/API_GetExecution.html
---

# GetExecution
<a name="API_GetExecution"></a>

Retrieve an execution by its id.

## Request Syntax
<a name="API_GetExecution_RequestSyntax"></a>

```
{
   "identifier": "{{string}}"
}
```

## Request Parameters
<a name="API_GetExecution_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [identifier](#API_GetExecution_RequestSyntax) **   <a name="diagnostictools-GetExecution-request-identifier"></a>
The unique identifier for an existing troubleshooting execution to examine. The execution ID is returned by StartExecution
Type: String
Length Constraints: Minimum length of 12. Maximum length of 2048.
Required: Yes

## Response Syntax
<a name="API_GetExecution_ResponseSyntax"></a>

```
{
   "execution": {
      "creationTime": number,
      "executionId": "string",
      "parameters": "string",
      "requesterArn": "string",
      "requesterId": "string",
      "requestState": "string",
      "roleArn": "string",
      "status": "string",
      "storageRegion": "string",
      "targetRegions": [ "string" ],
      "toolId": "string",
      "toolVersionId": "string"
   }
}
```

## Response Elements
<a name="API_GetExecution_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [execution](#API_GetExecution_ResponseSyntax) **   <a name="diagnostictools-GetExecution-response-execution"></a>
Execution Information Metadata
Type: [Execution](API_Execution.md) object

## Errors
<a name="API_GetExecution_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have sufficient access to perform this action.
 ** message **
Throttle error message.
HTTP Status Code: 400

 ** InternalServerException **
The request failed because of an internal error. Try your request again later
 ** message **
Error Message
 ** retryAfterSeconds **
Second after which client can retry the transaction
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request failed because it references a resource that doesn't exist.
 ** message **
Reason for the resource not found.
 ** resourceId **
The unique ID of the resource referenced in the failed request.
 ** resourceType **
The resource type of the resource referenced in the failed request.
HTTP Status Code: 400

 ** ThrottlingException **
The request failed because it exceeded a throttling quota.
 ** message **
Throttle error message.
 ** quotaCode **
The quota code recognized by the AWS Service Quotas service.
 ** retryAfterSeconds **
Second after which client can retry the transaction
 ** serviceCode **
The code for the AWS-service; that owns the quota.
HTTP Status Code: 400

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
 ** fieldList **
The field that caused the error, if applicable. If more than one field caused the error, pick one and elaborate in the message.
 ** message **
Description of the error.
 ** reason **
Reason the request failed validation.
HTTP Status Code: 400

## Examples
<a name="API_GetExecution_Examples"></a>

This example illustrates one usage of `GetExecution`.

### Example
<a name="API_GetExecution_Example_1"></a>

 **Using AWS JSON protocol (default)**

#### Sample Request
<a name="API_GetExecution_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ts.us-east-2.amazonaws.com
X-Amz-Target: Troubleshooting.GetExecution
Content-Type: application/x-amz-json-1.0
X-Amz-Date: <Date>
Authorization: <AuthParams>
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
{
    "executionId": "e-aaaaaaaaa"
}
```

#### Sample Response
<a name="API_GetExecution_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <requestId>
Content-Length: 0
Date: <Date>
Content-Type: application/x-amz-json-1.0
{
    "execution": {
        "creationTime": 1700601,
        "executionId": "e-aaaaaaaaa",
        "requestState": "SUBMITTED",
        "requesterArn": "requesterArn",
        "requesterId": "user-id",
        "roleArn": "<sample role>",
        "status": "CREATED",
        "storageRegion": "us-east-2",
        "tags": [],
        "targetRegions": [
            "us-east-1"
        ],
        "toolId": "EC2SystemsManager",
        "toolVersionId": "1.0.0"
    }
}
```

## See Also
<a name="API_GetExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/troubleshooting-2023-01-01/GetExecution)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/troubleshooting-2023-01-01/GetExecution)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/troubleshooting-2023-01-01/GetExecution)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/troubleshooting-2023-01-01/GetExecution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/troubleshooting-2023-01-01/GetExecution)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/troubleshooting-2023-01-01/GetExecution)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/troubleshooting-2023-01-01/GetExecution)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/troubleshooting-2023-01-01/GetExecution)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/troubleshooting-2023-01-01/GetExecution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/troubleshooting-2023-01-01/GetExecution)
