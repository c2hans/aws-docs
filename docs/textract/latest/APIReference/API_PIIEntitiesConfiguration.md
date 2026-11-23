---
source_url: https://docs.aws.amazon.com/textract/latest/APIReference/API_PIIEntitiesConfiguration.html
---

# PIIEntitiesConfiguration

Specifies which personally identifiable information (PII) entity types to detect and how to mask them.

## Contents
<a name="API_PIIEntitiesConfiguration_Contents"></a>

 ** PiiEntityTypes **   <a name="Textract-Type-PIIEntitiesConfiguration-PiiEntityTypes"></a>
The list of PII entity types to detect. Each type can appear only once.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 32 items.
Valid Values: `ALL | ADDRESS | AGE | NAME | EMAIL | PHONE | USERNAME | PASSWORD | DRIVER_ID | LICENSE_PLATE | VEHICLE_IDENTIFICATION_NUMBER | CREDIT_DEBIT_CARD_CVV | CREDIT_DEBIT_CARD_EXPIRY | CREDIT_DEBIT_CARD_NUMBER | PIN | INTERNATIONAL_BANK_ACCOUNT_NUMBER | SWIFT_CODE | IP_ADDRESS | MAC_ADDRESS | URL | AWS_ACCESS_KEY | AWS_SECRET_KEY | US_BANK_ACCOUNT_NUMBER | US_BANK_ROUTING_NUMBER | US_INDIVIDUAL_TAX_IDENTIFICATION_NUMBER | US_PASSPORT_NUMBER | US_SOCIAL_SECURITY_NUMBER | CA_HEALTH_NUMBER | CA_SOCIAL_INSURANCE_NUMBER | UK_NATIONAL_HEALTH_SERVICE_NUMBER | UK_NATIONAL_INSURANCE_NUMBER | UK_UNIQUE_TAXPAYER_REFERENCE_NUMBER`
Required: Yes

 ** RedactionMaskMode **   <a name="Textract-Type-PIIEntitiesConfiguration-RedactionMaskMode"></a>
How detected PII is masked in the redacted output.
Type: String
Valid Values: `PII | ENTITY_TYPE`
Required: Yes

## See Also
<a name="API_PIIEntitiesConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/textract-2018-06-27/PIIEntitiesConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/textract-2018-06-27/PIIEntitiesConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/textract-2018-06-27/PIIEntitiesConfiguration)
