---
source_url: https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-storage.html
---

# UpdateStorage
<a name="clusters-clusterarn-storage"></a>

Updates cluster broker volume size (or) sets cluster storage mode to TIERED.

## URI
<a name="clusters-clusterarn-storage-url"></a>

`/v1/clusters/{{clusterArn}}/storage`

## HTTP methods
<a name="clusters-clusterarn-storage-http-methods"></a>

### PUT
<a name="clusters-clusterarn-storageput"></a>

**Operation ID:** `UpdateStorage`

Updates cluster broker volume size (or) sets cluster storage mode to TIERED.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{clusterArn}} | String | True | The Amazon Resource Name (ARN) that uniquely identifies the cluster. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 |  UpdateStorageResponse | Successful response. |
| 400 | Error | The request isn't valid because the input is incorrect. Correct your input and then submit it again. |
| 401 | Error | The request is not authorized. The provided credentials couldn't be validated. |
| 403 | Error | Access forbidden. Check your credentials and then retry your request. |
| 404 | Error | The resource could not be found due to incorrect input. Correct the input, then retry the request. |
| 429 | Error | 429 response |
| 500 | Error | There was an unexpected internal server error. Retrying your request might resolve the issue. |
| 503 | Error | 503 response |

### OPTIONS
<a name="clusters-clusterarn-storageoptions"></a>

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
<a name="clusters-clusterarn-storage-schemas"></a>

### Request bodies
<a name="clusters-clusterarn-storage-request-examples"></a>

#### PUT schema
<a name="clusters-clusterarn-storage-request-body-put-example"></a>

```
{
  "volumeSizeGB": integer,
  "storageMode": enum,
  "provisionedThroughput": {
    "volumeThroughput": integer,
    "enabled": boolean
  },
  "currentVersion": "string"
}
```

### Response bodies
<a name="clusters-clusterarn-storage-response-examples"></a>

#### UpdateStorageResponse schema
<a name="clusters-clusterarn-storage-response-body-updatestorageresponse-example"></a>

```
{
  "clusterArn": "string",
  "clusterOperationArn": "string"
}
```

#### Error schema
<a name="clusters-clusterarn-storage-response-body-error-example"></a>

```
{
  "message": "string",
  "invalidParameter": "string"
}
```

## Properties
<a name="clusters-clusterarn-storage-properties"></a>

### Error
<a name="clusters-clusterarn-storage-model-error"></a>

Returns information about an error.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| invalidParameter | string | False | The parameter that caused the error. |
| message | string | False | The description of the error. |

### ProvisionedThroughput
<a name="clusters-clusterarn-storage-model-provisionedthroughput"></a>

Contains information about provisioned throughput for EBS storage volumes attached to kafka broker nodes.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| enabled | boolean | False | Provisioned throughput is enabled or not. |
| volumeThroughput | integer | False | Throughput value of the EBS volumes for the data drive on each kafka broker node in MiB per second. |

### StorageMode
<a name="clusters-clusterarn-storage-model-storagemode"></a>

Controls storage mode for various supported storage tiers.
+ `LOCAL`
+ `TIERED`

### UpdateStorageRequest
<a name="clusters-clusterarn-storage-model-updatestoragerequest"></a>

Request object for UpdateStorageApi.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| currentVersion | string | True | The version of cluster to update from. A successful operation will then generate a new version. |
| provisionedThroughput | [ProvisionedThroughput](#clusters-clusterarn-storage-model-provisionedthroughput) | False | EBS volume provisioned throughput information. |
| storageMode | [StorageMode](#clusters-clusterarn-storage-model-storagemode) | False | Controls storage mode for supported storage tiers. |
| volumeSizeGB | integer | False | size of the EBS volume to update. |

### UpdateStorageResponse
<a name="clusters-clusterarn-storage-model-updatestorageresponse"></a>

Response body for UpdateStorageResponse Api.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| clusterArn | string | False | The Amazon Resource Name (ARN) of the cluster. |
| clusterOperationArn | string | False | The Amazon Resource Name (ARN) of the cluster operation. |

## See also
<a name="clusters-clusterarn-storage-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### UpdateStorage
<a name="UpdateStorage-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/kafka-2018-11-14/UpdateStorage)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/kafka-2018-11-14/UpdateStorage)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/kafka-2018-11-14/UpdateStorage)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/kafka-2018-11-14/UpdateStorage)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/kafka-2018-11-14/UpdateStorage)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/kafka-2018-11-14/UpdateStorage)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/kafka-2018-11-14/UpdateStorage)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/kafka-2018-11-14/UpdateStorage)
+ [AWS SDK for Python (Boto3)](/goto/boto3/kafka-2018-11-14/UpdateStorage)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/kafka-2018-11-14/UpdateStorage)
