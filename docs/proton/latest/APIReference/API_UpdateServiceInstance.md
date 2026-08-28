---
source_url: https://docs.aws.amazon.com/proton/latest/APIReference/API_UpdateServiceInstance.html
---

AWS has decided to discontinue AWS Proton, with support ending on October 7, 2026. New customers will not be able to sign up after October 7, 2025, but existing customers can continue to use the service until October 7, 2026.For more information, see [AWS Proton Service Deprecation and Migration Guide](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html).

# UpdateServiceInstance
<a name="API_UpdateServiceInstance"></a>

Update a service instance.

There are a few modes for updating a service instance. The `deploymentType` field defines the mode.

**Note**
You can't update a service instance while its deployment status, or the deployment status of a component attached to it, is `IN_PROGRESS`.
For more information about components, see [AWS Proton components](https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html) in the * AWS Proton User Guide*.

## Request Syntax
<a name="API_UpdateServiceInstance_RequestSyntax"></a>

```
{
   "clientToken": "{{string}}",
   "deploymentType": "{{string}}",
   "name": "{{string}}",
   "serviceName": "{{string}}",
   "spec": "{{string}}",
   "templateMajorVersion": "{{string}}",
   "templateMinorVersion": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateServiceInstance_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [clientToken](#API_UpdateServiceInstance_RequestSyntax) **   <a name="proton-UpdateServiceInstance-request-clientToken"></a>
The client token of the service instance to update.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `[!-~]*`
Required: No

 ** [deploymentType](#API_UpdateServiceInstance_RequestSyntax) **   <a name="proton-UpdateServiceInstance-request-deploymentType"></a>
The deployment type. It defines the mode for updating a service instance, as follows:

 `NONE`
In this mode, a deployment *doesn't* occur. Only the requested metadata parameters are updated.

 `CURRENT_VERSION`
In this mode, the service instance is deployed and updated with the new spec that you provide. Only requested parameters are updated. *Don’t* include major or minor version parameters when you use this deployment type.

 `MINOR_VERSION`
In this mode, the service instance is deployed and updated with the published, recommended (latest) minor version of the current major version in use, by default. You can also specify a different minor version of the current major version in use.

 `MAJOR_VERSION`
In this mode, the service instance is deployed and updated with the published, recommended (latest) major and minor version of the current template, by default. You can specify a different major version that's higher than the major version in use and a minor version.
Type: String
Valid Values: `NONE | CURRENT_VERSION | MINOR_VERSION | MAJOR_VERSION`
Required: Yes

 ** [name](#API_UpdateServiceInstance_RequestSyntax) **   <a name="proton-UpdateServiceInstance-request-name"></a>
The name of the service instance to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9A-Za-z]+[0-9A-Za-z_\-]*`
Required: Yes

 ** [serviceName](#API_UpdateServiceInstance_RequestSyntax) **   <a name="proton-UpdateServiceInstance-request-serviceName"></a>
The name of the service that the service instance belongs to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9A-Za-z]+[0-9A-Za-z_\-]*`
Required: Yes

 ** [spec](#API_UpdateServiceInstance_RequestSyntax) **   <a name="proton-UpdateServiceInstance-request-spec"></a>
The formatted specification that defines the service instance update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 51200.
Required: No

 ** [templateMajorVersion](#API_UpdateServiceInstance_RequestSyntax) **   <a name="proton-UpdateServiceInstance-request-templateMajorVersion"></a>
The major version of the service template to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `(0|([1-9]{1}\d*))`
Required: No

 ** [templateMinorVersion](#API_UpdateServiceInstance_RequestSyntax) **   <a name="proton-UpdateServiceInstance-request-templateMinorVersion"></a>
The minor version of the service template to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `(0|([1-9]{1}\d*))`
Required: No

## Response Syntax
<a name="API_UpdateServiceInstance_ResponseSyntax"></a>

```
{
   "serviceInstance": {
      "arn": "string",
      "createdAt": number,
      "deploymentStatus": "string",
      "deploymentStatusMessage": "string",
      "environmentName": "string",
      "lastAttemptedDeploymentId": "string",
      "lastClientRequestToken": "string",
      "lastDeploymentAttemptedAt": number,
      "lastDeploymentSucceededAt": number,
      "lastSucceededDeploymentId": "string",
      "name": "string",
      "serviceName": "string",
      "spec": "string",
      "templateMajorVersion": "string",
      "templateMinorVersion": "string",
      "templateName": "string"
   }
}
```

## Response Elements
<a name="API_UpdateServiceInstance_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [serviceInstance](#API_UpdateServiceInstance_ResponseSyntax) **   <a name="proton-UpdateServiceInstance-response-serviceInstance"></a>
The service instance summary data that's returned by AWS Proton.
Type: [ServiceInstance](API_ServiceInstance.md) object

## Errors
<a name="API_UpdateServiceInstance_Errors"></a>

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
<a name="API_UpdateServiceInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/proton-2020-07-20/UpdateServiceInstance)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/proton-2020-07-20/UpdateServiceInstance)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/proton-2020-07-20/UpdateServiceInstance)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/proton-2020-07-20/UpdateServiceInstance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/proton-2020-07-20/UpdateServiceInstance)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/proton-2020-07-20/UpdateServiceInstance)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/proton-2020-07-20/UpdateServiceInstance)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/proton-2020-07-20/UpdateServiceInstance)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/proton-2020-07-20/UpdateServiceInstance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/proton-2020-07-20/UpdateServiceInstance)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Proton. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query proton` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
