---
source_url: https://docs.aws.amazon.com/appfabric/latest/adminguide/singularity-cloud-security.html
---

# Singularity Cloud
<a name="singularity-cloud-security"></a>

The Singularity Cloud platform protects your enterprise from threats of all categories, at all stages. Its patented AI (Artificial Intelligence) extends security from known signatures and patterns to the most sophisticated attacks, such as zero-day and ransomware.

## AWS AppFabric audit log ingestion considerations
<a name="singularity-cloud-security-ingestion-considerations"></a>

The following sections describe the AppFabric output schema, output formats, and output destinations to use with Singularity Cloud.

### Schema and format
<a name="singularity-cloud-security-schema-format"></a>

Singularity Cloud supports the following AppFabric output schema and formats:

OCSF - JSON: AppFabric normalizes the data using the Open Cybersecurity Schema Framework (OCSF) and outputs the data in the JSON format.

### Output locations
<a name="singularity-cloud-security-output-locations"></a>

Singularity Cloud supports receiving Audit Logs from following AppFabric Output locations.
+ Amazon Simple Storage Service (Amazon S3)
  + To configure Singularity Cloud to receive data from the Amazon S3 bucket that contains your audit logs, follow the instructions in Singularity Cloud’s documentation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS AppFabric. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appfabric` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
