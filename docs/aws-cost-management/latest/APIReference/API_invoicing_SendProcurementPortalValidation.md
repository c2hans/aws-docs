---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_SendProcurementPortalValidation.html
---

# SendProcurementPortalValidation
<a name="API_invoicing_SendProcurementPortalValidation"></a>

 * **This feature API is subject to changing at any time. For more information, see the [AWS Service Terms](https://aws.amazon.com/service-terms/) (Betas and Previews).** *

Sends a validation request for a procurement portal preference. This operation initiates the validation process by issuing a validation code that confirms ownership and connectivity of the configured procurement portal endpoint. Use `VerifyProcurementPortalValidation` to submit the received code and complete validation.

## Request Syntax
<a name="API_invoicing_SendProcurementPortalValidation_RequestSyntax"></a>

```
{
   "ClientToken": "{{string}}",
   "ProcurementPortalPreferenceArn": "{{string}}"
}
```

## Request Parameters
<a name="API_invoicing_SendProcurementPortalValidation_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientToken](#API_invoicing_SendProcurementPortalValidation_RequestSyntax) **   <a name="awscostmanagement-invoicing_SendProcurementPortalValidation-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure idempotency of the request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `\S+`
Required: No

 ** [ProcurementPortalPreferenceArn](#API_invoicing_SendProcurementPortalValidation_RequestSyntax) **   <a name="awscostmanagement-invoicing_SendProcurementPortalValidation-request-ProcurementPortalPreferenceArn"></a>
The Amazon Resource Name (ARN) of the procurement portal preference to validate.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `arn:aws:invoicing::[0-9]{12}:procurement-portal-preference/[-a-zA-Z0-9]+`
Required: Yes

## Response Syntax
<a name="API_invoicing_SendProcurementPortalValidation_ResponseSyntax"></a>

```
{
   "ProcurementPortalPreferenceArn": "string"
}
```

## Response Elements
<a name="API_invoicing_SendProcurementPortalValidation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ProcurementPortalPreferenceArn](#API_invoicing_SendProcurementPortalValidation_ResponseSyntax) **   <a name="awscostmanagement-invoicing_SendProcurementPortalValidation-response-ProcurementPortalPreferenceArn"></a>
The Amazon Resource Name (ARN) of the procurement portal preference for which the validation request was sent.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `arn:aws:invoicing::[0-9]{12}:procurement-portal-preference/[-a-zA-Z0-9]+`

## Errors
<a name="API_invoicing_SendProcurementPortalValidation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this action.
 ** resourceName **
You don't have sufficient access to perform this action.
HTTP Status Code: 400

 ** InternalServerException **
The processing request failed because of an unknown error, exception, or failure.
 ** retryAfterSeconds **
The processing request failed because of an unknown error, exception, or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource could not be found.
 ** resourceName **
The resource could not be found.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 400

 ** ValidationException **
 The input fails to satisfy the constraints specified by an AWS service.
 ** fieldList **
 The input fails to satisfy the constraints specified by an AWS service.
 ** reason **
You don't have sufficient access to perform this action.
 ** resourceName **
You don't have sufficient access to perform this action.
HTTP Status Code: 400

## See Also
<a name="API_invoicing_SendProcurementPortalValidation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/invoicing-2024-12-01/SendProcurementPortalValidation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/invoicing-2024-12-01/SendProcurementPortalValidation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/invoicing-2024-12-01/SendProcurementPortalValidation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/invoicing-2024-12-01/SendProcurementPortalValidation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/invoicing-2024-12-01/SendProcurementPortalValidation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/invoicing-2024-12-01/SendProcurementPortalValidation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/invoicing-2024-12-01/SendProcurementPortalValidation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/invoicing-2024-12-01/SendProcurementPortalValidation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/invoicing-2024-12-01/SendProcurementPortalValidation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/invoicing-2024-12-01/SendProcurementPortalValidation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
