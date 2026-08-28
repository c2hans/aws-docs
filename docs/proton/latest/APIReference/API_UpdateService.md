---
source_url: https://docs.aws.amazon.com/proton/latest/APIReference/API_UpdateService.html
---

AWS has decided to discontinue AWS Proton, with support ending on October 7, 2026. New customers will not be able to sign up after October 7, 2025, but existing customers can continue to use the service until October 7, 2026.For more information, see [AWS Proton Service Deprecation and Migration Guide](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html).

# UpdateService
<a name="API_UpdateService"></a>

Edit a service description or use a spec to add and delete service instances.

**Note**
Existing service instances and the service pipeline *can't* be edited using this API. They can only be deleted.

Use the `description` parameter to modify the description.

Edit the `spec` parameter to add or delete instances.

**Note**
You can't delete a service instance (remove it from the spec) if it has an attached component.
For more information about components, see [AWS Proton components](https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html) in the * AWS Proton User Guide*.

## Request Syntax
<a name="API_UpdateService_RequestSyntax"></a>

```
{
   "description": "{{string}}",
   "name": "{{string}}",
   "spec": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateService_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [description](#API_UpdateService_RequestSyntax) **   <a name="proton-UpdateService-request-description"></a>
The edited service description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: No

 ** [name](#API_UpdateService_RequestSyntax) **   <a name="proton-UpdateService-request-name"></a>
The name of the service to edit.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9A-Za-z]+[0-9A-Za-z_\-]*`
Required: Yes

 ** [spec](#API_UpdateService_RequestSyntax) **   <a name="proton-UpdateService-request-spec"></a>
Lists the service instances to add and the existing service instances to remain. Omit the existing service instances to delete from the list. *Don't* include edits to the existing service instances or pipeline. For more information, see [Edit a service](https://docs.aws.amazon.com/proton/latest/userguide/ag-svc-update.html) in the * AWS Proton User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 51200.
Required: No

## Response Syntax
<a name="API_UpdateService_ResponseSyntax"></a>

```
{
   "service": {
      "arn": "string",
      "branchName": "string",
      "createdAt": number,
      "description": "string",
      "lastModifiedAt": number,
      "name": "string",
      "pipeline": {
         "arn": "string",
         "createdAt": number,
         "deploymentStatus": "string",
         "deploymentStatusMessage": "string",
         "lastAttemptedDeploymentId": "string",
         "lastDeploymentAttemptedAt": number,
         "lastDeploymentSucceededAt": number,
         "lastSucceededDeploymentId": "string",
         "spec": "string",
         "templateMajorVersion": "string",
         "templateMinorVersion": "string",
         "templateName": "string"
      },
      "repositoryConnectionArn": "string",
      "repositoryId": "string",
      "spec": "string",
      "status": "string",
      "statusMessage": "string",
      "templateName": "string"
   }
}
```

## Response Elements
<a name="API_UpdateService_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [service](#API_UpdateService_ResponseSyntax) **   <a name="proton-UpdateService-response-service"></a>
The service detail data that's returned by AWS Proton.
Type: [Service](API_Service.md) object

## Errors
<a name="API_UpdateService_Errors"></a>

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
<a name="API_UpdateService_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/proton-2020-07-20/UpdateService)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/proton-2020-07-20/UpdateService)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/proton-2020-07-20/UpdateService)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/proton-2020-07-20/UpdateService)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/proton-2020-07-20/UpdateService)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/proton-2020-07-20/UpdateService)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/proton-2020-07-20/UpdateService)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/proton-2020-07-20/UpdateService)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/proton-2020-07-20/UpdateService)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/proton-2020-07-20/UpdateService)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Proton. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query proton` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
