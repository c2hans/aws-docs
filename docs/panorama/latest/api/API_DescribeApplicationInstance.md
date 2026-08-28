---
source_url: https://docs.aws.amazon.com/panorama/latest/api/API_DescribeApplicationInstance.html
---

# DescribeApplicationInstance
<a name="API_DescribeApplicationInstance"></a>

**Important**
End of support notice: On May 31, 2026, AWS will end support for AWS Panorama. After May 31, 2026, you will no longer be able to access the AWS Panorama console or AWS Panorama resources. For more information, see [AWS Panorama end of support](https://docs.aws.amazon.com/panorama/latest/dev/panorama-end-of-support.html).

Returns information about an application instance on a device.

## Request Syntax
<a name="API_DescribeApplicationInstance_RequestSyntax"></a>

```
GET /application-instances/{{ApplicationInstanceId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeApplicationInstance_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ApplicationInstanceId](#API_DescribeApplicationInstance_RequestSyntax) **   <a name="panorama-DescribeApplicationInstance-request-uri-ApplicationInstanceId"></a>
The application instance's ID.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\-\_]+`
Required: Yes

## Request Body
<a name="API_DescribeApplicationInstance_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeApplicationInstance_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ApplicationInstanceId": "string",
   "ApplicationInstanceIdToReplace": "string",
   "Arn": "string",
   "CreatedTime": number,
   "DefaultRuntimeContextDevice": "string",
   "DefaultRuntimeContextDeviceName": "string",
   "Description": "string",
   "HealthStatus": "string",
   "LastUpdatedTime": number,
   "Name": "string",
   "RuntimeContextStates": [
      {
         "DesiredState": "string",
         "DeviceReportedStatus": "string",
         "DeviceReportedTime": number,
         "RuntimeContextName": "string"
      }
   ],
   "RuntimeRoleArn": "string",
   "Status": "string",
   "StatusDescription": "string",
   "Tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_DescribeApplicationInstance_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ApplicationInstanceId](#API_DescribeApplicationInstance_ResponseSyntax) **   <a name="panorama-DescribeApplicationInstance-response-ApplicationInstanceId"></a>
The application instance's ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\-\_]+`

 ** [ApplicationInstanceIdToReplace](#API_DescribeApplicationInstance_ResponseSyntax) **   <a name="panorama-DescribeApplicationInstance-response-ApplicationInstanceIdToReplace"></a>
The ID of the application instance that this instance replaced.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\-\_]+`

 ** [Arn](#API_DescribeApplicationInstance_ResponseSyntax) **   <a name="panorama-DescribeApplicationInstance-response-Arn"></a>
The application instance's ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [CreatedTime](#API_DescribeApplicationInstance_ResponseSyntax) **   <a name="panorama-DescribeApplicationInstance-response-CreatedTime"></a>
When the application instance was created.
Type: Timestamp

 ** [DefaultRuntimeContextDevice](#API_DescribeApplicationInstance_ResponseSyntax) **   <a name="panorama-DescribeApplicationInstance-response-DefaultRuntimeContextDevice"></a>
The device's ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\-\_]+`

 ** [DefaultRuntimeContextDeviceName](#API_DescribeApplicationInstance_ResponseSyntax) **   <a name="panorama-DescribeApplicationInstance-response-DefaultRuntimeContextDeviceName"></a>
The device's bane.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\-\_]+`

 ** [Description](#API_DescribeApplicationInstance_ResponseSyntax) **   <a name="panorama-DescribeApplicationInstance-response-Description"></a>
The application instance's description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `.*`

 ** [HealthStatus](#API_DescribeApplicationInstance_ResponseSyntax) **   <a name="panorama-DescribeApplicationInstance-response-HealthStatus"></a>
The application instance's health status.
Type: String
Valid Values: `RUNNING | ERROR | NOT_AVAILABLE`

 ** [LastUpdatedTime](#API_DescribeApplicationInstance_ResponseSyntax) **   <a name="panorama-DescribeApplicationInstance-response-LastUpdatedTime"></a>
The application instance was updated.
Type: Timestamp

 ** [Name](#API_DescribeApplicationInstance_ResponseSyntax) **   <a name="panorama-DescribeApplicationInstance-response-Name"></a>
The application instance's name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\-\_]+`

 ** [RuntimeContextStates](#API_DescribeApplicationInstance_ResponseSyntax) **   <a name="panorama-DescribeApplicationInstance-response-RuntimeContextStates"></a>
The application instance's state.
Type: Array of [ReportedRuntimeContextState](API_ReportedRuntimeContextState.md) objects

 ** [RuntimeRoleArn](#API_DescribeApplicationInstance_ResponseSyntax) **   <a name="panorama-DescribeApplicationInstance-response-RuntimeRoleArn"></a>
The application instance's runtime role ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `arn:[a-z0-9][-.a-z0-9]{0,62}:iam::[0-9]{12}:role/.+`

 ** [Status](#API_DescribeApplicationInstance_ResponseSyntax) **   <a name="panorama-DescribeApplicationInstance-response-Status"></a>
The application instance's status.
Type: String
Valid Values: `DEPLOYMENT_PENDING | DEPLOYMENT_REQUESTED | DEPLOYMENT_IN_PROGRESS | DEPLOYMENT_ERROR | DEPLOYMENT_SUCCEEDED | REMOVAL_PENDING | REMOVAL_REQUESTED | REMOVAL_IN_PROGRESS | REMOVAL_FAILED | REMOVAL_SUCCEEDED | DEPLOYMENT_FAILED`

 ** [StatusDescription](#API_DescribeApplicationInstance_ResponseSyntax) **   <a name="panorama-DescribeApplicationInstance-response-StatusDescription"></a>
The application instance's status description.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [Tags](#API_DescribeApplicationInstance_ResponseSyntax) **   <a name="panorama-DescribeApplicationInstance-response-Tags"></a>
The application instance's tags.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `.+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `.*`

## Errors
<a name="API_DescribeApplicationInstance_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The requestor does not have permission to access the target action or resource.
HTTP Status Code: 403

 ** ConflictException **
The target resource is in use.
 ** ErrorArguments **
A list of attributes that led to the exception and their values.
 ** ErrorId **
A unique ID for the error.
 ** ResourceId **
The resource's ID.
 ** ResourceType **
The resource's type.
HTTP Status Code: 409

 ** InternalServerException **
An internal error occurred.
 ** RetryAfterSeconds **
The number of seconds a client should wait before retrying the call.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The target resource was not found.
 ** ResourceId **
The resource's ID.
 ** ResourceType **
The resource's type.
HTTP Status Code: 404

 ** ValidationException **
The request contains an invalid parameter value.
 ** ErrorArguments **
A list of attributes that led to the exception and their values.
 ** ErrorId **
A unique ID for the error.
 ** Fields **
A list of request parameters that failed validation.
 ** Reason **
The reason that validation failed.
HTTP Status Code: 400

## See Also
<a name="API_DescribeApplicationInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/panorama-2019-07-24/DescribeApplicationInstance)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/panorama-2019-07-24/DescribeApplicationInstance)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/panorama-2019-07-24/DescribeApplicationInstance)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/panorama-2019-07-24/DescribeApplicationInstance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/panorama-2019-07-24/DescribeApplicationInstance)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/panorama-2019-07-24/DescribeApplicationInstance)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/panorama-2019-07-24/DescribeApplicationInstance)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/panorama-2019-07-24/DescribeApplicationInstance)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/panorama-2019-07-24/DescribeApplicationInstance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/panorama-2019-07-24/DescribeApplicationInstance)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Panorama. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query panorama` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
