---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_GetInvoiceUnit.html
---

# GetInvoiceUnit
<a name="API_invoicing_GetInvoiceUnit"></a>

This retrieves the invoice unit definition.

## Request Syntax
<a name="API_invoicing_GetInvoiceUnit_RequestSyntax"></a>

```
{
   "AsOf": {{number}},
   "InvoiceUnitArn": "{{string}}"
}
```

## Request Parameters
<a name="API_invoicing_GetInvoiceUnit_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AsOf](#API_invoicing_GetInvoiceUnit_RequestSyntax) **   <a name="awscostmanagement-invoicing_GetInvoiceUnit-request-AsOf"></a>
 The state of an invoice unit at a specified time. You can see legacy invoice units that are currently deleted if the `AsOf` time is set to before it was deleted. If an `AsOf` is not provided, the default value is the current time.
Type: Timestamp
Required: No

 ** [InvoiceUnitArn](#API_invoicing_GetInvoiceUnit_RequestSyntax) **   <a name="awscostmanagement-invoicing_GetInvoiceUnit-request-InvoiceUnitArn"></a>
 The ARN to identify an invoice unit. This information can't be modified or deleted.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `arn:aws[-a-z0-9]*:[a-z0-9]+:[-a-z0-9]*:[0-9]{12}:[-a-zA-Z0-9/:_]+`
Required: Yes

## Response Syntax
<a name="API_invoicing_GetInvoiceUnit_ResponseSyntax"></a>

```
{
   "Description": "string",
   "InvoiceReceiver": "string",
   "InvoiceUnitArn": "string",
   "LastModified": number,
   "Name": "string",
   "Rule": {
      "BillSourceAccounts": [ "string" ],
      "LinkedAccounts": [ "string" ]
   },
   "TaxInheritanceDisabled": boolean
}
```

## Response Elements
<a name="API_invoicing_GetInvoiceUnit_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Description](#API_invoicing_GetInvoiceUnit_ResponseSyntax) **   <a name="awscostmanagement-invoicing_GetInvoiceUnit-response-Description"></a>
 The assigned description for an invoice unit.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Pattern: `[\S\s]*`

 ** [InvoiceReceiver](#API_invoicing_GetInvoiceUnit_ResponseSyntax) **   <a name="awscostmanagement-invoicing_GetInvoiceUnit-response-InvoiceReceiver"></a>
 The AWS account ID chosen to be the receiver of an invoice unit. All invoices generated for that invoice unit will be sent to this account ID.
Type: String
Pattern: `\d{12}`

 ** [InvoiceUnitArn](#API_invoicing_GetInvoiceUnit_ResponseSyntax) **   <a name="awscostmanagement-invoicing_GetInvoiceUnit-response-InvoiceUnitArn"></a>
 The ARN to identify an invoice unit. This information can't be modified or deleted.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `arn:aws[-a-z0-9]*:[a-z0-9]+:[-a-z0-9]*:[0-9]{12}:[-a-zA-Z0-9/:_]+`

 ** [LastModified](#API_invoicing_GetInvoiceUnit_ResponseSyntax) **   <a name="awscostmanagement-invoicing_GetInvoiceUnit-response-LastModified"></a>
 The most recent date the invoice unit response was updated.
Type: Timestamp

 ** [Name](#API_invoicing_GetInvoiceUnit_ResponseSyntax) **   <a name="awscostmanagement-invoicing_GetInvoiceUnit-response-Name"></a>
 The unique name of the invoice unit that is shown on the generated invoice.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `(?! )[\p{L}\p{N}\p{Z}-_]*(?<! )`

 ** [Rule](#API_invoicing_GetInvoiceUnit_ResponseSyntax) **   <a name="awscostmanagement-invoicing_GetInvoiceUnit-response-Rule"></a>
 This is used to categorize the invoice unit. Values are AWS account IDs. Currently, the only supported rule is `LINKED_ACCOUNT`.
Type: [InvoiceUnitRule](API_invoicing_InvoiceUnitRule.md) object

 ** [TaxInheritanceDisabled](#API_invoicing_GetInvoiceUnit_ResponseSyntax) **   <a name="awscostmanagement-invoicing_GetInvoiceUnit-response-TaxInheritanceDisabled"></a>
 Whether the invoice unit based tax inheritance is/ should be enabled or disabled.
Type: Boolean

## Errors
<a name="API_invoicing_GetInvoiceUnit_Errors"></a>

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
<a name="API_invoicing_GetInvoiceUnit_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/invoicing-2024-12-01/GetInvoiceUnit)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/invoicing-2024-12-01/GetInvoiceUnit)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/invoicing-2024-12-01/GetInvoiceUnit)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/invoicing-2024-12-01/GetInvoiceUnit)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/invoicing-2024-12-01/GetInvoiceUnit)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/invoicing-2024-12-01/GetInvoiceUnit)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/invoicing-2024-12-01/GetInvoiceUnit)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/invoicing-2024-12-01/GetInvoiceUnit)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/invoicing-2024-12-01/GetInvoiceUnit)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/invoicing-2024-12-01/GetInvoiceUnit)
