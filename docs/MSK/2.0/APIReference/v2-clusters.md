---
source_url: https://docs.aws.amazon.com/MSK/2.0/APIReference/v2-clusters.html
---

# Clusters
<a name="v2-clusters"></a>

Represents the Amazon MSK clusters in an account.

## URI
<a name="v2-clusters-url"></a>

`/api/v2/clusters`

## HTTP methods
<a name="v2-clusters-http-methods"></a>

### GET
<a name="v2-clustersget"></a>

**Operation ID:** `ListClustersV2`

Lists all serverless and provisioned clusters.

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| nextToken | String | False | If the response of ListClusters is truncated, it returns a nextToken in the response. This nextToken should be sent in the subsequent request to ListClusters. |
| clusterNameFilter | String | False | Returns clusters starting with given name. |
| maxResults | String | False | Maximum number of clusters to fetch in one get request. |
| clusterTypeFilter | String | False | Returns clusters with the given type. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 |  ListClustersV2Response | HTTP Status Code 200: OK. |
| 400 | None | HTTP Status Code 400: Bad request due to incorrect input. Correct your request and then retry it. |
| 401 | None | HTTP Status Code 401: Unauthorized request. The provided credentials couldn't be validated. |
| 403 | None | HTTP Status Code 403: Access forbidden. Correct your credentials and then retry your request. |
| 404 | None | HTTP Status Code 404: Resource not found due to incorrect input. Correct your request and then retry it. |
| 429 | None | HTTP Status Code 429: Limit exceeded. Resource limit reached. |
| 500 | None | HTTP Status Code 500: Unexpected internal server error. Retrying your request might resolve the issue. |
| 503 | None | HTTP Status Code 503: Service Unavailable. Retrying your request in some time might resolve the issue. |

### POST
<a name="v2-clusterspost"></a>

**Operation ID:** `CreateClusterV2`

Creates a serverless or provisioned cluster.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 |  CreateClusterV2Response | HTTP Status Code 200: OK. |
| 400 | None | HTTP Status Code 400: Bad request due to incorrect input. Correct your request and then retry it. |
| 401 | None | HTTP Status Code 401: Unauthorized request. The provided credentials couldn't be validated. |
| 403 | None | HTTP Status Code 403: Access forbidden. Correct your credentials and then retry your request. |
| 404 | None | HTTP Status Code 404: Resource not found due to incorrect input. Correct your request and then retry it. |
| 409 | None | HTTP Status Code 409: Conflict. This cluster name already exists. Retry your request with another name. |
| 429 | None | HTTP Status Code 429: Limit exceeded. Resource limit reached. |
| 500 | None | HTTP Status Code 500: Unexpected internal server error. Retrying your request might resolve the issue. |
| 503 | None | HTTP Status Code 503: Service Unavailable. Retrying your request in some time might resolve the issue. |

### OPTIONS
<a name="v2-clustersoptions"></a>

Enable CORS by returning correct headers

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | 200 response |

## Schemas
<a name="v2-clusters-schemas"></a>

### Request bodies
<a name="v2-clusters-request-examples"></a>

#### POST schema
<a name="v2-clusters-request-body-post-example"></a>

```
{
  "provisioned": {
    "encryptionInfo": {
      "encryptionInTransit": {
        "inCluster": boolean,
        "clientBroker": enum
      },
      "encryptionAtRest": {
        "dataVolumeKMSKeyId": "string"
      }
    },
    "numberOfBrokerNodes": integer,
    "configurationInfo": {
      "arn": "string",
      "revision": integer
    },
    "enhancedMonitoring": enum,
    "storageMode": enum,
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
        }
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
  },
  "clusterName": "string",
  "serverless": {
    "vpcConfigs": [
      {
        "securityGroupIds": [
          "string"
        ],
        "subnetIds": [
          "string"
        ]
      }
    ],
    "clientAuthentication": {
      "sasl": {
        "iam": {
          "enabled": boolean
        }
      }
    }
  },
  "tags": {
  }
}
```

### Response bodies
<a name="v2-clusters-response-examples"></a>

