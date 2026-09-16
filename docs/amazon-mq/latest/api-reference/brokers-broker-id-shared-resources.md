---
source_url: https://docs.aws.amazon.com/amazon-mq/latest/api-reference/brokers-broker-id-shared-resources.html
---

# Shared Resources
<a name="brokers-broker-id-shared-resources"></a>

You can retrieve information about the networking resources shared to a broker for private networking. Use this API to check the status of shared resources and retrieve DNS names for use in your broker configuration.

## URI
<a name="brokers-broker-id-shared-resources-url"></a>

`/v1/brokers/{{broker-id}}/shared-resources`

## HTTP methods
<a name="brokers-broker-id-shared-resources-http-methods"></a>

### GET
<a name="brokers-broker-id-shared-resourcesget"></a>

**Operation ID:** `DescribeSharedResources`

Returns the resources shared to a broker.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{broker-id}} | String | True | The unique ID that Amazon MQ generates for the broker. |

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| nextToken | String | False | The token that specifies the next page of results Amazon MQ should return. To request the first page, leave nextToken empty. |
| maxResults | Integer | False | The maximum number of brokers that Amazon MQ can return per page (20 by default). This value must be an integer from 5 to 100. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 |  DescribeSharedResourcesOutput | HTTP Status Code 200: OK. |
| 400 | Error | HTTP Status Code 400: Bad request due to incorrect input. Correct your request and then retry it. |
| 403 | Error | HTTP Status Code 403: Access forbidden. Correct your credentials and then retry your request. |
| 404 | Error | HTTP Status Code 404: Resource not found due to incorrect input. Correct your request and then retry it. |
| 500 | Error | HTTP Status Code 500: Unexpected internal server error. Retrying your request might resolve the issue. |

### OPTIONS
<a name="brokers-broker-id-shared-resourcesoptions"></a>

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{broker-id}} | String | True | The unique ID that Amazon MQ generates for the broker. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | Default response for CORS method |

## Schemas
<a name="brokers-broker-id-shared-resources-schemas"></a>

### Response bodies
<a name="brokers-broker-id-shared-resources-response-examples"></a>

#### DescribeSharedResourcesOutput schema
<a name="brokers-broker-id-shared-resources-response-body-describesharedresourcesoutput-example"></a>

```
{
  "nextToken": "string",
  "sharedResources": [
    {
      "type": enum,
      "resourceArn": "string",
      "status": enum,
      "dnsNames": [
        "string"
      ],
      "resourceShareArns": [
        "string"
      ],
      "error": {
        "code": enum,
        "message": "string"
      }
    }
  ]
}
```

#### Error schema
<a name="brokers-broker-id-shared-resources-response-body-error-example"></a>

```
{
  "errorAttribute": "string",
  "message": "string"
}
```

## Properties
<a name="brokers-broker-id-shared-resources-properties"></a>

### DescribeSharedResourcesOutput
<a name="brokers-broker-id-shared-resources-model-describesharedresourcesoutput"></a>

Returns the networking resources shared to the broker.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| nextToken | string | False | The token that specifies the next page of results Amazon MQ should return. To request the first page, leave nextToken empty. |
| sharedResources | Array of type [SharedResource](#brokers-broker-id-shared-resources-model-sharedresource) | False | A list of resources shared to the broker. |

### Error
<a name="brokers-broker-id-shared-resources-model-error"></a>

Returns information about an error.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| errorAttribute | string | False | The attribute which caused the error. |
| message | string | False | The explanation of the error. |

### SharedResource
<a name="brokers-broker-id-shared-resources-model-sharedresource"></a>

A resource shared to the broker.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| dnsNames | Array of type string | False | The DNS names accessible by the broker. |
| error | [SharedResourceError](#brokers-broker-id-shared-resources-model-sharedresourceerror) | False | Information on the error encountered by the resource. |
| resourceArn | string | True | The ARN of the shared resource. |
| resourceShareArns | Array of type string | False | The resource shares to which the resource belongs. |
| status | [SharedResourceStatus](#brokers-broker-id-shared-resources-model-sharedresourcestatus) | True | The status of the shared resource. |
| type | [SharedResourceType](#brokers-broker-id-shared-resources-model-sharedresourcetype) | True | The type of shared resource. |

### SharedResourceError
<a name="brokers-broker-id-shared-resources-model-sharedresourceerror"></a>

Information on the error encountered by the resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| code | [SharedResourceErrorCode](#brokers-broker-id-shared-resources-model-sharedresourceerrorcode) | True | The error code associated with the error. |
| message | string | True | The error message. |

### SharedResourceErrorCode
<a name="brokers-broker-id-shared-resources-model-sharedresourceerrorcode"></a>

The error code associated with the error.
+ `RESOURCE_MISSING`
+ `ACCEPT_FAILED`
+ `MISMATCHED_AZ`

### SharedResourceStatus
<a name="brokers-broker-id-shared-resources-model-sharedresourcestatus"></a>

The status of the shared resource.
+ `AVAILABLE`
+ `SETUP_IN_PROGRESS`
+ `DELETION_IN_PROGRESS`
+ `ERROR`

### SharedResourceType
<a name="brokers-broker-id-shared-resources-model-sharedresourcetype"></a>

The type of shared resource.
+ `RESOURCE_SHARE`
+ `RESOURCE`

## See also
<a name="brokers-broker-id-shared-resources-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### DescribeSharedResources
<a name="DescribeSharedResources-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/mq-2017-11-27/DescribeSharedResources)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/mq-2017-11-27/DescribeSharedResources)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/mq-2017-11-27/DescribeSharedResources)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/mq-2017-11-27/DescribeSharedResources)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/mq-2017-11-27/DescribeSharedResources)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/mq-2017-11-27/DescribeSharedResources)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/mq-2017-11-27/DescribeSharedResources)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/mq-2017-11-27/DescribeSharedResources)
+ [AWS SDK for Python (Boto3)](/goto/boto3/mq-2017-11-27/DescribeSharedResources)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/mq-2017-11-27/DescribeSharedResources)
