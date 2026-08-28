---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-matter-standard/certification-strategy.html
---

# Considerations for certification strategy
<a name="certification-strategy"></a>

Matter enables interoperability between different smart-home devices and platforms. However, certifying with Matter may not always be the best choice for device manufacturers. The costs of implementation and certification may not make practical or financial sense, depending on the device type and use cases. This section explores some of the key reasons why a manufacturer might choose to not certify certain devices with Matter.

While the Matter standard aims to simplify development and enable universal compatibility, certain types of smart-home devices may face practical barriers to certification that outweigh the benefits. For products with stringent constraints, non-IP protocols, limited audiences, or non-defined device types in Matter, pursuing Matter certification might not be the best strategy initially. These could be the reasons a manufacturer might avoid adopting Matter. However, Matter does allow for IP-enabled gateway devices to proxy for non-IP endpoints. For certain legacy devices, a gateway approach can be a viable path to Matter compatibility, while avoiding a full device redesign.

As of 2026, with Matter now at version 1.5 and thousands of certified devices in the market, the ecosystem has matured significantly. The barriers to certification have been reduced through improved SDKs, better documentation, and expanded testing infrastructure. However, the considerations outlined below remain relevant for manufacturers evaluating their certification strategy.

As the Matter standard evolves and its scope expands to cover more use cases, the case for certification might strengthen over time, even for these product categories. Device manufacturers need to evaluate their specific situations and roadmaps to determine the best approach regarding Matter compliance. In many situations, there might be sound technical or business reasons for opting out of certification, at least temporarily.

## Non-IP connectivity protocols
<a name="connectivity-protocols"></a>

In order to adopt the Matter standard, devices must operate on IP networks, such as Wi-Fi, Ethernet, and Thread. Non-IP wireless protocols, such as Zigbee, Z-Wave, and Bluetooth LE, are commonly used in low-bandwidth devices. These protocols require an additional non-IP to IP-based protocol translator to be compatible with Matter. Upgrading the communication module or introducing a translation gateway typically increases the hardware cost of the device.

Adding IP stack support means allocating more memory and processing power for network handling. This might exceed the capabilities of extremely low-cost and low-power devices. The addition of extra memory or flash to support IP would also increase manufacturing costs and reduce battery life. For use cases where on and off power or sensor data is all that is needed, non-IP protocols can provide an efficient solution.

Matter essentially rules out certifying any devices that rely on proprietary, non-IP wireless standards. This could limit manufacturers who want to use alternative connectivity methods for their low-end products. While IP-based protocols like Wi-Fi and Ethernet are necessary to interface different ecosystems, non-IP standards still have merit for basic connectivity of sensors and switches in some applications.

Matter bridges have become more common and standardized, allowing manufacturers to maintain their existing non-IP device lines while gaining Matter compatibility through certified bridge products. This approach has proven successful for Zigbee and Z-Wave device ecosystems, where a single bridge can expose multiple legacy devices as Matter endpoints.

## Hardware limitations
<a name="hardware-limitations"></a>

Another challenge is that Matter requires a minimum level of on-device processing power and memory to support the necessary software stack. However, the most basic smart-home devices often have very limited embedded chip capabilities, due to cost and size constraints.

For example, a simple door or window sensor might contain only a microcontroller with less than 100 KB of flash memory and 10 KB of RAM. This does not provide enough storage and processing headroom for a full Matter implementation. Adding more powerful and expensive silicon would drive up the bills of materials significantly.

In cases where cost and size are the top priorities, manufacturers might find Matter requirements do not align with their hardware budgets. Certifying very basic sensors, switches, or controllers with Matter could force unnecessary hardware upgrades that affect affordability.

Matter 1.4.2 (June 2025) introduced improvements to transport reliability and Bluetooth Low Energy (BLE) commissioning that have optimized resource usage. The maturity of the SDK and availability of reference implementations have also reduced the overhead of Matter integration. However, for extremely constrained devices (under 100 KB flash), the gateway proxy approach remains the most practical solution.

## Customer ecosystems
<a name="customer-ecosystems"></a>

Another factor to consider is whether a manufacturer's target customer base uses smart-home platforms that are compatible with Matter. If most consumers in that segment do not use Matter controllers or Matter-enabled hubs and apps, there may be little incentive to certify products.

For example, a company focusing on serving the needs of elderly users might find their customers have simple setups without Matter administrators. Or do-it-yourself (DIY) home automation enthusiasts might prefer custom solutions and don't need Matter's plug-and-play experience across brands.

In scenarios where the target demographic does not engage with Matter infrastructure, certifying adds complexity without clear benefits. Resources might be better spent on optimizing the user experience within the relevant platforms instead of diverting efforts to Matter compliance.

As of 2026, Matter adoption has reached critical mass with major ecosystems (Amazon Alexa, Google Home, Apple HomeKit, Samsung SmartThings) fully supporting the standard. Consumer awareness of Matter has grown significantly, with the Matter logo becoming a recognized mark of interoperability. The target demographic question has shifted from 'Do customers use Matter?' to 'Can we afford not to support Matter?' as it becomes a baseline expectation in many market segments.

## Device types not yet defined
<a name="device-types"></a>

While Matter's scope has expanded dramatically from the initial release, covering most common smart-home categories and many appliances, some niche verticals still await standardization.

If a company develops unique device types that are not covered by existing Matter profiles, certification is not possible until new profiles are drafted. This could delay a new product's launch while waiting for Matter to expand its scope.

Rather than hold off on releasing innovations, some manufacturers might prefer bringing niche solutions to market sooner through proprietary means. Certifying later is still an option after the relevant profiles mature. For first-mover advantages, going direct-to-consumer without Matter might be preferable in some cases.

## An alternative: Proxying at gateways
<a name="gateway-proxying"></a>

In situations where an endpoint device has limitations that prevent direct Matter certification, an alternative approach is to proxy the device's Matter capability at a gateway. The gateway serves as a bridge that translates between the local wireless protocol of the endpoint and the IP-based Matter protocol.

For example, a basic temperature sensor communicating over a proprietary radio standard could still appear as a Matter device to the Matter admin. The gateway receives sensor data on a non-IP interface but exposes virtual Matter entities representing that data over IP to controllers. This allows you to use existing hardware and gain some interoperability benefits through the gateway.

Of course, this adds complexity for developers and requires gateways to support the necessary translation layer. But it might be a viable compromise in cases where direct certification is too challenging for the device itself. Proxies could help low-power or niche solutions participate in Matter ecosystems without a complete hardware overhaul.

The Matter bridge specification has matured, with numerous certified bridge products now available from major manufacturers. This has made the gateway approach more viable and standardized compared to the early days of Matter. Manufacturers can now partner with bridge providers or develop their own certified bridges to bring non-IP devices into the Matter ecosystem without redesigning the endpoint hardware.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
