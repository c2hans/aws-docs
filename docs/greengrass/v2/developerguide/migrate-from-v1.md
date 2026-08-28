---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html
---

# Migrate from AWS IoT Greengrass Version 1
<a name="migrate-from-v1"></a>

AWS IoT Greengrass Version 2 is a major version release of the AWS IoT Greengrass Core software, APIs, and console. AWS IoT Greengrass V2 introduces several improvements to AWS IoT Greengrass V1, such as modular applications, deployments to large fleets of devices, and support for additional platforms.

**Note**
End of support notice: On October 7, 2026, AWS will end support for AWS IoT Greengrass Version 1. After October 7, 2026, you will no longer be able to access the AWS IoT Greengrass V1 console or AWS IoT Greengrass V1 resources.

Follow instructions in this guide to migrate from AWS IoT Greengrass V1 to AWS IoT Greengrass V2.

## Migration overview
<a name="migration-overview"></a>

At a high level, you can use the following procedure to upgrade core devices from AWS IoT Greengrass V1 to AWS IoT Greengrass V2.

Before migrating, you'll choose between two runtime options:
+ **Greengrass nucleus** (lower migration effort, full feature support)
+ **Greengrass nucleus lite** (higher migration effort, designed for resource-constrained devices).

The exact procedure that you follow depends on your device resources, required features, and specific environment requirements.

![An overview of how to migrate from AWS IoT Greengrass V1 to AWS IoT Greengrass V2.](http://docs.aws.amazon.com/greengrass/v2/developerguide/images/migration-workflow-updated.png)

1.

**[Understand the differences between V1 and V2](greengrass-v1-concept-differences.md)**

   AWS IoT Greengrass V2 introduces new fundamental concepts for device fleets and deployable software, and V2 simplifies several concepts from V1.

   The AWS IoT Greengrass V2 cloud service and AWS IoT Greengrass Core software v2.x aren't backward compatible with the AWS IoT Greengrass V1 cloud service and AWS IoT Greengrass Core software v1.x. As a result, AWS IoT Greengrass V1 over-the-air (OTA) updates can't upgrade core devices from V1 to V2.

1.

**[Choose your runtime (Greengrass nucleus or Greengrass nucleus lite)](choose-runtime.md)**

   Decide between Greengrass nucleus or Greengrass nucleus lite based on your device resources and feature requirements:
   + **Greengrass nucleus path**: Lower migration effort. Lambda functions can be imported as Lambda components with minimal code changes. Supports V1 features (local shadow service, client devices, connectors).
   + **Greengrass nucleus lite path**: Higher migration effort. Lambda functions need to be converted to generic components, requiring code changes to use AWS IoT Device SDK V2/AWS IoT Greengrass Component SDK instead of AWS IoT Greengrass Core SDK. Does not support local shadow service, client devices, or connectors.

1.

**[Set up a new device to test V1 applications on V2](set-up-test-device.md)**

   To minimize risk to your devices in production, create a new device to test your V1 applications on V2. Choose the setup guide based on your runtime selection:
   + **Option A - Greengrass nucleus runtime**: [Set up a new device to test V1 applications on V2](set-up-v2-test-device.md). Import Lambda functions as Lambda components with minimal code changes.
   + **Option B - Greengrass nucleus lite runtime**: [Set up a new device to test V1 applications on V2 (Greengrass nucleus lite)](set-up-v2-test-device-lite.md). Convert Lambda functions to generic components using AWS IoT Device SDK.

1.

**[Upgrade V1 core devices to run V2](upgrade-v1-core-devices.md)**

   After testing on a new device, upgrade your existing V1 core devices to run the AWS IoT Greengrass Core software v2.x and AWS IoT Greengrass V2 components. To migrate a fleet of devices from V1 to V2, you repeat this step for each device in the fleet.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
