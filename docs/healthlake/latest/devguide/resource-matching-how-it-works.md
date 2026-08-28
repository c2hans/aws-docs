---
source_url: https://docs.aws.amazon.com/healthlake/latest/devguide/resource-matching-how-it-works.html
---

# How resource matching works
<a name="resource-matching-how-it-works"></a>

Whenever a resource is written to your data store – through a bulk import job or a REST API `create`, `update` or `delete`, resource matching evaluates its `identifier` values against the other resources of the same type in the data store. Matching is deterministic: two resources are linked when they share a high-confidence healthcare identifier, and each identifier is matched according to its real-world scope.
+ **Globally unique identifiers** – an identifier such as a National Provider Identifier (NPI) or Social Security Number (SSN) refers to the same entity regardless of which system issued the record. These are matched on value.
+ **Scoped identifiers** – an identifier such as a medical record number (MRN), driver's license, or device serial number is only unique within a namespace (a hospital, a state, a manufacturer). These are matched on the combination of the identifying system and value, so that MRN `456` at one hospital is never linked to MRN `456` at another.

Resource matching also recognizes when the same identifier is represented under different system URIs. For example, an SSN under `http://hl7.org/fhir/sid/us-ssn` and under `urn:oid:2.16.840.1.113883.4.1` are treated as the same identifier, so resources from sources that use different URI conventions still match.

Resource matching does not apply priority ordering or conflict resolution between identifiers: any shared, non-placeholder identifier is enough to link two resources. Because matching is non-destructive, you review the resulting links and decide how to act on them.

**Note**
Resource matching evaluates resources of the same type against one another (for example, `Patient` to `Patient`). It does not link resources of different types.

**Note**
A resource sharing an identifier with more than 100 other resources may not be matched against all of them.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthLake. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query healthlake` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
