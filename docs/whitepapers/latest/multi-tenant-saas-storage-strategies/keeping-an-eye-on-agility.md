---
source_url: https://docs.aws.amazon.com/whitepapers/latest/multi-tenant-saas-storage-strategies/keeping-an-eye-on-agility.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Keeping an eye on agility
<a name="keeping-an-eye-on-agility"></a>

 The matrix of multitenant storage options can be daunting. It can be challenging to identify the solution that represents the best mix of flexibility, isolation, and manageability. Although it’s important to consider all the options, it’s also essential to continually factor agility into your multitenant storage thinking. The success of SaaS organizations is often heavily influenced by the amount of agility that is baked into their solution.

 The storage technology and isolation model you select directly impacts your ability to easily deploy new features and functionality. The shape of your structure and content of your data often change to support new features, and this means your underlying storage model must accommodate these changes without requiring downtime. Each isolation model has pros and cons when it comes to supporting this seamless migration. As you consider your options, give these factors the appropriate weight.

 While the silo, bridge, and pool models all have an agility footprint, you can apply common tenets to help you remain as nimble as possible. A key tenet is the rather obvious but occasionally violated need to minimize one-off variations for tenant data. The silo and bridge models, for example, can lead to storage variations that can complicate your ability to push out new features to all of your SaaS customers as part of a single automated event. Teams often use automation and continuous deployment to limit the amount of friction introduced by their multitenant storage strategy.

 As you settle into a storage strategy, expect and embrace the reality that your storage requirements continually evolve. The needs of SaaS customers are a moving target, and the storage model you pick today might not be a good fit tomorrow. AWS also continues to introduce new features and services that can represent new opportunities to enhance your approach to storage.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
