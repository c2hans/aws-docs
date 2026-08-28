---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/sec_protect_data_transit_encrypt.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SEC09-BP02 Enforce encryption in transit
<a name="sec_protect_data_transit_encrypt"></a>

 Enforce your defined encryption requirements based on appropriate standards and recommendations to help you meet your organizational, legal, and compliance requirements. AWS services provide HTTPS endpoints using TLS for communication, thus providing encryption in transit when communicating with the AWS APIs. Insecure protocols, such as HTTP, can be audited and blocked in a VPC through the use of security groups. HTTP requests can also be [automatically redirected to HTTPS](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-https-viewers-to-cloudfront.html) in Amazon CloudFront or on an [Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-listeners.html#redirect-actions). You have full control over your computing resources to implement encryption in transit across your services. Additionally, you can use VPN connectivity into your VPC from an external network to facilitate encryption of traffic. Third-party solutions are available in the AWS Marketplace, if you have special requirements.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>
+  Enforce encryption in transit: Your defined encryption requirements should be based on the latest standards and best practices and only allow secure protocols. For example, only configure a security group to allow HTTPS protocol to an application load balancer or Amazon Elastic Compute Cloud (Amazon EC2) instance.
+  Configure secure protocols in edge services: Configure HTTPS with Amazon CloudFront and required ciphers.
  + [ Using HTTPS with CloudFront ](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-https.html)
+  Use a VPN for external connectivity: Consider using an IPsec virtual private network (VPN) for securing point-to-point or network-to-network connections to provide both data privacy and integrity.
  + [ VPN connections ](https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/vpn-connections.html)
+  Configure secure protocols in load balancers: Enable HTTPS listener for securing connections to load balancers.
  + [ HTTPS listeners for your application load balancer ](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-https-listener.html)
+  Configure secure protocols for instances: Consider configuring HTTPS encryption on instances.
  + [ Tutorial: Configure Apache web server on Amazon Linux 2 to use SSL/TLS ](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/SSL-on-an-instance.html)
+  Configure secure protocols in Amazon Relational Database Service (Amazon RDS): Use secure socket layer (SSL) or transport layer security (TLS) to encrypt connection to database instances.
  + [ Using SSL to encrypt a connection to a DB Instance ](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL.html)
+  Configure secure protocols in Amazon Redshift: Configure your cluster to require an secure socket layer (SSL) or transport layer security (TLS) connection.
  + [ Configure security options for connections ](https://docs.aws.amazon.com/redshift/latest/mgmt/connecting-ssl-support.html)
+  Configure secure protocols in additional AWS services For the AWS services you use, determine the encryption-in-transit capabilities.

## Resources
<a name="resources"></a>

 **Related documents:**
+ [AWS documentation ](https://docs.aws.amazon.com/index.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
