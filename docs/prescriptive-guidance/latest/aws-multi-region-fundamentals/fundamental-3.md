---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-multi-region-fundamentals/fundamental-3.html
---

# Multi-Region fundamental 3: Understanding your workload dependencies
<a name="fundamental-3"></a>

A specific workload might have several dependencies in a Region, such as AWS services used, internal dependencies, third-party dependencies, network dependencies, certificates, keys, secrets, and parameters. To ensure operation of the workload during a failure scenario, there should be no dependencies between the primary Region and the standby Region; each should be able to operate independently of the other. To achieve this, scrutinize all dependencies in the workload to make sure that they are available within each Region. This is required because a failure in the primary Region should not affect the standby Region. In addition, you must understand how the workload operates when a dependency is in a degraded state or completely unavailable, so you can engineer solutions to handle this appropriately.

## 3.a: AWS services
<a name="3a-aws-services"></a>

When you design a multi-Region architecture, it's important to understand the AWS services that will be used, the [multi-Region features](https://repost.aws/articles/AR02pJIdoARYKX6Rhkdra-Zg/aws-multi-region-capabilities) of those services, and what solutions you will need to engineer to accomplish multi-Region goals. For example, Amazon Aurora and Amazon DynamoDB can asynchronously replicate data to a standby Region. All AWS service dependencies will need to be available in all Regions that a workload is going to run from. To confirm that the services you use are available in the desired Regions, review the [AWS services by Region list](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/?p=ugi&l=na).

## 3.b: Internal and third-party dependencies
<a name="3b-dependencies"></a>

Make sure that every workload's internal dependencies are available in the Regions from which they operate. For example, if the workload is composed of many microservices, identify all the microservices that comprise a business capability and verify that all those microservices are deployed in each Region from which the workload operates. Alternatively, define a strategy to gracefully handle microservices that become unavailable.

Cross-Region calls between microservices within a workload are not advised, and Regional isolation should be maintained. This is because creating cross-Region dependencies adds the risk of correlated failure, which offsets the benefits of isolated Regional implementations of the workload. On-premises dependencies might be part of the workload as well, so it is important to understand how characteristics of these integrations could change if the primary Region were to change. For example, if the standby Region is located farther from the on-premises environment, the increased latency might have a negative impact.

Understanding software as a service (SaaS) solutions, software development kits (SDKs), and other third-party product dependencies, and being able to exercise scenarios where these dependencies are either degraded or unavailable will provide more insight into how the chain of systems operates and behaves under different failure modes. These dependencies could be within your application code, such as managing secrets externally by using [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/), or they could involve a third-party vault solution (such as HashiCorp), or authentication systems that have a dependency on [AWS IAM Identity Center](https://aws.amazon.com/iam/identity-center/)for federated logins.

Having redundancy when it comes to dependencies can increase resilience. If a SaaS solution or third-party dependency uses the same primary AWS Region as the workload, work with the vendor to determine if their resilience posture matches your requirements for the workload.

Additionally, be aware of shared fate between the workload and its dependencies, such as third-party applications. If the dependencies are not available in (or from) a secondary Region after a failover, the workload might not recover fully.

## 3.c: Failover mechanism
<a name="3c-failover-mechanism"></a>

DNS is commonly used as a failover mechanism to shift traffic away from the primary Region to a standby Region. Critically review and scrutinize all dependencies the failover mechanism takes. For example, if your workload uses [Amazon Route 53](https://aws.amazon.com/route53/), understanding that the control plane is hosted in `us-east-1` means you are taking a dependency on the control plane in that specific Region. This is not recommended as part of a failover mechanism if the primary Region is also `us-east-1` because it creates a single point of failure. If you use another failover mechanism, you should have a deep understanding of scenarios in which failover wouldn't work as expected, and then plan for contingency or develop a new mechanism if required. [Amazon Application Recovery Controller (ARC) Region switch](https://docs.aws.amazon.com/r53recovery/latest/dg/region-switch.html) is a fully managed multi-Region recovery service that you can use as your failover mechanism.

As discussed in the previous section, all microservices that are part of a business capability need to be available in each Region in which the workload is deployed. As part of the failover strategy, all microservices that are part of the business capability should fail over together to remove the chance of cross-Region calls. Alternatively, if microservices fail over independently, there is a potential for undesirable behavior such as microservices potentially making cross-Region calls. This introduces latency and could lead to the workload becoming unavailable during client timeouts.

## 3.d: Configuration dependencies
<a name="3d-configuration-dependencies"></a>

Certificates, keys, secrets, Amazon Machine Images (AMIs), container images, and parameters are part of the dependency analysis needed when designing for a multi-Region architecture. Whenever possible, it's best to localize these components within each Region so they do not have shared fate between Regions for these dependencies. For example, you should vary the expiration dates of certificates to prevent a scenario where an expiring certificate (with alarms set to "notify in advance") impacts multiple Regions.

Encryption keys and secrets should be Region-specific as well. That way, if there is an error in the rotation of a key or secret, the impact is limited to a specific Region.

Lastly, any workload parameters should be stored locally for the workload to retrieve in the specific Region.

## Key guidance
<a name="key-guidance-3"></a>
+ A multi-Region architecture benefits from physical and logical separation between Regions. Introducing cross-Region dependencies at the application layer breaks this benefit. Avoid such dependencies.
+ Failover controls should work with no dependencies on the primary Region.
+ Failover should be coordinated across a user journey to remove the possibility of increased latency and dependency of cross-Region calls.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
