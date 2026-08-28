---
source_url: https://docs.aws.amazon.com/whitepapers/latest/device-manufacturing-provisioning/the-device-manufacturing-supply-chain.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# The device manufacturing supply chain
<a name="the-device-manufacturing-supply-chain"></a>

![A diagram that shows the IoT device manufacturing process.](http://docs.aws.amazon.com/whitepapers/latest/device-manufacturing-provisioning/images/device-manufacturing.png)

 As an IoT project moves from a development phase to production, a supply chain is necessary between the device maker through to the customer.

 Device makers specify the components, form factor, and functionality of a device. Device makers are also responsible for product design, developing hardware and software for products, developing and maintaining AWS Cloud applications, provisioning templates, policies, and resources, and the sales and marketing of the product. Most device makers do not have the ability to physically manufacture a large number of devices, and must outsource this manufacturing to a contract manufacturer.

 During the prototyping stage, device makers might use high-mix, low-volume contract manufacturing to rapidly produce engineering samples in low volumes. When moving from the prototyping to production phase, a high-volume contract manufacturer is used to take advantage of the economy of scale.

 Low-mix, high-volume contract manufacturers have the production line, tooling, and processes in place to produce a large volume of devices. Contract manufacturers build devices to the specification provided by the device maker. This specification includes printed circuit board (PCB) schematics, a bill of materials, and the firmware that is loaded onto the device. Contract manufacturers place components onto PCBs ([pick and place](https://en.wikipedia.org/wiki/Pick-and-place_machine)), program the processors with firmware and credentials provided by the device makers, and package the devices into a final product. Products are then provided to distribution channels to fulfill sales. Contract manufacturers must source the individual components to build the final product from their supply chain.

 After the device is built, it can be sent to the device maker for direct distribution or engineering samples. The devices can also be sent directly to distributors or retailers who sell the device and fulfill the supply chain to end customers.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
