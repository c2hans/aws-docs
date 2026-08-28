---
source_url: https://docs.aws.amazon.com/codeartifact/latest/ug/domains.html
---

# Working with domains in CodeArtifact
<a name="domains"></a>

CodeArtifact *domains* make it easier to manage multiple repositories across an organization. You can use a domain to apply permissions across many repositories owned by different AWS accounts. An asset is stored only once in a domain, even if it's available from multiple repositories.

Although you can have multiple domains, we recommend a single production domain that contains all published artifacts so that your development teams can find and share packages. You can use a second preproduction domain to test changes to the production domain configuration.

These topics describe how to use the CodeArtifact console, the AWS CLI, and CloudFormation to create or configure CodeArtifact domains.

**Topics**
+ [Domain overview](domain-overview.md)
+ [Create a domain](domain-create.md)
+ [Delete a domain](delete-domain.md)
+ [Domain policies](domain-policies.md)
+ [Tag a domain](tag-domains.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeArtifact. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codeartifact` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
