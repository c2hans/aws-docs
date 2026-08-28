---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-workload-assessment/deployment-and-automation.html
---

# Deployment and automation
<a name="deployment-and-automation"></a>

|
|
| Question | Example response |
| --- |--- |
| What are the requirements for scaling and load balancing? | ?? |
| What are the requirements for updating and rolling out new versions? | Blue/green deployments, canary releases, rolling updates, and so on. |
| What are the requirements for disaster recovery and business continuity? | Backup and restore procedures, failover mechanisms, high availability configurations, and so on. |
| What are the requirements for automating the training, deployment, and management of the generative AI model? | Automated training pipeline, continuous deployment, automatic scaling, and so on. |
| How will the generative AI model be updated and retrained as new data becomes available? | Through periodic retraining, incremental learning, transfer learning, and so on. |
| What are the requirements for automating monitoring and management? | Automated alerts, automatic scaling, self-healing, and so on. |
| What is your preferred deployment environment for generative AI workloads? | A hybrid approach that uses AWS for model training and our on-premises infrastructure for inference to meet data residency requirements. |
| Are there any specific cloud platforms you prefer for generative AI deployments? | AWS services, particularly Amazon SageMaker AI for model development and deployment, and Amazon Bedrock for foundation models. |
| What containerization technologies are you considering for generative AI workloads? | We want to standardize on Docker containers that are orchestrated with Kubernetes to ensure portability and scalability across our hybrid environment. |
| Do you have any preferred tools for CI/CD in your generative AI pipeline? | GitLab for version control and CI/CD pipelines, integrated with Jenkins for automated testing and deployment. |
| What orchestration tools are you considering for managing generative AI workflows? | Apache Airflow for workflow orchestration, particularly for data preprocessing and model training pipelines. |
| Do you have any specific requirements for on-premises infrastructure to support generative AI workloads? | We're investing in GPU-accelerated servers and high-speed networking to support on-premises inference workloads. |
| How do you plan to manage model versioning and deployment across different environments? | We plan to use MLflow for model tracking and versioning, and integrate it with our Kubernetes infrastructure for seamless deployment across environments. |
| What monitoring and observability tools are you considering for generative AI deployments? | Prometheus for metrics collection and Grafana for visualization, with additional custom logging solutions for model-specific monitoring. |
| How are you addressing data movement and synchronization in a hybrid deployment model? | We will use AWS DataSync for efficient data transfer between on-premises storage and AWS, with automated synchronization jobs that are scheduled based on our training cycles. |
| What security measures are you implementing for generative AI deployments across different environments? | We will use IAM for cloud resources, integrated with our on-premises Active Directory to implement end-to-end encryption and network segmentation to secure data flows. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
