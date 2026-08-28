---
source_url: https://docs.aws.amazon.com/whitepapers/latest/multi-tenant-saas-storage-strategies/linked-account-silo-model.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Linked account silo model
<a name="linked-account-silo-model"></a>

 Before digging into specifics of each storage service, let’s look at how you can use AWS Linked Accounts to implement the silo model on top of any of the AWS storage solutions. To achieve a silo with this approach, your solution needs to provision a separate Linked Account for every tenant. This can truly achieve a silo because the entire infrastructure for a tenant is completely isolated from other tenants.

 The Linked Account approach relies on the Consolidated Billing feature that allows customers to associate child accounts with an overall payer account. The idea here is that—even with separate linked accounts for each tenant—the billing for these tenants is still aggregated and presented as part of a single bill to the payer account.

 The following figure shows a conceptual view of how Linked Accounts are used to implement the silo model. Here you have two tenants with separate accounts, each of which is associated with a payer account. With this flavor of isolation, you have the freedom to leverage any of the available AWS storage technologies to house your tenant’s data.

![A document depicting the silo model with linked accounts.](http://docs.aws.amazon.com/whitepapers/latest/multi-tenant-saas-storage-strategies/images/silo-model.png)

 At first blush, this can seem like a very appealing strategy for those SaaS providers that require a silo environment. It certainly can simplify some aspects of management and migration of individual tenants. Assembling a view of your tenant costs would also be more straightforward because you can summarize the AWS expenses at the Linked Account level.

 Even with these advantages, the Linked Account silo model has important limitations. Provisioning, for example, is certainly more complex. In addition to creating the tenant’s infrastructure, you need to automate the creation of each Linked Account and adjust any limits that need it. The larger challenge, however, is scale. AWS has constraints on the number of Linked Accounts you can create, and these limits aren’t likely to align with environments that will be creating a large number of new SaaS tenants.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
