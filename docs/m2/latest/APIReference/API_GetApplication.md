---
source_url: https://docs.aws.amazon.com/m2/latest/APIReference/API_GetApplication.html
---

# GetApplication
<a name="API_GetApplication"></a>

**Important**
 AWS Mainframe Modernization Service (Managed Runtime Environment experience) will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html).

Describes the details of a specific application.

## Request Syntax
<a name="API_GetApplication_RequestSyntax"></a>

```
GET /applications/{{applicationId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetApplication_RequestParameters"></a>

The request uses the following URI parameters.

 ** [applicationId](#API_GetApplication_RequestSyntax) **   <a name="m2-GetApplication-request-uri-applicationId"></a>
The identifier of the application.
Pattern: `\S{1,80}`
Required: Yes

## Request Body
<a name="API_GetApplication_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetApplication_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "applicationArn": "string",
   "applicationId": "string",
   "creationTime": number,
   "deployedVersion": {
      "applicationVersion": number,
      "status": "string",
      "statusReason": "string"
   },
   "description": "string",
   "engineType": "string",
   "environmentId": "string",
   "kmsKeyId": "string",
   "lastStartTime": number,
   "latestVersion": {
      "applicationVersion": number,
      "creationTime": number,
      "status": "string",
      "statusReason": "string"
   },
   "listenerArns": [ "string" ],
   "listenerPorts": [ number ],
   "loadBalancerDnsName": "string",
   "logGroups": [
      {
         "logGroupName": "string",
         "logType": "string"
      }
   ],
   "name": "string",
   "roleArn": "string",
   "status": "string",
   "statusReason": "string",
   "tags": {
      "string" : "string"
   },
   "targetGroupArns": [ "string" ]
}
```

