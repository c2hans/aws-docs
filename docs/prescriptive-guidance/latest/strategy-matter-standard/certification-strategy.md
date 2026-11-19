---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-matter-standard/certification-strategy.html
---

# Considerations for certification strategy

Matter enables interoperability between different smart home devices and platforms. However, certifying with Matter may not be the right choice for every device manufacturer. The costs of implementation and certification may not make practical or financial sense, depending on the device type and use cases. This section explores some of the key reasons why a manufacturer might choose not to certify certain devices with Matter.

While the Matter standard aims to simplify development and improve compatibility across devices, certain types of smart home devices may face practical barriers to certification that outweigh the benefits. For products with stringent constraints, non-IP protocols, limited audiences, or device types that Matter doesn't define, pursuing Matter certification might not be an effective strategy initially. These factors might lead a manufacturer to avoid adopting Matter. However, Matter does allow IP-enabled gateway devices to proxy for non-IP endpoints. For certain legacy devices, a gateway approach can be a viable path to Matter compatibility, while avoiding a full device redesign.

As of Matter version 1.5, with thousands of certified devices in the market, the Matter standard has matured. Improved SDKs, more complete documentation, and expanded testing infrastructure have reduced the barriers to certification. However, the considerations outlined below remain relevant for manufacturers evaluating their certification strategy.

As the Matter standard evolves and its scope expands to cover more use cases, the case for certification might strengthen over time, even for these product categories. Device manufacturers need to evaluate their specific situations and roadmaps to determine the appropriate approach to Matter certification. In many situations, there might be sound technical or business reasons for opting out of certification, at least temporarily.

## Non-IP connectivity protocols
<a name="connectivity-protocols"></a>

To adopt the Matter standard, devices must operate on IP networks, such as Wi-Fi, Ethernet, and Thread. Low-bandwidth devices commonly use non-IP wireless protocols, such as Zigbee, Z-Wave, and Bluetooth LE. These protocols require an additional non-IP to IP-based protocol translator to be compatible with Matter. Upgrading the communication module or introducing a translation gateway typically increases the hardware cost of the device.

Adding IP stack support means allocating more memory and processing power for network handling. This might exceed the capabilities of extremely low-cost and low-power devices. Adding extra memory or flash storage to support IP would also increase manufacturing costs and reduce battery life. For use cases that require only power switching (on and off) or sensor data, non-IP protocols can provide an efficient solution.

Matter doesn't certify devices that rely solely on proprietary, non-IP wireless standards. This could limit manufacturers who want to use alternative connectivity methods for their low-cost products. While IP-based protocols like Wi-Fi and Ethernet are required to interface with different smart home systems, non-IP standards can still provide basic connectivity for sensors and switches in some applications.

Matter bridges allow manufacturers to maintain their existing non-IP device lines while gaining Matter compatibility through certified bridge products. This approach works for Zigbee and Z-Wave devices, where a single bridge can expose multiple legacy devices as Matter endpoints.

## Hardware limitations
<a name="hardware-limitations"></a>

Another challenge is that Matter requires a minimum level of on-device processing power and memory to support the necessary software stack. However, the most basic smart-home devices often have very limited embedded chip capabilities, due to cost and size constraints.

For example, a simple door or window sensor might contain only a microcontroller with less than 100 KB of flash memory and 10 KB of RAM. This does not provide enough storage and processing headroom for a full Matter implementation. Adding more powerful and expensive silicon would drive up the bills of materials significantly.

In cases where cost and size are the top priorities, manufacturers might find Matter requirements do not align with their hardware budgets. Certifying very basic sensors, switches, or controllers with Matter could force unnecessary hardware upgrades that affect affordability.

Matter version 1.4.2 (June 2025) introduced improvements to transport reliability and Bluetooth Low Energy (BLE) commissioning that reduce resource usage. The maturity of the SDK and the availability of reference implementations have also reduced the overhead of Matter integration. However, for extremely constrained devices (under 100 KB flash), the gateway proxy approach remains a practical solution.

## Customer ecosystems
<a name="customer-ecosystems"></a>

Another factor to consider is whether a manufacturer's target customer base uses smart-home systems that are compatible with Matter. If most consumers in that segment do not use Matter controllers or Matter-enabled hubs and apps, there may be little incentive to certify products.

For example, a company that serves elderly users might find that its customers have simple setups without Matter administrators. Similarly, do-it-yourself (DIY) home automation enthusiasts might prefer custom solutions and not need Matter's plug-and-play experience across brands.

In scenarios where the target demographic does not engage with Matter infrastructure, certification can add complexity with limited benefit. Consider investing resources in optimizing the user experience within the relevant systems instead of diverting effort to Matter compliance.

Matter support is growing among smart-home vendors, and in some market segments customers may expect it. Evaluate whether your target customers use Matter-enabled products, and weigh that against the cost of certification.

## Device types not yet defined
<a name="device-types"></a>

While Matter's scope has expanded dramatically from the initial release, covering most common smart-home categories and many appliances, some niche verticals still await standardization.

If a company develops unique device types that existing Matter profiles do not cover, it cannot certify them until Matter defines new profiles. This could delay a new product's launch while the company waits for Matter to expand its scope.

Rather than hold off on releasing innovations, some manufacturers might prefer bringing niche solutions to market sooner through proprietary means. Certifying later is still an option after the relevant profiles mature. For first-mover advantages, going direct-to-consumer without Matter might be preferable in some cases.

## An alternative: Proxying at gateways
<a name="gateway-proxying"></a>

In situations where an endpoint device has limitations that prevent direct Matter certification, an alternative approach is to proxy the device's Matter capability at a gateway. The gateway serves as a bridge that translates between the local wireless protocol of the endpoint and the IP-based Matter protocol.

For example, a basic temperature sensor communicating over a proprietary radio standard can still appear as a Matter device to the Matter controller. The gateway receives sensor data on a non-IP interface but exposes virtual Matter entities representing that data over IP to controllers. This approach allows you to use existing hardware and gain interoperability benefits through the gateway.

This approach adds complexity for developers and requires gateways to support the necessary translation layer. However, it can be a viable compromise when direct certification is too challenging for the device itself. Proxies can help low-power or specialized devices participate in Matter networks without redesigning the hardware.

The Matter bridge specification has matured, with numerous certified bridge products now available from manufacturers. This has made the gateway approach more viable and standardized compared to earlier Matter releases. Manufacturers can now partner with bridge providers or develop their own certified bridges to bring non-IP devices into Matter networks without redesigning the endpoint hardware.
