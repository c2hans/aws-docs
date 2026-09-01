---
source_url: https://docs.aws.amazon.com/healthlake/latest/devguide/managing-data-stores.html
---

# Managing data stores with AWS HealthLake
<a name="managing-data-stores"></a>

With AWS HealthLake, you create and manage data stores for FHIR R4 resources. When you create a HealthLake data store, a FHIR data respository is made available via a RESTful API [endpoint](reference-healthlake-endpoints-quotas.md#reference-healthlake-endpoints). You can choose to import (preload) Synthea open source FHIR R4 health data into your data store when you create it. For more information, see [Preloaded data types](reference-healthlake-preloaded-data-types.md).

**Important**
HealthLake supports two types of FHIR data store authorization strategies, AWS SigV4 or SMART on FHIR. You must choose one of the authorization strategies prior to creating a HealthLake FHIR data store. For more information, see [Data store authorization strategy](getting-started-concepts.md#concept-data-store-authorization-strategy).

To find the FHIR-related capabilities (behaviors) of an active HealthLake data store, retrieve its [Capability Statement](reference-fhir-capability-statement.md).

The following topics describe how to use HealthLake cloud native actions to create, describe, list, update, tag, delete, and restore FHIR data stores using the AWS CLI, AWS SDKs, and AWS Management Console.

**Topics**
+ [Creating a data store](managing-data-stores-create.md)
+ [Getting data store properties](managing-data-stores-describe.md)
+ [Listing data stores](managing-data-stores-list.md)
+ [Updating a data store](managing-data-stores-update.md)
+ [Tagging data stores](managing-data-stores-tagging.md)
+ [Deleting a data store](managing-data-stores-delete.md)
+ [Restoring a data store](managing-data-stores-restore.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthLake. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query healthlake` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
