---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-aws-data/technical-assessment.html
---

# Technical assessment
<a name="technical-assessment"></a>

A technical assessment is important because it gives you a map of the current technical capabilities that your company has in place. The assessment covers data governance, data ingestion, data transformation, data sharing, ML platform, process, and automation.

Here are examples of questions you can ask during the technical assessment, by team. You can add questions based on your context.

**Data engineering team:**
+ What are the current challenges associated with ingesting data for your team?
+ Are there any external or internal data sources your team needs that aren't available for ingestion? Why aren't they available?
+ What types of data sources do you ingest data from (for example, MySQL databases, Salesforce API, files received, website navigation data)?
+ How long does it take to ingest data from a new data source?
+ Are the processes of ingesting data from a new source automated?
+ How easy is it for a development team to publish transactional data for analytics from their application?
+ Do you have tools for full loads or incremental loads (in batches or micro-batches) from your data source?
+ Do you have change data capture (CDC) tools for continuous loads from your databases?
+ Do you have data streaming options for data ingestion?
+ How do you perform data transformation for batch and real-time data?
+ How do you manage the orchestration of data transformation workflows?
+ Which activities do you perform most frequently: data discovery and cataloging, data ingestion, data transformation, helping business analysts, helping data scientists, data governance, training teams and users)?
+ When a dataset is created, how is it classified for data privacy? How do you clean it to make it meaningful for your internal consumers?
+ Is data governance and data stewardship centralized or decentralized?
+ How do you enforce data governance? Do you have an automated process?
+ Who is the data owner and steward in each phase of the pipeline: data ingestion, data processing, data sharing, or data usage? Is there a data domain concept for determining owners and stewards?
+ What are the main challenges in sharing datasets within the organization with access control?
+ Do you use infrastructure as a code (IaC) to deploy and manage data pipelines?
+ Do you have a data lake strategy?
  + Is your data lake distributed or centralized across the organization?
+ How is your data catalog organized? Is it companywide or per area?
+ Do you have a data lakehouse approach in place?
+ Do you use or plan to use data mesh concepts?

You can complement these questions with the [AWS Well-Architected Framework Data Analytics Lens](https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/analytics-lens.html).

**Business analysis team:**
+ How would you describe the following characteristics of the data that's available for your work:
  + Cleanliness
  + Quality
  + Classification
  + Metadata
  + Business meaning
+ Does your team participate in business glossary definitions of datasets in your domain?
+ What is the impact of not having the data you need to perform your job at the time you need it?
+ Do you have any examples of scenarios where you don't have access to data or it takes too long to obtain the data? How long does it take to obtain the data you need?
+ How often do you use a smaller dataset than you needed because of technical issues or processing time?
+ Do you have a sandbox environment with the scale and tools that you need?
+ Can you perform A/B testing to validate hypotheses?
+ Are you missing any tools you need to perform your job?
  + Which types of tools?
  + Why aren't they available?
+ Are there any important activities that you don't have time to perform?
+ Which activities consume your time the most?
+ How are your business views refreshed?
  + Are they scheduled and managed automatically?
+ In which scenarios would you need data that's fresher than the data you get?
+ How do you share analyses? Which tools and processes do you use for sharing?
+ Do you often create new data products and make them available to other teams?
  + What is your process for sharing data products with other business areas or across the company?

**Data science teams (to determine model deployment):**
+ How would you describe the following characteristics of the data that's available for your work:
  + Cleanliness
  + Quality
  + Classification
  + Metadata
  + Meaning
+ Do you have any automated tools for training, testing, and deploying machine learning (ML) models?
+ Do you have machine size options for performing each step in the creation and deployment of an ML model?
+ How are the ML models put in production?
+ What are the steps to deploy a new model? How automated are they?
+ Do you have the components to train, test, and deploy ML models for batch and real-time data?
+ Can you use and process a dataset that's large enough to represent the data you need to create the model?
+ How do you monitor your models and take actions to retrain them?
+ How do you measure the impact of the models to your business?
+ Can you perform A/B testing to validate hypotheses for business teams?

For additional questions, see the [AWS Well-Architected Framework Machine Learning Lens](https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/machine-learning-lens.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
