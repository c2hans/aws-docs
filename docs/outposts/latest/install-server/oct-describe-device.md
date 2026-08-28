---
source_url: https://docs.aws.amazon.com/outposts/latest/install-server/oct-describe-device.html
---

# describe-device
<a name="oct-describe-device"></a>

The **describe-device** command returns information about the Outposts server, including the protocol version, management device type, server type, asset ID, serial number, and manufacturer.

**Syntax**

```
Outpost>describe-device
```

**Parameters**
This command has no parameters.

**Example output: Success**

```
Outpost> describe-device
success: True
protocol: 0.1
management_device_type: {{management-device}}
server_type: {{server-type}}
server_asset_id: {{asset-id}}
server_serial_number: {{serial-number}}
server_manufacturer: {{manufacturer}}
checksum: {{checksum}}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Outposts. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query outposts` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
