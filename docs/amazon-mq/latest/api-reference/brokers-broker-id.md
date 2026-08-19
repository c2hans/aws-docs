---
source_url: https://docs.aws.amazon.com/amazon-mq/latest/api-reference/brokers-broker-id.html
---

# Broker
<a name="brokers-broker-id"></a>

A broker is a message broker environment running on Amazon MQ. It is the basic building block of Amazon MQ. For more information about the different components of an Amazon MQ broker, see [How Amazon MQ works](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/amazon-mq-how-it-works.html) in the *Amazon MQ Developer Guide*.

## URI
<a name="brokers-broker-id-url"></a>

`/v1/brokers/{{broker-id}}`

## HTTP methods
<a name="brokers-broker-id-http-methods"></a>

### GET
<a name="brokers-broker-idget"></a>

**Operation ID:** `DescribeBroker`

Returns information about the specified broker.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{broker-id}} | String | True | The unique ID that Amazon MQ generates for the broker. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 |  DescribeBrokerOutput | HTTP Status Code 200: OK. |
| 400 | Error | HTTP Status Code 400: Bad request due to incorrect input. Correct your request and then retry it. |
| 403 | Error | HTTP Status Code 403: Access forbidden. Correct your credentials and then retry your request. |
| 404 | Error | HTTP Status Code 404: Resource not found due to incorrect input. Correct your request and then retry it. |
| 500 | Error | HTTP Status Code 500: Unexpected internal server error. Retrying your request might resolve the issue. |

### PUT
<a name="brokers-broker-idput"></a>

**Operation ID:** `UpdateBroker`

Adds a pending configuration change to a broker.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{broker-id}} | String | True | The unique ID that Amazon MQ generates for the broker. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 |  UpdateBrokerOutput | HTTP Status Code 200: OK. |
| 400 | Error | HTTP Status Code 400: Bad request due to incorrect input. Correct your request and then retry it. |
| 403 | Error | HTTP Status Code 403: Access forbidden. Correct your credentials and then retry your request. |
| 404 | Error | HTTP Status Code 404: Resource not found due to incorrect input. Correct your request and then retry it. |
| 409 | Error | HTTP Status Code 409: Configuration ID is already in use. Remove the configuration from all brokers and retry the request. |
| 500 | Error | HTTP Status Code 500: Unexpected internal server error. Retrying your request might resolve the issue. |

### DELETE
<a name="brokers-broker-iddelete"></a>

**Operation ID:** `DeleteBroker`

Deletes a broker. Note: This API is asynchronous.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{broker-id}} | String | True | The unique ID that Amazon MQ generates for the broker. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 |  DeleteBrokerOutput | HTTP Status Code 200: OK. |
| 400 | Error | HTTP Status Code 400: Bad request due to incorrect input. Correct your request and then retry it. |
| 403 | Error | HTTP Status Code 403: Access forbidden. Correct your credentials and then retry your request. |
| 404 | Error | HTTP Status Code 404: Resource not found due to incorrect input. Correct your request and then retry it. |
| 500 | Error | HTTP Status Code 500: Unexpected internal server error. Retrying your request might resolve the issue. |

### OPTIONS
<a name="brokers-broker-idoptions"></a>

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{broker-id}} | String | True | The unique ID that Amazon MQ generates for the broker. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | Default response for CORS method |

## Schemas
<a name="brokers-broker-id-schemas"></a>

### Request bodies
<a name="brokers-broker-id-request-examples"></a>

#### PUT schema
<a name="brokers-broker-id-request-body-put-example"></a>

```
{
  "dataReplicationMode": enum,
  "engineVersion": "string",
  "maintenanceWindowStartTime": {
    "dayOfWeek": enum,
    "timeZone": "string",
    "timeOfDay": "string"
  },
  "configuration": {
    "id": "string",
    "revision": integer
  },
  "storageConfiguration": {
    "efs": {
      "throughputMode": enum
    }
  },
  "storageSize": integer,
  "authenticationStrategy": enum,
  "securityGroups": [
    "string"
  ],
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
  "logs": {
    "general": boolean,
    "audit": boolean
  },
  "hostInstanceType": "string",
  "autoMinorVersionUpgrade": boolean,
  "resourceShareArns": [
    "string"
  ]
}
```

