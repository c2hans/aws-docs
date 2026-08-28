---
source_url: https://docs.aws.amazon.com/healthlake/latest/devguide/exporting-fhir-data.html
---

# Exporting FHIR data with AWS HealthLake
<a name="exporting-fhir-data"></a>

Use native AWS HealthLake actions to start, describe, and list FHIR export jobs. You can queue export jobs. The asynchronous export jobs are processed in a FIFO (First In First Out) manner. You can queue jobs the same way you start export jobs. If one is in progress, it will simply queue up. You can create, read, update, or delete FHIR resources while an export job is in progress.

**Note**
You can also export FHIR data from a HealthLake data store using the FHIR R4 `$export` operation. For more information, see [Exporting HealthLake data with FHIR `$export`](reference-fhir-operations-export.md).

**Topics**
+ [Starting an export job](exporting-fhir-data-start.md)
+ [Getting export job properties](exporting-fhir-data-describe.md)
+ [Listing export jobs](exporting-fhir-data-list.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthLake. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query healthlake` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
