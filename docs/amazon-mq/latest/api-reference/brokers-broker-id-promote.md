---
source_url: https://docs.aws.amazon.com/amazon-mq/latest/api-reference/brokers-broker-id-promote.html
---

# Brokers broker-id Promote
<a name="brokers-broker-id-promote"></a>

## URI
<a name="brokers-broker-id-promote-url"></a>

`/v1/brokers/{{broker-id}}/promote`

## HTTP methods
<a name="brokers-broker-id-promote-http-methods"></a>

### POST
<a name="brokers-broker-id-promotepost"></a>

**Operation ID:** `Promote`

Promotes a data replication replica broker to a primary.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{broker-id}} | String | True | The unique ID that Amazon MQ generates for the broker. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 |  PromoteOutput | HTTP Status Code 200: OK. |
| 400 | Error | HTTP Status Code 400: Bad request due to incorrect input. Correct your request and then retry it. |
| 403 | Error | HTTP Status Code 403: Access forbidden. Correct your credentials and then retry your request. |
| 404 | Error | HTTP Status Code 404: Resource not found due to incorrect input. Correct your request and then retry it. |
| 500 | Error | HTTP Status Code 500: Unexpected internal server error. Retrying your request might resolve the issue. |

### OPTIONS
<a name="brokers-broker-id-promoteoptions"></a>

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{broker-id}} | String | True | The unique ID that Amazon MQ generates for the broker. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | Default response for CORS method |

## Schemas
<a name="brokers-broker-id-promote-schemas"></a>

### Request bodies
<a name="brokers-broker-id-promote-request-examples"></a>

#### POST schema
<a name="brokers-broker-id-promote-request-body-post-example"></a>

```
{
  "mode": enum
}
```

### Response bodies
<a name="brokers-broker-id-promote-response-examples"></a>

#### PromoteOutput schema
<a name="brokers-broker-id-promote-response-body-promoteoutput-example"></a>

```
{
  "brokerId": "string"
}
```

#### Error schema
<a name="brokers-broker-id-promote-response-body-error-example"></a>

```
{
  "errorAttribute": "string",
  "message": "string"
}
```

## Properties
<a name="brokers-broker-id-promote-properties"></a>

### Error
<a name="brokers-broker-id-promote-model-error"></a>

Returns information about an error.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| errorAttribute | string | False | The attribute which caused the error. |
| message | string | False | The explanation of the error. |

### PromoteInput
<a name="brokers-broker-id-promote-model-promoteinput"></a>

Creates a Promote request with the properties specified.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| mode | [PromoteMode](#brokers-broker-id-promote-model-promotemode) | True | The Promote mode requested. Note: Valid values for the parameter are SWITCHOVER, FAILOVER. |

### PromoteMode
<a name="brokers-broker-id-promote-model-promotemode"></a>

The Promote mode requested.
+ `SWITCHOVER`
+ `FAILOVER`

### PromoteOutput
<a name="brokers-broker-id-promote-model-promoteoutput"></a>

Returns information about the updated broker.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| brokerId | string | False | The unique ID that Amazon MQ generates for the broker. |

## See also
<a name="brokers-broker-id-promote-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### Promote
<a name="Promote-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/mq-2017-11-27/Promote)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/mq-2017-11-27/Promote)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/mq-2017-11-27/Promote)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/mq-2017-11-27/Promote)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/mq-2017-11-27/Promote)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/mq-2017-11-27/Promote)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/mq-2017-11-27/Promote)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/mq-2017-11-27/Promote)
+ [AWS SDK for Python](/goto/boto3/mq-2017-11-27/Promote)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/mq-2017-11-27/Promote)