### Response bodies
<a name="brokers-broker-id-response-examples"></a>

#### DescribeBrokerOutput schema
<a name="brokers-broker-id-response-body-describebrokeroutput-example"></a>

```
{
  "pendingEngineVersion": "string",
  "pendingAuthenticationStrategy": enum,
  "pendingSecurityGroups": [
    "string"
  ],
  "configurations": {
    "current": {
      "id": "string",
      "revision": integer
    },
    "pending": {
      "id": "string",
      "revision": integer
    },
    "history": [
      {
        "id": "string",
        "revision": integer
      }
    ]
  },
  "brokerState": enum,
  "pendingDataReplicationMode": enum,
  "engineType": enum,
  "brokerInstances": [
    {
      "endpoints": [
        "string"
      ],
      "consoleURL": "string",
      "ipAddress": "string"
    }
  ],
  "hostInstanceType": "string",
  "dataReplicationMode": enum,
  "storageConfiguration": {
    "efs": {
      "throughputMode": enum
    }
  },
  "storageSize": integer,
  "pendingStorageSize": integer,
  "publiclyAccessible": boolean,
  "logs": {
    "generalLogGroup": "string",
    "general": boolean,
    "audit": boolean,
    "pending": {
      "general": boolean,
      "audit": boolean
    },
    "auditLogGroup": "string"
  },
  "ldapServerMetadata": {
    "roleSearchMatching": "string",
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
  "subnetIds": [
    "string"
  ],
  "pendingHostInstanceType": "string",
  "engineVersion": "string",
  "brokerArn": "string",
  "brokerId": "string",
  "deploymentMode": enum,
  "maintenanceWindowStartTime": {
    "dayOfWeek": enum,
    "timeZone": "string",
    "timeOfDay": "string"
  },
  "created": "string",
  "authenticationStrategy": enum,
  "users": [
    {
      "pendingChange": enum,
      "username": "string"
    }
  ],
  "pendingStorageConfiguration": {
    "efs": {
      "throughputMode": enum
    }
  },
  "tags": {
  },
  "dataReplicationMetadata": {
    "dataReplicationCounterpart": {
      "brokerId": "string",
      "region": "string"
    },
    "dataReplicationRole": "string"
  },
  "pendingLdapServerMetadata": {
    "roleSearchMatching": "string",
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
  "encryptionOptions": {
    "useAwsOwnedKey": boolean,
    "kmsKeyId": "string"
  },
  "pendingDataReplicationMetadata": {
    "dataReplicationCounterpart": {
      "brokerId": "string",
      "region": "string"
    },
    "dataReplicationRole": "string"
  },
  "storageType": enum,
  "actionsRequired": [
    {
      "actionRequiredCode": "string",
      "actionRequiredInfo": "string"
    }
  ],
  "securityGroups": [
    "string"
  ],
  "brokerName": "string",
  "autoMinorVersionUpgrade": boolean
}
```

#### UpdateBrokerOutput schema
<a name="brokers-broker-id-response-body-updatebrokeroutput-example"></a>

```
{
  "engineVersion": "string",
  "brokerId": "string",
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
  "pendingDataReplicationMode": enum,
  "hostInstanceType": "string",
  "pendingStorageConfiguration": {
    "efs": {
      "throughputMode": enum
    }
  },
  "dataReplicationMode": enum,
  "dataReplicationMetadata": {
    "dataReplicationCounterpart": {
      "brokerId": "string",
      "region": "string"
    },
    "dataReplicationRole": "string"
  },
  "storageSize": integer,
  "pendingDataReplicationMetadata": {
    "dataReplicationCounterpart": {
      "brokerId": "string",
      "region": "string"
    },
    "dataReplicationRole": "string"
  },
  "securityGroups": [
    "string"
  ],
  "logs": {
    "general": boolean,
    "audit": boolean
  },
  "ldapServerMetadata": {
    "roleSearchMatching": "string",
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
  "resourceShareArns": [
    "string"
  ]
}
```

