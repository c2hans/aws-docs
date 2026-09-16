---
source_url: https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-operations.html
---

# Cluster Operations
<a name="clusters-clusterarn-operations"></a>

Represents the operations that have been performed on an MSK cluster.

## URI
<a name="clusters-clusterarn-operations-url"></a>

`/v1/clusters/{{clusterArn}}/operations`

## HTTP methods
<a name="clusters-clusterarn-operations-http-methods"></a>

### GET
<a name="clusters-clusterarn-operationsget"></a>

**Operation ID:** `ListClusterOperations`

Returns a list of all the operations that have been performed on the specified MSK cluster.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{clusterArn}} | String | True | The Amazon Resource Name (ARN) that uniquely identifies the cluster. |

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| nextToken | String | False | The paginated results marker. When the result of the operation is truncated, the call returns `NextToken` in the response. To get the next batch, provide this token in your next request. |
| maxResults | String | False | The maximum number of results to return in the response (default maximum 100 results per API call). If there are more results, the response includes a `NextToken` parameter. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 |  ListClusterOperationsResponse | Successful response. |
| 400 | Error | The request isn't valid because the input is incorrect. Correct your input and then submit it again. |
| 401 | Error | The request is not authorized. The provided credentials couldn't be validated. |
| 403 | Error | Access forbidden. Check your credentials and then retry your request. |
| 404 | Error | The resource could not be found due to incorrect input. Correct the input, then retry the request. |
| 429 | Error | 429 response |
| 500 | Error | There was an unexpected internal server error. Retrying your request might resolve the issue. |
| 503 | Error | 503 response |

### OPTIONS
<a name="clusters-clusterarn-operationsoptions"></a>

Enable CORS by returning the correct headers.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{clusterArn}} | String | True | The Amazon Resource Name (ARN) that uniquely identifies the cluster. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | Default response for CORS method |

## Schemas
<a name="clusters-clusterarn-operations-schemas"></a>

### Response bodies
<a name="clusters-clusterarn-operations-response-examples"></a>

#### ListClusterOperationsResponse schema
<a name="clusters-clusterarn-operations-response-body-listclusteroperationsresponse-example"></a>

```
{
  "nextToken": "string",
  "clusterOperationInfoList": [
    {
      "clusterArn": "string",
      "creationTime": "string",
      "clientRequestId": "string",
      "operationState": "string",
      "sourceClusterInfo": {
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
        "brokerCountUpdateInfo": {
          "createdBrokerIds": [
            number
          ],
          "deletedBrokerIds": [
            number
          ]
        },
        "instanceType": "string",
        "zookeeperAccess": {
          "enabled": boolean
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
        "brokerEBSVolumeInfo": [
          {
            "volumeSizeGB": integer,
            "provisionedThroughput": {
              "volumeThroughput": integer,
              "enabled": boolean
            },
            "kafkaBrokerNodeId": "string"
          }
        ],
        "numberOfBrokerNodes": integer,
        "enhancedMonitoring": enum,
        "storageMode": enum,
        "kafkaVersion": "string",
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
      "errorInfo": {
        "errorString": "string",
        "errorCode": "string"
      },
      "vpcConnectionInfo": {
        "owner": "string",
        "vpcConnectionArn": "string",
        "creationTime": "string",
        "userIdentity": {
          "principalId": "string",
          "type": enum
        }
      },
      "operationType": "string",
      "endTime": "string",
      "operationSteps": [
        {
          "stepName": "string",
          "stepInfo": {
            "stepStatus": "string"
          }
        }
      ],
      "operationArn": "string",
      "targetClusterInfo": {
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
        "brokerCountUpdateInfo": {
          "createdBrokerIds": [
            number
          ],
          "deletedBrokerIds": [
            number
          ]
        },
        "instanceType": "string",
        "zookeeperAccess": {
          "enabled": boolean
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
        "brokerEBSVolumeInfo": [
          {
            "volumeSizeGB": integer,
            "provisionedThroughput": {
              "volumeThroughput": integer,
              "enabled": boolean
            },
            "kafkaBrokerNodeId": "string"
          }
        ],
        "numberOfBrokerNodes": integer,
        "enhancedMonitoring": enum,
        "storageMode": enum,
        "kafkaVersion": "string",
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
    }
  ]
}
```

