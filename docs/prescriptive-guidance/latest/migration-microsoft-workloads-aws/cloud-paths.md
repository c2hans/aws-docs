---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-microsoft-workloads-aws/cloud-paths.html
---

# Paths to the cloud
<a name="cloud-paths"></a>

This section describes a high-level approach for implementing best practices to migrate your Windows applications to AWS. Details of these migration strategies and steps are described in the subsequent sections of this guide.

## Migration strategies
<a name="migration-strategies"></a>

A migration strategy is the approach used to migrate a workload to the AWS Cloud. There are seven migration strategies for moving applications to the cloud. These strategies are known as the 7 Rs and build upon the [7 Rs](https://www.gartner.com/smarterwithgartner/7-options-to-modernize-legacy-systems) that Gartner identified in 2019.
+ **Rehost (lift and shift)** – Move an application to the cloud without making any changes to take advantage of cloud capabilities.
+ **Relocate (hypervisor-level lift and shift)** – Move infrastructure to the cloud without purchasing new hardware, rewriting applications, or modifying your existing operations.
+ **Replatform (lift and reshape)** – Move an application to the cloud and introduce some level of optimization to take advantage of cloud capabilities.
+ **Repurchase (drop and shop)** – Switch to a different product, typically by moving from a traditional license to a software as a service (SaaS) model.
+ **Refactor/re-architect** – Move an application and modify its architecture by taking full advantage of cloud-native features to improve agility, performance, and scalability.
+ **Retain (revisit)** – Keep applications in your source environment. These might include applications that require major refactoring, and you want to postpone that work until a later time, and legacy applications that you want to retain, because there's no business justification for migrating them.
+ **Retire **– Decommission or remove applications that are no longer needed in your source environment.

## Main transformations
<a name="main-transformations"></a>

The following main transformations take place when you modernize legacy Windows applications and databases:
+ **Rehost** – The first step is moving your on-premises infrastructure to cloud infrastructure. This strategy is often referred to as "lift and shift" or rehosting. Rehosting means migrating existing applications and databases to a cloud server instance. There is no need for code changes and you're responsible for managing the instance configuration, software image, and other resources.
+ **Replatform** – After you migrate to a cloud environment, the next transformation is around replatforming the applications and databases into a more automated and managed environment. From an application perspective, that means moving from virtual machines (VMs) to containers or to a managed application platform. Containerizing applications can help you develop, maintain, and deploy applications faster and improve portability. Alternatively, [AWS Elastic Beanstalk ](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/Welcome.html)offers a managed platform that automatically handles capacity provisioning, load balancing, and scaling. This helps you to replatform applications with minimal infrastructure management and without the need to fully containerize them. On the database side, moving from a self-service model to a managed database service, like Amazon RDS for SQL Server, eliminates the need for provisioning, patching, and backups. This frees up resources for activities that can add more value to your organization.
+ **Refactor/re-architect** – The third area of transformation is to move from commercial software licensing to open-source options. Many traditional commercial software vendors have built their businesses around software license agreements that are aimed at locking in customers and using punitive licensing terms to force upgrades and migrations. Often, commercial software license fees typically add 20–50 percent of cost on top of equivalent open-source options. We recommend refactoring your applications and databases to take advantage of open-source options so that you can reduce costs, improve performance, and gain access to the latest innovations.

You can complete these main areas of transformation progressively in stages or all at once depending on your application and overall readiness to modernize.

## Choosing a migration strategy
<a name="choosing-migration-strategy"></a>

The migration strategy to choose depends on the business and IT goals of your organization. Some of the most common business drivers are reducing cost, reducing risk, improving efficiency, addressing skill gaps, and speeding up innovation. We recommend that you evaluate which drivers are important for you, and then choose a migration strategy based on your drivers by using the following guidance. Also, remember that all three approaches are possible roads on your cloud modernization journey, depending on your priorities during each phase of the journey.

### When to rehost
<a name="when-to-rehost.f48ced19-5d28-5bbd-afee-cfd3483f7360"></a>

Rehosting (or lift and shift) is typically faster and easier because you don't need to make code or architecture changes in the application. Rehosting also minimizes risks and disruption to the business. The operations team can continue to run the business as usual because the application isn't changed. This is especially true for migrations at scale where even a small change becomes significant because of the large number of workloads involved. However, it's important to consider that rehosting doesn't take full advantage of cloud benefits. For example, if you migrate an application with an existing platform issue, that issue will remain after the migration. Finally, it's worth considering that the total cost of ownership (TCO) and return on investment (ROI) for rehosting is lower compared with the other migration approaches.

### When to replatform/re-architect
<a name="when-to-replatform-re-architect.c00b83a2-2bd9-5387-8570-a8bc2a871ae2"></a>

Replatforming is generally more cost-effective than rehosting. You can use replatforming to enhance automation and enable your applications to better use cloud capabilities such as auto-scaling, monitoring, and performing backups. Replatforming reduces operational overhead for the cloud operations team and minimizes risks from pre-existing platform issues. However, replatforming takes longer than a rehosting migration. Also, replatforming requires additional skills to configure the automation that performs code changes on the application and to operationalize the new platform.

### When to refactor
<a name="when-to-refactor.0715bc0c-55b3-5093-b8dd-0083de7b14e5"></a>

A refactor is generally the most cost-effective migration approach. Refactoring is a cloud-native approach that enables applications to rapidly adapt to new requirements by decoupling application components to improve on application resiliency. However, refactoring requires more advanced coding and automation skills. Refactoring also takes longer to implement because it involves rebuilding applications.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
