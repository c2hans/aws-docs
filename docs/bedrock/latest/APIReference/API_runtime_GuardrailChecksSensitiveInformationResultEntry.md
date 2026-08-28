---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_GuardrailChecksSensitiveInformationResultEntry.html
---

# GuardrailChecksSensitiveInformationResultEntry
<a name="API_runtime_GuardrailChecksSensitiveInformationResultEntry"></a>

The detection result for a single sensitive information entity found in the evaluated messages.

## Contents
<a name="API_runtime_GuardrailChecksSensitiveInformationResultEntry_Contents"></a>

 ** beginOffset **   <a name="bedrock-Type-runtime_GuardrailChecksSensitiveInformationResultEntry-beginOffset"></a>
The start character offset of the detected entity within the content block.
Type: Integer
Valid Range: Minimum value of 0.
Required: Yes

 ** confidenceScore **   <a name="bedrock-Type-runtime_GuardrailChecksSensitiveInformationResultEntry-confidenceScore"></a>
The confidence score for the detection, ranging from 0.0 to 1.0. Higher values indicate greater confidence.
Type: Double
Valid Range: Minimum value of 0.0. Maximum value of 1.0.
Required: Yes

 ** contentIndex **   <a name="bedrock-Type-runtime_GuardrailChecksSensitiveInformationResultEntry-contentIndex"></a>
The zero-based index of the content block within the message where the entity was detected.
Type: Integer
Valid Range: Minimum value of 0.
Required: Yes

 ** endOffset **   <a name="bedrock-Type-runtime_GuardrailChecksSensitiveInformationResultEntry-endOffset"></a>
The end character offset of the detected entity within the content block.
Type: Integer
Valid Range: Minimum value of 0.
Required: Yes

 ** messageIndex **   <a name="bedrock-Type-runtime_GuardrailChecksSensitiveInformationResultEntry-messageIndex"></a>
The zero-based index of the message in the input messages array where the entity was detected.
Type: Integer
Valid Range: Minimum value of 0.
Required: Yes

 ** type **   <a name="bedrock-Type-runtime_GuardrailChecksSensitiveInformationResultEntry-type"></a>
The PII entity type that was detected.
Type: String
Valid Values: `ADDRESS | AGE | AWS_ACCESS_KEY | AWS_SECRET_KEY | CA_HEALTH_NUMBER | CA_SOCIAL_INSURANCE_NUMBER | CREDIT_DEBIT_CARD_CVV | CREDIT_DEBIT_CARD_EXPIRY | CREDIT_DEBIT_CARD_NUMBER | DRIVER_ID | EMAIL | INTERNATIONAL_BANK_ACCOUNT_NUMBER | IP_ADDRESS | LICENSE_PLATE | MAC_ADDRESS | NAME | PASSWORD | PHONE | PIN | SWIFT_CODE | UK_NATIONAL_HEALTH_SERVICE_NUMBER | UK_NATIONAL_INSURANCE_NUMBER | UK_UNIQUE_TAXPAYER_REFERENCE_NUMBER | URL | USERNAME | US_BANK_ACCOUNT_NUMBER | US_BANK_ROUTING_NUMBER | US_INDIVIDUAL_TAX_IDENTIFICATION_NUMBER | US_PASSPORT_NUMBER | US_SOCIAL_SECURITY_NUMBER | VEHICLE_IDENTIFICATION_NUMBER`
Required: Yes

## See Also
<a name="API_runtime_GuardrailChecksSensitiveInformationResultEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-runtime-2023-09-30/GuardrailChecksSensitiveInformationResultEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-runtime-2023-09-30/GuardrailChecksSensitiveInformationResultEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-runtime-2023-09-30/GuardrailChecksSensitiveInformationResultEntry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
