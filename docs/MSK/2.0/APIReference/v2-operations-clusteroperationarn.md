---
source_url: https://docs.aws.amazon.com/MSK/2.0/APIReference/v2-operations-clusteroperationarn.html
---

# V2 Operations clusterOperationArn
<a name="v2-operations-clusteroperationarn"></a>

## URI
<a name="v2-operations-clusteroperationarn-url"></a>

`/api/v2/operations/{{clusterOperationArn}}`

## HTTP methods
<a name="v2-operations-clusteroperationarn-http-methods"></a>

### GET
<a name="v2-operations-clusteroperationarnget"></a>

**Operation ID:** `DescribeClusterOperationV2`

Returns a description of the cluster operation specified by the ARN.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{clusterOperationArn}} | String | True | ARN of the cluster operation to describe. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 |  DescribeClusterOperationV2Response | 200 response |
| 400 | None | HTTP Status Code 400: Bad request due to incorrect input. Correct your request and then retry it. |
| 401 | None | HTTP Status Code 401: Unauthorized request. The provided credentials couldn't be validated. |
| 403 | None | HTTP Status Code 403: Access forbidden. Correct your credentials and then retry your request. |
| 404 | None | HTTP Status Code 404: Resource not found due to incorrect input. Correct your request and then retry it. |
| 429 | None | HTTP Status Code 429: Limit exceeded. Resource limit reached. |
| 500 | None | HTTP Status Code 500: Unexpected internal server error. Retrying your request might resolve the issue. |
| 503 | None | HTTP Status Code 503: Service Unavailable. Retrying your request in some time might resolve the issue. |

### OPTIONS
<a name="v2-operations-clusteroperationarnoptions"></a>

Enable CORS by returning correct headers

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{clusterOperationArn}} | String | True |  |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | 200 response |

## Schemas
<a name="v2-operations-clusteroperationarn-schemas"></a>

### Response bodies
<a name="v2-operations-clusteroperationarn-response-examples"></a>

#### DescribeClusterOperationV2Response schema
<a name="v2-operations-clusteroperationarn-response-body-describeclusteroperationv2response-example"></a>

```
{
  "clusterOperationInfo": {
    "clusterType": enum,
    "clusterArn": "string",
    "provisioned": {
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
          }
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
        },
        "zookeeperAccess": {
          "enabled": boolean
        }
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
      "operationSteps": [
        {
          "stepName": "string",
          "stepInfo": {
            "stepStatus": "string"
          }
        }
      ],
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
          }
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
        },
        "zookeeperAccess": {
          "enabled": boolean
        }
      }
    },
    "operationState": "string",
    "serverless": {
      "vpcConnectionInfo": {
        "owner": "string",
        "vpcConnectionArn": "string",
        "creationTime": "string",
        "userIdentity": {
          "principalId": "string",
          "type": enum
        }
      }
    },
    "errorInfo": {
      "errorString": "string",
      "errorCode": "string"
    },
    "operationType": "string",
    "startTime": "string",
    "endTime": "string",
    "operationArn": "string"
  }
}
```

## Properties
<a name="v2-operations-clusteroperationarn-properties"></a>

### BrokerCountUpdateInfo
<a name="v2-operations-clusteroperationarn-model-brokercountupdateinfo"></a>

Contains the list of broker ids being changed during a broker count update.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| createdBrokerIds | Array of type number | False | List of Kafka Broker IDs being created. |
| deletedBrokerIds | Array of type number | False | List of Kafka Broker IDs being deleted. |

### BrokerEBSVolumeInfo
<a name="v2-operations-clusteroperationarn-model-brokerebsvolumeinfo"></a>

