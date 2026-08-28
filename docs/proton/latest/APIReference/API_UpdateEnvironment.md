---
source_url: https://docs.aws.amazon.com/proton/latest/APIReference/API_UpdateEnvironment.html
---

AWS has decided to discontinue AWS Proton, with support ending on October 7, 2026. New customers will not be able to sign up after October 7, 2025, but existing customers can continue to use the service until October 7, 2026.For more information, see [AWS Proton Service Deprecation and Migration Guide](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html).

# UpdateEnvironment
<a name="API_UpdateEnvironment"></a>

Update an environment.

If the environment is associated with an environment account connection, *don't* update or include the `protonServiceRoleArn` and `provisioningRepository` parameter to update or connect to an environment account connection.

You can only update to a new environment account connection if that connection was created in the same environment account that the current environment account connection was created in. The account connection must also be associated with the current environment.

If the environment *isn't* associated with an environment account connection, *don't* update or include the `environmentAccountConnectionId` parameter. You *can't* update or connect the environment to an environment account connection if it *isn't* already associated with an environment connection.

You can update either the `environmentAccountConnectionId` or `protonServiceRoleArn` parameter and value. You can’t update both.

If the environment was configured for AWS-managed provisioning, omit the `provisioningRepository` parameter.

If the environment was configured for self-managed provisioning, specify the `provisioningRepository` parameter and omit the `protonServiceRoleArn` and `environmentAccountConnectionId` parameters.

