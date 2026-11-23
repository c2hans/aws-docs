---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_payments_BusinessUnit.html
---

# BusinessUnit

The AWS business unit that issued a financial record. A business unit has two parts: the merchant of record, which is the AWS entity that issued the record, and the line of business within that entity.

## Contents
<a name="API_payments_BusinessUnit_Contents"></a>

 ** merchantOfRecord **   <a name="awscostmanagement-Type-payments_BusinessUnit-merchantOfRecord"></a>
The AWS entity that issued the invoice and collects payment for it, such as `Amazon Web Services, Inc.` or `Amazon Web Services EMEA SARL`. This is the invoicing entity shown in the AWS Billing and Cost Management console. For AWS Marketplace purchases, it can differ from the seller of record.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** lineOfBusiness **   <a name="awscostmanagement-Type-payments_BusinessUnit-lineOfBusiness"></a>
The line of business within the merchant of record that issued the record. This member is absent when the line of business isn't known for the record. The following values are valid:
+  `AWS_CLOUD_SERVICES` – Your usage of AWS services.
+  `PROSERVE_MARKETING_AND_TRAINING` – AWS Professional Services, marketing, and training: consulting, events, and training that AWS sells.
+  `AWS_MARKETPLACE` – Products that you bought from sellers in AWS Marketplace.
Type: String
Valid Values: `AWS_CLOUD_SERVICES | PROSERVE_MARKETING_AND_TRAINING | AWS_MARKETPLACE`
Required: No

## See Also
<a name="API_payments_BusinessUnit_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payments-2026-09-23/BusinessUnit)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payments-2026-09-23/BusinessUnit)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payments-2026-09-23/BusinessUnit)
