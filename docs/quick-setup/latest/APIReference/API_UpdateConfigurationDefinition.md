---
source_url: https://docs.aws.amazon.com/quick-setup/latest/APIReference/API_UpdateConfigurationDefinition.html
---

# UpdateConfigurationDefinition
<a name="API_UpdateConfigurationDefinition"></a>

Updates a Quick Setup configuration definition.

## Request Syntax
<a name="API_UpdateConfigurationDefinition_RequestSyntax"></a>

```
PUT /configurationDefinition/{{ManagerArn}}/{{Id}} HTTP/1.1
Content-type: application/json

{
   "LocalDeploymentAdministrationRoleArn": "{{string}}",
   "LocalDeploymentExecutionRoleName": "{{string}}",
   "Parameters": {
      "{{string}}" : "{{string}}"
   },
   "TypeVersion": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateConfigurationDefinition_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Id](#API_UpdateConfigurationDefinition_RequestSyntax) **   <a name="quicksetup-UpdateConfigurationDefinition-request-uri-Id"></a>
The ID of the configuration definition you want to update.
Pattern: `[a-z0-9-]{1,20}`
Required: Yes

 ** [ManagerArn](#API_UpdateConfigurationDefinition_RequestSyntax) **   <a name="quicksetup-UpdateConfigurationDefinition-request-uri-ManagerArn"></a>
The ARN of the configuration manager associated with the definition to update.
Pattern: `arn:aws(-cn|-us-gov)?:ssm-quicksetup:([^:]+):(\d{12}):configuration-manager/[0-9a-fA-F]{8}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{12}`
Required: Yes

## Request Body
<a name="API_UpdateConfigurationDefinition_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [LocalDeploymentAdministrationRoleArn](#API_UpdateConfigurationDefinition_RequestSyntax) **   <a name="quicksetup-UpdateConfigurationDefinition-request-LocalDeploymentAdministrationRoleArn"></a>
The ARN of the IAM role used to administrate local configuration deployments.
Although this element is listed as "Required: No", a value can be omitted only for organizational deployments of types other than `AWSQuickSetupType-PatchPolicy`. A value must be provided when you are running an organizational deployment for a patch policy or running any type of deployment for a single account.
Type: String
Pattern: `arn:aws(-cn|-us-gov)?:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+.*`
Required: No

 ** [LocalDeploymentExecutionRoleName](#API_UpdateConfigurationDefinition_RequestSyntax) **   <a name="quicksetup-UpdateConfigurationDefinition-request-LocalDeploymentExecutionRoleName"></a>
The name of the IAM role used to deploy local configurations.
Although this element is listed as "Required: No", a value can be omitted only for organizational deployments of types other than `AWSQuickSetupType-PatchPolicy`. A value must be provided when you are running an organizational deployment for a patch policy or running any type of deployment for a single account.
Type: String
Pattern: `([\w+=,.@\/-]{1,512}\/)?[\w+=,.@-]{1,64}`
Required: No

 ** [Parameters](#API_UpdateConfigurationDefinition_RequestSyntax) **   <a name="quicksetup-UpdateConfigurationDefinition-request-Parameters"></a>
The parameters for the configuration definition type.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 256.
Key Pattern: `[A-Za-z0-9+=@_\/\s-]+`
Value Length Constraints: Minimum length of 0. Maximum length of 40960.
Required: No

 ** [TypeVersion](#API_UpdateConfigurationDefinition_RequestSyntax) **   <a name="quicksetup-UpdateConfigurationDefinition-request-TypeVersion"></a>
The version of the Quick Setup type to use.
Type: String
Pattern: `\d{1,3}(\.\d{1,3})?$|^LATEST`
Required: No

## Response Syntax
<a name="API_UpdateConfigurationDefinition_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateConfigurationDefinition_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateConfigurationDefinition_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The requester has insufficient permissions to perform the operation.
HTTP Status Code: 403

 ** ConflictException **
Another request is being processed. Wait a few minutes and try again.
HTTP Status Code: 409

 ** InternalServerException **
An error occurred on the server side.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource couldn't be found. Check the ID or name and try again.
HTTP Status Code: 404

 ** ThrottlingException **
The request or operation exceeds the maximum allowed request rate per AWS account and AWS Region.
HTTP Status Code: 429

 ** ValidationException **
The request is invalid. Verify the values provided for the request parameters are accurate.
HTTP Status Code: 400

## See Also
<a name="API_UpdateConfigurationDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-quicksetup-2018-05-10/UpdateConfigurationDefinition)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-quicksetup-2018-05-10/UpdateConfigurationDefinition)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-quicksetup-2018-05-10/UpdateConfigurationDefinition)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-quicksetup-2018-05-10/UpdateConfigurationDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-quicksetup-2018-05-10/UpdateConfigurationDefinition)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-quicksetup-2018-05-10/UpdateConfigurationDefinition)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-quicksetup-2018-05-10/UpdateConfigurationDefinition)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-quicksetup-2018-05-10/UpdateConfigurationDefinition)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-quicksetup-2018-05-10/UpdateConfigurationDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-quicksetup-2018-05-10/UpdateConfigurationDefinition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Quick Setup. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quick-setup` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
