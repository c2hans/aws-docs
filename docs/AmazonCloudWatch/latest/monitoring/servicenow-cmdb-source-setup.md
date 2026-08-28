---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/servicenow-cmdb-source-setup.html
---

# Source configuration for ServiceNow CMDB Audit Log
<a name="servicenow-cmdb-source-setup"></a>

## Integrating with ServiceNow CMDB
<a name="servicenow-cmdb-integration"></a>

ServiceNow is an enterprise platform that provides IT service management (ITSM) and configuration management database (CMDB) capabilities for tracking and managing IT assets, configurations, and changes across organizations. CloudWatch Pipeline uses the ServiceNow Table API to retrieve information about sys\_audit, syslog, sysevent, and syslog\_transactions from your ServiceNow instance.

## Authenticating with ServiceNow CMDB
<a name="servicenow-cmdb-authentication"></a>

To read the logs, the pipeline needs to authenticate with your ServiceNow instance. The ServiceNow Table API supports OAuth 2.0.
+ Make sure the REST API is enabled on your ServiceNow instance.
+ Enable OAuth 2.0 Client Credentials grant type in your ServiceNow instance
+ Create an OAuth Application Registry for external client authentication
+ In the AWS Secrets Manager, create a secret and store the Application (client) ID under the key `client_id` and the client secret under the key `client_secret`.
+ Configure OAuth Application User and assign required roles

## Configuring the CloudWatch Pipeline
<a name="servicenow-cmdb-pipeline-config"></a>

When configuring the pipeline to read audit logs from ServiceNow choose ServiceNow CMDB as the data source. Fill in the required information like `instance_url` and the secret where `client_id` and `client_secret` are stored. After you create the pipeline, data will be available in the selected CloudWatch Logs log group.

## Supported Open Cybersecurity Schema Framework Event Classes
<a name="servicenow-cmdb-ocsf-events"></a>

This integration supports OCSF schema version v1.5.0 and events that map to Entity Management (3004), API Activity (6003), and Datastore Activity (6005). These events are from specific tables and filtered for CMDB reference.

**Entity Management** contains events from following tables:
+ sys\_audit

**API Activity** contains events from following tables:
+ sysevent
+ syslog

**Datastore Activity** contains events from following tables:
+ syslog\_transactions

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
