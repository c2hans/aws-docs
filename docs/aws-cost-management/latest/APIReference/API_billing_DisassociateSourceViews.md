---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_DisassociateSourceViews.html
---

# DisassociateSourceViews
<a name="API_billing_DisassociateSourceViews"></a>

 Removes the association between one or more source billing views and an existing billing view. This allows modifying the composition of aggregate billing views.

## Request Syntax
<a name="API_billing_DisassociateSourceViews_RequestSyntax"></a>

```
{
   "arn": "{{string}}",
   "sourceViews": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_billing_DisassociateSourceViews_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [arn](#API_billing_DisassociateSourceViews_RequestSyntax) **   <a name="awscostmanagement-billing_DisassociateSourceViews-request-arn"></a>
 The Amazon Resource Name (ARN) of the billing view to disassociate source views from.
Type: String
Pattern: `arn:aws[a-z-]*:(billing)::[0-9]{12}:billingview/[a-zA-Z0-9/:_\+=\.\-@]{0,75}[a-zA-Z0-9]`
Required: Yes

 ** [sourceViews](#API_billing_DisassociateSourceViews_RequestSyntax) **   <a name="awscostmanagement-billing_DisassociateSourceViews-request-sourceViews"></a>
 A list of ARNs of the source billing views to disassociate.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Pattern: `arn:aws[a-z-]*:(billing)::[0-9]{12}:billingview/[a-zA-Z0-9/:_\+=\.\-@]{0,75}[a-zA-Z0-9]`
Required: Yes

## Response Syntax
<a name="API_billing_DisassociateSourceViews_ResponseSyntax"></a>

```
{
   "arn": "string"
}
```

## Response Elements
<a name="API_billing_DisassociateSourceViews_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_billing_DisassociateSourceViews_ResponseSyntax) **   <a name="awscostmanagement-billing_DisassociateSourceViews-response-arn"></a>
 The ARN of the billing view that the source views were disassociated from.
Type: String
Pattern: `arn:aws[a-z-]*:(billing)::[0-9]{12}:billingview/[a-zA-Z0-9/:_\+=\.\-@]{0,75}[a-zA-Z0-9]`

## Errors
<a name="API_billing_DisassociateSourceViews_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this action.
HTTP Status Code: 400

 ** BillingViewHealthStatusException **
 Exception thrown when a billing view's health status prevents an operation from being performed. This may occur if the billing view is in a state other than `HEALTHY`.
HTTP Status Code: 400

 ** ConflictException **
 The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request.
 ** resourceId **
 The identifier for the service resource associated with the request.
 ** resourceType **
 The type of resource associated with the request.
HTTP Status Code: 400

 ** InternalServerException **
The request processing failed because of an unknown error, exception, or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
 The specified ARN in the request doesn't exist.
 ** resourceId **
 Value is a list of resource IDs that were not found.
 ** resourceType **
 Value is the type of resource that was not found.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 400

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
 ** fieldList **
The input fails to satisfy the constraints specified by an AWS service.
 ** reason **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_billing_DisassociateSourceViews_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/billing-2023-09-07/DisassociateSourceViews)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/billing-2023-09-07/DisassociateSourceViews)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billing-2023-09-07/DisassociateSourceViews)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/billing-2023-09-07/DisassociateSourceViews)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billing-2023-09-07/DisassociateSourceViews)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/billing-2023-09-07/DisassociateSourceViews)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/billing-2023-09-07/DisassociateSourceViews)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/billing-2023-09-07/DisassociateSourceViews)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/billing-2023-09-07/DisassociateSourceViews)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billing-2023-09-07/DisassociateSourceViews)
