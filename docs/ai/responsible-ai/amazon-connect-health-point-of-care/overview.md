---
source_url: https://docs.aws.amazon.com/ai/responsible-ai/amazon-connect-health-point-of-care/overview.html
---

# Amazon Connect Health (Point of Care)
<a name="overview"></a>

![Banner background image](https://docs.aws.amazon.com/ai/responsible-ai/amazon-connect-health-point-of-care/images/card-background.jpg)

An AWS AI Service Card explains the use cases for which the service is intended, how machine learning (ML) is used by the service, and key considerations in the responsible design and use of the service. A Service Card will evolve as AWS receives customer feedback, and as the service progresses through its lifecycle. AWS recommends that customers assess the performance of any AI service on their own content for each use case they need to solve. For more information, please see [AWS Responsible Use of AI Guide](https://d1.awsstatic.com/products/generative-ai/responsbile-ai/AWS-Responsible-Use-of-AI-Guide-Final.pdf) and the references at the end. Please also be sure to review the [AWS Responsible AI Policy](https://aws.amazon.com/ai/responsible-ai/policy/), [AWS Acceptable Use Policy](https://aws.amazon.com/aup/), and [AWS Service Terms](https://aws.amazon.com/service-terms/) for the services you plan to use.

This Service Card applies to the point of care capabilities of Amazon Connect Health (ambient documentation, medical coding, and patient insights) that are current as of Aug 3, 2026.

## Overview of Amazon Connect Health Point of Care
<a name="overview-section"></a>

Amazon Connect Health is a HIPAA-eligible agentic AI service that handles patient engagement tasks and point of care tasks alongside healthcare teams, using various generative AI models fine-tuned on healthcare domain expert guidelines and large-scale real-world medical data. This AI Service Card describes considerations for responsibly deploying and using three of Amazon Connect Health's key features: ambient documentation, medical coding, and patient insights. For more information, see the [Amazon Connect Health User Guide](https://docs.aws.amazon.com/connecthealth/latest/userguide/what-is-service.html).

Ambient Documentation generates clinical notes in various formats and patient-friendly after-visit summaries from conversations during medical appointments, seamlessly enabling healthcare providers to review, edit, and approve clinical notes while reducing the burden of clinical documentation. Medical Coding generates ICD-10 and CPT codes directly from clinical notes with source traceability and confidence scores that support coder validation, reducing administrative work associated with clinical and billing coding. Patient Insights helps providers find relevant patient information before a visit by synthesizing structured and unstructured EHR records into a visit-specific summary tailored to the provider's specialty and reason for the visit. These point of care capabilities are available through the Amazon Connect Health API, enabling developers to embed AI agents directly into EHR workflows, clinical applications, and administrative systems, including the StartMedicalScribeListeningSession API for ambient documentation streaming and the StartPatientInsightsJob API for generating pre-visit summaries.

Effectiveness of point of care capabilities is defined by how faithfully each output reflects its source and how completely it captures what the source contains. For ambient documentation, that means the generated clinical note captures the content of the conversation completely and contains only statements supported by the transcript. For medical coding, it means the generated ICD-10 and CPT codes match the codes a certified coder would bill, with each code traceable to the supporting documentation. For patient insights, it means the summary surfaces the relevant history from the patient's records, with every statement traceable to those records with no fabrication. Customers should conduct their own evaluations, as the benchmarks presented in this Service Card are sample performance metrics and are not a substitute for customer testing on their own content in their intended contexts of use. As one example, customers may evaluate quality by comparing generated outputs against the customer's own ground truth: notes against clinician-authored notes, codes against historically billed codes validated by certified coders, and summaries against source patient records and documents.

The performance of Amazon Connect Health is influenced by both intrinsic and confounding variation. Intrinsic variation refers to the natural diversity of inputs that the system must correctly handle, for example, recognizing that a cardiology visit and a dermatology visit require different clinical vocabulary, documentation structure, and coding logic. Confounding variation refers to external factors that degrade input quality but should not affect output correctness, for example, understanding that a clinical conversation recorded in a quiet exam room and the same conversation recorded with background noise should produce the same documentation. The foreseeable variations encountered across Amazon Connect Health point of care capabilities include: (1) clinical complexity (intrinsic): visits range from a focused single-complaint encounter to a complex multi-system review with numerous active diagnoses, each requiring different levels of documentation detail and coding specificity; (2) audio environment (confounding): recording quality varies with device positioning, room acoustics, background noise from medical equipment, and overlapping speakers during multi-party conversations; (3) speech and voice diversity (confounding): patients vary in age, accent, dialect, and speech patterns influenced by medical conditions (e.g., a patient with Parkinson's disease may speak more softly or with irregular rhythm); and (4) data completeness (confounding): upstream EHR records may contain gaps, outdated information, or inconsistent terminology that the system must tolerate without producing inaccurate outputs. Since different Amazon Connect Health capabilities process different input modalities and clinical contexts, customers should evaluate performance on their own content for each use case to understand how these variations affect results in their environment.

## Intended Use Cases and Limitations
<a name="use-cases-limitations"></a>

Amazon Connect Health is designed for healthcare provider organizations and health technology developers who need to streamline high-volume, repetitive tasks across clinical workflows while preserving human oversight at every step. Point of care features offer the following capabilities:

Ambient Documentation generates clinical notes from conversations during medical appointments, taking into account patient longitudinal history from the EHR. It formats unstructured data into existing clinical note formats and customizable templates, and also generates patient-friendly after-visit summaries. The service takes an audio recording of the patient-clinician conversation, customization instructions, and background patient context from the EHR, and returns a conversation transcript, a clinical note in industry-recognized formats (for example, SOAP notes) or customized to provider templates, and an after-visit summary (a patient-friendly consultation and action plan summary) for provider review. Evidence mapping links generated sentences to their data source (for example, a specific diagnosis listed in the note linked to the patient's EHR data or to the specific transcript segment that supports it) to support provider review and validation.

Medical Coding generates ICD-10 and CPT codes directly from clinical notes with audit-ready source traceability and confidence scores, enabling coders to validate predictions against source documentation. Customers can upload past coding examples to adapt the model to their organization's specific coding policies. The service takes clinical notes, patient context, visit type, provider input, and optional customer coding examples, and returns ICD-10 and CPT codes with evidence mapping, confidence scores (0 to 1), and modifiers. For example, for an office visit note documenting hypertension management with medication adjustment, the system generates ICD-10 code I10 (Essential hypertension, confidence: 0.95) and CPT code 99214 (Office visit, established patient, moderate complexity, confidence: 0.88), with evidence mapped to the specific sentences in the clinical note supporting each code.

Patient Insights synthesizes a patient's longitudinal records and documents into insights tailored to the provider's specialty and reason for the visit, surfacing relevant history, health events and results since prior visits, and suggested items to address during the encounter. The service takes patient records (internal and external sources in FHIR), unstructured documents, and the visit type (for example, inpatient, ambulatory, or outpatient visits) and encounter context (for example, provider specialty and reason for visit), and returns a visit-specific summary with source-linked insights and Hierarchical Condition Categories (HCC) gap identification. For example, for a cardiology follow-up, the system summarizes the cardiology-relevant history, procedures, and lab results and medication changes since last visit. It displays LDL result review and medication adherence as key visit action, with each insight linked to its source record.

For ambient documentation, information not verbally expressed during the conversation will not be captured, and generated clinical notes or after-visit summaries may omit, misstate, or introduce information that is not supported by the conversation or provided patient context. This risk may increase with background noise, unclear or overlapping speech, poor device positioning, or complex conversations. Evidence mapping links generated content to the supporting dialogue or patient context so clinicians can verify and correct outputs before finalization. For medical coding, outputs are probabilistic; confidence scores help coders prioritize review, but human validation is required before claim submission; accuracy of output will be affected by clinical note completeness, specificity of clinical language, documentation style, and coding scenario complexity. For patient insights, information not present in connected data sources and documents will not appear in generated summaries. Accuracy will be affected by EHR data completeness and data source availability and recency, and breadth or complexity of the medical history.

All AI-generated outputs require human review before final action, and Amazon Connect Health point of care capabilities are not intended for (1) fully automated clinical, billing, or patient safety decisions without human oversight; (2) real-time clinical decision support during active or time-critical patient treatment (e.g., drug interaction alerts, diagnostic recommendations during procedures); (3) patient populations or clinical specialties for which the customer has not validated performance through their own testing; (4) replacement of certified medical coders (outputs are intended to assist, not replace, human coding professionals); (5) replacement of professional medical judgment; or (6) use as a diagnostic tool or for generating medical advice directly received by patients. Customers should maintain procedures allowing users to review, correct, reject, or override AI-generated outputs. Performance may vary across patient populations, EHR systems, clinical specialties, and care settings. At present, Amazon Connect Health services support US-English, with plans underway for expansion to other languages.

## Design of Amazon Connect Health Point of Care
<a name="design"></a>

**Machine learning**
Amazon Connect Health delivers its point of care capabilities using a combination of generative AI techniques, pairing speech recognition with generative models that ground every output in a verifiable source.
Ambient Documentation works as follows: (1) capture the audio of the patient-clinician conversation and, using speech recognition, generate a transcript; (2) detect and assign speaker roles (patient or clinician) and segment the transcript; (3) using generative AI, together with the patient context provided at the start of the session, generate a structured clinical note in the configured format or template; (4) link every statement in the note to the supporting dialogue in the transcript or the source patient context (evidence mapping); (5) generate a patient-friendly after-visit summary as a distinct output through the same documentation pipeline on request; (6) obtain provider review, revision, and approval.
Medical Coding works as follows: (1) ingest the clinical note along with the available patient context and visit type; (2) using generative AI informed by the relevant clinical context, predict the ICD-10 and CPT codes the documentation supports; (3) map each predicted code to the specific sentences in the note that support it and assign a confidence score; (4) link the appropriate ICD-10 diagnosis codes to the relevant CPT service codes performed; (5) apply any customer-uploaded coding examples so predictions reflect the organization's coding policies; (6) return the codes with evidence mapping, confidence scores, and modifiers for a certified coder to validate.
Patient Insights works as follows: (1) ingest the patient's records and documents from the connected internal and external FHIR sources; (2) extract and deduplicate medical facts across categories such as care gaps, chronic and active conditions, and trends; (3) link each extracted fact to the raw record that supports it (evidence linkage); (4) using generative AI and the encounter context (provider specialty and reason for visit), generate a visit-specific summary for provider review that surfaces the relevant history and suggested items for review, each insight linked to its source record.

**Controllability**
Amazon Connect Health is said to exhibit a consistent behavior when it produces the same kind of output for the same kind of input and configuration. Because the service does not expose free-form prompting, its behavior is shaped by a fixed set of control levers rather than by open-ended user input.
For point of care, the primary control levers are (a) fine-tuning the underlying generative models on healthcare domain expert guidelines and large-scale real-world medical data; (b) restricting the service to controlled customizations, with free prompting disabled, so the input surface stays bounded; (c) grounding every output in its source through evidence mapping and confidence scores, so generation stays tied to the transcript, records, or note rather than free composition; and (d) Amazon Bedrock guardrails together with output format validations that screen inputs and keep results in the expected structured form.
Across releases, AWS exercises these levers by fine-tuning the models to align with clinical guidelines, having clinical specialists design the workflow guidelines and review outputs for each model release, and validating output format and source grounding before results are returned.

**Performance Expectations**
Intrinsic and confounding variation will differ between customer applications. This means performance can differ even when applications support the same point of care workflow.
For Ambient Documentation, Application A may capture a focused patient-clinician visit in a quiet exam room using a standard note template. Application B may capture a longer, multi-party visit with background noise, overlapping speech, and a specialty-specific template. These differences can affect transcription accuracy, documentation completeness, and factual grounding.
For Medical Coding, Application A may process complete clinical notes that use specific terminology and reflect coding practices represented in the customer's adaptation examples. Application B may process sparse or ambiguous notes, more complex encounters, or documentation that differs from the examples used to adapt the model. These differences can affect code accuracy, evidence mapping, and the number of encounters for which the service returns predictions.
For Patient Insights, Application A may use complete, current records and a specific reason for the visit. Application B may use fragmented or outdated records, fewer connected data sources, or a broad encounter context. These differences can affect the completeness and relevance of the surfaced history, health events, and suggested visit items.
The overall utility of Amazon Connect Health depends on the service, the customer workflow, the available source data, and the encounters represented in the evaluation dataset. Customers should test each configured workflow using representative conversations, coding scenarios, records, and specialties before deployment and periodically thereafter.

**Test Driven Methodology**
We use multiple datasets and human evaluators to assess the performance of Amazon Connect Health. No single evaluation dataset captures performance completely, because evaluation datasets vary based on use case, intrinsic and confounding variation, the quality of ground truth available, and other factors. Our development process examines performance across these datasets, takes steps to improve both the models and the suite of evaluation datasets, and then iterates.
Evaluation datasets are drawn from diverse, de-identified clinical sources representing multiple healthcare settings, specialties, and patient populations. Results are validated through multiple independent runs to ensure reproducibility, and human clinical expert review supplements automated evaluation to capture nuanced safety and quality considerations.
Evaluation includes both manual and automated approaches. Manual evaluation uses human-in-the-loop comparison of AI-generated outputs to source records, and automated evaluations are conducted at scale for quality assurance and continuous monitoring. Clinical specialists design workflow guidelines and provide manual review for each model release. All capabilities share evaluation layers consisting of automated evaluations, manual clinical specialist reviews, source evidence mapping, LLM guardrails through Amazon Bedrock, and output format validations.
Customers should validate performance in their own environment for their intended contexts of use before deployment and periodically thereafter.

**Safety**
Safety is a shared responsibility between AWS and our customers. Our goal for safety is to mitigate key risks of concern to our enterprise customers and to society more broadly, and we align the behaviors of the underlying models with internal design policies and our commitment to responsible AI development practices. Customers are responsible for end-to-end testing of their applications and deciding if test results meet their specific expectations of safety.
For point of care capabilities, outputs are designed to be reviewed by qualified professionals before any clinical or billing action is taken. Evidence mapping and confidence scores enable reviewers to identify and correct potential errors before finalization. Factual grounding supports safer review by helping qualified professionals identify unsupported content, but it does not establish clinical completeness or eliminate the need for human review. See Veracity for measured factual-grounding results.
These review mechanisms reduce risk but do not eliminate the possibility of errors in generated outputs. AWS offers services and tools to help customers identify and mitigate safety risks, such as Amazon Bedrock Guardrails.

**Fairness**
Amazon Connect Health is designed to deliver accurate, consistent outputs across the full diversity of patient and clinician interactions, regardless of patient demographics, clinical specialty, geographic region, or care setting.
Datasets are built to capture a diverse range of voices, accents, dialects, and acoustic conditions. Routine testing on datasets with reliable demographic labels identifies performance gaps, and steps are taken to improve performance for groups on which the AI performs least well. This includes fairness testing for ambient documentation across diverse speaker demographics, accents, and acoustic conditions.
For ambient documentation, we evaluate factuality and completeness across patient and physician demographics, including gender, age group, and race. On a held-out set of 250 English-language appointments with automatic speech recognition transcripts, observed recall across the measured demographic groups ranged from 83.8% to 86.7%, against an overall recall of 86%. Observed hallucination rates ranged from 2.9% to 6.5%, against an overall rate of 3.5%. Subgroup sample sizes varied, including a pediatric subgroup of six appointments, so these results are descriptive and do not establish equivalent performance across every demographic group.
For medical coding and patient insights, which operate on clinical notes and structured records rather than audio, fairness is assessed by testing performance consistency across patient demographics and clinical settings, with steps taken to improve performance for any group on which the AI performs least well.
Because results depend on the interaction between Amazon Connect Health, the customer workflow, and the patient population served, customers should test capabilities on their own content and patient populations and monitor real-world performance.

**Veracity**
Amazon Connect Health is designed to generate outputs that are factually grounded in source data. For Ambient Documentation, evaluation on a de-identified patient dataset found that 94% of generated clinical note content was directly supported by or reasonably inferred from the appointment transcript. For Medical Coding, every code prediction links to source documentation with a confidence score. For Patient Insights, evaluation on a de-identified patient dataset found that fewer than 1% of atomic clinical statements were fabricated, inaccurate, or unsupported by the source FHIR records.
These results measure factual grounding. They do not establish that every output contains all clinically important information or is safe to use without qualified human review. For Ambient Documentation, evidence mapping links generated note content to the supporting transcript or patient context. For Medical Coding, evidence mapping links predicted codes to supporting documentation. For Patient Insights, each generated insight links to its source record. Customers should evaluate veracity and completeness using their own representative content.

**Robustness**
Amazon Connect Health is trained and tested across a variety of healthcare settings, EHR systems, clinical specialties, and patient populations, and similar inputs are expected to produce consistent outputs. For ambient documentation, the service is designed to remain reliable under real-world audio conditions such as background noise, speaker overlap, and variation in conversation length. For medical coding, it is designed to handle variation in documentation style and clinical language, and for patient insights, incomplete or variably structured records. Steps are taken across all capabilities to improve performance for scenarios on which the AI performs least well, with continuous iteration based on real-world usage patterns.

**Explainability**
Amazon Connect Health provides source traceability across all capabilities. For ambient documentation, evidence mapping links every sentence in the generated clinical note to the relevant dialogue in the conversation transcript, enabling clinicians to review and verify before signing. For medical coding, every ICD-10 and CPT code links directly to source documentation with confidence scores (0 to 1), considering evidence mapping, medical necessity, diagnosis-treatment alignment, and code specificity. For patient insights, every insight links directly to source EHR data, enabling clinicians to verify the basis of each recommendation.

**Privacy**
Amazon Connect Health is built on HIPAA-eligible infrastructure designed for healthcare workloads. Customer content is not used to train models without customer consent, and customers can opt out at any time. Inputs and outputs are never shared between customers. Comprehensive audit trails support compliance and audit defense. For more information, see Section 50.3 of the [AWS Service Terms](https://aws.amazon.com/service-terms/) and the [AWS Data Privacy FAQs](https://aws.amazon.com/compliance/data-privacy-faq/).

**Security**
Data is encrypted in transit and at rest. Role-based access controls, end-to-end encrypted connections, and continuous monitoring maintain governance across all patient interactions. Amazon Connect Health operates within HIPAA-eligible AWS infrastructure with security controls designed for healthcare workloads.

**Transparency**
Amazon Connect Health provides information to customers in this Service Card, AWS documentation and the AWS Console. We accept feedback through customer support mechanisms such as account managers. Customers who incorporate Amazon Connect Health in their workflow are responsible for determining their disclosure obligations, disclosing their use of ML and speech recognition technology to end users and other individuals impacted by the application where applicable, and giving their end users the ability to provide feedback to improve workflows. In their documentation, customers can also reference this AI Service Card.

**Governance**
We have rigorous methodologies to build our AWS AI services responsibly, including a working backwards product development process that incorporates Responsible AI at the design phase, design consultations, and implementation assessments by dedicated Responsible AI science and data experts, routine testing, reviews with customers, best practice development, dissemination, and training.

## Deployment and performance optimization best practices
<a name="deployment-performance-optimization-best-practices"></a>

Customers deploying Amazon Connect Health as a component of their application have a high degree of influence on overall application performance, including accuracy, fairness, and robustness. The following levers describe how customers and their end users exert this influence. AWS encourages customers to build and operate their applications responsibly, as described in the [AWS Responsible Use of AI Guide](https://d1.awsstatic.com/products/generative-ai/responsbile-ai/AWS-Responsible-Use-of-AI-Guide-Final.pdf). This includes implementing Responsible AI practices to address key dimensions including controllability, safety, fairness, veracity, robustness, explainability, privacy, security, transparency, and governance.

**Workflow Design**

The performance of any application using Amazon Connect Health depends on the design of the customer workflow, including the factors discussed below:

1. **Effectiveness Criteria:** Customers should define and enforce criteria for the use cases they implement, and, for each use case, define the inputs and outputs permitted and how human reviewers apply their judgment to determine final results. These criteria should address the responsible AI dimensions above, including safety, fairness, and accuracy. Recommendations:
   + Define what a complete and accurate note, code set, or insight summary looks like for each workflow, and the error types that matter most
   + Set the confidence or evidence thresholds at which an output is accepted, corrected, or returned for review
   + Establish how clinicians and coders accept, edit, or reject AI-generated outputs before they are finalized

1. **Human Oversight:** The outputs produced by Amazon Connect Health are probabilistic, and accuracy may be impacted by the confounding factors described above. Amazon Connect Health should not be used to fully automate clinical documentation, billing, patient safety, or identity verification workflows without appropriate human oversight. Recommendations:
   + Implement review workflows for all AI-generated outputs before they are finalized (e.g., clinician sign-off on notes, coder validation of billing codes)
   + Use evidence mapping and source traceability to help reviewers verify the basis of each output
   + Define clear accountability for who reviews and approves AI-generated outputs in each workflow

1. **Workflow Configuration:** How the workflow is configured shapes the fit and quality of generated documentation, insights, and codes, and the efficiency of clinician review. Recommendations:
   + Configure ambient documentation templates to match your organization's existing EHR note structures and clinical specialties
   + Map SDK integrations to your existing clinical and administrative workflows rather than creating parallel processes

1. **EHR Data Quality:** The accuracy of patient insights, ambient documentation, and medical coding outputs is directly affected by the completeness and quality of available EHR data. Recommendations:
   + Maintain up-to-date patient records in connected EHR systems
   + Connect external data sources where available to improve the breadth of patient insights
   + Ensure that clinical notes used as input for medical coding are complete and use specific clinical language

1. **Audio Quality (Ambient Capabilities):** For ambient documentation, recording conditions directly impact transcription and note generation quality. Recommendations:
   + For ambient documentation, use a lossless audio format with PCM 16-bit encoding at 16,000 Hz or higher sample rate
   + Position recording devices to minimize distance from speakers and reduce background noise
   + Address variation in recording conditions across clinical settings (e.g., exam rooms vs. open areas)

1. **Customization:** Amazon Connect Health supports controlled customization to adapt to organizational needs. Recommendations:
   + For medical coding, upload past coding examples to adapt the model to your organization's specific coding policies and reimbursement guidelines
   + For ambient documentation, configure templates and Smart Phrase mappings to match your organization's documentation standards

1. **Consistency:** Customers should set and enforce policies for the kinds of inputs permitted and for how humans use their own judgment to assess Amazon Connect Health outputs. Recommendations:
   + Apply policies consistently across all patient populations and demographic groups
   + Standardize how reviewers assess AI-generated outputs (e.g., consistent criteria for accepting or modifying clinical notes)
   + Ensure that escalation protocols are applied uniformly regardless of patient demographics
   + Document and train staff on standard operating procedures for each capability

1. **Performance Drift:** Changes in the kinds of inputs submitted to Amazon Connect Health and updates to the underlying models may lead to different outputs over time. Recommendations:
   + Periodically retest performance against your own ground truth data
   + Monitor key metrics (note accuracy, coding accuracy) over time
   + Adjust workflows if performance changes are observed
   + Maintain versioned records of your evaluation results to track trends

1. **Model Updates:** When AWS releases new versions of Amazon Connect Health, customers may experience changes in performance on their use cases. AWS notifies customers when a new version is released and provides time to migrate from an old version to the new one. Recommendations:
   + Retest performance on your own use cases when a new version is released
   + Migrate within the provided window and compare results against your prior benchmark

## Further information
<a name="further-info"></a>
+ For service documentation, see the [Amazon Connect Health Developer Guide](https://docs.aws.amazon.com/connecthealth/latest/userguide/what-is-service.html).
+ For details on privacy and other legal considerations, see the following AWS policies: [Acceptable Use](https://aws.amazon.com/aup/), [Responsible AI](https://aws.amazon.com/ai/responsible-ai/policy/), [Legal](https://aws.amazon.com/legal/), [Compliance](https://aws.amazon.com/compliance/), and [Privacy](https://aws.amazon.com/privacy/).
+ For help optimizing workflows, see [Generative AI Innovation Center](https://aws.amazon.com/ai/generative-ai/innovation-center/), [AWS Customer Support](https://aws.amazon.com/contact-us/), [AWS Professional Services](https://aws.amazon.com/professional-services/), [Ground Truth Plus](https://aws.amazon.com/sagemaker/groundtruth/), and [Amazon Augmented AI](https://aws.amazon.com/augmented-ai/).
+ If you have any questions or feedback about AWS AI service cards, please complete [ this form](https://pages.awscloud.com/global-ln-gc-400-ai-service-cards-contact-us-registration.html).

## Glossary
<a name="glossary"></a>

 **Controllability: **Steering and monitoring AI system behavior.

 **Privacy & Security: **Appropriately obtaining, using and protecting data and models.

 **Safety: **Preventing harmful system output and misuse.

 **Fairness: **Considering impacts on different groups of stakeholders.

 **Explainability: **Understanding and evaluating system outputs.

 **Veracity & Robustness: **Achieving correct system outputs, even with unexpected or adversarial inputs.

 **Transparency: **Enabling stakeholders to make informed choices about their engagement with an AI system.

 **Governance: **Incorporating best practices into the AI supply chain, including providers and deployers.
