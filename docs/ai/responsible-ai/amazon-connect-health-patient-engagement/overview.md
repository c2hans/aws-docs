---
source_url: https://docs.aws.amazon.com/ai/responsible-ai/amazon-connect-health-patient-engagement/overview.html
---

# Amazon Connect Health (Patient Engagement)

![Banner background image](https://docs.aws.amazon.com/ai/responsible-ai/amazon-connect-health-patient-engagement/images/card-background.jpg)

An AWS AI Service Card explains the use cases for which the service is intended, how machine learning (ML) is used by the service, and key considerations in the responsible design and use of the service. A Service Card will evolve as AWS receives customer feedback, and as the service progresses through its lifecycle. AWS recommends that customers assess the performance of any AI service on their own content for each use case they need to solve. For more information, please see [AWS Responsible Use of AI Guide](https://d1.awsstatic.com/products/generative-ai/responsbile-ai/AWS-Responsible-Use-of-AI-Guide-Final.pdf) and the references at the end. Please also be sure to review the [AWS Responsible AI Policy](https://aws.amazon.com/ai/responsible-ai/policy/), [AWS Acceptable Use Policy](https://aws.amazon.com/aup/), and [AWS Service Terms](https://aws.amazon.com/service-terms/) for the services you plan to use.

This Service Card applies to the patient engagement capabilities of Amazon Connect Health (patient verification and appointment management) that are current as of Nov 18, 2026.

## Overview of Amazon Connect Health Patient Engagement
<a name="overview-section"></a>

Amazon Connect Health is a HIPAA-eligible agentic AI service that handles patient engagement tasks and point of care tasks alongside healthcare teams, using various generative AI models fine-tuned on healthcare domain expert guidelines and large-scale real-world medical data. This AI Service Card describes considerations for responsibly deploying and using two of Amazon Connect Health's key features, patient verification and appointment management, implemented by the Amazon Connect Health API. For more information, see the [Amazon Connect Health User Guide](https://docs.aws.amazon.com/connecthealth/latest/userguide/what-is-service.html).

Patient engagement capabilities (patient verification and appointment management) are delivered through voice-based interactions with patients via Amazon Connect and real-time connectivity to Electronic Health Record (EHR) systems. Patient verification delivers a secure AI conversation where patients can answer identity questions, allowing them to be verified early and reduce contact center staff burden. Appointment management allows patients to manage their appointments and insurance eligibility checks via natural language voice interactions.

Effectiveness of patient engagement is defined by goal fulfillment, meaning the agent either completes the patient's request on its own or, when it cannot, appropriately escalates the interaction to a human agent with conversation context. For patient verification, that means correctly confirming the patient's identity against their record, or escalating when identity cannot be confirmed. For appointment management, it means reliably conducting initial insurance eligibility and coverage checks and coordinating scheduling using provider availability, patient preferences, and scheduling constraints, or transferring to a human agent when a request falls outside what the agent can resolve. AWS recommends that customers conduct their own evaluations because performance varies by workflow, caller population, and deployment environment. As one example, for patient verification and appointment management, customers may evaluate quality by testing the agents across a variety of real-world scenarios to check for goal fulfillment.

The performance of Amazon Connect Health is influenced by both intrinsic and confounding variation. Intrinsic variation refers to the natural diversity of inputs that the system must correctly handle. Confounding variation refers to external factors that degrade input quality but should not affect output correctness, for example, understanding that a clinical conversation recorded in a quiet exam room and the same conversation recorded with background noise should produce the same documentation. The foreseeable variations encountered across Amazon Connect Health patient engagement capabilities include: (1) audio environment: recording quality varies with device positioning, room acoustics, background noise from medical equipment, and overlapping speakers during multi-party conversations; (2) speech and voice diversity: patients vary in age, accent, dialect, and speech patterns influenced by medical conditions (e.g., a patient with Parkinson's disease may speak more softly or with irregular rhythm); and (3) data completeness: upstream EHR records may contain gaps, outdated information, or inconsistent terminology that the system must tolerate without producing inaccurate outputs. Since different Amazon Connect Health capabilities process different input modalities and clinical contexts, customers should evaluate performance on their own content for each use case to understand how these variations affect results in their environment.

## Intended Use Cases and Limitations
<a name="use-cases-limitations"></a>

Amazon Connect Health is designed for healthcare provider organizations and health technology developers who need to streamline high-volume, repetitive tasks while preserving human oversight. Patient engagement features offer the following capabilities:

Patient Verification delivers a secure AI conversation where patients can answer identity questions, allowing them to be verified early through real-time EHR access, reducing multi-step manual record lookup for contact center staff. Customers configure required verification attributes, such as date of birth, phone number, MRN, last 4 digits of SSN, or zip code, to verify the identity of the patient. Configuration is based on their organization's security requirements and patient populations. The service prompts patients for answers to self-identification questions, and takes their spoken or DTMF (touchtone) responses as input, along with EHR patient records, to return a structured verification result. The verification result includes the overall authentication decision (verified or not verified), the matched patient details, the attributes checked (for example, date of birth or phone number confirmation), and escalation context at handoff (for example, a summary of the conversation with the patient providing context for escalation to contact center staff).

Appointment Management assists with scheduling, rescheduling, cancellations, and appointment lookup via natural language voice interactions with real-time EHR access and insurance eligibility checks, to reduce administrative burden and provide patient support outside of business hours for straightforward scheduling tasks. Interactions requiring resolution beyond the agent's capabilities are escalated to human staff, with context summaries provided at transfer. The service takes patient voice or DTMF (touchtone) input via phone call together with EHR scheduling data and insurance eligibility data, and returns a completed appointment management action (for example, an appointment scheduled with provider, date, and time confirmation; rescheduled to a new slot; or cancelled), along with escalation context if the interaction is transferred, including a conversation summary and the patient intent. Relevant confounding factors include audio quality, background noise, EHR data completeness, and insurance system availability.

However, customers should be aware of the system's limitations. For patient verification and appointment management, accuracy can be affected by audio quality, background noise, unclear speech, or incomplete EHR data (including insurance system availability). Amazon Connect Health patient engagement capabilities are not intended for (1) fully automated clinical, billing, insurance eligibility, healthcare access, or patient safety decisions without human oversight; (2) real-time clinical decision support during active or time-critical patient treatment (e.g., drug interaction alerts, diagnostic recommendations during procedures, clinical triaging during patient conversations); (3) patient populations or clinical specialties for which the customer has not validated performance through their own testing; (4) use as a diagnostic tool or for generating medical advice directly received by patients; or (5) replacement of professional medical judgment. Customers should maintain procedures allowing users to review, correct, reject, or override AI-generated outputs. Performance may vary across patient populations, EHR systems, clinical specialties, and care settings. Amazon Bedrock Guardrails are applied across all patient engagement agents to screen inputs and outputs for harmful or disallowed content and attacks such as prompt injection and verification bypass. Separately, the service uses an LLM prompt to detect situations that may require escalation, including high medical risk, an explicit request for human assistance, or patient frustration. These controls reduce risk but do not eliminate the possibility of unsafe content or missed escalations. At present, Amazon Connect Health services support US-English, with plans underway for expansion to other languages.

## Design of Amazon Connect Health Patient Engagement
<a name="design"></a>

**Machine learning**
Amazon Connect Health delivers its patient engagement capabilities using a combination of generative AI techniques, primarily LLM-based conversational AI that interprets natural-language speech and drives a controlled, multi-turn dialogue.
Patient Verification works as follows: (1) capture the caller's spoken or DTMF (touchtone) input over the phone and convert speech to text; (2) use the conversational LLM to interpret the caller's responses and collect the verification attributes the customer has configured, at least 3 of the 5 available (date of birth, phone number, ZIP code, last 4 of SSN, or medical record number); (3) match the collected attributes against the patient's record in the connected EHR in real time; (4) apply Amazon Bedrock standard and customized guardrails to screen unsafe content and block prompt injection, verification bypass, and other disallowed inputs or outputs; separately, use an LLM prompt to detect high medical risk, requests for human assistance, or patient frustration and trigger escalation when appropriate; (5) return a structured verification decision (verified or not verified) with the matched patient details and, if the call is handed off, an escalation summary.
Appointment Management works as follows: (1) capture the caller's spoken or DTMF input over the phone and convert speech to text; (2) classify the caller's intent, such as schedule, reschedule, cancel, or look up an appointment; (3) drive the interaction with decision-tree-style reasoning that keeps each step controlled, collecting scheduling preferences and the configurable insurance details requested (insurer name, insurance status); (4) check provider availability against the EHR and run an insurance eligibility check; (5) complete the requested action and confirm it or, when the request falls outside the agent's scope or the separate escalation detection identifies a need for human assistance, escalate to a human agent with a context summary.

**Controllability**
We consider the behavior of Amazon Connect Health to be consistent when it produces the same kind of output for the same kind of caller input and configuration. The service does not provide customers with a free-form prompting interface. Instead, its behavior is shaped by a defined set of control mechanisms.
For patient engagement, the primary control levers are (a) fine-tuning the underlying generative models on healthcare domain expert guidelines and large-scale real-world medical data; (b) restricting the service to controlled customizations, with free prompting disabled, so the input surface stays bounded; (c) decision-tree-style reasoning that holds each step of a verification or scheduling dialogue to a controlled outcome; (d) Amazon Bedrock standard and customized guardrails that screen inputs and outputs for toxicity, harmful content, prompt injection, verification bypass, and other disallowed content; (e) separate LLM prompt-based escalation detection for safety risks, requests for human assistance, and patient frustration; and (f) output validations that keep results in the expected structured form. Across releases, AWS exercises these levers by fine-tuning the models to align with clinical and organizational guidelines, having clinical specialists design the workflow guidelines, and tuning the guardrails to block unsafe inputs and outputs.

**Performance Expectations**
Intrinsic and confounding variation will differ between customer applications. This means performance can differ even when applications support the same patient engagement workflow.
For Patient Verification, Application A may receive clear audio, consistent caller responses, and current patient records containing the configured verification attributes. Application B may receive noisy audio, callers who need additional guidance, or records with missing or outdated attributes. These differences can affect whether the service correctly verifies the caller or escalates the interaction for human review.
For Appointment Management, Application A may support routine scheduling requests using current provider availability and insurance information. Application B may support workflows with more appointment constraints, incomplete insurance data, or limited availability across providers and locations. These differences can affect whether the service completes the requested scheduling action or appropriately escalates it to staff.
The overall utility of Amazon Connect Health depends on the service, the customer workflow, and the population and scenarios represented in the evaluation dataset. Customers should test each configured workflow using representative conversations and data before deployment and periodically thereafter.

**Test Driven Methodology**
We use simulated conversations and human evaluators to assess the performance of Amazon Connect Health. No single evaluation dataset captures performance completely because evaluation results vary by use case, caller behavior, workflow configuration, the quality of available ground truth, and other factors. Our development process examines performance across these scenarios, improves both the agents and the evaluation suite, and then repeats the evaluation. The evaluation covers three healthcare AI agents: Patient Verification, Insurance Verification, and Appointment Management. Conversations are generated by patient simulators using entirely synthetic patient profiles drawn from mock healthcare data. Synthetic attributes include phone number, date of birth, medical record number, ZIP code, and the last four digits of a Social Security number. Each agent is evaluated across three caller difficulty tiers. Easy scenarios involve cooperative, straightforward callers. Medium scenarios feature callers who may be hesitant, somewhat disorganized, forgetful, or in need of guidance. Hard scenarios simulate callers who may be anxious, frustrated, forgetful, less cooperative, or in need of frequent reassurance, testing the agent's resilience and empathy under challenging but realistic interaction conditions. For Patient Verification, the evaluation tests multiple combinations of verification factors, such as phone number with date of birth and the last four digits of a Social Security number, or medical record number with date of birth and ZIP code. Results are validated through multiple independent runs to assess reproducibility. Evaluation includes both manual and automated approaches. Manual evaluation uses human-in-the-loop comparison of AI-generated outputs to synthetic source profiles and expected outcomes, and automated evaluations are conducted at scale for quality assurance and continuous monitoring. Clinical specialists design workflow guidelines. All capabilities share evaluation layers consisting of automated evaluations, source evidence mapping, Amazon Bedrock Guardrails, separate LLM prompt-based escalation detection, and output format validations.
These evaluations use simulated conversations and entirely synthetic patient profiles. They may not capture the full range or prevalence of production audio conditions, caller behavior, EHR and insurance data quality, integration latency, or operational workflows. The evaluation set is not weighted to represent the distribution of production calls, so its results should not be interpreted as production success or failure rates. Customers should validate performance using representative conversations, data, and workflows in their own environment for their intended contexts of use before deployment and periodically thereafter.

**Safety**
Safety is a shared responsibility between AWS and our customers. Our goal for safety is to mitigate key risks of concern to our enterprise customers and to society more broadly, and we align the behaviors of the underlying models with internal design policies and our commitment to responsible AI development practices. Customers are responsible for end-to-end testing of their applications and deciding if test results meet their specific expectations of safety.
For patient engagement capabilities, Amazon Bedrock standard and customized guardrails screen agent inputs and outputs for toxicity, harmful content, prompt injection, verification bypass, and certain keyword-triggered content. Separately, an LLM prompt detects situations that may require escalation, including safety risks, an explicit request for human assistance, patient frustration, or repeated inability to complete the requested task. For example, escalation is triggered when a patient states they are experiencing or describe symptoms of a medical emergency, explicitly requests to speak with a human agent, or when the agent cannot complete the requested task after several attempts. These controls reduce risk but do not eliminate the possibility of missed escalations or harmful outputs. AWS offers services and tools to help customers identify and mitigate safety risks, such as Amazon Bedrock Guardrails.

**Fairness**
Amazon Connect Health is designed to deliver accurate, consistent outcomes across patient interactions with different voice characteristics.
For Patient Verification and Appointment Management, AWS evaluates performance using simulated English-language calls sampled across gender, elder and non-elder voice profiles, and six English voice-profile groups: US English, African American English, Spanish-accented English, Chinese-accented English, British English, and Indian English. These voice profiles were sampled across easy, medium, and hard call conditions using predefined distributions. Each tier used an equal gender mix, while elder-voice representation and the weighting of non-EN-US voice profiles increased in the medium and hard tiers. The evaluation also varied speech speed and volume, pauses, background noise, and connection quality.
These evaluations test the service across a range of simulated voice and acoustic conditions. Results are reported across the combined evaluation set rather than separately for each voice-profile, gender, or elder and non-elder group. Customers should evaluate Patient Verification and Appointment Management using callers and operating conditions representative of the populations they serve.

**Veracity**
Amazon Connect Health is designed to keep Patient Engagement responses and actions grounded in information provided during the interaction and data available through configured customer systems. For Patient Verification, the service compares caller-provided information with the patient record according to the customer's configured verification requirements. For Appointment Management, the service uses connected scheduling and insurance information to assist with appointment coordination and initial eligibility and coverage checks. When the available information is insufficient or a request falls outside the configured workflow, the service is designed to escalate the interaction to a human agent with relevant context.
For answering patient questions about verification and appointment management, the service used a customer-provided informational document describing the customer's processes. The relevant supporting information was correctly retrieved for 91.63% of answerable questions. Across an evaluation set of 218 questions using two configurations of the document, answers were judged correct or partially correct in 89.91% and 94.19% of cases. Expected answers were prepared with an AI model and have not been reviewed by the customer. These results are based on informational materials from one customer and do not establish performance on other customers' documents.
Incomplete, outdated, or conflicting source data may cause the service to provide incomplete or inaccurate information or take an incorrect action. Customers should evaluate interactions against their source systems, test representative workflows, and monitor for inaccurate statements, incorrect actions, and inappropriate escalation.

**Robustness**
Amazon Connect Health is trained and tested across a variety of healthcare settings, EHR systems, clinical specialties, and patient populations. Similar caller inputs are expected to produce consistent outcomes, and the service is designed to remain reliable under real-world audio conditions such as background noise, unclear speech, and variation in caller phrasing and accent. For patient engagement capabilities, robustness is validated against a broad set of simulated patient scenarios before release, covering diverse caller difficulty levels and edge cases. Steps are taken across all capabilities to improve performance for scenarios on which the AI performs least well, with continuous iteration based on real-world usage patterns.

**Explainability**
Amazon Connect Health provides source traceability across all capabilities. For patient verification, a complete audit trail captures attributes used, verification result, and escalation reasons at handoff to human agents. For appointment management, scheduling decisions, insurance eligibility check results, and escalation context are surfaced to human agents at transfer.

**Privacy**
Amazon Connect Health is built on HIPAA-eligible infrastructure designed for healthcare workloads. Customer content is not used to train models without customer consent, and customers can opt out at any time. Patient data retrieved from EHR systems during patient verification is not persisted, and data remains only in the EHR system (zero-persistence architecture). Inputs and outputs are never shared between customers. Comprehensive audit trails support compliance and audit defense. For more information, see Section 50.3 of the [AWS Service Terms](https://aws.amazon.com/service-terms/) and the [AWS Data Privacy FAQs](https://aws.amazon.com/compliance/data-privacy-faq/).

**Security**
Data is encrypted in transit and at rest. Role-based access controls, end-to-end encrypted connections, and continuous monitoring maintain governance across all patient interactions. Amazon Connect Health operates within HIPAA-eligible AWS infrastructure with security controls designed for healthcare workloads.

**Transparency**
Amazon Connect Health provides information to customers in this Service Card, AWS documentation and the AWS Console. We accept feedback through customer support mechanisms such as account managers. Patients are informed that they are interacting with AI during patient verification and appointment management conversations. Customers who incorporate Amazon Connect Health in their workflow are responsible for determining their disclosure obligations, disclosing their use of ML and speech recognition technology to end users and other individuals impacted by the application where applicable, and giving their end users the ability to provide feedback to improve workflows. In their documentation, customers can also reference this AI Service Card.

**Governance**
We have rigorous methodologies to build our AWS AI services responsibly, including a working backwards product development process that incorporates Responsible AI at the design phase, design consultations, and implementation assessments by dedicated Responsible AI science and data experts, routine testing, reviews with customers, best practice development, dissemination, and training.

## Deployment and performance optimization best practices
<a name="deployment-performance-optimization-best-practices"></a>

Customers deploying Amazon Connect Health as a component of their application have a high degree of influence on overall application performance, including accuracy, fairness, and robustness. The following levers describe how customers and their end users exert this influence. AWS encourages customers to build and operate their applications responsibly, as described in the [AWS Responsible Use of AI Guide](https://d1.awsstatic.com/products/generative-ai/responsbile-ai/AWS-Responsible-Use-of-AI-Guide-Final.pdf). This includes implementing Responsible AI practices to address key dimensions including controllability, safety, fairness, veracity, robustness, explainability, privacy, security, transparency, and governance.

**Workflow Design**

The performance of any application using Amazon Connect Health depends on the design of the customer workflow, including the factors discussed below:

1. **Effectiveness Criteria:** Customers should define and enforce criteria for the use cases they implement, and, for each use case, define the inputs and outputs permitted and how human reviewers apply their judgment to determine final results. These criteria should address the responsible AI dimensions above, including safety, fairness, and accuracy. Recommendations:
   + Define what a successful verification or appointment outcome looks like, and the error types that matter most for your workflow
   + Set thresholds for when the agent should resolve a request autonomously versus escalate to a human agent
   + Establish how reviewers accept, correct, or override AI-generated outcomes

1. **Human Oversight:** The outputs produced by Amazon Connect Health are probabilistic, and accuracy may be impacted by the confounding factors described above. Amazon Connect Health should not be used to fully automate clinical documentation, billing, patient safety, insurance eligibility determinations or healthcare access decisions, or identity verification workflows without appropriate human oversight. Recommendations:
   + Implement review workflows for all AI-generated outputs before they are finalized (e.g., staff review of verification decisions)
   + Use evidence mapping and source traceability to help reviewers verify the basis of each output
   + Maintain escalation protocols for patient-facing capabilities; ensure human staff are available to receive escalated interactions with the context summaries provided
   + Define clear accountability for who reviews and approves AI-generated outputs in each workflow

1. **Workflow Configuration:** How the workflow is configured shapes task completion and the patient experience. Recommendations:
   + Configure patient verification attributes based on your organization's security requirements and patient populations (select at least 3 of 5 available attributes)
   + Choose the appointment management mode that fits your operations: self-service (the agent handles scheduling, rescheduling, cancellation, and lookup end-to-end without human involvement) or assisted booking (the agent verifies the patient and collects scheduling preferences, then escalates to a human agent for complex appointments such as surgeries or imaging)
   + Configure escalation paths so that requests the agent cannot resolve are routed to the appropriate human staff with the context summaries provided
   + Configure the output templates that define what information is returned at the end of an interaction (for example, the verification decision and attributes checked, or the confirmed appointment details and escalation context)
   + Design appointment management flows to account for after-hours escalation scenarios: decide whether patients should be asked to call back or be placed in a queue
   + Map SDK integrations to your existing clinical and administrative workflows rather than creating parallel processes

1. **EHR Data Quality:** The accuracy of patient verification and appointment management outputs is affected by the completeness and quality of available EHR data. Recommendations:
   + Maintain up-to-date patient records in connected EHR systems
   + Verify that patient demographic and scheduling data is current for patient verification and appointment management

1. **Audio Quality (Patient-Facing Capabilities):** For patient verification and appointment management, audio quality affects speech recognition accuracy. Recommendations:
   + For patient-facing capabilities, ensure phone system audio quality meets minimum standards and inform patients if background noise may affect the interaction

1. **Customization:** Amazon Connect Health supports controlled customization to adapt to organizational needs. Recommendations:
   + For patient verification, select the combination of verification attributes that balances security requirements with patient experience for your population
   + Work with your implementation team to define escalation thresholds and safety guardrail sensitivity appropriate for your patient population

1. **Consistency:** Customers should set and enforce policies for the kinds of inputs permitted and for how humans use their own judgment to assess Amazon Connect Health outputs. Recommendations:
   + Apply policies consistently across all patient populations and demographic groups
   + Standardize how reviewers assess AI-generated outputs (e.g., consistent criteria for accepting or modifying clinical notes)
   + Ensure that escalation protocols are applied uniformly regardless of patient demographics
   + Document and train staff on standard operating procedures for each capability

1. **Performance Drift:** Changes in the kinds of inputs submitted to Amazon Connect Health and updates to the underlying models may lead to different outputs over time. Recommendations:
   + Periodically retest performance against your own ground truth data
   + Monitor key metrics (authentication success rates) over time
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
