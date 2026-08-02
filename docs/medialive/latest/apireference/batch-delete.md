---
source_url: https://docs.aws.amazon.com/medialive/latest/apireference/batch-delete.html
---

# Batch action: delete
<a name="batch-delete"></a>

## URI
<a name="batch-delete-url"></a>

`/prod/batch/delete`

## HTTP methods
<a name="batch-delete-http-methods"></a>

### POST
<a name="batch-deletepost"></a>

**Operation ID:** `BatchDelete`

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | BatchDeleteResultModel | 200 response |
| 400 | InvalidRequest | 400 response |
| 403 | AccessDenied | 403 response |
| 404 | ResourceNotFound | 404 response |
| 409 | ResourceConflict | 409 response |
| 429 | LimitExceeded | 429 response |
| 500 | InternalServiceError | 500 response |
| 502 | BadGatewayException | 502 response |
| 504 | GatewayTimeoutException | 504 response |

## Schemas
<a name="batch-delete-schemas"></a>

### Request bodies
<a name="batch-delete-request-examples"></a>

#### POST schema
<a name="batch-delete-request-body-post-example"></a>

```
{
  "channelIds": [
    "string"
  ],
  "inputIds": [
    "string"
  ],
  "inputSecurityGroupIds": [
    "string"
  ],
  "multiplexIds": [
    "string"
  ]
}
```

### Response bodies
<a name="batch-delete-response-examples"></a>

#### BatchDeleteResultModel schema
<a name="batch-delete-response-body-batchdeleteresultmodel-example"></a>

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
<a name="batch-delete-response-body-invalidrequest-example"></a>

```
{
  "message": "string"
}
```

#### AccessDenied schema
<a name="batch-delete-response-body-accessdenied-example"></a>

```
{
  "message": "string"
}
```

#### ResourceNotFound schema
<a name="batch-delete-response-body-resourcenotfound-example"></a>

```
{
  "message": "string"
}
```

#### ResourceConflict schema
<a name="batch-delete-response-body-resourceconflict-example"></a>

```
{
  "message": "string"
}
```

#### LimitExceeded schema
<a name="batch-delete-response-body-limitexceeded-example"></a>

```
{
  "message": "string"
}
```

#### InternalServiceError schema
<a name="batch-delete-response-body-internalserviceerror-example"></a>

```
{
  "message": "string"
}
```

#### BadGatewayException schema
<a name="batch-delete-response-body-badgatewayexception-example"></a>

```
{
  "message": "string"
}
```

#### GatewayTimeoutException schema
<a name="batch-delete-response-body-gatewaytimeoutexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="batch-delete-properties"></a>

### AccessDenied
<a name="batch-delete-model-accessdenied"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### BadGatewayException
<a name="batch-delete-model-badgatewayexception"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### BatchDelete
<a name="batch-delete-model-batchdelete"></a>

Batch delete resource request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| channelIds | Array of type string | False | List of channel IDs |
| inputIds | Array of type string | False | List of input IDs |
| inputSecurityGroupIds | Array of type string | False | List of input security group IDs |
| multiplexIds | Array of type string | False | List of multiplex IDs |

### BatchDeleteResultModel
<a name="batch-delete-model-batchdeleteresultmodel"></a>

Batch delete resource results

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| failed | Array of type [BatchFailedResultModel](#batch-delete-model-batchfailedresultmodel) | False | List of failed operations |
| successful | Array of type [BatchSuccessfulResultModel](#batch-delete-model-batchsuccessfulresultmodel) | False | List of successful operations |

### BatchFailedResultModel
<a name="batch-delete-model-batchfailedresultmodel"></a>

Details from a failed operation

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| arn | string | False | ARN of the resource |
| code | string | False | Error code for the failed operation |
| id | string | False | ID of the resource |
| message | string | False | Error message for the failed operation |

### BatchSuccessfulResultModel
<a name="batch-delete-model-batchsuccessfulresultmodel"></a>

Details from a successful operation

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| arn | string | False | ARN of the resource |
| id | string | False | ID of the resource |
| state | string | False | Current state of the resource |

### GatewayTimeoutException
<a name="batch-delete-model-gatewaytimeoutexception"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### InternalServiceError
<a name="batch-delete-model-internalserviceerror"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### InvalidRequest
<a name="batch-delete-model-invalidrequest"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### LimitExceeded
<a name="batch-delete-model-limitexceeded"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### ResourceConflict
<a name="batch-delete-model-resourceconflict"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### ResourceNotFound
<a name="batch-delete-model-resourcenotfound"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

## See also
<a name="batch-delete-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### BatchDelete
<a name="BatchDelete-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/medialive-2017-10-14/BatchDelete)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/medialive-2017-10-14/BatchDelete)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/medialive-2017-10-14/BatchDelete)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/medialive-2017-10-14/BatchDelete)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/medialive-2017-10-14/BatchDelete)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/medialive-2017-10-14/BatchDelete)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/medialive-2017-10-14/BatchDelete)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/medialive-2017-10-14/BatchDelete)
+ [AWS SDK for Python](/goto/boto3/medialive-2017-10-14/BatchDelete)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/medialive-2017-10-14/BatchDelete)
