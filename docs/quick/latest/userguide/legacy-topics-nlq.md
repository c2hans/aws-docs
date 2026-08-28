---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/legacy-topics-nlq.html
---

# Making legacy Topics natural-language-friendly
<a name="legacy-topics-nlq"></a>

To improve the accuracy of answers in a legacy Topic, configure the following metadata:

1. **Dataset names and descriptions** — Give datasets friendly names so readers can identify them.

1. **Date fields** — Specify default dates and time basis for each dataset.

1. **Exclude unused fields** — Remove irrelevant fields from the Topic to improve accuracy.

1. **Rename fields** — Give fields user-friendly names and descriptions.

1. **Synonyms** — Add alternative names that readers might use to refer to fields or values.

1. **Semantic types** — Specify the type of information in each field (location, currency, date, person, etc.).

1. **Field roles and aggregations** — Specify whether fields are dimensions or measures, and set default aggregations.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quick` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
