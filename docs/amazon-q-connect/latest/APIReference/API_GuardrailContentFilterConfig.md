---
source_url: https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_GuardrailContentFilterConfig.html
---

# GuardrailContentFilterConfig
<a name="API_amazon-q-connect_GuardrailContentFilterConfig"></a>

Contains filter strengths for harmful content. AI Guardrail's support the following content filters to detect and filter harmful user inputs and FM-generated outputs.
+  **Hate**: Describes input prompts and model responses that discriminate, criticize, insult, denounce, or dehumanize a person or group on the basis of an identity (such as race, ethnicity, gender, religion, sexual orientation, ability, and national origin).
+  **Insults**: Describes input prompts and model responses that includes demeaning, humiliating, mocking, insulting, or belittling language. This type of language is also labeled as bullying.
+  **Sexual**: Describes input prompts and model responses that indicates sexual interest, activity, or arousal using direct or indirect references to body parts, physical traits, or sex.
+  **Violence**: Describes input prompts and model responses that includes glorification of, or threats to inflict physical pain, hurt, or injury toward a person, group, or thing.

Content filtering depends on the confidence classification of user inputs and FM responses across each of the four harmful categories. All input and output statements are classified into one of four confidence levels (NONE, LOW, MEDIUM, HIGH) for each harmful category. For example, if a statement is classified as *Hate* with HIGH confidence, the likelihood of the statement representing hateful content is high. A single statement can be classified across multiple categories with varying confidence levels. For example, a single statement can be classified as *Hate* with HIGH confidence, * Insults* with LOW confidence, *Sexual* with NONE confidence, and *Violence* with MEDIUM confidence.

## Contents
<a name="API_amazon-q-connect_GuardrailContentFilterConfig_Contents"></a>

 ** inputStrength **   <a name="connect-Type-amazon-q-connect_GuardrailContentFilterConfig-inputStrength"></a>
The strength of the content filter to apply to prompts. As you increase the filter strength, the likelihood of filtering harmful content increases and the probability of seeing harmful content in your application reduces.
Type: String
Valid Values: `NONE | LOW | MEDIUM | HIGH`
Required: Yes

 ** outputStrength **   <a name="connect-Type-amazon-q-connect_GuardrailContentFilterConfig-outputStrength"></a>
The strength of the content filter to apply to model responses. As you increase the filter strength, the likelihood of filtering harmful content increases and the probability of seeing harmful content in your application reduces.
Type: String
Valid Values: `NONE | LOW | MEDIUM | HIGH`
Required: Yes

 ** type **   <a name="connect-Type-amazon-q-connect_GuardrailContentFilterConfig-type"></a>
The harmful category that the content filter is applied to.
Type: String
Valid Values: `SEXUAL | VIOLENCE | HATE | INSULTS | MISCONDUCT | PROMPT_ATTACK`
Required: Yes

## See Also
<a name="API_amazon-q-connect_GuardrailContentFilterConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/GuardrailContentFilterConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/GuardrailContentFilterConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/GuardrailContentFilterConfig)
