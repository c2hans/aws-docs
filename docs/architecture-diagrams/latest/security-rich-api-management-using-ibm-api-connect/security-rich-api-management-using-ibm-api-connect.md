---
source_url: https://docs.aws.amazon.com/architecture-diagrams/latest/security-rich-api-management-using-ibm-api-connect/security-rich-api-management-using-ibm-api-connect.html
---

# Security-rich API Management Using IBM API Connect on AWS
<a name="security-rich-api-management-using-ibm-api-connect"></a>

Publication date: **October 26, 2023 ([Diagram history](#diagram-history))**

Take advantage of agility, security, and elasticity to create, manage, secure, and socialize all of your APIs across the cloud in order to power digital applications with a market-leading and scalable API management solution.

## Security-rich API Management Using IBM API Connect on AWS Diagram
<a name="diagram1"></a>

![Reference architecture diagram showinghow to take advantage of agility, security, and elasticity to create, manage, secure, and socialize all of your APIs across the cloud in order to power digital applications with a market-leading and scalable API management solution.](http://docs.aws.amazon.com/architecture-diagrams/latest/security-rich-api-management-using-ibm-api-connect/images/security-rich-api-management-using-ibm-api-connect.png)

1.  The API developer creates API endpoints, specifies access controls, and publishes the APIs to the developer portal for external discovery by app developers using IBM API Connect.

1.  An application developer can access the API Connect developer portal to search and discovers APIs.

1.  API calls can be authorized using different authentication and authorization mechanisms, such as OAuth providers or a user registry.

1.  API Connect can be integrated with Stripe Billing to monetize APIs, generate monthly invoices, and charge customers automatically.

1.  API implementation and integration can span across **Amazon Elastic Compute Cloud** (Amazon EC2), **Amazon Elastic Kubernetes Service** (Amazon EKS), **AWS Elastic Beanstalk**, **Red Hat OpenShift Service on AWS** (ROSA), and corporate data center applications. The API developer can also use an **AWS Lambda** policy to initiate **Lambda** functions with AWS-native service integrations.

1.  **AWS CodePipeline** can be integrated with an API Connect CI/CD pipeline to publish and test APIs and product changes.

1.  Client applications (consuming applications) such as web apps, mobile apps, and IoT devices can invoke and consume the APIs.

1.  The API analytics data can be offloaded to **Amazon Simple Storage Service** (Amazon S3), which integrates with **Amazon Quick** to visualize using dashboards. You can review API traffic patterns, latency, consumption, and more, then make data driven insights into your API initiatives.

## Download editable diagram
<a name="download-editable-diagram"></a>

To customize this reference architecture diagram based on your business needs, [download the ZIP file](samples/security-rich-api-management-using-ibm-api-connect.zip) which contains an editable PowerPoint.

## Create a free AWS account
<a name="create-a-free-aws-account"></a>

[https://portal.aws.amazon.com/gp/aws/developer/registration/index.html](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html)

Sign up for an AWS account. New accounts include 12 months of [AWS Free Tier](https://aws.amazon.com/free/) access, including the use of Amazon EC2, Amazon S3, and Amazon DynamoDB.

## Further reading
<a name="further-reading"></a>

 For additional information, refer to
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Contributors
<a name="contributors"></a>

 Contributors to this reference architecture diagram include:
+  Sankar Cherukuri, Partner Solutions Architect, Amazon Web Services

## Diagram history
<a name="diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date |
| --- |--- |--- |
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | October 26, 2023 |

**Note**
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.
