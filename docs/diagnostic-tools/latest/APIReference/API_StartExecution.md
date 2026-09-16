---
source_url: https://docs.aws.amazon.com/diagnostic-tools/latest/APIReference/API_StartExecution.html
---

# StartExecution
<a name="API_StartExecution"></a>

Triggers new execution of a specific tool.

## Request Syntax
<a name="API_StartExecution_RequestSyntax"></a>

```
{
   "executionParameters": "{{string}}",
   "roleArn": "{{string}}",
   "storageRegion": "{{string}}",
   "tags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ],
   "targetRegions": [ "{{string}}" ],
   "toolId": "{{string}}",
   "toolVersionId": "{{string}}"
}
```

## Request Parameters
<a name="API_StartExecution_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [executionParameters](#API_StartExecution_RequestSyntax) **   <a name="diagnostictools-StartExecution-request-executionParameters"></a>
Tool Execution Parameter.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 32764.
Required: No

 ** [roleArn](#API_StartExecution_RequestSyntax) **   <a name="diagnostictools-StartExecution-request-roleArn"></a>
ARN of Service Role passed which will be used to execute Diagnostic Tool
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws[a-z0-9-]*:iam::\d{12}:role\/[\w\-\/.@+=,]{1,65}`
Required: Yes

 ** [storageRegion](#API_StartExecution_RequestSyntax) **   <a name="diagnostictools-StartExecution-request-storageRegion"></a>
Select AWS Region where you want to store execution output from available options
Type: String
Valid Values: `us-east-2 | us-west-2 | eu-west-1`
Required: Yes

 ** [tags](#API_StartExecution_RequestSyntax) **   <a name="diagnostictools-StartExecution-request-tags"></a>
Optional metadata that you assign to a resource. You can specify a maximum of five tags for an execution. Tags enable you to categorize a resource in different ways, such as by purpose, owner, or environment.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

 ** [targetRegions](#API_StartExecution_RequestSyntax) **   <a name="diagnostictools-StartExecution-request-targetRegions"></a>
List of AWS Region Diagnostic Tool service allowed to query AWS Services during tool execution
Type: Array of strings
Required: Yes

 ** [toolId](#API_StartExecution_RequestSyntax) **   <a name="diagnostictools-StartExecution-request-toolId"></a>
Unique-id of Diagnostic Tool which you want to execute
Type: String
Length Constraints: Minimum length of 8. Maximum length of 64.
Pattern: `\w+`
Required: Yes

 ** [toolVersionId](#API_StartExecution_RequestSyntax) **   <a name="diagnostictools-StartExecution-request-toolVersionId"></a>
Associate Version id for tool which you to execution
Type: String
Length Constraints: Minimum length of 5. Maximum length of 17.
Pattern: `[0-9]{1,5}.[0-9]{1,5}.[0-9]{1,5}`
Required: No

## Response Syntax
<a name="API_StartExecution_ResponseSyntax"></a>

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
<a name="API_StartExecution_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [execution](#API_StartExecution_ResponseSyntax) **   <a name="diagnostictools-StartExecution-response-execution"></a>
Execution Information Metadata
Type: [Execution](API_Execution.md) object

## Errors
<a name="API_StartExecution_Errors"></a>

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

 ** ServiceQuotaExceededException **
The request failed because it would cause a service quota to be exceeded.
 ** message **
Failure message.
 ** quotaCode **
The quota code recognized by the AWS Service Quotas service.
 ** resourceId **
The unique ID of the resource referenced in the failed request.
 ** resourceType **
The resource type of the resource referenced in the failed request.
 ** serviceCode **
The code for the AWS-service; that owns the quota.
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
<a name="API_StartExecution_Examples"></a>

This example illustrates one usage of `StartExecution`.

### Example
<a name="API_StartExecution_Example_1"></a>

 **Using AWS JSON protocol (default)**

#### Sample Request
<a name="API_StartExecution_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ts.us-east-2.amazonaws.com
X-Amz-Target: Troubleshooting.StartExecution
Content-Type: application/x-amz-json-1.0
X-Amz-Date: <Date>
Authorization: <AuthParams>
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
{
    "toolId": "EC2SystemsManager",
    "toolVersionId": "1.0.0",
    "roleArn": "<sample role>",
    "targetRegions": [
        "us-east-1"
    ],
    "storageRegion": "us-east-2",
    "parameters": {"apis":[true,true,true,false,false,false,false,false]}
}
```

#### Sample Response
<a name="API_StartExecution_Example_1_Response"></a>

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
<a name="API_StartExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/troubleshooting-2023-01-01/StartExecution)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/troubleshooting-2023-01-01/StartExecution)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/troubleshooting-2023-01-01/StartExecution)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/troubleshooting-2023-01-01/StartExecution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/troubleshooting-2023-01-01/StartExecution)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/troubleshooting-2023-01-01/StartExecution)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/troubleshooting-2023-01-01/StartExecution)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/troubleshooting-2023-01-01/StartExecution)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/troubleshooting-2023-01-01/StartExecution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/troubleshooting-2023-01-01/StartExecution)
