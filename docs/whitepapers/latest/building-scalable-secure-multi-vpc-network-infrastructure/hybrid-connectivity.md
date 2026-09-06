---
source_url: https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/hybrid-connectivity.html
---

# Hybrid connectivity
<a name="hybrid-connectivity"></a>

 This section focuses on securely connecting your cloud resources with your on-premises data centers. There are three approaches for enabling hybrid connectivity:
+  **One-to-one connectivity** — In this setup, a VPN connection and/or Direct Connect private VIF is created for every VPC. This is accomplished by using the virtual private gateway (VGW). This option is great for small numbers of VPCs, but as a customer scales their VPCs, managing hybrid connectivity per VPC can become difficult.
+  **Edge consolidation** — In this setup, customers consolidate hybrid IT connectivity for multiple VPCs at a single endpoint. All the VPCs share these hybrid connections. This is accomplished by using AWS Transit Gateway and the Direct Connect gateway.
+  **Full mesh hybrid consolidation** — In this setup, customers consolidate connectivity for multiple VPCs at a single endpoint using CloudWAN, built on AWS Transit Gateway. This is a full policy-based approach to networking in one or more AWS accounts, represented in code. At this time, using Direct Connect for edge connectivity requires peering Transit Gateway to CloudWAN.
