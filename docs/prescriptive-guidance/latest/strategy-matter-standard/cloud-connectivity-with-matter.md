---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-matter-standard/cloud-connectivity-with-matter.html
---

# Cloud connectivity with Matter
<a name="cloud-connectivity-with-matter"></a>

While Matter enables basic local device interoperability, additional cloud connectivity is required to deliver robust over-the-air updates, telemetry data, remote management, and integration with proprietary vendor services. Device makers have options, such as shipping a Matter gateway hub, using a household's Matter-certified hub, or integrating direct cloud connectivity into endpoints. Standards for Matter-to-cloud connectivity are emerging, but manufacturers still need to integrate additional connectivity software stacks into Matter devices. Delivering the full value of smart-home devices in areas like diagnostics and new feature updates requires Matter manufacturers to consider cloud integration, beyond basic local operation.

## Enabling advanced device capabilities with cloud connectivity for matter endpoints
<a name="advanced-capabilities"></a>

The Matter standard promises to unify IoT devices from different vendors through a common protocol. It specifies how smart-home devices discover, communicate, and interoperate with each other on the local network by using IP-based networking technologies, such as Ethernet, Wi-Fi, and Thread. This local interoperability enables Matter-certified devices from different vendors to work together seamlessly for activities like automated scenes and voice control. However, Matter does not define cloud interfaces or require internet connectivity for the device endpoints.

Many smart devices today rely on additional cloud connectivity for key features, such as over-the-air (OTA) updates, remote access, and integrations with manufacturer platforms. Device makers looking to build Matter-compliant products while retaining advanced functionality face some design considerations around supplementing Matter with cloud connectivity. While basic local control and voice assistant integration work for simple Matter devices, additional cloud connectivity is required to enable more advanced capabilities.

## Use cases that require cloud connectivity
<a name="use-cases-cloud-connectivity"></a>

Although Matter handles local device interoperability, additional cloud connectivity enables several important smart-home device capabilities:
+ **Over-the-air (OTA) updates** – Delivering firmware and software updates over the internet allows vendors to easily enhance devices that are already deployed. Without OTA, updates would be handled manually. While Matter standard describes how the OTA updates are handled and delivered to Matter-certified endpoints, it is dependent on the functionality supported by the Matter hub that the endpoint is connected to. Additionally, there are restrictions regarding which updates are provided to the endpoint. For example, when the endpoint requests an update, only the latest update available is provided. All devices of the same type are provided that single update. There is no option to do a sequential update or even an OTA rollback or deletion of an update. Enabling cloud connectivity on the endpoint can mitigate this lack of fine-grained management of OTA updates. Matter version 1.4.2 (June 2025) introduced improvements to transport reliability and testing infrastructure that have enhanced OTA update mechanisms. However, the fundamental limitations around sequential updates and rollback capabilities remain, making direct cloud connectivity valuable for manufacturers that require fine-grained update control and fleet management capabilities.
+ **Camera streaming and media** – Matter version 1.5 (November 2025) introduced camera support using side-channel protocols, such as Real-Time Streaming Protocol (RTSP) over Wi-Fi or Ethernet. While Matter handles device discovery and basic control, the actual video streaming occurs through separate protocols. This often requires cloud infrastructure for remote viewing, recording, and AI-based features, such as person detection.
+ **Remote access and control** – Accessing and controlling devices remotely from outside of the home network requires a cloud endpoint. Matter, as currently defined, only supports local access. While a Matter endpoint can be controlled with a user app inside the local network, remote control is only available if it's supported by the Matter hub. Even then, typically, only basic remote controls are available.
+ **Telemetry and diagnostics** – Aggregating field data, such as error logs and sensor streams, in the cloud allows vendors to monitor device health and identify issues. While Matter supports radio and protocol-related diagnostics through the general diagnostics cluster, any detailed diagnostics specific to the device requires cloud connectivity so that the manufacturer can retrieve data from the device.
+ **Vendor-specific integrations** – Any custom features and data types that are not defined in the Matter specification require connectivity to vendor cloud platforms. This is particularly important for devices with advanced features like cameras (Matter version 1.5), energy management devices (Matter version 1.4), and appliances (Matter versions 1.2-1.3) that may require manufacturer-specific cloud services for full functionality.
+ **External integrations** – Linking to third-party services like voice assistants not on Matter ecosystem or third-party payment gateways (as needed per use case) requires internet connectivity beyond the Matter admin.

With these critical capabilities relying on cloud connectivity, Matter endpoints often need additional options for internet access.

## Architectures for enabling cloud connectivity
<a name="architectures-cloud-connectivity"></a>

For Matter devices, there are three general approaches to providing the necessary cloud connectivity while meeting the local operation specifications.

### Smart-home hub with built-in gateway
<a name="smart-home-hub-with-built-in-gateway.f96f8003-5f1e-5fc7-9775-21a5e46d0727"></a>

Some device makers might choose to ship a proprietary home hub that incorporates both the Matter administrator and a gateway to their cloud services. This home hub would manage attached Matter endpoints locally per the standard, while also facilitating cloud connections for advanced functions. The hub could support OTA updates, remote access, and telemetry collection for endpoints.

### Offload cloud connectivity to an existing Matter hub
<a name="offload-cloud-connectivity-to-an-existing-matter-hub.2218d5ed-7699-56a3-a07a-c5a9f9a90dc5"></a>

Rather than bundle a custom hub, devices could be designed to connect with Matter hubs, such as Amazon Echo, Google Nest Hub, Apple HomePod, or Samsung SmartThings Hub, for internet connectivity. In this case, the existing Matter hub handles local device communication according to the standard, and it also provides a gateway to the cloud for endpoints that require it. This takes advantage of infrastructure consumers might already have. However, this approach depends on the level of support offered by the Matter hub for features that are not specified as normative for Matter hubs in the standard.

### Direct cloud connectivity in endpoints
<a name="direct-cloud-connectivity-in-endpoints.edad60f5-ec55-54e8-a8b2-fd5894260b1c"></a>

Devices with direct internet connectivity, such as Wi-Fi, could integrate separate connectivity for the Matter local network and for vendor cloud services. This allows the device to act as its own gateway to the cloud. However, solutions are needed for non-Wi-Fi endpoints that rely on protocols such as Thread. This allows devices to connect to the cloud independently, but it might not be feasible for simple, low-cost, battery-powered devices.

## Bridging Matter and manufacturer cloud platforms
<a name="bridging-platforms"></a>

While Matter simplifies local interoperability, additional effort is required to smoothly connect Matter admin systems and manufacturer cloud platforms. The Connectivity Standards Alliance (CSA) continues to develop standards for Matter-to-cloud connectivity. As of 2026, while formal cloud interface standards are still evolving, industry best practices have emerged from the deployment of thousands of Matter devices. Widely adopting standards for this cloud connectivity would ease development for device makers.

The optimal path depends on the use cases, price points, and business models of specific products. It is clear that robust access to cloud services is necessary to unlock the full functionality that smart-home consumers expect—even for Matter-compliant devices that are focused on local interoperability. Device makers have an opportunity to use Matter for interoperability while still providing the advanced capabilities through thoughtfully designed cloud connectivity.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