## Response Elements
<a name="API_GetApplication_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [applicationArn](#API_GetApplication_ResponseSyntax) **   <a name="m2-GetApplication-response-applicationArn"></a>
The Amazon Resource Name (ARN) of the application.
Type: String
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]|):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+=,@.-]{0,1023}`

 ** [applicationId](#API_GetApplication_ResponseSyntax) **   <a name="m2-GetApplication-response-applicationId"></a>
The identifier of the application.
Type: String
Pattern: `\S{1,80}`

 ** [creationTime](#API_GetApplication_ResponseSyntax) **   <a name="m2-GetApplication-response-creationTime"></a>
The timestamp when this application was created.
Type: Timestamp

 ** [deployedVersion](#API_GetApplication_ResponseSyntax) **   <a name="m2-GetApplication-response-deployedVersion"></a>
The version of the application that is deployed.
Type: [DeployedVersionSummary](API_DeployedVersionSummary.md) object

 ** [description](#API_GetApplication_ResponseSyntax) **   <a name="m2-GetApplication-response-description"></a>
The description of the application.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.

 ** [engineType](#API_GetApplication_ResponseSyntax) **   <a name="m2-GetApplication-response-engineType"></a>
The type of the target platform for the application.
Type: String
Valid Values: `microfocus | bluage`

 ** [environmentId](#API_GetApplication_ResponseSyntax) **   <a name="m2-GetApplication-response-environmentId"></a>
The identifier of the runtime environment where you want to deploy the application.
Type: String
Pattern: `\S{1,80}`

 ** [kmsKeyId](#API_GetApplication_ResponseSyntax) **   <a name="m2-GetApplication-response-kmsKeyId"></a>
The identifier of a customer managed key.
Type: String

 ** [lastStartTime](#API_GetApplication_ResponseSyntax) **   <a name="m2-GetApplication-response-lastStartTime"></a>
The timestamp when you last started the application. Null until the application runs for the first time.
Type: Timestamp

 ** [latestVersion](#API_GetApplication_ResponseSyntax) **   <a name="m2-GetApplication-response-latestVersion"></a>
The latest version of the application.
Type: [ApplicationVersionSummary](API_ApplicationVersionSummary.md) object

 ** [listenerArns](#API_GetApplication_ResponseSyntax) **   <a name="m2-GetApplication-response-listenerArns"></a>
The Amazon Resource Name (ARN) for the network load balancer listener created in your AWS account. AWS Mainframe Modernization creates this listener for you the first time you deploy an application.
Type: Array of strings
Array Members: Minimum number of 1 item.
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]|):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+=,@.-]{0,1023}`

 ** [listenerPorts](#API_GetApplication_ResponseSyntax) **   <a name="m2-GetApplication-response-listenerPorts"></a>
The port associated with the network load balancer listener created in your AWS account.
Type: Array of integers
Array Members: Minimum number of 1 item.

 ** [loadBalancerDnsName](#API_GetApplication_ResponseSyntax) **   <a name="m2-GetApplication-response-loadBalancerDnsName"></a>
The public DNS name of the load balancer created in your AWS account.
Type: String
Pattern: `\S{1,100}`

 ** [logGroups](#API_GetApplication_ResponseSyntax) **   <a name="m2-GetApplication-response-logGroups"></a>
The list of log summaries. Each log summary includes the log type as well as the log group identifier. These are CloudWatch logs. AWS Mainframe Modernization pushes the application log to CloudWatch under the customer's account.
Type: Array of [LogGroupSummary](API_LogGroupSummary.md) objects

 ** [name](#API_GetApplication_ResponseSyntax) **   <a name="m2-GetApplication-response-name"></a>
The unique identifier of the application.
Type: String
Pattern: `[A-Za-z0-9][A-Za-z0-9_\-]{1,59}`

 ** [roleArn](#API_GetApplication_ResponseSyntax) **   <a name="m2-GetApplication-response-roleArn"></a>
The Amazon Resource Name (ARN) of the role associated with the application.
Type: String
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]|):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+=,@.-]{0,1023}`

 ** [status](#API_GetApplication_ResponseSyntax) **   <a name="m2-GetApplication-response-status"></a>
The status of the application.
Type: String
Valid Values: `Creating | Created | Available | Ready | Starting | Running | Stopping | Stopped | Failed | Deleting | Deleting From Environment`

 ** [statusReason](#API_GetApplication_ResponseSyntax) **   <a name="m2-GetApplication-response-statusReason"></a>
The reason for the reported status.
Type: String

 ** [tags](#API_GetApplication_ResponseSyntax) **   <a name="m2-GetApplication-response-tags"></a>
A list of tags associated with the application.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:).+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [targetGroupArns](#API_GetApplication_ResponseSyntax) **   <a name="m2-GetApplication-response-targetGroupArns"></a>
Returns the Amazon Resource Names (ARNs) of the target groups that are attached to the network load balancer.
Type: Array of strings
Array Members: Minimum number of 1 item.
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]|):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+=,@.-]{0,1023}`

## Errors
<a name="API_GetApplication_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The account or role doesn't have the right permissions to make the request.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error occurred during the processing of the request.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource was not found.
 ** resourceId **
The ID of the missing resource.
 ** resourceType **
The type of the missing resource.
HTTP Status Code: 404

 ** ThrottlingException **
The number of requests made exceeds the limit.
 ** quotaCode **
The identifier of the throttled request.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
 ** serviceCode **
The identifier of the service that the throttled request was made to.
HTTP Status Code: 429

 ** ValidationException **
One or more parameters provided in the request is not valid.
 ** fieldList **
The list of fields that failed service validation.
 ** reason **
The reason why it failed service validation.
HTTP Status Code: 400

## See Also
<a name="API_GetApplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/m2-2021-04-28/GetApplication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/m2-2021-04-28/GetApplication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/m2-2021-04-28/GetApplication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/m2-2021-04-28/GetApplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/m2-2021-04-28/GetApplication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/m2-2021-04-28/GetApplication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/m2-2021-04-28/GetApplication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/m2-2021-04-28/GetApplication)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/m2-2021-04-28/GetApplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/m2-2021-04-28/GetApplication)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Mainframe Modernization. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query m2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
