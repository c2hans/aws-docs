---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_UpdateInvoiceUnit.html
---

# UpdateInvoiceUnit
<a name="API_invoicing_UpdateInvoiceUnit"></a>

You can update the invoice unit configuration at any time, and AWS will use the latest configuration at the end of the month.

## Request Syntax
<a name="API_invoicing_UpdateInvoiceUnit_RequestSyntax"></a>

```
{
   "ClientToken": "{{string}}",
   "Description": "{{string}}",
   "InvoiceUnitArn": "{{string}}",
   "Rule": {
      "BillSourceAccounts": [ "{{string}}" ],
      "LinkedAccounts": [ "{{string}}" ]
   },
   "TaxInheritanceDisabled": {{boolean}}
}
```

## Request Parameters
<a name="API_invoicing_UpdateInvoiceUnit_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientToken](#API_invoicing_UpdateInvoiceUnit_RequestSyntax) **   <a name="awscostmanagement-invoicing_UpdateInvoiceUnit-request-ClientToken"></a>
 A unique, case-sensitive identifier that you provide to ensure idempotency of the request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `\S+`
Required: No

 ** [Description](#API_invoicing_UpdateInvoiceUnit_RequestSyntax) **   <a name="awscostmanagement-invoicing_UpdateInvoiceUnit-request-Description"></a>
The assigned description for an invoice unit. This information can't be modified or deleted.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Pattern: `[\S\s]*`
Required: No

 ** [InvoiceUnitArn](#API_invoicing_UpdateInvoiceUnit_RequestSyntax) **   <a name="awscostmanagement-invoicing_UpdateInvoiceUnit-request-InvoiceUnitArn"></a>
The ARN to identify an invoice unit. This information can't be modified or deleted.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `arn:aws[-a-z0-9]*:[a-z0-9]+:[-a-z0-9]*:[0-9]{12}:[-a-zA-Z0-9/:_]+`
Required: Yes

 ** [Rule](#API_invoicing_UpdateInvoiceUnit_RequestSyntax) **   <a name="awscostmanagement-invoicing_UpdateInvoiceUnit-request-Rule"></a>
The `InvoiceUnitRule` object used to update invoice units.
Type: [InvoiceUnitRule](API_invoicing_InvoiceUnitRule.md) object
Required: No

 ** [TaxInheritanceDisabled](#API_invoicing_UpdateInvoiceUnit_RequestSyntax) **   <a name="awscostmanagement-invoicing_UpdateInvoiceUnit-request-TaxInheritanceDisabled"></a>
Whether the invoice unit based tax inheritance is/ should be enabled or disabled.
Type: Boolean
Required: No

## Response Syntax
<a name="API_invoicing_UpdateInvoiceUnit_ResponseSyntax"></a>

```
{
   "InvoiceUnitArn": "string"
}
```

## Response Elements
<a name="API_invoicing_UpdateInvoiceUnit_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [InvoiceUnitArn](#API_invoicing_UpdateInvoiceUnit_ResponseSyntax) **   <a name="awscostmanagement-invoicing_UpdateInvoiceUnit-response-InvoiceUnitArn"></a>
 The ARN to identify an invoice unit. This information can't be modified or deleted.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `arn:aws[-a-z0-9]*:[a-z0-9]+:[-a-z0-9]*:[0-9]{12}:[-a-zA-Z0-9/:_]+`

## Errors
<a name="API_invoicing_UpdateInvoiceUnit_Errors"></a>

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
<a name="API_invoicing_UpdateInvoiceUnit_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/invoicing-2024-12-01/UpdateInvoiceUnit)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/invoicing-2024-12-01/UpdateInvoiceUnit)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/invoicing-2024-12-01/UpdateInvoiceUnit)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/invoicing-2024-12-01/UpdateInvoiceUnit)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/invoicing-2024-12-01/UpdateInvoiceUnit)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/invoicing-2024-12-01/UpdateInvoiceUnit)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/invoicing-2024-12-01/UpdateInvoiceUnit)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/invoicing-2024-12-01/UpdateInvoiceUnit)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/invoicing-2024-12-01/UpdateInvoiceUnit)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/invoicing-2024-12-01/UpdateInvoiceUnit)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
