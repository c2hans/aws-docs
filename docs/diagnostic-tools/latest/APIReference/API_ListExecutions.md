---
source_url: https://docs.aws.amazon.com/diagnostic-tools/latest/APIReference/API_ListExecutions.html
---

# ListExecutions
<a name="API_ListExecutions"></a>

List all of the executions available for the current user.

## Request Syntax
<a name="API_ListExecutions_RequestSyntax"></a>

```
{
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListExecutions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListExecutions_RequestSyntax) **   <a name="diagnostictools-ListExecutions-request-maxResults"></a>
The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListExecutions_RequestSyntax) **   <a name="diagnostictools-ListExecutions-request-nextToken"></a>
The token for the next set of items to return. (You received this token from a previous call.)
Type: String
Pattern: `[A-Za-z0-9\-_]*={0,3}`
Required: No

## Response Syntax
<a name="API_ListExecutions_ResponseSyntax"></a>

```
{
   "executionList": [
      {
         "creationTime": number,
         "executionId": "string",
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
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListExecutions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [executionList](#API_ListExecutions_ResponseSyntax) **   <a name="diagnostictools-ListExecutions-response-executionList"></a>
Array of Execution objects
Type: Array of [ExecutionSummary](API_ExecutionSummary.md) objects

 ** [nextToken](#API_ListExecutions_ResponseSyntax) **   <a name="diagnostictools-ListExecutions-response-nextToken"></a>
The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.
Type: String
Pattern: `[A-Za-z0-9\-_]*={0,3}`

## Errors
<a name="API_ListExecutions_Errors"></a>

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
<a name="API_ListExecutions_Examples"></a>

This example illustrates one usage of `ListExecutions`.

### Example
<a name="API_ListExecutions_Example_1"></a>

 **Using AWS JSON protocol (default)**

#### Sample Request
<a name="API_ListExecutions_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ts.us-east-2.amazonaws.com
X-Amz-Target: Troubleshooting.ListExecutions
Content-Type: application/x-amz-json-1.0
X-Amz-Date: <Date>
Authorization: <AuthParams>
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
{
    "maxResults": 2
}
```

#### Sample Response
<a name="API_ListExecutions_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <requestId>
Content-Length: 0
Date: <Date>
Content-Type: application/x-amz-json-1.0
{
    "nextToken": "nextTokenToRetrieveNextPage",
    "executionList": [
        {
            "creationTime": 1699927.553,
            "executionId": "e-aaaaaaaaa",
            "requestState": "SUBMITTED",
            "requesterArn": "<requester iam arn>",
            "requesterId": "<requester iam arn>",
            "roleArn": "<pass role>",
            "status": "SUCCESSFUL",
            "storageRegion": "us-east-2",
            "targetRegions": [
            "us-east-1"
            ],
            "toolId": "EC2SystemsManager",
            "toolVersionId": "1.0.0"
        },
        {
            "creationTime": 1699927.553,
            "executionId": "e-bbbbbbbb",
            "requestState": "SUBMITTED",
            "requesterArn": "<requester iam arn>",
            "requesterId": "<requester iam arn>",
            "roleArn": "<pass role>",
            "status": "SUCCESSFUL",
            "storageRegion": "us-east-1",
            "targetRegions": [
            "us-west-2"
            ],
            "toolId": "EC2SystemsManager",
            "toolVersionId": "1.0.1"
        }
    ]
}
```

## See Also
<a name="API_ListExecutions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/troubleshooting-2023-01-01/ListExecutions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/troubleshooting-2023-01-01/ListExecutions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/troubleshooting-2023-01-01/ListExecutions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/troubleshooting-2023-01-01/ListExecutions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/troubleshooting-2023-01-01/ListExecutions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/troubleshooting-2023-01-01/ListExecutions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/troubleshooting-2023-01-01/ListExecutions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/troubleshooting-2023-01-01/ListExecutions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/troubleshooting-2023-01-01/ListExecutions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/troubleshooting-2023-01-01/ListExecutions)
