---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_UpdateEnrollmentStatus.html
---

# UpdateEnrollmentStatus
<a name="API_CostOptimizationHub_UpdateEnrollmentStatus"></a>

Updates the enrollment (opt in and opt out) status of an account to the Cost Optimization Hub service.

If the account is a management account of an organization, this action can also be used to enroll member accounts of the organization.

You must have the appropriate permissions to opt in to Cost Optimization Hub and to view its recommendations. When you opt in, Cost Optimization Hub automatically creates a service-linked role in your account to access its data.

## Request Syntax
<a name="API_CostOptimizationHub_UpdateEnrollmentStatus_RequestSyntax"></a>

```
{
   "includeMemberAccounts": {{boolean}},
   "status": "{{string}}"
}
```

## Request Parameters
<a name="API_CostOptimizationHub_UpdateEnrollmentStatus_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [includeMemberAccounts](#API_CostOptimizationHub_UpdateEnrollmentStatus_RequestSyntax) **   <a name="awscostmanagement-CostOptimizationHub_UpdateEnrollmentStatus-request-includeMemberAccounts"></a>
Indicates whether to enroll member accounts of the organization if the account is the management account or delegated administrator.
Type: Boolean
Required: No

 ** [status](#API_CostOptimizationHub_UpdateEnrollmentStatus_RequestSyntax) **   <a name="awscostmanagement-CostOptimizationHub_UpdateEnrollmentStatus-request-status"></a>
Sets the account status.
Type: String
Valid Values: `Active | Inactive`
Required: Yes

## Response Syntax
<a name="API_CostOptimizationHub_UpdateEnrollmentStatus_ResponseSyntax"></a>

```
{
   "status": "string"
}
```

## Response Elements
<a name="API_CostOptimizationHub_UpdateEnrollmentStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [status](#API_CostOptimizationHub_UpdateEnrollmentStatus_ResponseSyntax) **   <a name="awscostmanagement-CostOptimizationHub_UpdateEnrollmentStatus-response-status"></a>
The enrollment status of the account.
Type: String

## Errors
<a name="API_CostOptimizationHub_UpdateEnrollmentStatus_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You are not authorized to use this operation with the given parameters.
HTTP Status Code: 400

 ** InternalServerException **
An error on the server occurred during the processing of your request. Try again later.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 400

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
 ** fields **
The list of fields that are invalid.
 ** reason **
The reason for the validation exception.
HTTP Status Code: 400

## See Also
<a name="API_CostOptimizationHub_UpdateEnrollmentStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cost-optimization-hub-2022-07-26/UpdateEnrollmentStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cost-optimization-hub-2022-07-26/UpdateEnrollmentStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cost-optimization-hub-2022-07-26/UpdateEnrollmentStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cost-optimization-hub-2022-07-26/UpdateEnrollmentStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cost-optimization-hub-2022-07-26/UpdateEnrollmentStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cost-optimization-hub-2022-07-26/UpdateEnrollmentStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cost-optimization-hub-2022-07-26/UpdateEnrollmentStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cost-optimization-hub-2022-07-26/UpdateEnrollmentStatus)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cost-optimization-hub-2022-07-26/UpdateEnrollmentStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cost-optimization-hub-2022-07-26/UpdateEnrollmentStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