Specifies the EBS volume object per broker which captures broker identifier and corresponding target volume size. Broker identifier could be id or arn or the keyword 'ALL'. If it is 'ALL', all nodes of the cluster will be considered for the operation.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| kafkaBrokerNodeId | string | True | Kafka id of the broker in the cluster to update. |
| provisionedThroughput | [ProvisionedThroughput](#v2-operations-clusteroperationarn-model-provisionedthroughput) | False | EBS volume provisioned throughput information. |
| volumeSizeGB | integer | False | Size of the EBS volume to update. |

### BrokerLogs
<a name="v2-operations-clusteroperationarn-model-brokerlogs"></a>

Broker Logs details for cluster.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| cloudWatchLogs | [CloudWatchLogs](#v2-operations-clusteroperationarn-model-cloudwatchlogs) | False | CloudWatch Log destination details. |
| firehose | [Firehose](#v2-operations-clusteroperationarn-model-firehose) | False |  |
| s3 | [S3](#v2-operations-clusteroperationarn-model-s3) | False | S3 Log destination details. |

### ClientAuthentication
<a name="v2-operations-clusteroperationarn-model-clientauthentication"></a>

Includes all client authentication information.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| sasl | [Sasl](#v2-operations-clusteroperationarn-model-sasl) | False | Details for ClientAuthentication using SASL. |
| tls | [Tls](#v2-operations-clusteroperationarn-model-tls) | False | Details for ClientAuthentication using TLS. |
| unauthenticated | [Unauthenticated](#v2-operations-clusteroperationarn-model-unauthenticated) | False | Details for ClientAuthentication using no authentication. |

### ClientBroker
<a name="v2-operations-clusteroperationarn-model-clientbroker"></a>

Client-broker encryption in transit setting.
+ `TLS`
+ `TLS_PLAINTEXT`
+ `PLAINTEXT`

### CloudWatchLogs
<a name="v2-operations-clusteroperationarn-model-cloudwatchlogs"></a>

CloudWatchLogs details for BrokerLogs.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| enabled | boolean | True | Broker logs for destination CW enabled or not. |
| logGroup | string | False | CloudWatch LogGroup where the logs will be delivered. |

### ClusterOperationStep
<a name="v2-operations-clusteroperationarn-model-clusteroperationstep"></a>

Step taken during a cluster operation.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| stepInfo | [ClusterOperationStepInfo](#v2-operations-clusteroperationarn-model-clusteroperationstepinfo) | False | Information about the step and its status. |
| stepName | string | False | The name of the step. |

### ClusterOperationStepInfo
<a name="v2-operations-clusteroperationarn-model-clusteroperationstepinfo"></a>

State information about the operation step.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| stepStatus | string | False | The steps current status. |

### ClusterOperationV2
<a name="v2-operations-clusteroperationarn-model-clusteroperationv2"></a>

Returns information about a cluster operation.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| clusterArn | string | False | ARN of the cluster. |
| clusterType | [ClusterType](#v2-operations-clusteroperationarn-model-clustertype) | False | Type of the backend cluster. |
| endTime | string | False | The time at which the operation finished. |
| errorInfo | [ErrorInfo](#v2-operations-clusteroperationarn-model-errorinfo) | False | If cluster operation failed from an error, it describes the error. |
| operationArn | string | False | ARN of the cluster operation. |
| operationState | string | False | State of the cluster operation. |
| operationType | string | False | Type of the cluster operation. |
| provisioned | [ClusterOperationV2Provisioned](#v2-operations-clusteroperationarn-model-clusteroperationv2provisioned) | False | Properties of a provisioned cluster. |
| serverless | [ClusterOperationV2Serverless](#v2-operations-clusteroperationarn-model-clusteroperationv2serverless) | False | Properties of a serverless cluster. |
| startTime | string | False | The time at which operation was created. |

### ClusterOperationV2Provisioned
<a name="v2-operations-clusteroperationarn-model-clusteroperationv2provisioned"></a>

Returns information about a provisioned cluster operation.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| operationSteps | Array of type [ClusterOperationStep](#v2-operations-clusteroperationarn-model-clusteroperationstep) | False | Steps completed during the operation. |
| sourceClusterInfo | [MutableClusterInfo](#v2-operations-clusteroperationarn-model-mutableclusterinfo) | False | Information about cluster attributes before a cluster is updated. |
| targetClusterInfo | [MutableClusterInfo](#v2-operations-clusteroperationarn-model-mutableclusterinfo) | False | Information about cluster attributes after a cluster is updated. |
| vpcConnectionInfo | [VpcConnectionInfo](#v2-operations-clusteroperationarn-model-vpcconnectioninfo) | False | Description of the VPC connection for CreateVpcConnection and DeleteVpcConnection operations. |

### ClusterOperationV2Serverless
<a name="v2-operations-clusteroperationarn-model-clusteroperationv2serverless"></a>

Returns information about a serverless cluster operation.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| vpcConnectionInfo | [VpcConnectionInfoServerless](#v2-operations-clusteroperationarn-model-vpcconnectioninfoserverless) | False | Description of the VPC connection for CreateVpcConnection and DeleteVpcConnection operations. |

### ClusterType
<a name="v2-operations-clusteroperationarn-model-clustertype"></a>

The type of backend cluster.
+ `PROVISIONED`
+ `SERVERLESS`

### ConfigurationInfo
<a name="v2-operations-clusteroperationarn-model-configurationinfo"></a>

Specifies the configuration to be used on the brokers.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| arn | string | True | ARN of the configuration to use. |
| revision | integer<br />Format: int64<br />Minimum: 1 | True | The revision of the configuration to use. |

### ConnectivityInfo
<a name="v2-operations-clusteroperationarn-model-connectivityinfo"></a>

Broker access controls

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| publicAccess | [PublicAccess](#v2-operations-clusteroperationarn-model-publicaccess) | False | Access control settings for brokers |
| vpcConnectivity | [VpcConnectivity](#v2-operations-clusteroperationarn-model-vpcconnectivity) | False | VPC connection control settings for brokers. |

### DescribeClusterOperationV2Response
<a name="v2-operations-clusteroperationarn-model-describeclusteroperationv2response"></a>

Information about a cluster operation.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| clusterOperationInfo | [ClusterOperationV2](#v2-operations-clusteroperationarn-model-clusteroperationv2) | False | Cluster operation information. |

### EncryptionAtRest
<a name="v2-operations-clusteroperationarn-model-encryptionatrest"></a>

Details for encryption at rest.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| dataVolumeKMSKeyId | string | True | KMS key used for data volume encryption. |

### EncryptionInTransit
<a name="v2-operations-clusteroperationarn-model-encryptionintransit"></a>

Details for encryption in transit.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| clientBroker | [ClientBroker](#v2-operations-clusteroperationarn-model-clientbroker) | False | Client-broker encryption in transit setting. |
| inCluster | boolean | False | In-cluster encryption in transit setting. |

### EncryptionInfo
<a name="v2-operations-clusteroperationarn-model-encryptioninfo"></a>

Includes all encryption related information.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| encryptionAtRest | [EncryptionAtRest](#v2-operations-clusteroperationarn-model-encryptionatrest) | False | Details for encryption at rest. |
| encryptionInTransit | [EncryptionInTransit](#v2-operations-clusteroperationarn-model-encryptionintransit) | False | Details for encryption in transit. |

### EnhancedMonitoring
<a name="v2-operations-clusteroperationarn-model-enhancedmonitoring"></a>

Controls level of cluster metrics Amazon pushes to customer's cloudwatch account.
+ `DEFAULT`
+ `PER_BROKER`
+ `PER_TOPIC_PER_BROKER`
+ `PER_TOPIC_PER_PARTITION`

### ErrorInfo
<a name="v2-operations-clusteroperationarn-model-errorinfo"></a>

Error Information about a failed cluster operation.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| errorCode | string | False | error code. |
| errorString | string | False | error message. |

### Firehose
<a name="v2-operations-clusteroperationarn-model-firehose"></a>

Firehose details for BrokerLogs.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| deliveryStream | string | False | Firehose delivery stream where the logs will be delivered. |
| enabled | boolean | True | Broker logs for destination firehose enabled or not. |

### IAM
<a name="v2-operations-clusteroperationarn-model-iam"></a>

Details for SASL/IAM client authentication.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| enabled | boolean | False | SASL/IAM authentication is enabled or not. |

### JmxExporter
<a name="v2-operations-clusteroperationarn-model-jmxexporter"></a>

JMX Exporter details.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| enabledInBroker | boolean | True | JMX Exporter being enabled in broker. |

### LoggingInfo
<a name="v2-operations-clusteroperationarn-model-logginginfo"></a>

Logging info details for the cluster.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| brokerLogs | [BrokerLogs](#v2-operations-clusteroperationarn-model-brokerlogs) | True | Broker Logs details. |

### MutableClusterInfo
<a name="v2-operations-clusteroperationarn-model-mutableclusterinfo"></a>

Information about cluster attributes that can be updated using update APIs.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| brokerCountUpdateInfo | [BrokerCountUpdateInfo](#v2-operations-clusteroperationarn-model-brokercountupdateinfo) | False | Describes brokers being changed during a broker count update. |
| brokerEBSVolumeInfo | Array of type [BrokerEBSVolumeInfo](#v2-operations-clusteroperationarn-model-brokerebsvolumeinfo) | False |  |
| clientAuthentication | [ClientAuthentication](#v2-operations-clusteroperationarn-model-clientauthentication) | False | Client Authentication details. |
| configurationInfo | [ConfigurationInfo](#v2-operations-clusteroperationarn-model-configurationinfo) | False | Information about the Kafka configuration deployed on the brokers of the cluster. |
| connectivityInfo | [ConnectivityInfo](#v2-operations-clusteroperationarn-model-connectivityinfo) | False | Defines the connectivity configuration of the cluster. |
| encryptionInfo | [EncryptionInfo](#v2-operations-clusteroperationarn-model-encryptioninfo) | False | Encryption details. |
| enhancedMonitoring | [EnhancedMonitoring](#v2-operations-clusteroperationarn-model-enhancedmonitoring) | False | This knob controls level of metrics pushed customer's CloudWatch account. |
| instanceType | string | False | The instance type. |
| kafkaVersion | string | False | The Kafka version. |
| loggingInfo | [LoggingInfo](#v2-operations-clusteroperationarn-model-logginginfo) | False | LoggingInfo details. |
| numberOfBrokerNodes | integer | False | The number of Kafka broker nodes of the Cluster. |
| openMonitoring | [OpenMonitoring](#v2-operations-clusteroperationarn-model-openmonitoring) | False | Open monitoring details. |
| rebalancing | [Rebalancing](#v2-operations-clusteroperationarn-model-rebalancing) | False | Specifies if intelligent rebalancing is turned on for your cluster. The default intelligent rebalancing status is ACTIVE for all new MSK Provisioned clusters that you create with Express brokers. |
| storageMode | [StorageMode](#v2-operations-clusteroperationarn-model-storagemode) | False | This controls storage mode for supported storage tiers. |
| zookeeperAccess | [ZookeeperAccess](#v2-operations-clusteroperationarn-model-zookeeperaccess) | False | The ZooKeeper access setting for the cluster. |

### NodeExporter
<a name="v2-operations-clusteroperationarn-model-nodeexporter"></a>

Node Exporter details.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| enabledInBroker | boolean | True | Node Exporter being enabled in broker. |

### OpenMonitoring
<a name="v2-operations-clusteroperationarn-model-openmonitoring"></a>

JMX and Node monitoring for cluster.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| prometheus | [Prometheus](#v2-operations-clusteroperationarn-model-prometheus) | True | Prometheus details. |

### Prometheus
<a name="v2-operations-clusteroperationarn-model-prometheus"></a>

Prometheus details.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| jmxExporter | [JmxExporter](#v2-operations-clusteroperationarn-model-jmxexporter) | False | JMX Exporter details. |
| nodeExporter | [NodeExporter](#v2-operations-clusteroperationarn-model-nodeexporter) | False | Node Exporter details. |

### ProvisionedThroughput
<a name="v2-operations-clusteroperationarn-model-provisionedthroughput"></a>

Contains information about provisioned throughput for the EBS storage volumes that are attached to the brokers.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| enabled | boolean | False | Whether provisioned throughput is turned on. |
| volumeThroughput | integer | False | Throughput value of the EBS volumes for the data drive on each broker in MiB per second. |

### PublicAccess
<a name="v2-operations-clusteroperationarn-model-publicaccess"></a>

Broker access controls

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| type | string | False | If public access is disabled, or if enabled the EIP provider |

### Rebalancing
<a name="v2-operations-clusteroperationarn-model-rebalancing"></a>

Contains information about intelligent rebalancing for the cluster. Intelligent rebalancing performs automatic partition balancing operations when you scale your clusters up or down.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| status | [RebalancingStatus](#v2-operations-clusteroperationarn-model-rebalancingstatus) | True | Intelligent rebalancing status. The default intelligent rebalancing status is ACTIVE for all new MSK Provisioned clusters with Express brokers. |

### RebalancingStatus
<a name="v2-operations-clusteroperationarn-model-rebalancingstatus"></a>

Intelligent rebalancing status. The default intelligent rebalancing status is ACTIVE for all new MSK Provisioned clusters with Express brokers.
+ `PAUSED`
+ `ACTIVE`

### S3
<a name="v2-operations-clusteroperationarn-model-s3"></a>

S3 details for BrokerLogs.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| bucket | string | False | Name of the bucket where the logs will be delivered. |
| enabled | boolean | True | Broker logs for destination S3 enabled or not. |
| prefix | string | False | prefix to the S3 bucket where the logs will be delivered. |

### Sasl
<a name="v2-operations-clusteroperationarn-model-sasl"></a>

Details for client authentication using SASL.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| iam | [IAM](#v2-operations-clusteroperationarn-model-iam) | False | Details for ClientAuthentication using IAM. |
| scram | [Scram](#v2-operations-clusteroperationarn-model-scram) | False | Details for SASL/SCRAM client authentication. |

### Scram
<a name="v2-operations-clusteroperationarn-model-scram"></a>

Details for SASL/SCRAM client authentication.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| enabled | boolean | False | SASL/SCRAM authentication is enabled or not. |

### StorageMode
<a name="v2-operations-clusteroperationarn-model-storagemode"></a>

Controls storage mode for various supported storage tiers.
+ `LOCAL`
+ `TIERED`

### Tls
<a name="v2-operations-clusteroperationarn-model-tls"></a>

The details of client authentication using TLS.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| certificateAuthorityArnList | Array of type string | False | List of ACM CertificateAuthority ARNs. |
| enabled | boolean | False | Whether TLS authentication is turned on. |

### Unauthenticated
<a name="v2-operations-clusteroperationarn-model-unauthenticated"></a>

Details for allowing no client authentication.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| enabled | boolean | False | Unauthenticated is enabled or not. |

### UserIdentity
<a name="v2-operations-clusteroperationarn-model-useridentity"></a>

Description of the requester that calls the API operation.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| principalId | string | False | A unique identifier for the requester that calls the API operation. |
| type | [UserIdentityType](#v2-operations-clusteroperationarn-model-useridentitytype) | False | The identity type of the requester that calls the API operation. |

### UserIdentityType
<a name="v2-operations-clusteroperationarn-model-useridentitytype"></a>

The identity type of the requester that calls the API operation.
+ `AWSAccount`
+ `AWSService`

### VpcConnectionInfo
<a name="v2-operations-clusteroperationarn-model-vpcconnectioninfo"></a>

Description of the VPC connection.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| creationTime | string | False | The time when Amazon MSK creates the VPC Connnection. |
| owner | string | False | The owner of the VPC connection. |
| userIdentity | [UserIdentity](#v2-operations-clusteroperationarn-model-useridentity) | False | Description of the requester that calls the API operation. |
| vpcConnectionArn | string | False | The Amazon Resource Name (ARN) of the VPC connection. |

### VpcConnectionInfoServerless
<a name="v2-operations-clusteroperationarn-model-vpcconnectioninfoserverless"></a>

Description of the VPC connection for CreateVpcConnection and DeleteVpcConnection operations.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| creationTime | string | False | The time when Amazon MSK creates the VPC Connnection. |
| owner | string | False | The owner of the VPC connection. |
| userIdentity | [UserIdentity](#v2-operations-clusteroperationarn-model-useridentity) | False | Description of the requester that calls the API operation. |
| vpcConnectionArn | string | False | The Amazon Resource Name (ARN) of the VPC connection. |

### VpcConnectivity
<a name="v2-operations-clusteroperationarn-model-vpcconnectivity"></a>

VPC connection control settings for brokers.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| clientAuthentication | [VpcConnectivityClientAuthentication](#v2-operations-clusteroperationarn-model-vpcconnectivityclientauthentication) | False | VPC connection control settings for brokers. |

### VpcConnectivityClientAuthentication
<a name="v2-operations-clusteroperationarn-model-vpcconnectivityclientauthentication"></a>

Includes all client authentication information for VpcConnectivity.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| sasl | [VpcConnectivitySasl](#v2-operations-clusteroperationarn-model-vpcconnectivitysasl) | False | Details for VpcConnectivity ClientAuthentication using SASL. |
| tls | [VpcConnectivityTls](#v2-operations-clusteroperationarn-model-vpcconnectivitytls) | False | Details for VpcConnectivity ClientAuthentication using TLS. |

### VpcConnectivityIAM
<a name="v2-operations-clusteroperationarn-model-vpcconnectivityiam"></a>

Details for SASL/IAM client authentication for VpcConnectivity.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| enabled | boolean | False | Specifies whether SASL/IAM authentication is enabled or not. |

### VpcConnectivitySasl
<a name="v2-operations-clusteroperationarn-model-vpcconnectivitysasl"></a>

Details for client authentication using SASL for VpcConnectivity.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| iam | [VpcConnectivityIAM](#v2-operations-clusteroperationarn-model-vpcconnectivityiam) | False | Details for ClientAuthentication using IAM for VpcConnectivity. |
| scram | [VpcConnectivityScram](#v2-operations-clusteroperationarn-model-vpcconnectivityscram) | False | Details for SASL/SCRAM client authentication for VpcConnectivity. |

### VpcConnectivityScram
<a name="v2-operations-clusteroperationarn-model-vpcconnectivityscram"></a>

Details for SASL/SCRAM client authentication for vpcConnectivity.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| enabled | boolean | False | Specifies whether SASL/SCRAM authentication is enabled or not. |

### VpcConnectivityTls
<a name="v2-operations-clusteroperationarn-model-vpcconnectivitytls"></a>

Details for client authentication using TLS for vpcConnectivity.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| enabled | boolean | False | Specifies whether TLS authentication is enabled or not. |

### ZookeeperAccess
<a name="v2-operations-clusteroperationarn-model-zookeeperaccess"></a>

ZooKeeper access control settings for the cluster.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| enabled | boolean | False | Specifies whether direct Apache ZooKeeper client access is enabled or disabled for the cluster. |

## See also
<a name="v2-operations-clusteroperationarn-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### DescribeClusterOperationV2
<a name="DescribeClusterOperationV2-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/kafka-2018-11-14/DescribeClusterOperationV2)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/kafka-2018-11-14/DescribeClusterOperationV2)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/kafka-2018-11-14/DescribeClusterOperationV2)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/kafka-2018-11-14/DescribeClusterOperationV2)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/kafka-2018-11-14/DescribeClusterOperationV2)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/kafka-2018-11-14/DescribeClusterOperationV2)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/kafka-2018-11-14/DescribeClusterOperationV2)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/kafka-2018-11-14/DescribeClusterOperationV2)
+ [AWS SDK for Python](/goto/boto3/kafka-2018-11-14/DescribeClusterOperationV2)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/kafka-2018-11-14/DescribeClusterOperationV2)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Streaming for Apache Kafka. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query MSK` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
