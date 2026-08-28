---
source_url: https://docs.aws.amazon.com/iot-mi/latest/devguide/client-initialization.html
---

# Client initialization
<a name="client-initialization"></a>

To start using the `DeviceSDKClient`, initialize it with a client ID.

```
iotmi_statusCode_t DeviceSDKClient(const std::string& clientId)
```

This creates a new `DeviceSDKClient` instance with the specified `clientId`. The `clientId` must match the one you register with managed integrations.

**Parameters**
`clientId` (string) - The client ID for this instance.

```
connect()
```

Connects the `DeviceSDKClient` instance to managed integrations.

**Returns**
+ `IOTMI_STATUS_OK` - The connection was successful.
+ `IOTMI_STATUS_CUSTOM_PLUGIN_CONNECTION_ERROR` - An error occurred while connecting to managed integrations.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Managed integrations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-mi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