#### ListClustersV2Response schema
<a name="v2-clusters-response-body-listclustersv2response-example"></a>

```
{
  "nextToken": "string",
  "clusterInfoList": [
    {
      "clusterType": enum,
      "clusterArn": "string",
      "activeOperationArn": "string",
      "provisioned": {
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
          }
        },
        "numberOfBrokerNodes": integer,
        "enhancedMonitoring": enum,
        "storageMode": enum,
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
            }
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
      },
      "creationTime": "string",
      "clusterName": "string",
      "serverless": {
        "vpcConfigs": [
          {
            "securityGroupIds": [
              "string"
            ],
            "subnetIds": [
              "string"
            ]
          }
        ],
        "kafkaVersion": "string",
        "clientAuthentication": {
          "sasl": {
            "iam": {
              "enabled": boolean
            }
          }
        }
      },
      "stateInfo": {
        "code": "string",
        "message": "string"
      },
      "state": enum,
      "currentVersion": "string",
      "tags": {
      }
    }
  ]
}
```

#### CreateClusterV2Response schema
<a name="v2-clusters-response-body-createclusterv2response-example"></a>

```
{
  "clusterType": enum,
  "clusterArn": "string",
  "clusterName": "string",
  "state": enum
}
```

## Properties
<a name="v2-clusters-properties"></a>

### BrokerAZDistribution
<a name="v2-clusters-model-brokerazdistribution"></a>

The distribution of broker nodes across Availability Zones.
+ `DEFAULT`

### BrokerLogs
<a name="v2-clusters-model-brokerlogs"></a>

