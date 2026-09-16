---
source_url: https://docs.aws.amazon.com/medialive/latest/apireference/inputsecuritygroups-inputsecuritygroupid.html
---

# Input security groups: group ID
<a name="inputsecuritygroups-inputsecuritygroupid"></a>

## URI
<a name="inputsecuritygroups-inputsecuritygroupid-url"></a>

`/prod/inputSecurityGroups/{{inputSecurityGroupId}}`

## HTTP methods
<a name="inputsecuritygroups-inputsecuritygroupid-http-methods"></a>

### DELETE
<a name="inputsecuritygroups-inputsecuritygroupiddelete"></a>

**Operation ID:** `DeleteInputSecurityGroup`

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{inputSecurityGroupId}} | String | True |  |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | Empty | 200 response |
| 400 | InvalidRequest | 400 response |
| 403 | AccessDenied | 403 response |
| 404 | ResourceNotFound | 404 response |
| 429 | LimitExceeded | 429 response |
| 500 | InternalServiceError | 500 response |
| 502 | BadGatewayException | 502 response |
| 504 | GatewayTimeoutException | 504 response |

### GET
<a name="inputsecuritygroups-inputsecuritygroupidget"></a>

**Operation ID:** `DescribeInputSecurityGroup`

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{inputSecurityGroupId}} | String | True |  |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | InputSecurityGroup | 200 response |
| 400 | InvalidRequest | 400 response |
| 403 | AccessDenied | 403 response |
| 404 | ResourceNotFound | 404 response |
| 429 | LimitExceeded | 429 response |
| 500 | InternalServiceError | 500 response |
| 502 | BadGatewayException | 502 response |
| 504 | GatewayTimeoutException | 504 response |

### PUT
<a name="inputsecuritygroups-inputsecuritygroupidput"></a>

**Operation ID:** `UpdateInputSecurityGroup`

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{inputSecurityGroupId}} | String | True |  |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | UpdateInputSecurityGroupResultModel | 200 response |
| 400 | InvalidRequest | 400 response |
| 403 | AccessDenied | 403 response |
| 404 | ResourceNotFound | 404 response |
| 409 | ResourceConflict | 409 response |
| 500 | InternalServiceError | 500 response |
| 502 | BadGatewayException | 502 response |
| 504 | GatewayTimeoutException | 504 response |

## Schemas
<a name="inputsecuritygroups-inputsecuritygroupid-schemas"></a>

### Request bodies
<a name="inputsecuritygroups-inputsecuritygroupid-request-examples"></a>

#### PUT schema
<a name="inputsecuritygroups-inputsecuritygroupid-request-body-put-example"></a>

```
{
  "tags": {
  },
  "whitelistRules": [
    {
      "cidr": "string"
    }
  ]
}
```

### Response bodies
<a name="inputsecuritygroups-inputsecuritygroupid-response-examples"></a>

#### Empty schema
<a name="inputsecuritygroups-inputsecuritygroupid-response-body-empty-example"></a>

```
{
}
```

#### InputSecurityGroup schema
<a name="inputsecuritygroups-inputsecuritygroupid-response-body-inputsecuritygroup-example"></a>

```
{
  "arn": "string",
  "id": "string",
  "inputs": [
    "string"
  ],
  "state": enum,
  "tags": {
  },
  "whitelistRules": [
    {
      "cidr": "string"
    }
  ]
}
```

#### UpdateInputSecurityGroupResultModel schema
<a name="inputsecuritygroups-inputsecuritygroupid-response-body-updateinputsecuritygroupresultmodel-example"></a>

```
{
  "securityGroup": {
    "arn": "string",
    "id": "string",
    "inputs": [
      "string"
    ],
    "state": enum,
    "tags": {
    },
    "whitelistRules": [
      {
        "cidr": "string"
      }
    ]
  }
}
```

#### InvalidRequest schema
<a name="inputsecuritygroups-inputsecuritygroupid-response-body-invalidrequest-example"></a>

```
{
  "message": "string"
}
```

#### AccessDenied schema
<a name="inputsecuritygroups-inputsecuritygroupid-response-body-accessdenied-example"></a>

```
{
  "message": "string"
}
```

#### ResourceNotFound schema
<a name="inputsecuritygroups-inputsecuritygroupid-response-body-resourcenotfound-example"></a>

```
{
  "message": "string"
}
```

#### ResourceConflict schema
<a name="inputsecuritygroups-inputsecuritygroupid-response-body-resourceconflict-example"></a>

```
{
  "message": "string"
}
```

#### LimitExceeded schema
<a name="inputsecuritygroups-inputsecuritygroupid-response-body-limitexceeded-example"></a>

```
{
  "message": "string"
}
```

#### InternalServiceError schema
<a name="inputsecuritygroups-inputsecuritygroupid-response-body-internalserviceerror-example"></a>

```
{
  "message": "string"
}
```

#### BadGatewayException schema
<a name="inputsecuritygroups-inputsecuritygroupid-response-body-badgatewayexception-example"></a>

```
{
  "message": "string"
}
```

#### GatewayTimeoutException schema
<a name="inputsecuritygroups-inputsecuritygroupid-response-body-gatewaytimeoutexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="inputsecuritygroups-inputsecuritygroupid-properties"></a>

### AccessDenied
<a name="inputsecuritygroups-inputsecuritygroupid-model-accessdenied"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### BadGatewayException
<a name="inputsecuritygroups-inputsecuritygroupid-model-badgatewayexception"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### Empty
<a name="inputsecuritygroups-inputsecuritygroupid-model-empty"></a>

