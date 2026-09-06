---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-banking-modernization-clm/strategy-faq.html
---

# FAQ
<a name="strategy-faq"></a>

## How can I be sure that AWS services won't store any personal data?
<a name="how-can-i-be-sure-that-aws-services-won-t-store-any-personal-data-.59459320-5e6a-51af-b3f2-af871f16d81d"></a>

You can use AWS Config to check the compliance of the architecture components in combination with Macie to detect and remediate any personal data that's discovered.

## Is the architecture compliant with GDPR?
<a name="is-the-architecture-compliant-with-gdpr-.767c0c2e-212b-5fcb-80b2-4457e75954dd"></a>

Yes, as per GDPR Chapter 2, [Article 5](https://gdpr-info.eu/art-5-gdpr/), the architecture is designed not to retain any data related to the user in the long term but only to processes PII. This is ensured through continuous compliance mechanisms. Additionally, Macie ensures tagging and classification of any PII data that could endanger GDPR compliance.

## How can I ensure proper data confidentiality?
<a name="how-can-i-ensure-proper-data-confidentiality-.f2f75246-ff2c-511d-9bfa-10620ed461b2"></a>

Confidentiality is ensured through continuous compliance and security patterns by using Security Hub, AWS Config, and Macie. Confidentiality breaches are immediately detected, remediated, and escalated. We also recommend that you add guardrails at the deployment phase. Guardrails help ensure that no critical change that could endanger confidentiality gets pushed to the architecture.

## Can I integrate an AWS banking modernization solution with any legacy banking system?
<a name="can-i-integrate-an-aws-banking-modernization-solution-with-any-legacy-banking-system-.58ff42f1-90c0-5d81-98a7-5f0e97bf6555"></a>

The solution is designed to be adaptable and can integrate with any legacy banking system that can accept standard API calls.

## Can I customize the onboarding dialog?
<a name="can-i-customize-the-onboarding-dialog-.5d5b29b4-3818-595f-8a81-a313e20ac09c"></a>

Yes, you can customize the chatbot dialog to fit your use case and targeted dialog sequence. For more information, see [QnA Bot on AWS](https://aws.amazon.com/solutions/implementations/aws-qnabot/) in the AWS Solutions Library.
