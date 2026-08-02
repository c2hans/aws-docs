---
source_url: https://docs.aws.amazon.com/whitepapers/latest/best-practices-deploying-amazon-workspaces/scenario-2-extending-on-premises-ad-ds-into-aws-replica.html
---

# Scenario 2: Extending on-premises AD DS into AWS (replica)
<a name="scenario-2-extending-on-premises-ad-ds-into-aws-replica"></a>

 This scenario is similar to scenario 1. However, in this scenario, a replica of the customer AD DS is deployed on AWS in combination with AD Connector. This reduces latency of authentication or query requests to AD DS running on Amazon Elastic Compute Cloud (Amazon EC2). The following figure shows a high-level view of each of the components and the user authentication flow.

![Sample architecture showing a replica of the customer AD DS is deployed on AWS in combination with AD Connector.](http://docs.aws.amazon.com/whitepapers/latest/best-practices-deploying-amazon-workspaces/images/extend-customer-ad-cloud.png)

 As in scenario 1, AD Connector is used for all user or MFA authentication, which in turn is proxied to the customer AD DS (refer to [the previous figure](scenario-1-using-ad-connector-to-proxy-authentication-to-on-premises-active-directory-service.md#fig5)). In this scenario, the customer AD DS is deployed across AZs on Amazon EC2 instances that are promoted to be domain controllers in the customer’s on-premises [AD forest](https://ipwithease.com/what-is-a-forest-in-active-directory/), running in the AWS Cloud. Each domain controller is deployed into VPC private subnets to make AD DS highly available in the AWS Cloud. For best practices for deploying AD DS on AWS, refer to the [Design Considerations](using-multi-region-aws-managed-active-directory-with-amazon-workspaces.md) section of this document.

 After WorkSpaces instances are deployed, they have access to the cloud-based domain controllers for secure, low-latency directory services and DNS. All network traffic, including AD DS communication, authentication requests, and AD replication, is secured either within the private subnets or across the customer VPN tunnel or Direct Connect.

 This architecture uses the following components or constructs:

## AWS
<a name="aws-1"></a>
+  **Amazon VPC** — Creation of an Amazon VPC with at least four private subnets across two AZs — two for the customer AD DS, two for AD Connector or Amazon WorkSpaces.
+  **DHCP Options Set** — Creation of an Amazon VPC DHCP options set. This allows the customer to define a specified domain name and DNSs (AD DS local). For more information, refer to [DHCP Options Sets](https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_DHCP_Options.html).
+  **Amazon Virtual Private Gateway** — Enable communication with a customer-owned network over an IPsec VPN tunnel or AWS Direct Connect connection.
+  **Amazon EC2**
  +  Customer corporate AD DS domain controllers deployed on Amazon EC2 instances in dedicated private VPC subnets.
  +  Customer (optional) RADIUS servers for MFA on Amazon EC2 instances in dedicated private VPC subnets.
+  **AWS Directory Services** — AD Connector is deployed into a pair of Amazon VPC private subnets.
+  **Amazon WorkSpaces** — WorkSpaces are deployed into the same private subnets as the AD Connector. For more information, refer to the [Active Directory: Sites and Services](design-considerations.md#active-directory-sites-and-services) section of this document.

## Customer
<a name="customer-1"></a>
+  **Network connectivity** — Corporate VPN or AWS Direct Connect endpoints.
+  **AD DS** — Corporate AD DS (required for replication).
+  **MFA (optional)** — Corporate RADIUS server.
+  **End user devices** — Corporate or BYOL end user devices (such as Windows, Macs, iPads, Android tablets, zero clients, and Chromebooks) used to access the Amazon WorkSpaces service. Refer to the [list of client applications for supported devices and web browsers](https://docs.aws.amazon.com/workspaces/latest/userguide/workspaces-user-getting-started.html#choose-client). This solution doesn’t have the same caveats as scenario 1. Amazon WorkSpaces and AWS Directory Service have no reliance on the connectivity in place.
+  **Reliance on connectivity** — If connectivity to the customer data center is lost, end users can continue to work because authentication and *optional* MFA are processed locally.
+  **Latency** — With the exception of replication traffic, all authentication is local and low latency. Refer to the [Active Directory: Sites and Services](design-considerations.md#active-directory-sites-and-services) section of this document.
+  **Traffic costs** — In this scenario, authentication is local, with only AD DS replication having to traverse the VPN or Direct Connect link, reducing data transfer.

 In general, the WorkSpaces experience is enhanced and isn’t highly dependent connectivity to the on-premises domain controllers, as shown in the previous figure. This is also the case when a customer wants to scale WorkSpaces to thousands of desktops, especially in relation to AD DS global catalog queries, as this traffic remains local to the WorkSpaces environment.