#### DeleteBrokerOutput schema
<a name="brokers-broker-id-response-body-deletebrokeroutput-example"></a>

```
{
  "brokerId": "string"
}
```

#### Error schema
<a name="brokers-broker-id-response-body-error-example"></a>

```
{
  "errorAttribute": "string",
  "message": "string"
}
```

## Properties
<a name="brokers-broker-id-properties"></a>

### ActionRequired
<a name="brokers-broker-id-model-actionrequired"></a>

Action required for a broker.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| actionRequiredCode | string | False | The code you can use to find instructions on the action required to resolve your broker issue. |
| actionRequiredInfo | string | False | Information about the action required to resolve your broker issue. |

### AuthenticationStrategy
<a name="brokers-broker-id-model-authenticationstrategy"></a>

Optional. The authentication strategy used to secure the broker. The default is `SIMPLE`.
+ `SIMPLE`
+ `LDAP`
+ `CONFIG_MANAGED`

### BrokerInstance
<a name="brokers-broker-id-model-brokerinstance"></a>

Returns information about all brokers.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| consoleURL | string | False | The brokers web console URL. |
| endpoints | Array of type string | False | The broker's wire-level protocol endpoints. |
| ipAddress | string | False | The IP address of the Elastic Network Interface (ENI) attached to the broker. Does not apply to RabbitMQ brokers. |

### BrokerState
<a name="brokers-broker-id-model-brokerstate"></a>

The broker's status.
+ `CREATION_IN_PROGRESS`
+ `CREATION_FAILED`
+ `DELETION_IN_PROGRESS`
+ `RUNNING`
+ `REBOOT_IN_PROGRESS`
+ `CRITICAL_ACTION_REQUIRED`
+ `REPLICA`

### BrokerStorageConfiguration
<a name="brokers-broker-id-model-brokerstorageconfiguration"></a>

