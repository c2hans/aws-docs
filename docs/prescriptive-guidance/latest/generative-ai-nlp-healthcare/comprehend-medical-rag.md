---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/generative-ai-nlp-healthcare/comprehend-medical-rag.html
---

# Combining Amazon Comprehend Medical with large language models
<a name="comprehend-medical-rag"></a>

A [2024 study by NEJM AI](https://ai.nejm.org/doi/pdf/10.1056/AIdbp2300040) showed that using an LLM, with zero-shot prompting, for medical coding tasks generally leads to poor performance. Using Amazon Comprehend Medical with an LLM can help mitigate these performance issues. Amazon Comprehend Medical results are helpful context for an LLM that is performing NLP tasks. For example, providing context from Amazon Comprehend Medical to the large language model can help you:
+ Enhance the accuracy of entity selections by using the initial results from Amazon Comprehend Medical as context for the LLM
+ Implement custom entity recognition, summarization, question-answering, and additional use cases

This section describes how you can combine Amazon Comprehend Medical with an LLM by using a Retrieval Augmented Generation (RAG) approach. *Retrieval Augmented Generation (RAG)* is a generative AI technology in which an LLM references an authoritative data source that is outside of its training data sources before generating a response. For more information, see [What is RAG](https://aws.amazon.com/what-is/retrieval-augmented-generation/).

To illustrate this approach, this section uses the example of medical (diagnosis) coding related to ICD-10-CM. It includes a sample architecture and prompt engineering templates to help accelerate your innovation. It also includes best practices for using Amazon Comprehend Medical within a RAG workflow.

## RAG-based architecture with Amazon Comprehend Medical
<a name="comprehend-medical-rag-architecture"></a>

The following diagram illustrates a RAG approach for identifying ICD-10-CM diagnosis codes from patient notes. It uses Amazon Comprehend Medical as a knowledge source. In a RAG approach, the retrieval method commonly retrieves information from a vector database containing applicable knowledge. Instead of a vector database, this architecture uses Amazon Comprehend Medical for the retrieval task. The orchestrator sends the patient note information to Amazon Comprehend Medical and retrieves the ICD-10-CM code information. The orchestrator sends this context to the downstream foundation model (LLM), through Amazon Bedrock. The LLM generates a response by using the ICD-10-CM code information, and that response is sent back to the client application.

![A RAG workflow that uses Amazon Comprehend Medical as a knowledge source.](https://docs.aws.amazon.com/prescriptive-guidance/latest/generative-ai-nlp-healthcare/images/guide-img/30175f3c-77fd-446d-b6ec-cdf244f32c6e/images/875f0a6d-c38d-4ca0-b221-cafcb92240a5.png)

The diagram shows the following RAG workflow:

1. The client application sends the patient notes as a query to the orchestrator. An example of these patient notes might be "The patient is a 71-year-old female patient of Dr. X. The patient presented to the emergency room last evening with approximately 7-day to 8-day history of abdominal pain, which has been persistent. She has had no definite fevers or chills and no history of jaundice. The patient denies any significant recent weight loss."

1. The orchestrator uses Amazon Comprehend Medical to retrieve ICD-10-CM codes relevant to the medical information in the query. It uses the **InferICD10CM** API to extract and infer the ICD-10-CM codes from the patient notes.

1. The orchestrator constructs a prompt that includes the prompt template, the original query, and the ICD-10-CM codes retrieved from Amazon Comprehend Medical. It sends this enhanced context to Amazon Bedrock.

1. Amazon Bedrock processes the input and uses a foundation model to generate a response that includes the ICD-10-CM codes and their corresponding evidence from the query. The generated response includes the identified ICD-10-CM codes and evidence from the patient notes that supports each code. The following is a sample response:

   ```
   <response>
   <icd10>
   <code>R10.9</code>
   <evidence>history of abdominal pain</evidence>
   </icd10>
   <icd10>
   <code>R10.30</code>
   <evidence>history of abdominal pain</evidence>
   </icd10>
   </response>
   ```

1. Amazon Bedrock sends the generated response to the orchestrator.

1. The orchestrator sends the response back to the client application, where the user can review the response.

## Use cases for using Amazon Comprehend Medical in a RAG workflow
<a name="comprehend-medical-rag-use-cases"></a>

Amazon Comprehend Medical can perform specific NLP tasks. For more information, see [Use cases for Amazon Comprehend Medical](comprehend-medical.md#comprehend-medical-use-cases).

You might want to integrate Amazon Comprehend Medical into a RAG workflow for advanced use cases, such as the following:
+ Generate detailed clinical summaries by combining extracted medical entities with contextual information from patient records
+ Automate medical coding for complex cases by using extracted entities with ontology-linked information for code assignment
+ Automate the creation of structured clinical notes from unstructured text by using extracted medical entities
+ Analyze medication side effects based on extracted medication names and attributes
+ Develop intelligent clinical support systems that combine extracted medical information with up-to-date research and guidelines

## Best practices for using Amazon Comprehend Medical in a RAG workflow
<a name="comprehend-medical-rag-best-practices"></a>

When integrating Amazon Comprehend Medical results into a prompt for an LLM, it's essential to follow best practices. This can improve performance and accuracy. The following are key recommendations:
+ **Understand Amazon Comprehend Medical confidence scores** – Amazon Comprehend Medical provides confidence scores for each detected entity and ontology linking. It's crucial to understand the meaning of these scores and establish appropriate thresholds for your specific use case. Confidence scores help filter out low-confidence entities, reducing noise and improving the quality of the LLM's input.
+ **Use confidence scores in prompt engineering** – When crafting prompts for the LLM, consider incorporating Amazon Comprehend Medical confidence scores as additional context. This helps the LLM prioritize or weigh entities based on their confidence levels, potentially improving the quality of the output.
+ **Evaluate Amazon Comprehend Medical results with ground truth data** – *Ground truth data* is information that is known to be true. It can be used to validate that an AI/ML application is producing accurate results. Before integrating Amazon Comprehend Medical results into your LLM workflow, evaluate the service's performance on a representative sample of your data. Compare the results with ground truth annotations to identify potential discrepancies or areas for improvement. This evaluation helps you understand the strengths and limitations of Amazon Comprehend Medical for your use case.
+ **Strategically select relevant information** – Amazon Comprehend Medical can provide a large amount of information, but not all of it may be relevant to your task. Carefully select the entities, attributes, and metadata that are most relevant to your use case. Providing too much irrelevant information to the LLM can introduce noise and potentially decrease performance.
+ **Align entity definitions** – Ensure that the definitions of entities and attributes used by Amazon Comprehend Medical align with your interpretation. If there are discrepancies, consider providing additional context or clarification to the LLM to bridge the gap between the Amazon Comprehend Medical output and your requirements. If Amazon Comprehend Medical entity doesn't meet your expectations, you can implement custom entity detection by including additional instructions (and possible examples) within the prompt.
+ **Provide domain-specific knowledge** – While Amazon Comprehend Medical provides valuable medical information, it might not capture all the nuances of your specific domain. Consider supplementing Amazon Comprehend Medical results with additional domain-specific knowledge sources, such as ontologies, terminologies, or expert-curated datasets. This provides more comprehensive context to the LLM.
+ **Adhere to ethical and regulatory guidelines** – When dealing with medical data, it's important to adhere to ethical principles and regulatory guidelines, such as those related to data privacy, security, and responsible use of AI systems in healthcare. Make sure that your implementation complies with relevant laws and industry best practices.

By following these best practices, AI/ML practitioners can effectively use the strengths of both Amazon Comprehend Medical and LLMs. For medical NLP tasks, these best practices help mitigate potential risks and can improve performance.

## Prompt engineering for Amazon Comprehend Medical context
<a name="comprehend-medical-rag-prompt-engineering"></a>

[Prompt engineering](https://aws.amazon.com/what-is/prompt-engineering/) is the process of designing and refining prompts to guide a generative AI solution to generate desired outputs. You choose the most appropriate formats, phrases, words, and symbols that guide the AI to interact with your users more meaningfully.

Depending on the API operation you perform, Amazon Comprehend Medical returns the detected entities, ontology codes and descriptions, and confidence scores. These results become context within the prompt when your solution invokes the target LLM. You must engineer the prompt to present the context within the prompt template.

**Note**
The example prompts in this section follow [Anthropic guidance](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview). If you're using a different LLM provider, follow the recommendations from that provider.

In general, you insert both the original medical text and the Amazon Comprehend Medical results into the prompt. The following is a common prompt structure:

```
<medical_text>
medical text
</medical_text>

<comprehend_medical_text_results>
comprehend medical text results
</comprehend_medical_text_results>

<prompt_instructions>
prompt instructions
</prompt_instructions>
```

This section provides strategies for including Amazon Comprehend Medical results as prompt context for the following common medical NLP tasks:
+ Filter Amazon Comprehend Medical results
+ Extend medical NLP tasks with Amazon Comprehend Medical
+ Apply guardrails with Amazon Comprehend Medical

### Filter Amazon Comprehend Medical results
<a name="filter-9999999999999999cmpm--results.524d0de9-f1ed-5264-beda-18b8f678aac7"></a>

Amazon Comprehend Medical typically provides a large amount of information. You might want to reduce the number of results that the medical professional must review. In this case, you can use an LLM to filter these results. Amazon Comprehend Medical entities include a confidence score that you can use as a filtering mechanism when designing the prompt.

The following is an example patient note:

```
Carlie had a seizure 2 weeks ago. She is complaining of frequent headaches
Nausea is also present. She also complains of eye trouble with blurry vision
Meds : Topamax 50 mgs at breakfast daily,
Send referral order to neurologist
Follow-up as scheduled
```

In this patient note, Amazon Comprehend Medical detects the following entities.

![Entity detection in Amazon Comprehend Medical.](https://docs.aws.amazon.com/prescriptive-guidance/latest/generative-ai-nlp-healthcare/images/guide-img/30175f3c-77fd-446d-b6ec-cdf244f32c6e/images/564b2486-16c9-4676-9417-eab4c91ff9be.png)

The entities link to the following ICD-10-CM codes for seizure and headaches.

|
|
| Category | ICD-10-CM code | ICD-10-CM description | Confidence score |
| --- |--- |--- |--- |
| Seizure | R56.9 | Unspecified convulsions | 0.8348 |
| Seizure | G40.909 | Epilepsy, unspecified, not intractable, without status epilepticus | 0.5424 |
| Seizure | R56.00 | Simple febrile convulsions | 0.4937 |
| Seizure | G40.09 | Other seizures | 0.4397 |
| Seizure | G40.409 | Other generalized epilepsy and epileptic syndromes, not intractable, without status epilepticus | 0.4138 |
| Headaches | R51 | Headache | 0.4067 |
| Headaches | R51.9 | Headache, unspecified | 0.3844 |
| Headaches | G44.52 | New daily persistent headache (NDPH) | 0.3005 |
| Headaches | G44 | Other headache syndrome | 0.2670 |
| Headaches | G44.8 | Other specified headache syndromes | 0.2542 |

You can pass ICD-10-CM codes into the prompt to increase LLM precision. To reduce noise, you can filter the ICD-10-CM codes by using the confidence score included in the Amazon Comprehend Medical results. The following is an example prompt that includes only ICD-10-CM codes that have a confidence score higher than 0.4:

```
<patient_note>
Carlie had a seizure 2 weeks ago. She is complaining of frequent headaches
Nausea is also present. She also complains of eye trouble with blurry vision
Meds : Topamax 50 mgs at breakfast daily,
Send referral order to neurologist
Follow-up as scheduled
</patient_note>

<comprehend_medical_results>
<icd-10>
  <entity>
    <text>seizure</text>
    <code>
      <description>Unspecified convulsions</description>
      <code_value>R56.9</code_value>
      <score>0.8347607851028442</score>
    </code>
    <code>
      <description>Epilepsy, unspecified, not intractable, without status epilepticus</description>
      <code_value>G40.909</code_value>
      <score>0.542376697063446</score>
    </code>
    <code>
      <description>Other seizures</description>
      <code_value>G40.89</code_value>
      <score>0.43966275453567505</score>
    </code>
    <code>
      <description>Other generalized epilepsy and epileptic syndromes, not intractable, without status epilepticus</description>
      <code_value>G40.409</code_value>
      <score>0.41382506489753723</score>
    </code>
  </entity>
  <entity>
    <text>headaches</text>
    <code>
      <description>Headache</description>
      <code_value>R51</code_value>
      <score>0.4066613018512726</score>
    </code>
  </entity>
  <entity>
    <text>Nausea</text>
    <code>
      <description>Nausea</description>
      <code_value>R11.0</code_value>
      <score>0.6460834741592407</score>
    </code>
  </entity>
  <entity>
    <text>eye trouble</text>
    <code>
      <description>Unspecified disorder of eye and adnexa</description>
      <code_value>H57.9</code_value>
      <score>0.6780954599380493</score>
    </code>
    <code>
      <description>Unspecified visual disturbance</description>
      <code_value>H53.9</code_value>
      <score>0.5871203541755676</score>
    </code>
    <code>
      <description>Unspecified disorder of binocular vision</description>
      <code_value>H53.30</code_value>
      <score>0.5539672374725342</score>
    </code>
  </entity>
  <entity>
    <text>blurry vision</text>
    <code>
      <description>Other visual disturbances</description>
      <code_value>H53.8</code_value>
      <score>0.9001834392547607</score>
    </code>
  </entity>
</icd-10>
</comprehend_medical_results>

<prompt>
Given the patient note and Amazon Comprehend Medical ICD-10-CM code results above, please select the most relevant ICD-10-CM diagnosis codes for the patient.
For each selected code, provide a brief explanation of why it is relevant based on the information in the patient note.
</prompt>
```

### Extend medical NLP tasks with Amazon Comprehend Medical
<a name="extend-medical-nlp-tasks-with-9999999999999999cmpm-.b559feba-c172-5097-b137-123863315f40"></a>

When processing medical text, context from Amazon Comprehend Medical can help the LLM to select better tokens. In this example, you want to match diagnosis symptoms to medications. You also want to find text that relates to medical tests, such as terms that relate to a blood panel test. You can use Amazon Comprehend Medical to detect the entities and the medication names. In this case, you would use the [DetectEntitiesV2](https://docs.aws.amazon.com/comprehend-medical/latest/dev/textanalysis-entitiesv2.html) and [InferRxNorm](https://docs.aws.amazon.com/comprehend-medical/latest/dev/ontology-RxNorm.html) APIs for Amazon Comprehend Medical.

The following is an example patient note:

```
Carlie had a seizure 2 weeks ago. She is complaining of increased frequent headaches
Given lyme disease symptoms such as muscle ache and stiff neck will order prescription.
Meds : Topamax 50 mgs at breakfast daily. Amoxicillan 25 mg by mouth twice a day
Place MRI radiology order at RadNet
```

To focus on the diagnosis code, only the entities related to `MEDICAL_CONDITION` with type `DX_NAME` are used in the prompt. Other metadata is excluded due to irrelevance. For medication entities, the medication name along with extracted attributes is included. Other medication entity metadata from Amazon Comprehend Medical is excluded due to irrelevance. The following is an example prompt that uses filtered Amazon Comprehend Medical results. The prompt  focuses on `MEDICAL_CONDITION` entities that have the `DX_NAME` type. This prompt is designed to more precisely link diagnosis codes with medication and more precisely extract medical order tests:

```
<patient_note>
Carlie had a seizure 2 weeks ago. She is complaining of increased freqeunt headaches
Given lyme disease symptoms such as muscle ache and stiff neck will order prescription.
Meds : Topamax 50 mgs at breakfast daily. Amoxicillan 25 mg by mouth twice a day
Place MRI radiology order at RadNet
</patient_note>

<detect_entity_results>
<entity>
    <text>seizure</text>
    <category>MEDICAL_CONDITION</category>
    <type>DX_NAME</type>
</entity>
<entity>
    <text>headaches</text>
    <category>MEDICAL_CONDITION</category>
    <type>DX_NAME</type>
</entity>
<entity>
    <text>lyme disease</text>
    <category>MEDICAL_CONDITION</category>
    <type>DX_NAME</type>
</entity>
<entity>
    <text>muscle ache</text>
    <category>MEDICAL_CONDITION</category>
    <type>DX_NAME</type>
</entity>
<entity>
    <text>stiff neck</text>
    <category>MEDICAL_CONDITION</category>
    <type>DX_NAME</type>
</entity>
</detect_entity_results>

<rx_results>
<entity>
    <text>Topamax</text>
    <category>MEDICATION</category>
    <type>BRAND_NAME</type>
    <attributes>
        <attribute>
            <type>FREQUENCY</type>
            <text>at breakfast daily</text>
        </attribute>
        <attribute>
            <type>DOSAGE</type>
            <text>50 mgs</text>
        </attribute>
        <attribute>
            <type>ROUTE_OR_MODE</type>
            <text>by mouth</text>
        </attribute>
    </attributes>
</entity>
<entity>
    <text>Amoxicillan</text>
    <category>MEDICATION</category>
    <type>GENERIC_NAME</type>
    <attributes>
        <attribute>
            <type>ROUTE_OR_MODE</type>
            <text>by mouth</text>
        </attribute>
        <attribute>
            <type>DOSAGE</type>
            <text>25 mg</text>
        </attribute>
        <attribute>
            <type>FREQUENCY</type>
            <text>twice a day</text>
        </attribute>
    </attributes>
</entity>
</rx_results>

<prompt>
Based on the patient note and the detected entities, can you please:
1. Link the diagnosis symptoms with the medications prescribed.
Provide your reasoning for the linkages.
2. Extract any entities related to medical order tests mentioned in the note.
</prompt>
```

### Apply guardrails with Amazon Comprehend Medical
<a name="apply-guardrails-with-9999999999999999cmpm-.3a705f55-a7fe-5074-aeb6-1fea29ac083d"></a>

You can use an LLM and Amazon Comprehend Medical to create guardrails before the generated response is used. You can run this workflow on either unmodified or post-processed medical text. Use cases include addressing protected health information (PHI), detecting hallucinations, or implementing custom policies for publishing results. For example, you can use context from Amazon Comprehend Medical to identify PHI data and then use the LLM to remove that PHI data.

The following is an example of information from a patient record that includes PHI:

```
Patient name: John Doe
Patient SSN: 123-34-5678
Patient DOB: 01/01/2024
Patient address: 123 Main St, Anytown USA
Exam details: good health. Pulse is 60 bpm. needs to work on diet with BMI of 190
```

The following is an example prompt that includes the Amazon Comprehend Medical results as context:

```
<original_text>
Patient name: John Doe
Patient SSN: 123-34-5678 Patient DOB: 01/01/2024
Patient address: 123 Main St, Anytown USA
Exam details: good health. Pulse is 60 bpm. needs to work on diet with BMI of 190
</original_text>

<comprehend_medical_phi_entities>
<entity>
  <text>John Doe</text>
  <category>PROTECTED_HEALTH_INFORMATION</category>
  <score>0.9967944025993347</score>
  <type>NAME</type>
</entity>
<entity>
  <text>123-34-5678</text>
  <category>PROTECTED_HEALTH_INFORMATION</category>
  <score>0.9998034834861755</score>
  <type>ID</type>
</entity>
<entity>
  <text>01/01/2000</text>
  <category>PROTECTED_HEALTH_INFORMATION</category>
  <score>0.9964448809623718</score>
  <type>DATE</type>
</entity>
</comprehend_medical_phi_entities>

<instructions>
Using the provided original text and the Amazon Comprehend Medical PHI entities detected, please analyze the text to determine if it contains any additional protected health information (PHI) beyond the entities already identified. If additional PHI is found, please list and categorize it. If no additional PHI is found, please state that explicitly.
In addition if PHI is found, generate updated text with the PHI removed.
</instructions>
```
