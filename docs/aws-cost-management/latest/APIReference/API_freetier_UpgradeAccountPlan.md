---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_freetier_UpgradeAccountPlan.html
---

# UpgradeAccountPlan
<a name="API_freetier_UpgradeAccountPlan"></a>

 The account plan type for the AWS account.

## Request Syntax
<a name="API_freetier_UpgradeAccountPlan_RequestSyntax"></a>

```
{
   "accountPlanType": "{{string}}"
}
```

## Request Parameters
<a name="API_freetier_UpgradeAccountPlan_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [accountPlanType](#API_freetier_UpgradeAccountPlan_RequestSyntax) **   <a name="awscostmanagement-freetier_UpgradeAccountPlan-request-accountPlanType"></a>
 The target account plan type. This makes it explicit about the change and latest value of the `accountPlanType`.
Type: String
Valid Values: `FREE | PAID`
Required: Yes

## Response Syntax
<a name="API_freetier_UpgradeAccountPlan_ResponseSyntax"></a>

```
{
   "accountId": "string",
   "accountPlanStatus": "string",
   "accountPlanType": "string"
}
```

## Response Elements
<a name="API_freetier_UpgradeAccountPlan_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [accountId](#API_freetier_UpgradeAccountPlan_ResponseSyntax) **   <a name="awscostmanagement-freetier_UpgradeAccountPlan-response-accountId"></a>
 A unique identifier that identifies the account.
Type: String
Pattern: `[0-9]{12}`

 ** [accountPlanStatus](#API_freetier_UpgradeAccountPlan_ResponseSyntax) **   <a name="awscostmanagement-freetier_UpgradeAccountPlan-response-accountPlanStatus"></a>
 This indicates the latest state of the account plan within its lifecycle.
Type: String
Valid Values: `NOT_STARTED | ACTIVE | EXPIRED`

 ** [accountPlanType](#API_freetier_UpgradeAccountPlan_ResponseSyntax) **   <a name="awscostmanagement-freetier_UpgradeAccountPlan-response-accountPlanType"></a>
 The type of plan for the account.
Type: String
Valid Values: `FREE | PAID`

## Errors
<a name="API_freetier_UpgradeAccountPlan_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 You don't have sufficient access to perform this action.
HTTP Status Code: 400

 ** InternalServerException **
An unexpected error occurred during the processing of your request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
 This exception is thrown when the requested resource cannot be found.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 400

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_freetier_UpgradeAccountPlan_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/freetier-2023-09-07/UpgradeAccountPlan)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/freetier-2023-09-07/UpgradeAccountPlan)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/freetier-2023-09-07/UpgradeAccountPlan)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/freetier-2023-09-07/UpgradeAccountPlan)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/freetier-2023-09-07/UpgradeAccountPlan)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/freetier-2023-09-07/UpgradeAccountPlan)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/freetier-2023-09-07/UpgradeAccountPlan)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/freetier-2023-09-07/UpgradeAccountPlan)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/freetier-2023-09-07/UpgradeAccountPlan)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/freetier-2023-09-07/UpgradeAccountPlan)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
