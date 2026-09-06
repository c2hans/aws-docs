---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-modern-healthcare-data/appendix-b.html
---

# Appendix B. Meeting patient goals
<a name="appendix-b"></a>

Patients and their caregivers have varied goals and expectations when it comes to healthcare. They want to receive safe and effective treatment, and make informed decisions about their healthcare. They also want to control who has access to their healthcare data and how that data is used.

Healthcare providers have ethical and legal responsibilities to give patients control of their Protected Health Information (PHI). In the United States, the Health Insurance Portability and Accountability Act (HIPAA) states that "individuals have the right to review and obtain a copy of their PHI, a right to restrict disclosure of their PHI, and a right to an accounting of the disclosures of their PHI." For more information, see [Summary of the HIPAA Privacy Rule](https://www.hhs.gov/hipaa/for-professionals/privacy/laws-regulations/index.html). Most European Union member states recognize the patient's right to self-determination and confidentiality with respect to PHI. For more information, see the report [Patients' rights in the European Union](https://op.europa.eu/en/publication-detail/-/publication/8f187ea5-024b-11e8-b8f5-01aa75ed71a1/language-en). In Japan, regulatory frameworks and healthcare systems give patients the right and ability to manage, distribute, and use their PHI. For more information, see [Personal Health Record (PHR) Utilization Project](https://www.amed.go.jp/en/program/list/05/01/005.html).

These rights of self-determination and privacy mean healthcare providers should be able to trace and protect data through every aspect of the data architecture, including:
+ Data ingestion
+ Processing
+ Persistence
+ Security
+ Governance
+ Federation
+ Sharing

At the same time, patients expect prompt, effective treatment in emergencies. Therefore, data protections should be designed so that they don't impair the ability of healthcare providers to treat patients effectively.

The following sections discuss these goals, and the ways in which a modern health data strategy can help meet them.

## Managing consent for treatment and research
<a name="consent"></a>

When receiving treatment or undergoing tests, a patient consents to sharing healthcare data with the healthcare provider. The terms of that consent are usually the type and volume of data collected, who can access the data, and how it can be used. In most regulatory environments, these terms must follow the data regardless of how the provider transforms and stores it. Everyone who accesses the data must do so in a way that is consistent with the patient's consent.

A modern healthcare-data strategy should explicitly define the following:
+ How patient consent is created
+ How that consent remains attached to the patient data
+ How systems control access in a way that respects the patient's consent

It's also important for consent-tracking systems to include mechanisms for auditing data access to confirm compliance with regulations.

## Providing personalized information to patients
<a name="personalized-info"></a>

The rapid growth of medical information on the internet has made it more challenging for patients to find reliable information about their conditions and standards of care. Precision medicine adds to this challenge. Precision medicine takes into account individual differences in peoples' genes, environments, and lifestyles. There is an extremely large number of possible genotypes. When those are multiplied by the number of variables related to environment and lifestyle, it becomes apparent that every individual is medically unique.

When patients search the internet for information about their specific medical conditions—treatment options, medicines, therapies, diet and exercise guidelines, or other guidance—they find copious information. However, that information can be limited in its applicability to the patient's personal medical situation. Patients might also find it difficult to understand insurance coverage and out-of-pocket expenses for different treatment options. By using a modern healthcare-data strategy, healthcare organizations can unlock data from silos and make it available so that patients can access and understand their personal health information, find accurate information about their condition, and get helpful and appropriate guidance.

## Connecting patients with clinical trials
<a name="clinical-trials"></a>

"Rare diseases, defined as diseases or conditions affecting a small proportion of the population, impact one in 17 people, amounting to over 400 million people worldwide. But while 7,000 rare diseases have been identified in the US alone, just 500 therapies have been approved by regulators.... Rare disease trials differ significantly from 'ordinary' trials. ... Patients can be difficult to find, small in number and spread around the world, potentially complicating the recruitment and enrollment processes." —Peter Buckman and the Forbes Business Development Council, [Rare Diseases: Unique But Under-Addressed In Clinical Development](https://www.forbes.com/councils/forbesbusinessdevelopmentcouncil/2022/08/02/rare-diseases-unique-but-under-addressed-in-clinical-development/)

Patients with conditions for which there is no approved treatment, especially rare diseases, are keenly interested in finding clinical trials for new therapies. But for researchers, patient recruitment—the ability to identify and enroll the right number of the right patients—is a primary reason that clinical trials fail. A modern healthcare-data strategy helps patients to find the clinical trials that are most suitable for their personal condition. It also increases the success rate for clinical trials by helping researchers identify and recruit the right patients.

## Providing multimodal health-record portability
<a name="portability"></a>

Modern health records are multimodal. They contain traditional electronic health record (EHR) data, radiology records, genomic sequencing data, electron microscopy data, tissue samples, patient device data, and much more. As a result, patient medical records are often large and diverse. Patients might receive data from many providers and share that data with other providers and payers.

Conveying large, complex data using physical media is no longer viable. Gaps in health records might result in poor quality of care and excess out-of-pocket expenses for patients. A modern healthcare-data strategy includes mechanisms that simplify the process of conveying multimodal health records between labs, providers, and payers.
