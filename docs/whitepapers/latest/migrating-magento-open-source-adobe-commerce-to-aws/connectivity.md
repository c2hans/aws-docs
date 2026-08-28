---
source_url: https://docs.aws.amazon.com/whitepapers/latest/migrating-magento-open-source-adobe-commerce-to-aws/connectivity.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Connectivity
<a name="connectivity"></a>

 The migration of Magento Open Source or Adobe Commerce on Cloud Infrastructure Self-Service might be part of an enterprise cloud adoption strategy, driven by a compelling event or a combination of the two. Regardless of the reasons, make sure to consider systems dependent on Magento Open Source or Adobe Commerce on Cloud Infrastructure Self-Service and vice versa. Connectivity between the Magento Open Source or Adobe Commerce on Cloud Infrastructure Self-Service systems running in AWS and these dependent systems (whether in AWS, a data center, or a SaaS/PaaS provider) is key to planning and successfully running a migration. Make sure to also consider connectivity for the Magento administrator, system administrator, database administrator, and infrastructure administrator.

## Types of connectivity
<a name="types-of-connectivity"></a>

 Five connectivity channels are available in AWS:
+  API (serverless resources such as Amazon S3, Amazon DynamoDB, etc.)
+  Internet (publicly routed, typically brokered via SFTP based automation)
+  VPN (IPSEC/B2B)
+  AWS Direct Connect (Dedicated connectivity, via either a physical or logical connection)
+  Intra VPC (typically environment:tier <-> environment:tier),
+  Inter VPC (via Peering or Transit Gateway) and AWS PrivateLink (typically private connectivity, AWS based SaaS offerings).

 Whether your connectivity is between tiers, environments, other services within your enterprise on and off AWS or with an AWS Partner, each of these approaches has advantages and disadvantages associated with them.

### Network dependencies
<a name="network-dependencies"></a>

 Of most importance, however, is fully understanding the network dependency map that exists within your Magento Open Source or Adobe Commerce on Cloud Infrastructure Self-Service environment ahead of migration. Having a dependency map can help better plan the steps required in the migration and avoid accelerated post migration changes required to account for missed dependencies, both building to support a successful migration.

 Investigation around this might begin with reviewing load balancer and firewall configurations as they relate to hostnames and IP addresses of the servers Magento Open Source or Adobe Commerce on Cloud Infrastructure Self-Service is running on, its related service configurations and any associated logs – particularly load balancer, firewall, and application performance management (APM) logs which may provide hints around third-party services not otherwise discoverable.

### Service congruency
<a name="service-congruency"></a>

 For example, a typical Magento Open Source or Adobe Commerce on Cloud Infrastructure Self-Service environment is likely accessed from the internet via a load balancing appliance or a firewall providing NAT public IP address space, and may have integrations to other internet-based services (for example, a web service offered by a payment processor or shipping company) as well as legacy integrations via SFTP or a similar internet-based file sharing service.

 These legacy integrations described earlier would translate into AWS services in the way of an Application Load Balancer on one set of subnets protected via a security group and web application firewall, to a fleet of EC2 instances running Magento Open Source or Adobe Commerce on Cloud Infrastructure Self-Service dependent services. A NAT gateway providing outbound access to internet-based services. Same or separate fleet of EC2 instances for providing integration with other internet services such as payment processors, or leverage serverless solutions such AWS lambda and [AWS Transfer for SFTP](https://aws.amazon.com/sftp/) for Amazon S3 based on the use-case.

![Reference architecture diagram showing service congruencies for containers](http://docs.aws.amazon.com/whitepapers/latest/migrating-magento-open-source-adobe-commerce-to-aws/images/reference-architecture-magento-congruencies.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
