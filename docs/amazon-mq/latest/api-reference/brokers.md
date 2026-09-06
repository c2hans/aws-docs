---
source_url: https://docs.aws.amazon.com/amazon-mq/latest/api-reference/brokers.html
---

# Brokers
<a name="brokers"></a>

This is a collection of brokers. A broker is a message broker environment running on Amazon MQ. It is the basic building block of Amazon MQ. For more information, see [Broker instance types](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/broker-instance-types.html) in the *Amazon MQ Developer Guide*.

## URI
<a name="brokers-url"></a>

`/v1/brokers`

## HTTP methods
<a name="brokers-http-methods"></a>

### GET
<a name="brokersget"></a>

**Operation ID:** `ListBrokers`

Returns a list of all brokers.

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| nextToken | String | False | The token that specifies the next page of results Amazon MQ should return. To request the first page, leave nextToken empty. |
| maxResults | String | False | The maximum number of brokers that Amazon MQ can return per page (20 by default). This value must be an integer from 5 to 100. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 |  ListBrokersOutput | HTTP Status Code 200: OK. |
| 400 | Error | HTTP Status Code 400: Bad request due to incorrect input. Correct your request and then retry it. |
| 403 | Error | HTTP Status Code 403: Access forbidden. Correct your credentials and then retry your request. |
| 500 | Error | HTTP Status Code 500: Unexpected internal server error. Retrying your request might resolve the issue. |

### POST
<a name="brokerspost"></a>

**Operation ID:** `CreateBroker`

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

