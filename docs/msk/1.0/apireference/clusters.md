---
source_url: https://docs.aws.amazon.com/msk/1.0/apireference/clusters.html
---

# Clusters
<a name="clusters"></a>

Use this resource to create an Amazon MSK cluster and to get a list of existing clusters.

## URI
<a name="clusters-url"></a>

`/v1/clusters`

## HTTP methods
<a name="clusters-http-methods"></a>

### GET
<a name="clustersget"></a>

**Operation ID:** `ListClusters`

Returns a list of all the MSK clusters.

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| nextToken | String | False | The paginated results marker. When the result of the operation is truncated, the call returns `NextToken` in the response. To get the next batch, provide this token in your next request. |
| clusterNameFilter | String | False | Specify a prefix of the name of the clusters that you want to list. The service lists all the clusters whose names start with this prefix. |
| maxResults | String | False | The maximum number of results to return in the response (default maximum 100 results per API call). If there are more results, the response includes a `NextToken` parameter. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 |  ListClustersResponse | Successful response. |
| 400 | Error | The request isn't valid because the input is incorrect. Correct your input and then submit it again. |
| 401 | Error | The request is not authorized. The provided credentials couldn't be validated. |
| 403 | Error | Access forbidden. Check your credentials and then retry your request. |
| 404 | Error | The resource could not be found due to incorrect input. Correct the input, then retry the request. |
| 429 | Error | 429 response |
| 500 | Error | There was an unexpected internal server error. Retrying your request might resolve the issue. |
| 503 | Error | 503 response |

### POST
<a name="clusterspost"></a>

**Operation ID:** `CreateCluster`

Creates a new MSK cluster. The following Python 3.6 examples shows how you can create a cluster that's distributed over two Availability Zones. Before you run this Python script, replace the example subnet and security-group IDs with the IDs of your subnets and security group. When you create an MSK cluster, its brokers get evenly distributed over a number of Availability Zones that's equal to the number of subnets that you specify in the `BrokerNodeGroupInfo` parameter. In this example, you can add a third subnet to get a cluster that's distributed over three Availability Zones.

```
import boto3

client = boto3.client('kafka')

response = client.create_cluster(
    BrokerNodeGroupInfo={
        'BrokerAZDistribution': 'DEFAULT',
        'ClientSubnets': [
            'subnet-012345678901fedcba',
            'subnet-9876543210abcdef01'
        ],
        'InstanceType': 'kafka.m5.large',
        'SecurityGroups': [
            'sg-012345abcdef789789'
        ]
    },
    ClusterName='SalesCluster',
    EncryptionInfo={
        'EncryptionInTransit': {
            'ClientBroker': 'TLS_PLAINTEXT',
            'InCluster': True
        }
    },
    EnhancedMonitoring='PER_TOPIC_PER_BROKER',
    KafkaVersion='2.2.1',
    NumberOfBrokerNodes=2
)

print(response)
```

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 |  CreateClusterResponse | Successful response. |
| 400 | Error | The request isn't valid because the input is incorrect. Correct your input and then submit it again. |
| 401 | Error | The request is not authorized. The provided credentials couldn't be validated. |
| 403 | Error | Access forbidden. Check your credentials and then retry your request. |
| 404 | Error | The resource could not be found due to incorrect input. Correct the input, then retry the request. |
| 409 | Error | This cluster name already exists. Retry your request using another name. |
| 429 | Error | 429 response |
| 500 | Error | There was an unexpected internal server error. Retrying your request might resolve the issue. |
| 503 | Error | 503 response |

### OPTIONS
<a name="clustersoptions"></a>

Enable CORS by returning the correct headers.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | The default response for a CORS method. |

## Schemas
<a name="clusters-schemas"></a>

### Request bodies
<a name="clusters-request-examples"></a>

#### POST schema
<a name="clusters-request-body-post-example"></a>

