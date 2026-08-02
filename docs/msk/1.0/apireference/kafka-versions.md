---
source_url: https://docs.aws.amazon.com/msk/1.0/apireference/kafka-versions.html
---

# Apache Kafka Versions
<a name="kafka-versions"></a>

Objects that represent Apache Kafka versions.

## URI
<a name="kafka-versions-url"></a>

`/v1/kafka-versions`

## HTTP methods
<a name="kafka-versions-http-methods"></a>

### GET
<a name="kafka-versionsget"></a>

**Operation ID:** `ListKafkaVersions`

Returns the Apache Kafka version objects.

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| nextToken | String | False | The paginated results marker. When the result of the operation is truncated, the call returns `NextToken` in the response. To get the next batch, provide this token in your next request. |
| maxResults | String | False | The maximum number of results to return in the response (default maximum 100 results per API call). If there are more results, the response includes a `NextToken` parameter. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 |  ListKafkaVersionsResponse | 200 response |
| 400 | Error | The request isn't valid because the input is incorrect. Correct your input and then submit it again. |
| 401 | Error | The request is not authorized. The provided credentials couldn't be validated. |
| 403 | Error | Access forbidden. Check your credentials and then retry your request. |
| 404 | Error | The resource could not be found due to incorrect input. Correct the input, then retry the request. |
| 429 | Error | 429 response |
| 500 | Error | There was an unexpected internal server error. Retrying your request might resolve the issue. |
| 503 | Error | 503 response |

### OPTIONS
<a name="kafka-versionsoptions"></a>

Enable CORS by returning the correct headers.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | Default response for CORS method |

## Schemas
<a name="kafka-versions-schemas"></a>

### Response bodies
<a name="kafka-versions-response-examples"></a>

#### ListKafkaVersionsResponse schema
<a name="kafka-versions-response-body-listkafkaversionsresponse-example"></a>

```
{
  "nextToken": "string",
  "kafkaVersions": [
    {
      "version": "string",
      "status": enum
    }
  ]
}
```

#### Error schema
<a name="kafka-versions-response-body-error-example"></a>

```
{
  "message": "string",
  "invalidParameter": "string"
}
```

## Properties
<a name="kafka-versions-properties"></a>

### Error
<a name="kafka-versions-model-error"></a>

Returns information about an error.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| invalidParameter | string | False | The parameter that caused the error. |
| message | string | False | The description of the error. |

### KafkaVersion
<a name="kafka-versions-model-kafkaversion"></a>

Information about an Apache Kafka version.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| status | [KafkaVersionStatus](#kafka-versions-model-kafkaversionstatus) | False | The status of the Apache Kafka version. |
| version | string | False | The Apache Kafka version. |

### KafkaVersionStatus
<a name="kafka-versions-model-kafkaversionstatus"></a>

The status of an Apache Kafka version.
+ `ACTIVE`
+ `DEPRECATED`

### ListKafkaVersionsResponse
<a name="kafka-versions-model-listkafkaversionsresponse"></a>

Response for ListKafkaVersions.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| kafkaVersions | Array of type [KafkaVersion](#kafka-versions-model-kafkaversion) | False | An array of Apache Kafka version objects. |
| nextToken | string | False | Paginated results marker. |

## See also
<a name="kafka-versions-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### ListKafkaVersions
<a name="ListKafkaVersions-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/kafka-2018-11-14/ListKafkaVersions)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/kafka-2018-11-14/ListKafkaVersions)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/kafka-2018-11-14/ListKafkaVersions)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/kafka-2018-11-14/ListKafkaVersions)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/kafka-2018-11-14/ListKafkaVersions)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/kafka-2018-11-14/ListKafkaVersions)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/kafka-2018-11-14/ListKafkaVersions)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/kafka-2018-11-14/ListKafkaVersions)
+ [AWS SDK for Python](/goto/boto3/kafka-2018-11-14/ListKafkaVersions)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/kafka-2018-11-14/ListKafkaVersions)
