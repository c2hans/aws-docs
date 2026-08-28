---
source_url: https://docs.aws.amazon.com/clouddirectory/latest/APIReference/arns.html
---

Amazon Cloud Directory is no longer open to new customers, and will reach end of support on July 24, 2027. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) and [Amazon Neptune](https://aws.amazon.com/neptune/). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/).

# Arn Examples
<a name="arns"></a>

The following examples are separated by ARN types and show how they can be constructed for each schema state (where applicable). A schema can exist in three states:
+ *Development:* This is a mutable state of the schema. All new schemas are in the development state. Once the schema is finalized, it can be published. All development schemas are under the development sub root of the schema metadata container.
+ *Published:* Published schemas are immutable and have a version associated with them. All published schemas are under the published sub root of the schema container.
+ *Applied:* Applied schemas are mutable in a way that allows you to add new schema facets. However, existing schema facets cannot be changed. You can apply only published schemas to directories. You can't apply schemas at the node level, but only at the directory root level.

## Schema Arns
<a name="schemaarns"></a>

- **Development**
  - **Format or Example:** Format / **Schema Arn:** arn:aws:clouddirectory:us-west-2:{{accountId}}:schema/development/{{SchemaName}}
  - **Format or Example:** Example / **Schema Arn:** arn:aws:clouddirectory:us-west-2:12345678910:schema/development/cognito

- **Published**
  - **Format or Example:** Format / **Schema Arn:** arn:aws:clouddirectory:us-west-2:{{accountId}}:schema/published/{{SchemaName}}/{{SchemaVersion}}
  - **Format or Example:** Example / **Schema Arn:**  arn:aws:clouddirectory:us-west-2:12345678910:schema/published/cognito/1.0
  - **Format or Example:** Format / **Schema Arn:** arn:aws:clouddirectory:us-west-2:{{accountId}}:schema/published/{{SchemaName}}/{{SchemaVersion}}/{{SchemaMinorVersion}}
  - **Format or Example:** Example / **Schema Arn:**  arn:aws:clouddirectory:us-west-2:12345678910:schema/published/cognito/1.0/XYZ

- **Applied**
  - **Format or Example:** Format / **Schema Arn:** arn:aws:clouddirectory:us-west-2:{{accountId}}:directory/{{directoryId}}/{{SchemaName}}/{{SchemaVersion}}
  - **Format or Example:** Example / **Schema Arn:** arn:aws:clouddirectory:us-west-2:12345678910:directory/ARIqk1HD-UjdtmcIrJHEvPI/schema/cognito/1.0
  - **Format or Example:** Format / **Schema Arn:** arn:aws:clouddirectory:us-west-2:{{accountId}}:directory/{{directoryId}}/{{SchemaName}}/{{SchemaVersion}}/{{SchemaMinorVersion}}
  - **Format or Example:** Example / **Schema Arn:**  arn:aws:clouddirectory:us-west-2:12345678910:directory/ARIqk1HD-UjdtmcIrJHEvPI/schema/cognito/1.0/XYZ

## Directory Arns
<a name="directoryarns"></a>

- **Directory Arn**
  - **Format or example:** Format / **Arn:** arn:aws:clouddirectory:us-west-2:{{Directory owner accountId}}:directory/{{directoryId}}
  - **Format or example:** Example / **Arn:** arn:aws:clouddirectory:us-west-2:12345678910:directory/ARIqk1HD-UjdtmcIrJHEvPI

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cloud Directory. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clouddirectory` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
