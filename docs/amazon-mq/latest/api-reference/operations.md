---
source_url: https://docs.aws.amazon.com/amazon-mq/latest/api-reference/operations.html
---

# Operations
<a name="operations"></a>

The Amazon MQ REST API includes the following operations.
+ [CreateBroker](brokers.md#CreateBroker)

  Creates a broker. Note: This API is asynchronous.

  To create a broker, you must either use the `AmazonMQFullAccess` IAM policy or include the following EC2 permissions in your IAM policy.
  + `ec2:CreateNetworkInterface`

    This permission is required to allow Amazon MQ to create an elastic network interface (ENI) on behalf of your account.
  + `ec2:CreateNetworkInterfacePermission`

    This permission is required to attach the ENI to the broker instance.
  + `ec2:DeleteNetworkInterface`
  + `ec2:DeleteNetworkInterfacePermission`
  + `ec2:DetachNetworkInterface`
  + `ec2:DescribeInternetGateways`
  + `ec2:DescribeNetworkInterfaces`
  + `ec2:DescribeNetworkInterfacePermissions`
  + `ec2:DescribeRouteTables`
  + `ec2:DescribeSecurityGroups`
  + `ec2:DescribeSubnets`
  + `ec2:DescribeVpcs`

  For more information, see [Create an IAM User and Get Your AWS Credentials](https://docs.aws.amazon.com//amazon-mq/latest/developer-guide/amazon-mq-setting-up.html#create-iam-user) and [Never Modify or Delete the Amazon MQ Elastic Network Interface](https://docs.aws.amazon.com//amazon-mq/latest/developer-guide/connecting-to-amazon-mq.html#never-modify-delete-elastic-network-interface) in the *Amazon MQ Developer Guide*.
+ [CreateConfiguration](configurations.md#CreateConfiguration)

  Creates a new configuration for the specified configuration name. Amazon MQ uses the default configuration (the engine type and version).
+ [CreateTags](tags-resource-arn.md#CreateTags)

  Add a tag to a resource.
+ [CreateUser](brokers-broker-id-users-username.md#CreateUser)

  Creates an ActiveMQ user.
**Important**
Do not add personally identifiable information (PII) or other confidential or sensitive information in broker usernames. Broker usernames are accessible to other AWS services, including CloudWatch Logs. Broker usernames are not intended to be used for private or sensitive data.
+ [DeleteBroker](brokers-broker-id.md#DeleteBroker)

  Deletes a broker. Note: This API is asynchronous.
+ [DeleteConfiguration](configurations-configuration-id.md#DeleteConfiguration)

  Deletes the specified configuration.
+ [DeleteTags](tags-resource-arn.md#DeleteTags)

  Removes a tag from a resource.
+ [DeleteUser](brokers-broker-id-users-username.md#DeleteUser)

  Deletes an ActiveMQ user.
+ [DescribeBroker](brokers-broker-id.md#DescribeBroker)

  Returns information about the specified broker.
+ [DescribeBrokerEngineTypes](broker-engine-types.md#DescribeBrokerEngineTypes)

  Describe available engine types and versions.
+ [DescribeBrokerInstanceOptions](broker-instance-options.md#DescribeBrokerInstanceOptions)

  Describe available broker instance options.
+ [DescribeConfiguration](configurations-configuration-id.md#DescribeConfiguration)

  Returns information about the specified configuration.
+ [DescribeConfigurationRevision](configurations-configuration-id-revisions-configuration-revision.md#DescribeConfigurationRevision)

  Returns the specified configuration revision for the specified configuration.
+ [DescribeSharedResources](brokers-broker-id-shared-resources.md#DescribeSharedResources)

  Returns the resources shared to a broker.
+ [DescribeUser](brokers-broker-id-users-username.md#DescribeUser)

  Returns information about an ActiveMQ user.
+ [ListBrokers](brokers.md#ListBrokers)

  Returns a list of all brokers.
+ [ListConfigurationRevisions](configurations-configuration-id-revisions.md#ListConfigurationRevisions)

  Returns a list of all revisions for the specified configuration.
+ [ListConfigurations](configurations.md#ListConfigurations)

  Returns a list of all configurations.
+ [ListTags](tags-resource-arn.md#ListTags)

  Lists tags for a resource.
+ [ListUsers](brokers-broker-id-users.md#ListUsers)

  Returns a list of all ActiveMQ users.
+ [Promote](brokers-broker-id-promote.md#Promote)

  Promotes a data replication replica broker to a primary.
+ [RebootBroker](brokers-broker-id-reboot.md#RebootBroker)

  Reboots a broker. Note: This API is asynchronous.
+ [UpdateBroker](brokers-broker-id.md#UpdateBroker)

  Adds a pending configuration change to a broker.
+ [UpdateConfiguration](configurations-configuration-id.md#UpdateConfiguration)

  Updates the specified configuration.
+ [UpdateUser](brokers-broker-id-users-username.md#UpdateUser)

  Updates the information for an ActiveMQ user.
