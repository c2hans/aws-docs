---
source_url: https://docs.aws.amazon.com/appfabric/latest/adminguide/dynatrace.html
---

# Dynatrace
<a name="dynatrace"></a>

The Dynatrace® Platform combines broad and deep observability and continuous runtime application security with advanced AIOps to provide answers and intelligent automation from data. This enables innovators to modernize and automate cloud operations, deliver software faster and more securely, and ensure flawless digital experiences.

## AWS AppFabric audit log ingestion considerations
<a name="dynatrace-ingestion-considerations"></a>

The following sections describe the AppFabric output schema, output formats, and output destinations to use with the Dynatrace Platform.

### Schema and format
<a name="dynatrace-schema-format"></a>

The Dynatrace Platform supports the following AppFabric output schema and formats:
+ OCSF - JSON: AppFabric normalizes the data using the Open Cybersecurity Schema Framework (OCSF) and outputs the data in the JSON format.

### Output locations
<a name="dynatrace-output-locations"></a>

The Dynatrace Platform supports receiving Audit Logs from following AppFabric Output locations.
+ Amazon Simple Storage Service (Amazon S3)
  + To configure the Dynatrace Platform to receive data from the Amazon S3 bucket that contains your audit logs, follow the instructions in [Dynatrace’s S3 Log Forwarder project](https://github.com/dynatrace-oss/dynatrace-aws-s3-log-forwarder) on GitHub.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS AppFabric. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appfabric` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
