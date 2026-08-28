---
source_url: https://docs.aws.amazon.com/msk/latest/developerguide/msk-tagging-basics.html
---

# Tag basics for Amazon MSK clusters
<a name="msk-tagging-basics"></a>

You can use the Amazon MSK API to complete the following tasks:
+ Add tags to an Amazon MSK resource.
+ List the tags for an Amazon MSK resource.
+ Remove tags from an Amazon MSK resource.

You can use tags to categorize your Amazon MSK resources. For example, you can categorize your Amazon MSK clusters by purpose, owner, or environment. Because you define the key and value for each tag, you can create a custom set of categories to meet your specific needs. For example, you might define a set of tags that help you track clusters by owner and associated application.

The following are several examples of tags:
+ `Project: {{Project name}}`
+ `Owner: {{Name}}`
+ `Purpose: Load testing`
+ `Environment: Production`

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Streaming for Apache Kafka. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query msk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
