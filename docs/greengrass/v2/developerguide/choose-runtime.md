---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/choose-runtime.html
---

# Choose your runtime (Greengrass nucleus or Greengrass nucleus lite)
<a name="choose-runtime"></a>

Choosing between Greengrass nucleus and Greengrass nucleus lite depends on your device resources and the features your Lambda functions use. Review the event source compatibility matrix in the following table, then use the decision flow diagram to determine which runtime is appropriate for your migration. For a detailed comparison of Greengrass nucleus and Greengrass nucleus lite features, see [Choosing your runtime](choosing-your-runtime.md).

## Event source compatibility matrix
<a name="event-source-compatibility"></a>

In AWS IoT Greengrass V1, Lambda functions can communicate with five types of event sources: other Lambda functions, AWS IoT Core, local shadow service, client devices, and connectors. The following table shows which of these event sources are supported in each V2 runtime.

Note: Event source names use AWS IoT Greengrass V1 terminology. When migrating to V2, Lambda functions are converted to either Lambda components (supported only in Greengrass nucleus) or generic components (supported in both Greengrass nucleus and Greengrass nucleus lite).

| Event Source | Greengrass nucleus | Greengrass nucleus lite |
| --- | --- | --- |
| Other Lambda functions in the group | ✓ (Lambda components and generic components) | ✓ (Generic components only) |
| AWS IoT Core service | ✓ | ✓ |
| Local shadow service | ✓ | ✗ |
| Client device | ✓ | ✗ |
| Connector | ✓ | ✗ |

## Runtime selection decision flow
<a name="runtime-selection-decision-flow"></a>

![Decision flow diagram for choosing between Greengrass nucleus and Greengrass nucleus lite.](http://docs.aws.amazon.com/greengrass/v2/developerguide/images/runtime-selection-decision-flow.png)

### Notes
<a name="runtime-selection-notes"></a>

1. For Greengrass nucleus lite requirements and compatibility details, see [Greengrass nucleus lite](greengrass-nucleus-lite-component.md). Greengrass nucleus lite requires a minimum of 5 MB RAM and is designed for resource-constrained devices.

1. The decision flow provides guidance based on typical use cases, but is not a strict requirement. Customers with both resource-constrained and resource-sufficient devices may choose to use a single runtime across all devices for operational simplicity, even if some devices could support either runtime.

## Next steps
<a name="next-steps-runtime"></a>

After choosing your runtime, proceed to set up your test device:
+ For Greengrass nucleus runtime: [Set up a new device to test V1 applications on V2](set-up-v2-test-device.md)
+ For Greengrass nucleus lite runtime: [Set up a new device with Greengrass nucleus lite](set-up-v2-test-device-lite.md)
