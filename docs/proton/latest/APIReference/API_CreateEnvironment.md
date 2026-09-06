---
source_url: https://docs.aws.amazon.com/proton/latest/APIReference/API_CreateEnvironment.html
---

AWS has decided to discontinue AWS Proton, with support ending on October 7, 2026. New customers will not be able to sign up after October 7, 2025, but existing customers can continue to use the service until October 7, 2026.For more information, see [AWS Proton Service Deprecation and Migration Guide](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html).

# CreateEnvironment
<a name="API_CreateEnvironment"></a>

Deploy a new environment. An AWS Proton environment is created from an environment template that defines infrastructure and resources that can be shared across services.

**You can provision environments using the following methods:**
+  AWS-managed provisioning: AWS Proton makes direct calls to provision your resources.
+ Self-managed provisioning: AWS Proton makes pull requests on your repository to provide compiled infrastructure as code (IaC) files that your IaC engine uses to provision resources.

For more information, see [Environments](https://docs.aws.amazon.com/proton/latest/userguide/ag-environments.html) and [Provisioning methods](https://docs.aws.amazon.com/proton/latest/userguide/ag-works-prov-methods.html) in the * AWS Proton User Guide*.

## Request Syntax
<a name="API_CreateEnvironment_RequestSyntax"></a>

```
{
   "codebuildRoleArn": "{{string}}",
   "componentRoleArn": "{{string}}",
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
   "tags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ],
   "templateMajorVersion": "{{string}}",
   "templateMinorVersion": "{{string}}",
   "templateName": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateEnvironment_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [codebuildRoleArn](#API_CreateEnvironment_RequestSyntax) **   <a name="proton-CreateEnvironment-request-codebuildRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM service role that allows AWS Proton to provision infrastructure using CodeBuild-based provisioning on your behalf.
To use CodeBuild-based provisioning for the environment or for any service instance running in the environment, specify either the `environmentAccountConnectionId` or `codebuildRoleArn` parameter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws|aws-cn|aws-us-gov):iam::\d{12}:role/([\w+=,.@-]{1,512}[/:])*([\w+=,.@-]{1,64})`
Required: No

 ** [componentRoleArn](#API_CreateEnvironment_RequestSyntax) **   <a name="proton-CreateEnvironment-request-componentRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM service role that AWS Proton uses when provisioning directly defined components in this environment. It determines the scope of infrastructure that a component can provision.
You must specify `componentRoleArn` to allow directly defined components to be associated with this environment.
For more information about components, see [AWS Proton components](https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html) in the * AWS Proton User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws|aws-cn|aws-us-gov):iam::\d{12}:role/([\w+=,.@-]{1,512}[/:])*([\w+=,.@-]{1,64})`
Required: No

 ** [description](#API_CreateEnvironment_RequestSyntax) **   <a name="proton-CreateEnvironment-request-description"></a>
A description of the environment that's being created and deployed.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: No

 ** [environmentAccountConnectionId](#API_CreateEnvironment_RequestSyntax) **   <a name="proton-CreateEnvironment-request-environmentAccountConnectionId"></a>
The ID of the environment account connection that you provide if you're provisioning your environment infrastructure resources to an environment account. For more information, see [Environment account connections](https://docs.aws.amazon.com/proton/latest/userguide/ag-env-account-connections.html) in the * AWS Proton User guide*.
To use AWS-managed provisioning for the environment, specify either the `environmentAccountConnectionId` or `protonServiceRoleArn` parameter and omit the `provisioningRepository` parameter.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

 ** [name](#API_CreateEnvironment_RequestSyntax) **   <a name="proton-CreateEnvironment-request-name"></a>
The name of the environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9A-Za-z]+[0-9A-Za-z_\-]*`
Required: Yes

 ** [protonServiceRoleArn](#API_CreateEnvironment_RequestSyntax) **   <a name="proton-CreateEnvironment-request-protonServiceRoleArn"></a>
The Amazon Resource Name (ARN) of the AWS Proton service role that allows AWS Proton to make calls to other services on your behalf.
To use AWS-managed provisioning for the environment, specify either the `environmentAccountConnectionId` or `protonServiceRoleArn` parameter and omit the `provisioningRepository` parameter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `arn:(aws|aws-cn|aws-us-gov):[a-zA-Z0-9-]+:[a-zA-Z0-9-]*:\d{12}:([\w+=,.@-]+[/:])*[\w+=,.@-]+`
Required: No

 ** [provisioningRepository](#API_CreateEnvironment_RequestSyntax) **   <a name="proton-CreateEnvironment-request-provisioningRepository"></a>
The linked repository that you use to host your rendered infrastructure templates for self-managed provisioning. A linked repository is a repository that has been registered with AWS Proton. For more information, see [CreateRepository](API_CreateRepository.md).
To use self-managed provisioning for the environment, specify this parameter and omit the `environmentAccountConnectionId` and `protonServiceRoleArn` parameters.
Type: [RepositoryBranchInput](API_RepositoryBranchInput.md) object
Required: No

 ** [spec](#API_CreateEnvironment_RequestSyntax) **   <a name="proton-CreateEnvironment-request-spec"></a>
A YAML formatted string that provides inputs as defined in the environment template bundle schema file. For more information, see [Environments](https://docs.aws.amazon.com/proton/latest/userguide/ag-environments.html) in the * AWS Proton User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 51200.
Required: Yes

 ** [tags](#API_CreateEnvironment_RequestSyntax) **   <a name="proton-CreateEnvironment-request-tags"></a>
An optional list of metadata items that you can associate with the AWS Proton environment. A tag is a key-value pair.
For more information, see [AWS Proton resources and tagging](https://docs.aws.amazon.com/proton/latest/userguide/resources.html) in the * AWS Proton User Guide*.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** [templateMajorVersion](#API_CreateEnvironment_RequestSyntax) **   <a name="proton-CreateEnvironment-request-templateMajorVersion"></a>
The major version of the environment template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `(0|([1-9]{1}\d*))`
Required: Yes

 ** [templateMinorVersion](#API_CreateEnvironment_RequestSyntax) **   <a name="proton-CreateEnvironment-request-templateMinorVersion"></a>
The minor version of the environment template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `(0|([1-9]{1}\d*))`
Required: No

 ** [templateName](#API_CreateEnvironment_RequestSyntax) **   <a name="proton-CreateEnvironment-request-templateName"></a>
The name of the environment template. For more information, see [Environment Templates](https://docs.aws.amazon.com/proton/latest/userguide/ag-templates.html) in the * AWS Proton User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9A-Za-z]+[0-9A-Za-z_\-]*`
Required: Yes

## Response Syntax
<a name="API_CreateEnvironment_ResponseSyntax"></a>

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
<a name="API_CreateEnvironment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [environment](#API_CreateEnvironment_ResponseSyntax) **   <a name="proton-CreateEnvironment-response-environment"></a>
The environment detail data that's returned by AWS Proton.
Type: [Environment](API_Environment.md) object

## Errors
<a name="API_CreateEnvironment_Errors"></a>

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

 ** ServiceQuotaExceededException **
A quota was exceeded. For more information, see [AWS Proton Quotas](https://docs.aws.amazon.com/proton/latest/userguide/ag-limits.html) in the * AWS Proton User Guide*.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 400

 ** ValidationException **
The input is invalid or an out-of-range value was supplied for the input parameter.
HTTP Status Code: 400

## See Also
<a name="API_CreateEnvironment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/proton-2020-07-20/CreateEnvironment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/proton-2020-07-20/CreateEnvironment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/proton-2020-07-20/CreateEnvironment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/proton-2020-07-20/CreateEnvironment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/proton-2020-07-20/CreateEnvironment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/proton-2020-07-20/CreateEnvironment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/proton-2020-07-20/CreateEnvironment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/proton-2020-07-20/CreateEnvironment)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/proton-2020-07-20/CreateEnvironment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/proton-2020-07-20/CreateEnvironment)
