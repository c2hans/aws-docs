---
source_url: https://docs.aws.amazon.com/amazon-mq/latest/api-reference/broker-engine-types.html
---

# Broker Engine Types
<a name="broker-engine-types"></a>

Retrieve information about available broker engines. AWS does not support all instance types in all availability zones and regions. For more information, see the [ActiveMQ version management](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/activemq-version-management.html) and the [RabbitMQ version management](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/rabbitmq-version-management.html) sections in the Amazon MQ Developer Guide.

This API will tell you, for a given region and availability zone, which broker engine types and engine versions you can create.

## URI
<a name="broker-engine-types-url"></a>

`/v1/broker-engine-types`

## HTTP methods
<a name="broker-engine-types-http-methods"></a>

### GET
<a name="broker-engine-typesget"></a>

**Operation ID:** `DescribeBrokerEngineTypes`

Describe available engine types and versions.

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| engineType | String | False | Filter response by engine type. |
| nextToken | String | False | The token that specifies the next page of results Amazon MQ should return. To request the first page, leave nextToken empty. |
| maxResults | String | False | The maximum number of brokers that Amazon MQ can return per page (20 by default). This value must be an integer from 5 to 100. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 |  BrokerEngineTypeOutput | HTTP Status Code 200: OK. |
| 400 | Error | HTTP Status Code 400: Bad request due to incorrect input. Correct your request and then retry it. |
| 403 | Error | HTTP Status Code 403: Access forbidden. Correct your credentials and then retry your request. |
| 500 | Error | HTTP Status Code 500: Unexpected internal server error. Retrying your request might resolve the issue. |

### OPTIONS
<a name="broker-engine-typesoptions"></a>

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | Default response for CORS method |

## Schemas
<a name="broker-engine-types-schemas"></a>

### Response bodies
<a name="broker-engine-types-response-examples"></a>

#### BrokerEngineTypeOutput schema
<a name="broker-engine-types-response-body-brokerenginetypeoutput-example"></a>

```
{
  "nextToken": "string",
  "maxResults": integer,
  "brokerEngineTypes": [
    {
      "engineVersions": [
        {
          "name": "string"
        }
      ],
      "engineType": enum
    }
  ]
}
```

#### Error schema
<a name="broker-engine-types-response-body-error-example"></a>

```
{
  "errorAttribute": "string",
  "message": "string"
}
```

## Properties
<a name="broker-engine-types-properties"></a>

### BrokerEngineType
<a name="broker-engine-types-model-brokerenginetype"></a>

Types of broker engines.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| engineType | [EngineType](#broker-engine-types-model-enginetype) | False | The broker's engine type. |
| engineVersions | Array of type [EngineVersion](#broker-engine-types-model-engineversion) | False | The list of engine versions. |

### BrokerEngineTypeOutput
<a name="broker-engine-types-model-brokerenginetypeoutput"></a>

Returns a list of broker engine type.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| brokerEngineTypes | Array of type [BrokerEngineType](#broker-engine-types-model-brokerenginetype) | False | List of available engine types and versions. |
| maxResults | integer<br />Minimum: 5<br />Maximum: 100 | True | Required. The maximum number of engine types that can be returned per page (20 by default). This value must be an integer from 5 to 100. |
| nextToken | string | False | The token that specifies the next page of results Amazon MQ should return. To request the first page, leave nextToken empty. |

### EngineType
<a name="broker-engine-types-model-enginetype"></a>

The type of broker engine. Amazon MQ supports ActiveMQ and RabbitMQ.
+ `ACTIVEMQ`
+ `RABBITMQ`

### EngineVersion
<a name="broker-engine-types-model-engineversion"></a>

Id of the engine version.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| name | string | False | Id for the version. |

### Error
<a name="broker-engine-types-model-error"></a>

Returns information about an error.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| errorAttribute | string | False | The attribute which caused the error. |
| message | string | False | The explanation of the error. |

## See also
<a name="broker-engine-types-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### DescribeBrokerEngineTypes
<a name="DescribeBrokerEngineTypes-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/mq-2017-11-27/DescribeBrokerEngineTypes)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/mq-2017-11-27/DescribeBrokerEngineTypes)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/mq-2017-11-27/DescribeBrokerEngineTypes)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/mq-2017-11-27/DescribeBrokerEngineTypes)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/mq-2017-11-27/DescribeBrokerEngineTypes)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/mq-2017-11-27/DescribeBrokerEngineTypes)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/mq-2017-11-27/DescribeBrokerEngineTypes)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/mq-2017-11-27/DescribeBrokerEngineTypes)
+ [AWS SDK for Python (Boto3)](/goto/boto3/mq-2017-11-27/DescribeBrokerEngineTypes)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/mq-2017-11-27/DescribeBrokerEngineTypes)