Broker Logs details for cluster.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| cloudWatchLogs | [CloudWatchLogs](#v2-clusters-model-cloudwatchlogs) | False | CloudWatch Log destination details. |
| firehose | [Firehose](#v2-clusters-model-firehose) | False |  |
| s3 | [S3](#v2-clusters-model-s3) | False | S3 Log destination details. |

### BrokerNodeGroupInfo
<a name="v2-clusters-model-brokernodegroupinfo"></a>

Describes the setup to be used for the brokers.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| brokerAZDistribution | [BrokerAZDistribution](#v2-clusters-model-brokerazdistribution) | False | The distribution of broker nodes across Availability Zones. |
| clientSubnets | Array of type string | True | The list of subnets in the client VPC to connect to. |
| connectivityInfo | [ConnectivityInfo](#v2-clusters-model-connectivityinfo) | False | Information about the cluster access configuration. |
| instanceType | string<br />MinLength: 5<br />MaxLength: 32 | True | The type of broker used for the cluster. |
| securityGroups | Array of type string | False | The security groups to attach to the ENIs for the broker nodes. |
| storageInfo | [StorageInfo](#v2-clusters-model-storageinfo) | False | Data volume information. |
| zoneIds | Array of type string | False | The zoneIds for brokers in customer account. |

### BrokerSoftwareInfo
<a name="v2-clusters-model-brokersoftwareinfo"></a>

Information about current software installed in the cluster.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| configurationArn | string | False | ARN of the configuration used on the cluster. |
| configurationRevision | integer<br />Format: int64 | False | Revision of the configuration to use. |
| kafkaVersion | string | False | The version of Apache Kafka to install and run on the cluster. |

### ClientAuthentication
<a name="v2-clusters-model-clientauthentication"></a>

Includes all client authentication information.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| sasl | [Sasl](#v2-clusters-model-sasl) | False | Details for ClientAuthentication using SASL. |
| tls | [Tls](#v2-clusters-model-tls) | False | Details for ClientAuthentication using TLS. |
| unauthenticated | [Unauthenticated](#v2-clusters-model-unauthenticated) | False | Details for ClientAuthentication using no authentication. |

### ClientBroker
<a name="v2-clusters-model-clientbroker"></a>

Client-broker encryption in transit setting.
+ `TLS`
+ `TLS_PLAINTEXT`
+ `PLAINTEXT`

### CloudWatchLogs
<a name="v2-clusters-model-cloudwatchlogs"></a>

CloudWatchLogs details for BrokerLogs.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| enabled | boolean | True | Broker logs for destination CW enabled or not. |
| logGroup | string | False | CloudWatch LogGroup where the logs will be delivered. |

### Cluster
<a name="v2-clusters-model-cluster"></a>

Returns information about a cluster.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| activeOperationArn | string | False | Arn of active cluster operation. |
| clusterArn | string | False | The Amazon Resource Name (ARN) of the cluster. |
| clusterName | string | False | The name of the cluster. |
| clusterType | [ClusterType](#v2-clusters-model-clustertype) | False | Type of the backend cluster. |
| creationTime | string | False | The time when the cluster was created. |
| currentVersion | string | False | Current version of cluster. |
| provisioned | [Provisioned](#v2-clusters-model-provisioned) | False | Properties of a provisioned cluster. |
| serverless | [Serverless](#v2-clusters-model-serverless) | False | Properties of a serverless cluster. |
| state | [ClusterState](#v2-clusters-model-clusterstate) | False | State of the cluster. |
| stateInfo | [StateInfo](#v2-clusters-model-stateinfo) | False | Includes information of the cluster state. |
| tags | object | False | Tags attached to the cluster. |

### ClusterState
<a name="v2-clusters-model-clusterstate"></a>

The sate of an MSK cluster.
+ `ACTIVE`
+ `CREATING`
+ `UPDATING`
+ `DELETING`
+ `FAILED`
+ `MAINTENANCE`
+ `REBOOTING_BROKER`
+ `HEALING`

### ClusterType
<a name="v2-clusters-model-clustertype"></a>

The type of backend cluster.
+ `PROVISIONED`
+ `SERVERLESS`

### ConfigurationInfo
<a name="v2-clusters-model-configurationinfo"></a>

Specifies the configuration to be used on the brokers.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| arn | string | True | ARN of the configuration to use. |
| revision | integer<br />Format: int64<br />Minimum: 1 | True | The revision of the configuration to use. |

### ConnectivityInfo
<a name="v2-clusters-model-connectivityinfo"></a>

Broker access controls

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| publicAccess | [PublicAccess](#v2-clusters-model-publicaccess) | False | Access control settings for brokers |
| vpcConnectivity | [VpcConnectivity](#v2-clusters-model-vpcconnectivity) | False | VPC connection control settings for brokers. |

### CreateClusterV2Request
<a name="v2-clusters-model-createclusterv2request"></a>

Creates a provisioned or serverless cluster.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| clusterName | string<br />MinLength: 1<br />MaxLength: 64 | True | The name of the cluster. |
| provisioned | [ProvisionedRequest](#v2-clusters-model-provisionedrequest) | False | Properties required for creating a provisioned cluster. |
| serverless | [ServerlessRequest](#v2-clusters-model-serverlessrequest) | False | Properties required for creating a serverless cluster. |
| tags | object | False | Create tags when creating the cluster. |

### CreateClusterV2Response
<a name="v2-clusters-model-createclusterv2response"></a>

Returns information about the created cluster.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| clusterArn | string | False | The Amazon Resource Name (ARN) of the cluster. |
| clusterName | string | False | Name of the cluster provided by the customer. |
| clusterType | [ClusterType](#v2-clusters-model-clustertype) | False | Type of the backend cluster. |
| state | [ClusterState](#v2-clusters-model-clusterstate) | False | State of the cluster. |

### CustomerActionStatus
<a name="v2-clusters-model-customeractionstatus"></a>

A type of an action required from the customer.
+ `CRITICAL_ACTION_REQUIRED`
+ `ACTION_RECOMMENDED`
+ `NONE`

### EBSStorageInfo
<a name="v2-clusters-model-ebsstorageinfo"></a>

Contains information about the EBS storage volumes that are attached to the brokers.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| provisionedThroughput | [ProvisionedThroughput](#v2-clusters-model-provisionedthroughput) | False | EBS volume provisioned throughput information. |
| volumeSize | integer<br />Minimum: 1<br />Maximum: 16384 | False | The size of the EBS volumes for the data drive on each of the brokers in GiB. |

### EncryptionAtRest
<a name="v2-clusters-model-encryptionatrest"></a>

Details for encryption at rest.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| dataVolumeKMSKeyId | string | True | KMS key used for data volume encryption. |

### EncryptionInTransit
<a name="v2-clusters-model-encryptionintransit"></a>

Details for encryption in transit.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| clientBroker | [ClientBroker](#v2-clusters-model-clientbroker) | False | Client-broker encryption in transit setting. |
| inCluster | boolean | False | In-cluster encryption in transit setting. |

### EncryptionInfo
<a name="v2-clusters-model-encryptioninfo"></a>

Includes all encryption related information.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| encryptionAtRest | [EncryptionAtRest](#v2-clusters-model-encryptionatrest) | False | Details for encryption at rest. |
| encryptionInTransit | [EncryptionInTransit](#v2-clusters-model-encryptionintransit) | False | Details for encryption in transit. |

### EnhancedMonitoring
<a name="v2-clusters-model-enhancedmonitoring"></a>

Controls level of cluster metrics Amazon pushes to customer's cloudwatch account.
+ `DEFAULT`
+ `PER_BROKER`
+ `PER_TOPIC_PER_BROKER`
+ `PER_TOPIC_PER_PARTITION`

### Firehose
<a name="v2-clusters-model-firehose"></a>

Firehose details for BrokerLogs.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| deliveryStream | string | False | Firehose delivery stream where the logs will be delivered. |
| enabled | boolean | True | Broker logs for destination firehose enabled or not. |

### IAM
<a name="v2-clusters-model-iam"></a>

Details for SASL/IAM client authentication.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| enabled | boolean | False | SASL/IAM authentication is enabled or not. |

### JmxExporter
<a name="v2-clusters-model-jmxexporter"></a>

JMX Exporter details.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| enabledInBroker | boolean | True | JMX Exporter being enabled in broker. |

### JmxExporterInfo
<a name="v2-clusters-model-jmxexporterinfo"></a>

JMX Exporter details.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| enabledInBroker | boolean | True | JMX Exporter being enabled in broker. |

### ListClustersV2Response
<a name="v2-clusters-model-listclustersv2response"></a>

The response contains an array of cluster information and a nextToken if the response is truncated.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| clusterInfoList | Array of type [Cluster](#v2-clusters-model-cluster) | False | An array of clusters. |
| nextToken | string | False | If the response of ListClustersV2 is truncated, it returns a NextToken in the response. Pass this NextToken in a subsequent request to ListClustersV2 to get the next set of results. |

### LoggingInfo
<a name="v2-clusters-model-logginginfo"></a>

Logging info details for the cluster.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| brokerLogs | [BrokerLogs](#v2-clusters-model-brokerlogs) | True | Broker Logs details. |

### NodeExporter
<a name="v2-clusters-model-nodeexporter"></a>

Node Exporter details.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| enabledInBroker | boolean | True | Node Exporter being enabled in broker. |

### NodeExporterInfo
<a name="v2-clusters-model-nodeexporterinfo"></a>

Node Exporter details.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| enabledInBroker | boolean | True | Node Exporter being enabled in broker. |

### OpenMonitoring
<a name="v2-clusters-model-openmonitoring"></a>

JMX and Node monitoring for cluster.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| prometheus | [Prometheus](#v2-clusters-model-prometheus) | True | Prometheus details. |

### OpenMonitoringInfo
<a name="v2-clusters-model-openmonitoringinfo"></a>

JMX and Node monitoring for the cluster.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| prometheus | [PrometheusInfo](#v2-clusters-model-prometheusinfo) | True | Prometheus details. |

### Prometheus
<a name="v2-clusters-model-prometheus"></a>

Prometheus details.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| jmxExporter | [JmxExporter](#v2-clusters-model-jmxexporter) | False | JMX Exporter details. |
| nodeExporter | [NodeExporter](#v2-clusters-model-nodeexporter) | False | Node Exporter details. |

### PrometheusInfo
<a name="v2-clusters-model-prometheusinfo"></a>

Prometheus details.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| jmxExporter | [JmxExporterInfo](#v2-clusters-model-jmxexporterinfo) | False | JMX Exporter details. |
| nodeExporter | [NodeExporterInfo](#v2-clusters-model-nodeexporterinfo) | False | Node Exporter details. |

### Provisioned
<a name="v2-clusters-model-provisioned"></a>

Properties of a provisioned cluster.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| brokerNodeGroupInfo | [BrokerNodeGroupInfo](#v2-clusters-model-brokernodegroupinfo) | False | Information about the brokers of the cluster. |
| clientAuthentication | [ClientAuthentication](#v2-clusters-model-clientauthentication) | False | Includes all client authentication information. |
| currentBrokerSoftwareInfo | [BrokerSoftwareInfo](#v2-clusters-model-brokersoftwareinfo) | False | Information about the version of the software that is deployed on the brokers of the cluster. |
| customerActionStatus | [CustomerActionStatus](#v2-clusters-model-customeractionstatus) | False | Determines if there is an action required from the customer. |
| encryptionInfo | [EncryptionInfo](#v2-clusters-model-encryptioninfo) | False | Includes all encryption related information. |
| enhancedMonitoring | [EnhancedMonitoring](#v2-clusters-model-enhancedmonitoring) | False | This knob controls level of metrics pushed customer's cloudwatch account. |
| loggingInfo | [LoggingInfo](#v2-clusters-model-logginginfo) | False | Logging Info details. |
| numberOfBrokerNodes | integer | False | The number of brokers to create in the cluster. |
| openMonitoring | [OpenMonitoring](#v2-clusters-model-openmonitoring) | False | Open monitoring details. |
| rebalancing | [Rebalancing](#v2-clusters-model-rebalancing) | False | Contains information about intelligent rebalancing for the cluster. |
| storageMode | [StorageMode](#v2-clusters-model-storagemode) | False | This controls storage mode for supported storage tiers. |
| zookeeperConnectString | string | False | The connection string to use to connect to zookeeper cluster on plaintext port. |
| zookeeperConnectStringTls | string | False | The connection string to use to connect to zookeeper cluster on Tls port. |

### ProvisionedRequest
<a name="v2-clusters-model-provisionedrequest"></a>

Properties for creating a provisioned cluster.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| brokerNodeGroupInfo | [BrokerNodeGroupInfo](#v2-clusters-model-brokernodegroupinfo) | False | Information about the brokers of the cluster. |
| clientAuthentication | [ClientAuthentication](#v2-clusters-model-clientauthentication) | False | Includes all client authentication related information. |
| configurationInfo | [ConfigurationInfo](#v2-clusters-model-configurationinfo) | False | The configuration to be used on the brokers. |
| encryptionInfo | [EncryptionInfo](#v2-clusters-model-encryptioninfo) | False | Includes all encryption related information. |
| enhancedMonitoring | [EnhancedMonitoring](#v2-clusters-model-enhancedmonitoring) | False | Specifies the monitoring level for the cluster. |
| kafkaVersion | string<br />MinLength: 1<br />MaxLength: 128 | False | The version of Apache Kafka to install and run on the cluster. |
| loggingInfo | [LoggingInfo](#v2-clusters-model-logginginfo) | False | Logging Info details. |
| numberOfBrokerNodes | integer | False | The number of brokers to create in the cluster. |
| openMonitoring | [OpenMonitoringInfo](#v2-clusters-model-openmonitoringinfo) | False | The open-monitoring details. |
| rebalancing | [Rebalancing](#v2-clusters-model-rebalancing) | False | Specifies if intelligent rebalancing should be turned on for the new cluster. The default intelligent rebalancing status is ACTIVE for all new MSK Provisioned clusters that you create with Express brokers. |
| storageMode | [StorageMode](#v2-clusters-model-storagemode) | False | Specifies the storage mode for supported storage tiers. |

### ProvisionedThroughput
<a name="v2-clusters-model-provisionedthroughput"></a>

Contains information about provisioned throughput for the EBS storage volumes that are attached to the brokers.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| enabled | boolean | False | Whether provisioned throughput is turned on. |
| volumeThroughput | integer | False | Throughput value of the EBS volumes for the data drive on each broker in MiB per second. |

### PublicAccess
<a name="v2-clusters-model-publicaccess"></a>

Broker access controls

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| type | string | False | If public access is disabled, or if enabled the EIP provider |

### Rebalancing
<a name="v2-clusters-model-rebalancing"></a>

Contains information about intelligent rebalancing for the cluster. Intelligent rebalancing performs automatic partition balancing operations when you scale your clusters up or down.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| status | [RebalancingStatus](#v2-clusters-model-rebalancingstatus) | True | Intelligent rebalancing status. The default intelligent rebalancing status is ACTIVE for all new MSK Provisioned clusters with Express brokers. |

### RebalancingStatus
<a name="v2-clusters-model-rebalancingstatus"></a>

Intelligent rebalancing status. The default intelligent rebalancing status is ACTIVE for all new MSK Provisioned clusters with Express brokers.
+ `PAUSED`
+ `ACTIVE`

### S3
<a name="v2-clusters-model-s3"></a>

S3 details for BrokerLogs.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| bucket | string | False | Name of the bucket where the logs will be delivered. |
| enabled | boolean | True | Broker logs for destination S3 enabled or not. |
| prefix | string | False | prefix to the S3 bucket where the logs will be delivered. |

### Sasl
<a name="v2-clusters-model-sasl"></a>

Details for client authentication using SASL.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| iam | [IAM](#v2-clusters-model-iam) | False | Details for ClientAuthentication using IAM. |
| scram | [Scram](#v2-clusters-model-scram) | False | Details for SASL/SCRAM client authentication. |

### Scram
<a name="v2-clusters-model-scram"></a>

Details for SASL/SCRAM client authentication.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| enabled | boolean | False | SASL/SCRAM authentication is enabled or not. |

### Serverless
<a name="v2-clusters-model-serverless"></a>

Properties to create a serverless cluster

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| clientAuthentication | [ServerlessClientAuthentication](#v2-clusters-model-serverlessclientauthentication) | True | Includes all client authentication related information. |
| kafkaVersion | string | False | The version of Apache Kafka for the serverless cluster. |
| vpcConfigs | Array of type [VpcConfig](#v2-clusters-model-vpcconfig) | True | VPC configuration information |

### ServerlessClientAuthentication
<a name="v2-clusters-model-serverlessclientauthentication"></a>

Details for client authentication using SASL.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| sasl | [ServerlessSasl](#v2-clusters-model-serverlesssasl) | False | Details for ClientAuthentication using IAM. |

### ServerlessRequest
<a name="v2-clusters-model-serverlessrequest"></a>

Properties for creating a serverless cluster.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| clientAuthentication | [ServerlessClientAuthentication](#v2-clusters-model-serverlessclientauthentication) | True | Includes all client authentication related information. |
| vpcConfigs | Array of type [VpcConfig](#v2-clusters-model-vpcconfig) | True | VPC configuration information |

### ServerlessSasl
<a name="v2-clusters-model-serverlesssasl"></a>

Details for client authentication using SASL for Serverless Cluster.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| iam | [IAM](#v2-clusters-model-iam) | False | Details for ClientAuthentication using IAM for Serverless Cluster. |

### StateInfo
<a name="v2-clusters-model-stateinfo"></a>

Includes information about the cluster state.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| code | string | False | Code for cluster state. |
| message | string | False | Message for cluster state. |

### StorageInfo
<a name="v2-clusters-model-storageinfo"></a>

Contains information about the storage volumes that are attached to the brokers.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| ebsStorageInfo | [EBSStorageInfo](#v2-clusters-model-ebsstorageinfo) | False | EBS volume information. |

### StorageMode
<a name="v2-clusters-model-storagemode"></a>

Controls storage mode for various supported storage tiers.
+ `LOCAL`
+ `TIERED`

### Tls
<a name="v2-clusters-model-tls"></a>

The details of client authentication using TLS.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| certificateAuthorityArnList | Array of type string | False | List of ACM CertificateAuthority ARNs. |
| enabled | boolean | False | Whether TLS authentication is turned on. |

### Unauthenticated
<a name="v2-clusters-model-unauthenticated"></a>

Details for allowing no client authentication.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| enabled | boolean | False | Unauthenticated is enabled or not. |

### VpcConfig
<a name="v2-clusters-model-vpcconfig"></a>

Includes information about subnets and security groups for a VPC.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| securityGroupIds | Array of type string | False | The security groups to attach to the ENIs for the broker nodes. |
| subnetIds | Array of type string | True | The list of subnets in the client VPC to connect to. Client subnets can't occupy the Availability Zone with ID use1-az3. |

### VpcConnectivity
<a name="v2-clusters-model-vpcconnectivity"></a>

VPC connection control settings for brokers.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| clientAuthentication | [VpcConnectivityClientAuthentication](#v2-clusters-model-vpcconnectivityclientauthentication) | False | VPC connection control settings for brokers. |

### VpcConnectivityClientAuthentication
<a name="v2-clusters-model-vpcconnectivityclientauthentication"></a>

Includes all client authentication information for VpcConnectivity.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| sasl | [VpcConnectivitySasl](#v2-clusters-model-vpcconnectivitysasl) | False | Details for VpcConnectivity ClientAuthentication using SASL. |
| tls | [VpcConnectivityTls](#v2-clusters-model-vpcconnectivitytls) | False | Details for VpcConnectivity ClientAuthentication using TLS. |

### VpcConnectivityIAM
<a name="v2-clusters-model-vpcconnectivityiam"></a>

Details for SASL/IAM client authentication for VpcConnectivity.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| enabled | boolean | False | Specifies whether SASL/IAM authentication is enabled or not. |

### VpcConnectivitySasl
<a name="v2-clusters-model-vpcconnectivitysasl"></a>

Details for client authentication using SASL for VpcConnectivity.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| iam | [VpcConnectivityIAM](#v2-clusters-model-vpcconnectivityiam) | False | Details for ClientAuthentication using IAM for VpcConnectivity. |
| scram | [VpcConnectivityScram](#v2-clusters-model-vpcconnectivityscram) | False | Details for SASL/SCRAM client authentication for VpcConnectivity. |

### VpcConnectivityScram
<a name="v2-clusters-model-vpcconnectivityscram"></a>

Details for SASL/SCRAM client authentication for vpcConnectivity.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| enabled | boolean | False | Specifies whether SASL/SCRAM authentication is enabled or not. |

### VpcConnectivityTls
<a name="v2-clusters-model-vpcconnectivitytls"></a>

Details for client authentication using TLS for vpcConnectivity.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| enabled | boolean | False | Specifies whether TLS authentication is enabled or not. |

## See also
<a name="v2-clusters-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### ListClustersV2
<a name="ListClustersV2-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/kafka-2018-11-14/ListClustersV2)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/kafka-2018-11-14/ListClustersV2)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/kafka-2018-11-14/ListClustersV2)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/kafka-2018-11-14/ListClustersV2)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/kafka-2018-11-14/ListClustersV2)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/kafka-2018-11-14/ListClustersV2)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/kafka-2018-11-14/ListClustersV2)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/kafka-2018-11-14/ListClustersV2)
+ [AWS SDK for Python](/goto/boto3/kafka-2018-11-14/ListClustersV2)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/kafka-2018-11-14/ListClustersV2)

### CreateClusterV2
<a name="CreateClusterV2-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/kafka-2018-11-14/CreateClusterV2)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/kafka-2018-11-14/CreateClusterV2)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/kafka-2018-11-14/CreateClusterV2)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/kafka-2018-11-14/CreateClusterV2)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/kafka-2018-11-14/CreateClusterV2)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/kafka-2018-11-14/CreateClusterV2)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/kafka-2018-11-14/CreateClusterV2)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/kafka-2018-11-14/CreateClusterV2)
+ [AWS SDK for Python](/goto/boto3/kafka-2018-11-14/CreateClusterV2)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/kafka-2018-11-14/CreateClusterV2)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Streaming for Apache Kafka. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query MSK` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
