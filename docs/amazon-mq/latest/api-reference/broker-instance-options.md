---
source_url: https://docs.aws.amazon.com/amazon-mq/latest/api-reference/broker-instance-options.html
---

# Broker Instance Options
<a name="broker-instance-options"></a>

You can retrieve information about broker instances. For more information about the different components of an Amazon MQ broker, see [How Amazon MQ works](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/amazon-mq-how-it-works.html) in the *Amazon MQ Developer Guide*.

## URI
<a name="broker-instance-options-url"></a>

`/v1/broker-instance-options`

## HTTP methods
<a name="broker-instance-options-http-methods"></a>

### GET
<a name="broker-instance-optionsget"></a>

**Operation ID:** `DescribeBrokerInstanceOptions`

Describe available broker instance options.

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| hostInstanceType | String | False | Filter response by host instance type. |
| nextToken | String | False | The token that specifies the next page of results Amazon MQ should return. To request the first page, leave nextToken empty. |
| storageType | String | False | Filter response by storage type. |
| maxResults | String | False | The maximum number of brokers that Amazon MQ can return per page (20 by default). This value must be an integer from 5 to 100. |
| engineType | String | False | Filter response by engine type. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 |  BrokerInstanceOptionsOutput | HTTP Status Code 200: OK. |
| 400 | Error | HTTP Status Code 400: Bad request due to incorrect input. Correct your request and then retry it. |
| 403 | Error | HTTP Status Code 403: Access forbidden. Correct your credentials and then retry your request. |
| 500 | Error | HTTP Status Code 500: Unexpected internal server error. Retrying your request might resolve the issue. |

### OPTIONS
<a name="broker-instance-optionsoptions"></a>

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | Default response for CORS method |

## Schemas
<a name="broker-instance-options-schemas"></a>

### Response bodies
<a name="broker-instance-options-response-examples"></a>

#### BrokerInstanceOptionsOutput schema
<a name="broker-instance-options-response-body-brokerinstanceoptionsoutput-example"></a>

```
{
  "nextToken": "string",
  "maxResults": integer,
  "brokerInstanceOptions": [
    {
      "supportedDeploymentModes": [
        enum
      ],
      "supportedEngineVersions": [
        "string"
      ],
      "storageType": enum,
      "engineType": enum,
      "availabilityZones": [
        {
          "name": "string"
        }
      ],
      "hostInstanceType": "string"
    }
  ]
}
```

#### Error schema
<a name="broker-instance-options-response-body-error-example"></a>

```
{
  "errorAttribute": "string",
  "message": "string"
}
```

## Properties
<a name="broker-instance-options-properties"></a>

### AvailabilityZone
<a name="broker-instance-options-model-availabilityzone"></a>

Name of the availability zone.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| name | string | False | Id for the availability zone. |

### BrokerInstanceOption
<a name="broker-instance-options-model-brokerinstanceoption"></a>

Option for host instance type.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| availabilityZones | Array of type [AvailabilityZone](#broker-instance-options-model-availabilityzone) | False | The list of available az. |
| engineType | [EngineType](#broker-instance-options-model-enginetype) | False | The broker's engine type. |
| hostInstanceType | string | False | The broker's instance type. |
| storageType | [BrokerStorageType](#broker-instance-options-model-brokerstoragetype) | False | The broker's storage type. |
| supportedDeploymentModes | Array of type [DeploymentMode](#broker-instance-options-model-deploymentmode) | False | The list of supported deployment modes. |
| supportedEngineVersions | Array of type string | False | The list of supported engine versions. |

### BrokerInstanceOptionsOutput
<a name="broker-instance-options-model-brokerinstanceoptionsoutput"></a>

Returns a list of broker instance options.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| brokerInstanceOptions | Array of type [BrokerInstanceOption](#broker-instance-options-model-brokerinstanceoption) | False | List of available broker instance options. |
| maxResults | integer<br />Minimum: 5<br />Maximum: 100 | True | Required. The maximum number of instance options that can be returned per page (20 by default). This value must be an integer from 5 to 100. |
| nextToken | string | False | The token that specifies the next page of results Amazon MQ should return. To request the first page, leave nextToken empty. |

### BrokerStorageType
<a name="broker-instance-options-model-brokerstoragetype"></a>

The broker's storage type.

**Important**
 `EFS` is not supported for RabbitMQ engine type.
+ `EBS`
+ `EFS`

### DeploymentMode
<a name="broker-instance-options-model-deploymentmode"></a>

The broker's deployment mode.
+ `SINGLE_INSTANCE`
+ `ACTIVE_STANDBY_MULTI_AZ`
+ `CLUSTER_MULTI_AZ`

### EngineType
<a name="broker-instance-options-model-enginetype"></a>

The type of broker engine. Amazon MQ supports ActiveMQ and RabbitMQ.
+ `ACTIVEMQ`
+ `RABBITMQ`

### Error
<a name="broker-instance-options-model-error"></a>

Returns information about an error.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| errorAttribute | string | False | The attribute which caused the error. |
| message | string | False | The explanation of the error. |

## See also
<a name="broker-instance-options-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### DescribeBrokerInstanceOptions
<a name="DescribeBrokerInstanceOptions-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/mq-2017-11-27/DescribeBrokerInstanceOptions)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/mq-2017-11-27/DescribeBrokerInstanceOptions)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/mq-2017-11-27/DescribeBrokerInstanceOptions)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/mq-2017-11-27/DescribeBrokerInstanceOptions)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/mq-2017-11-27/DescribeBrokerInstanceOptions)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/mq-2017-11-27/DescribeBrokerInstanceOptions)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/mq-2017-11-27/DescribeBrokerInstanceOptions)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/mq-2017-11-27/DescribeBrokerInstanceOptions)
+ [AWS SDK for Python (Boto3)](/goto/boto3/mq-2017-11-27/DescribeBrokerInstanceOptions)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/mq-2017-11-27/DescribeBrokerInstanceOptions)
