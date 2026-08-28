---
source_url: https://docs.aws.amazon.com/healthlake/latest/devguide/integrating.html
---

# Integrating AWS HealthLake
<a name="integrating"></a>

The following AWS services integrate directly with AWS HealthLake to enable integrated natural language processing, SQL query, and data warehousing.
+ *Amazon Comprehend Medical* is a HIPAA eligible natural language processing service (NLP) that uses machine learning libraries to extract meaningful health data from unstructured medical text in HealthLake. For more information, see the [*Amazon Comprehend Medical Developer Guide*](https://docs.aws.amazon.com/comprehend-medical/latest/dev/comprehendmedical-welcome.html).
+ *Amazon Athena* is an interactive query service that enables you analyze HealthLake data directly in Amazon Simple Storage Service (Amazon S3) buckets using standard SQL. For more information, see the [*Amazon Athena Developer Guide*](https://docs.aws.amazon.com/athena/latest/ug/what-is.html).

**Topics**
+ [Natural language processing](integrating-nlp.md)
+ [SQL index and query](integrating-athena.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthLake. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query healthlake` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
