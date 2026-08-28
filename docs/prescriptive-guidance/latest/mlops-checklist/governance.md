---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/mlops-checklist/governance.html
---

# 9. Governance
<a name="governance"></a>

ML governance encompasses a set of processes and frameworks that help in the deployment of ML models. It includes model explainability, auditability, traceability, and other more abstract but essential requirements of a successful end-to-end ML lifecycle.

|  |
| --- |
| 9.1 Data quality and compliance | The ML system accounts for personal identifying information (PII) considerations, including anonymization. It has documented and reviewed column-level lineage for understanding the source, quality, and appropriateness of the data. It also has automated data quality checks for anomalies. |
| --- |--- |
| **9.2 Audit and documentation** | The ML system has a full log of all changes during development, including experiments run and reasons for choices made for regulatory compliance. |
| **9.3 Reproducibility and traceability** | The ML system includes a full data snapshot for precise and rapid model re-instantiation, or it has the ability to recreate the environment and retrain with a data sample. |
| **9.4 Human-in-the-loop signoff** | The ML system has manual verification and authorization for regulatory compliance. The system requires signoffs for every environment move (for example, Dev, QA, pre-Prod, and Prod). |
| **9.5 Bias and adversarial attacks testing** | The ML system has *Red Team* adversarial testing using multiple tools and attack vectors, and automated bias checking on specific subpopulations. This component ties back to the Observability and model management section. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
