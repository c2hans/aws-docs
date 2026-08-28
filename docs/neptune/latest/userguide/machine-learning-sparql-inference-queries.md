---
source_url: https://docs.aws.amazon.com/neptune/latest/userguide/machine-learning-sparql-inference-queries.html
---

# SPARQL inference queries in Neptune ML
<a name="machine-learning-sparql-inference-queries"></a>

Neptune ML maps the RDF graph into a property graph to model the ML Task. Currently, it supports the following use-cases:
+ **Object classification**   –   Predicts the categorical feature of an object.
+ **Object regression**   –   Predicts a numerical property of an object.
+ **Object prediction**   –   Predicts an object given a subject and a relationship.
+ **Subject prediction**   –   Predicts a subject given an object and a relationship.

**Note**
Neptune ML does not support subject classification and regression use cases with SPARQL.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Neptune. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