The storage configurations of a broker.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| efs | [EfsBrokerStorageConfiguration](#brokers-broker-id-model-efsbrokerstorageconfiguration) | False |  |

### BrokerStorageType
<a name="brokers-broker-id-model-brokerstoragetype"></a>

The broker's storage type.

**Important**
 `EFS` is not supported for RabbitMQ engine type.
+ `EBS`
+ `EFS`

### ChangeType
<a name="brokers-broker-id-model-changetype"></a>

The type of change pending for the ActiveMQ user.
+ `CREATE`
+ `UPDATE`
+ `DELETE`

### ConfigurationId
<a name="brokers-broker-id-model-configurationid"></a>

A list of information about the configuration.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| id | string | True | Required. The unique ID that Amazon MQ generates for the configuration. |
| revision | integer | False | The revision number of the configuration. |

### Configurations
<a name="brokers-broker-id-model-configurations"></a>

Broker configuration information

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| current | [ConfigurationId](#brokers-broker-id-model-configurationid) | False | The broker's current configuration. |
| history | Array of type [ConfigurationId](#brokers-broker-id-model-configurationid) | False | The history of configurations applied to the broker. |
| pending | [ConfigurationId](#brokers-broker-id-model-configurationid) | False | The broker's pending configuration. |

### DataReplicationCounterpart
<a name="brokers-broker-id-model-datareplicationcounterpart"></a>

Specifies a broker in a data replication pair.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| brokerId | string | True | Required. The unique broker id generated by Amazon MQ. |
| region | string | True | Required. The region of the broker. |

### DataReplicationMetadataOutput
<a name="brokers-broker-id-model-datareplicationmetadataoutput"></a>

The replication details of the data replication-enabled broker. Only returned if dataReplicationMode or pendingDataReplicationMode is set to CRDR.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| dataReplicationCounterpart | [DataReplicationCounterpart](#brokers-broker-id-model-datareplicationcounterpart) | False | Describes the replica/primary broker. Only returned if this broker is currently set as a primary or replica in the broker's dataReplicationRole property. |
| dataReplicationRole | string | True | Defines the role of this broker in a data replication pair. When a replica broker is promoted to primary, this role is interchanged. |

### DataReplicationMode
<a name="brokers-broker-id-model-datareplicationmode"></a>

Specifies whether a broker is a part of a data replication pair.
+ `NONE`
+ `CRDR`

### DeleteBrokerOutput
<a name="brokers-broker-id-model-deletebrokeroutput"></a>

Returns information about the deleted broker.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| brokerId | string | False | The unique ID that Amazon MQ generates for the broker. |

### DeploymentMode
<a name="brokers-broker-id-model-deploymentmode"></a>

The broker's deployment mode.
+ `SINGLE_INSTANCE`
+ `ACTIVE_STANDBY_MULTI_AZ`
+ `CLUSTER_MULTI_AZ`

### DescribeBrokerOutput
<a name="brokers-broker-id-model-describebrokeroutput"></a>

Returns information about the specified broker.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| actionsRequired | Array of type [ActionRequired](#brokers-broker-id-model-actionrequired) | False | Actions required for a broker. |
| authenticationStrategy | [AuthenticationStrategy](#brokers-broker-id-model-authenticationstrategy) | False | The authentication strategy used to secure the broker. The default is `SIMPLE`. |
| autoMinorVersionUpgrade | boolean | True | Enables automatic upgrades to new patch versions for brokers as new versions are released and supported by Amazon MQ. Automatic upgrades occur during the scheduled maintenance window or after a manual broker reboot. |
| brokerArn | string | False | The broker's Amazon Resource Name (ARN). |
| brokerId | string | False | The unique ID that Amazon MQ generates for the broker. |
| brokerInstances | Array of type [BrokerInstance](#brokers-broker-id-model-brokerinstance) | False | A list of information about allocated brokers. |
| brokerName | string | False | The broker's name. This value must be unique in your AWS account account, 1-50 characters long, must contain only letters, numbers, dashes, and underscores, and must not contain white spaces, brackets, wildcard characters, or special characters. |
| brokerState | [BrokerState](#brokers-broker-id-model-brokerstate) | False | The broker's status. |
| configurations | [Configurations](#brokers-broker-id-model-configurations) | False | The list of all revisions for the specified configuration. |
| created | string<br />Format: date-time | False | The time when the broker was created. |
| dataReplicationMetadata | [DataReplicationMetadataOutput](#brokers-broker-id-model-datareplicationmetadataoutput) | False | The replication details of the data replication-enabled broker. Only returned if dataReplicationMode is set to CRDR. |
| dataReplicationMode | [DataReplicationMode](#brokers-broker-id-model-datareplicationmode) | False | Describes whether this broker is a part of a data replication pair. |
| deploymentMode | [DeploymentMode](#brokers-broker-id-model-deploymentmode) | True | The broker's deployment mode. |
| encryptionOptions | [EncryptionOptions](#brokers-broker-id-model-encryptionoptions) | False | Encryption options for the broker. |
| engineType | [EngineType](#brokers-broker-id-model-enginetype) | True | The type of broker engine. Currently, Amazon MQ supports `ACTIVEMQ` and `RABBITMQ`. |
| engineVersion | string | False | The broker engine version. For more information, see the [ActiveMQ version management](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/activemq-version-management.html) and the [RabbitMQ version management](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/rabbitmq-version-management.html) sections in the Amazon MQ Developer Guide. |
| hostInstanceType | string | False | The broker's instance type. |
| ldapServerMetadata | [LdapServerMetadataOutput](#brokers-broker-id-model-ldapservermetadataoutput) | False | The metadata of the LDAP server used to authenticate and authorize connections to the broker. |
| logs | [LogsSummary](#brokers-broker-id-model-logssummary) | False | The list of information about logs currently enabled and pending to be deployed for the specified broker. |
| maintenanceWindowStartTime | [WeeklyStartTime](#brokers-broker-id-model-weeklystarttime) | False | The parameters that determine the WeeklyStartTime. |
| pendingAuthenticationStrategy | [AuthenticationStrategy](#brokers-broker-id-model-authenticationstrategy) | False | The authentication strategy that will be applied when the broker is rebooted. The default is `SIMPLE`. |
| pendingDataReplicationMetadata | [DataReplicationMetadataOutput](#brokers-broker-id-model-datareplicationmetadataoutput) | False | The pending replication details of the data replication-enabled broker. Only returned if pendingDataReplicationMode is set to CRDR. |
| pendingDataReplicationMode | [DataReplicationMode](#brokers-broker-id-model-datareplicationmode) | False | Describes whether this broker will be a part of a data replication pair after reboot. |
| pendingEngineVersion | string | False | The broker engine version to upgrade to. For more information, see the [ActiveMQ version management](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/activemq-version-management.html) and the [RabbitMQ version management](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/rabbitmq-version-management.html) sections in the Amazon MQ Developer Guide. |
| pendingHostInstanceType | string | False | The broker's host instance type to upgrade to. For a list of supported instance types, see [Broker instance types](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/broker-instance-types). |
| pendingLdapServerMetadata | [LdapServerMetadataOutput](#brokers-broker-id-model-ldapservermetadataoutput) | False | The metadata of the LDAP server that will be used to authenticate and authorize connections to the broker after it is rebooted. |
| pendingSecurityGroups | Array of type string | False | The list of pending security groups to authorize connections to brokers. |
| pendingStorageConfiguration | [BrokerStorageConfiguration](#brokers-broker-id-model-brokerstorageconfiguration) | False | The pending broker's storage configuration. |
| pendingStorageSize | integer | False | The pending storage size in GB, applied after the next broker restart. Present only when a storage size update is pending. |
| publiclyAccessible | boolean | True | Enables connections from applications outside of the VPC that hosts the broker's subnets. |
| securityGroups | Array of type string | False | The list of rules (1 minimum, 125 maximum) that authorize connections to brokers. |
| storageConfiguration | [BrokerStorageConfiguration](#brokers-broker-id-model-brokerstorageconfiguration) | False | The broker's storage configuration. |
| storageSize | integer | False | The broker's storage size in GB. Present only when the broker has a custom storage size that differs from the instance-type default. |
| storageType | [BrokerStorageType](#brokers-broker-id-model-brokerstoragetype) | False | The broker's storage type. |
| subnetIds | Array of type string | False | The list of groups that define which subnets and IP ranges the broker can use from different Availability Zones. |
| tags | object | False | The list of all tags associated with this broker. |
| users | Array of type [UserSummary](#brokers-broker-id-model-usersummary) | False | The list of all broker usernames for the specified broker. |

### EfsBrokerStorageConfiguration
<a name="brokers-broker-id-model-efsbrokerstorageconfiguration"></a>

The storage configuration of an EFS broker storage

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| throughputMode | string<br />Values: `ELASTIC \| STANDARD` | False | Throughput mode of EFS broker storage |

### EncryptionOptions
<a name="brokers-broker-id-model-encryptionoptions"></a>

Encryption options for the broker.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| kmsKeyId | string | False | The customer master key (CMK) to use for the A AWS KMS (KMS). This key is used to encrypt your data at rest. If not provided, Amazon MQ will use a default CMK to encrypt your data. |
| useAwsOwnedKey | boolean | True | Enables the use of an AWS owned CMK using AWS KMS (KMS). Set to `true` by default, if no value is provided, for example, for RabbitMQ brokers. |

### EngineType
<a name="brokers-broker-id-model-enginetype"></a>

The type of broker engine. Amazon MQ supports ActiveMQ and RabbitMQ.
+ `ACTIVEMQ`
+ `RABBITMQ`

### Error
<a name="brokers-broker-id-model-error"></a>

Returns information about an error.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| errorAttribute | string | False | The attribute which caused the error. |
| message | string | False | The explanation of the error. |

### LdapServerMetadataInput
<a name="brokers-broker-id-model-ldapservermetadatainput"></a>

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

### LdapServerMetadataOutput
<a name="brokers-broker-id-model-ldapservermetadataoutput"></a>

Optional. The metadata of the LDAP server used to authenticate and authorize connections to the broker.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| hosts | Array of type string | True | Specifies the location of the LDAP server such as AWS Directory Service for Microsoft Active Directory. Optional failover server. |
| roleBase | string | True | The distinguished name of the node in the directory information tree (DIT) to search for roles or groups. For example, `ou=group, ou=corp, dc=corp, dc=example, dc=com`. |
| roleName | string | False | Specifies the LDAP attribute that identifies the group name attribute in the object returned from the group membership query. |
| roleSearchMatching | string | True | The LDAP search filter used to find roles within the `roleBase`. The distinguished name of the user matched by `userSearchMatching` is substituted into the `{0}` placeholder in the search filter. The client's username is substituted into the `{1}` placeholder. For example, if you set this option to `(member=uid={1})`for the user `janedoe`, the search filter becomes `(member=uid=janedoe)` after string substitution. It matches all role entries that have a member attribute equal to `uid=janedoe` under the subtree selected by the `roleBase`. |
| roleSearchSubtree | boolean | False | The directory search scope for the role. If set to true, scope is to search the entire subtree. |
| serviceAccountUsername | string | True | Service account username. A service account is an account in your LDAP server that has access to initiate a connection. For example, `cn=admin,dc=corp, dc=example, dc=com`. |
| userBase | string | True | Select a particular subtree of the directory information tree (DIT) to search for user entries. The subtree is specified by a DN, which specifies the base node of the subtree. For example, by setting this option to `ou=Users,ou=corp, dc=corp, dc=example, dc=com`, the search for user entries is restricted to the subtree beneath `ou=Users, ou=corp, dc=corp, dc=example, dc=com`. |
| userRoleName | string | False | Specifies the name of the LDAP attribute for the user group membership. |
| userSearchMatching | string | True | The LDAP search filter used to find users within the `userBase`. The client's username is substituted into the `{0}` placeholder in the search filter. For example, if this option is set to `(uid={0})` and the received username is `janedoe`, the search filter becomes `(uid=janedoe)` after string substitution. It will result in matching an entry like `uid=janedoe, ou=Users,ou=corp, dc=corp, dc=example, dc=com`. |
| userSearchSubtree | boolean | False | The directory search scope for the user. If set to true, scope is to search the entire subtree. |

### Logs
<a name="brokers-broker-id-model-logs"></a>

The list of information about logs to be enabled for the specified broker.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| audit | boolean | False | Enables audit logging. Every user management action made using JMX or the ActiveMQ Web Console is logged. Does not apply to RabbitMQ brokers. |
| general | boolean | False | Enables general logging. |

### LogsSummary
<a name="brokers-broker-id-model-logssummary"></a>

The list of information about logs currently enabled and pending to be deployed for the specified broker.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| audit | boolean | False | Enables audit logging. Every user management action made using JMX or the ActiveMQ Web Console is logged. |
| auditLogGroup | string | False | The location of the CloudWatch Logs log group where audit logs are sent. |
| general | boolean | True | Enables general logging. |
| generalLogGroup | string | True | The location of the CloudWatch Logs log group where general logs are sent. |
| pending | [PendingLogs](#brokers-broker-id-model-pendinglogs) | False | The list of information about logs pending to be deployed for the specified broker. |

### PendingLogs
<a name="brokers-broker-id-model-pendinglogs"></a>

The list of information about logs to be enabled for the specified broker.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| audit | boolean | False | Enables audit logging. Every user management action made using JMX or the ActiveMQ Web Console is logged. |
| general | boolean | False | Enables general logging. |

### UpdateBrokerInput
<a name="brokers-broker-id-model-updatebrokerinput"></a>

Updates the broker using the specified properties.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| authenticationStrategy | [AuthenticationStrategy](#brokers-broker-id-model-authenticationstrategy) | False | Optional. The authentication strategy used to secure the broker. The default is `SIMPLE`. |
| autoMinorVersionUpgrade | boolean | False | Enables automatic upgrades to new patch versions for brokers as new versions are released and supported by Amazon MQ. Automatic upgrades occur during the scheduled maintenance window or after a manual broker reboot.Must be set to `true` for ActiveMQ brokers version 5.18 and above and for RabbitMQ brokers version 3.13 and above. |
| configuration | [ConfigurationId](#brokers-broker-id-model-configurationid) | False | A list of information about the configuration. |
| dataReplicationMode | [DataReplicationMode](#brokers-broker-id-model-datareplicationmode) | False | Defines whether this broker is a part of a data replication pair. |
| engineVersion | string | False | The broker engine version. For more information, see the [ActiveMQ version management](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/activemq-version-management.html) and the [RabbitMQ version management](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/rabbitmq-version-management.html) sections in the Amazon MQ Developer Guide.When upgrading to ActiveMQ version 5.18 and above or RabbitMQ version 3.13 and above, you must have `autoMinorVersionUpgrade` set to `true` for the broker. |
| hostInstanceType | string | False | The broker's host instance type to upgrade to. For a list of supported instance types, see [Broker instance types](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/broker-instance-types). |
| ldapServerMetadata | [LdapServerMetadataInput](#brokers-broker-id-model-ldapservermetadatainput) | False | Optional. The metadata of the LDAP server used to authenticate and authorize connections to the broker. Does not apply to RabbitMQ brokers. |
| logs | [Logs](#brokers-broker-id-model-logs) | False | Enables Amazon CloudWatch logging for brokers. |
| maintenanceWindowStartTime | [WeeklyStartTime](#brokers-broker-id-model-weeklystarttime) | False | The parameters that determine the WeeklyStartTime. |
| resourceShareArns | Array of type string | False | The list of resource shares to update on the broker. |
| securityGroups | Array of type string | False | The list of security groups (1 minimum, 5 maximum) that authorizes connections to brokers. |
| storageConfiguration | [BrokerStorageConfiguration](#brokers-broker-id-model-brokerstorageconfiguration) | False | The broker's storage configuration. |
| storageSize | integer | False | The broker's storage size in GB. Applies only to RabbitMQ version 4.x brokers with `CLUSTER_MULTI_AZ` deployment mode on `mq.m7g` instance types. Set to `0` to reset the storage size to the instance-type default. The updated storage size takes effect after the broker restarts. For more information about allowed storage size ranges, see [Instance types](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/rmq-broker-instance-types.html) in the *Amazon MQ Developer Guide*. |

### UpdateBrokerOutput
<a name="brokers-broker-id-model-updatebrokeroutput"></a>

Returns information about the updated broker.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| authenticationStrategy | [AuthenticationStrategy](#brokers-broker-id-model-authenticationstrategy) | False | Optional. The authentication strategy used to secure the broker. The default is `SIMPLE`. |
| autoMinorVersionUpgrade | boolean | False | Enables automatic upgrades to new patch versions for brokers as new versions are released and supported by Amazon MQ. Automatic upgrades occur during the scheduled maintenance window or after a manual broker reboot. |
| brokerId | string | True | Required. The unique ID that Amazon MQ generates for the broker. |
| configuration | [ConfigurationId](#brokers-broker-id-model-configurationid) | False | The ID of the updated configuration. |
| dataReplicationMetadata | [DataReplicationMetadataOutput](#brokers-broker-id-model-datareplicationmetadataoutput) | False | The replication details of the data replication-enabled broker. Only returned if dataReplicationMode is set to CRDR. |
| dataReplicationMode | [DataReplicationMode](#brokers-broker-id-model-datareplicationmode) | False | Describes whether this broker is a part of a data replication pair. |
| engineVersion | string | False | The broker engine version to upgrade to. For more information, see the [ActiveMQ version management](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/activemq-version-management.html) and the [RabbitMQ version management](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/rabbitmq-version-management.html) sections in the Amazon MQ Developer Guide. |
| hostInstanceType | string | False | The broker's host instance type to upgrade to. For a list of supported instance types, see [Broker instance types](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/broker-instance-types). |
| ldapServerMetadata | [LdapServerMetadataOutput](#brokers-broker-id-model-ldapservermetadataoutput) | False | Optional. The metadata of the LDAP server used to authenticate and authorize connections to the broker. Does not apply to RabbitMQ brokers. |
| logs | [Logs](#brokers-broker-id-model-logs) | False | The list of information about logs to be enabled for the specified broker. |
| maintenanceWindowStartTime | [WeeklyStartTime](#brokers-broker-id-model-weeklystarttime) | False | The parameters that determine the WeeklyStartTime. |
| pendingDataReplicationMetadata | [DataReplicationMetadataOutput](#brokers-broker-id-model-datareplicationmetadataoutput) | False | The pending replication details of the data replication-enabled broker. Only returned if pendingDataReplicationMode is set to CRDR. |
| pendingDataReplicationMode | [DataReplicationMode](#brokers-broker-id-model-datareplicationmode) | False | Describes whether this broker will be a part of a data replication pair after reboot. |
| pendingStorageConfiguration | [BrokerStorageConfiguration](#brokers-broker-id-model-brokerstorageconfiguration) | False | The pending broker's storage configuration. |
| resourceShareArns | Array of type string | False | The pending broker's target list of resource shares. |
| securityGroups | Array of type string | False | The list of security groups (1 minimum, 5 maximum) that authorizes connections to brokers. |
| storageSize | integer | False | The broker's storage size in GB. |

### UserSummary
<a name="brokers-broker-id-model-usersummary"></a>

Returns a list of all broker users. Does not apply to RabbitMQ brokers.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| pendingChange | [ChangeType](#brokers-broker-id-model-changetype) | False | The type of change pending for the broker user. |
| username | string | True | Required. The username of the broker user. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . \_ \~). This value must be 2-100 characters long. |

### WeeklyStartTime
<a name="brokers-broker-id-model-weeklystarttime"></a>

The scheduled time period relative to UTC during which Amazon MQ begins to apply pending updates or patches to the broker.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| dayOfWeek | string<br />Values: `MONDAY \| TUESDAY \| WEDNESDAY \| THURSDAY \| FRIDAY \| SATURDAY \| SUNDAY` | True | Required. The day of the week. |
| timeOfDay | string | True | Required. The time, in 24-hour format. |
| timeZone | string | False | The time zone, UTC by default, in either the Country/City format, or the UTC offset format. |

## See also
<a name="brokers-broker-id-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### DescribeBroker
<a name="DescribeBroker-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/mq-2017-11-27/DescribeBroker)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/mq-2017-11-27/DescribeBroker)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/mq-2017-11-27/DescribeBroker)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/mq-2017-11-27/DescribeBroker)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/mq-2017-11-27/DescribeBroker)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/mq-2017-11-27/DescribeBroker)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/mq-2017-11-27/DescribeBroker)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/mq-2017-11-27/DescribeBroker)
+ [AWS SDK for Python](/goto/boto3/mq-2017-11-27/DescribeBroker)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/mq-2017-11-27/DescribeBroker)

### UpdateBroker
<a name="UpdateBroker-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/mq-2017-11-27/UpdateBroker)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/mq-2017-11-27/UpdateBroker)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/mq-2017-11-27/UpdateBroker)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/mq-2017-11-27/UpdateBroker)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/mq-2017-11-27/UpdateBroker)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/mq-2017-11-27/UpdateBroker)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/mq-2017-11-27/UpdateBroker)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/mq-2017-11-27/UpdateBroker)
+ [AWS SDK for Python](/goto/boto3/mq-2017-11-27/UpdateBroker)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/mq-2017-11-27/UpdateBroker)

### DeleteBroker
<a name="DeleteBroker-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/mq-2017-11-27/DeleteBroker)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/mq-2017-11-27/DeleteBroker)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/mq-2017-11-27/DeleteBroker)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/mq-2017-11-27/DeleteBroker)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/mq-2017-11-27/DeleteBroker)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/mq-2017-11-27/DeleteBroker)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/mq-2017-11-27/DeleteBroker)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/mq-2017-11-27/DeleteBroker)
+ [AWS SDK for Python](/goto/boto3/mq-2017-11-27/DeleteBroker)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/mq-2017-11-27/DeleteBroker)
