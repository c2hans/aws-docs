---
source_url: https://docs.aws.amazon.com/controltower/latest/userguide/lz-api-decommission.html
---

# Decommission your landing zone with APIs
<a name="lz-api-decommission"></a>

The process of cleaning up all of a landing zones resources is referred to as *decommissioning* a landing zone.

**Important**
We strongly recommend that you perform this decommissioning process only if you intend to stop using your landing zone. It is not possible to re-create your existing landing zone after you've decommissioned it.

For more details about decommissioning a landing zone, including important information about how AWS Control Tower handles your data and existing AWS Organizations, review [Decommission an AWS Control Tower landing zone](decommission-landing-zone.md).

To decommission a landing zone, call `DeleteLandingZone` API. This API returns an `OperationIdentifier`, which you can then use when calling the `GetLandingZoneOperation` API to check the delete operation's status.

```
 aws controltower delete-landing-zone --landing-zone-identifier "arn:aws:controltower:us-west-2:123456789012:landingzone/1A2B3C4D5E6F7G8H"
```

**Output**:

```
{
   "operationIdentifier": "55XXXXXX-e2XX-41XX-a7XX-446XXXXXXXXX"
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Control Tower. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query controltower` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
