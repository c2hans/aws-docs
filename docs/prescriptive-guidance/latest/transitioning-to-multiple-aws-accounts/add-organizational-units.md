---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/transitioning-to-multiple-aws-accounts/add-organizational-units.html
---

# Add organizational units
<a name="add-organizational-units"></a>

Establishing the proper organization structure is critical to setting up a multi-account environment. Because you use service control policies (SCPs) to define the maximum permissions for an OU and the accounts within it, your organization structure must be logical from a management, permissions, and financial reporting perspective. For more information about the structure of an organization, including organizational units (OUs), see [Terminology and concepts](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html) (AWS Organizations documentation).

In this section, you customize the landing zone by creating nested OUs that help you segment and structure your environments, such as production and non-production. These recommended best practices are designed to segment your landing zone to separate production and non-production resources and separate infrastructure from workloads.

For more information about how to create OUs, see [Managing organizational units](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_ous.html) (AWS Organizations documentation).

## Best practices
<a name="ou-best-practices"></a>
+ Within the **Workloads** OU that you created in [Create a landing zone](create-landing-zone.md), create the following nested OUs:
  + **Prod** – Use this OU for AWS accounts that store and access production data, including customer data.
  + **NonProd** – Use this OU for AWS accounts that store non-production data, such as development, staging, or testing environments

Under the organization root, create an **Infrastructure\_Prod** OU. Use this OU to host a centralized networking account.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
