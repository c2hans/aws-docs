---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeTask.html
---

# DescribeTask
<a name="API_DescribeTask"></a>

Retrieves detailed information about a specific task in a workspace.

## Request Syntax
<a name="API_DescribeTask_RequestSyntax"></a>

```
GET /workspaces/{{workspaceName}}/tasks/{{taskName}}?version={{taskVersion}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeTask_RequestParameters"></a>

The request uses the following URI parameters.

 ** [taskName](#API_DescribeTask_RequestSyntax) **   <a name="iotsitewise-DescribeTask-request-uri-taskName"></a>
The name of the task.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** [taskVersion](#API_DescribeTask_RequestSyntax) **   <a name="iotsitewise-DescribeTask-request-uri-taskVersion"></a>
The version number of the task to retrieve. If not specified, returns the latest version.
Length Constraints: Minimum length of 1. Maximum length of 10.
Pattern: `^(0|([1-9]{1}\d*))$`

 ** [workspaceName](#API_DescribeTask_RequestSyntax) **   <a name="iotsitewise-DescribeTask-request-uri-workspaceName"></a>
The name of the workspace.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

## Request Body
<a name="API_DescribeTask_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeTask_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "createdAt": number,
   "description": "string",
   "status": {
      "error": {
         "code": "string",
         "message": "string"
      },
      "state": "string"
   },
   "taskArn": "string",
   "taskConfiguration": { ... },
   "taskName": "string",
   "updatedAt": number,
   "version": "string",
   "workspaceName": "string"
}
```

## Response Elements
<a name="API_DescribeTask_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_DescribeTask_ResponseSyntax) **   <a name="iotsitewise-DescribeTask-response-createdAt"></a>
The time the task was created, in Unix epoch time.
Type: Timestamp

 ** [description](#API_DescribeTask_ResponseSyntax) **   <a name="iotsitewise-DescribeTask-response-description"></a>
The description of the task.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\u0000-\u001F\u007F]+`

 ** [status](#API_DescribeTask_ResponseSyntax) **   <a name="iotsitewise-DescribeTask-response-status"></a>
The current lifecycle status of the task.
Type: [ResourceStatus](API_ResourceStatus.md) object

 ** [taskArn](#API_DescribeTask_ResponseSyntax) **   <a name="iotsitewise-DescribeTask-response-taskArn"></a>
The ARN of the task.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws(-cn|-us-gov)?:[a-zA-Z0-9-:\/_\.]+$`

 ** [taskConfiguration](#API_DescribeTask_ResponseSyntax) **   <a name="iotsitewise-DescribeTask-response-taskConfiguration"></a>
The task execution configuration. Contains a [containerTaskConfiguration](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ContainerTaskConfiguration.html) for custom container workloads.
Type: [TaskConfiguration](API_TaskConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [taskName](#API_DescribeTask_ResponseSyntax) **   <a name="iotsitewise-DescribeTask-response-taskName"></a>
The name of the task.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`

 ** [updatedAt](#API_DescribeTask_ResponseSyntax) **   <a name="iotsitewise-DescribeTask-response-updatedAt"></a>
The time the task was last updated, in Unix epoch time.
Type: Timestamp

 ** [version](#API_DescribeTask_ResponseSyntax) **   <a name="iotsitewise-DescribeTask-response-version"></a>
The version of the task.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10.
Pattern: `^(0|([1-9]{1}\d*))$`

 ** [workspaceName](#API_DescribeTask_ResponseSyntax) **   <a name="iotsitewise-DescribeTask-response-workspaceName"></a>
The name of the workspace.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`

## Errors
<a name="API_DescribeTask_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access is denied.
HTTP Status Code: 403

 ** InternalFailureException **
 AWS IoT SiteWise can't process your request right now. Try again later.
HTTP Status Code: 500

 ** InvalidRequestException **
The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The requested resource can't be found.
HTTP Status Code: 404

 ** ThrottlingException **
Your request exceeded a rate limit. For example, you might have exceeded the number of AWS IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.
For more information, see [Quotas](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html) in the * AWS IoT SiteWise User Guide*.
HTTP Status Code: 429

## See Also
<a name="API_DescribeTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotsitewise-2019-12-02/DescribeTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotsitewise-2019-12-02/DescribeTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/DescribeTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotsitewise-2019-12-02/DescribeTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/DescribeTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotsitewise-2019-12-02/DescribeTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotsitewise-2019-12-02/DescribeTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotsitewise-2019-12-02/DescribeTask)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotsitewise-2019-12-02/DescribeTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/DescribeTask)
