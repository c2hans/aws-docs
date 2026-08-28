---
source_url: https://docs.aws.amazon.com/proton/latest/APIReference/API_NotifyResourceDeploymentStatusChange.html
---

AWS has decided to discontinue AWS Proton, with support ending on October 7, 2026. New customers will not be able to sign up after October 7, 2025, but existing customers can continue to use the service until October 7, 2026.For more information, see [AWS Proton Service Deprecation and Migration Guide](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html).

# NotifyResourceDeploymentStatusChange
<a name="API_NotifyResourceDeploymentStatusChange"></a>

Notify AWS Proton of status changes to a provisioned resource when you use self-managed provisioning.

For more information, see [Self-managed provisioning](https://docs.aws.amazon.com/proton/latest/userguide/ag-works-prov-methods.html#ag-works-prov-methods-self) in the * AWS Proton User Guide*.

## Request Syntax
<a name="API_NotifyResourceDeploymentStatusChange_RequestSyntax"></a>

```
{
   "deploymentId": "{{string}}",
   "outputs": [
      {
         "key": "{{string}}",
         "valueString": "{{string}}"
      }
   ],
   "resourceArn": "{{string}}",
   "status": "{{string}}",
   "statusMessage": "{{string}}"
}
```

## Request Parameters
<a name="API_NotifyResourceDeploymentStatusChange_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [deploymentId](#API_NotifyResourceDeploymentStatusChange_RequestSyntax) **   <a name="proton-NotifyResourceDeploymentStatusChange-request-deploymentId"></a>
The deployment ID for your provisioned resource.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

 ** [outputs](#API_NotifyResourceDeploymentStatusChange_RequestSyntax) **   <a name="proton-NotifyResourceDeploymentStatusChange-request-outputs"></a>
The provisioned resource state change detail data that's returned by AWS Proton.
Type: Array of [Output](API_Output.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** [resourceArn](#API_NotifyResourceDeploymentStatusChange_RequestSyntax) **   <a name="proton-NotifyResourceDeploymentStatusChange-request-resourceArn"></a>
The provisioned resource Amazon Resource Name (ARN).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `arn:(aws|aws-cn|aws-us-gov):[a-zA-Z0-9-]+:[a-zA-Z0-9-]*:\d{12}:([\w+=,.@-]+[/:])*[\w+=,.@-]+`
Required: Yes

 ** [status](#API_NotifyResourceDeploymentStatusChange_RequestSyntax) **   <a name="proton-NotifyResourceDeploymentStatusChange-request-status"></a>
The status of your provisioned resource.
Type: String
Valid Values: `IN_PROGRESS | FAILED | SUCCEEDED`
Required: No

 ** [statusMessage](#API_NotifyResourceDeploymentStatusChange_RequestSyntax) **   <a name="proton-NotifyResourceDeploymentStatusChange-request-statusMessage"></a>
The deployment status message for your provisioned resource.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 5000.
Required: No

## Response Elements
<a name="API_NotifyResourceDeploymentStatusChange_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_NotifyResourceDeploymentStatusChange_Errors"></a>

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
<a name="API_NotifyResourceDeploymentStatusChange_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/proton-2020-07-20/NotifyResourceDeploymentStatusChange)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/proton-2020-07-20/NotifyResourceDeploymentStatusChange)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/proton-2020-07-20/NotifyResourceDeploymentStatusChange)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/proton-2020-07-20/NotifyResourceDeploymentStatusChange)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/proton-2020-07-20/NotifyResourceDeploymentStatusChange)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/proton-2020-07-20/NotifyResourceDeploymentStatusChange)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/proton-2020-07-20/NotifyResourceDeploymentStatusChange)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/proton-2020-07-20/NotifyResourceDeploymentStatusChange)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/proton-2020-07-20/NotifyResourceDeploymentStatusChange)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/proton-2020-07-20/NotifyResourceDeploymentStatusChange)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Proton. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query proton` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
