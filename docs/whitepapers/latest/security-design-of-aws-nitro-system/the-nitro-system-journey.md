---
source_url: https://docs.aws.amazon.com/whitepapers/latest/security-design-of-aws-nitro-system/the-nitro-system-journey.html
---

# The Nitro System journey
<a name="the-nitro-system-journey"></a>

 The Nitro System is the product of a multi-year journey of re-imagining virtualization technology for AWS Cloud infrastructure. Over the course of this journey, every component of virtualization technology was re-implemented and replaced. While customers saw improved cost, performance, and security from EC2 instances released earlier in this process, [instances based on the resulting complete Nitro System](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html#ec2-nitro-instances), in which every component has been replaced, are meaningfully different from those prior instance types. The Nitro System provides enhanced security, confidentiality, and performance to customers of Amazon EC2, and provides a foundation that enables the delivery of new innovative technologies at a rapid pace.

 The introduction of the Nitro System consisted of an incremental decomposition of the software components running in Dom0 on a general-purpose data center CPU into independent purpose-built service processor units. What started as a tightly coupled monolithic virtualization system was, step by step, transformed into a purpose-built microservices architecture. Starting with the C5 instance type introduced in 2017, the Nitro System has entirely eliminated the need for Dom0 on an EC2 instance. Instead, a custom-developed, minimized hypervisor based on [KVM](https://www.linux-kvm.org/page/Main_Page) provides a lightweight VMM, while offloading other functions such as those previously performed by the device-models in Dom0 into a set of discrete Nitro Cards.

![A diagram depicting Nitro System virtualization architecture.](http://docs.aws.amazon.com/whitepapers/latest/security-design-of-aws-nitro-system/images/nitro-system-architecture.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
