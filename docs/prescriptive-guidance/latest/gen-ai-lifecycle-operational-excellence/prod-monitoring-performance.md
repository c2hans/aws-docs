---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-lifecycle-operational-excellence/prod-monitoring-performance.html
---

# Pillars of monitoring generative AI application performance in production
<a name="prod-monitoring-performance"></a>

Effective performance monitoring in the production stage helps you make sure that the system remains reliable and effective. A well-rounded monitoring framework includes monitoring across the following three pillars:
+ **Application and system health** – This pillar helps you validate that the generative AI application is highly available and cost efficient. It focuses on the operational stability, scalability, and runtime performance of the application and support infrastructure. Some example key metrics include:
  + **Latency** – Speed of response delivery
  + **Throughput** – Volume of requests
  + **Uptime and reliability** – System availability, error rates, and service-level agreement (SLA) adherence
  + **Resource utilization** – CPU, GPU, memory, and bandwidth consumption
  + **Cost efficiency** – Infrastructure and API usage costs
+ **Business and user-interaction health** – This pillar helps you evaluate whether the application meets business objectives. This can include tracking adoption, customer satisfaction, and measurable impacts on the business process. Example key metrics include:
  + **User engagement** – Track active user count, repeat usage, task completion rates.
  + **Customer satisfaction** – Monitor net promoter score (NPS) and qualitative feedback trends.
  + **Business impact** – Track productivity improvements, cost savings, revenue growth, or task automation efficiency.
  + **Compliance and risk indicators** – Adhere to governance requirements, such as logging actions related to data access, model changes, and production deployments. Track regulatory compliance, such as tracking use of PII and verifying consent. Investigate and resolve policy violations, such as improper model use or ethics complaints.
+ **Model and AI quality health** –** **This pillar helps you assess the accuracy, consistency, and fairness of the model. It helps you make sure that the output remains relevant, aligned with the intended outcome, and free from degradation, hallucinations, or ethical issues. Key metrics include the following:
  + **Accuracy and relevance** – Alignment of output with user prompts
  + **Hallucination rates** – Frequency of generating false or misleading information
  + **Bias and fairness** – Monitoring for skewed or harmful outputs
  + **Model drift detection** – Identifying any shift in the model effectiveness due to changing inputs
  + **Explainability and traceability** – Attributing outputs to a specific model version, prompt, or knowledge source
  + **Prompt and knowledge base versioning** – Measuring the impact of prompt engineering or a RAG dataset over time

Production monitoring underpins a robust system with three main key components: capture, alerts, and response. Monitoring should provide real-time insights into the health of the application, actionable alerts, and (ideally) automation to react to these alerts.

When implementing the metric or log capture system, you need to consider the following:
+ Which metrics and logs need to be captured
+ How to capture this information
+ How frequently to record it
+ When to aggregate metrics or summarize logs
+ Where to store the captured information
+ How to access the captured information

While having metrics, logs, and traces is useful, you often need to sift through a lot of information to find and detect a problem. Thus, it is important to define and create actionable alerts that align to your business objectives and technical requirements. Use rule-based or ML-based mechanisms to detect errors or anomalies in the system, and confirm that these alerts are directed to the relevant stakeholders with an actionable outcome.

The final component of a monitoring system focuses on how to respond to these alerts. The response should be systematic and, ideally, automated. This involves designing runbooks that attach to each alert in order to help teams effectively perform root-cause analysis. Alternatively, you can create codified runbooks that automate the investigation and resolution process.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
