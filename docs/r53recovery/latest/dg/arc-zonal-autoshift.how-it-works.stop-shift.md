---
source_url: https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-autoshift.how-it-works.stop-shift.html
---

# Stopping an active autoshift or practice run for a resource
<a name="arc-zonal-autoshift.how-it-works.stop-shift"></a>

To stop an in-progress autoshift for a resource you must cancel the zonal shift.

Regular practice runs still take place for the resource, on the same schedule. If you want to stop practice runs in addition to disabling autoshifts, you must delete the practice run configuration associated with the resource.

When you delete a practice run configuration, AWS stops performing practice runs that shift traffic for the resource away from an Availability Zone each week. In addition, because zonal autoshift requires practice runs, when you delete a practice run configuration using the ARC console, this action also disables zonal autoshift for the resource. However, note that if you use the zonal autoshift API to delete a practice run, you must first disable zonal autoshift for the resource.

For more information, see [Canceling a zonal autoshift](arc-zonal-autoshift.canceling-an-autoshift.md) and [Enabling and working with zonal autoshift](arc-zonal-autoshift.start-cancel.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Application Recovery Controller. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query r53recovery` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
