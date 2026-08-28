---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/mainframe-decomposition-aws-transform/migration-waves.html
---

# Planning migration waves
<a name="migration-waves"></a>

After decomposition is complete, AWS Transform creates a draft wave plan (with table and chart view) for the domains. The following screen illustration shows the table view.

![Table view of domain waves in AWS Transform.](http://docs.aws.amazon.com/prescriptive-guidance/latest/mainframe-decomposition-aws-transform/images/guide-img/b2468f31-0c9f-4fc4-9a0f-816b3ed5739c/images/37c7af14-a0cc-49b0-81cc-8df15954c866.png)

Choose each domain to add a wave preference for it, and then choose **Save**. You can then choose **Add and regenerate** to create new wave plans based on your changes. In the following screen illustration, the Card Demo Batch Processing domain has been assigned to wave 4.

![Assigning a wave preference to domains in AWS Transform.](http://docs.aws.amazon.com/prescriptive-guidance/latest/mainframe-decomposition-aws-transform/images/guide-img/b2468f31-0c9f-4fc4-9a0f-816b3ed5739c/images/000093eb-09b9-4525-8c86-4d8a6e49c2ee.png)

When you're ready to finalize your domain preferences, choose **Send to AWS Transform**. AWS Transform incorporates the preferred plan into its recommendations. The revised plan is based on the preferred wave plan and additional considerations, such as dependencies between components.

You can now refactor your code for each phase of the migration by using the finalized wave plans.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