```
{
  "encryptionInfo": {
    "encryptionInTransit": {
      "inCluster": boolean,
      "clientBroker": enum
    },
    "encryptionAtRest": {
      "dataVolumeKMSKeyId": "string"
    }
  },
  "configurationInfo": {
    "arn": "string",
    "revision": integer
  },
  "loggingInfo": {
    "brokerLogs": {
      "s3": {
        "bucket": "string",
        "prefix": "string",
        "enabled": boolean
      },
      "firehose": {
        "deliveryStream": "string",
        "enabled": boolean
      },
      "cloudWatchLogs": {
        "logGroup": "string",
        "enabled": boolean
      }
    },
    "authorizerLogs": {
      "s3": {
        "bucket": "string",
        "prefix": "string",
        "enabled": boolean
      },
      "firehose": {
        "deliveryStream": "string",
        "enabled": boolean
      },
      "cloudWatchLogs": {
        "logGroup": "string",
        "enabled": boolean
      }
    }
  },
  "tags": {
  },
  "numberOfBrokerNodes": integer,
  "enhancedMonitoring": enum,
  "storageMode": enum,
  "clusterName": "string",
  "kafkaVersion": "string",
  "clientAuthentication": {
    "sasl": {
      "iam": {
        "enabled": boolean
      },
      "scram": {
        "enabled": boolean
      }
    },
    "unauthenticated": {
      "enabled": boolean
    },
    "tls": {
      "certificateAuthorityArnList": [
        "string"
      ],
      "enabled": boolean
    }
  },
  "brokerNodeGroupInfo": {
    "clientSubnets": [
      "string"
    ],
    "zoneIds": [
      "string"
    ],
    "instanceType": "string",
    "connectivityInfo": {
      "vpcConnectivity": {
        "clientAuthentication": {
          "sasl": {
            "iam": {
              "enabled": boolean
            },
            "scram": {
              "enabled": boolean
            }
          },
          "tls": {
            "enabled": boolean
          }
        }
      },
      "publicAccess": {
        "type": "string"
      },
      "networkType": "string"
    },
    "securityGroups": [
      "string"
    ],
    "brokerAZDistribution": enum,
    "storageInfo": {
      "ebsStorageInfo": {
        "provisionedThroughput": {
          "volumeThroughput": integer,
          "enabled": boolean
        },
        "volumeSize": integer
      }
    }
  },
  "openMonitoring": {
    "prometheus": {
      "nodeExporter": {
        "enabledInBroker": boolean
      },
      "jmxExporter": {
        "enabledInBroker": boolean
      }
    }
  },
  "rebalancing": {
    "status": enum
  }
}
```

### Response bodies
<a name="clusters-response-examples"></a>

#### ListClustersResponse schema
<a name="clusters-response-body-listclustersresponse-example"></a>

```
{
  "nextToken": "string",
  "clusterInfoList": [
    {
      "encryptionInfo": {
        "encryptionInTransit": {
          "inCluster": boolean,
          "clientBroker": enum
        },
        "encryptionAtRest": {
          "dataVolumeKMSKeyId": "string"
        }
      },
      "zookeeperConnectString": "string",
      "creationTime": "string",
      "customerActionStatus": enum,
      "zookeeperConnectStringTls": "string",
      "loggingInfo": {
        "brokerLogs": {
          "s3": {
            "bucket": "string",
            "prefix": "string",
            "enabled": boolean
          },
          "firehose": {
            "deliveryStream": "string",
            "enabled": boolean
          },
          "cloudWatchLogs": {
            "logGroup": "string",
            "enabled": boolean
          }
        },
        "authorizerLogs": {
          "s3": {
            "bucket": "string",
            "prefix": "string",
            "enabled": boolean
          },
          "firehose": {
            "deliveryStream": "string",
            "enabled": boolean
          },
          "cloudWatchLogs": {
            "logGroup": "string",
            "enabled": boolean
          }
        }
      },
      "currentVersion": "string",
      "tags": {
      },
      "numberOfBrokerNodes": integer,
      "clusterArn": "string",
      "activeOperationArn": "string",
      "enhancedMonitoring": enum,
      "storageMode": enum,
      "clusterName": "string",
      "stateInfo": {
        "code": "string",
        "message": "string"
      },
      "clientAuthentication": {
        "sasl": {
          "iam": {
            "enabled": boolean
          },
          "scram": {
            "enabled": boolean
          }
        },
        "unauthenticated": {
          "enabled": boolean
        },
        "tls": {
          "certificateAuthorityArnList": [
            "string"
          ],
          "enabled": boolean
        }
      },
      "state": enum,
      "brokerNodeGroupInfo": {
        "clientSubnets": [
          "string"
        ],
        "zoneIds": [
          "string"
        ],
        "instanceType": "string",
        "connectivityInfo": {
          "vpcConnectivity": {
            "clientAuthentication": {
              "sasl": {
                "iam": {
                  "enabled": boolean
                },
                "scram": {
                  "enabled": boolean
                }
              },
              "tls": {
                "enabled": boolean
              }
            }
          },
          "publicAccess": {
            "type": "string"
          },
          "networkType": "string"
        },
        "securityGroups": [
          "string"
        ],
        "brokerAZDistribution": enum,
        "storageInfo": {
          "ebsStorageInfo": {
            "provisionedThroughput": {
              "volumeThroughput": integer,
              "enabled": boolean
            },
            "volumeSize": integer
          }
        }
      },
      "openMonitoring": {
        "prometheus": {
          "nodeExporter": {
            "enabledInBroker": boolean
          },
          "jmxExporter": {
            "enabledInBroker": boolean
          }
        }
      },
      "rebalancing": {
        "status": enum
      },
      "currentBrokerSoftwareInfo": {
        "configurationRevision": integer,
        "kafkaVersion": "string",
        "configurationArn": "string"
      }
    }
  ]
}
```

