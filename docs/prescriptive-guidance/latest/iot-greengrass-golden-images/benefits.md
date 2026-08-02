---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/iot-greengrass-golden-images/benefits.html
---

# Why use golden images?
<a name="benefits"></a>

There are numerous reasons for using a golden image to program devices in the factory.

If you're planning to manufacture AWS IoT Greengrass devices at scale, you might consider it problematic to perform an AWS IoT Greengrass cloud deployment for each device on the manufacturing line. Your reasons might include:
+ **It's too slow**: The time required to perform a deployment for every device can affect your manufacturing line productivity.
+ **There's no internet connectivity**: Contract manufacturers sometimes don't have internet connectivity on the manufacturing line, so a cloud deployment might not even be possible.
+ **There's intermittent internet connectivity**: Even if internet connectivity is nominally available, your company might require that your manufacturing line not be stalled by a temporary loss of connectivity, so a cloud deployment might not be desirable.

If you choose not to perform an AWS IoT Greengrass deployment on the manufacturing line, you could ship your device with no application components installed. However, your devices might still require application components to be installed during manufacture for the following reasons:
+ **Factory acceptance testing (FAT)**: You might need to perform FAT on every device, or a sampling of devices, as part of your quality assurance (QA) processes. Your device will likely have its own domain-specific I/O and interfaces that can be tested only if your device is in a fully working state and runs your own application software.
+ **Field internet connectivity isn't reliable**: When your device is installed or unboxed in the field, you can't be sure that there will be internet connectivity in its environment. Therefore, you can't rely on a cloud deployment to put the device into a fully working state.
+ **Device needs to work immediately**: Your device might have to be in a fully working state when it's first unboxed in the field and not able to wait for the first cloud deployment to complete, even if internet connectivity is reliable.
+ **Cellular network data charges**: Your device might have cellular network connectivity, and downloading all your application component artifacts during an initial cloud deployment in the field might incur significant cost.

Consequently, an AWS IoT Greengrass device typically needs to be manufactured with application components partially or fully installed and configured, but might not be able to use an AWS IoT Greengrass cloud deployment. This guide discusses how you can achieve that objective.

## Using the Greengrass CLI instead of a golden image
<a name="using-cli"></a>

An alternative to using golden images is to locally compose your software image on each device by automating the installation of the Greengrass runtime, and then automating the installation of components by using the [Greengrass command line interface (CLI)](https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-cli-component.html). However:
+ You would need to install the Greengrass CLI first, in an offline environment. Although this type of installation is possible, there is no documented procedure for it.
+ You would need to collect and organize all component artifacts and recipes, and have them available on the manufacturing line.
+ You would need to use the [Greengrass CLI local deployment command](https://docs.aws.amazon.com/greengrass/v2/developerguide/gg-cli-deployment.html) to deploy each component.
+ You would need be careful when you use the `groupId` and component versions for the local deployments to make sure that subsequent cloud deployments won't be in conflict.
+ If the Greengrass CLI is not required on your device in the field, you would typically remove it as a final step.

Overall, the Greengrass CLI approach is slower, and more prone to error, than a golden image.
