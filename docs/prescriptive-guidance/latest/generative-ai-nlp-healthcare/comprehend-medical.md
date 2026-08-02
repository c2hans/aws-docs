---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/generative-ai-nlp-healthcare/comprehend-medical.html
---

# Using Amazon Comprehend Medical
<a name="comprehend-medical"></a>

[Amazon Comprehend Medical](https://docs.aws.amazon.com/comprehend-medical/latest/dev/comprehendmedical-welcome.html) is an AWS service that detects and returns useful information in unstructured clinical text such as physician's notes, discharge summaries, test results, and case notes. It uses natural language processing (NLP) models to detect entities. *Entities* are textual references to medical information, such as medical conditions, medications, or protected health information (PHI).

**Important**
Amazon Comprehend Medical is not a substitute for professional medical advice, diagnosis, or treatment. Amazon Comprehend Medical provides confidence scores that indicate the level of confidence in the accuracy of the detected entities. Identify the right confidence threshold for your use case, and use high confidence thresholds in situations that require high accuracy. In certain use cases, results should be reviewed and verified by appropriately trained human reviewers. For example, Amazon Comprehend Medical should only be used in patient care scenarios after review for accuracy and sound medical judgment by trained medical professionals.

You can access Amazon Comprehend Medical through the AWS Management Console, the AWS Command Line Interface (AWS CLI), or through the AWS SDKs. The AWS SDKs are available for various programming languages and platforms, such as Java, Python, Ruby, .NET, iOS, and Android. You can use the SDKs to programmatically access Amazon Comprehend Medical from your client application.

This section reviews the main capabilities of Amazon Comprehend Medical. It also discusses the advantages of using this service compared to a large language model (LLM).

## Amazon Comprehend Medical capabilities
<a name="comprehend-medical-capabilities"></a>

Amazon Comprehend Medical offers APIs for near real-time and batch inference. These APIs can ingest medical text and provide results for medical NLP tasks by using medical entity recognition and identifying entity relationships. You can perform analysis both on single files or as a batch analysis on multiple files stored in an Amazon Simple Storage Service (Amazon S3) bucket. Amazon Comprehend Medical offers the following text analysis API operations for synchronous entity detection:
+ [Detect entities](https://docs.aws.amazon.com/comprehend-medical/latest/dev/textanalysis-entitiesv2.html) – Detects general medical categories such as anatomy, medical condition, PHI category, procedures, and time expressions.
+ [Detect PHI](https://docs.aws.amazon.com/comprehend-medical/latest/dev/textanalysis-phi.html) – Detects specific entities such as age, date, name, and similar personal information.

Amazon Comprehend Medical also includes multiple API operations that you can use to perform batch text analysis on clinical documents. To learn more about how to use these API operations, see [Text analysis batch APIs](https://docs.aws.amazon.com/comprehend-medical/latest/dev/textanalysis-batchapi.html).

Use Amazon Comprehend Medical to detect entities in clinical text and link those entities to concepts in standardized medical ontologies, including the RxNorm, ICD-10-CM, and SNOMED CT knowledge bases. You can perform analysis both on single files or as a batch analysis on large documents or multiple files stored in an Amazon S3 bucket. Amazon Comprehend Medical offers the following ontology linking API operations:
+ [InferICD10CM](https://docs.aws.amazon.com/comprehend-medical/latest/dev/ontology-icd10.html) – The **InferICD10CM** operation detects potential medical conditions and links them to codes from the 2019 version of the International Classification of Diseases, 10th Revision, Clinical Modification (ICD-10-CM). For each potential medical condition detected, Amazon Comprehend Medical lists the matching ICD-10-CM codes and descriptions. Listed medical conditions in the results include a confidence score, which indicates the confidence that Amazon Comprehend Medical has in the accuracy of the entities to the matched concepts in the results.
+ [InferRxNorm](https://docs.aws.amazon.com/comprehend-medical/latest/dev/ontology-RxNorm.html) – The **InferRxNorm** operation identifies medications that are listed in a patient record as entities. It links entities to concept identifiers (RxCUI) from the RxNorm database from the National Library of Medicine. Each RxCUI is unique for different strengths and dose forms. Listed medications in the results include a confidence score, which indicates the confidence that Amazon Comprehend Medical has in the accuracy of the entities matched to the concepts from the RxNorm knowledge base. Amazon Comprehend Medical lists the top RxCUIs that potentially match for each medication that it detects in descending order based on confidence score.
+ [InferSNOMEDCT](https://docs.aws.amazon.com/comprehend-medical/latest/dev/ontology-linking-snomed.html) – The **InferSNOMEDCT** operation identifies possible medical concepts as entities and links them to codes from the 2021-03 version of the Systematized Nomenclature of Medicine, Clinical Terms (SNOMED CT). SNOMED CT provides a comprehensive vocabulary of medical concepts, including medical conditions and anatomy, as well as medical tests, treatments, and procedures. For each matched concept ID, Amazon Comprehend Medical returns the top five medical concepts, each with a confidence score and contextual information such as traits and attributes. The SNOMED CT concept IDs can then be used to structure patient clinical data for medical coding, reporting, or clinical analytics when used with the SNOMED CT polyhierarchy.

For more information, see [Text analysis APIs](https://docs.aws.amazon.com/comprehend-medical/latest/dev/comprehendmedical-textanalysis.html) and [Ontology Linking APIs](https://docs.aws.amazon.com/comprehend-medical/latest/dev/comprehendmedical-ontologies.html) in the Amazon Comprehend Medical documentation.

## Use cases for Amazon Comprehend Medical
<a name="comprehend-medical-use-cases"></a>

As a standalone service, Amazon Comprehend Medical might address your organization's use case. Amazon Comprehend Medical can perform tasks such as the following:
+ Help with medical coding in patient records
+ Detect protected health information (PHI) data
+ Validating medication, including attributes such as dosage, frequency, and form

Amazon Comprehend Medical results are digestible for the majority of medical practices. However, you might need to consider alternatives if you have limitations such as the following:
+ **Different entity definitions** – For example, your definition of `FREQUENCY` of a medication entity might differ. For frequency, Amazon Comprehend Medical predicts *as needed*, but your organization might use the term *pro re nata (PRN)*.
+ **Overwhelming quantity of results** – For example, patient notes frequently contain multiple symptoms and keywords that map to multiple ICD-10-CM codes. However, several of the keywords are not applicable for diagnosis. In this case, the provider has to evaluate numerous ICD-10-CM entities and their confidence scores, which requires manual processing time.
+ **Custom entities or NLP tasks** – For example, providers might want to extract PRN evidence, such as *take as needed for pain*. Because this isn't available through Amazon Comprehend Medical, a different AI/ML model is warranted. A different AI/ML solution is required if the NLP task is outside of entity recognition, such as summarization, question-answering, and sentiment analysis.
