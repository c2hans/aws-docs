---
source_url: https://docs.aws.amazon.com/iot-mi/latest/devguide/device-and-device-profile-lifecycle-management.html
---

# Device and device profile lifecycle
<a name="device-and-device-profile-lifecycle-management"></a>

Managing the lifecycle of your devices and device profiles ensures your fleet of devices are secure and running efficiently.

**Topics**
+ [Device](#device)
+ [Device profile](#device-profile)

## Device
<a name="device"></a>

During initial onboarding, Managed Integrations creates a digital twin of your physical device called a *Managed Thing*. The Managed Thing has a `managedThingID` that provides a global unique identifier to identify the device in Managed Integrations across all regions. The device pairs with the local hub during provisioning for real-time communication with Managed Integrations or a third-party cloud for third-party devices. A device is also associated with an owner as identified by the `owner` parameter in the public APIs for a Managed Thing such as `GetManagedThing`. The device is linked to the corresponding device profile based on the type of device.

**Note**
A physical device may have multiple records if it is provisioned multiple times under different customers.

The device lifecycle starts with the creation of the Managed Thing in Managed Integrations using the `CreateManagedThing` API and ends when the customer deletes the Managed Thing using the `DeleteManagedThing` API. The lifecycle of a device is managed by the following public APIs:
+ `CreateManagedThing`
+ `ListManagedThings`
+ `GetManagedThing`
+ `UpdateManagedThing`
+ `DeleteManagedThing`

## Device profile
<a name="device-profile"></a>

A device profile represents a specific type of device such as a light bulb or doorbell. It is associated with a manufacturer and contains the capabilities of the device. The device profile stores the authentication materials needed for device connectivity setup requests with Managed Integrations. The authentication materials used are the device bar code.

During the device manufacturing process, the manufacturer can register their device profiles with Managed Integrations. This enables the manufacturer to obtain the necessary materials for the devices from Managed Integrations during the onboarding and provisioning workflows. The metadata from the device profile is stored on the physical device or printed on the device labeling. The lifecycle of the device profile ends when the manufacturer deletes it in Managed Integrations.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Managed integrations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-mi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
