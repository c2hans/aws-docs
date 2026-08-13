---
source_url: https://docs.aws.amazon.com/whitepapers/latest/build-static-websites-aws/moving-to-an-aws-architecture.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Moving to an AWS architecture
<a name="moving-to-an-aws-architecture"></a>

 To translate a traditional hosting environment to an AWS architecture, you could use a “lift- and-shift” approach where you substitute AWS services instead of using the traditional environment.

 In this approach, you can substitute the following AWS services:
+  [Amazon Elastic Compute Cloud](https://aws.amazon.com/ec2) (Amazon EC2) to run Linux or Windows based servers
+  [Elastic Load Balancing](https://aws.amazon.com/elasticloadbalancing) (ELB) to load balance and distribute the web traffic.
+  [Amazon Elastic Block Store](https://aws.amazon.com/ebs) (Amazon EBS) or [Amazon Elastic File System](https://aws.amazon.com/efs) (Amazon EFS) to store static content.
+  [Amazon Virtual Private Cloud](https://aws.amazon.com/vpc) (Amazon VPC) to deploy Amazon EC2 instances. Amazon VPC is your isolated and private virtual network in the AWS Cloud and gives you full control over the network topology, firewall configuration, and routing rules.
+  Web servers can be spread across multiple [Availability Zones](https://aws.amazon.com/about-aws/global-infrastructure/) for high availability, even if an entire data center were to be down.
+  [*AWS Auto Scaling*](https://aws.amazon.com/autoscaling) automatically adds servers during high traffic periods and scales back when traffic decreases.

 The following diagram shows the basic architecture of a “lift and shift” approach.

![A diagram depicting AWS architecture for a lift and shift.](http://docs.aws.amazon.com/whitepapers/latest/build-static-websites-aws/images/lift-and-shift.png)

 Using this AWS architecture, you gain the security, scalability, cost, and agility benefits of running in AWS. This architecture benefits from AWS world-class infrastructure and security operations. By using Auto Scaling, the website is ready for traffic spikes, so you are prepared for product launches and viral websites. With AWS, you only pay for what you use, and there’s no need to over-provision for peak capacity. In addition, you gain increased agility because AWS services are available on demand. (Compare this to the traditional process in which provisioning servers, storage, or networking can take weeks.) You don’t have to manage infrastructure, so this frees up time and resources to create business differentiating value.

 AWS challenges traditional IT assumptions and enables new “cloud-native” architectures. You can architect a modern static website without needing a single webserver.
