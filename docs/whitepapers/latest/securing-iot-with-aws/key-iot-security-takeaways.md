---
source_url: https://docs.aws.amazon.com/whitepapers/latest/securing-iot-with-aws/key-iot-security-takeaways.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Key IoT security takeaways
<a name="key-iot-security-takeaways"></a>

 Despite the number of best practices available, there is no one-size-fits-all approach to mitigating the risks to IoT solutions. Depending on the device, system, service, and environment in which the devices are deployed, different threats, vulnerabilities, and risk tolerances exist for customers to consider. Here are key takeaways to help incorporate complete security across data, devices, and cloud services:

1.  **Incorporate security in the design phase.**

    The foundation of an IoT solution starts and ends with security. Because devices may send large amounts of sensitive data, and end users of IoT applications may also have the ability to directly control a device, the security of *things* must be a pervasive design requirement. Security is not a static formula; IoT applications must be able to continuously model, monitor, and iterate on security best practices.

    A challenge for IoT security is the lifecycle of a physical device and the constrained hardware for sensors, microcontrollers, actuators, and embedded libraries. These constrained factors may limit the security capabilities each device can perform. With these additional dynamics, IoT solutions must continuously adapt their architecture, firmware, and software to stay ahead of the changing security landscape. Although the constrained factors of devices can present increased risks, hurdles, and potential tradeoffs between security and cost, building a secure IoT solution must be the primary objective for any organization.

1.  **Build on recognized IT security and cybersecurity frameworks.**

    AWS supports an open, standards-based approach to promote secure IoT adoption. When considering the billions of devices and connection points necessary to support a robust IoT ecosystem for consumer, industrial, and public sector use, interoperability is vital. Thus, AWS IoT services adhere to industry standard protocols and best practices. Additionally, AWS IoT Core supports other industry-standard and custom protocols, allowing devices to communicate with each other even if they are using different protocols. AWS is a strong proponent of interoperability so that developers can build on top of existing platforms to support evolving customer needs. AWS also supports a thriving partner ecosystem to expand the menu of choices and stretch the limits of what is possible for customers. Applying globally recognized best practices carries a number of benefits across all IoT stakeholders including:
   +  Repeatability and reuse, instead of re-starting and re-doing
   +  Consistency and consensus to promote the compatibility of technology and interoperability across geographical boundaries
   +  Maximizing efficiencies to accelerate IT modernization and transformation

1.  **Focus on impact to prioritize security measures.**

    Attacks or abnormalities are not identical and may not have the same impact on people, business operations, and data. Understanding customer IoT ecosystems and where devices will operate within this ecosystem informs decisions on where the greatest security risks are—within the device as part of the network or physical component. Focusing on the risk impact assessment and consequences is critical for determining where security efforts should be directed along with who is responsible for those efforts in the IoT ecosystem.

1.  **Start with using zero-trust security principles.**

    Zero-trust principles are intended for an organization’s infrastructure, which includes operational technology (OT), IT systems, IoT, and Industrial Internet of Things (IIoT). Traditional security models rely heavily on network segmentation and give high levels of trust to devices based on their network presence. In comparison, zero trust requires your users, devices, and systems to prove their trustworthiness, and it enforces fine-grained, identity-based rules that govern access to applications, data, and other assets. AWS provides guidance on [how to implement zero trust IoT solutions with AWS IoT](https://aws.amazon.com/blogs/iot/how-to-implement-zero-trust-iot-solutions-with-aws-iot-3/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
