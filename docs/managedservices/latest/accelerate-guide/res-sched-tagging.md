---
source_url: https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/res-sched-tagging.html
---

# Tagging resources for AMS Resource Scheduler
<a name="res-sched-tagging"></a>

Tagging resources for AMS Resource Scheduler.

Once you add schedules and periods to AMS Resource Schedule, you need to tag your resources with the Resource Scheduler tag name as the tag key, or the your customized one, and the schedule name as the tag value. For details on how to tag your resources in your AMS Accelerate account, see [Tagging in AMS Accelerate](acc-tagging.md).

**Note**
If Resource Tagger is used to tag the resources, the default Tag key for Resource Scheduler must be customized to have the prefix '`ams:rt:`' as all tags applied by the resource tagger have the key prefix '`ams:rt:`'. Otherwise, the resources tagged with resource tagger will not be managed by Resource Scheduler. To know more about customizing the default Tag key for Resource Scheduler, see [Customizing AMS Resource Scheduler](res-sched-customizing.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Services. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managedservices` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
