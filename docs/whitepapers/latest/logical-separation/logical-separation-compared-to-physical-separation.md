---
source_url: https://docs.aws.amazon.com/whitepapers/latest/logical-separation/logical-separation-compared-to-physical-separation.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Logical Separation Compared to Physical Separation
<a name="logical-separation-compared-to-physical-separation"></a>

 Customers can leverage some or all aspects of the AWS capabilities below to meet or exceed the security of their on-premises physical separation requirements.
+  **Unified authentication and authorization** – A robust and granular authentication and authorization model common across all AWS services that integrates with on-premises user identity management systems.
+  **Rich monitoring and logging** – Deep and granular logging services for visibility of all API calls and resource state across AWS services. Current configuration and application events are logged in a centralized fashion to quickly understand both current security posture as well as a record of previous configuration states.
+  **Virtual private cloud (VPC) and accompanying features** — VPC is a software-defined network that allows customers to create segmented or micro-segmented network domains to isolate traffic flow between different compute environments and AWS services as well as to join together segments when needed in safe and limited ways.
+  **Encrypting data at-rest and in-transit** — Encryption options for all AWS storage services, powerful certificate creation and lifecycle management for encrypting data in transit. Key management via [AWS Key Management Service (AWS KMS)](https://aws.amazon.com/kms) or optionally using [AWS CloudHSM](https://aws.amazon.com/cloudhsm/) for key generation and storage.
+  **Host and instance isolation** — Options to provision dedicated hypervisor-enabled or bare-metal architectures to maintain customer data on a physical compute host is not shared with others.
+  **Serverless and container architecture** — Isolated execution environments offer a smaller, ephemeral runtime environment to simplify security controls.

**Topics**
+ [Unified Authentication and Authorization Mechanisms](unified-authentication-and-authorization-mechanisms.md)
+ [Rich Monitoring and Logging](rich-monitoring-and-logging.md)
+ [VPC and Accompanying Features](vpc-and-accompanying-features.md)
+ [Encrypting Data-at-Rest and Data-in-Transit](encrypting-data-at-rest-and--in-transit.md)
+ [Host and Instance Features](host-and-instance-features.md)
+ [Serverless and Containers](serverless-and-containers.md)
