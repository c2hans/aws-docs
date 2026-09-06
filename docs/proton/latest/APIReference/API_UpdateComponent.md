---
source_url: https://docs.aws.amazon.com/proton/latest/APIReference/API_UpdateComponent.html
---

AWS has decided to discontinue AWS Proton, with support ending on October 7, 2026. New customers will not be able to sign up after October 7, 2025, but existing customers can continue to use the service until October 7, 2026.For more information, see [AWS Proton Service Deprecation and Migration Guide](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html).

# UpdateComponent
<a name="API_UpdateComponent"></a>

Update a component.

There are a few modes for updating a component. The `deploymentType` field defines the mode.

**Note**
You can't update a component while its deployment status, or the deployment status of a service instance attached to it, is `IN_PROGRESS`.

For more information about components, see [AWS Proton components](https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html) in the * AWS Proton User Guide*.

## Request Syntax
<a name="API_UpdateComponent_RequestSyntax"></a>

```
{
   "clientToken": "{{string}}",
   "deploymentType": "{{string}}",
   "description": "{{string}}",
   "name": "{{string}}",
   "serviceInstanceName": "{{string}}",
   "serviceName": "{{string}}",
   "serviceSpec": "{{string}}",
   "templateFile": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateComponent_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [clientToken](#API_UpdateComponent_RequestSyntax) **   <a name="proton-UpdateComponent-request-clientToken"></a>
The client token for the updated component.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `[!-~]*`
Required: No

 ** [deploymentType](#API_UpdateComponent_RequestSyntax) **   <a name="proton-UpdateComponent-request-deploymentType"></a>
The deployment type. It defines the mode for updating a component, as follows:

 `NONE`
In this mode, a deployment *doesn't* occur. Only the requested metadata parameters are updated. You can only specify `description` in this mode.

 `CURRENT_VERSION`
In this mode, the component is deployed and updated with the new `serviceSpec`, `templateSource`, and/or `type` that you provide. Only requested parameters are updated.
Type: String
Valid Values: `NONE | CURRENT_VERSION`
Required: Yes

 ** [description](#API_UpdateComponent_RequestSyntax) **   <a name="proton-UpdateComponent-request-description"></a>
An optional customer-provided description of the component.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: No

 ** [name](#API_UpdateComponent_RequestSyntax) **   <a name="proton-UpdateComponent-request-name"></a>
The name of the component to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9A-Za-z]+[0-9A-Za-z_\-]*`
Required: Yes

 ** [serviceInstanceName](#API_UpdateComponent_RequestSyntax) **   <a name="proton-UpdateComponent-request-serviceInstanceName"></a>
The name of the service instance that you want to attach this component to. Don't specify to keep the component's current service instance attachment. Specify an empty string to detach the component from the service instance it's attached to. Specify non-empty values for both `serviceInstanceName` and `serviceName` or for neither of them.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Pattern: `.*(^$)|^[0-9A-Za-z]+[0-9A-Za-z_\-]*`
Required: No

 ** [serviceName](#API_UpdateComponent_RequestSyntax) **   <a name="proton-UpdateComponent-request-serviceName"></a>
The name of the service that `serviceInstanceName` is associated with. Don't specify to keep the component's current service instance attachment. Specify an empty string to detach the component from the service instance it's attached to. Specify non-empty values for both `serviceInstanceName` and `serviceName` or for neither of them.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Pattern: `.*(^$)|^[0-9A-Za-z]+[0-9A-Za-z_\-]*`
Required: No

 ** [serviceSpec](#API_UpdateComponent_RequestSyntax) **   <a name="proton-UpdateComponent-request-serviceSpec"></a>
The service spec that you want the component to use to access service inputs. Set this only when the component is attached to a service instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 51200.
Required: No

 ** [templateFile](#API_UpdateComponent_RequestSyntax) **   <a name="proton-UpdateComponent-request-templateFile"></a>
A path to the Infrastructure as Code (IaC) file describing infrastructure that a custom component provisions.
Components support a single IaC file, even if you use Terraform as your template language.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 51200.
Required: No

## Response Syntax
<a name="API_UpdateComponent_ResponseSyntax"></a>

```
{
   "component": {
      "arn": "string",
      "createdAt": number,
      "deploymentStatus": "string",
      "deploymentStatusMessage": "string",
      "description": "string",
      "environmentName": "string",
      "lastAttemptedDeploymentId": "string",
      "lastClientRequestToken": "string",
      "lastDeploymentAttemptedAt": number,
      "lastDeploymentSucceededAt": number,
      "lastModifiedAt": number,
      "lastSucceededDeploymentId": "string",
      "name": "string",
      "serviceInstanceName": "string",
      "serviceName": "string",
      "serviceSpec": "string"
   }
}
```

## Response Elements
<a name="API_UpdateComponent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [component](#API_UpdateComponent_ResponseSyntax) **   <a name="proton-UpdateComponent-response-component"></a>
The detailed data of the updated component.
Type: [Component](API_Component.md) object

## Errors
<a name="API_UpdateComponent_Errors"></a>

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
<a name="API_UpdateComponent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/proton-2020-07-20/UpdateComponent)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/proton-2020-07-20/UpdateComponent)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/proton-2020-07-20/UpdateComponent)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/proton-2020-07-20/UpdateComponent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/proton-2020-07-20/UpdateComponent)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/proton-2020-07-20/UpdateComponent)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/proton-2020-07-20/UpdateComponent)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/proton-2020-07-20/UpdateComponent)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/proton-2020-07-20/UpdateComponent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/proton-2020-07-20/UpdateComponent)
