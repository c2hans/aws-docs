---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/sec_network_protection_create_layers.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SEC05-BP01 Create network layers
<a name="sec_network_protection_create_layers"></a>

 Group components that share reachability requirements into layers. For example, a database cluster in a virtual private cloud (VPC) with no need for internet access should be placed in subnets with no route to or from the internet. In a serverless workload operating without a VPC, similar layering and segmentation with microservices can achieve the same goal.

Components such as Amazon Elastic Compute Cloud (Amazon EC2) instances, Amazon Relational Database Service (Amazon RDS) database clusters, and AWS Lambda functions that share reachability requirements can be segmented into layers formed by subnets. For example, an Amazon RDS database cluster in a VPC with no need for internet access should be placed in subnets with no route to or from the internet. This layered approach for the controls mitigates the impact of a single layer misconfiguration, which could allow unintended access. For Lambda, you can run your functions in your VPC to take advantage of VPC-based controls.

For network connectivity that can include thousands of VPCs, AWS accounts, and on-premises networks, you should use [AWS Transit Gateway](http://aws.amazon.com/transit-gateway). It acts as a hub that controls how traffic is routed among all the connected networks, which act like spokes. Traffic between an Amazon Virtual Private Cloud and AWS Transit Gateway remains on the AWS private network, which reduces external threat vectors such as distributed denial of service (DDoS) attacks and common exploits, such as SQL injection, cross-site scripting, cross-site request forgery, or abuse of broken authentication code. AWS Transit Gateway inter-region peering also encrypts inter-region traffic with no single point of failure or bandwidth bottleneck.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>
+  Create subnets in VPC: Create subnets for each layer (in groups that include multiple Availability Zones), and associate route tables to control routing.
  +  [VPCs and subnets ](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html)
  +  [Route tables ](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html)

## Resources
<a name="resources"></a>

 **Related documents:**
+  [AWS Firewall Manager](https://docs.aws.amazon.com/waf/latest/developerguide/fms-chapter.html)
+ [ Amazon Inspector ](https://aws.amazon.com/inspector)
+  [Amazon VPC Security](https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Security.html)
+  [Getting started with AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/getting-started.html)

 **Related videos:**
+  [AWS Transit Gateway reference architectures for many VPCs ](https://youtu.be/9Nikqn_02Oc)
+  [Application Acceleration and Protection with Amazon CloudFront, AWS WAF, and AWS Shield](https://youtu.be/0xlwLEccRe0)

 **Related examples:**
+  [Lab: Automated Deployment of VPC](https://www.wellarchitectedlabs.com/Security/200_Automated_Deployment_of_VPC/README.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
