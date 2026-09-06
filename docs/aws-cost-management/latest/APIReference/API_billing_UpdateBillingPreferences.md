---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_UpdateBillingPreferences.html
---

# UpdateBillingPreferences
<a name="API_billing_UpdateBillingPreferences"></a>

Updates billing preferences for the specified feature. Each feature targets a distinct billing capability and has its own set of supported keys. The action sets the value for each provided key; keys not present in the request are unchanged.

Sharing keys (`RI_SHARING`, `CREDIT_SHARING`, `CREDIT_LEVEL_SHARING`, and sharing keys under `CREDIT_PREFERENCE_OPTIONS`) may only be set by the management account of a consolidated billing family. The `credit/{creditId}/status` key may be set by member accounts for credits they own, or by the management account for any credit in the family.

## Request Syntax
<a name="API_billing_UpdateBillingPreferences_RequestSyntax"></a>

```
{
   "billingPreferencesPerKey": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ],
   "feature": "{{string}}"
}
```

## Request Parameters
<a name="API_billing_UpdateBillingPreferences_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [billingPreferencesPerKey](#API_billing_UpdateBillingPreferences_RequestSyntax) **   <a name="awscostmanagement-billing_UpdateBillingPreferences-request-billingPreferencesPerKey"></a>
Key/value pairs to apply. All keys in a single request must be valid for the specified `feature` and must not be duplicated. For `CREDIT_PREFERENCE_OPTIONS`, all keys must reference the same `creditId`.
Type: Array of [BillingPreferenceForKey](API_billing_BillingPreferenceForKey.md) objects
Array Members: Minimum number of 1 item.
Required: Yes

 ** [feature](#API_billing_UpdateBillingPreferences_RequestSyntax) **   <a name="awscostmanagement-billing_UpdateBillingPreferences-request-feature"></a>
The feature to update. Valid values: `BILLING_ALERTS`, `RI_SHARING`, `CREDIT_SHARING`, `CREDIT_LEVEL_SHARING`, `CREDIT_PREFERENCE_OPTIONS`. The history features (`RI_SHARING_HISTORY` and `CREDIT_SHARING_HISTORY`) are read-only and cannot be updated.
Type: String
Valid Values: `RI_SHARING | RI_SHARING_HISTORY | CREDIT_SHARING | CREDIT_SHARING_HISTORY | CREDIT_LEVEL_SHARING | BILLING_ALERTS | CREDIT_PREFERENCE_OPTIONS`
Required: Yes

## Response Elements
<a name="API_billing_UpdateBillingPreferences_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_billing_UpdateBillingPreferences_Errors"></a>

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
<a name="API_billing_UpdateBillingPreferences_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/billing-2023-09-07/UpdateBillingPreferences)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/billing-2023-09-07/UpdateBillingPreferences)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billing-2023-09-07/UpdateBillingPreferences)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/billing-2023-09-07/UpdateBillingPreferences)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billing-2023-09-07/UpdateBillingPreferences)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/billing-2023-09-07/UpdateBillingPreferences)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/billing-2023-09-07/UpdateBillingPreferences)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/billing-2023-09-07/UpdateBillingPreferences)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/billing-2023-09-07/UpdateBillingPreferences)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billing-2023-09-07/UpdateBillingPreferences)
