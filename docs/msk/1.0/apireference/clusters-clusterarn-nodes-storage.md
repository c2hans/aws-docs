---
source_url: https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-nodes-storage.html
---

# Broker Storage
<a name="clusters-clusterarn-nodes-storage"></a>

Represents the EBS storage associated with the brokers.

## URI
<a name="clusters-clusterarn-nodes-storage-url"></a>

`/v1/clusters/{{clusterArn}}/nodes/storage`

## HTTP methods
<a name="clusters-clusterarn-nodes-storage-http-methods"></a>

### PUT
<a name="clusters-clusterarn-nodes-storageput"></a>

**Operation ID:** `UpdateBrokerStorage`

Updates the EBS storage associated with Amazon MSK brokers. You can increase the amount of EBS storage per broker. You can't decrease the storage. To increase storage, wait for the cluster to be in the ACTIVE state. Storage volumes remain available during this scaling-up operation.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{clusterArn}} | String | True | The Amazon Resource Name (ARN) that uniquely identifies the cluster. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 |  UpdateBrokerStorageResponse | Successful response. |
| 400 | Error | The request isn't valid because the input is incorrect. Correct your input and then submit it again. |
| 401 | Error | The request is not authorized. The provided credentials couldn't be validated. |
| 403 | Error | Access forbidden. Check your credentials and then retry your request. |
| 404 | Error | The resource could not be found due to incorrect input. Correct the input, then retry the request. |
| 429 | Error | 429 response |
| 500 | Error | There was an unexpected internal server error. Retrying your request might resolve the issue. |
| 503 | Error | 503 response |

### OPTIONS
<a name="clusters-clusterarn-nodes-storageoptions"></a>

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
<a name="clusters-clusterarn-nodes-storage-schemas"></a>

### Request bodies
<a name="clusters-clusterarn-nodes-storage-request-examples"></a>

#### PUT schema
<a name="clusters-clusterarn-nodes-storage-request-body-put-example"></a>

```
{
  "targetBrokerEBSVolumeInfo": [
    {
      "volumeSizeGB": integer,
      "provisionedThroughput": {
        "volumeThroughput": integer,
        "enabled": boolean
      },
      "kafkaBrokerNodeId": "string"
    }
  ],
  "currentVersion": "string"
}
```

### Response bodies
<a name="clusters-clusterarn-nodes-storage-response-examples"></a>

#### UpdateBrokerStorageResponse schema
<a name="clusters-clusterarn-nodes-storage-response-body-updatebrokerstorageresponse-example"></a>

```
{
  "clusterArn": "string",
  "clusterOperationArn": "string"
}
```

#### Error schema
<a name="clusters-clusterarn-nodes-storage-response-body-error-example"></a>

```
{
  "message": "string",
  "invalidParameter": "string"
}
```

## Properties
<a name="clusters-clusterarn-nodes-storage-properties"></a>

### BrokerEBSVolumeInfo
<a name="clusters-clusterarn-nodes-storage-model-brokerebsvolumeinfo"></a>

Specifies the EBS volume upgrade information. The broker identifier must be set to the keyword `ALL`. This means the changes apply to all the brokers in the cluster.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| kafkaBrokerNodeId | string | True | The ID of the broker to update. The only allowed value is `ALL`. This means that Amazon MSK applies the same storage update to all broker nodes. |
| provisionedThroughput | [ProvisionedThroughput](#clusters-clusterarn-nodes-storage-model-provisionedthroughput) | False | EBS volume provisioned throughput information. |
| volumeSizeGB | integer | False | Size of the EBS volume to update. |

### Error
<a name="clusters-clusterarn-nodes-storage-model-error"></a>

Returns information about an error.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| invalidParameter | string | False | The parameter that caused the error. |
| message | string | False | The description of the error. |

### ProvisionedThroughput
<a name="clusters-clusterarn-nodes-storage-model-provisionedthroughput"></a>

Contains information about provisioned throughput for EBS storage volumes attached to kafka broker nodes.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| enabled | boolean | False | Provisioned throughput is enabled or not. |
| volumeThroughput | integer | False | Throughput value of the EBS volumes for the data drive on each kafka broker node in MiB per second. |

### UpdateBrokerStorageRequest
<a name="clusters-clusterarn-nodes-storage-model-updatebrokerstoragerequest"></a>

Request object for UpdateBrokerStorage.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| currentVersion | string | True | The version of the MSK cluster to update. Cluster versions aren't simple numbers. You can describe an MSK cluster to find its version. When this update operation is successful, it generates a new cluster version.  |
| targetBrokerEBSVolumeInfo | Array of type [BrokerEBSVolumeInfo](#clusters-clusterarn-nodes-storage-model-brokerebsvolumeinfo) | True | Describes the target volume size and the ID of the broker to apply the update to.<br />The value you specify for Target-Volume-in-GiB must be a whole number that is greater than 100 GiB.<br />The storage per broker after the update operation can't exceed 16384 GiB. |

### UpdateBrokerStorageResponse
<a name="clusters-clusterarn-nodes-storage-model-updatebrokerstorageresponse"></a>

Response body for UpdateBrokerStorage.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| clusterArn | string | False | The Amazon Resource Name (ARN) of the cluster. |
| clusterOperationArn | string | False | The Amazon Resource Name (ARN) of the cluster operation. |

## See also
<a name="clusters-clusterarn-nodes-storage-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### UpdateBrokerStorage
<a name="UpdateBrokerStorage-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/kafka-2018-11-14/UpdateBrokerStorage)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/kafka-2018-11-14/UpdateBrokerStorage)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/kafka-2018-11-14/UpdateBrokerStorage)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/kafka-2018-11-14/UpdateBrokerStorage)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/kafka-2018-11-14/UpdateBrokerStorage)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/kafka-2018-11-14/UpdateBrokerStorage)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/kafka-2018-11-14/UpdateBrokerStorage)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/kafka-2018-11-14/UpdateBrokerStorage)
+ [AWS SDK for Python (Boto3)](/goto/boto3/kafka-2018-11-14/UpdateBrokerStorage)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/kafka-2018-11-14/UpdateBrokerStorage)
