---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-workload-assessment/data-strategy.html
---

# Data strategy
<a name="data-strategy"></a>

|
|
| Question | Example response |
| --- |--- |
| What specific data types are crucial for your generative AI workloads, and what percentage of these are currently accessible? | Customer call logs and product reviews data are crucial. Currently, 85% of these data types are accessible for our generative AI projects. |
| How do you ensure and measure the quality of your data? | We have implemented data quality metrics, including completeness, accuracy, consistency, and timeliness. We use automated tools to regularly assess these metrics and have a dedicated team for data cleansing and enrichment. |
| What percentage of your data meets your quality standards for generative AI use? | Currently, 78% of our data meets our quality standards. We're aiming for 95% within the next 12 months through improved data cleaning processes. |
| How do you plan to build trust about data usage in generative AI among your stakeholders? | We're implementing an AI ethics board, providing clear explanations of AI decisions, and conducting quarterly AI audits to ensure transparency and fairness. |
| How comprehensive is your documentation for data sources and lineage? | We maintain a detailed data catalog that includes metadata for all our data sources, including origin, update frequency, and usage. We use data lineage tools to track how data flows and transforms across our systems. |
| How do you ensure diversity in your datasets to prevent bias in AI models? | We actively source data from diverse demographics and regularly audit our datasets for representational bias. We also use synthetic data generation techniques to balance under-represented categories. |
| What is your data refresh rate for critical generative AI models, and how do you determine this frequency? | Critical models are refreshed weekly. This frequency is determined by A/B testing performance metrics, and we aim for no more than 2% degradation between refreshes. |
| How many versions of critical datasets do you maintain and for how long? | We maintain the last five versions of each critical dataset, with a retention period of 18 months for each version. |
| How many cross-functional teams are involved in your generative AI initiatives and have access to your data? | We have three cross-functional teams. Each team includes data scientists, domain experts, ethicists, and business analysts. |
| What data governance policies and practices do you have in place? | We have a cross-functional data governance committee that oversees our data policies. We've implemented role-based access controls, data classification schemes, and regular audits to ensure compliance with our governance framework. |
| What measures do you have in place to ensure data privacy, obtain proper consent, and maintain confidentiality? | We have implemented a comprehensive data privacy framework aligned with GDPR and CCPA. This includes obtaining explicit consent for data usage, implementing data anonymization techniques, and regular privacy impact assessments. |
| What percentage of your AI training datasets have been audited for bias in the last quarter? | 70% of our AI training datasets were audited for bias last quarter. We're implementing automated bias detection tools to reach 100% quarterly audits. |
| What is your current data processing capacity, and how much do you project needing for future generative AI workloads? | Our current capacity is 10 TB/day. We project needing 30 TB/day within a year and are scaling our infrastructure to meet this demand. |
| What is your strategy for balancing data privacy with the data needs of generative AI models? | We're implementing advanced anonymization techniques and synthetic data generation. Our goal is to increase our usable data for AI by 40% while reducing privacy risks by 60% over the next year. |
| What percentage of your machine learning (ML) datasets are accurately labeled, and what's your target accuracy rate? | Currently, 85% of our ML datasets are accurately labeled. We're targeting a 95% accuracy rate within the next quarter by employing both human and automated labeling techniques. |
