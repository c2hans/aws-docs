---
source_url: https://docs.aws.amazon.com/workspaces-instances/latest/api/API_GetWorkspaceInstance.html
---

# GetWorkspaceInstance
<a name="API_GetWorkspaceInstance"></a>

Retrieves detailed information about a specific WorkSpace Instance.

## Request Syntax
<a name="API_GetWorkspaceInstance_RequestSyntax"></a>

```
{
   "WorkspaceInstanceId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetWorkspaceInstance_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [WorkspaceInstanceId](#API_GetWorkspaceInstance_RequestSyntax) **   <a name="workspacesinstances-GetWorkspaceInstance-request-WorkspaceInstanceId"></a>
Unique identifier of the WorkSpace Instance to retrieve.
Type: String
Length Constraints: Minimum length of 15. Maximum length of 70.
Pattern: `wsinst-[0-9a-zA-Z]{8,63}`
Required: Yes

## Response Syntax
<a name="API_GetWorkspaceInstance_ResponseSyntax"></a>

```
{
   "BillingConfiguration": {
      "BillingMode": "string"
   },
   "EC2InstanceErrors": [
      {
         "EC2ErrorCode": "string",
         "EC2ErrorMessage": "string",
         "EC2ExceptionType": "string"
      }
   ],
   "EC2ManagedInstance": {
      "InstanceId": "string"
   },
   "ProvisionState": "string",
   "WorkspaceInstanceErrors": [
      {
         "ErrorCode": "string",
         "ErrorMessage": "string"
      }
   ],
   "WorkspaceInstanceId": "string"
}
```

## Response Elements
<a name="API_GetWorkspaceInstance_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [BillingConfiguration](#API_GetWorkspaceInstance_ResponseSyntax) **   <a name="workspacesinstances-GetWorkspaceInstance-response-BillingConfiguration"></a>
Returns the current billing configuration for the WorkSpace Instance, indicating the active billing mode.
Type: [BillingConfiguration](API_BillingConfiguration.md) object

 ** [EC2InstanceErrors](#API_GetWorkspaceInstance_ResponseSyntax) **   <a name="workspacesinstances-GetWorkspaceInstance-response-EC2InstanceErrors"></a>
Includes any underlying EC2 instance errors encountered.
Type: Array of [EC2InstanceError](API_EC2InstanceError.md) objects

 ** [EC2ManagedInstance](#API_GetWorkspaceInstance_ResponseSyntax) **   <a name="workspacesinstances-GetWorkspaceInstance-response-EC2ManagedInstance"></a>
Details of the associated EC2 managed instance.
Type: [EC2ManagedInstance](API_EC2ManagedInstance.md) object

 ** [ProvisionState](#API_GetWorkspaceInstance_ResponseSyntax) **   <a name="workspacesinstances-GetWorkspaceInstance-response-ProvisionState"></a>
Current provisioning state of the WorkSpaces Instance.
Type: String
Valid Values: `ALLOCATING | ALLOCATED | DEALLOCATING | DEALLOCATED | ERROR_ALLOCATING | ERROR_DEALLOCATING`

 ** [WorkspaceInstanceErrors](#API_GetWorkspaceInstance_ResponseSyntax) **   <a name="workspacesinstances-GetWorkspaceInstance-response-WorkspaceInstanceErrors"></a>
Captures any errors specific to the WorkSpace Instance lifecycle.
Type: Array of [WorkspaceInstanceError](API_WorkspaceInstanceError.md) objects

 ** [WorkspaceInstanceId](#API_GetWorkspaceInstance_ResponseSyntax) **   <a name="workspacesinstances-GetWorkspaceInstance-response-WorkspaceInstanceId"></a>
Unique identifier of the retrieved WorkSpaces Instance.
Type: String
Length Constraints: Minimum length of 15. Maximum length of 70.
Pattern: `wsinst-[0-9a-zA-Z]{8,63}`

## Errors
<a name="API_GetWorkspaceInstance_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Indicates insufficient permissions to perform the requested action.
 ** Message **
Detailed explanation of the access denial.
HTTP Status Code: 400

 ** InternalServerException **
Indicates an unexpected server-side error occurred.
 ** Message **
Description of the internal server error.
 ** RetryAfterSeconds **
Recommended wait time before retrying the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Indicates the requested resource could not be found.
 ** Message **
Details about the missing resource.
 ** ResourceId **
Identifier of the resource that was not found.
 ** ResourceType **
Type of the resource that was not found.
HTTP Status Code: 400

 ** ThrottlingException **
Indicates the request rate has exceeded limits.
 ** Message **
Description of the throttling event.
 ** QuotaCode **
Specific code for the throttling quota.
 ** RetryAfterSeconds **
Recommended wait time before retrying the request.
 ** ServiceCode **
Code identifying the service experiencing throttling.
HTTP Status Code: 400

 ** ValidationException **
Indicates invalid input parameters in the request.
 ** FieldList **
List of fields that failed validation.
 ** Message **
Overall description of validation failures.
 ** Reason **
Specific reason for the validation failure.
HTTP Status Code: 400

## See Also
<a name="API_GetWorkspaceInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workspaces-instances-2022-07-26/GetWorkspaceInstance)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workspaces-instances-2022-07-26/GetWorkspaceInstance)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-instances-2022-07-26/GetWorkspaceInstance)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workspaces-instances-2022-07-26/GetWorkspaceInstance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-instances-2022-07-26/GetWorkspaceInstance)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workspaces-instances-2022-07-26/GetWorkspaceInstance)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workspaces-instances-2022-07-26/GetWorkspaceInstance)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workspaces-instances-2022-07-26/GetWorkspaceInstance)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workspaces-instances-2022-07-26/GetWorkspaceInstance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-instances-2022-07-26/GetWorkspaceInstance)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for WorkSpaces Instances. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces-instances` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