For more information, see [Environments](https://docs.aws.amazon.com/proton/latest/userguide/ag-environments.html) and [Provisioning methods](https://docs.aws.amazon.com/proton/latest/userguide/ag-works-prov-methods.html) in the * AWS Proton User Guide*.

There are four modes for updating an environment. The `deploymentType` field defines the mode.

 `NONE`
In this mode, a deployment *doesn't* occur. Only the requested metadata parameters are updated.

 `CURRENT_VERSION`
In this mode, the environment is deployed and updated with the new spec that you provide. Only requested parameters are updated. *Don’t* include minor or major version parameters when you use this `deployment-type`.

 `MINOR_VERSION`
In this mode, the environment is deployed and updated with the published, recommended (latest) minor version of the current major version in use, by default. You can also specify a different minor version of the current major version in use.

 `MAJOR_VERSION`
In this mode, the environment is deployed and updated with the published, recommended (latest) major and minor version of the current template, by default. You can also specify a different major version that's higher than the major version in use and a minor version.

## Request Syntax
<a name="API_UpdateEnvironment_RequestSyntax"></a>

```
{
   "codebuildRoleArn": "{{string}}",
   "componentRoleArn": "{{string}}",
   "deploymentType": "{{string}}",
   "description": "{{string}}",
   "environmentAccountConnectionId": "{{string}}",
   "name": "{{string}}",
   "protonServiceRoleArn": "{{string}}",
   "provisioningRepository": {
      "branch": "{{string}}",
      "name": "{{string}}",
      "provider": "{{string}}"
   },
   "spec": "{{string}}",
   "templateMajorVersion": "{{string}}",
   "templateMinorVersion": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateEnvironment_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [codebuildRoleArn](#API_UpdateEnvironment_RequestSyntax) **   <a name="proton-UpdateEnvironment-request-codebuildRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM service role that allows AWS Proton to provision infrastructure using CodeBuild-based provisioning on your behalf.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws|aws-cn|aws-us-gov):iam::\d{12}:role/([\w+=,.@-]{1,512}[/:])*([\w+=,.@-]{1,64})`
Required: No

 ** [componentRoleArn](#API_UpdateEnvironment_RequestSyntax) **   <a name="proton-UpdateEnvironment-request-componentRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM service role that AWS Proton uses when provisioning directly defined components in this environment. It determines the scope of infrastructure that a component can provision.
The environment must have a `componentRoleArn` to allow directly defined components to be associated with the environment.
For more information about components, see [AWS Proton components](https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html) in the * AWS Proton User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws|aws-cn|aws-us-gov):iam::\d{12}:role/([\w+=,.@-]{1,512}[/:])*([\w+=,.@-]{1,64})`
Required: No

 ** [deploymentType](#API_UpdateEnvironment_RequestSyntax) **   <a name="proton-UpdateEnvironment-request-deploymentType"></a>
There are four modes for updating an environment. The `deploymentType` field defines the mode.

 `NONE`
In this mode, a deployment *doesn't* occur. Only the requested metadata parameters are updated.

 `CURRENT_VERSION`
In this mode, the environment is deployed and updated with the new spec that you provide. Only requested parameters are updated. *Don’t* include major or minor version parameters when you use this `deployment-type`.

 `MINOR_VERSION`
In this mode, the environment is deployed and updated with the published, recommended (latest) minor version of the current major version in use, by default. You can also specify a different minor version of the current major version in use.

 `MAJOR_VERSION`
In this mode, the environment is deployed and updated with the published, recommended (latest) major and minor version of the current template, by default. You can also specify a different major version that is higher than the major version in use and a minor version (optional).
Type: String
Valid Values: `NONE | CURRENT_VERSION | MINOR_VERSION | MAJOR_VERSION`
Required: Yes

 ** [description](#API_UpdateEnvironment_RequestSyntax) **   <a name="proton-UpdateEnvironment-request-description"></a>
A description of the environment update.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: No

 ** [environmentAccountConnectionId](#API_UpdateEnvironment_RequestSyntax) **   <a name="proton-UpdateEnvironment-request-environmentAccountConnectionId"></a>
The ID of the environment account connection.
You can only update to a new environment account connection if it was created in the same environment account that the current environment account connection was created in and is associated with the current environment.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

 ** [name](#API_UpdateEnvironment_RequestSyntax) **   <a name="proton-UpdateEnvironment-request-name"></a>
The name of the environment to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9A-Za-z]+[0-9A-Za-z_\-]*`
Required: Yes

 ** [protonServiceRoleArn](#API_UpdateEnvironment_RequestSyntax) **   <a name="proton-UpdateEnvironment-request-protonServiceRoleArn"></a>
The Amazon Resource Name (ARN) of the AWS Proton service role that allows AWS Proton to make API calls to other services your behalf.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `arn:(aws|aws-cn|aws-us-gov):[a-zA-Z0-9-]+:[a-zA-Z0-9-]*:\d{12}:([\w+=,.@-]+[/:])*[\w+=,.@-]+`
Required: No

 ** [provisioningRepository](#API_UpdateEnvironment_RequestSyntax) **   <a name="proton-UpdateEnvironment-request-provisioningRepository"></a>
The linked repository that you use to host your rendered infrastructure templates for self-managed provisioning. A linked repository is a repository that has been registered with AWS Proton. For more information, see [CreateRepository](API_CreateRepository.md).
Type: [RepositoryBranchInput](API_RepositoryBranchInput.md) object
Required: No

 ** [spec](#API_UpdateEnvironment_RequestSyntax) **   <a name="proton-UpdateEnvironment-request-spec"></a>
The formatted specification that defines the update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 51200.
Required: No

 ** [templateMajorVersion](#API_UpdateEnvironment_RequestSyntax) **   <a name="proton-UpdateEnvironment-request-templateMajorVersion"></a>
The major version of the environment to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `(0|([1-9]{1}\d*))`
Required: No

 ** [templateMinorVersion](#API_UpdateEnvironment_RequestSyntax) **   <a name="proton-UpdateEnvironment-request-templateMinorVersion"></a>
The minor version of the environment to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `(0|([1-9]{1}\d*))`
Required: No

## Response Syntax
<a name="API_UpdateEnvironment_ResponseSyntax"></a>

```
{
   "environment": {
      "arn": "string",
      "codebuildRoleArn": "string",
      "componentRoleArn": "string",
      "createdAt": number,
      "deploymentStatus": "string",
      "deploymentStatusMessage": "string",
      "description": "string",
      "environmentAccountConnectionId": "string",
      "environmentAccountId": "string",
      "lastAttemptedDeploymentId": "string",
      "lastDeploymentAttemptedAt": number,
      "lastDeploymentSucceededAt": number,
      "lastSucceededDeploymentId": "string",
      "name": "string",
      "protonServiceRoleArn": "string",
      "provisioning": "string",
      "provisioningRepository": {
         "arn": "string",
         "branch": "string",
         "name": "string",
         "provider": "string"
      },
      "spec": "string",
      "templateMajorVersion": "string",
      "templateMinorVersion": "string",
      "templateName": "string"
   }
}
```

## Response Elements
<a name="API_UpdateEnvironment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [environment](#API_UpdateEnvironment_ResponseSyntax) **   <a name="proton-UpdateEnvironment-response-environment"></a>
The environment detail data that's returned by AWS Proton.
Type: [Environment](API_Environment.md) object

## Errors
<a name="API_UpdateEnvironment_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
There *isn't* sufficient access for performing this action.
HTTP Status Code: 400

 ** ConflictException **
The request *couldn't* be made due to a conflicting operation or resource.
HTTP Status Code: 400

 ** InternalServerException **
The request failed to register with the service.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested resource *wasn't* found.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 400

 ** ValidationException **
The input is invalid or an out-of-range value was supplied for the input parameter.
HTTP Status Code: 400

## See Also
<a name="API_UpdateEnvironment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/proton-2020-07-20/UpdateEnvironment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/proton-2020-07-20/UpdateEnvironment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/proton-2020-07-20/UpdateEnvironment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/proton-2020-07-20/UpdateEnvironment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/proton-2020-07-20/UpdateEnvironment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/proton-2020-07-20/UpdateEnvironment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/proton-2020-07-20/UpdateEnvironment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/proton-2020-07-20/UpdateEnvironment)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/proton-2020-07-20/UpdateEnvironment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/proton-2020-07-20/UpdateEnvironment)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Proton. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query proton` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
