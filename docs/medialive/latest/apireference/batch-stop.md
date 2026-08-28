---
source_url: https://docs.aws.amazon.com/medialive/latest/apireference/batch-stop.html
---

# Batch action: stop
<a name="batch-stop"></a>

## URI
<a name="batch-stop-url"></a>

`/prod/batch/stop`

## HTTP methods
<a name="batch-stop-http-methods"></a>

### POST
<a name="batch-stoppost"></a>

**Operation ID:** `BatchStop`

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | BatchStopResultModel | 200 response |
| 400 | InvalidRequest | 400 response |
| 403 | AccessDenied | 403 response |
| 404 | ResourceNotFound | 404 response |
| 409 | ResourceConflict | 409 response |
| 429 | LimitExceeded | 429 response |
| 500 | InternalServiceError | 500 response |
| 502 | BadGatewayException | 502 response |
| 504 | GatewayTimeoutException | 504 response |

## Schemas
<a name="batch-stop-schemas"></a>

### Request bodies
<a name="batch-stop-request-examples"></a>

#### POST schema
<a name="batch-stop-request-body-post-example"></a>

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
<a name="batch-stop-response-examples"></a>

#### BatchStopResultModel schema
<a name="batch-stop-response-body-batchstopresultmodel-example"></a>

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
<a name="batch-stop-response-body-invalidrequest-example"></a>

```
{
  "message": "string"
}
```

#### AccessDenied schema
<a name="batch-stop-response-body-accessdenied-example"></a>

```
{
  "message": "string"
}
```

#### ResourceNotFound schema
<a name="batch-stop-response-body-resourcenotfound-example"></a>

```
{
  "message": "string"
}
```

#### ResourceConflict schema
<a name="batch-stop-response-body-resourceconflict-example"></a>

```
{
  "message": "string"
}
```

#### LimitExceeded schema
<a name="batch-stop-response-body-limitexceeded-example"></a>

```
{
  "message": "string"
}
```

#### InternalServiceError schema
<a name="batch-stop-response-body-internalserviceerror-example"></a>

```
{
  "message": "string"
}
```

#### BadGatewayException schema
<a name="batch-stop-response-body-badgatewayexception-example"></a>

```
{
  "message": "string"
}
```

#### GatewayTimeoutException schema
<a name="batch-stop-response-body-gatewaytimeoutexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="batch-stop-properties"></a>

### AccessDenied
<a name="batch-stop-model-accessdenied"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### BadGatewayException
<a name="batch-stop-model-badgatewayexception"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### BatchFailedResultModel
<a name="batch-stop-model-batchfailedresultmodel"></a>

Details from a failed operation

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| arn | string | False | ARN of the resource |
| code | string | False | Error code for the failed operation |
| id | string | False | ID of the resource |
| message | string | False | Error message for the failed operation |

### BatchStop
<a name="batch-stop-model-batchstop"></a>

Batch stop resource request

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| channelIds | Array of type string | False | List of channel IDs |
| multiplexIds | Array of type string | False | List of multiplex IDs |

### BatchStopResultModel
<a name="batch-stop-model-batchstopresultmodel"></a>

Batch stop resource results

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| failed | Array of type [BatchFailedResultModel](#batch-stop-model-batchfailedresultmodel) | False | List of failed operations |
| successful | Array of type [BatchSuccessfulResultModel](#batch-stop-model-batchsuccessfulresultmodel) | False | List of successful operations |

### BatchSuccessfulResultModel
<a name="batch-stop-model-batchsuccessfulresultmodel"></a>

Details from a successful operation

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| arn | string | False | ARN of the resource |
| id | string | False | ID of the resource |
| state | string | False | Current state of the resource |

### GatewayTimeoutException
<a name="batch-stop-model-gatewaytimeoutexception"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### InternalServiceError
<a name="batch-stop-model-internalserviceerror"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### InvalidRequest
<a name="batch-stop-model-invalidrequest"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### LimitExceeded
<a name="batch-stop-model-limitexceeded"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### ResourceConflict
<a name="batch-stop-model-resourceconflict"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### ResourceNotFound
<a name="batch-stop-model-resourcenotfound"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

## See also
<a name="batch-stop-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### BatchStop
<a name="BatchStop-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/medialive-2017-10-14/BatchStop)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/medialive-2017-10-14/BatchStop)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/medialive-2017-10-14/BatchStop)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/medialive-2017-10-14/BatchStop)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/medialive-2017-10-14/BatchStop)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/medialive-2017-10-14/BatchStop)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/medialive-2017-10-14/BatchStop)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/medialive-2017-10-14/BatchStop)
+ [AWS SDK for Python](/goto/boto3/medialive-2017-10-14/BatchStop)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/medialive-2017-10-14/BatchStop)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
