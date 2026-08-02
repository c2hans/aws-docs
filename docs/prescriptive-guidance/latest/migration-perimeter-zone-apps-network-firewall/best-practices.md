---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-perimeter-zone-apps-network-firewall/best-practices.html
---

# Best practices
<a name="best-practices"></a>

We recommend the following best practices for migrating your perimeter zone applications to the AWS Cloud:
+ Design your target architecture to support third-party network firewalls, only if you can expose the firewalls to the application VPC network over a Gateway Load Balancer.
+ Use a trusted network to secure the traffic flow between your AWS application's VPC and your on-premises environment. You can build a trusted network by using [AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html) or [AWS Site-to-Site VPN](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html).
+ Use your target architecture to expose web applications to untrusted networks, but avoid using it with an API.
+ Use [VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html) during the testing phase. This is because there can be multiple interconnected components that require the correct configuration and verification.
+ Validate the inbound and outbound rules required for each application and their availability in Network Firewall during the design phase of the migration.
+ If an external AWS service such as Amazon Simple Storage Service (Amazon S3) or Amazon DynamoDB is required, then we recommend exposing that service to the application VPC through endpoints (within the endpoint's subnet). This prevents communication over the untrusted network.
+ Provide access to the resources (Amazon EC2, in this case) through [AWS Systems Manager Session Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html) to avoid direct SSH access to the resources.
+ The Application Load Balancer provides high availability to the application and the routing of incoming and outgoing traffic by using Network Firewall. No separate load balancer for the security subnet is required.
+ Keep in mind that the Application Load Balancer is an internet-facing load balancer, even though the endpoint's subnet doesn't have direct internet access. There is no internet gateway on **Route table endpoint A **and **Route table endpoint B** in the diagram from the *Perimeter zone architecture based on Network Firewall* section of this guide. The subnet is protected by Network Firewall and has internet access through Network Firewall.
+ Use Network Firewall to provide inbound and outbound web filtering for unencrypted web traffic.
