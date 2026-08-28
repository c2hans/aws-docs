---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-10-03/framework/sec_network_protection_create_layers.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SEC05-BP01 Create network layers
<a name="sec_network_protection_create_layers"></a>

Group components that share sensitivity requirements into layers to minimize the potential scope of impact of unauthorized access. For example, a database cluster in a virtual private cloud (VPC) with no need for internet access should be placed in subnets with no route to or from the internet. Traffic should only flow from the adjacent next least sensitive resource. Consider a web application sitting behind a load balancer. Your database should not be accessible directly from the load balancer. Only the business logic or web server should have direct access to your database.

 **Desired outcome:** Create a layered network. Layered networks help logically group similar networking components. They also shrink the potential scope of impact of unauthorized network access. A properly layered network makes it harder for unauthorized users to pivot to additional resources within your AWS environment. In addition to securing internal network paths, you should also protect your network edge, such as web applications and API endpoints.

 **Common anti-patterns:**
+  Creating all resources in a single VPC or subnet.
+  Using overly permissive security groups.
+  Failing to use subnets.
+  Allowing direct access to data stores such as databases.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>

 Components such as Amazon Elastic Compute Cloud (Amazon EC2) instances, Amazon Relational Database Service (Amazon RDS) database clusters, and AWS Lambda functions that share reachability requirements can be segmented into layers formed by subnets. Consider deploying serverless workloads, such as [Lambda](https://docs.aws.amazon.com/lambda/index.html) functions, within a VPC or behind an [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html). [AWS Fargate](https://aws.amazon.com/fargate/getting-started/) tasks that have no need for internet access should be placed in subnets with no route to or from the internet. This layered approach mitigates the impact of a single layer misconfiguration, which could allow unintended access. For AWS Lambda, you can run your functions in your VPC to take advantage of VPC-based controls.

 For network connectivity that can include thousands of VPCs, AWS accounts, and on-premises networks, you should use [AWS Transit Gateway](https://aws.amazon.com/transit-gateway/). Transit Gateway acts as a hub that controls how traffic is routed among all the connected networks, which act like spokes. Traffic between Amazon Virtual Private Cloud (Amazon VPC) and Transit Gateway remains on the AWS private network, which reduces external exposure to unauthorized users and potential security issues. Transit Gateway Inter-Region peering also encrypts inter-Region traffic with no single point of failure or bandwidth bottleneck.

 **Implementation steps**
+  **Use [Reachability Analyzer](https://docs.aws.amazon.com/vpc/latest/reachability/how-reachability-analyzer-works.html) to analyze the path between a source and destination based on configuration:** Reachability Analyzer allows you to automate verification of connectivity to and from VPC connected resources. Note that this analysis is done by reviewing configuration (no network packets are sent in conducting the analysis).
+  **Use [Amazon VPC Network Access Analyzer](https://docs.aws.amazon.com/vpc/latest/network-access-analyzer/what-is-network-access-analyzer.html) to identify unintended network access to resources:** Amazon VPC Network Access Analyzer allows you to specify your network access requirements and identify potential network paths.
+  **Consider whether resources need to be in a public subnet:** Do not place resources in public subnets of your VPC unless they absolutely must receive inbound network traffic from public sources.
+  **Create [subnets in your VPCs](https://docs.aws.amazon.com/vpc/latest/userguide/how-it-works.html):** Create subnets for each network layer (in groups that include multiple Availability Zones) to enhance micro-segmentation. Also verify that you have associated the correct [route tables](https://docs.aws.amazon.com/vpc/latest/userguide/how-it-works.html) with your subnets to control routing and internet connectivity.
+  **Use [AWS Firewall Manager](https://docs.aws.amazon.com/waf/latest/developerguide/security-group-policies.html) to manage your VPC security groups:** AWS Firewall Manager helps lessen the management burden of using multiple security groups.
+  **Use [AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html) to protect against common web vulnerabilities:** AWS WAF can help enhance edge security by inspecting traffic for common web vulnerabilities, such as SQL injection. It also allows you to restrict traffic from IP addresses originating from certain countries or geographical locations.
+  **Use [Amazon CloudFront](https://docs.aws.amazon.com/cloudfront/index.html) as a content distribution network (CDN):** Amazon CloudFront can help speed up your web application by storing data closer to your users. It can also improve edge security by enforcing HTTPS, restricting access to geographic areas, and ensuring that network traffic can only access resources when routed through CloudFront.
+  **Use [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html) when creating application programming interfaces (APIs):** Amazon API Gateway helps publish, monitor, and secure REST, HTTPS, and WebSocket APIs.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [AWS Firewall Manager](https://docs.aws.amazon.com/waf/latest/developerguide/fms-chapter.html)
+ [ Amazon Inspector ](https://aws.amazon.com/inspector)
+  [Amazon VPC Security](https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Security.html)
+ [ Reachability Analyzer ](https://docs.aws.amazon.com/vpc/latest/reachability/what-is-reachability-analyzer.html)
+ [ Amazon VPC Network Access Analyzer ](https://docs.aws.amazon.com/vpc/latest/network-access-analyzer/getting-started.html#run-analysis)

 **Related videos:**
+  [AWS Transit Gateway reference architectures for many VPCs ](https://youtu.be/9Nikqn_02Oc)
+  [Application Acceleration and Protection with Amazon CloudFront, AWS WAF, and AWS Shield](https://youtu.be/0xlwLEccRe0)
+ [AWS re:Inforce 2022 - Validate effective network access controls on AWS](https://www.youtube.com/watch?v=aN2P2zeQek0)
+ [AWS re:Inforce 2022 - Advanced protections against bots using AWS WAF](https://www.youtube.com/watch?v=pZ2eftlwZns)

 **Related examples:**
+  [Well-Architected Lab - Automated Deployment of VPC](https://www.wellarchitectedlabs.com/Security/200_Automated_Deployment_of_VPC/README.html)
+ [ Workshop: Amazon VPC Network Access Analyzer ](https://catalog.us-east-1.prod.workshops.aws/workshops/cf2ecaa4-e4be-4f40-b93f-e9fe3b1c1f64)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
