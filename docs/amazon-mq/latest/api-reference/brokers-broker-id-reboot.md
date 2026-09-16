---
source_url: https://docs.aws.amazon.com/amazon-mq/latest/api-reference/brokers-broker-id-reboot.html
---

# Broker Reboot
<a name="brokers-broker-id-reboot"></a>

To apply a new configuration to a broker or to initiate a failover in a multi-AZ broker, you can reboot the broker. In addition, if your broker becomes unresponsive, you can reboot it to recover from a faulty state.

**Note**
You can reboot only a broker with the RUNNING status.

## URI
<a name="brokers-broker-id-reboot-url"></a>

`/v1/brokers/{{broker-id}}/reboot`

## HTTP methods
<a name="brokers-broker-id-reboot-http-methods"></a>

### POST
<a name="brokers-broker-id-rebootpost"></a>

**Operation ID:** `RebootBroker`

Reboots a broker. Note: This API is asynchronous.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{broker-id}} | String | True | The unique ID that Amazon MQ generates for the broker. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | HTTP Status Code 200: OK. |
| 400 | Error | HTTP Status Code 400: Bad request due to incorrect input. Correct your request and then retry it. |
| 403 | Error | HTTP Status Code 403: Access forbidden. Correct your credentials and then retry your request. |
| 404 | Error | HTTP Status Code 404: Resource not found due to incorrect input. Correct your request and then retry it. |
| 500 | Error | HTTP Status Code 500: Unexpected internal server error. Retrying your request might resolve the issue. |

### OPTIONS
<a name="brokers-broker-id-rebootoptions"></a>

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{broker-id}} | String | True | The unique ID that Amazon MQ generates for the broker. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | Default response for CORS method |

## Schemas
<a name="brokers-broker-id-reboot-schemas"></a>

### Response bodies
<a name="brokers-broker-id-reboot-response-examples"></a>

#### Error schema
<a name="brokers-broker-id-reboot-response-body-error-example"></a>

```
{
  "errorAttribute": "string",
  "message": "string"
}
```

## Properties
<a name="brokers-broker-id-reboot-properties"></a>

### Error
<a name="brokers-broker-id-reboot-model-error"></a>

Returns information about an error.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| errorAttribute | string | False | The attribute which caused the error. |
| message | string | False | The explanation of the error. |

## See also
<a name="brokers-broker-id-reboot-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### RebootBroker
<a name="RebootBroker-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/mq-2017-11-27/RebootBroker)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/mq-2017-11-27/RebootBroker)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/mq-2017-11-27/RebootBroker)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/mq-2017-11-27/RebootBroker)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/mq-2017-11-27/RebootBroker)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/mq-2017-11-27/RebootBroker)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/mq-2017-11-27/RebootBroker)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/mq-2017-11-27/RebootBroker)
+ [AWS SDK for Python (Boto3)](/goto/boto3/mq-2017-11-27/RebootBroker)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/mq-2017-11-27/RebootBroker)
