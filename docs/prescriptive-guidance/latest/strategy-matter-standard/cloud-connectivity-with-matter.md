---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-matter-standard/cloud-connectivity-with-matter.html
---

# Cloud connectivity with Matter
<a name="cloud-connectivity-with-matter"></a>

While Matter enables basic local device interoperability, you need additional cloud connectivity to support over-the-air updates, telemetry data, remote management, and integration with proprietary vendor services. Device makers have options, such as shipping a Matter gateway hub, using a household's Matter-certified hub, or integrating direct cloud connectivity into endpoints. Standards for Matter-to-cloud connectivity are emerging, but manufacturers still need to integrate additional connectivity software stacks into Matter devices. To support capabilities such as diagnostics and new feature updates, Matter manufacturers should consider cloud integration in addition to basic local operation.

## Enabling advanced device capabilities with cloud connectivity for matter endpoints
<a name="advanced-capabilities"></a>

The Matter standard is designed to unify IoT devices from different vendors through a common protocol. It specifies how smart-home devices discover, communicate, and interoperate with each other on the local network by using IP-based networking technologies, such as Ethernet, Wi-Fi, and Thread. This local interoperability enables Matter-certified devices from different vendors to work together for activities like automated scenes and voice control. However, Matter doesn't define cloud interfaces or require internet connectivity for the device endpoints.

Many smart devices today rely on additional cloud connectivity for key features, such as over-the-air (OTA) updates, remote access, and integrations with manufacturer services. Device makers who want to build Matter-certified products while retaining advanced functionality must consider how to supplement Matter with cloud connectivity. While basic local control and voice assistant integration work for simple Matter devices, more advanced capabilities require additional cloud connectivity.

## Use cases that require cloud connectivity
<a name="use-cases-cloud-connectivity"></a>

Although Matter handles local device interoperability, additional cloud connectivity enables several smart-home device capabilities:
+ **Over-the-air (OTA) updates** – Delivering firmware and software updates over the internet allows vendors to enhance devices that are already deployed. Without OTA, vendors must update devices manually. While the Matter standard describes how to handle and deliver OTA updates to Matter-certified endpoints, it depends on the functionality that the connected Matter hub supports. Additionally, there are restrictions on which updates the endpoint receives. For example, when the endpoint requests an update, it receives only the latest available update. All devices of the same type receive that single update. There is no option to do a sequential update, an OTA rollback, or a deletion of an update. Enabling cloud connectivity on the endpoint can mitigate this lack of fine-grained management of OTA updates. Matter version 1.4.2 (June 2025) introduced improvements to transport reliability and testing infrastructure that enhance OTA update mechanisms. However, the fundamental limitations around sequential updates and rollback capabilities remain. Direct cloud connectivity helps manufacturers that require fine-grained update control and fleet management capabilities.
+ **Camera streaming and media** – Matter version 1.5 (November 2025) introduced camera support using side-channel protocols, such as Real-Time Streaming Protocol (RTSP) over Wi-Fi or Ethernet. While Matter handles device discovery and basic control, the actual video streaming occurs through separate protocols. This often requires cloud infrastructure for remote viewing, recording, and AI-based features, such as person detection.
+ **Remote access and control** – Accessing and controlling devices remotely from outside of the home network requires a cloud endpoint. Matter, as currently defined, only supports local access. While a Matter endpoint can be controlled with a user app inside the local network, remote control is only available if it's supported by the Matter hub. Even then, typically, only basic remote controls are available.
+ **Telemetry and diagnostics** – Aggregating field data, such as error logs and sensor streams, in the cloud allows vendors to monitor device health and identify issues. While Matter supports radio and protocol-related diagnostics through the general diagnostics cluster, detailed device-specific diagnostics require cloud connectivity so that the manufacturer can retrieve data from the device.
+ **Vendor-specific integrations** – Custom features and data types that the Matter specification doesn't define require connectivity to vendor cloud services. This is particularly relevant for devices with advanced features, such as cameras (Matter version 1.5), energy management devices (Matter version 1.4), and appliances (Matter versions 1.2–1.3), that might require manufacturer-specific cloud services for full functionality.
+ **External integrations** – Linking to third-party services, such as voice assistants that don't support Matter or third-party payment gateways (depending on the use case), requires internet connectivity beyond the Matter hub.

Because these capabilities rely on cloud connectivity, Matter endpoints often need additional options for internet access.

## Architectures for enabling cloud connectivity
<a name="architectures-cloud-connectivity"></a>

For Matter devices, there are three general approaches to providing the necessary cloud connectivity while meeting the local operation specifications.

### Smart-home hub with built-in gateway
<a name="smart-home-hub-with-built-in-gateway.8af01c0c-d8ad-579f-8615-a95d1c4e4b75"></a>

Some device makers might choose to ship a proprietary home hub that incorporates both the Matter administrator and a gateway to their cloud services. This home hub would manage attached Matter endpoints locally per the standard, while also facilitating cloud connections for advanced functions. The hub could support over-the-air (OTA) updates, remote access, and telemetry collection for endpoints.

### Offload cloud connectivity to an existing Matter hub
<a name="offload-cloud-connectivity-to-an-existing-matter-hub.2218d5ed-7699-56a3-a07a-c5a9f9a90dc5"></a>

Rather than bundle a custom hub, devices could be designed to connect with Matter hubs, such as Amazon Echo, Google Nest Hub, Apple HomePod, or Samsung SmartThings Hub, for internet connectivity. In this case, the existing Matter hub handles local device communication according to the standard, and it also provides a gateway to the cloud for endpoints that require it. This takes advantage of infrastructure consumers might already have. However, this approach depends on the level of support offered by the Matter hub for features that are not specified as normative for Matter hubs in the standard.

### Direct cloud connectivity in endpoints
<a name="direct-cloud-connectivity-in-endpoints.148b5570-0875-58c1-966c-65e58dfb8868"></a>

Devices with direct internet connectivity, such as Wi-Fi, could integrate separate connectivity for the Matter local network and for vendor cloud services. This allows the device to act as its own gateway to the cloud and connect independently. However, this approach might not be feasible for simple, low-cost, battery-powered devices. Non-Wi-Fi endpoints that rely on protocols such as Thread require additional solutions.

## Bridging Matter and manufacturer cloud platforms
<a name="bridging-platforms"></a>

While Matter simplifies local interoperability, you need additional effort to connect Matter admin systems and manufacturer cloud services. The Connectivity Standards Alliance (CSA) continues to develop standards for Matter-to-cloud connectivity. As of 2026, formal cloud interface standards are still evolving, but common industry practices have emerged from the deployment of Matter devices. Wider adoption of standards for this cloud connectivity would ease development for device makers.

The most suitable approach depends on the use cases, price points, and business models of specific products. Access to cloud services is typically necessary to provide the advanced functionality that smart-home consumers expect, even for Matter-compliant devices that focus on local interoperability. Device makers can use Matter for interoperability while still providing advanced capabilities through well-designed cloud connectivity.
