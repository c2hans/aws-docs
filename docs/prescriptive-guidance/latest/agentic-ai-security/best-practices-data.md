---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-security/best-practices-data.html
---

# 5. Data security and governance for agentic AI systems on AWS
<a name="best-practices-data"></a>

Data protection in agentic AI systems extends beyond traditional access controls. It includes model training data and inference outputs. Proper classification and handling reduce the likelihood of inadvertent exposure through model interactions or training processes.

**This section contains the following best practices:**
+ [5.1 Implement pipelines for fine-tuning data (AI-specific)](#best-practices-5-data-pipelines)
+ [5.2 Restrict AI operations against sensitive systems (AI-specific)](#best-practices-5-restrict-ai-operations)
+ [5.3 Establish a data governance framework (General)](#best-practices-5-data-governance)
+ [5.4 Prevent data loss (General)](#best-practices-5-data-loss)

## 5.1 Implement pipelines for fine-tuning data (AI-specific)
<a name="best-practices-5-data-pipelines"></a>

Fine-tuning data shapes system behavior and responses. For more information, see [Machine Learning Lens - AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/machine-learning-lens.html). Understanding the lineage, bias, and quality of the data can support informed decisions about which data to include when fine tuning. Including data from other systems or data generated from the in-scope system without appropriate data quality measures can open the system to poisoning or misinformation attacks. For these reasons, it is highly recommended that you implement a [data pipeline](https://docs.aws.amazon.com/pdfs/whitepapers/latest/aws-glue-best-practices-build-efficient-data-pipeline/aws-glue-best-practices-build-efficient-data-pipeline.pdf) to deliver data into the production system and remove human access to this data.

Fine-tuning data might be vulnerable to exposure through some attack methods. For this reason, we recommend that you perform a risk evaluation on what data is used. For more information, see [Implement data purification filters for model training workflows](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/gensec06-bp01.html) in the AWS Well-Architected Framework. For some organizations, using sensitive data for fine tuning might be unpalatable due to the risk of sensitive information disclosure through prompt manipulation. This conservative approach can help protect your organization's data.

## 5.2 Restrict AI operations against sensitive systems (AI-specific)
<a name="best-practices-5-restrict-ai-operations"></a>

Restrict AI operations against critical data sources by implementing validation and approval workflows before data access or modification. When downstream systems lack adequate controls, deploy a deterministic broker tool to mediate between agents and data sources.

The following image shows how you can use a deterministic broker tool to inspect user prompts for malicious attacks. On the left side of the image, without a deterministic broker tool, the agent might allow a malicious action on the data system. On the right side of the image, a deterministic broker tool provides an additional control layer. It implements adaptive authentication to inspect and govern high-risk data modifications. For more information about adaptive authentication, see [Working with adaptive authentication](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-settings-adaptive-authentication.html) in the Amazon Cognito documentation.

![A broker tool inspects prompts for malicious actions and governs high-risk data modifications.](http://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-security/images/guide-img/562fab0c-abe0-4a40-a738-87a61cbd8d2a/images/745b9514-1977-4e65-9063-e6416f59e5b5.png)

## 5.3 Establish a data governance framework (General)
<a name="best-practices-5-data-governance"></a>

Authorization systems control access to organizational assets, and data is one of the most important resources that require protection. Mature [data governance](https://aws.amazon.com/what-is/data-governance/) provides the foundation that enables agents to operate autonomously while respecting organizational data protection policies. Data governance frameworks should align with authorization systems to eliminate ambiguity or errors when agents evaluate access permissions. For more information, see [Data security, lifecycle, and strategy for generative AI applications](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-data-considerations-gen-ai/introduction.html) on AWS Prescriptive Guidance.

## 5.4 Prevent data loss (General)
<a name="best-practices-5-data-loss"></a>

[Data loss prevention (DLP)](https://aws.amazon.com/what-is/data-loss-prevention/) technology can act as an additional defense-in-depth layer for agentic AI systems. It can detect and prevent unauthorized data exfiltration. DLP implementations vary widely, and efficacy as a control can vary depending on the data type, volume, and baseline. If organizations have well-established DLP capabilities, extending these capabilities to support agentic AI systems can provide an efficient supplementary control.
