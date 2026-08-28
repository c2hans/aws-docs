---
source_url: https://docs.aws.amazon.com/medialive/latest/apireference/batch-start.html
---

# Batch action: start
<a name="batch-start"></a>

## URI
<a name="batch-start-url"></a>

`/prod/batch/start`

## HTTP methods
<a name="batch-start-http-methods"></a>

### POST
<a name="batch-startpost"></a>

**Operation ID:** `BatchStart`

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | BatchStartResultModel | 200 response |
| 400 | InvalidRequest | 400 response |
| 403 | AccessDenied | 403 response |
| 404 | ResourceNotFound | 404 response |
| 409 | ResourceConflict | 409 response |
| 429 | LimitExceeded | 429 response |
| 500 | InternalServiceError | 500 response |
| 502 | BadGatewayException | 502 response |
| 504 | GatewayTimeoutException | 504 response |

## Schemas
<a name="batch-start-schemas"></a>

### Request bodies
<a name="batch-start-request-examples"></a>

#### POST schema
<a name="batch-start-request-body-post-example"></a>

```
{
  "channelIds": [
    "string"
  ],
  "multiplexIds": [
    "string"
  ]
}
```

### Response bodies
<a name="batch-start-response-examples"></a>

#### BatchStartResultModel schema
<a name="batch-start-response-body-batchstartresultmodel-example"></a>

```
{
  "failed": [
    {
      "arn": "string",
      "code": "string",
      "id": "string",
      "message": "string"
    }
  ],
  "successful": [
    {
      "arn": "string",
      "id": "string",
      "state": "string"
    }
  ]
}
```

#### InvalidRequest schema
<a name="batch-start-response-body-invalidrequest-example"></a>

```
{
  "message": "string"
}
```

#### AccessDenied schema
<a name="batch-start-response-body-accessdenied-example"></a>

```
{
  "message": "string"
}
```

#### ResourceNotFound schema
<a name="batch-start-response-body-resourcenotfound-example"></a>

```
{
  "message": "string"
}
```

#### ResourceConflict schema
<a name="batch-start-response-body-resourceconflict-example"></a>

```
{
  "message": "string"
}
```

#### LimitExceeded schema
<a name="batch-start-response-body-limitexceeded-example"></a>

```
{
  "message": "string"
}
```

#### InternalServiceError schema
<a name="batch-start-response-body-internalserviceerror-example"></a>

```
{
  "message": "string"
}
```

#### BadGatewayException schema
<a name="batch-start-response-body-badgatewayexception-example"></a>

```
{
  "message": "string"
}
```

#### GatewayTimeoutException schema
<a name="batch-start-response-body-gatewaytimeoutexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="batch-start-properties"></a>

### AccessDenied
<a name="batch-start-model-accessdenied"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### BadGatewayException
<a name="batch-start-model-badgatewayexception"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### BatchFailedResultModel
<a name="batch-start-model-batchfailedresultmodel"></a>

Details from a failed operation

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| arn | string | False | ARN of the resource |
| code | string | False | Error code for the failed operation |
| id | string | False | ID of the resource |
| message | string | False | Error message for the failed operation |

### BatchStart
<a name="batch-start-model-batchstart"></a>

Batch start resource request

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| channelIds | Array of type string | False | List of channel IDs |
| multiplexIds | Array of type string | False | List of multiplex IDs |

### BatchStartResultModel
<a name="batch-start-model-batchstartresultmodel"></a>

Batch start resource results

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| failed | Array of type [BatchFailedResultModel](#batch-start-model-batchfailedresultmodel) | False | List of failed operations |
| successful | Array of type [BatchSuccessfulResultModel](#batch-start-model-batchsuccessfulresultmodel) | False | List of successful operations |

### BatchSuccessfulResultModel
<a name="batch-start-model-batchsuccessfulresultmodel"></a>

Details from a successful operation

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| arn | string | False | ARN of the resource |
| id | string | False | ID of the resource |
| state | string | False | Current state of the resource |

### GatewayTimeoutException
<a name="batch-start-model-gatewaytimeoutexception"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### InternalServiceError
<a name="batch-start-model-internalserviceerror"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### InvalidRequest
<a name="batch-start-model-invalidrequest"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### LimitExceeded
<a name="batch-start-model-limitexceeded"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### ResourceConflict
<a name="batch-start-model-resourceconflict"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### ResourceNotFound
<a name="batch-start-model-resourcenotfound"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

## See also
<a name="batch-start-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### BatchStart
<a name="BatchStart-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/medialive-2017-10-14/BatchStart)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/medialive-2017-10-14/BatchStart)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/medialive-2017-10-14/BatchStart)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/medialive-2017-10-14/BatchStart)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/medialive-2017-10-14/BatchStart)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/medialive-2017-10-14/BatchStart)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/medialive-2017-10-14/BatchStart)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/medialive-2017-10-14/BatchStart)
+ [AWS SDK for Python](/goto/boto3/medialive-2017-10-14/BatchStart)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/medialive-2017-10-14/BatchStart)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
