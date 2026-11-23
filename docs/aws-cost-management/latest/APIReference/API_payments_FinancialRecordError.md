---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_payments_FinancialRecordError.html
---

# FinancialRecordError

The reason that one of the records requested from `BatchGetFinancialRecord` couldn't be returned. The other records in the request are unaffected.

## Contents
<a name="API_payments_FinancialRecordError_Contents"></a>

 ** code **   <a name="awscostmanagement-Type-payments_FinancialRecordError-code"></a>
The error code that indicates why the retrieval failed. The following values are valid:
+  `NOT_FOUND` – No financial record on your account matches the key.
+  `INTERNAL_ERROR` – An internal error occurred while processing this record. The other records in the request are unaffected. You can retry this record.
Type: String
Valid Values: `NOT_FOUND | INTERNAL_ERROR`
Required: Yes

 ** key **   <a name="awscostmanagement-Type-payments_FinancialRecordError-key"></a>
The key of the record that couldn't be retrieved, as you requested it.
Type: [FinancialRecordKey](API_payments_FinancialRecordKey.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** message **   <a name="awscostmanagement-Type-payments_FinancialRecordError-message"></a>
A description of why the operation couldn't retrieve this record. The wording can change at any time and isn't localized, so don't parse this value. To handle the error in your code, use `code` instead.
Type: String
Required: Yes

## See Also
<a name="API_payments_FinancialRecordError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payments-2026-09-23/FinancialRecordError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payments-2026-09-23/FinancialRecordError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payments-2026-09-23/FinancialRecordError)
