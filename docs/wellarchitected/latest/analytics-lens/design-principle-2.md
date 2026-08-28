---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/design-principle-2.html
---

# 2 – Modernize deployment of the analytics jobs and applications
<a name="design-principle-2"></a>

 **How do you deploy jobs and applications in a controlled and reproducible way?** Using modern development practices, such as continuous integration/continuous delivery (CI/CD), can help ensure that changes are rolled out in a controlled and repeatable way.

 Your team should use test automation to verify infrastructure, code changes, and data updates at every stage of your deployment lifecycle. The analytics processing often requires management of complex workflows. It includes job scheduling, managing dependencies between jobs, and monitoring jobs. You also need an orchestration tool for data movement.

|  **ID**  |  **Priority**  |  **Best practice**  |
| --- | --- | --- |
| ☐ BP 2.1  |  Recommended  |  Use version control for job and application changes.  |
| ☐ BP 2.2  |  Recommended  |  Create test data and provision staging environment.  |
| ☐ BP 2.3  |  Recommended  |  Test and validate analytics jobs and application deployments.  |
| ☐ BP 2.4  |  Recommended  |  Build standard operating procedures for deployment, test, rollback, and backfill tasks.  |

 For more details, refer to the following information:
+ Reference architecture: [Deployment Pipeline Reference Architecture](https://pipelines.devops.aws.dev/)
+ AWS Big Data Blog: [Build, Test and Deploy ETL solutions using AWS Glue and AWS CDK based CI/CD pipelines ](https://aws.amazon.com/blogs/big-data/build-test-and-deploy-etl-solutions-using-aws-glue-and-aws-cdk-based-ci-cd-pipelines/)
+  AWS Big Data Blog: [AWS serverless data analytics pipeline reference architecture](https://aws.amazon.com/blogs/big-data/aws-serverless-data-analytics-pipeline-reference-architecture/)
+  AWS Whitepaper: [Building a Cloud Operating Model](https://docs.aws.amazon.com/whitepapers/latest/building-cloud-operating-model/building-cloud-operating-model.html)
+  AWS Big Data Blog: [Build a DataOps platform to break silos between engineers and analysts](https://aws.amazon.com/blogs/big-data/build-a-dataops-platform-to-break-silos-between-engineers-and-analysts/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
