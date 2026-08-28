---
source_url: https://docs.aws.amazon.com/clouddirectory/latest/developerguide/key_concepts_schema.html
---

Amazon Cloud Directory is no longer open to new customers, and will reach end of support on July 24, 2027. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) and [Amazon Neptune](https://aws.amazon.com/neptune/). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/).

# Schema
<a name="key_concepts_schema"></a>

A schema is a collection of facets that define what objects can be created in a directory and how they are organized. A schema also enforces data integrity and interoperability. A single schema can be applied to more than one directory at a time. For more information, see [Schemas](schemas.md).

## Facets
<a name="key_concepts_facets"></a>

A facet is a collection of attributes, constraints, and links defined within a schema. Combined together, facets define the objects in a directory. For example, Person and Device can be facets to define corporate employees with association of multiple devices. For more information, see [Facets](schemas_whatarefacets.md).

## Managed Schemas
<a name="key_concepts_sampleschemas"></a>

A schema provided to make it easier to quickly develop and maintain your applications. For more information, see [Managed Schema](schemas_managed.md).

## Sample Schemas
<a name="key_concepts_sampleschemas"></a>

The set of sample schemas provided by default in the Directory Service console. For example, Person, Organization, and Device are all sample schemas. For more information, see [Sample Schemas](schemas_sampleschemastopic.md).

## Custom Schemas
<a name="key_concepts_customschemas"></a>

One or more schemas defined by a user that can be uploaded from the Schemas section or during the Cloud Directory creation process of the Directory Service console, or created by API calls.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cloud Directory. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clouddirectory` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
