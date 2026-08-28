---
source_url: https://docs.aws.amazon.com/r53recovery/latest/dg/actions.zonalshift.html
---

# Zonal shift API operations
<a name="actions.zonalshift"></a>

The following table lists ARC API operations that you can use using zonal shift, which moves traffic away from an Availability Zone for multi-AZ applications. The table also includes links to relevant documentation.

For examples of how to use common zonal shift API operations with the AWS Command Line Interface, see [Examples of using the AWS CLI with zonal shift](getting-started-cli-zonalshift.md).

| Action | Using the ARC console | Using the ARC API |
| --- | --- | --- |
| Start a zonal shift | See [Starting a zonal shift](arc-zonal-shift.start-cancel.md#arc-zonal-shift.start) | See [StartZonalShift](https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_StartZonalShift.html) |
| Update a zonal shift | See [Updating or canceling a zonal shift](arc-zonal-shift.start-cancel.md#arc-zonal-shift.update-cancel) | See [UpdateZonalShift](https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_UpdateZonalShift.html) |
| List zonal shifts | See [Zonal shift in ARC](arc-zonal-shift.md) | See [ListZonalShifts](https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_ListZonalShifts.html) |
| List managed resources | See [Supported resources](arc-zonal-shift.resource-types.md) | See [ListManagedResources](https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_ListManagedResources.html) |
| Get managed resource | See [Supported resources](arc-zonal-shift.resource-types.md) | See [GetManagedResource](https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_GetManagedResource.html) |
| Cancel a zonal shift | See [Updating or canceling a zonal shift](arc-zonal-shift.start-cancel.md#arc-zonal-shift.update-cancel) | See [CancelZonalShift](https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_CancelZonalShift.html) |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Application Recovery Controller. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query r53recovery` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
