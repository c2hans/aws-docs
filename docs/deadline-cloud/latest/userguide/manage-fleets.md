---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/userguide/manage-fleets.html
---

# Deadline Cloud fleets
<a name="manage-fleets"></a>

This section explains how to manage service-managed fleets and customer-managed fleets (CMF) for Deadline Cloud.

You can set up two types of Deadline Cloud fleets:
+ Service-managed fleets are fleets of workers that have default settings provided by Deadline Cloud. These default settings are designed to be efficient and cost effective.
+ Customer-managed fleets (CMFs) provide you with full control over your processing pipeline. A CMF can reside within AWS infrastructure, on premises, or in a co-located data center. CMFs include provisioning, operations, management, and decommissioning workers in the fleet.

When you associate a fleet with multiple queues, it divides its workers evenly among those queues.

For more information about choosing between the two fleet types, see [Choose between service-managed and customer-managed fleets](fleet-types.md).

**Topics**
+ [Choose between service-managed and customer-managed fleets](fleet-types.md)
+ [Service-managed fleets](smf-manage.md)
+ [Customer-managed fleets](manage-cmf.md)
+ [Auto scaling configuration](auto-scaling-configuration.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
