---
source_url: https://docs.aws.amazon.com/medialive/latest/apireference/inputdevicetransfers.html
---

# Input devices: input device transfers
<a name="inputdevicetransfers"></a>

## URI
<a name="inputdevicetransfers-url"></a>

`/prod/inputDeviceTransfers`

## HTTP methods
<a name="inputdevicetransfers-http-methods"></a>

### GET
<a name="inputdevicetransfersget"></a>

**Operation ID:** `ListInputDeviceTransfers`

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| transferType | String | True |  |
| nextToken | String | False |  |
| maxResults | String | False |  |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | ListInputDeviceTransfersResultModel | 200 response |
| 400 | InvalidRequest | 400 response |
| 403 | AccessDenied | 403 response |
| 422 | ValidationError | 422 response |
| 429 | LimitExceeded | 429 response |
| 500 | InternalServiceError | 500 response |
| 502 | BadGatewayException | 502 response |
| 504 | GatewayTimeoutException | 504 response |

## Schemas
<a name="inputdevicetransfers-schemas"></a>

### Response bodies
<a name="inputdevicetransfers-response-examples"></a>

#### ListInputDeviceTransfersResultModel schema
<a name="inputdevicetransfers-response-body-listinputdevicetransfersresultmodel-example"></a>

```
{
  "inputDeviceTransfers": [
    {
      "id": "string",
      "message": "string",
      "targetCustomerId": "string",
      "transferType": enum
    }
  ],
  "nextToken": "string"
}
```

#### InvalidRequest schema
<a name="inputdevicetransfers-response-body-invalidrequest-example"></a>

```
{
  "message": "string"
}
```

#### AccessDenied schema
<a name="inputdevicetransfers-response-body-accessdenied-example"></a>

```
{
  "message": "string"
}
```

#### ValidationError schema
<a name="inputdevicetransfers-response-body-validationerror-example"></a>

```
{
  "elementPath": "string",
  "errorMessage": "string"
}
```

#### LimitExceeded schema
<a name="inputdevicetransfers-response-body-limitexceeded-example"></a>

```
{
  "message": "string"
}
```

#### InternalServiceError schema
<a name="inputdevicetransfers-response-body-internalserviceerror-example"></a>

```
{
  "message": "string"
}
```

#### BadGatewayException schema
<a name="inputdevicetransfers-response-body-badgatewayexception-example"></a>

```
{
  "message": "string"
}
```

#### GatewayTimeoutException schema
<a name="inputdevicetransfers-response-body-gatewaytimeoutexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="inputdevicetransfers-properties"></a>

### AccessDenied
<a name="inputdevicetransfers-model-accessdenied"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### BadGatewayException
<a name="inputdevicetransfers-model-badgatewayexception"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### GatewayTimeoutException
<a name="inputdevicetransfers-model-gatewaytimeoutexception"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### InputDeviceTransferType
<a name="inputdevicetransfers-model-inputdevicetransfertype"></a>

The type of device transfer. INCOMING for an input device that is being transferred to you, OUTGOING for an input device that you are transferring to another AWS account.
+ `OUTGOING`
+ `INCOMING`

### InternalServiceError
<a name="inputdevicetransfers-model-internalserviceerror"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### InvalidRequest
<a name="inputdevicetransfers-model-invalidrequest"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### LimitExceeded
<a name="inputdevicetransfers-model-limitexceeded"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### ListInputDeviceTransfersResultModel
<a name="inputdevicetransfers-model-listinputdevicetransfersresultmodel"></a>

The list of input devices in the transferred state. The recipient hasn't yet accepted or rejected the transfer.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| inputDeviceTransfers | Array of type [TransferringInputDeviceSummary](#inputdevicetransfers-model-transferringinputdevicesummary) | False | The list of devices that you are transferring or are being transferred to you. |
| nextToken | string | False | A token to get additional list results. |

### TransferringInputDeviceSummary
<a name="inputdevicetransfers-model-transferringinputdevicesummary"></a>

Details about the input device that is being transferred.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| id | string | False | The unique ID of the input device. |
| message | string | False | The optional message that the sender has attached to the transfer. |
| targetCustomerId | string | False | The AWS account ID for the recipient of the input device transfer. |
| transferType | [InputDeviceTransferType](#inputdevicetransfers-model-inputdevicetransfertype) | False | The type (direction) of the input device transfer. |

### ValidationError
<a name="inputdevicetransfers-model-validationerror"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| elementPath | string | False | Path to the source of the error. |
| errorMessage | string | False | The error message. |

## See also
<a name="inputdevicetransfers-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### ListInputDeviceTransfers
<a name="ListInputDeviceTransfers-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/medialive-2017-10-14/ListInputDeviceTransfers)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/medialive-2017-10-14/ListInputDeviceTransfers)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/medialive-2017-10-14/ListInputDeviceTransfers)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/medialive-2017-10-14/ListInputDeviceTransfers)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/medialive-2017-10-14/ListInputDeviceTransfers)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/medialive-2017-10-14/ListInputDeviceTransfers)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/medialive-2017-10-14/ListInputDeviceTransfers)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/medialive-2017-10-14/ListInputDeviceTransfers)
+ [AWS SDK for Python](/goto/boto3/medialive-2017-10-14/ListInputDeviceTransfers)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/medialive-2017-10-14/ListInputDeviceTransfers)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
