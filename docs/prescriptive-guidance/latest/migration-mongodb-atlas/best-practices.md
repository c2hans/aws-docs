---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-mongodb-atlas/best-practices.html
---

# Best practices
<a name="best-practices"></a>

## Provisioning and CI/CD automation
<a name="ci-cd"></a>

MongoDB Atlas is available for provisioning through AWS Marketplace. You can subscribe to the [pay-as-you-go MongoDB Atlas option](https://aws.amazon.com/marketplace/pp/prodview-pp445qepfdy34) to pay through AWS without any upfront commitments. Choosing the [Atlas free-forever tier](https://www.mongodb.com/pricing) provides a free starting point and the ability to scale as required. For more information about these options, see the blog post [Introducing Pay as You Go MongoDB Atlas on AWS Marketplace](https://www.mongodb.com/blog/post/introducing-pay-as-you-go-mongodb-atlas-aws-marketplace) on the MongoDB website.

You can deploy MongoDB Atlas infrastructure resources by using CloudFormation templates and the AWS Cloud Development Kit (AWS CDK). This approach facilitates continuous integration and continuous delivery (CI/CD) automation. For more information, see the blog post [MongoDB Atlas Integrations for CloudFormation and CDK are now Generally Available](https://www.mongodb.com/blog/post/atlas-integrations-aws-cloud-formation-cdk-now-generally-available) on the MongoDB website.

## Security
<a name="security"></a>

You can connect to MongoDB Atlas from AWS services through a secured private network with multiple authentication options:
+ Configure connectivity between your databases and AWS services by using VPC peering or AWS PrivateLink.
+ Implement SAML 2.0 authentication by using [AWS IAM Identity Center](https://aws.amazon.com/iam/identity-center/).
+ Use integrated authentication by using [AWS Identity and Access Management (IAM).](https://www.mongodb.com/docs/atlas/security/passwordless-authentication/)
+ Use integrated security credentials with [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html) and [AWS Key Management Service (AWS KMS)](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html).

The following sections describe these integrations in more detail.

### Private network connectivity
<a name="private-network-connectivity.f81b4505-2e99-5c35-a475-124c4b715396"></a>

You can use AWS PrivateLink to connect MongoDB Atlas to your AWS applications and ensure private connectivity among all your AWS services and accounts. For more information, see the blog post [MongoDB Atlas Integrations for CloudFormation and CDK are now Generally Available](https://www.mongodb.com/blog/post/atlas-integrations-aws-cloud-formation-cdk-now-generally-available) on the MongoDB website.

The following diagram illustrates the private network connectivity option.

![Integrating MongoDB Atlas with AWS PrivateLink, for private network connectivity.](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-mongodb-atlas/images/guide-img/2acef6bf-a074-43c2-a021-70385dda418f/images/af2a19b7-a894-4383-9552-fbd0bcce716d.png)

AWS PrivateLink provides these benefits:
+ One-way connection: no extension of the network trust boundary.
+ Consolidated security controls across AWS applications and environments through private networking.
+  Ability to use a virtual private network (VPN) in conjunction with either VPC peering or PrivateLink, for developers who want to access Atlas from AWS environments.

### Implementing SAML 2.0 authentication
<a name="implementing-saml-2.0-authentication.c448fa3a-43e9-5424-a555-e3b46e1b8771"></a>

Atlas supports SAML 2.0 authentication through integration with IAM Identity Center and other identity management providers. SAML 2.0 authentication is an open standard for exchanging identity and security information between applications and service providers. Atlas administrators can centralize user management and single sign-on by using identity management services such as IAM Identity Center or existing corporate directory services. The following diagram shows how you can use IAM Identity Center with Atlas. For more information, see the AWS blog post [How to Integrate AWS Single Sign-On with MongoDB Atlas](https://aws.amazon.com/blogs/apn/how-to-integrate-aws-single-sign-on-with-mongodb-atlas/).

![Integrating MongoDB Atlas with IAM Identity Center, to implement SAML authentication.](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-mongodb-atlas/images/guide-img/2acef6bf-a074-43c2-a021-70385dda418f/images/50910bee-d6d5-437b-9b6d-eac08e303e07.png)

[AWS Partner Network Blog](https://aws.amazon.com/blogs/apn/tag/mongodb-atlas/)

For additional best practices for using MongoDB Atlas on AWS, see .