For more information, see [Create an IAM User and Get Your AWS Credentials](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/amazon-mq-setting-up.html#create-iam-user) and [Never Modify or Delete the Amazon MQ Elastic Network Interface](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/connecting-to-amazon-mq.html#never-modify-delete-elastic-network-interface) in the *Amazon MQ Developer Guide*.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 |  CreateBrokerOutput | HTTP Status Code 200: OK. |
| 400 | Error | HTTP Status Code 400: Bad request due to incorrect input. Correct your request and then retry it. |
| 401 | Error | HTTP Status Code 401: Unauthorized request. The provided credentials couldn't be validated. |
| 403 | Error | HTTP Status Code 403: Access forbidden. Correct your credentials and then retry your request. |
| 409 | Error | HTTP Status Code 409: Configuration ID is already in use. Remove the configuration from all brokers and retry the request. |
| 500 | Error | HTTP Status Code 500: Unexpected internal server error. Retrying your request might resolve the issue. |

### OPTIONS
<a name="brokersoptions"></a>

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | Default response for CORS method |

## Schemas
<a name="brokers-schemas"></a>

### Request bodies
<a name="brokers-request-examples"></a>

#### POST schema
<a name="brokers-request-body-post-example"></a>

```
{
  "engineVersion": "string",
  "deploymentMode": enum,
  "maintenanceWindowStartTime": {
    "dayOfWeek": enum,
    "timeZone": "string",
    "timeOfDay": "string"
  },
  "configuration": {
    "id": "string",
    "revision": integer
  },
  "authenticationStrategy": enum,
  "engineType": enum,
  "hostInstanceType": "string",
  "users": [
    {
      "password": "string",
      "replicationUser": boolean,
      "groups": [
        "string"
      ],
      "consoleAccess": boolean,
      "username": "string"
    }
  ],
  "tags": {
  },
  "dataReplicationMode": enum,
  "creatorRequestId": "string",
  "storageConfiguration": {
    "efs": {
      "throughputMode": enum
    }
  },
  "storageSize": integer,
  "encryptionOptions": {
    "useAwsOwnedKey": boolean,
    "kmsKeyId": "string"
  },
  "publiclyAccessible": boolean,
  "storageType": enum,
  "securityGroups": [
    "string"
  ],
  "dataReplicationPrimaryBrokerArn": "string",
  "brokerName": "string",
  "logs": {
    "general": boolean,
    "audit": boolean
  },
  "ldapServerMetadata": {
    "roleSearchMatching": "string",
    "serviceAccountPassword": "string",
    "roleBase": "string",
    "hosts": [
      "string"
    ],
    "roleName": "string",
    "userBase": "string",
    "roleSearchSubtree": boolean,
    "serviceAccountUsername": "string",
    "userRoleName": "string",
    "userSearchMatching": "string",
    "userSearchSubtree": boolean
  },
  "autoMinorVersionUpgrade": boolean,
  "subnetIds": [
    "string"
  ]
}
```

### Response bodies
<a name="brokers-response-examples"></a>

#### ListBrokersOutput schema
<a name="brokers-response-body-listbrokersoutput-example"></a>

```
{
  "brokerSummaries": [
    {
      "brokerArn": "string",
      "brokerId": "string",
      "deploymentMode": enum,
      "created": "string",
      "brokerState": enum,
      "engineType": enum,
      "brokerName": "string",
      "hostInstanceType": "string"
    }
  ],
  "nextToken": "string"
}
```

#### CreateBrokerOutput schema
<a name="brokers-response-body-createbrokeroutput-example"></a>

```
{
  "brokerArn": "string",
  "brokerId": "string"
}
```

#### Error schema
<a name="brokers-response-body-error-example"></a>

```
{
  "errorAttribute": "string",
  "message": "string"
}
```

## Properties
<a name="brokers-properties"></a>

### AuthenticationStrategy
<a name="brokers-model-authenticationstrategy"></a>

Optional. The authentication strategy used to secure the broker. The default is `SIMPLE`.
+ `SIMPLE`
+ `LDAP`
+ `CONFIG_MANAGED`

### BrokerState
<a name="brokers-model-brokerstate"></a>

The broker's status.
+ `CREATION_IN_PROGRESS`
+ `CREATION_FAILED`
+ `DELETION_IN_PROGRESS`
+ `RUNNING`
+ `REBOOT_IN_PROGRESS`
+ `CRITICAL_ACTION_REQUIRED`
+ `REPLICA`

### BrokerStorageConfiguration
<a name="brokers-model-brokerstorageconfiguration"></a>

The storage configurations of a broker.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| efs | [EfsBrokerStorageConfiguration](#brokers-model-efsbrokerstorageconfiguration) | False |  |

### BrokerStorageType
<a name="brokers-model-brokerstoragetype"></a>

The broker's storage type.

**Important**
 `EFS` is not supported for RabbitMQ engine type.
+ `EBS`
+ `EFS`

### BrokerSummary
<a name="brokers-model-brokersummary"></a>

Returns information about all brokers.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| brokerArn | string | False | The broker's Amazon Resource Name (ARN). |
| brokerId | string | False | The unique ID that Amazon MQ generates for the broker. |
| brokerName | string | False | The broker's name. This value is unique in your AWS account, 1-50 characters long, and containing only letters, numbers, dashes, and underscores, and must not contain white spaces, brackets, wildcard characters, or special characters. |
| brokerState | [BrokerState](#brokers-model-brokerstate) | False | The broker's status. |
| created | string<br />Format: date-time | False | The time when the broker was created. |
| deploymentMode | [DeploymentMode](#brokers-model-deploymentmode) | True | The broker's deployment mode. |
| engineType | [EngineType](#brokers-model-enginetype) | True | The type of broker engine. |
| hostInstanceType | string | False | The broker's instance type. |

### ConfigurationId
<a name="brokers-model-configurationid"></a>

A list of information about the configuration.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| id | string | True | Required. The unique ID that Amazon MQ generates for the configuration. |
| revision | integer | False | The revision number of the configuration. |

### CreateBrokerInput
<a name="brokers-model-createbrokerinput"></a>

Creates a broker.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| authenticationStrategy | [AuthenticationStrategy](#brokers-model-authenticationstrategy) | False | Optional. The authentication strategy used to secure the broker. The default is `SIMPLE`. |
| autoMinorVersionUpgrade | boolean | False | Enables automatic upgrades to new patch versions for brokers as new versions are released and supported by Amazon MQ. Automatic upgrades occur during the scheduled maintenance window or after a manual broker reboot. Set to `true` by default, if no value is specified.Must be set to `true` for ActiveMQ brokers version 5.18 and above and for RabbitMQ brokers version 3.13 and above. |
| brokerName | string | True | Required. The broker's name. This value must be unique in your AWS account, 1-50 characters long, must contain only letters, numbers, dashes, and underscores, and must not contain white spaces, brackets, wildcard characters, or special characters.  Do not add personally identifiable information (PII) or other confidential or sensitive information in broker names. Broker names are accessible to other AWS services, including CloudWatch Logs. Broker names are not intended to be used for private or sensitive data.   |
| configuration | [ConfigurationId](#brokers-model-configurationid) | False | A list of information about the configuration. |
| creatorRequestId | string | False | The unique ID that the requester receives for the created broker. Amazon MQ passes your ID with the API action.  We recommend using a Universally Unique Identifier (UUID) for the creatorRequestId. You may omit the `creatorRequestId` if your application doesn't require idempotency.   |
| dataReplicationMode | [DataReplicationMode](#brokers-model-datareplicationmode) | False | Defines whether this broker is a part of a data replication pair. |
| dataReplicationPrimaryBrokerArn | string | False | The Amazon Resource Name (ARN) of the primary broker that is used to replicate data from in a data replication pair, and is applied to the replica broker. Must be set when dataReplicationMode is set to CRDR. |
| deploymentMode | [DeploymentMode](#brokers-model-deploymentmode) | True | Required. The broker's deployment mode. |
| encryptionOptions | [EncryptionOptions](#brokers-model-encryptionoptions) | False | Encryption options for the broker.  |
| engineType | [EngineType](#brokers-model-enginetype) | True | Required. The type of broker engine. Currently, Amazon MQ supports `ACTIVEMQ` and `RABBITMQ`. |
| engineVersion | string | False | The broker engine version. Defaults to the latest available version for the specified broker engine type. For more information, see the [ActiveMQ version management](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/activemq-version-management.html) and the [RabbitMQ version management](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/rabbitmq-version-management.html) sections in the Amazon MQ Developer Guide. |
| hostInstanceType | string | True | Required. The broker's instance type. |
| ldapServerMetadata | [LdapServerMetadataInput](#brokers-model-ldapservermetadatainput) | False | Optional. The metadata of the LDAP server used to authenticate and authorize connections to the broker. Does not apply to RabbitMQ brokers. |
| logs | [Logs](#brokers-model-logs) | False | Enables Amazon CloudWatch logging for brokers. |
| maintenanceWindowStartTime | [WeeklyStartTime](#brokers-model-weeklystarttime) | False | The parameters that determine the WeeklyStartTime. |
| publiclyAccessible | boolean | True | Enables connections from applications outside of the VPC that hosts the broker's subnets. Set to `false` by default, if no value is provided. |
| securityGroups | Array of type string | False | The list of rules (1 minimum, 125 maximum) that authorize connections to brokers. |
| storageConfiguration | [BrokerStorageConfiguration](#brokers-model-brokerstorageconfiguration) | False | The broker's storage configuration. |
| storageSize | integer | False | The broker's storage size in GB. Applies only to RabbitMQ version 4.x brokers with `CLUSTER_MULTI_AZ` deployment mode on `mq.m7g` instance types. If not specified, the broker uses the default storage size for the instance type. For more information about allowed storage size ranges, see [Instance types](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/rmq-broker-instance-types.html) in the *Amazon MQ Developer Guide*. |
| storageType | [BrokerStorageType](#brokers-model-brokerstoragetype) | False | The broker's storage type. |
| subnetIds | Array of type string | False | The list of groups that define which subnets and IP ranges the broker can use from different Availability Zones. If you specify more than one subnet, the subnets must be in different Availability Zones. Amazon MQ will not be able to create VPC endpoints for your broker with multiple subnets in the same Availability Zone. A SINGLE\_INSTANCE deployment requires one subnet (for example, the default subnet). An ACTIVE\_STANDBY\_MULTI\_AZ Amazon MQ for ActiveMQ deployment requires two subnets. A CLUSTER\_MULTI\_AZ Amazon MQ for RabbitMQ deployment has no subnet requirements when deployed with public accessibility. Deployment without public accessibility requires at least one subnet.  If you specify subnets in a [shared VPC](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-sharing.html) for a RabbitMQ broker, the associated VPC to which the specified subnets belong must be owned by your AWS account. Amazon MQ will not be able to create VPC endpoints in VPCs that are not owned by your AWS account.  |
| tags | object | False | Create tags when creating the broker. |
| users | Array of type [User](#brokers-model-user) | False | The list of broker users (persons or applications) who can access queues and topics. For Amazon MQ for RabbitMQ brokers, one and only one administrative user is accepted and created when a broker is first provisioned. All subsequent broker users are created by making RabbitMQ API calls directly to brokers or via the RabbitMQ web console.<br />When OAuth 2.0 is enabled, the broker accepts one or no users. |

### CreateBrokerOutput
<a name="brokers-model-createbrokeroutput"></a>

Returns information about the created broker.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| brokerArn | string | False | The broker's Amazon Resource Name (ARN). |
| brokerId | string | False | The unique ID that Amazon MQ generates for the broker. |

### DataReplicationMode
<a name="brokers-model-datareplicationmode"></a>

Specifies whether a broker is a part of a data replication pair.
+ `NONE`
+ `CRDR`

### DeploymentMode
<a name="brokers-model-deploymentmode"></a>

The broker's deployment mode.
+ `SINGLE_INSTANCE`
+ `ACTIVE_STANDBY_MULTI_AZ`
+ `CLUSTER_MULTI_AZ`

### EfsBrokerStorageConfiguration
<a name="brokers-model-efsbrokerstorageconfiguration"></a>

The storage configuration of an EFS broker storage

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| throughputMode | string<br />Values: `ELASTIC \| STANDARD` | False | Throughput mode of EFS broker storage |

### EncryptionOptions
<a name="brokers-model-encryptionoptions"></a>

Encryption options for the broker.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| kmsKeyId | string | False | The customer master key (CMK) to use for the A AWS KMS (KMS). This key is used to encrypt your data at rest. If not provided, Amazon MQ will use a default CMK to encrypt your data. |
| useAwsOwnedKey | boolean | True | Enables the use of an AWS owned CMK using AWS KMS (KMS). Set to `true` by default, if no value is provided, for example, for RabbitMQ brokers. |

### EngineType
<a name="brokers-model-enginetype"></a>

The type of broker engine. Amazon MQ supports ActiveMQ and RabbitMQ.
+ `ACTIVEMQ`
+ `RABBITMQ`

### Error
<a name="brokers-model-error"></a>

Returns information about an error.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| errorAttribute | string | False | The attribute which caused the error. |
| message | string | False | The explanation of the error. |

### LdapServerMetadataInput
<a name="brokers-model-ldapservermetadatainput"></a>

Optional. The metadata of the LDAP server used to authenticate and authorize connections to the broker.

**Important**
Does not apply to RabbitMQ brokers.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| hosts | Array of type string | True | Specifies the location of the LDAP server such as AWS Directory Service for Microsoft Active Directory. Optional failover server. |
| roleBase | string | True | The distinguished name of the node in the directory information tree (DIT) to search for roles or groups. For example, `ou=group, ou=corp, dc=corp, dc=example, dc=com`. |
| roleName | string | False | Specifies the LDAP attribute that identifies the group name attribute in the object returned from the group membership query. |
| roleSearchMatching | string | True | The LDAP search filter used to find roles within the `roleBase`. The distinguished name of the user matched by `userSearchMatching` is substituted into the `{0}` placeholder in the search filter. The client's username is substituted into the `{1}` placeholder. For example, if you set this option to `(member=uid={1})`for the user `janedoe`, the search filter becomes `(member=uid=janedoe)` after string substitution. It matches all role entries that have a member attribute equal to `uid=janedoe` under the subtree selected by the `roleBase`. |
| roleSearchSubtree | boolean | False | The directory search scope for the role. If set to true, scope is to search the entire subtree. |
| serviceAccountPassword | string | True | Service account password. A service account is an account in your LDAP server that has access to initiate a connection. For example, `cn=admin,dc=corp, dc=example, dc=com`. |
| serviceAccountUsername | string | True | Service account username. A service account is an account in your LDAP server that has access to initiate a connection. For example, `cn=admin,dc=corp, dc=example, dc=com`. |
| userBase | string | True | Select a particular subtree of the directory information tree (DIT) to search for user entries. The subtree is specified by a DN, which specifies the base node of the subtree. For example, by setting this option to `ou=Users,ou=corp, dc=corp, dc=example, dc=com`, the search for user entries is restricted to the subtree beneath `ou=Users, ou=corp, dc=corp, dc=example, dc=com`. |
| userRoleName | string | False | Specifies the name of the LDAP attribute for the user group membership. |
| userSearchMatching | string | True | The LDAP search filter used to find users within the `userBase`. The client's username is substituted into the `{0}` placeholder in the search filter. For example, if this option is set to `(uid={0})` and the received username is `janedoe`, the search filter becomes `(uid=janedoe)` after string substitution. It will result in matching an entry like `uid=janedoe, ou=Users,ou=corp, dc=corp, dc=example, dc=com`. |
| userSearchSubtree | boolean | False | The directory search scope for the user. If set to true, scope is to search the entire subtree. |

### ListBrokersOutput
<a name="brokers-model-listbrokersoutput"></a>

A list of information about all brokers.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| brokerSummaries | Array of type [BrokerSummary](#brokers-model-brokersummary) | False | A list of information about all brokers. |
| nextToken | string | False | The token that specifies the next page of results Amazon MQ should return. To request the first page, leave nextToken empty. |

### Logs
<a name="brokers-model-logs"></a>

The list of information about logs to be enabled for the specified broker.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| audit | boolean | False | Enables audit logging. Every user management action made using JMX or the ActiveMQ Web Console is logged. Does not apply to RabbitMQ brokers. |
| general | boolean | False | Enables general logging. |

### User
<a name="brokers-model-user"></a>

A user associated with the broker. For Amazon MQ for RabbitMQ brokers, one and only one administrative user is accepted and created when a broker is first provisioned. All subsequent broker users are created by making RabbitMQ API calls directly to brokers or via the RabbitMQ web console.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| consoleAccess | boolean | False | Enables access to the ActiveMQ Web Console for the ActiveMQ user. Does not apply to RabbitMQ brokers. |
| groups | Array of type string | False | The list of groups (20 maximum) to which the ActiveMQ user belongs. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . \_ \~). This value must be 2-100 characters long. Does not apply to RabbitMQ brokers. |
| password | string<br />Format: password | True |  Required. The password of the user. This value must be at least 12 characters long, must contain at least 4 unique characters, and must not contain commas, colons, or equal signs (,:=). |
| replicationUser | boolean | False | Defines if this user is intended for CRDR replication purposes. |
| username | string | True | The username of the broker user. The following restrictions apply to broker usernames:+   For Amazon MQ for ActiveMQ brokers, this value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . \_ \~). This value must be 2-100 characters long.  <br />+  For Amazon MQ for RabbitMQ brokers, this value can contain only alphanumeric characters, dashes, periods, underscores (- . \_). This value must not contain a tilde (\~) character. Amazon MQ prohibts using `guest` as a valid usename. This value must be 2-100 characters long.   Do not add personally identifiable information (PII) or other confidential or sensitive information in broker usernames. Broker usernames are accessible to other AWS services, including CloudWatch Logs. Broker usernames are not intended to be used for private or sensitive data.   |

### WeeklyStartTime
<a name="brokers-model-weeklystarttime"></a>

The scheduled time period relative to UTC during which Amazon MQ begins to apply pending updates or patches to the broker.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| dayOfWeek | string<br />Values: `MONDAY \| TUESDAY \| WEDNESDAY \| THURSDAY \| FRIDAY \| SATURDAY \| SUNDAY` | True | Required. The day of the week. |
| timeOfDay | string | True | Required. The time, in 24-hour format. |
| timeZone | string | False | The time zone, UTC by default, in either the Country/City format, or the UTC offset format. |

## See also
<a name="brokers-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### ListBrokers
<a name="ListBrokers-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/mq-2017-11-27/ListBrokers)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/mq-2017-11-27/ListBrokers)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/mq-2017-11-27/ListBrokers)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/mq-2017-11-27/ListBrokers)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/mq-2017-11-27/ListBrokers)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/mq-2017-11-27/ListBrokers)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/mq-2017-11-27/ListBrokers)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/mq-2017-11-27/ListBrokers)
+ [AWS SDK for Python](/goto/boto3/mq-2017-11-27/ListBrokers)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/mq-2017-11-27/ListBrokers)

### CreateBroker
<a name="CreateBroker-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/mq-2017-11-27/CreateBroker)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/mq-2017-11-27/CreateBroker)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/mq-2017-11-27/CreateBroker)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/mq-2017-11-27/CreateBroker)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/mq-2017-11-27/CreateBroker)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/mq-2017-11-27/CreateBroker)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/mq-2017-11-27/CreateBroker)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/mq-2017-11-27/CreateBroker)
+ [AWS SDK for Python](/goto/boto3/mq-2017-11-27/CreateBroker)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/mq-2017-11-27/CreateBroker)
