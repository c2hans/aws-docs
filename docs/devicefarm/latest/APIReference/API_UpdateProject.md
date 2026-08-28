---
source_url: https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_UpdateProject.html
---

# UpdateProject
<a name="API_UpdateProject"></a>

Modifies the specified project name, given the project ARN and a new name.

## Request Syntax
<a name="API_UpdateProject_RequestSyntax"></a>

```
{
   "arn": "{{string}}",
   "defaultJobTimeoutMinutes": {{number}},
   "environmentVariables": [
      {
         "name": "{{string}}",
         "value": "{{string}}"
      }
   ],
   "executionRoleArn": "{{string}}",
   "name": "{{string}}",
   "vpcConfig": {
      "securityGroupIds": [ "{{string}}" ],
      "subnetIds": [ "{{string}}" ],
      "vpcId": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_UpdateProject_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [arn](#API_UpdateProject_RequestSyntax) **   <a name="devicefarm-UpdateProject-request-arn"></a>
The Amazon Resource Name (ARN) of the project whose name to update.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 1011.
Pattern: `^arn:aws:devicefarm:.+`
Required: Yes

 ** [defaultJobTimeoutMinutes](#API_UpdateProject_RequestSyntax) **   <a name="devicefarm-UpdateProject-request-defaultJobTimeoutMinutes"></a>
The number of minutes a test run in the project executes before it times out.
Type: Integer
Required: No

 ** [environmentVariables](#API_UpdateProject_RequestSyntax) **   <a name="devicefarm-UpdateProject-request-environmentVariables"></a>
 A set of environment variables which are used by default for all runs in the project. These environment variables are applied to the test run during the execution of a test spec file.
 For more information about using test spec files, please see [Custom test environments ](https://docs.aws.amazon.com/devicefarm/latest/developerguide/custom-test-environments.html) in *AWS Device Farm.*
Type: Array of [EnvironmentVariable](API_EnvironmentVariable.md) objects
Array Members: Minimum number of 1 item. Maximum number of 32 items.
Required: No

 ** [executionRoleArn](#API_UpdateProject_RequestSyntax) **   <a name="devicefarm-UpdateProject-request-executionRoleArn"></a>
An IAM role to be assumed by the test host for all runs in the project.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^arn:aws:iam::[0-9]{12}:role/.+`
Required: No

 ** [name](#API_UpdateProject_RequestSyntax) **   <a name="devicefarm-UpdateProject-request-name"></a>
A string that represents the new name of the project that you are updating.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** [vpcConfig](#API_UpdateProject_RequestSyntax) **   <a name="devicefarm-UpdateProject-request-vpcConfig"></a>
The VPC security groups and subnets that are attached to a project.
Type: [VpcConfig](API_VpcConfig.md) object
Required: No

## Response Syntax
<a name="API_UpdateProject_ResponseSyntax"></a>

```
{
   "project": {
      "arn": "string",
      "created": number,
      "defaultJobTimeoutMinutes": number,
      "environmentVariables": [
         {
            "name": "string",
            "value": "string"
         }
      ],
      "executionRoleArn": "string",
      "name": "string",
      "vpcConfig": {
         "securityGroupIds": [ "string" ],
         "subnetIds": [ "string" ],
         "vpcId": "string"
      }
   }
}
```

## Response Elements
<a name="API_UpdateProject_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [project](#API_UpdateProject_ResponseSyntax) **   <a name="devicefarm-UpdateProject-response-project"></a>
The project to update.
Type: [Project](API_Project.md) object

## Errors
<a name="API_UpdateProject_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ArgumentException **
An invalid argument was specified.
 ** message **
Any additional information about the exception.
HTTP Status Code: 400

 ** LimitExceededException **
A limit was exceeded.
 ** message **
Any additional information about the exception.
HTTP Status Code: 400

 ** NotFoundException **
The specified entity was not found.
 ** message **
Any additional information about the exception.
HTTP Status Code: 400

 ** ServiceAccountException **
There was a problem with the service account.
 ** message **
Any additional information about the exception.
HTTP Status Code: 400

## See Also
<a name="API_UpdateProject_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/devicefarm-2015-06-23/UpdateProject)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/devicefarm-2015-06-23/UpdateProject)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devicefarm-2015-06-23/UpdateProject)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/devicefarm-2015-06-23/UpdateProject)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devicefarm-2015-06-23/UpdateProject)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/devicefarm-2015-06-23/UpdateProject)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/devicefarm-2015-06-23/UpdateProject)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/devicefarm-2015-06-23/UpdateProject)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/devicefarm-2015-06-23/UpdateProject)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devicefarm-2015-06-23/UpdateProject)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Device Farm Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devicefarm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
