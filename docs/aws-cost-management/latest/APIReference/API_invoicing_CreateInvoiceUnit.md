---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_CreateInvoiceUnit.html
---

# CreateInvoiceUnit
<a name="API_invoicing_CreateInvoiceUnit"></a>

This creates a new invoice unit with the provided definition.

## Request Syntax
<a name="API_invoicing_CreateInvoiceUnit_RequestSyntax"></a>

```
{
   "ClientToken": "{{string}}",
   "Description": "{{string}}",
   "InvoiceReceiver": "{{string}}",
   "Name": "{{string}}",
   "ResourceTags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "Rule": {
      "BillSourceAccounts": [ "{{string}}" ],
      "LinkedAccounts": [ "{{string}}" ]
   },
   "TaxInheritanceDisabled": {{boolean}}
}
```

## Request Parameters
<a name="API_invoicing_CreateInvoiceUnit_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientToken](#API_invoicing_CreateInvoiceUnit_RequestSyntax) **   <a name="awscostmanagement-invoicing_CreateInvoiceUnit-request-ClientToken"></a>
 A unique, case-sensitive identifier that you provide to ensure idempotency of the request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `\S+`
Required: No

 ** [Description](#API_invoicing_CreateInvoiceUnit_RequestSyntax) **   <a name="awscostmanagement-invoicing_CreateInvoiceUnit-request-Description"></a>
 The invoice unit's description. This can be changed at a later time.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Pattern: `[\S\s]*`
Required: No

 ** [InvoiceReceiver](#API_invoicing_CreateInvoiceUnit_RequestSyntax) **   <a name="awscostmanagement-invoicing_CreateInvoiceUnit-request-InvoiceReceiver"></a>
 The AWS account ID chosen to be the receiver of an invoice unit. All invoices generated for that invoice unit will be sent to this account ID.
Type: String
Pattern: `\d{12}`
Required: Yes

 ** [Name](#API_invoicing_CreateInvoiceUnit_RequestSyntax) **   <a name="awscostmanagement-invoicing_CreateInvoiceUnit-request-Name"></a>
 The unique name of the invoice unit that is shown on the generated invoice. This can't be changed once it is set. To change this name, you must delete the invoice unit recreate.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `(?! )[\p{L}\p{N}\p{Z}-_]*(?<! )`
Required: Yes

 ** [ResourceTags](#API_invoicing_CreateInvoiceUnit_RequestSyntax) **   <a name="awscostmanagement-invoicing_CreateInvoiceUnit-request-ResourceTags"></a>
 The tag structure that contains a tag key and value.
Type: Array of [ResourceTag](API_invoicing_ResourceTag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

 ** [Rule](#API_invoicing_CreateInvoiceUnit_RequestSyntax) **   <a name="awscostmanagement-invoicing_CreateInvoiceUnit-request-Rule"></a>
The `InvoiceUnitRule` object used to create invoice units.
Type: [InvoiceUnitRule](API_invoicing_InvoiceUnitRule.md) object
Required: Yes

 ** [TaxInheritanceDisabled](#API_invoicing_CreateInvoiceUnit_RequestSyntax) **   <a name="awscostmanagement-invoicing_CreateInvoiceUnit-request-TaxInheritanceDisabled"></a>
Whether the invoice unit based tax inheritance is/ should be enabled or disabled.
Type: Boolean
Required: No

## Response Syntax
<a name="API_invoicing_CreateInvoiceUnit_ResponseSyntax"></a>

```
{
   "InvoiceUnitArn": "string"
}
```

## Response Elements
<a name="API_invoicing_CreateInvoiceUnit_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [InvoiceUnitArn](#API_invoicing_CreateInvoiceUnit_ResponseSyntax) **   <a name="awscostmanagement-invoicing_CreateInvoiceUnit-response-InvoiceUnitArn"></a>
 The ARN to identify an invoice unit. This information can't be modified or deleted.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `arn:aws[-a-z0-9]*:[a-z0-9]+:[-a-z0-9]*:[0-9]{12}:[-a-zA-Z0-9/:_]+`

## Errors
<a name="API_invoicing_CreateInvoiceUnit_Errors"></a>

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
<a name="API_invoicing_CreateInvoiceUnit_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/invoicing-2024-12-01/CreateInvoiceUnit)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/invoicing-2024-12-01/CreateInvoiceUnit)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/invoicing-2024-12-01/CreateInvoiceUnit)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/invoicing-2024-12-01/CreateInvoiceUnit)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/invoicing-2024-12-01/CreateInvoiceUnit)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/invoicing-2024-12-01/CreateInvoiceUnit)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/invoicing-2024-12-01/CreateInvoiceUnit)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/invoicing-2024-12-01/CreateInvoiceUnit)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/invoicing-2024-12-01/CreateInvoiceUnit)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/invoicing-2024-12-01/CreateInvoiceUnit)
