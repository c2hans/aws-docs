---
source_url: https://docs.aws.amazon.com/whitepapers/latest/migrating-magento-open-source-adobe-commerce-to-aws/migration-strategies.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Migration strategies
<a name="migration-strategies"></a>

 This section provides the six common migration strategies for moving applications and systems to the cloud and then describes which of those strategies apply to on-premises Magento Open Source or Adobe Commerce on Cloud Infrastructure Self-Service or enterprise edition on AWS. workloads. It’s useful to understand these broader strategies since Magento Open Source or Adobe Commerce on Cloud Infrastructure Self-Service is typically just one component of a portfolio of applications and therefore part of an overall migration plan.

## Six common strategies: "Six Rs"
<a name="six-common-strategies-six-rs"></a>

 The six approaches described below are common migration strategies and build upon ["The 5 Rs" outlined by Gartner in 2011](https://www.gartner.com/en/documents/1485116/migrating-applications-to-the-cloud-rehost-refactor-revi). Choosing the right on-premises Magento Open Source or Adobe Commerce on Cloud Infrastructure Self-Service or enterprise edition on AWS migration strategy depends upon the business drivers for cloud adoption, as well as time considerations, business and financial constraints, and resource requirements.

### Re-host
<a name="re-host"></a>

 Rehosting, or *lift and shift*, is typically used when an organization is looking to quickly migrate applications to the cloud to meet a business case. Applications are moved as-is to the cloud without making any changes to the application or its dependencies. Although this strategy does not immediately bring the full benefits of the cloud, it allows for a swift migration and cost savings from hosting in the cloud.

### Re-platform
<a name="re-platform"></a>

 Also referred to as *lift, tinker, and shift*, re-platforming involves taking an existing application, migrating it to the cloud, and replacing specific application dependencies with fully managed alternatives available in the cloud. For example, rather than directly hosting a relational database on EC2 instances, the database for many applications can be easily replaced by Amazon Relational Database Service (Amazon RDS). The benefit to this strategy is that the operating responsibility of undifferentiated components can be offloaded to AWS without requiring significant changes to the core application.

### Re-purchase
<a name="re-purchase"></a>

 Re-purchase strategy involves moving from perpetual licenses to a software-as-a-service (Saas) model. In context of Adobe, a re-purchase strategy would involve moving from a traditional on-premises Magento Open Source or Adobe Commerce on Cloud Infrastructure Self-Service or enterprise edition on AWS (often referred to as M1) to Magento Commerce cloud by Adobe.

### Re-factor / Re-architect
<a name="re-factor-re-architect"></a>

 Re-factor or Re-architect strategy gives the most opportunity to optimize and re-skin or re-imagine the application architecture from ground up. This presents an opportunity to deliver features using cloud native technologies. This strategy is often driven by strong business need to add features, scale, or performance that would otherwise be difficult to achieve in the application’s existing environment.

### Retire
<a name="retire"></a>

 This strategy involves completing a discovery of the existing environment and removing applications and features that are no longer needed. For example, hardware monitoring may not be required if you are planning to move to a managed Magento Open Source or Adobe Commerce on Cloud Infrastructure Self-Service solution.

### Retain
<a name="retain"></a>

 This is also referred to as a *re-visit* strategy or do nothing. This strategy involves revisiting the existing Magento Open Source or Adobe Commerce on Cloud Infrastructure Self-Service application at a later point in time because migrating to cloud may not align with current business needs.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
