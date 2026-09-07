---
source_url: https://docs.aws.amazon.com/whitepapers/latest/sagemaker-studio-admin-best-practices/operating-model.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Operating model
<a name="operating-model"></a>

 An *operating model* is a framework that brings people, processes, and technologies together to help an organization deliver business value in a scalable, consistent, efficient manner. The ML operating model provides a standard product development process for teams across the organization. There are three models for implementing the operating model, depending on the size, complexity, and business drivers:
+  **Centralized data science team** — In this model, all data science activities are centralized within a single team or organization. This is similar to the Center of Excellence (COE) model, where all business units go to this team for data science projects.
+  **Decentralized data science teams** — In this model, data science activities are distributed across different business functions or divisions, or based on different product lines.
+  **Federated data science teams** — In this model, shared services functions such as code repositories, continuous integration and continuous delivery (CI/CD) pipelines, and so on are managed by the centralized team, and each business unit or product level function is managed by decentralized teams. This is similar to the hub and spoke model, where each business unit has their own data science teams; however, these business unit teams coordinate their activities with the centralized team.

 Before deciding to launch your first studio domain for production use cases, consider your operating model and AWS best practices for organizing your environment. For more information, refer to [Organizing Your AWS Environment Using Multiple Accounts](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.html).

The next section provides guidance on organizing your account structure for each of the operating models.

## Recommended account structure
<a name="recommended-account-structure"></a>

 In this section, we briefly introduce an operating model account structure that you can start with and modify according to your organization’s operating requirements. Regardless of the operating model you choose, we recommend implementing the following common best practices:
+  Use [AWS Control Tower](https://aws.amazon.com/controltower/) for setup, management, and governance of your accounts.
+  Centralize your identities with your Identity Provider (IdP), and [AWS IAM Identity Center](https://aws.amazon.com/iam/identity-center/) with a delegated administrator [Securitiy Tooling account](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/security-tooling.html) and enable secure access to workloads.
+  Run ML workloads with account level isolation across development, test, and production workloads.
+  Stream ML workload logs to a log archive account, and then filter and apply log analysis in an observability account.
+  Run a centralized governance account for provisioning, controlling, and auditing data access.
+  Embed security and governance services (SGS) with appropriate preventive and detective guardrails into each account to ensure security and compliance, as per your organization and workload requirements.

### Centralized model account structure
<a name="centralized-model-account-structure"></a>

 In this model, the ML platform team is responsible for providing:
+  A shared services tooling account that addresses the Machine Learning Operations ([MLOps](https://en.wikipedia.org/wiki/MLOps)) requirements across data science teams.
+  ML workload development, test, and production accounts that are shared across data science teams.
+  Governance policies to ensure each data science team workload runs in isolation.
+  Common best practices.

![A diagram depicting a centralized operating model account structure.](https://docs.aws.amazon.com/whitepapers/latest/sagemaker-studio-admin-best-practices/images/com-account-structure.png)

### Decentralized model account structure
<a name="decentralized-model-account-structure"></a>

 In this model, each ML team operates independently for provisioning, managing, and governing ML accounts and resources. However, we recommend ML teams use a centralized observability and data governance model approach to simplify data governance and audit management.

![A diagram that depicts a decentralized operating model account structure.](https://docs.aws.amazon.com/whitepapers/latest/sagemaker-studio-admin-best-practices/images/decentralized-model.png)

### Federated model account structure
<a name="federated-model-account-structure"></a>

 This model is similar to the centralized model; however, the key difference is that each data science/ML team gets their own set of development/test/production workload accounts that enable robust physical isolation of their ML resources, and also enable each team to scale independently without impacting other teams.

![A document depicting a federated operating model account structure.](https://docs.aws.amazon.com/whitepapers/latest/sagemaker-studio-admin-best-practices/images/fom-account-structure.png)

## ML platform multitenancy
<a name="ml-platform-multitenancy"></a>

 *Multitenancy* is a software architecture where a single software instance can serve multiple, distinct, user groups. A *tenant* is a group of users who share common access with specific privileges to the software instance. For example, if you are building several ML products, then each product team with similar access requirements can be considered a tenant or a team.

 While it possible to implement multiple teams within a SageMaker AI Studio instance (such as [SageMaker AI Domain](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-entity-status.html)), weigh those advantages against trade-offs such as blast radius, cost attribution, and account level limits when you bring multiple teams into a single SageMaker AI Studio domain. Learn more about those trade-offs and best practices in the following sections.

If you need absolute resource isolation, consider implementing SageMaker AI Studio domains for each tenant in different account. Depending on your isolation requirements, you may implement multiple lines of businesses (LOBs) as multiple domains within a single account and Region. Use shared spaces for near real-time collaboration between members of the same team/LOB. With multiple domains, you will still use identity access management (IAM) policies and permissions to ensure resource isolation.

SageMaker AI resources created from a domain are auto-tagged with the domain [Amazon Resource Name](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) (ARN) and the user profile or space ARN for easy resource isolation. For sample policies, refer to [Domain resource isolation documentation](https://docs.aws.amazon.com/sagemaker/latest/dg/domain-resource-isolation.html). There you can see the detailed reference for when to use a multi-account or a multi-domain strategy, along with the feature comparisons in the documentation, and you can view sample scripts to backfill tags for existing domains on the [GitHub repository](https://github.com/aws-samples/sm-studio-best-practices/tree/main/domain-management).

Finally, you can implement a self-service deployment of SageMaker AI Studio resources into multiple accounts using [AWS Service Catalog](https://aws.amazon.com/servicecatalog/). For more information, refer to [Manage AWS Service Catalog products in multiple AWS accounts and AWS Regions](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/manage-aws-service-catalog-products-in-multiple-aws-accounts-and-aws-regions.html).