#### Error schema
<a name="clusters-clusterarn-operations-response-body-error-example"></a>

```
{
  "message": "string",
  "invalidParameter": "string"
}
```

## Properties
<a name="clusters-clusterarn-operations-properties"></a>

### AuthorizerLogs
<a name="clusters-clusterarn-operations-model-authorizerlogs"></a>

Authorizer Logs details for cluster.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| cloudWatchLogs | [CloudWatchLogs](#clusters-clusterarn-operations-model-cloudwatchlogs) | False | CloudWatch Log destination details. |
| firehose | [Firehose](#clusters-clusterarn-operations-model-firehose) | False | Firehose Log destination details. |
| s3 | [S3](#clusters-clusterarn-operations-model-s3) | False | S3 Log destination details. |

### BrokerCountUpdateInfo
<a name="clusters-clusterarn-operations-model-brokercountupdateinfo"></a>

Contains the list of broker ids being changed during a broker count update.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| createdBrokerIds | Array of type number | False | List of Kafka Broker IDs being created. If operation is INCREASE\_BROKER\_COUNT, the list contains numeric ids of brokers added by the operation. |
| deletedBrokerIds | Array of type number | False | List of Kafka Broker IDs being deleted. If operation is DECREASE\_BROKER\_COUNT, the list contains numeric ids of brokers removed by the operation. |

### BrokerEBSVolumeInfo
<a name="clusters-clusterarn-operations-model-brokerebsvolumeinfo"></a>

Specifies the EBS volume upgrade information. The broker identifier must be set to the keyword `ALL`. This means the changes apply to all the brokers in the cluster.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| kafkaBrokerNodeId | string | True | The ID of the broker to update. The only allowed value is `ALL`. This means that Amazon MSK applies the same storage update to all broker nodes. |
| provisionedThroughput | [ProvisionedThroughput](#clusters-clusterarn-operations-model-provisionedthroughput) | False | EBS volume provisioned throughput information. |
| volumeSizeGB | integer | False | Size of the EBS volume to update. |

### BrokerLogs
<a name="clusters-clusterarn-operations-model-brokerlogs"></a>

The broker logs configuration for this MSK cluster.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| cloudWatchLogs | [CloudWatchLogs](#clusters-clusterarn-operations-model-cloudwatchlogs) | False | Details of the CloudWatch Logs destination for broker logs. |
| firehose | [Firehose](#clusters-clusterarn-operations-model-firehose) | False | Details of the Kinesis Data Firehose delivery stream that is the destination for broker logs. |
| s3 | [S3](#clusters-clusterarn-operations-model-s3) | False | Details of the Amazon S3 destination for broker logs. |

### ClientAuthentication
<a name="clusters-clusterarn-operations-model-clientauthentication"></a>

Includes all client authentication information.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| sasl | [Sasl](#clusters-clusterarn-operations-model-sasl) | False | Details for client authentication using SASL. To turn on SASL, you must also turn on `EncryptionInTransit` by setting `inCluster` to true. You must set `clientBroker` to either `TLS` or `TLS_PLAINTEXT`. If you choose `TLS_PLAINTEXT`, then you must also set `unauthenticated` to true. |
| tls | [Tls](#clusters-clusterarn-operations-model-tls) | False | Details for ClientAuthentication using TLS. To turn on TLS access control, you must also turn on `EncryptionInTransit` by setting `inCluster` to true and `clientBroker` to `TLS`. |
| unauthenticated | [Unauthenticated](#clusters-clusterarn-operations-model-unauthenticated) | False | Details for ClientAuthentication using no authentication. |

### ClientBroker
<a name="clusters-clusterarn-operations-model-clientbroker"></a>

Client-broker encryption in transit setting.
+ `TLS`
+ `TLS_PLAINTEXT`
+ `PLAINTEXT`

### CloudWatchLogs
<a name="clusters-clusterarn-operations-model-cloudwatchlogs"></a>

Details of the CloudWatch Logs destination for broker logs.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| enabled | boolean | True | Specifies whether broker logs get sent to the specified CloudWatch Logs destination. |
| logGroup | string | False | The CloudWatch log group that is the destination for broker logs. |

### ClusterOperationInfo
<a name="clusters-clusterarn-operations-model-clusteroperationinfo"></a>

Returns information about a cluster operation.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| clientRequestId | string | False | The ID of the API request that triggered this operation. |
| clusterArn | string | False | ARN of the cluster. |
| creationTime | string | False | The time that the operation was created. |
| endTime | string | False | The time at which the operation finished. |
| errorInfo | [ErrorInfo](#clusters-clusterarn-operations-model-errorinfo) | False | Describes the error if the operation fails. |
| operationArn | string | False | ARN of the cluster operation. |
| operationState | string | False | State of the cluster operation. |
| operationSteps | Array of type [ClusterOperationStep](#clusters-clusterarn-operations-model-clusteroperationstep) | False | Steps completed during the operation. |
| operationType | string | False | Type of the cluster operation. |
| sourceClusterInfo | [MutableClusterInfo](#clusters-clusterarn-operations-model-mutableclusterinfo) | False | Information about cluster attributes before a cluster is updated. |
| targetClusterInfo | [MutableClusterInfo](#clusters-clusterarn-operations-model-mutableclusterinfo) | False | Information about cluster attributes after a cluster is updated. |
| vpcConnectionInfo | [VpcConnectionInfo](#clusters-clusterarn-operations-model-vpcconnectioninfo) | False | Description of the VPC connection for CreateVpcConnection and DeleteVpcConnection operations. |

### ClusterOperationStep
<a name="clusters-clusterarn-operations-model-clusteroperationstep"></a>

Step taken during a cluster operation.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| stepInfo | [ClusterOperationStepInfo](#clusters-clusterarn-operations-model-clusteroperationstepinfo) | False | Information about the step and its status. |
| stepName | string | False | The name of the step. |

### ClusterOperationStepInfo
<a name="clusters-clusterarn-operations-model-clusteroperationstepinfo"></a>

Information about a step in an operation.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| stepStatus | string | False | The step's current status. |

### ConfigurationInfo
<a name="clusters-clusterarn-operations-model-configurationinfo"></a>

Specifies the configuration to use for the brokers.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| arn | string | True | ARN of the configuration to use. |
| revision | integer<br />Format: int64<br />Minimum: 1 | True | The revision of the configuration to use. |

### ConnectivityInfo
<a name="clusters-clusterarn-operations-model-connectivityinfo"></a>

Broker access controls.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| networkType | string<br />MinLength: 4<br />MaxLength: 4 | False | The network type of the cluster, which is IPv4 or DUAL. The DUAL network type uses both IPv4 and IPv6 addresses for your cluster and its resources. By default, a cluster uses the IPv4 network type. |
| publicAccess | [PublicAccess](#clusters-clusterarn-operations-model-publicaccess) | False | Access control settings for the cluster's brokers. |
| vpcConnectivity | [VpcConnectivity](#clusters-clusterarn-operations-model-vpcconnectivity) | False | VPC connection control settings for brokers |

### EncryptionAtRest
<a name="clusters-clusterarn-operations-model-encryptionatrest"></a>

The data-volume encryption details. You can't update encryption at rest settings for existing clusters.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| dataVolumeKMSKeyId | string | True | The Amazon Resource Name (ARN) of the Amazon KMS key for encrypting data at rest. If you don't specify a KMS key, MSK creates one for you and uses it. |

### EncryptionInTransit
<a name="clusters-clusterarn-operations-model-encryptionintransit"></a>

The settings for encrypting data in transit.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| clientBroker | [ClientBroker](#clusters-clusterarn-operations-model-clientbroker) | False | Indicates the encryption setting for data in transit between clients and brokers. You must set it to one of the following values.<br /> `TLS` means that client-broker communication is enabled with TLS only.<br /> `TLS_PLAINTEXT` means that client-broker communication is enabled for both TLS-encrypted, as well as plaintext data.<br /> `PLAINTEXT` means that client-broker communication is enabled in plaintext only.<br />The default value is `TLS`. |
| inCluster | boolean | False | When set to true, it indicates that data communication among the broker nodes of the cluster is encrypted. When set to false, the communication happens in plaintext.<br />The default value is true. |

### EncryptionInfo
<a name="clusters-clusterarn-operations-model-encryptioninfo"></a>

Includes encryption-related information, such as the Amazon KMS key used for encrypting data at rest and whether you want MSK to encrypt your data in transit.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| encryptionAtRest | [EncryptionAtRest](#clusters-clusterarn-operations-model-encryptionatrest) | False | The data-volume encryption details. |
| encryptionInTransit | [EncryptionInTransit](#clusters-clusterarn-operations-model-encryptionintransit) | False | The details for encryption in transit. |

### EnhancedMonitoring
<a name="clusters-clusterarn-operations-model-enhancedmonitoring"></a>

Specifies which Apache Kafka metrics Amazon MSK gathers and sends to Amazon CloudWatch for this cluster. This property has three possible values: `DEFAULT`, `PER_BROKER`, and `PER_TOPIC_PER_BROKER`. For a list of the metrics associated with each of these three levels of monitoring, see [Monitoring](https://docs.aws.amazon.com/msk/latest/developerguide/monitoring.html).
+ `DEFAULT`
+ `PER_BROKER`
+ `PER_TOPIC_PER_BROKER`
+ `PER_TOPIC_PER_PARTITION`

### Error
<a name="clusters-clusterarn-operations-model-error"></a>

Returns information about an error.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| invalidParameter | string | False | The parameter that caused the error. |
| message | string | False | The description of the error. |

### ErrorInfo
<a name="clusters-clusterarn-operations-model-errorinfo"></a>

Returns information about an error state of the cluster.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| errorCode | string | False | A number describing the error programmatically. |
| errorString | string | False | An optional field to provide more details about the error. |

### Firehose
<a name="clusters-clusterarn-operations-model-firehose"></a>

Firehose details for BrokerLogs.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| deliveryStream | string | False | The Kinesis Data Firehose delivery stream that is the destination for broker logs. |
| enabled | boolean | True | Specifies whether broker logs get sent to the specified Kinesis Data Firehose delivery stream. |

### IAM
<a name="clusters-clusterarn-operations-model-iam"></a>

Details for SASL/IAM client authentication.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| enabled | boolean | False | SASL/IAM authentication is enabled or not. |

### JmxExporter
<a name="clusters-clusterarn-operations-model-jmxexporter"></a>

Indicates whether you want to enable or disable the JMX Exporter.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| enabledInBroker | boolean | True | Indicates whether you want to enable or disable the JMX Exporter. |

### ListClusterOperationsResponse
<a name="clusters-clusterarn-operations-model-listclusteroperationsresponse"></a>

The response contains an array containing cluster operation information and a next token if the response is truncated. Displays operations of the type DECREASE\_BROKER\_COUNT in results list (after a successful broker removal operation).

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| clusterOperationInfoList | Array of type [ClusterOperationInfo](#clusters-clusterarn-operations-model-clusteroperationinfo) | False | An array of cluster operation information objects. |
| nextToken | string | False | If the response of ListClusterOperations is truncated, Amazon MSK returns a NextToken in the response. Send this NextToken in your subsequent request to ListClusterOperations. |

### LoggingInfo
<a name="clusters-clusterarn-operations-model-logginginfo"></a>

You can configure your MSK cluster to send broker logs to different destination types. This is a container for the configuration details related to broker logs.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| authorizerLogs | [AuthorizerLogs](#clusters-clusterarn-operations-model-authorizerlogs) | False | Authorizer Logs details. |
| brokerLogs | [BrokerLogs](#clusters-clusterarn-operations-model-brokerlogs) | False | You can configure your MSK cluster to send broker logs to different destination types. This configuration specifies the details of these destinations. |

### MutableClusterInfo
<a name="clusters-clusterarn-operations-model-mutableclusterinfo"></a>

Information about cluster attributes that can be updated via update APIs.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| brokerCountUpdateInfo | [BrokerCountUpdateInfo](#clusters-clusterarn-operations-model-brokercountupdateinfo) | False | Describes brokers being changed during a broker count update. |
| brokerEBSVolumeInfo | Array of type [BrokerEBSVolumeInfo](#clusters-clusterarn-operations-model-brokerebsvolumeinfo) | False | Specifies the size of the EBS volume and the ID of the associated broker. |
| clientAuthentication | [ClientAuthentication](#clusters-clusterarn-operations-model-clientauthentication) | False | Client Authentication details. |
| configurationInfo | [ConfigurationInfo](#clusters-clusterarn-operations-model-configurationinfo) | False | Information about the changes in the configuration of the brokers. |
| connectivityInfo | [ConnectivityInfo](#clusters-clusterarn-operations-model-connectivityinfo) | False | Defines the connectivity setting of the cluster. |
| encryptionInfo | [EncryptionInfo](#clusters-clusterarn-operations-model-encryptioninfo) | False | Encryption details. |
| enhancedMonitoring | [EnhancedMonitoring](#clusters-clusterarn-operations-model-enhancedmonitoring) | False | The monitoring level. |
| instanceType | string | False | The broker type. |
| kafkaVersion | string | False | The Apache Kafka version. |
| loggingInfo | [LoggingInfo](#clusters-clusterarn-operations-model-logginginfo) | False | LoggingInfo details. |
| numberOfBrokerNodes | integer | False | The number of broker nodes in the cluster. |
| openMonitoring | [OpenMonitoring](#clusters-clusterarn-operations-model-openmonitoring) | False | Open monitoring details. |
| rebalancing | [Rebalancing](#clusters-clusterarn-operations-model-rebalancing) | False | Specifies if intelligent rebalancing is turned on for your cluster. The default intelligent rebalancing status is `ACTIVE` for all new MSK Provisioned clusters that you create with Express brokers. |
| storageMode | [StorageMode](#clusters-clusterarn-operations-model-storagemode) | False | This controls storage mode for supported storage tiers. |
| zookeeperAccess | [ZookeeperAccess](#clusters-clusterarn-operations-model-zookeeperaccess) | False | The ZooKeeper access setting for the cluster. |

### NodeExporter
<a name="clusters-clusterarn-operations-model-nodeexporter"></a>

Indicates whether you want to enable or disable the Node Exporter.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| enabledInBroker | boolean | True | Indicates whether you want to enable or disable the Node Exporter. |

### OpenMonitoring
<a name="clusters-clusterarn-operations-model-openmonitoring"></a>

JMX and Node monitoring for the MSK cluster.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| prometheus | [Prometheus](#clusters-clusterarn-operations-model-prometheus) | True | Prometheus exporter settings. |

### Prometheus
<a name="clusters-clusterarn-operations-model-prometheus"></a>

Prometheus settings for open monitoring.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| jmxExporter | [JmxExporter](#clusters-clusterarn-operations-model-jmxexporter) | False | Indicates whether you want to enable or disable the JMX Exporter. |
| nodeExporter | [NodeExporter](#clusters-clusterarn-operations-model-nodeexporter) | False | Indicates whether you want to enable or disable the Node Exporter. |

### ProvisionedThroughput
<a name="clusters-clusterarn-operations-model-provisionedthroughput"></a>

Contains information about provisioned throughput for EBS storage volumes attached to kafka broker nodes.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| enabled | boolean | False | Provisioned throughput is enabled or not. |
| volumeThroughput | integer | False | Throughput value of the EBS volumes for the data drive on each kafka broker node in MiB per second. |

### PublicAccess
<a name="clusters-clusterarn-operations-model-publicaccess"></a>

Broker access controls

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| type | string | False | DISABLED means that public access is turned off. SERVICE\_PROVIDED\_EIPS means that public access is turned on. |

### Rebalancing
<a name="clusters-clusterarn-operations-model-rebalancing"></a>

Specifies whether or not intelligent rebalancing is turned on for a newly created MSK Provisioned cluster with Express brokers. Intelligent rebalancing performs automatic partition balancing operations when you scale your clusters up or down.

By default, intelligent rebalancing is `ACTIVE` for all new Express-based clusters.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| status | [RebalancingStatus](#clusters-clusterarn-operations-model-rebalancingstatus) | True | Intelligent rebalancing status. The default intelligent rebalancing status is `ACTIVE` for all new Express-based clusters. |

### RebalancingStatus
<a name="clusters-clusterarn-operations-model-rebalancingstatus"></a>

Intelligent rebalancing status. The default intelligent rebalancing status is `ACTIVE` for all new Express-based clusters.
+ `PAUSED`
+ `ACTIVE`

### S3
<a name="clusters-clusterarn-operations-model-s3"></a>

The details of the Amazon S3 destination for broker logs.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| bucket | string | False | The name of the S3 bucket that is the destination for broker logs. |
| enabled | boolean | True | Specifies whether broker logs get sent to the specified Amazon S3 destination. |
| prefix | string | False | The S3 prefix that is the destination for broker logs. |

### Sasl
<a name="clusters-clusterarn-operations-model-sasl"></a>

Details for client authentication using SASL. To turn on SASL, you must also turn on `EncryptionInTransit` by setting `inCluster` to true. You must set `clientBroker` to either `TLS` or `TLS_PLAINTEXT`. If you choose `TLS_PLAINTEXT`, then you must also set `unauthenticated` to true.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| iam | [IAM](#clusters-clusterarn-operations-model-iam) | False | Details for ClientAuthentication using IAM. |
| scram | [Scram](#clusters-clusterarn-operations-model-scram) | False | Details for SASL/SCRAM client authentication. |

### Scram
<a name="clusters-clusterarn-operations-model-scram"></a>

Details for SASL/SCRAM client authentication.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| enabled | boolean | False | SASL/SCRAM authentication is enabled or not. |

### StorageMode
<a name="clusters-clusterarn-operations-model-storagemode"></a>

Controls storage mode for various supported storage tiers.
+ `LOCAL`
+ `TIERED`

### Tls
<a name="clusters-clusterarn-operations-model-tls"></a>

Details for client authentication using TLS.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| certificateAuthorityArnList | Array of type string | False | List of AWS Private CA Amazon Resource Name (ARN)s. |
| enabled | boolean | False | TLS authentication is enabled or not. |

### Unauthenticated
<a name="clusters-clusterarn-operations-model-unauthenticated"></a>

Details for allowing no client authentication.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| enabled | boolean | False | Unauthenticated is enabled or not. |

### UserIdentity
<a name="clusters-clusterarn-operations-model-useridentity"></a>

Description of the requester that calls the API operation.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| principalId | string | False | A unique identifier for the requester that calls the API operation. |
| type | [UserIdentityType](#clusters-clusterarn-operations-model-useridentitytype) | False | The identity type of the requester that calls the API operation. |

### UserIdentityType
<a name="clusters-clusterarn-operations-model-useridentitytype"></a>

The identity type of the requester that calls the API operation.
+ `AWSAccount`
+ `AWSService`

### VpcConnectionInfo
<a name="clusters-clusterarn-operations-model-vpcconnectioninfo"></a>

Description of the VPC connection.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| creationTime | string | False | The time when Amazon MSK creates the VPC Connnection. |
| owner | string | False | The owner of the VPC Connection. |
| userIdentity | [UserIdentity](#clusters-clusterarn-operations-model-useridentity) | False | Description of the requester that calls the API operation. |
| vpcConnectionArn | string | False | The Amazon Resource Name (ARN) of the VPC connection. |

### VpcConnectivity
<a name="clusters-clusterarn-operations-model-vpcconnectivity"></a>

VPC connection control settings for brokers.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| clientAuthentication | [VpcConnectivityClientAuthentication](#clusters-clusterarn-operations-model-vpcconnectivityclientauthentication) | False | VPC connection control settings for brokers. |

### VpcConnectivityClientAuthentication
<a name="clusters-clusterarn-operations-model-vpcconnectivityclientauthentication"></a>

Includes all client authentication information for VpcConnectivity.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| sasl | [VpcConnectivitySasl](#clusters-clusterarn-operations-model-vpcconnectivitysasl) | False | Details for VpcConnectivity ClientAuthentication using SASL. |
| tls | [VpcConnectivityTls](#clusters-clusterarn-operations-model-vpcconnectivitytls) | False | Details for VpcConnectivity ClientAuthentication using TLS. |

### VpcConnectivityIAM
<a name="clusters-clusterarn-operations-model-vpcconnectivityiam"></a>

Details for SASL/IAM client authentication for VpcConnectivity.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| enabled | boolean | False | SASL/IAM authentication is enabled or not. |

### VpcConnectivitySasl
<a name="clusters-clusterarn-operations-model-vpcconnectivitysasl"></a>

Details for client authentication using SASL for VpcConnectivity.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| iam | [VpcConnectivityIAM](#clusters-clusterarn-operations-model-vpcconnectivityiam) | False | Details for ClientAuthentication using IAM for VpcConnectivity. |
| scram | [VpcConnectivityScram](#clusters-clusterarn-operations-model-vpcconnectivityscram) | False | Details for SASL/SCRAM client authentication for VpcConnectivity. |

### VpcConnectivityScram
<a name="clusters-clusterarn-operations-model-vpcconnectivityscram"></a>

Details for SASL/SCRAM client authentication for vpcConnectivity.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| enabled | boolean | False | SASL/SCRAM authentication is enabled or not. |

### VpcConnectivityTls
<a name="clusters-clusterarn-operations-model-vpcconnectivitytls"></a>

Details for client authentication using TLS for vpcConnectivity.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| enabled | boolean | False | TLS authentication is enabled or not. |

### ZookeeperAccess
<a name="clusters-clusterarn-operations-model-zookeeperaccess"></a>

ZooKeeper access control settings for the cluster.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| enabled | boolean | False | Specifies whether direct Apache ZooKeeper client access is enabled or disabled for the cluster. |

## See also
<a name="clusters-clusterarn-operations-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### ListClusterOperations
<a name="ListClusterOperations-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/kafka-2018-11-14/ListClusterOperations)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/kafka-2018-11-14/ListClusterOperations)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/kafka-2018-11-14/ListClusterOperations)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/kafka-2018-11-14/ListClusterOperations)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/kafka-2018-11-14/ListClusterOperations)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/kafka-2018-11-14/ListClusterOperations)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/kafka-2018-11-14/ListClusterOperations)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/kafka-2018-11-14/ListClusterOperations)
+ [AWS SDK for Python (Boto3)](/goto/boto3/kafka-2018-11-14/ListClusterOperations)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/kafka-2018-11-14/ListClusterOperations)
