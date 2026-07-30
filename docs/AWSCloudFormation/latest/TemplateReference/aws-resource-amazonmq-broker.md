---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-amazonmq-broker.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AmazonMQ::Broker
<a name="aws-resource-amazonmq-broker"></a>

Creates a broker. Note: This API is asynchronous.

To create a broker, you must either use the `AmazonMQFullAccess` IAM policy or include the following EC2 permissions in your IAM policy.
+  `ec2:CreateNetworkInterface`

  This permission is required to allow Amazon MQ to create an elastic network interface (ENI) on behalf of your account.
+  `ec2:CreateNetworkInterfacePermission`

  This permission is required to attach the ENI to the broker instance.
+  `ec2:DeleteNetworkInterface`
+  `ec2:DeleteNetworkInterfacePermission`
+  `ec2:DetachNetworkInterface`
+  `ec2:DescribeInternetGateways`
+  `ec2:DescribeNetworkInterfaces`
+  `ec2:DescribeNetworkInterfacePermissions`
+  `ec2:DescribeRouteTables`
+  `ec2:DescribeSecurityGroups`
+  `ec2:DescribeSubnets`
+  `ec2:DescribeVpcs`

For more information, see [Create an IAM User and Get Your AWS Credentials](https://docs.aws.amazon.com//amazon-mq/latest/developer-guide/amazon-mq-setting-up.html#create-iam-user) and [Never Modify or Delete the Amazon MQ Elastic Network Interface](https://docs.aws.amazon.com//amazon-mq/latest/developer-guide/connecting-to-amazon-mq.html#never-modify-delete-elastic-network-interface) in the *Amazon MQ Developer Guide*.

## Syntax
<a name="aws-resource-amazonmq-broker-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-amazonmq-broker-syntax.json"></a>

```
{
  "Type" : "AWS::AmazonMQ::Broker",
  "Properties" : {
      "[AuthenticationStrategy](#cfn-amazonmq-broker-authenticationstrategy)" : {{String}},
      "[AutoMinorVersionUpgrade](#cfn-amazonmq-broker-autominorversionupgrade)" : {{Boolean}},
      "[BrokerName](#cfn-amazonmq-broker-brokername)" : {{String}},
      "[Configuration](#cfn-amazonmq-broker-configuration)" : {{ConfigurationId}},
      "[DataReplicationMode](#cfn-amazonmq-broker-datareplicationmode)" : {{String}},
      "[DataReplicationPrimaryBrokerArn](#cfn-amazonmq-broker-datareplicationprimarybrokerarn)" : {{String}},
      "[DeploymentMode](#cfn-amazonmq-broker-deploymentmode)" : {{String}},
      "[EncryptionOptions](#cfn-amazonmq-broker-encryptionoptions)" : {{EncryptionOptions}},
      "[EngineType](#cfn-amazonmq-broker-enginetype)" : {{String}},
      "[EngineVersion](#cfn-amazonmq-broker-engineversion)" : {{String}},
      "[HostInstanceType](#cfn-amazonmq-broker-hostinstancetype)" : {{String}},
      "[LdapServerMetadata](#cfn-amazonmq-broker-ldapservermetadata)" : {{LdapServerMetadata}},
      "[Logs](#cfn-amazonmq-broker-logs)" : {{LogList}},
      "[MaintenanceWindowStartTime](#cfn-amazonmq-broker-maintenancewindowstarttime)" : {{MaintenanceWindow}},
      "[PubliclyAccessible](#cfn-amazonmq-broker-publiclyaccessible)" : {{Boolean}},
      "[ResourceShareArns](#cfn-amazonmq-broker-resourcesharearns)" : {{[ String, ... ]}},
      "[SecurityGroups](#cfn-amazonmq-broker-securitygroups)" : {{[ String, ... ]}},
      "[StorageSize](#cfn-amazonmq-broker-storagesize)" : {{Integer}},
      "[StorageType](#cfn-amazonmq-broker-storagetype)" : {{String}},
      "[SubnetIds](#cfn-amazonmq-broker-subnetids)" : {{[ String, ... ]}},
      "[Tags](#cfn-amazonmq-broker-tags)" : {{[ TagsEntry, ... ]}},
      "[Users](#cfn-amazonmq-broker-users)" : {{[ User, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-amazonmq-broker-syntax.yaml"></a>

```
Type: AWS::AmazonMQ::Broker
Properties:
  [AuthenticationStrategy](#cfn-amazonmq-broker-authenticationstrategy): {{String}}
  [AutoMinorVersionUpgrade](#cfn-amazonmq-broker-autominorversionupgrade): {{Boolean}}
  [BrokerName](#cfn-amazonmq-broker-brokername): {{String}}
  [Configuration](#cfn-amazonmq-broker-configuration): {{
    ConfigurationId}}
  [DataReplicationMode](#cfn-amazonmq-broker-datareplicationmode): {{String}}
  [DataReplicationPrimaryBrokerArn](#cfn-amazonmq-broker-datareplicationprimarybrokerarn): {{String}}
  [DeploymentMode](#cfn-amazonmq-broker-deploymentmode): {{String}}
  [EncryptionOptions](#cfn-amazonmq-broker-encryptionoptions): {{
    EncryptionOptions}}
  [EngineType](#cfn-amazonmq-broker-enginetype): {{String}}
  [EngineVersion](#cfn-amazonmq-broker-engineversion): {{String}}
  [HostInstanceType](#cfn-amazonmq-broker-hostinstancetype): {{String}}
  [LdapServerMetadata](#cfn-amazonmq-broker-ldapservermetadata): {{
    LdapServerMetadata}}
  [Logs](#cfn-amazonmq-broker-logs): {{
    LogList}}
  [MaintenanceWindowStartTime](#cfn-amazonmq-broker-maintenancewindowstarttime): {{
    MaintenanceWindow}}
  [PubliclyAccessible](#cfn-amazonmq-broker-publiclyaccessible): {{Boolean}}
  [ResourceShareArns](#cfn-amazonmq-broker-resourcesharearns): {{
    - String}}
  [SecurityGroups](#cfn-amazonmq-broker-securitygroups): {{
    - String}}
  [StorageSize](#cfn-amazonmq-broker-storagesize): {{Integer}}
  [StorageType](#cfn-amazonmq-broker-storagetype): {{String}}
  [SubnetIds](#cfn-amazonmq-broker-subnetids): {{
    - String}}
  [Tags](#cfn-amazonmq-broker-tags): {{
    - TagsEntry}}
  [Users](#cfn-amazonmq-broker-users): {{
    - User}}
```

## Properties
<a name="aws-resource-amazonmq-broker-properties"></a>

`AuthenticationStrategy`  <a name="cfn-amazonmq-broker-authenticationstrategy"></a>
Optional. The authentication strategy used to secure the broker. The default is `SIMPLE`.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`AutoMinorVersionUpgrade`  <a name="cfn-amazonmq-broker-autominorversionupgrade"></a>
Enables automatic upgrades to new patch versions for brokers as new versions are released and supported by Amazon MQ. Automatic upgrades occur during the scheduled maintenance window or after a manual broker reboot. Set to `true` by default, if no value is specified.
Must be set to `true` for ActiveMQ brokers version 5.18 and above and for RabbitMQ brokers version 3.13 and above.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BrokerName`  <a name="cfn-amazonmq-broker-brokername"></a>
Required. The broker's name. This value must be unique in your AWS account, 1-50 characters long, must contain only letters, numbers, dashes, and underscores, and must not contain white spaces, brackets, wildcard characters, or special characters.
 Do not add personally identifiable information (PII) or other confidential or sensitive information in broker names. Broker names are accessible to other AWS services, including CloudWatch Logs. Broker names are not intended to be used for private or sensitive data.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9A-Za-z_-]{1,50}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Configuration`  <a name="cfn-amazonmq-broker-configuration"></a>
A list of information about the configuration.
*Required*: No
*Type*: [ConfigurationId](aws-properties-amazonmq-broker-configurationid.md)
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`DataReplicationMode`  <a name="cfn-amazonmq-broker-datareplicationmode"></a>
Defines whether this broker is a part of a data replication pair.
*Required*: No
*Type*: String
*Allowed values*: `NONE | CRDR`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataReplicationPrimaryBrokerArn`  <a name="cfn-amazonmq-broker-datareplicationprimarybrokerarn"></a>
The Amazon Resource Name (ARN) of the primary broker that is used to replicate data from in a data replication pair, and is applied to the replica broker. Must be set when dataReplicationMode is set to CRDR.
*Required*: No
*Type*: String
*Pattern*: `^arn:.*`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DeploymentMode`  <a name="cfn-amazonmq-broker-deploymentmode"></a>
Required. The broker's deployment mode.
*Required*: Yes
*Type*: String
*Allowed values*: `SINGLE_INSTANCE | ACTIVE_STANDBY_MULTI_AZ | CLUSTER_MULTI_AZ`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EncryptionOptions`  <a name="cfn-amazonmq-broker-encryptionoptions"></a>
Encryption options for the broker.
*Required*: No
*Type*: [EncryptionOptions](aws-properties-amazonmq-broker-encryptionoptions.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EngineType`  <a name="cfn-amazonmq-broker-enginetype"></a>
Required. The type of broker engine. Currently, Amazon MQ supports `ACTIVEMQ` and `RABBITMQ`.
*Required*: Yes
*Type*: String
*Allowed values*: `ACTIVEMQ | RABBITMQ`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EngineVersion`  <a name="cfn-amazonmq-broker-engineversion"></a>
The broker engine version. Defaults to the latest available version for the specified broker engine type. For more information, see the [ActiveMQ version management](https://docs.aws.amazon.com//amazon-mq/latest/developer-guide/activemq-version-management.html) and the [RabbitMQ version management](https://docs.aws.amazon.com//amazon-mq/latest/developer-guide/rabbitmq-version-management.html) sections in the Amazon MQ Developer Guide.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HostInstanceType`  <a name="cfn-amazonmq-broker-hostinstancetype"></a>
Required. The broker's instance type.
*Required*: Yes
*Type*: String
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`LdapServerMetadata`  <a name="cfn-amazonmq-broker-ldapservermetadata"></a>
Optional. The metadata of the LDAP server used to authenticate and authorize connections to the broker. Does not apply to RabbitMQ brokers.
*Required*: No
*Type*: [LdapServerMetadata](aws-properties-amazonmq-broker-ldapservermetadata.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Logs`  <a name="cfn-amazonmq-broker-logs"></a>
Enables Amazon CloudWatch logging for brokers.
*Required*: No
*Type*: [LogList](aws-properties-amazonmq-broker-loglist.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaintenanceWindowStartTime`  <a name="cfn-amazonmq-broker-maintenancewindowstarttime"></a>
The parameters that determine the WeeklyStartTime.
*Required*: No
*Type*: [MaintenanceWindow](aws-properties-amazonmq-broker-maintenancewindow.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PubliclyAccessible`  <a name="cfn-amazonmq-broker-publiclyaccessible"></a>
Enables connections from applications outside of the VPC that hosts the broker's subnets. Set to `false` by default, if no value is provided.
*Required*: Yes
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ResourceShareArns`  <a name="cfn-amazonmq-broker-resourcesharearns"></a>
The list of resource share ARNs to associate with the broker for private networking. Only supported for RabbitMQ brokers in commercial partitions.
When specifying this property for a new broker, the creation time will be longer than usual and the broker will be restarted during the creation process.
*Required*: No
*Type*: Array of String
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`SecurityGroups`  <a name="cfn-amazonmq-broker-securitygroups"></a>
The list of rules (1 minimum, 125 maximum) that authorize connections to brokers.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StorageSize`  <a name="cfn-amazonmq-broker-storagesize"></a>
The broker's storage size in GB. Applies only to RabbitMQ version 4.x brokers with `CLUSTER_MULTI_AZ` deployment mode on `mq.m7g` instance types. If not specified, the broker uses the default storage size for the instance type. For more information about allowed storage size ranges, see [Instance types](https://docs.aws.amazon.com//amazon-mq/latest/developer-guide/rmq-broker-instance-types.html) in the *Amazon MQ Developer Guide*.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StorageType`  <a name="cfn-amazonmq-broker-storagetype"></a>
The broker's storage type.
*Required*: No
*Type*: String
*Allowed values*: `EBS | EFS`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SubnetIds`  <a name="cfn-amazonmq-broker-subnetids"></a>
The list of groups that define which subnets and IP ranges the broker can use from different Availability Zones. If you specify more than one subnet, the subnets must be in different Availability Zones. Amazon MQ will not be able to create VPC endpoints for your broker with multiple subnets in the same Availability Zone. A SINGLE\_INSTANCE deployment requires one subnet (for example, the default subnet). An ACTIVE\_STANDBY\_MULTI\_AZ Amazon MQ for ActiveMQ deployment requires two subnets. A CLUSTER\_MULTI\_AZ Amazon MQ for RabbitMQ deployment has no subnet requirements when deployed with public accessibility. Deployment without public accessibility requires at least one subnet.
 If you specify subnets in a [shared VPC](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-sharing.html) for a RabbitMQ broker, the associated VPC to which the specified subnets belong must be owned by your AWS account. Amazon MQ will not be able to create VPC endpoints in VPCs that are not owned by your AWS account.
*Required*: No
*Type*: Array of String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-amazonmq-broker-tags"></a>
Create tags when creating the broker.
*Required*: No
*Type*: Array of [TagsEntry](aws-properties-amazonmq-broker-tagsentry.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Users`  <a name="cfn-amazonmq-broker-users"></a>
The list of broker users (persons or applications) who can access queues and topics. For Amazon MQ for RabbitMQ brokers, one and only one administrative user is accepted and created when a broker is first provisioned. All subsequent broker users are created by making RabbitMQ API calls directly to brokers or via the RabbitMQ web console.
When OAuth 2.0 is enabled, the broker accepts one or no users.
*Required*: No
*Type*: Array of [User](aws-properties-amazonmq-broker-user.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-amazonmq-broker-return-values"></a>

### Ref
<a name="aws-resource-amazonmq-broker-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Amazon MQ broker ID. For example:

 `b-1234a5b6-78cd-901e-2fgh-3i45j6k178l9`

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-amazonmq-broker-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-amazonmq-broker-return-values-fn--getatt-fn--getatt"></a>

`AmqpEndpoints`  <a name="AmqpEndpoints-fn::getatt"></a>
The AMQP endpoints of each broker instance as a list of strings.
 `amqp+ssl://b-4aada85d-a80c-4be0-9d30-e344a01b921e-1.mq.eu-central-amazonaws.com:5671`

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the Amazon MQ broker.
 `arn:aws:mq:us-east-2:123456789012:broker:MyBroker:b-1234a5b6-78cd-901e-2fgh-3i45j6k178l9`

`ConfigurationId`  <a name="ConfigurationId-fn::getatt"></a>
The unique ID that Amazon MQ generates for the configuration.
 `c-1234a5b6-78cd-901e-2fgh-3i45j6k178l9`

`ConfigurationRevision`  <a name="ConfigurationRevision-fn::getatt"></a>
The revision number of the configuration.
 `1`

`ConsoleURLs`  <a name="ConsoleURLs-fn::getatt"></a>
Property description not available.

`EngineVersionCurrent`  <a name="EngineVersionCurrent-fn::getatt"></a>
Property description not available.

`IpAddresses`  <a name="IpAddresses-fn::getatt"></a>
The IP addresses of each broker instance as a list of strings. Does not apply to RabbitMQ brokers.
 `['198.51.100.2', '203.0.113.9']`

`MqttEndpoints`  <a name="MqttEndpoints-fn::getatt"></a>
The MQTT endpoints of each broker instance as a list of strings.
 `mqtt+ssl://b-4aada85d-a80c-4be0-9d30-e344a01b921e-1.mq.eu-central-amazonaws.com:8883`

`OpenWireEndpoints`  <a name="OpenWireEndpoints-fn::getatt"></a>
The OpenWire endpoints of each broker instance as a list of strings.
 `ssl://b-4aada85d-a80c-4be0-9d30-e344a01b921e-1.mq.eu-central-amazonaws.com:61617`

`StompEndpoints`  <a name="StompEndpoints-fn::getatt"></a>
The STOMP endpoints of each broker instance as a list of strings.
 `stomp+ssl://b-4aada85d-a80c-4be0-9d30-e344a01b921e-1.mq.eu-central-amazonaws.com:61614`

`WssEndpoints`  <a name="WssEndpoints-fn::getatt"></a>
The WSS endpoints of each broker instance as a list of strings.
 `wss://b-4aada85d-a80c-4be0-9d30-e344a01b921e-1.mq.eu-central-amazonaws.com:61619`

## Examples
<a name="aws-resource-amazonmq-broker--examples"></a>

**Topics**
+ [Basic Amazon MQ Broker](#aws-resource-amazonmq-broker--examples--Basic_Amazon_MQ_Broker)
+ [Complex Amazon MQ Broker](#aws-resource-amazonmq-broker--examples--Complex_Amazon_MQ_Broker)

### Basic Amazon MQ Broker
<a name="aws-resource-amazonmq-broker--examples--Basic_Amazon_MQ_Broker"></a>

The following examples creates a basic Amazon MQ broker. The RabbitMQ example creates a broker with one administrative user, while the ActiveMQ example creates a broker with one user that belongs to a group.

#### JSON
<a name="aws-resource-amazonmq-broker--examples--Basic_Amazon_MQ_Broker--json"></a>

```
{
  "Description": "Create a basic Amazon MQ for ActiveMQ broker",
  "Resources": {
    "BasicBroker": {
      "Type": "AWS::AmazonMQ::Broker",
      "Properties": {
        "AutoMinorVersionUpgrade": "false",
        "BrokerName": "MyBasicActiveBroker",
        "DeploymentMode": "SINGLE_INSTANCE",
        "EngineType": "ActiveMQ",
        "EngineVersion": "5.15.0",
        "HostInstanceType": "mq.t2.micro",
        "PubliclyAccessible": "true",
        "Users": [
          {
            "ConsoleAccess": "true",
            "Groups": [
              "MyGroup"
            ],
            "Password" : "AmazonMqPassword",
            "Username" : "AmazonMqUsername"
          }
        ]
      }
    }
  }
}
```

#### JSON
<a name="aws-resource-amazonmq-broker--examples--Basic_Amazon_MQ_Broker--json"></a>

```
{
"Description": "Create a basic Amazon MQ for RabbitMQ broker",
"Resources": {
  "BasicBroker": {
    "Type": "AWS::AmazonMQ::Broker",
    "Properties": {
      "AutoMinorVersionUpgrade": "false",
      "BrokerName": "MyBasicRabbitBroker",
      "DeploymentMode": "SINGLE_INSTANCE",
      "EngineType": "RabbitMQ",
      "EngineVersion": "3.8.6",
      "HostInstanceType": "mq.t3.micro",
      "PubliclyAccessible": "true",
      "Users": [
          {
            "Password" : "AmazonMqPassword",
            "Username" : "AmazonMqUsername"
          }
        ]
      }
    }
  }
}
```

#### YAML
<a name="aws-resource-amazonmq-broker--examples--Basic_Amazon_MQ_Broker--yaml"></a>

```
---
Description: "Create a basic Amazon MQ for ActiveMQ broker"
Resources:
  BasicBroker:
    Type: "AWS::AmazonMQ::Broker"
    Properties:
      AutoMinorVersionUpgrade: "false"
      BrokerName: MyBasicActiveBroker
      DeploymentMode: SINGLE_INSTANCE
      EngineType: ActiveMQ
      EngineVersion: "5.15.0"
      HostInstanceType: mq.t2.micro
      PubliclyAccessible: "true"
      Users:
        -
          ConsoleAccess: "true"
          Groups:
            - MyGroup
          Password: AmazonMqPassword
          Username: AmazonMqUsername
```

#### YAML
<a name="aws-resource-amazonmq-broker--examples--Basic_Amazon_MQ_Broker--yaml"></a>

```
---
Description: "Create a basic Amazon MQ for RabbitMQ broker"
Resources:
  BasicBroker:
    Type: "AWS::AmazonMQ::Broker"
    Properties:
      AutoMinorVersionUpgrade: "false"
      BrokerName: MyBasicRabbitBroker
      DeploymentMode: SINGLE_INSTANCE
      EngineType: RabbitMQ
      EngineVersion: "3.8.6"
      HostInstanceType: mq.t3.micro
      PubliclyAccessible: "true"
      Users:
        -
          Password: AmazonMqPassword
          Username: AmazonMqUsername
```

### Complex Amazon MQ Broker
<a name="aws-resource-amazonmq-broker--examples--Complex_Amazon_MQ_Broker"></a>

The following example creates a complex Amazon MQ broker. The ActiveMQ example creates a broker with two users that don't belong to a group and one user that belongs in a group. The RabbitMQ example creates one administrator user, which can then create and manage other users via the RabbitMQ web console or the management API.

#### JSON
<a name="aws-resource-amazonmq-broker--examples--Complex_Amazon_MQ_Broker--json"></a>

```
{
  "Description": "Create a complex, single-instance Amazon MQ for ActiveMQ broker",
  "Resources": {
    "ComplexBroker": {
      "Type": "AWS::AmazonMQ::Broker",
      "Properties": {
        "AutoMinorVersionUpgrade": "false",
        "BrokerName": "MyComplexActiveBroker",
        "Configuration": {
          "Id": { "Ref": "Configuration1" },
          "Revision" : { "Fn::GetAtt": ["Configuration1", "Revision"] }
        },
        "DeploymentMode": "SINGLE_INSTANCE",
        "EngineType": "ActiveMQ",
        "EngineVersion": "5.15.0",
        "HostInstanceType": "mq.t2.micro",
        "Logs": {
            "General": true,
            "Audit": false
        },
        "MaintenanceWindowStartTime": {
          "DayOfWeek": "Monday",
          "TimeOfDay": "22:45",
          "TimeZone": "America/Los_Angeles"
        },
        "PubliclyAccessible": "true",
        "SecurityGroups": [
          "sg-a1b234cd",
          "sg-e5f678gh"
        ],
        "SubnetIds": [
          "subnet-12a3b45c",
          "subnet-67d8e90f"
        ],
        "Users": [{
          "ConsoleAccess": "true",
          "Password" : "AmazonMqPassword",
          "Username" : "AmazonMqUsername"
        }, {
          "Password" : "AmazonMqPassword2",
          "Username" : "AmazonMqUsername2"
        }, {
          "Groups": [
            "MyGroup1",
            "MyGroup2"
          ],
          "Password" : "AmazonMqPassword3",
          "Username" : "AmazonMqUsername3"
        }]
      }
    }
  }
}
```

#### JSON
<a name="aws-resource-amazonmq-broker--examples--Complex_Amazon_MQ_Broker--json"></a>

```
{
  "Description": "Create a complex, single-instance Amazon MQ RabbitMQ broker without public accessibility",
  "Resources": {
    "ComplexBroker": {
      "Type": "AWS::AmazonMQ::Broker",
      "Properties": {
        "AutoMinorVersionUpgrade": "true",
        "BrokerName": "MyComplexRabbitBroker",
        "DeploymentMode": "SINGLE_INSTANCE",
        "EngineType": "RabbitMQ",
        "EngineVersion": "3.8.6",
        "HostInstanceType": "mq.t3.micro",
        "Logs": {
          "General": true
        },
        "MaintenanceWindowStartTime": {
          "DayOfWeek": "Monday",
          "TimeOfDay": "22:45",
          "TimeZone": "America/Los_Angeles"
        },
        "PubliclyAccessible": "false",
        "SecurityGroups": [
          "sg-1a234b5cd6efgh7i8"
        ],
        "SubnetIds": [
          "subnet-123456b7891abcd1f"
        ],
        "Users": [
          {
            "Password" : "AmazonMqPassword",
            "Username" : "AmazonMqUsername"
          }
        ]
      }
    }
  }
}
```

#### YAML
<a name="aws-resource-amazonmq-broker--examples--Complex_Amazon_MQ_Broker--yaml"></a>

```
Description: Create a complex, single-instance Amazon MQ for ActiveMQ broker
Resources:
  ComplexBroker:
    Type: 'AWS::AmazonMQ::Broker'
    Properties:
      AutoMinorVersionUpgrade: 'false'
      BrokerName: MyComplexActiveBroker
      Configuration:
        Id: !Ref Configuration1
        Revision: !GetAtt
          - Configuration1
          - Revision
      DeploymentMode: SINGLE_INSTANCE
      EngineType: ActiveMQ
      EngineVersion: 5.15.0
      HostInstanceType: mq.t2.micro
      Logs:
        General: true
        Audit: false
      MaintenanceWindowStartTime:
        DayOfWeek: Monday
        TimeOfDay: '22:45'
        TimeZone: America/Los_Angeles
      PubliclyAccessible: 'true'
      SecurityGroups:
        - sg-a1b234cd
        - sg-e5f678gh
      SubnetIds:
        - subnet-12a3b45c
        - subnet-67d8e90f
      Users:
        - ConsoleAccess: 'true'
          Password: AmazonMqPassword
          Username: AmazonMqUsername
        - Password: AmazonMqPassword2
          Username: AmazonMqUsername2
        - Groups:
            - MyGroup1
            - MyGroup2
          Password: AmazonMqPassword3
          Username: AmazonMqUsername3
```

#### YAML
<a name="aws-resource-amazonmq-broker--examples--Complex_Amazon_MQ_Broker--yaml"></a>

```
Description: Create a single-instance Amazon MQ for RabbitMQ broker without public accessibility
Resources:
  ComplexBroker:
    Type: 'AWS::AmazonMQ::Broker'
    Properties:
      AutoMinorVersionUpgrade: false
      BrokerName: MyComplexRabbitBroker
      DeploymentMode: SINGLE_INSTANCE
      EngineType: RabbitMQ
      EngineVersion: 3.8.6
      HostInstanceType: mq.t3.micro
      Logs:
        General: true
      MaintenanceWindowStartTime:
        DayOfWeek: Monday
        TimeOfDay: '22:45'
        TimeZone: America/Los_Angeles
      PubliclyAccessible: false
      SecurityGroups:
        - 'sg-1a234b5cd6efgh7i8'
      SubnetIds:
        - 'subnet-123456b7891abcd1f'
      Users:
        - Password: AmazonMqPassword
          Username: AmazonMqUsername
```
