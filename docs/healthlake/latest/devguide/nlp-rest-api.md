---
source_url: https://docs.aws.amazon.com/healthlake/latest/devguide/nlp-rest-api.html
---

# Using FHIR REST API interactions
<a name="nlp-rest-api"></a>

By default, traits detected by the Amazon Comprehend Medical API operations are not returned when making a `GET` request. To see the results of the integrated NLP operations, you must specify a known `ID` for the following FHIR resource types.
+ `Linkage`
+ `Observation`
+ `Condition`
+ `MedicationStatement`

The results of HealthLake integrated NLP actions outside the `DocumentReference` resource type are available using a `GET` request where the specified `ID` is know to contain results from the Amazon Comprehend Medical API operations.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthLake. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query healthlake` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
