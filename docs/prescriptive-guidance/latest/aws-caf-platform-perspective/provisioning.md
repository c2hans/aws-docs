---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-caf-platform-perspective/provisioning.html
---

# Provisioning and orchestration
<a name="provisioning"></a>

**Create, manage, and distribute catalogs of approved cloud products to users.**

Provisioning infrastructure in a consistent, scalable, and repeatable manner becomes more challenging as your organization grows. Streamlined [provisioning and orchestration](https://aws.amazon.com/products/management-and-governance/use-cases/provisioning-and-orchestration/) help you achieve consistent governance and meet your compliance requirements while enabling users to deploy only approved cloud products.

Reusing pre-approved products in your organization enables your developers to build applications faster and more consistently while meeting the security and governance requirements of your organization.

## Start
<a name="provisioning-start"></a>

### Deploy a hub-and-spoke catalog model
<a name="deploy-a-hub-and-spoke-catalog-model.207b6fe4-23c4-50b5-bfd7-543de3144399"></a>

Software assets that are managed in a service catalog as portfolios are shared with users in one or more accounts in a hub-and-spoke pattern. You can use a private marketplace and private oﬀers to curate an assortment of third-party solutions and distribute them with your infrastructure as code (IaC) templates.

To enable your builders to consume pre-approved products, define a process to review, approve, and publish these products to your users. Start by designing and implementing a centrally managed repository that contains these pre-approved products. Design a system that grants access to the licenses and products in this repository when the users in your organization need to consume each product.

Allow the builders in your organization to submit products for approval to the publishing mechanism, so these products are made available for all users in your organization after they are approved.

### Curate templates for reuse
<a name="curate-templates-for-reuse.24c00a18-05e4-522e-b87c-fdaaf0d6248b"></a>

When you have codified the IaC templates for your solutions and defined your hub-and-spoke model, you should define two categories of templates for each spoke account: *provisioned/enforced* and *available to consume*. *Provisioned/enforced* templates are provisioned directly from the management account into each member account as foundational capabilities. *Available to consume* templates are available for builders to browse and provision in a self-service manner.

### Apply default parameters for reuse
<a name="apply-default-parameters-for-reuse.454ec463-3062-5f7e-9fb6-e02fe4ac0313"></a>

Implement IaC templates that include default parameters that your builders can preselect. This enables builders to align to governance without having to evaluate the details of each parameter, and prevents them from making incorrect choices. This approach exposes only what is needed for setup. For example, [AWS Service Catalog](https://docs.aws.amazon.com/servicecatalog/) implements this approach with a constraint capability that controls the rules that are applied to a product in a specific portfolio. This customization is preconfigured when the builder team uses self-service provisioning of templates.

### Establish an approval process
<a name="establish-an-approval-process.1a269c34-0fa1-5072-97b6-f7b895f34b41"></a>

Users should be able to submit requests to access a product they are not approved for if they have a business justification to use the product. Build a notification system that informs users when updates for the products they are using are available, so they can comply with the latest security updates.

Establish a workflow for builders to submit new products for review through the self-service portal. Builders can use the portal to define the audience for the product and to identify the user groups that should have access to the product. For each submission, use your defined processes to review, approve, and publish the product to the self-service portal.

## Advance
<a name="provisioning-advance"></a>

### Create a self-service portal
<a name="create-a-self-service-portal.92d24785-f675-5d9f-904a-81ad862a1947"></a>

Create a self-service portal to distribute, browse, and consume approved cloud products. The users in the organization can use this portal to search for the products they need to build their infrastructure and to deploy applications to their environment. Establish permissions boundaries for users who have access to the products in the portal, and set limits on the number of times a user can consume licensed products. Deﬁne a base set of resources that can be directly provisioned or made available as a self-service model in each of your spoke accounts, as the accounts are created, solutions such as [Customizations for AWS Control Tower](https://aws.amazon.com/solutions/implementations/customizations-for-aws-control-tower/).

### Enable a private marketplace
<a name="enable-a-private-marketplace.26ebabd8-04ec-5b43-8abe-b1b8fa626489"></a>

A private marketplace provides a curated catalog of purchased products (software, data, and professional services) and is implemented in a hub-and-spoke pattern (with one management account and multiple member accounts) so that spoke accounts can subscribe to only the approved software. This product governance helps control software costs and streamlines legal and contractual reviews. Create a private marketplace at the management account level to serve as the primary hub.

### Manage entitlements
<a name="manage-entitlements.85741f93-9d9a-5593-9fa3-3a6548e2491d"></a>

Enable controls that allow only authorized users and workloads to consume a license within vendor-defined limits. This helps reduce the risk of costly audits and unexpected licensing tune-ups.

## Excel
<a name="provisioning-excel"></a>

### Integrate with procurement systems
<a name="integrate-with-procurement-systems.f3db2af9-191a-5fc7-8913-190c57cdd2f2"></a>

Complement your existing procurement processes by integrating them into [AWS Marketplace](https://docs.aws.amazon.com/marketplace/latest/buyerguide/what-is-marketplace.html). This is done by extending your procurement systems (Coupa or SAP Ariba) to a private marketplace so your users can follow existing procurement and approval processes to obtain software. Create the appropriate IAM-managed permissions, use AWS Marketplace to generate the necessary information to configure your procurement solution, and configure your procurement solution to complete the integration. For example, you can [set up a punchout](https://docs.aws.amazon.com/marketplace/latest/buyerguide/procurement-system-integration-setup.html), attach purchase orders to your AWS invoices, and then align your procurement processes to use the standard provisioning solutions.

Enable your builders to access the pre-approved products through an internal API, so users can incorporate the products into their applications or build their own personalized portals for their teams to consume the products. Integrate the submission and publication process for creating new products, and allow users to request new licenses and access to products through APIs.

### Integrate with your ITSM tools
<a name="integrate-with-your-itsm-tools.cbf1e314-091c-5a5c-b114-e049b189c66e"></a>

If applicable, [connect with IT service management (ITSM) tools](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/integrations.html) and automate any updates to your configuration management database (CMDB). Establish processes and mechanisms to evaluate the products that your organization uses. Establish a mechanism to inform users of pre-approved products that they need to update for compliance. Use your ITSM tools to analyze your environment and to push security and compliance updates to products across your organization when critical updates are needed.

### Implement a lifecycle management and version distribution system
<a name="implement-a-lifecycle-management-and-version-distribution-system.43c4c461-30fb-59e6-ba2f-21a108761d43"></a>

Maintain versions of IaC templates, and versions of services provisioned from the templates, throughout their development lifecycle. You can use the hub-and-spoke model you implemented for your catalog to define whether a forced update is required at a spoke level (for example, if concurrent versions are available for self-service provisioning), and which versions need to be marked for obsolescence. Using a hub-and-spoke catalog also helps manage the audit and distribution of new versions as required.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
