---
source_url: https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_UpdateEnvironment.html
---

# UpdateEnvironment
<a name="API_UpdateEnvironment"></a>

Updates an environment.

## Request Syntax
<a name="API_UpdateEnvironment_RequestSyntax"></a>

```
PATCH /applications/{{ApplicationId}}/environments/{{EnvironmentId}} HTTP/1.1
Content-type: application/json

{
   "Description": "{{string}}",
   "Monitors": [
      {
         "AlarmArn": "{{string}}",
         "AlarmRoleArn": "{{string}}"
      }
   ],
   "Name": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateEnvironment_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ApplicationId](#API_UpdateEnvironment_RequestSyntax) **   <a name="appconfig-UpdateEnvironment-request-uri-ApplicationId"></a>
The ID or name of the application.
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** [EnvironmentId](#API_UpdateEnvironment_RequestSyntax) **   <a name="appconfig-UpdateEnvironment-request-uri-EnvironmentId"></a>
The ID or name of the environment.
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

## Request Body
<a name="API_UpdateEnvironment_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Description](#API_UpdateEnvironment_RequestSyntax) **   <a name="appconfig-UpdateEnvironment-request-Description"></a>
A description of the environment.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** [Monitors](#API_UpdateEnvironment_RequestSyntax) **   <a name="appconfig-UpdateEnvironment-request-Monitors"></a>
Amazon CloudWatch alarms to monitor during the deployment process.
Type: Array of [Monitor](API_Monitor.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Required: No

 ** [Name](#API_UpdateEnvironment_RequestSyntax) **   <a name="appconfig-UpdateEnvironment-request-Name"></a>
The name of the environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

## Response Syntax
<a name="API_UpdateEnvironment_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ApplicationId": "string",
   "Description": "string",
   "Id": "string",
   "Monitors": [
      {
         "AlarmArn": "string",
         "AlarmRoleArn": "string"
      }
   ],
   "Name": "string",
   "State": "string"
}
```

## Response Elements
<a name="API_UpdateEnvironment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ApplicationId](#API_UpdateEnvironment_ResponseSyntax) **   <a name="appconfig-UpdateEnvironment-response-ApplicationId"></a>
The application ID.
Type: String
Pattern: `[a-z0-9]{4,7}`

 ** [Description](#API_UpdateEnvironment_ResponseSyntax) **   <a name="appconfig-UpdateEnvironment-response-Description"></a>
The description of the environment.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [Id](#API_UpdateEnvironment_ResponseSyntax) **   <a name="appconfig-UpdateEnvironment-response-Id"></a>
The environment ID.
Type: String
Pattern: `[a-z0-9]{4,7}`

 ** [Monitors](#API_UpdateEnvironment_ResponseSyntax) **   <a name="appconfig-UpdateEnvironment-response-Monitors"></a>
Amazon CloudWatch alarms monitored during the deployment.
Type: Array of [Monitor](API_Monitor.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.

 ** [Name](#API_UpdateEnvironment_ResponseSyntax) **   <a name="appconfig-UpdateEnvironment-response-Name"></a>
The name of the environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [State](#API_UpdateEnvironment_ResponseSyntax) **   <a name="appconfig-UpdateEnvironment-response-State"></a>
The state of the environment. An environment can be in one of the following states: `READY_FOR_DEPLOYMENT`, `DEPLOYING`, `ROLLING_BACK`, or `ROLLED_BACK`
Type: String
Valid Values: `READY_FOR_DEPLOYMENT | DEPLOYING | ROLLING_BACK | ROLLED_BACK | REVERTED`

## Errors
<a name="API_UpdateEnvironment_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
The input fails to satisfy the constraints specified by an AWS service.
 ** Details **
Detailed information about the input that failed to satisfy the constraints specified by a call.
HTTP Status Code: 400

 ** InternalServerException **
There was an internal failure in the AWS AppConfig service.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested resource could not be found.
HTTP Status Code: 404

## Examples
<a name="API_UpdateEnvironment_Examples"></a>

### Example
<a name="API_UpdateEnvironment_Example_1"></a>

This example illustrates one usage of UpdateEnvironment.

#### Sample Request
<a name="API_UpdateEnvironment_Example_1_Request"></a>

```
PATCH /applications/abc1234/environments/54j1r29 HTTP/1.1
Host: appconfig.us-east-1.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/2.2.4 Python/3.8.8 Linux/5.4.134-73.228.amzn2int.x86_64 exe/x86_64.amzn.2 prompt/off command/appconfig.update-environment
X-Amz-Date: 20210920T214253Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20210920/us-east-1/appconfig/aws4_request, SignedHeaders=host;x-amz-date, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 47

{
	"Description": "An environment for examples."
}
```

#### Sample Response
<a name="API_UpdateEnvironment_Example_1_Response"></a>

```
{
    "ApplicationId": "abc1234",
    "Id": "54j1r29",
    "Name": "Example-Environment",
    "Description": "An environment for examples.",
    "State": "RolledBack"
}
```

## See Also
<a name="API_UpdateEnvironment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appconfig-2019-10-09/UpdateEnvironment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appconfig-2019-10-09/UpdateEnvironment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appconfig-2019-10-09/UpdateEnvironment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appconfig-2019-10-09/UpdateEnvironment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appconfig-2019-10-09/UpdateEnvironment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appconfig-2019-10-09/UpdateEnvironment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appconfig-2019-10-09/UpdateEnvironment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appconfig-2019-10-09/UpdateEnvironment)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/appconfig-2019-10-09/UpdateEnvironment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appconfig-2019-10-09/UpdateEnvironment)