### GatewayTimeoutException
<a name="inputsecuritygroups-inputsecuritygroupid-model-gatewaytimeoutexception"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### InputSecurityGroup
<a name="inputsecuritygroups-inputsecuritygroupid-model-inputsecuritygroup"></a>

An Input Security Group

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| arn | string | False | Unique ARN of Input Security Group |
| id | string | False | The Id of the Input Security Group |
| inputs | Array of type string | False | The list of inputs currently using this Input Security Group. |
| state | [InputSecurityGroupState](#inputsecuritygroups-inputsecuritygroupid-model-inputsecuritygroupstate) | False | The current state of the Input Security Group. |
| tags | [Tags](#inputsecuritygroups-inputsecuritygroupid-model-tags) | False | A collection of key-value pairs. |
| whitelistRules | Array of type [InputWhitelistRule](#inputsecuritygroups-inputsecuritygroupid-model-inputwhitelistrule) | False | Whitelist rules and their sync status |

### InputSecurityGroupState
<a name="inputsecuritygroups-inputsecuritygroupid-model-inputsecuritygroupstate"></a>
+ `IDLE`
+ `IN_USE`
+ `UPDATING`
+ `DELETED`

### InputSecurityGroupWhitelistRequest
<a name="inputsecuritygroups-inputsecuritygroupid-model-inputsecuritygroupwhitelistrequest"></a>

Request of IPv4 CIDR addresses to whitelist in a security group.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| tags | [Tags](#inputsecuritygroups-inputsecuritygroupid-model-tags) | False | A collection of key-value pairs. |
| whitelistRules | Array of type [InputWhitelistRuleCidr](#inputsecuritygroups-inputsecuritygroupid-model-inputwhitelistrulecidr) | False | List of IPv4 CIDR addresses to whitelist |

### InputWhitelistRule
<a name="inputsecuritygroups-inputsecuritygroupid-model-inputwhitelistrule"></a>

Whitelist rule

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| cidr | string | False | The IPv4 CIDR that's whitelisted. |

### InputWhitelistRuleCidr
<a name="inputsecuritygroups-inputsecuritygroupid-model-inputwhitelistrulecidr"></a>

An IPv4 CIDR to whitelist.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| cidr | string | False | The IPv4 CIDR to whitelist. |

### InternalServiceError
<a name="inputsecuritygroups-inputsecuritygroupid-model-internalserviceerror"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### InvalidRequest
<a name="inputsecuritygroups-inputsecuritygroupid-model-invalidrequest"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### LimitExceeded
<a name="inputsecuritygroups-inputsecuritygroupid-model-limitexceeded"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### ResourceConflict
<a name="inputsecuritygroups-inputsecuritygroupid-model-resourceconflict"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### ResourceNotFound
<a name="inputsecuritygroups-inputsecuritygroupid-model-resourcenotfound"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### Tags
<a name="inputsecuritygroups-inputsecuritygroupid-model-tags"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| `*` | string | False |  |

### UpdateInputSecurityGroupResultModel
<a name="inputsecuritygroups-inputsecuritygroupid-model-updateinputsecuritygroupresultmodel"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| securityGroup | [InputSecurityGroup](#inputsecuritygroups-inputsecuritygroupid-model-inputsecuritygroup) | False |  |

## See also
<a name="inputsecuritygroups-inputsecuritygroupid-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### DeleteInputSecurityGroup
<a name="DeleteInputSecurityGroup-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/medialive-2017-10-14/DeleteInputSecurityGroup)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/medialive-2017-10-14/DeleteInputSecurityGroup)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/medialive-2017-10-14/DeleteInputSecurityGroup)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/medialive-2017-10-14/DeleteInputSecurityGroup)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/medialive-2017-10-14/DeleteInputSecurityGroup)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/medialive-2017-10-14/DeleteInputSecurityGroup)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/medialive-2017-10-14/DeleteInputSecurityGroup)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/medialive-2017-10-14/DeleteInputSecurityGroup)
+ [AWS SDK for Python (Boto3)](/goto/boto3/medialive-2017-10-14/DeleteInputSecurityGroup)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/medialive-2017-10-14/DeleteInputSecurityGroup)

### DescribeInputSecurityGroup
<a name="DescribeInputSecurityGroup-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/medialive-2017-10-14/DescribeInputSecurityGroup)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/medialive-2017-10-14/DescribeInputSecurityGroup)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/medialive-2017-10-14/DescribeInputSecurityGroup)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/medialive-2017-10-14/DescribeInputSecurityGroup)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/medialive-2017-10-14/DescribeInputSecurityGroup)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/medialive-2017-10-14/DescribeInputSecurityGroup)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/medialive-2017-10-14/DescribeInputSecurityGroup)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/medialive-2017-10-14/DescribeInputSecurityGroup)
+ [AWS SDK for Python (Boto3)](/goto/boto3/medialive-2017-10-14/DescribeInputSecurityGroup)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/medialive-2017-10-14/DescribeInputSecurityGroup)

### UpdateInputSecurityGroup
<a name="UpdateInputSecurityGroup-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/medialive-2017-10-14/UpdateInputSecurityGroup)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/medialive-2017-10-14/UpdateInputSecurityGroup)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/medialive-2017-10-14/UpdateInputSecurityGroup)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/medialive-2017-10-14/UpdateInputSecurityGroup)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/medialive-2017-10-14/UpdateInputSecurityGroup)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/medialive-2017-10-14/UpdateInputSecurityGroup)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/medialive-2017-10-14/UpdateInputSecurityGroup)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/medialive-2017-10-14/UpdateInputSecurityGroup)
+ [AWS SDK for Python (Boto3)](/goto/boto3/medialive-2017-10-14/UpdateInputSecurityGroup)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/medialive-2017-10-14/UpdateInputSecurityGroup)
