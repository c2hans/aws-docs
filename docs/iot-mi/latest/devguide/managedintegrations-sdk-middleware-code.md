---
source_url: https://docs.aws.amazon.com/iot-mi/latest/devguide/managedintegrations-sdk-middleware-code.html
---

# Protocol-specific middleware code organization
<a name="managedintegrations-sdk-middleware-code"></a>

This section contains information about the location of the code for each component inside the `IotManagedIntegrationsDeviceSDK-Middleware` repository. The following is an example of the folder structure in this repository.

```
./IotManagedIntegrationsDeviceSDK-Middleware
|— greengrass
|— {{example}}-iot-ace-dpk
|— {{example}}-iot-ace-general
|— {{example}}-iot-ace-project
|— {{example}}-iot-ace-z3-gateway
|— {{example}}-iot-ace-zware
|— {{example}}-iot-ace-zwave-mw
```

**Topics**
+ [Zigbee middleware code organization](managedintegrations-sdk-middleware-zigbee.md)
+ [Z-Wave middleware code organization](managedintegrations-sdk-middleware-zwave.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Managed integrations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-mi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
