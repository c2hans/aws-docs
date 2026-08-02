---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/neptune-well-architected-framework/security-pillar.html
---

# Security pillar
<a name="security-pillar"></a>

Cloud security at AWS is the highest priority. As an AWS customer, you benefit from a data center and network architecture that is built to meet the requirements of the most security-sensitive organizations.

Security is a shared responsibility between AWS and you. The [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) describes this as security of the cloud and security in the cloud:
+ **Security of the cloud** – AWS is responsible for protecting the infrastructure that runs AWS services in the AWS Cloud. AWS also provides you with services that you can use securely. Third-party auditors regularly test and verify the effectiveness of AWS security as part of the [AWS compliance programs](https://aws.amazon.com/compliance/programs/). To learn about the compliance programs that apply to Amazon Neptune, see [AWS Services in Scope by Compliance Program](https://aws.amazon.com/compliance/services-in-scope/).
+ **Security in the cloud** – Your responsibility is determined by the AWS service that you use. You are also responsible for other factors, including the sensitivity of your data, your company's requirements, and applicable laws and regulations. For more information about data privacy, see the [Data Privacy FAQ](https://aws.amazon.com/compliance/data-privacy-faq). For information about data protection in Europe, see the [AWS Shared Responsibility Model and GDPR](https://aws.amazon.com/blogs/security/the-aws-shared-responsibility-model-and-gdpr/) blog post.

The [security pillar](https://docs.aws.amazon.com/wellarchitected/latest/framework/security.html) helps you understand how to apply the shared responsibility model when using Neptune. The following topics show you how to configure Neptune to meet your security and compliance objectives. You also learn how to use other AWS services that help you to monitor and secure your Neptune resources.

The security pillar includes the following key focus areas:
+ Data security
+ Network security
+ Authentication and authorization

## Implement data security
<a name="data-security"></a>

Data leakage and breaches put your customers at risk and can cause substantial negative impact on your company. The following best practices help protect your customer data from inadvertent and malicious exposure:
+ Cluster names, tags, parameter groups, AWS Identity and Access Management (IAM) roles, and other metadata should not contain confidential or sensitive information because that data might appear in billing or diagnostic logs.
+ URIs or links to external servers stored as data in Neptune should not contain credential information to validate requests.
+ Neptune encrypted instances provide an additional layer of data protection by helping to secure your data from unauthorized access to the underlying storage. You can use Neptune encryption to increase data protection of your applications that are deployed in the cloud. You can also Neptune encryption to fulfill compliance requirements for data at rest.

  To enable encryption for a new Neptune DB instance, choose **Yes** in the **Enable encryption** section on the Neptune console (selected by default), or by setting the [AWS::Neptune::DBCluster::StorageEncrypted](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbcluster.html#cfn-neptune-dbcluster-storageencrypted) property in CloudFormation. If encryption is enabled, Neptune will use the [Amazon Relational Database Service (Amazon RDS) AWS managed key by default](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.Keys.html), or you can create a [customer managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk). For information about creating a Neptune DB instance, see [Creating a new Neptune DB cluster](https://docs.aws.amazon.com/neptune/latest/userguide/get-started-create-cluster.html). For more details, see [Encrypting Neptune Resources at Rest](https://docs.aws.amazon.com/neptune/latest/userguide/encrypt.html). Your automated and manual snapshots use the same encryption that you selected for your Neptune cluster.
+ When using SPARQL and openCypher languages, practice proper input validation and parameterization techniques to prevent SQL injection and other forms of attacks. Avoid constructing queries that use string concatenation with user-supplied input. Use parameterized queries or prepared statements to safely pass input parameters to the graph database. For more information, see [Examples of openCypher parameterized queries](https://docs.aws.amazon.com/neptune/latest/userguide/opencypher-parameterized-queries.html) and [SPARQL Injection Defence](https://owasp.org/www-pdf-archive/Onofri-NapolitanoOWASPDayItaly2012.pdf).
+ For the Gremlin language, use [Gremlin Language Variants](https://tinkerpop.apache.org/docs/3.4.8/tutorials/gremlin-language-variants/#:~:text=A%20Gremlin%20language%20variant%20is,within%20their%20native%20programming%20language.) instead of directly passing string-based Gremlin Scripts to avoid potential injection issues.

## Secure your networks
<a name="network-security"></a>

An Amazon Neptune DB cluster can be created only in a virtual private cloud (VPC) on AWS. Until Neptune 1.4.6.0, the Neptune DB cluster's endpoints were accessible only within that VPC. As of Neptune 1.4.6.0 and later, Neptune instances can be configured to be [publicly accessible over the internet](https://docs.aws.amazon.com/neptune/latest/userguide/neptune-public-endpoints.html). It is a best practice to use this feature only in non-production environments to enable simplified access to Neptune for your developers (though IAM authentication is always required on to enable public accessibility). If you have public accessibility enabled, consider setting inbound security group rules for your database port to only known IP address traffic. In production environments or with clusters containing sensitive data, secure your Neptune data by not allowing public accessibility and limiting access to the VPC where your Neptune DB cluster is located. For more information, see [Connecting to your Amazon Neptune graph](https://docs.aws.amazon.com/neptune/latest/userguide/get-started-connecting.html).

To protect your data in transit, Neptune enforces SSL connections through HTTPS to any instance or cluster endpoint [using secure protocols and ciphers](https://docs.aws.amazon.com/neptune/latest/userguide/security-ssl.html). Neptune provides SSL certificates for your Neptune DB instances. Neptune SSL certificates support only cluster endpoint, reader endpoint, and instance endpoint hostnames.

If you are using a load balancer or a proxy server (such as [HAProxy](https://www.haproxy.org/)), you must use SSL termination and have your own SSL certificate on the proxy server. SSL passthrough doesn't work because the provided SSL certificates don't match the proxy server hostname. For more information about connecting to Neptune endpoints with SSL, see [Using the HTTP REST endpoint to connect to a Neptune DB instance](https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-sparql-http-rest.html).

## Implement authentication and authorization
<a name="authentication-authorization"></a>

To control who can perform Neptune management** **actions on Neptune DB clusters and DB instances, [enable IAM database authentication](https://docs.aws.amazon.com/neptune/latest/userguide/iam-auth-enable.html) and use IAM credentials. When you connect to AWS using IAM credentials, your IAM role must have IAM policies that grant the permissions required to perform Neptune management operations. Ensure that you follow [principle of least privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege), granting only the permissions required to complete a task. For more information, see [Using different kinds of IAM policies for controlling access to Neptune](https://docs.aws.amazon.com/neptune/latest/userguide/security-iam-access-manage.html#iam-auth-policy) and [IAM Authentication Using Temporary Credentials](https://docs.aws.amazon.com/neptune/latest/userguide/iam-auth-temporary-credentials.html).

To control who can connect to a Neptune cluster and query the data, you can use IAM to authenticate to your Neptune DB instance or DB cluster. If you enable IAM authentication in a Neptune DB cluster, anyone accessing the DB cluster must first be authenticated. For more information, see [Enabling IAM database authentication in Neptune](https://docs.aws.amazon.com/neptune/latest/userguide/iam-auth-enable.html) for steps to enable IAM authentication.

When IAM database authentication is enabled, each request must be signed using AWS Signature Version 4. To understand how to send signed requests to all Neptune endpoints with IAM authentication enabled, see [Connecting and Signing with AWS Signature Version 4](https://docs.aws.amazon.com/neptune/latest/userguide/iam-auth-connecting.html). Many libraries and tools, such as [awscurl](https://github.com/okigan/awscurl), already support AWS Signature Version 4.

 For interacting with other AWS services, Amazon Neptune uses IAM[ service-linked roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#iam-term-service-linked-role). A service-linked role is a unique type of IAM role that is linked directly to Neptune. Service-linked roles are predefined by Neptune and include all the permissions that the service requires to call other AWS services on your behalf. For more information, see [Using Service-Linked Roles for Neptune](https://docs.aws.amazon.com/neptune/latest/userguide/security-iam-service-linked-roles.html).
