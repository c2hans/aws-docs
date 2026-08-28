---
source_url: https://docs.aws.amazon.com/comprehend/latest/APIReference/API_EntityLabel.html
---

# EntityLabel
<a name="API_EntityLabel"></a>

Specifies one of the label or labels that categorize the personally identifiable information (PII) entity being analyzed.

## Contents
<a name="API_EntityLabel_Contents"></a>

 ** Name **   <a name="comprehend-Type-EntityLabel-Name"></a>
The name of the label.
Type: String
Valid Values: `BANK_ACCOUNT_NUMBER | BANK_ROUTING | CREDIT_DEBIT_NUMBER | CREDIT_DEBIT_CVV | CREDIT_DEBIT_EXPIRY | PIN | EMAIL | ADDRESS | NAME | PHONE | SSN | DATE_TIME | PASSPORT_NUMBER | DRIVER_ID | URL | AGE | USERNAME | PASSWORD | AWS_ACCESS_KEY | AWS_SECRET_KEY | IP_ADDRESS | MAC_ADDRESS | ALL | LICENSE_PLATE | VEHICLE_IDENTIFICATION_NUMBER | UK_NATIONAL_INSURANCE_NUMBER | CA_SOCIAL_INSURANCE_NUMBER | US_INDIVIDUAL_TAX_IDENTIFICATION_NUMBER | UK_UNIQUE_TAXPAYER_REFERENCE_NUMBER | IN_PERMANENT_ACCOUNT_NUMBER | IN_NREGA | INTERNATIONAL_BANK_ACCOUNT_NUMBER | SWIFT_CODE | UK_NATIONAL_HEALTH_SERVICE_NUMBER | CA_HEALTH_NUMBER | IN_AADHAAR | IN_VOTER_NUMBER`
Required: No

 ** Score **   <a name="comprehend-Type-EntityLabel-Score"></a>
The level of confidence that Amazon Comprehend has in the accuracy of the detection.
Type: Float
Required: No

## See Also
<a name="API_EntityLabel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehend-2017-11-27/EntityLabel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehend-2017-11-27/EntityLabel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehend-2017-11-27/EntityLabel)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Comprehend. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query comprehend` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
