---
source_url: https://docs.aws.amazon.com/iot-mi/latest/devguide/control-task-publication.html
---

# Control task publication
<a name="control-task-publication"></a>

Use these methods to publish control-related requests to the managed integrations components.

```
iotmi_statusCode_t iotmi_control_publish_request(DataModel::iotmi_client_request_t request)
```

Publishes a control-related request to the managed integrations components. For example, unsolicited events, command requests, or device state queries.

**Parameters**
`request` (DataModel::iotmi\_client\_request\_t) - A pointer to a request structure containing the details.

**Returns**
+ `IOTMI_STATUS_OK` - The request was published successfully.
+ `IOTMI_STATUS_CUSTOM_PLUGIN_CLIENT_NOT_CONNECTED` - The DeviceSDKClient instance is not connected to managed integrations.
+ `IOTMI_STATUS_INVALID_PARAMETER` - One or more parameters in the request are invalid.
+ `IOTMI_STATUS_INVALID_JSON_OBJECT` - The request payload is not a valid JSON object.
+ `IOTMI_STATUS_NO_MEMORY` - A memory allocation error occurred.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Managed integrations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-mi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
