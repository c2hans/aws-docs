---
source_url: https://docs.aws.amazon.com/snowball/latest/developer-guide/identifying-device.html
---

AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/) for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/) for secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/).

# How to identify a Snowball Edge
<a name="identifying-device"></a>

Use the `describe-device` command to find the device type, then look up the returned value of `DeviceType` in the table below to determine the configuration.

```
  snowballEdge describe-device
```

**Example of `describe-device` output**

```
  {
  "DeviceId" : "JID-206843500001-35-92-20-211-23-06-02-18-24",
  "UnlockStatus" : {
    "State" : "UNLOCKED"
  ...
  "DeviceType" : "V3_5C"
}
```

**`DeviceType` and Snowball Edge device configurations**

| `DeviceType` value | Device configuration |
| --- | --- |
| V3\_5C | Snowball Edge compute-optimized with AMD EPYC Gen2 and NVME |
| V3\_5S | Snowball Edge storage-optimized 210 TB |

For more information about Snowball Edge device configurations, see [AWS Snowball Edge device hardware information](device-differences.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Snowball Edge. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query snowball` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
