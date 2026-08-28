---
source_url: https://docs.aws.amazon.com/kendra/latest/dg/index-synonyms-enabling-synonyms-in-results.html
---

Amazon Kendra is no longer open to new customers. For capabilities similar to Amazon Kendra, explore Amazon Bedrock Knowledge Bases. [Learn more](https://docs.aws.amazon.com/kendra/latest/dg/kendra-availability-change.html).

# Highlights in search results
<a name="index-synonyms-enabling-synonyms-in-results"></a>

Synonym highlighting is on by default. Highlight information is included in Amazon Kendra SDK and CLI query results. If you interact with Amazon Kendra using the SDK or CLI, you determine how to display results.

Synonym highlights will have the highlight type `THESAURUS_SYNONYM`. For more information about highlights, see the [Highlight](https://docs.aws.amazon.com/kendra/latest/APIReference/API_Highlight.html) object.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kendra. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kendra` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
