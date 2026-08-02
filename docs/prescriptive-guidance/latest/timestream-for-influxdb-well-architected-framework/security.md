---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/timestream-for-influxdb-well-architected-framework/security.html
---

# Security pillar
<a name="security"></a>

The [security pillar](https://docs.aws.amazon.com/wellarchitected/latest/framework/security.html) helps you understand how to apply the shared responsibility model when using Timestream for InfluxDB.

The security pillar includes the following key focus areas:
+ Data security
+ Network security
+ Authentication and authorization

The following sections show you how to configure Timestream for InfluxDB to meet your security and compliance objectives. You also learn how to use other AWS services that help you to monitor and secure your Timestream for InfluxDB resources.

## Implement data security
<a name="data-security"></a>

Data leakage and breaches put your customers at risk and can cause substantial negative impact on your company. The AWS [shared responsibility model applies](https://aws.amazon.com/compliance/shared-responsibility-model/) to data protection in Timestream for InfluxDB. The following practices help protect your customer data from inadvertent and malicious exposure:
+ Don't include confidential information in instance names, tags, parameter groups, AWS Identity and Access Management (IAM) roles, and other metadata. That data might appear in billing or diagnostic logs.
+ Use encryption to increase data protection of your applications that are deployed in the cloud. Encrypted instances provide an additional layer of data protection by helping to secure your data from unauthorized access to the underlying storage. Timestream for InfluxDB encryption is enabled by default.
+ Use parameterization for APIs wherever possible.

For more information about data protection and encryption, see the [Timestream for InfluxDB documentation](https://docs.aws.amazon.com/timestream/latest/developerguide/data-protection-for-influx-db.html).

## Secure your networks
<a name="secure-networks"></a>

You can create a Timestream for InfluxDB instance only in a virtual private cloud (VPC) on AWS. To further secure your instance, do the following:
+ Restrict public access  to the instance's endpoint by doing one of the following:
  + Choose **Not publicly accessible **on the **Create InfluxDB database** page (selected by default).
  + Set the [PubliclyAccessible](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-timestream-influxdbinstance.html#cfn-timestream-influxdbinstance-publiclyaccessible) property to `false`** **in AWS CloudFormation (`AWS::Timestream::InfluxDBInstance`).

  When you choose **Not publicly accessible** or set `PubliclyAccessible` to `false`, the instance's endpoints are accessible only within the VPC. The endpoints are usually accessed from an [Amazon Elastic Compute Cloud (Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html)[)](https://docs.aws.amazon.com/ec2/) instance running in the same VPC as the Timestream for InfluxDB instance.
+ Use security groups to further secure your network access to Timestream for InfluxDB within the VPC.
+ Use SSL/TLS to communicate with AWS resources. Timestream for InfluxDB  requires TLS 1.2, and we recommend TLS 1.3.
+ Securely connect to your instance by following the instructions in [Creating and connecting to a Timestream for InfluxDB instance](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influx-getting-started-creating-db-instance.html).
+ Establish a private connection between your VPC and Amazon Timestream for InfluxDB control plane API endpoints by creating an [interface VPC endpoint](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-influxb-privatelink.html).

For more information about security, see the [Timestream for InfluxDB documentation](https://docs.aws.amazon.com/timestream/latest/developerguide/security-timestream-for-influxdb.html).

## Implement authentication and authorization
<a name="authenticate-authorize"></a>

Use IAM credentials to control management** **actions on Timestream for InfluxDB instances. When you connect to Timestream for InfluxDB by using IAM credentials, your IAM role must have IAM policies that grant the permissions required to perform Timestream for InfluxDB management operations. Ensure that you follow the principle of least privilege, granting only the permissions required to complete a task. For more information, see [Identity and Access Management for Amazon Timestream for InfluxDB](https://docs.aws.amazon.com/timestream/latest/developerguide/security-iam-for-influxdb.html).

You can use [Amazon Timestream for InfluxDB actions](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazontimestreaminfluxdb.html) in the IAM policy to control who can manage your Timestream for InfluxDB instance.

To provide fine-grained access control for your data stored in your Amazon Timestream for InfluxDB instance, give users [InfluxDB API tokens](https://docs.influxdata.com/influxdb/v2/admin/tokens/).

For interacting with other AWS services, Amazon Timestream for InfluxDB uses IAM service-linked roles. A service-linked role is a unique type of IAM role that is linked directly to Timestream for InfluxDB. Service-linked roles are predefined by Timestream for InfluxDB, and they include all the permissions that the service requires to call other AWS services on your behalf. For more information, see [Using Service-Linked Roles for Amazon Timestream for InfluxDB](https://docs.aws.amazon.com/timestream/latest/developerguide/using-service-linked-roles.html).
