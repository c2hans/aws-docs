---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/next-gen-api-dependency-discovery-config-structure.html
---

# DependencyDiscoveryConfig structure
<a name="next-gen-api-dependency-discovery-config-structure"></a>

```
{
  "status": "INITIALIZING | ENABLED | DISABLED",
  "updatedAt": "timestamp",
  "eligibleResourceCount": integer,
  "message": "string"
}
```

The following table describes the fields in the `DependencyDiscoveryConfig` structure.

| Field | Required | Description |
| --- | --- | --- |
| status | Yes | The current state of dependency discovery. Valid values: INITIALIZING (discovery is running), ENABLED (discovery is complete and active), or DISABLED (discovery is turned off). |
| updatedAt | No | The timestamp when the dependency discovery status was last updated. |
| eligibleResourceCount | No | The number of compute resources eligible for dependency discovery. Returns null until the resource discovery process completes its first run. |
| message | No | A message describing the current state of discovery. Returns null when discovery is complete and dependencies are available. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
