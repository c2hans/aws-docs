---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/use-ipv6.html
---

# Use IPv6 for local messaging
<a name="use-ipv6"></a>

You can configure the IP detector component to use IPv6 to send local messages.

**Note**
You must have IP detector v2.2.0 or later to use IPv6 to send local messages.

You can deploy the [IP detector component](ip-detector-component.md) to detect and use IPv6 addresses. You must update the configuration of the IP detector component to use IPv6 instead of IPv4. For more information, see [Use IP detector to automatically manage endpoints](manage-core-device-endpoints.md#use-ip-detector).

**Topics**
+ [Configure IP detector to use IPv6](#configure-ip-detector-ipv6)

## Configure IP detector to use IPv6
<a name="configure-ip-detector-ipv6"></a>

If you have a simple network setup, such as the client devices on the same network as the core device, you can deploy the [IP detector component](ip-detector-component.md) to use IPv6 for local messaging.

The IP detector component overwrites endpoints that you set manually.

**Important**
The core device's AWS IoT policy must allow the `greengrass:UpdateConnectivityInfo` permission to use the IP detector component. For more information, see [AWS IoT policies for data plane operations](device-auth.md#iot-policies) and [Configure the AWS IoT thing policy](connect-client-devices.md#configure-iot-policy-requirement).

You can do either of the following to deploy the IP detector component:
+ Use the **Configure discovery** page in the console. For more information, see [Configure cloud discovery (console)](connect-client-devices.md#configure-cloud-discovery-console).
+ Create and revise deployments to include the IP detector. You can use the console, AWS CLI, or AWS API to manage deployments. For more information, see [Create deployments](create-deployments.md).

### Deploy the IP detector component (console)
<a name="deploy-ip-detector-console-ipv6"></a>

1. In the [AWS IoT Greengrass console](https://console.aws.amazon.com/greengrass) navigation menu, choose **Components**.

1. On the **Components** page, choose the **Public components** tab, and then choose **aws.greengrass.clientdevices.IPDetector**.

1. On the **aws.greengrass.clientdevices.IPDetector** page, choose **Deploy**.

1. <a name="deploy-component-choose-deployment-step"></a>From **Add to deployment**, choose an existing deployment to revise, or choose to create a new deployment, and then choose **Next**.

1. <a name="deploy-component-choose-target-step"></a>If you chose to create a new deployment, choose the target core device or thing group for the deployment. On the **Specify target** page, under **Deployment target**, choose a core device or thing group, and then choose **Next**.

1. On the **Select components** page, verify that the **aws.greengrass.clientdevices.IPDetector** component is selected, choose **Next**.

1. On the **Configure components** page, select **aws.greengrass.clientdevices.IPDetector**, and then do the following:

   1. Choose **Configure component**.

   1. In the **Configure aws.greengrass.clientdevices.IPDetector** modal, under **Configuration update**, in **Configuration to merge**, you can enter a configuration update to configure the IP detector component. You can specify any of the following configuration options. Set `includeIPv4Addrs` to `false` and `includeIPv6Addrs` to `true`. You can then update the other IPv6 configuration options.
      + `defaultPort` – <a name="ip-detector-component-configuration-default-port-definition"></a>(Optional) The MQTT broker port to report when this component detects IP addresses. You must specify this parameter if you configure the MQTT broker to use a different port than the default port 8883.
      + `includeIPv4LoopbackAddrs` – <a name="ip-detector-component-configuration-include-ipv4-loopback-addrs-definition"></a>(Optional) You can enable this option to detect and report IPv4 loopback addresses. These are IP addresses, such as `localhost`, where a device can communicate with itself. Use this option in test environments where the core device and client device run on the same system.
      + `includeIPv4LinkLocalAddrs` – <a name="ip-detector-component-configuration-include-ipv4-link-local-addrs-definition"></a>(Optional) You can enable this option to detect and report IPv4 [link-local addresses](https://en.wikipedia.org/wiki/Link-local_address). Use this option if the core device's network doesn't have Dynamic Host Configuration Protocol (DHCP) or statically assigned IP addresses.
      + `includeIPv6LoopbackAddrs` – <a name="ip-detector-component-configuration-include-ipv6-loopback-addrs-definition"></a>(Optional) You can enable this option to detect and report IPv6 loopback addresses. These are IP addresses, such as `localhost`, where a device can communicate with itself. Use this option in test environments where the core device and client device run on the same system. You must set `includeIPv4Addrs` to `false` and `includeIPv6Addrs` to `true` to use this option. You must have IP detector v2.2.0 or later to use this option.
      + `includeIPv6LinkLocalAddrs` – <a name="ip-detector-component-configuration-include-ipv6-link-local-addrs-definition"></a>(Optional) You can enable this option to detect and report IPv6 [link-local addresses](https://en.wikipedia.org/wiki/Link-local_address). Use this option if the core device's network doesn't have Dynamic Host Configuration Protocol (DHCP) or statically assigned IP addresses. You must set `includeIPv4Addrs` to `false` and `includeIPv6Addrs` to `true` to use this option. You must have IP detector v2.2.0 or later to use this option.
      + `includeIPv4Addrs` – <a name="ip-detector-component-configuration-include-ipv4-addrs-definition"></a>(Optional) The default is set to true. You can enable this option to publish IPv4 addresses found on the core device. You must have IP detector v2.2.0 or later to use this option.
      + `includeIPv6Addrs` – <a name="ip-detector-component-configuration-include-ipv6-addrs-definition"></a>(Optional) You can enable this option to publish IPv6 addresses found on the core device. Set `includeIPv4Addrs` to `false` to use this option. You must have IP detector v2.2.0 or later to use this option.

      The configuration update might look similar to the following example.

      ```
      {
        "defaultPort": "8883",
        "includeIPv4LoopbackAddrs": false,
        "includeIPv4LinkLocalAddrs": false,
        "includeIPv6LoopbackAddrs": true,
        "includeIPv6LinkLocalAddrs": true,
        "includeIPv4Addrs": false,
        "includeIPv6Addrs": true
      }
      ```

   1. Choose **Confirm** to close the modal, and then choose **Next**.

1. <a name="deploy-component-configure-advanced-settings-step"></a>On the **Configure advanced settings** page, keep the default configuration settings, and choose **Next**.

1. <a name="deploy-component-review-and-deploy-step"></a>On the **Review** page, choose **Deploy**.

   The deployment can take up to a minute to complete.

### Deploy the IP detector component (AWS CLI)
<a name="deploy-ip-detector-cli-ipv6"></a>

To deploy the IP detector component, create a deployment document that includes `aws.greengrass.clientdevices.IPDetector` in the `components` object, and specify the configuration update for the component. Follow instructions in [Create deployments](create-deployments.md) to create a new deployment or revise an existing deployment.

You can specify any of the following options to configure the IP detector component when you create the deployment document:
+ `defaultPort` – <a name="ip-detector-component-configuration-default-port-definition"></a>(Optional) The MQTT broker port to report when this component detects IP addresses. You must specify this parameter if you configure the MQTT broker to use a different port than the default port 8883.
+ `includeIPv4LoopbackAddrs` – <a name="ip-detector-component-configuration-include-ipv4-loopback-addrs-definition"></a>(Optional) You can enable this option to detect and report IPv4 loopback addresses. These are IP addresses, such as `localhost`, where a device can communicate with itself. Use this option in test environments where the core device and client device run on the same system.
+ `includeIPv4LinkLocalAddrs` – <a name="ip-detector-component-configuration-include-ipv4-link-local-addrs-definition"></a>(Optional) You can enable this option to detect and report IPv4 [link-local addresses](https://en.wikipedia.org/wiki/Link-local_address). Use this option if the core device's network doesn't have Dynamic Host Configuration Protocol (DHCP) or statically assigned IP addresses.
+ `includeIPv6LoopbackAddrs` – <a name="ip-detector-component-configuration-include-ipv6-loopback-addrs-definition"></a>(Optional) You can enable this option to detect and report IPv6 loopback addresses. These are IP addresses, such as `localhost`, where a device can communicate with itself. Use this option in test environments where the core device and client device run on the same system. You must set `includeIPv4Addrs` to `false` and `includeIPv6Addrs` to `true` to use this option. You must have IP detector v2.2.0 or later to use this option.
+ `includeIPv6LinkLocalAddrs` – <a name="ip-detector-component-configuration-include-ipv6-link-local-addrs-definition"></a>(Optional) You can enable this option to detect and report IPv6 [link-local addresses](https://en.wikipedia.org/wiki/Link-local_address). Use this option if the core device's network doesn't have Dynamic Host Configuration Protocol (DHCP) or statically assigned IP addresses. You must set `includeIPv4Addrs` to `false` and `includeIPv6Addrs` to `true` to use this option. You must have IP detector v2.2.0 or later to use this option.
+ `includeIPv4Addrs` – <a name="ip-detector-component-configuration-include-ipv4-addrs-definition"></a>(Optional) The default is set to true. You can enable this option to publish IPv4 addresses found on the core device. You must have IP detector v2.2.0 or later to use this option.
+ `includeIPv6Addrs` – <a name="ip-detector-component-configuration-include-ipv6-addrs-definition"></a>(Optional) You can enable this option to publish IPv6 addresses found on the core device. Set `includeIPv4Addrs` to `false` to use this option. You must have IP detector v2.2.0 or later to use this option.

The following example partial deployment document specifies to use IPv6.

```
{
  {{...}},
  "components": {
    {{...}},
    "aws.greengrass.clientdevices.IPDetector": {
      "componentVersion": "2.1.1",
      "configurationUpdate": {
        "merge": "{\"defaultPort\":\"8883\",}"
      }
    }
  }
}
```
