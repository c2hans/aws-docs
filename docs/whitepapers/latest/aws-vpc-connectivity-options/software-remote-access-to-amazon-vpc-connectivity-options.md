---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/software-remote-access-to-amazon-vpc-connectivity-options.html
---

# Software remote access-to-Amazon VPC connectivity options
<a name="software-remote-access-to-amazon-vpc-connectivity-options"></a>

 With software remote access VPN, you can leverage low cost, elastic, and secure services to implement remote-access solutions while also providing a seamless experience connecting to AWS hosted resources. This option is typically preferred by smaller companies with less extensive remote networks or who have not already built and deployed remote access solutions for their employees.

 You can combine these patterns with the [Network-to-Amazon VPC connectivity options](network-to-amazon-vpc-connectivity-options.md) connectivity options and [Amazon VPC-to-Amazon VPC connectivity options](amazon-vpc-to-amazon-vpc-connectivity-options.md) to create a network that spans remote networks and multiple VPCs.

 The following table outlines the advantages and limitations of these options.

|  **Option**  |   **Use Case**   |   **Advantages**   |   **Limitations**   |
| --- | --- | --- | --- |
|  [AWS Client VPN](aws-client-vpn.md)  |  AWS managed remote access solution to Amazon VPC and/or internal networks  |  AWS managed high availability and scalability service  |  OpenVPN clients only  |
|  [Software client VPN](software-client-vpn.md)  |  Software VPN appliance remote access solution to Amazon VPC and/or internal networks  |  Supports a wider array of VPN vendors, products, and protocols <br /> Fully customer-managed solution  |  You are responsible for implementing HA solutions  |
