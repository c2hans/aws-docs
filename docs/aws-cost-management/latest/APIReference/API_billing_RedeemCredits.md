---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_RedeemCredits.html
---

# RedeemCredits
<a name="API_billing_RedeemCredits"></a>

Redeems an AWS promotional credit code on behalf of the calling account. On success, a new credit is added to the account's credit ledger with the amount, validity period, and applicable products defined by the promotion. The credit is then automatically applied to subsequent bills according to the standard credit application order.

## Request Syntax
<a name="API_billing_RedeemCredits_RequestSyntax"></a>

```
{
   "promoCode": "{{string}}"
}
```

## Request Parameters
<a name="API_billing_RedeemCredits_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [promoCode](#API_billing_RedeemCredits_RequestSyntax) **   <a name="awscostmanagement-billing_RedeemCredits-request-promoCode"></a>
The promotional credit code to redeem.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.*[^<>"&\%|' ]*.*`
Required: Yes

## Response Elements
<a name="API_billing_RedeemCredits_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_billing_RedeemCredits_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this action.
HTTP Status Code: 400

 ** InternalServerException **
The request processing failed because of an unknown error, exception, or failure.
HTTP Status Code: 500

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
<a name="API_billing_RedeemCredits_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/billing-2023-09-07/RedeemCredits)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/billing-2023-09-07/RedeemCredits)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billing-2023-09-07/RedeemCredits)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/billing-2023-09-07/RedeemCredits)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billing-2023-09-07/RedeemCredits)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/billing-2023-09-07/RedeemCredits)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/billing-2023-09-07/RedeemCredits)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/billing-2023-09-07/RedeemCredits)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/billing-2023-09-07/RedeemCredits)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billing-2023-09-07/RedeemCredits)
