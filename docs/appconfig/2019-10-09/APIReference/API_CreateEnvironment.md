---
source_url: https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_CreateEnvironment.html
---

# CreateEnvironment
<a name="API_CreateEnvironment"></a>

Creates an environment. For each application, you define one or more environments. An environment is a deployment group of AWS AppConfig targets, such as applications in a `Beta` or `Production` environment. You can also define environments for application subcomponents such as the `Web`, `Mobile` and `Back-end` components for your application. You can configure Amazon CloudWatch alarms for each environment. The system monitors alarms during a configuration deployment. If an alarm is triggered, the system rolls back the configuration.

## Request Syntax
<a name="API_CreateEnvironment_RequestSyntax"></a>

```
POST /applications/{{ApplicationId}}/environments HTTP/1.1
Content-type: application/json

{
   "Description": "{{string}}",
   "Monitors": [
      {
         "AlarmArn": "{{string}}",
         "AlarmRoleArn": "{{string}}"
      }
   ],
   "Name": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateEnvironment_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ApplicationId](#API_CreateEnvironment_RequestSyntax) **   <a name="appconfig-CreateEnvironment-request-uri-ApplicationId"></a>
The ID or name of the application.
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

## Request Body
<a name="API_CreateEnvironment_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Description](#API_CreateEnvironment_RequestSyntax) **   <a name="appconfig-CreateEnvironment-request-Description"></a>
A description of the environment.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** [Monitors](#API_CreateEnvironment_RequestSyntax) **   <a name="appconfig-CreateEnvironment-request-Monitors"></a>
Amazon CloudWatch alarms to monitor during the deployment process.
Type: Array of [Monitor](API_Monitor.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Required: No

 ** [Name](#API_CreateEnvironment_RequestSyntax) **   <a name="appconfig-CreateEnvironment-request-Name"></a>
A name for the environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** [Tags](#API_CreateEnvironment_RequestSyntax) **   <a name="appconfig-CreateEnvironment-request-Tags"></a>
Metadata to assign to the environment. Tags help organize and categorize your AWS AppConfig resources. Each tag consists of a key and an optional value, both of which you define.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateEnvironment_ResponseSyntax"></a>

```
HTTP/1.1 201
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
<a name="API_CreateEnvironment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [ApplicationId](#API_CreateEnvironment_ResponseSyntax) **   <a name="appconfig-CreateEnvironment-response-ApplicationId"></a>
The application ID.
Type: String
Pattern: `[a-z0-9]{4,7}`

 ** [Description](#API_CreateEnvironment_ResponseSyntax) **   <a name="appconfig-CreateEnvironment-response-Description"></a>
The description of the environment.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [Id](#API_CreateEnvironment_ResponseSyntax) **   <a name="appconfig-CreateEnvironment-response-Id"></a>
The environment ID.
Type: String
Pattern: `[a-z0-9]{4,7}`

 ** [Monitors](#API_CreateEnvironment_ResponseSyntax) **   <a name="appconfig-CreateEnvironment-response-Monitors"></a>
Amazon CloudWatch alarms monitored during the deployment.
Type: Array of [Monitor](API_Monitor.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.

 ** [Name](#API_CreateEnvironment_ResponseSyntax) **   <a name="appconfig-CreateEnvironment-response-Name"></a>
The name of the environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [State](#API_CreateEnvironment_ResponseSyntax) **   <a name="appconfig-CreateEnvironment-response-State"></a>
The state of the environment. An environment can be in one of the following states: `READY_FOR_DEPLOYMENT`, `DEPLOYING`, `ROLLING_BACK`, or `ROLLED_BACK`
Type: String
Valid Values: `READY_FOR_DEPLOYMENT | DEPLOYING | ROLLING_BACK | ROLLED_BACK | REVERTED`

## Errors
<a name="API_CreateEnvironment_Errors"></a>

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

 ** ServiceQuotaExceededException **
The number of one more AWS AppConfig resources exceeds the maximum allowed. Verify that your environment doesn't exceed the following service quotas:
Applications: 100 max
To resolve this issue, you can delete one or more resources and try again. Or, you can request a quota increase. For more information about quotas and to request an increase, see [Service quotas for AWS AppConfig](https://docs.aws.amazon.com/general/latest/gr/appconfig.html#limits_appconfig) in the Amazon Web Services General Reference.
HTTP Status Code: 402

## Examples
<a name="API_CreateEnvironment_Examples"></a>

### Example
<a name="API_CreateEnvironment_Example_1"></a>

This example illustrates one usage of CreateEnvironment.

#### Sample Request
<a name="API_CreateEnvironment_Example_1_Request"></a>

```
POST /applications/abc1234/environments HTTP/1.1
Host: appconfig.us-east-1.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/2.2.4 Python/3.8.8 Linux/5.4.134-73.228.amzn2int.x86_64 exe/x86_64.amzn.2 prompt/off command/appconfig.create-environment
X-Amz-Date: 20210916T221023Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20210916/us-east-1/appconfig/aws4_request, SignedHeaders=host;x-amz-date, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 31

{
	"Name": "Example-Environment"
}
```

#### Sample Response
<a name="API_CreateEnvironment_Example_1_Response"></a>

```
{
	"ApplicationId": "abc1234",
	"Description": null,
	"Id": "54j1r29",
	"Monitors": null,
	"Name": "Example-Environment",
	"State": "ReadyForDeployment"
}
```

## See Also
<a name="API_CreateEnvironment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appconfig-2019-10-09/CreateEnvironment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appconfig-2019-10-09/CreateEnvironment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appconfig-2019-10-09/CreateEnvironment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appconfig-2019-10-09/CreateEnvironment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appconfig-2019-10-09/CreateEnvironment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appconfig-2019-10-09/CreateEnvironment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appconfig-2019-10-09/CreateEnvironment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appconfig-2019-10-09/CreateEnvironment)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appconfig-2019-10-09/CreateEnvironment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appconfig-2019-10-09/CreateEnvironment)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS AppConfig. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appconfig` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
