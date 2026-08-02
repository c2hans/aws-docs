---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/choosing-your-runtime.html
---

# Choosing your AWS IoT Greengrass nucleus runtime
<a name="choosing-your-runtime"></a>

As of version 2.14.0, AWS IoT Greengrass provides two alternative implementations of its device runtime, an executable known as the nucleus. Despite their implementation differences, both runtimes are compatible with the AWS IoT Greengrass service and APIs and allow you to deploy components provided by AWS or develop custom components using the Greengrass SDK. It is also possible to mix devices, using either type of nucleus within the same fleet as necessary.

However, in order to achieve the desired portability or the specific memory saving benefits, it is essential to ensure that the nucleus you deploy on your Greengrass devices is compatible with the components you intend to use to accelerate the development of your AWS IoT solutions. To learn more about component compatibility, see [Components](https://docs.aws.amazon.com/greengrass/v2/developerguide/public-components.html).

Ultimately, the choice between the two Greengrass runtime options will depend on your specific use case, device constraints, feature requirements, and operating system.

## Greengrass nucleus
<a name="w2ab1b6c19b9"></a>

AWS IoT Greengrass nucleus is the fully-featured runtime that enables you to run AWS IoT Greengrass on a wide range of devices, including gateways, servers, and edge devices with more compute resources. Consider choosing Greengrass nucleus if:
+ **Compute resources:** Your device has sufficient compute resources, such as more than 128 MB of RAM and a relatively powerful processor (for example, greater than 1 GHz clock).
+ **Full OS support is needed:** Greengrass nucleus supports the widest range of operating systems (including most Linux distros and Windows).
+ **Components compatibility:** Greengrass nucleus offers the fullest compatibility with existing components published by the AWS IoT service team and partners.

## Greengrass nucleus lite
<a name="w2ab1b6c19c11"></a>

AWS IoT Greengrass nucleus lite is a lightweight, open-source runtime that enables you to run AWS IoT Greengrass on resource-constrained devices. This can be useful for low-cost, single-board computers with high-volume applications, such as smart home hubs, smart energy meters, smart vehicles, edge AI, and robotics. Consider choosing Greengrass nucleus lite if your devices are:
+ **Resource-constrained:** Your device has limited resources, such as RAM memory (512 MB or less), storage (FLASH) space or a low-performance processor (less than 1 GHz).
+ **Dependency limited:** Your device vendor software platform does not support Java or the specific JVM required by Greengrass nucleus.
+ **Operating system:** Your devices run a distribution of Linux that supports *systemd* (for example: Ubuntu, Yocto).

### Current limitations of Greengrass nucleus lite
<a name="w2ab1b6c19c11b7"></a>

Greengrass nucleus lite runtime offers a subset of the functionality available in Greengrass nucleus.

The AWS IoT Greengrass IPC (interprocess communication) mechanism allows components to communicate with the Greengrass nucleus. The lightweight version of the nucleus supports the following subset:

| Feature | Availability |
| --- | --- |
| SubscribeToTopic | Available |
| PublishToTopic | Available |
| PublishToIoTCore | Available |
| SubscribeToIoTCore | Available |
| UpdateState | Not currently available |
| SubscribeToComponentUpdates | Not currently available |
| DeferComponentUpdate | Not currently available |
| GetConfiguration | Available |
| UpdateConfiguration | Available |
| SubscribeToConfigurationUpdate | Available |
| SubscribeToValidateConfigurationUpdates | Not currently available. |
| SendConfigurationValidityReport | Not currently available. |
| GetSecretValue | Not currently available. |
| PutComponentMetric | Not currently available |
| GetComponentDetails | Not currently available |
| RestartComponent | Not currently available |
| StopComponent | Not currently available |
| CreateLocalDeployment | Available |
| CancelLocalDeployment | Not currently available |
| GetLocalDeploymentStatus | Not currently available |
| ListLocalDeployments | Not currently available |
| ListComponents | Not currently available |
| ValidateAuthorizationToken | Available |
| CreateDebugPassword | Not currently available |
| PauseComponent | Not currently available |
| ResumeComponent | Not currently available |
| GetThingShadow | Not currently available |
| UpdateThingShadow | Not currently available |
| DeleteThingShadow | Not currently available |
| ListNamedShadowsForThing | Not currently available |
| SubscribeToCertificateUpdates | Not currently available |
| VerifyClientDeviceIdentity | Not currently available |
| GetClientDeviceAuthToken | Not currently available |
| AuthorizeClientDeviceAction | Not currently available |
