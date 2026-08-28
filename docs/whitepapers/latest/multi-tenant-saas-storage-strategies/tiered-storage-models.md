---
source_url: https://docs.aws.amazon.com/whitepapers/latest/multi-tenant-saas-storage-strategies/tiered-storage-models.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Tiered storage models
<a name="tiered-storage-models"></a>

 AWS provides developers with a wide range of storage services, each of which can be applied in combinations to address the varying cost and performance requirements of SaaS tenants. The key here is not to artificially constrain your storage strategy to any one AWS service or storage technology.

 As you profile your application’s storage needs, take a more granular approach to matching the strengths of a given storage service with the specific requirements of the various components of your application. DynamoDB, for example, might be a great fit for one application service, while RDS might be a better fit for another. If you use a microservice architecture for your solution, where each service has its own view of storage, think about which storage technology best fits each service’s profile. It’s not uncommon to find a spectrum of different storage solutions in use across the set of microservices that make up your application.

 This strategy also creates an opportunity to use storage as another way of tiering your SaaS solution. Each tier could essentially leverage a separate storage strategy, offering varying levels of performance and SLAs that would distinguish the value proposition of your solution’s tiers. By using this approach, you can better align the tenant tiers with the cost and load they are imposing on your infrastructure.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
