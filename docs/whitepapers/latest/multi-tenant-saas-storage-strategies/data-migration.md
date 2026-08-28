---
source_url: https://docs.aws.amazon.com/whitepapers/latest/multi-tenant-saas-storage-strategies/data-migration.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Data migration
<a name="data-migration"></a>

 Data migration is one of those areas that is often left out of the evaluation of competing SaaS storage models. However, with SaaS, consider how your architectural choices will influence your ability to continually deploy new features and capabilities. Although performance and general tenant experience are important to emphasize, it’s also essential to consider how your storage solution will accommodate ongoing changes in the underlying representation of your data.

## Migration and multitenancy
<a name="migration-and-multitenancy"></a>

 Each of the multitenant storage models requires its own unique approach to tackling data migration. In the silo and bridge models, you can migrate data on a tenant-by-tenant basis. Your organization may find this appealing because it allows you to carefully migrate each SaaS tenant without exposing all tenants to the possibility of a migration error. However, this approach can introduce more complexity into the overall orchestration of your deployment lifecycle.

 Migrating data in the pool model can be both appealing and challenging. In one respect, migration in a pool model provides a single point that, once migrated, has all tenants successfully transitioned to your new data model. On the other hand, any problem introduced during a pool migration could impact all of your tenants.

 From the outset, you should be thinking about how data migration fits into your overall multitenant SaaS strategy. If you bake this migration orchestration into your delivery pipeline early, you tend to achieve a greater degree of agility in your release process.

## Minimizing invasive changes
<a name="minimizing-invasive-changes"></a>

 As a rule of thumb, you should have clear policies and tenets to follow as you consider how the data in your systems will evolve. Wherever possible, teams should favor data changes that have backward compatibility with earlier versions. If you can find ways to minimize changes to your application’s data representation, you will limit the high overhead of transforming your data into a new representation.

 You can leverage commonly used tools and techniques to orchestrate the migration process. In reality, while minimizing invasive changes is often of great importance to SaaS developers, it’s not unique to the SaaS domain. As such, it’s beyond the scope of what we’ll cover in this paper.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
