---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_freetier_GetAccountPlanState.html
---

# GetAccountPlanState
<a name="API_freetier_GetAccountPlanState"></a>

 This returns all of the information related to the state of the account plan related to Free Tier.

## Response Syntax
<a name="API_freetier_GetAccountPlanState_ResponseSyntax"></a>

```
{
   "accountId": "string",
   "accountPlanExpirationDate": "string",
   "accountPlanRemainingCredits": {
      "amount": number,
      "unit": "string"
   },
   "accountPlanStatus": "string",
   "accountPlanType": "string"
}
```

## Response Elements
<a name="API_freetier_GetAccountPlanState_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [accountId](#API_freetier_GetAccountPlanState_ResponseSyntax) **   <a name="awscostmanagement-freetier_GetAccountPlanState-response-accountId"></a>
 A unique identifier that identifies the account.
Type: String
Pattern: `[0-9]{12}`

 ** [accountPlanExpirationDate](#API_freetier_GetAccountPlanState_ResponseSyntax) **   <a name="awscostmanagement-freetier_GetAccountPlanState-response-accountPlanExpirationDate"></a>
 The timestamp for when the current account plan expires.
Type: Timestamp

 ** [accountPlanRemainingCredits](#API_freetier_GetAccountPlanState_ResponseSyntax) **   <a name="awscostmanagement-freetier_GetAccountPlanState-response-accountPlanRemainingCredits"></a>
 The amount of credits remaining for the account.
Type: [MonetaryAmount](API_freetier_MonetaryAmount.md) object

 ** [accountPlanStatus](#API_freetier_GetAccountPlanState_ResponseSyntax) **   <a name="awscostmanagement-freetier_GetAccountPlanState-response-accountPlanStatus"></a>
 The current status for the account plan.
Type: String
Valid Values: `NOT_STARTED | ACTIVE | EXPIRED`

 ** [accountPlanType](#API_freetier_GetAccountPlanState_ResponseSyntax) **   <a name="awscostmanagement-freetier_GetAccountPlanState-response-accountPlanType"></a>
 The plan type for the account.
Type: String
Valid Values: `FREE | PAID`

## Errors
<a name="API_freetier_GetAccountPlanState_Errors"></a>

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
<a name="API_freetier_GetAccountPlanState_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/freetier-2023-09-07/GetAccountPlanState)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/freetier-2023-09-07/GetAccountPlanState)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/freetier-2023-09-07/GetAccountPlanState)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/freetier-2023-09-07/GetAccountPlanState)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/freetier-2023-09-07/GetAccountPlanState)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/freetier-2023-09-07/GetAccountPlanState)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/freetier-2023-09-07/GetAccountPlanState)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/freetier-2023-09-07/GetAccountPlanState)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/freetier-2023-09-07/GetAccountPlanState)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/freetier-2023-09-07/GetAccountPlanState)
