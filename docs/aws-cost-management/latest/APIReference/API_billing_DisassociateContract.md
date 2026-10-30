---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_DisassociateContract.html
---

# DisassociateContract
<a name="API_billing_DisassociateContract"></a>

Removes the association between a private pricing contract and your AWS account. The account must have been associated with the contract previously. This operation is idempotent, so retrying is safe.

## Request Syntax
<a name="API_billing_DisassociateContract_RequestSyntax"></a>

```
{
   "contractArn": "{{string}}"
}
```

## Request Parameters
<a name="API_billing_DisassociateContract_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [contractArn](#API_billing_DisassociateContract_RequestSyntax) **   <a name="awscostmanagement-billing_DisassociateContract-request-contractArn"></a>
The Amazon Resource Name (ARN) of the contract to disassociate from your account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Pattern: `arn:aws[a-z-]*:billing::[0-9]{12}:contract/[a-zA-Z0-9_\+=\.\@-]{0,70}[a-zA-Z0-9]`
Required: Yes

## Response Elements
<a name="API_billing_DisassociateContract_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_billing_DisassociateContract_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this action.
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
<a name="API_billing_DisassociateContract_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/billing-2023-09-07/DisassociateContract)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/billing-2023-09-07/DisassociateContract)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billing-2023-09-07/DisassociateContract)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/billing-2023-09-07/DisassociateContract)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billing-2023-09-07/DisassociateContract)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/billing-2023-09-07/DisassociateContract)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/billing-2023-09-07/DisassociateContract)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/billing-2023-09-07/DisassociateContract)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/billing-2023-09-07/DisassociateContract)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billing-2023-09-07/DisassociateContract)
