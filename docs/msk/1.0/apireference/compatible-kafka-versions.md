---
source_url: https://docs.aws.amazon.com/msk/1.0/apireference/compatible-kafka-versions.html
---

# Compatible Apache Kafka Versions
<a name="compatible-kafka-versions"></a>

The Apache Kafka versions to which you can update the cluster.

## URI
<a name="compatible-kafka-versions-url"></a>

`/v1/compatible-kafka-versions`

## HTTP methods
<a name="compatible-kafka-versions-http-methods"></a>

### GET
<a name="compatible-kafka-versionsget"></a>

**Operation ID:** `GetCompatibleKafkaVersions`

Returns a list of the Apache Kafka versions to which you can update this cluster.

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| clusterArn | String | False | The Amazon Resource Name (ARN) of the cluster check. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 |  GetCompatibleKafkaVersionsResponse | 200 response |
| 400 | Error | The request isn't valid because the input is incorrect. Correct your input and then submit it again. |
| 401 | Error | The request is not authorized. The provided credentials couldn't be validated. |
| 403 | Error | Access forbidden. Check your credentials and then retry your request. |
| 404 | Error | The resource could not be found due to incorrect input. Correct the input, then retry the request. |
| 429 | Error | 429 response |
| 500 | Error | There was an unexpected internal server error. Retrying your request might resolve the issue. |
| 503 | Error | 503 response |

### OPTIONS
<a name="compatible-kafka-versionsoptions"></a>

Enable CORS by returning the correct headers.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | Default response for CORS method |

## Schemas
<a name="compatible-kafka-versions-schemas"></a>

### Response bodies
<a name="compatible-kafka-versions-response-examples"></a>

#### GetCompatibleKafkaVersionsResponse schema
<a name="compatible-kafka-versions-response-body-getcompatiblekafkaversionsresponse-example"></a>

```
{
  "compatibleKafkaVersions": [
    {
      "sourceVersion": "string",
      "targetVersions": [
        "string"
      ]
    }
  ]
}
```

#### Error schema
<a name="compatible-kafka-versions-response-body-error-example"></a>

```
{
  "message": "string",
  "invalidParameter": "string"
}
```

## Properties
<a name="compatible-kafka-versions-properties"></a>

### CompatibleKafkaVersion
<a name="compatible-kafka-versions-model-compatiblekafkaversion"></a>

Contains source Apache Kafka versions and compatible target Apache Kafka versions.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| sourceVersion | string | False | An Apache Kafka version. |
| targetVersions | Array of type string | False | A list of Apache Kafka versions. |

### Error
<a name="compatible-kafka-versions-model-error"></a>

Returns information about an error.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| invalidParameter | string | False | The parameter that caused the error. |
| message | string | False | The description of the error. |

### GetCompatibleKafkaVersionsResponse
<a name="compatible-kafka-versions-model-getcompatiblekafkaversionsresponse"></a>

Response body for GetCompatibleKafkaVersions.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| compatibleKafkaVersions | Array of type [CompatibleKafkaVersion](#compatible-kafka-versions-model-compatiblekafkaversion) | False | A list of CompatibleKafkaVersion objects. |

## See also
<a name="compatible-kafka-versions-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### GetCompatibleKafkaVersions
<a name="GetCompatibleKafkaVersions-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/kafka-2018-11-14/GetCompatibleKafkaVersions)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/kafka-2018-11-14/GetCompatibleKafkaVersions)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/kafka-2018-11-14/GetCompatibleKafkaVersions)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/kafka-2018-11-14/GetCompatibleKafkaVersions)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/kafka-2018-11-14/GetCompatibleKafkaVersions)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/kafka-2018-11-14/GetCompatibleKafkaVersions)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/kafka-2018-11-14/GetCompatibleKafkaVersions)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/kafka-2018-11-14/GetCompatibleKafkaVersions)
+ [AWS SDK for Python](/goto/boto3/kafka-2018-11-14/GetCompatibleKafkaVersions)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/kafka-2018-11-14/GetCompatibleKafkaVersions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Streaming for Apache Kafka. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query msk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