#### CreateClusterResponse schema
<a name="clusters-response-body-createclusterresponse-example"></a>

```
{
  "clusterArn": "string",
  "clusterName": "string",
  "state": enum
}
```

#### Error schema
<a name="clusters-response-body-error-example"></a>

```
{
  "message": "string",
  "invalidParameter": "string"
}
```

## Properties
<a name="clusters-properties"></a>

### AuthorizerLogs
<a name="clusters-model-authorizerlogs"></a>

Authorizer Logs details for cluster.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| cloudWatchLogs | [CloudWatchLogs](#clusters-model-cloudwatchlogs) | False | CloudWatch Log destination details. |
| firehose | [Firehose](#clusters-model-firehose) | False | Firehose Log destination details. |
| s3 | [S3](#clusters-model-s3) | False | S3 Log destination details. |

### BrokerAZDistribution
<a name="clusters-model-brokerazdistribution"></a>

This parameter is currently not in use.
+ `DEFAULT`

### BrokerLogs
<a name="clusters-model-brokerlogs"></a>

The broker logs configuration for this MSK cluster.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| cloudWatchLogs | [CloudWatchLogs](#clusters-model-cloudwatchlogs) | False | Details of the CloudWatch Logs destination for broker logs. |
| firehose | [Firehose](#clusters-model-firehose) | False | Details of the Kinesis Data Firehose delivery stream that is the destination for broker logs. |
| s3 | [S3](#clusters-model-s3) | False | Details of the Amazon S3 destination for broker logs. |

### BrokerNodeGroupInfo
<a name="clusters-model-brokernodegroupinfo"></a>

Describes the setup to be used for the broker nodes in the cluster.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| brokerAZDistribution | [BrokerAZDistribution](#clusters-model-brokerazdistribution) | False | This parameter is currently not in use. |
| clientSubnets | Array of type string | True | The list of subnets to connect to in the client virtual private cloud (VPC). Amazon creates elastic network interfaces inside these subnets. Client applications use elastic network interfaces to produce and consume data. <br />If you use the US West (N. California) Region, specify exactly two subnets. For other Regions where Amazon MSK is available, you can specify either two or three subnets. The subnets that you specify must be in distinct Availability Zones. When you create a cluster, Amazon MSK distributes the broker nodes evenly across the subnets that you specify.<br />Client subnets can't occupy the Availability Zone with ID `use1-az3`. |
| connectivityInfo | [ConnectivityInfo](#clusters-model-connectivityinfo) | False | Information about the cluster's connectivity setting. |
| instanceType | string<br />MinLength: 5<br />MaxLength: 32 | True | The type of Amazon EC2 instances to use for brokers. The following instance types are allowed: kafka.m5.large, kafka.m5.xlarge, kafka.m5.2xlarge, kafka.m5.4xlarge, kafka.m5.8xlarge, kafka.m5.12xlarge, kafka.m5.16xlarge, and kafka.m5.24xlarge. |
| securityGroups | Array of type string | False | The security groups to associate with the elastic network interfaces in order to specify who can connect to and communicate with the Amazon MSK cluster. If you don't specify a security group, Amazon MSK uses the default security group associated with the VPC. If you specify security groups that were shared with you, you must ensure that you have permissions to them. Specifically, you need the `ec2:DescribeSecurityGroups` permission. |
| storageInfo | [StorageInfo](#clusters-model-storageinfo) | False | Contains information about storage volumes attached to Amazon MSK broker nodes. |
| zoneIds | Array of type string | False | The zoneIds for brokers in customer account. |

### BrokerSoftwareInfo
<a name="clusters-model-brokersoftwareinfo"></a>

Information about the current software installed on the cluster.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| configurationArn | string | False | The Amazon Resource Name (ARN) of the configuration used for the cluster. This field isn't visible in this preview release. |
| configurationRevision | integer<br />Format: int64 | False | The revision of the configuration to use. This field isn't visible in this preview release. |
| kafkaVersion | string | False | The version of Apache Kafka. You can use Amazon MSK to create clusters that use Apache Kafka versions 1.1.1 and 2.2.1. See [Apache Kafka Versions](kafka-versions.md). |

### ClientAuthentication
<a name="clusters-model-clientauthentication"></a>

Includes all client authentication information.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| sasl | [Sasl](#clusters-model-sasl) | False | Details for client authentication using SASL. To turn on SASL, you must also turn on `EncryptionInTransit` by setting `inCluster` to true. You must set `clientBroker` to either `TLS` or `TLS_PLAINTEXT`. If you choose `TLS_PLAINTEXT`, then you must also set `unauthenticated` to true. |
| tls | [Tls](#clusters-model-tls) | False | Details for ClientAuthentication using TLS. To turn on TLS access control, you must also turn on `EncryptionInTransit` by setting `inCluster` to true and `clientBroker` to `TLS`. |
| unauthenticated | [Unauthenticated](#clusters-model-unauthenticated) | False | Details for ClientAuthentication using no authentication. |

### ClientBroker
<a name="clusters-model-clientbroker"></a>

Client-broker encryption in transit setting.
+ `TLS`
+ `TLS_PLAINTEXT`
+ `PLAINTEXT`

### CloudWatchLogs
<a name="clusters-model-cloudwatchlogs"></a>

Details of the CloudWatch Logs destination for broker logs.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| enabled | boolean | True | Specifies whether broker logs get sent to the specified CloudWatch Logs destination. |
| logGroup | string | False | The CloudWatch log group that is the destination for broker logs. |

### ClusterInfo
<a name="clusters-model-clusterinfo"></a>

Returns information about a cluster.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| activeOperationArn | string | False | Arn of active cluster operation. |
| brokerNodeGroupInfo | [BrokerNodeGroupInfo](#clusters-model-brokernodegroupinfo) | False | Information about the broker nodes. |
| clientAuthentication | [ClientAuthentication](#clusters-model-clientauthentication) | False | Includes all client authentication information. |
| clusterArn | string | False | The Amazon Resource Name (ARN) that uniquely identifies the cluster. |
| clusterName | string | False | The name of the cluster. |
| creationTime | string | False | The time when the cluster was created. |
| currentBrokerSoftwareInfo | [BrokerSoftwareInfo](#clusters-model-brokersoftwareinfo) | False | Information about the version of software currently deployed on the brokers in the cluster. |
| currentVersion | string | False | The current version of the MSK cluster. Cluster versions aren't simple integers. You can obtain the current version by describing the cluster. An example version is `KTVPDKIKX0DER`. |
| customerActionStatus | [CustomerActionStatus](#clusters-model-customeractionstatus) | False | Determines if there is an action required from the customer. |
| encryptionInfo | [EncryptionInfo](#clusters-model-encryptioninfo) | False | Includes all encryption-related information. |
| enhancedMonitoring | [EnhancedMonitoring](#clusters-model-enhancedmonitoring) | False | Specifies which Apache Kafka metrics Amazon MSK gathers and sends to Amazon CloudWatch for this cluster. This property has three possible values: `DEFAULT`, `PER_BROKER`, and `PER_TOPIC_PER_BROKER`. For a list of the metrics associated with each of these three levels of monitoring, see [Monitoring](https://docs.aws.amazon.com/msk/latest/developerguide/monitoring.html). |
| loggingInfo | [LoggingInfo](#clusters-model-logginginfo) | False | You can configure your MSK cluster to send broker logs to different destination types. This is a container for the configuration details related to broker logs. |
| numberOfBrokerNodes | integer | False | The number of broker nodes in the cluster. |
| openMonitoring | [OpenMonitoring](#clusters-model-openmonitoring) | False | Settings for open monitoring using Prometheus. |
| rebalancing | [Rebalancing](#clusters-model-rebalancing) | False | Specifies if intelligent rebalancing is turned on for your MSK Provisioned cluster with Express brokers. For all new Express-based clusters that you create, intelligent rebalancing is turned on by default. |
| state | [ClusterState](#clusters-model-clusterstate) | False | The state of the cluster. Amazon MSK automatically renews certificates on clusters every 13 months. It sets the state of the cluster to `MAINTENANCE` when it starts the certificate-update operation. It sets it back to `ACTIVE` when the update is done. While a cluster is in the `MAINTENANCE` state, you can continue to produce and consume data, but you can't perform any update operations on it. You can perform update operations on a cluster when it is in the `ACTIVE` state. |
| stateInfo | [StateInfo](#clusters-model-stateinfo) | False | Includes information of the cluster state. |
| storageMode | [StorageMode](#clusters-model-storagemode) | False | This controls storage mode for supported storage tiers. |
| tags | object | False | Tags attached to the cluster. |
| zookeeperConnectString | string | False | The connection string to use to connect to zookeeper cluster on plaintext port. |
| zookeeperConnectStringTls | string | False | The connection string to use to connect to the Apache ZooKeeper cluster on a TLS port. |

### ClusterState
<a name="clusters-model-clusterstate"></a>

The state of the cluster. Amazon MSK automatically renews certificates on clusters every 13 months. It sets the state of the cluster to `MAINTENANCE` when it starts the certificate-update operation. It sets it back to `ACTIVE` when the update is done. While a cluster is in the `MAINTENANCE` state, you can continue to produce and consume data, but you can't perform any update operations on it. You can perform update operations on a cluster when it is in the `ACTIVE` state.
+ `ACTIVE`
+ `CREATING`
+ `UPDATING`
+ `DELETING`
+ `FAILED`
+ `MAINTENANCE`
+ `REBOOTING_BROKER`
+ `HEALING`

### ConfigurationInfo
<a name="clusters-model-configurationinfo"></a>

Specifies the configuration to use for the brokers.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| arn | string | True | ARN of the configuration to use. |
| revision | integer<br />Format: int64<br />Minimum: 1 | True | The revision of the configuration to use. |

### ConnectivityInfo
<a name="clusters-model-connectivityinfo"></a>

Broker access controls.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| networkType | string<br />MinLength: 4<br />MaxLength: 4 | False | The network type of the cluster, which is IPv4 or DUAL. The DUAL network type uses both IPv4 and IPv6 addresses for your cluster and its resources. By default, a cluster uses the IPv4 network type. |
| publicAccess | [PublicAccess](#clusters-model-publicaccess) | False | Access control settings for the cluster's brokers. |
| vpcConnectivity | [VpcConnectivity](#clusters-model-vpcconnectivity) | False | VPC connection control settings for brokers |

### CreateClusterRequest
<a name="clusters-model-createclusterrequest"></a>

Creates a cluster.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| brokerNodeGroupInfo | [BrokerNodeGroupInfo](#clusters-model-brokernodegroupinfo) | True | Information about the broker nodes in the cluster. |
| clientAuthentication | [ClientAuthentication](#clusters-model-clientauthentication) | False | Includes all client authentication related information. |
| clusterName | string<br />MinLength: 1<br />MaxLength: 64 | True | The name of the cluster. |
| configurationInfo | [ConfigurationInfo](#clusters-model-configurationinfo) | False | Represents the configuration that you want MSK to use for the cluster. |
| encryptionInfo | [EncryptionInfo](#clusters-model-encryptioninfo) | False | Includes all encryption-related information. |
| enhancedMonitoring | [EnhancedMonitoring](#clusters-model-enhancedmonitoring) | False | Specifies the level of monitoring for the MSK cluster. The possible values are `DEFAULT`, `PER_BROKER`, and `PER_TOPIC_PER_BROKER`. |
| kafkaVersion | string<br />MinLength: 1<br />MaxLength: 128 | True | The version of Apache Kafka. You can use Amazon MSK to create clusters that use Apache Kafka versions 1.1.1 and 2.2.1. See [Apache Kafka Versions](kafka-versions.md). |
| loggingInfo | [LoggingInfo](#clusters-model-logginginfo) | False | Logging Info details. |
| numberOfBrokerNodes | integer | True | The number of broker nodes in the cluster. |
| openMonitoring | [OpenMonitoringInfo](#clusters-model-openmonitoringinfo) | False | The settings for open monitoring. |
| rebalancing | [Rebalancing](#clusters-model-rebalancing) | False | Specifies if intelligent rebalancing should be turned on for a new MSK Provisioned cluster with Express brokers. For all new Express-based clusters that you create, intelligent rebalancing is turned on by default. |
| storageMode | [StorageMode](#clusters-model-storagemode) | False | This controls storage mode for supported storage tiers. |
| tags | object | False | Create tags when creating the cluster. |

### CreateClusterResponse
<a name="clusters-model-createclusterresponse"></a>

Returns information about the created cluster.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| clusterArn | string | False | The Amazon Resource Name (ARN) of the cluster. |
| clusterName | string | False | The name of the MSK cluster. |
| state | [ClusterState](#clusters-model-clusterstate) | False | The state of the cluster. Amazon MSK automatically renews certificates on clusters every 13 months. It sets the state of the cluster to `MAINTENANCE` when it starts the certificate-update operation. It sets it back to `ACTIVE` when the update is done. While a cluster is in the `MAINTENANCE` state, you can continue to produce and consume data, but you can't perform any update operations on it. You can perform update operations on a cluster when it is in the `ACTIVE` state. |

### CustomerActionStatus
<a name="clusters-model-customeractionstatus"></a>

A type of an action required from the customer.
+ `CRITICAL_ACTION_REQUIRED`
+ `ACTION_RECOMMENDED`
+ `NONE`

### EBSStorageInfo
<a name="clusters-model-ebsstorageinfo"></a>

Contains information about the EBS storage volumes attached to the broker nodes.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| provisionedThroughput | [ProvisionedThroughput](#clusters-model-provisionedthroughput) | False | EBS volume provisioned throughput information. |
| volumeSize | integer<br />Minimum: 1<br />Maximum: 16384 | False | The size in GiB of the EBS volume for the data drive on each broker node. |

### EncryptionAtRest
<a name="clusters-model-encryptionatrest"></a>

The data-volume encryption details. You can't update encryption at rest settings for existing clusters.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| dataVolumeKMSKeyId | string | True | The Amazon Resource Name (ARN) of the Amazon KMS key for encrypting data at rest. If you don't specify a KMS key, MSK creates one for you and uses it. |

### EncryptionInTransit
<a name="clusters-model-encryptionintransit"></a>

The settings for encrypting data in transit.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| clientBroker | [ClientBroker](#clusters-model-clientbroker) | False | Indicates the encryption setting for data in transit between clients and brokers. You must set it to one of the following values.<br /> `TLS` means that client-broker communication is enabled with TLS only.<br /> `TLS_PLAINTEXT` means that client-broker communication is enabled for both TLS-encrypted, as well as plaintext data.<br /> `PLAINTEXT` means that client-broker communication is enabled in plaintext only.<br />The default value is `TLS`. |
| inCluster | boolean | False | When set to true, it indicates that data communication among the broker nodes of the cluster is encrypted. When set to false, the communication happens in plaintext.<br />The default value is true. |

### EncryptionInfo
<a name="clusters-model-encryptioninfo"></a>

Includes encryption-related information, such as the Amazon KMS key used for encrypting data at rest and whether you want MSK to encrypt your data in transit.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| encryptionAtRest | [EncryptionAtRest](#clusters-model-encryptionatrest) | False | The data-volume encryption details. |
| encryptionInTransit | [EncryptionInTransit](#clusters-model-encryptionintransit) | False | The details for encryption in transit. |

### EnhancedMonitoring
<a name="clusters-model-enhancedmonitoring"></a>

Specifies which Apache Kafka metrics Amazon MSK gathers and sends to Amazon CloudWatch for this cluster. This property has three possible values: `DEFAULT`, `PER_BROKER`, and `PER_TOPIC_PER_BROKER`. For a list of the metrics associated with each of these three levels of monitoring, see [Monitoring](https://docs.aws.amazon.com/msk/latest/developerguide/monitoring.html).
+ `DEFAULT`
+ `PER_BROKER`
+ `PER_TOPIC_PER_BROKER`
+ `PER_TOPIC_PER_PARTITION`

### Error
<a name="clusters-model-error"></a>

Returns information about an error.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| invalidParameter | string | False | The parameter that caused the error. |
| message | string | False | The description of the error. |

### Firehose
<a name="clusters-model-firehose"></a>

Firehose details for BrokerLogs.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| deliveryStream | string | False | The Kinesis Data Firehose delivery stream that is the destination for broker logs. |
| enabled | boolean | True | Specifies whether broker logs get sent to the specified Kinesis Data Firehose delivery stream. |

### IAM
<a name="clusters-model-iam"></a>

Details for SASL/IAM client authentication.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| enabled | boolean | False | SASL/IAM authentication is enabled or not. |

### JmxExporter
<a name="clusters-model-jmxexporter"></a>

Indicates whether you want to enable or disable the JMX Exporter.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| enabledInBroker | boolean | True | Indicates whether you want to enable or disable the JMX Exporter. |

### JmxExporterInfo
<a name="clusters-model-jmxexporterinfo"></a>

JMX Exporter details.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| enabledInBroker | boolean | True | JMX Exporter being enabled in broker. |

### ListClustersResponse
<a name="clusters-model-listclustersresponse"></a>

The response contains an array containing cluster information and a next token if the response is truncated.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| clusterInfoList | Array of type [ClusterInfo](#clusters-model-clusterinfo) | False | Information on each of the MSK clusters in the response. |
| nextToken | string | False | The paginated results marker. When the result of a `ListClusters` operation is truncated, the call returns `NextToken` in the response. To get another batch of clusters, provide this token in your next request. |

### LoggingInfo
<a name="clusters-model-logginginfo"></a>

You can configure your MSK cluster to send broker logs to different destination types. This is a container for the configuration details related to broker logs.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| authorizerLogs | [AuthorizerLogs](#clusters-model-authorizerlogs) | False | Authorizer Logs details. |
| brokerLogs | [BrokerLogs](#clusters-model-brokerlogs) | False | You can configure your MSK cluster to send broker logs to different destination types. This configuration specifies the details of these destinations. |

### NodeExporter
<a name="clusters-model-nodeexporter"></a>

Indicates whether you want to enable or disable the Node Exporter.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| enabledInBroker | boolean | True | Indicates whether you want to enable or disable the Node Exporter. |

### NodeExporterInfo
<a name="clusters-model-nodeexporterinfo"></a>

Node Exporter details.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| enabledInBroker | boolean | True | Node Exporter being enabled in broker. |

### OpenMonitoring
<a name="clusters-model-openmonitoring"></a>

JMX and Node monitoring for the MSK cluster.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| prometheus | [Prometheus](#clusters-model-prometheus) | True | Prometheus exporter settings. |

### OpenMonitoringInfo
<a name="clusters-model-openmonitoringinfo"></a>

JMX and Node monitoring for cluster.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| prometheus | [PrometheusInfo](#clusters-model-prometheusinfo) | True | Prometheus details. |

### Prometheus
<a name="clusters-model-prometheus"></a>

Prometheus settings for open monitoring.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| jmxExporter | [JmxExporter](#clusters-model-jmxexporter) | False | Indicates whether you want to enable or disable the JMX Exporter. |
| nodeExporter | [NodeExporter](#clusters-model-nodeexporter) | False | Indicates whether you want to enable or disable the Node Exporter. |

### PrometheusInfo
<a name="clusters-model-prometheusinfo"></a>

Prometheus details.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| jmxExporter | [JmxExporterInfo](#clusters-model-jmxexporterinfo) | False | JMX Exporter details. |
| nodeExporter | [NodeExporterInfo](#clusters-model-nodeexporterinfo) | False | Node Exporter details. |

### ProvisionedThroughput
<a name="clusters-model-provisionedthroughput"></a>

Contains information about provisioned throughput for EBS storage volumes attached to kafka broker nodes.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| enabled | boolean | False | Provisioned throughput is enabled or not. |
| volumeThroughput | integer | False | Throughput value of the EBS volumes for the data drive on each kafka broker node in MiB per second. |

### PublicAccess
<a name="clusters-model-publicaccess"></a>

Broker access controls

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| type | string | False | DISABLED means that public access is turned off. SERVICE\_PROVIDED\_EIPS means that public access is turned on. |

### Rebalancing
<a name="clusters-model-rebalancing"></a>

Specifies whether or not intelligent rebalancing is turned on for a newly created MSK Provisioned cluster with Express brokers. Intelligent rebalancing performs automatic partition balancing operations when you scale your clusters up or down.

By default, intelligent rebalancing is `ACTIVE` for all new Express-based clusters.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| status | [RebalancingStatus](#clusters-model-rebalancingstatus) | True | Intelligent rebalancing status. The default intelligent rebalancing status is `ACTIVE` for all new Express-based clusters. |

### RebalancingStatus
<a name="clusters-model-rebalancingstatus"></a>

Intelligent rebalancing status. The default intelligent rebalancing status is `ACTIVE` for all new Express-based clusters.
+ `PAUSED`
+ `ACTIVE`

### S3
<a name="clusters-model-s3"></a>

The details of the Amazon S3 destination for broker logs.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| bucket | string | False | The name of the S3 bucket that is the destination for broker logs. |
| enabled | boolean | True | Specifies whether broker logs get sent to the specified Amazon S3 destination. |
| prefix | string | False | The S3 prefix that is the destination for broker logs. |

### Sasl
<a name="clusters-model-sasl"></a>

Details for client authentication using SASL. To turn on SASL, you must also turn on `EncryptionInTransit` by setting `inCluster` to true. You must set `clientBroker` to either `TLS` or `TLS_PLAINTEXT`. If you choose `TLS_PLAINTEXT`, then you must also set `unauthenticated` to true.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| iam | [IAM](#clusters-model-iam) | False | Details for ClientAuthentication using IAM. |
| scram | [Scram](#clusters-model-scram) | False | Details for SASL/SCRAM client authentication. |

### Scram
<a name="clusters-model-scram"></a>

Details for SASL/SCRAM client authentication.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| enabled | boolean | False | SASL/SCRAM authentication is enabled or not. |

### StateInfo
<a name="clusters-model-stateinfo"></a>

Includes information about the state of the cluster.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| code | string | False | If the cluster is in an unusable state, this field contains the code that describes the issue. |
| message | string | False | If the cluster is in an unusable state, this field contains a message that describes the issue. |

### StorageInfo
<a name="clusters-model-storageinfo"></a>

Contains information about storage volumes attached to Amazon MSK broker nodes.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| ebsStorageInfo | [EBSStorageInfo](#clusters-model-ebsstorageinfo) | False | EBS volume information. |

### StorageMode
<a name="clusters-model-storagemode"></a>

Controls storage mode for various supported storage tiers.
+ `LOCAL`
+ `TIERED`

### Tls
<a name="clusters-model-tls"></a>

Details for client authentication using TLS.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| certificateAuthorityArnList | Array of type string | False | List of AWS Private CA Amazon Resource Name (ARN)s. |
| enabled | boolean | False | TLS authentication is enabled or not. |

### Unauthenticated
<a name="clusters-model-unauthenticated"></a>

Details for allowing no client authentication.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| enabled | boolean | False | Unauthenticated is enabled or not. |

### VpcConnectivity
<a name="clusters-model-vpcconnectivity"></a>

VPC connection control settings for brokers.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| clientAuthentication | [VpcConnectivityClientAuthentication](#clusters-model-vpcconnectivityclientauthentication) | False | VPC connection control settings for brokers. |

### VpcConnectivityClientAuthentication
<a name="clusters-model-vpcconnectivityclientauthentication"></a>

Includes all client authentication information for VpcConnectivity.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| sasl | [VpcConnectivitySasl](#clusters-model-vpcconnectivitysasl) | False | Details for VpcConnectivity ClientAuthentication using SASL. |
| tls | [VpcConnectivityTls](#clusters-model-vpcconnectivitytls) | False | Details for VpcConnectivity ClientAuthentication using TLS. |

### VpcConnectivityIAM
<a name="clusters-model-vpcconnectivityiam"></a>

Details for SASL/IAM client authentication for VpcConnectivity.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| enabled | boolean | False | SASL/IAM authentication is enabled or not. |

### VpcConnectivitySasl
<a name="clusters-model-vpcconnectivitysasl"></a>

Details for client authentication using SASL for VpcConnectivity.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| iam | [VpcConnectivityIAM](#clusters-model-vpcconnectivityiam) | False | Details for ClientAuthentication using IAM for VpcConnectivity. |
| scram | [VpcConnectivityScram](#clusters-model-vpcconnectivityscram) | False | Details for SASL/SCRAM client authentication for VpcConnectivity. |

### VpcConnectivityScram
<a name="clusters-model-vpcconnectivityscram"></a>

Details for SASL/SCRAM client authentication for vpcConnectivity.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| enabled | boolean | False | SASL/SCRAM authentication is enabled or not. |

### VpcConnectivityTls
<a name="clusters-model-vpcconnectivitytls"></a>

Details for client authentication using TLS for vpcConnectivity.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| enabled | boolean | False | TLS authentication is enabled or not. |

## See also
<a name="clusters-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### ListClusters
<a name="ListClusters-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/kafka-2018-11-14/ListClusters)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/kafka-2018-11-14/ListClusters)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/kafka-2018-11-14/ListClusters)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/kafka-2018-11-14/ListClusters)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/kafka-2018-11-14/ListClusters)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/kafka-2018-11-14/ListClusters)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/kafka-2018-11-14/ListClusters)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/kafka-2018-11-14/ListClusters)
+ [AWS SDK for Python](/goto/boto3/kafka-2018-11-14/ListClusters)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/kafka-2018-11-14/ListClusters)

### CreateCluster
<a name="CreateCluster-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/kafka-2018-11-14/CreateCluster)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/kafka-2018-11-14/CreateCluster)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/kafka-2018-11-14/CreateCluster)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/kafka-2018-11-14/CreateCluster)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/kafka-2018-11-14/CreateCluster)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/kafka-2018-11-14/CreateCluster)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/kafka-2018-11-14/CreateCluster)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/kafka-2018-11-14/CreateCluster)
+ [AWS SDK for Python](/goto/boto3/kafka-2018-11-14/CreateCluster)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/kafka-2018-11-14/CreateCluster)
