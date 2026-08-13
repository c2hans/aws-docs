---
source_url: https://docs.aws.amazon.com/greengrass/v1/developerguide/iot-analytics-connector.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# IoT Analytics connector (discontinued)
<a name="iot-analytics-connector"></a>

**Warning**  <a name="connectors-extended-life-phase-warning"></a>
This connector has moved into the *extended life phase*, and AWS IoT Greengrass won't release updates that provide features, enhancements to existing features, security patches, or bug fixes. For more information, see [AWS IoT Greengrass Version 1 maintenance policy](maintenance-policy.md).

**AWS IoT Analytics discontinued**
AWS IoT Analytics was discontinued on December 15, 2025. The IoT Analytics connector no longer functions. If you have this connector configured in your Greengrass group, remove it to avoid errors.

The IoT Analytics connector previously sent local device data to AWS IoT Analytics channels. Because AWS IoT Analytics has been discontinued, this connector can no longer deliver data. All AWS IoT Analytics API calls now return an `AccessDeniedException`.

To remove this connector from your Greengrass group, use the AWS IoT console or the AWS IoT Greengrass API to delete the connector from your group's connector definition, then deploy the group.
