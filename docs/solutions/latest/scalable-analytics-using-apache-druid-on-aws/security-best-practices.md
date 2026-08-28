---
source_url: https://docs.aws.amazon.com/solutions/latest/scalable-analytics-using-apache-druid-on-aws/security-best-practices.html
---

# Security best practices
<a name="security-best-practices"></a>

This section provides several security features to consider, as you develop and implement your own security policies.

**Note**
The following best practices are general guidelines and do not represent a complete security guidance. These best practices might not be appropriate or sufficient for your specific environment, so treat them as helpful considerations, not prescriptive guidance.

## User authentication and authorization
<a name="user-authentication-and-authorization"></a>

The guidance is configured to utilize basic authentication by default, offering adaptability for additional support such as OIDC and LDAP authentication through configuration settings. However, we advise caution when customizing user authentication and authorization settings.
+ In a production environment, we strongly recommend activating basic authentication at the very least to maintain a baseline security measure.
+ For OIDC authentication, ensuring the accuracy of group and role mapping is essential.
+ When creating Druid roles, adhere to the principle of least privilege to establish a minimum permission security stance.

## Domain and TLS certificate
<a name="domain-and-tls-certificate"></a>

The guidance integrates with [Amazon Route 53](https://aws.amazon.com/route53/) and [AWS Certificate Manager](https://aws.amazon.com/acm/), streamlining the provisioning of a domain and TLS certificate during deployment when a Route53 hosted zone configuration is specified. Alternatively, it provides the flexibility to deploy without Route 53 configuration, allowing for an external domain setup. In this scenario, a default HTTP listener is established using the application load balancer, and traffic will be exposed over HTTP without encryption in transit.

This scenario poses significant security risks, such as the potential for eavesdropping on sensitive information. To address this concern, we highly recommended establishing a custom domain and employ the TLS policy *ELBSecurityPolicy-TLS13-1-2-2021-06* to enhance security by encrypting the data in transit.

Upon completing the external domain setup, it is recommended to configure the TLS certificate ARN along with the domain, and trigger a redeployment of the guidance to implement these changes. This verifies that the application load balancer exposes HTTPS, thereby fortifying communication security through TLS encryption.

## Third-party extensions
<a name="third-party-extensions"></a>

The guidance’s default configuration includes a minimum set of essential extensions to enable core functionalities. Users have the flexibility to tailor the list of extensions that can be loaded into the cluster. It is important for users to assume responsibility for the security of the selected extensions.

To uphold a robust security posture, we strongly advise consistently monitoring for new releases and promptly applying updates, thereby proactively addressing and mitigating any potential vulnerabilities.

## Deploy the guidance into existing VPC
<a name="deploy-the-solution-into-existing-vpc"></a>

The guidance offers the flexibility to deploy into an existing VPC. When opting for this configuration, it is advisable to ensure that the existing VPC is equipped with three distinct types of subnets: public, private, and isolated, spanning across at least two availability zones.

Whether a subnet is public or private refers to whether traffic within the subnet is routed through an internet gateway. Public subnets have a route table entry to the internet through the internet gateway, but private subnets do not have this entry. Isolated subnets have no routes to destinations outside its VPC. For more information about subnet types, refer to the definition of [subnet types](https://docs.aws.amazon.com/vpc/latest/userguide/configure-subnets.html#subnet-types). This strategic subnet arrangement allows for optimal separation of component; the RDS database clusters operate in the isolated subnets, Druid nodes in the private subnets, and the load balancer is positioned in the public subnets. This architecture enhances security and scalability by appropriately isolating different layers of the infrastructure.

## AMI security
<a name="ami-security"></a>

The guidance automatically selects the latest AMI for Amazon Linux 2 in the deployment process. Opting for the most recent AMI ensures that the system benefits from the latest security patches, thereby maintaining an up-to-date and secure environment. This proactive approach aligns with best practices for security and helps safeguard the integrity of the deployed instances. Continuous use of the latest AMI version contributes to a more resilient and well-protected infrastructure.

The guidance also supports the flexibility to bring your own AMI. It is important to ensure that your base AMI adheres to security best practices.
+ Start with a secure and minimal base image, and then apply patches systematically to maintain a secure foundation for your instances.
+ Establish a routine and predictable patching schedule for your AMIs.
+ Regularly check for operating system and software updates, and apply patches in a timely manner to address known vulnerabilities.

## Public and private mode for EKS cluster endpoint
<a name="public-and-private-mode-for-eks-cluster-endpoint"></a>

Amazon EKS offers public-only, public-and-private, and private-only cluster endpoint modes. The default mode is configured to be private-only in the guidance, however we recommend configuring cluster endpoint in public and private mode. This option allows Kubernetes API calls within your cluster’s VPC (such as node-to-control-plane communication) to use the private VPC endpoint and traffic to remain within your cluster’s VPC.

You can access your cluster API server from the internet. However, we strongly recommend limiting the CIDR blocks that can use the public endpoint. Learn how to configure public and private endpoint access, including limiting CIDR blocks. For more guidance on how to secure the EKS clusters, refer to the [EKS best practices](https://aws.github.io/aws-eks-best-practices/security/docs/) topic.

## EKS master IAM role
<a name="eks-master-iam-role"></a>

For EKS deployment, the guidance requires the user to supply an ARN for the EKS master role. This role, serving as the IAM principal responsible for creating the cluster, is automatically endowed with `system:masters` permissions within the cluster’s Role-Based Access Control (RBAC) configuration in the Amazon EKS control panel. For more guidance on how to secure the access for this role, refer to the [EKS best practices](https://aws.github.io/aws-eks-best-practices/security/docs/iam/#create-the-cluster-with-a-dedicated-iam-role) topic.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Guidance for Scalable Analytics Using Apache Druid on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
