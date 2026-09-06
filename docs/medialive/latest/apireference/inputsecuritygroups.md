---
source_url: https://docs.aws.amazon.com/medialive/latest/apireference/inputsecuritygroups.html
---

# Input security groups
<a name="inputsecuritygroups"></a>

## URI
<a name="inputsecuritygroups-url"></a>

`/prod/inputSecurityGroups`

## HTTP methods
<a name="inputsecuritygroups-http-methods"></a>

### GET
<a name="inputsecuritygroupsget"></a>

**Operation ID:** `ListInputSecurityGroups`

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| nextToken | String | False |  |
| maxResults | String | False |  |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | ListInputSecurityGroupsResultModel | 200 response |
| 400 | InvalidRequest | 400 response |
| 403 | AccessDenied | 403 response |
| 429 | LimitExceeded | 429 response |
| 500 | InternalServiceError | 500 response |
| 502 | BadGatewayException | 502 response |
| 504 | GatewayTimeoutException | 504 response |

### POST
<a name="inputsecuritygroupspost"></a>

**Operation ID:** `CreateInputSecurityGroup`

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | CreateInputSecurityGroupResultModel | 200 response |
| 400 | InvalidRequest | 400 response |
| 403 | AccessDenied | 403 response |
| 429 | LimitExceeded | 429 response |
| 500 | InternalServiceError | 500 response |
| 502 | BadGatewayException | 502 response |
| 504 | GatewayTimeoutException | 504 response |

## Schemas
<a name="inputsecuritygroups-schemas"></a>

### Request bodies
<a name="inputsecuritygroups-request-examples"></a>

#### POST schema
<a name="inputsecuritygroups-request-body-post-example"></a>

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
<a name="inputsecuritygroups-response-examples"></a>

#### ListInputSecurityGroupsResultModel schema
<a name="inputsecuritygroups-response-body-listinputsecuritygroupsresultmodel-example"></a>

```
{
  "inputSecurityGroups": [
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
  ],
  "nextToken": "string"
}
```

#### CreateInputSecurityGroupResultModel schema
<a name="inputsecuritygroups-response-body-createinputsecuritygroupresultmodel-example"></a>

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
<a name="inputsecuritygroups-response-body-invalidrequest-example"></a>

```
{
  "message": "string"
}
```

#### AccessDenied schema
<a name="inputsecuritygroups-response-body-accessdenied-example"></a>

```
{
  "message": "string"
}
```

#### LimitExceeded schema
<a name="inputsecuritygroups-response-body-limitexceeded-example"></a>

```
{
  "message": "string"
}
```

#### InternalServiceError schema
<a name="inputsecuritygroups-response-body-internalserviceerror-example"></a>

```
{
  "message": "string"
}
```

#### BadGatewayException schema
<a name="inputsecuritygroups-response-body-badgatewayexception-example"></a>

```
{
  "message": "string"
}
```

#### GatewayTimeoutException schema
<a name="inputsecuritygroups-response-body-gatewaytimeoutexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="inputsecuritygroups-properties"></a>

### AccessDenied
<a name="inputsecuritygroups-model-accessdenied"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### BadGatewayException
<a name="inputsecuritygroups-model-badgatewayexception"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### CreateInputSecurityGroupResultModel
<a name="inputsecuritygroups-model-createinputsecuritygroupresultmodel"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| securityGroup | [InputSecurityGroup](#inputsecuritygroups-model-inputsecuritygroup) | False |  |

### GatewayTimeoutException
<a name="inputsecuritygroups-model-gatewaytimeoutexception"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### InputSecurityGroup
<a name="inputsecuritygroups-model-inputsecuritygroup"></a>

An Input Security Group

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| arn | string | False | Unique ARN of Input Security Group |
| id | string | False | The Id of the Input Security Group |
| inputs | Array of type string | False | The list of inputs currently using this Input Security Group. |
| state | [InputSecurityGroupState](#inputsecuritygroups-model-inputsecuritygroupstate) | False | The current state of the Input Security Group. |
| tags | [Tags](#inputsecuritygroups-model-tags) | False | A collection of key-value pairs. |
| whitelistRules | Array of type [InputWhitelistRule](#inputsecuritygroups-model-inputwhitelistrule) | False | Whitelist rules and their sync status |

### InputSecurityGroupState
<a name="inputsecuritygroups-model-inputsecuritygroupstate"></a>
+ `IDLE`
+ `IN_USE`
+ `UPDATING`
+ `DELETED`

### InputSecurityGroupWhitelistRequest
<a name="inputsecuritygroups-model-inputsecuritygroupwhitelistrequest"></a>

Request of IPv4 CIDR addresses to whitelist in a security group.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| tags | [Tags](#inputsecuritygroups-model-tags) | False | A collection of key-value pairs. |
| whitelistRules | Array of type [InputWhitelistRuleCidr](#inputsecuritygroups-model-inputwhitelistrulecidr) | False | List of IPv4 CIDR addresses to whitelist |

### InputWhitelistRule
<a name="inputsecuritygroups-model-inputwhitelistrule"></a>

Whitelist rule

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| cidr | string | False | The IPv4 CIDR that's whitelisted. |

### InputWhitelistRuleCidr
<a name="inputsecuritygroups-model-inputwhitelistrulecidr"></a>

An IPv4 CIDR to whitelist.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| cidr | string | False | The IPv4 CIDR to whitelist. |

### InternalServiceError
<a name="inputsecuritygroups-model-internalserviceerror"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### InvalidRequest
<a name="inputsecuritygroups-model-invalidrequest"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### LimitExceeded
<a name="inputsecuritygroups-model-limitexceeded"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### ListInputSecurityGroupsResultModel
<a name="inputsecuritygroups-model-listinputsecuritygroupsresultmodel"></a>

Result of input security group list request

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| inputSecurityGroups | Array of type [InputSecurityGroup](#inputsecuritygroups-model-inputsecuritygroup) | False | List of input security groups |
| nextToken | string | False |  |

### Tags
<a name="inputsecuritygroups-model-tags"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| `*` | string | False |  |

## See also
<a name="inputsecuritygroups-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### ListInputSecurityGroups
<a name="ListInputSecurityGroups-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/medialive-2017-10-14/ListInputSecurityGroups)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/medialive-2017-10-14/ListInputSecurityGroups)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/medialive-2017-10-14/ListInputSecurityGroups)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/medialive-2017-10-14/ListInputSecurityGroups)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/medialive-2017-10-14/ListInputSecurityGroups)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/medialive-2017-10-14/ListInputSecurityGroups)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/medialive-2017-10-14/ListInputSecurityGroups)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/medialive-2017-10-14/ListInputSecurityGroups)
+ [AWS SDK for Python](/goto/boto3/medialive-2017-10-14/ListInputSecurityGroups)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/medialive-2017-10-14/ListInputSecurityGroups)

### CreateInputSecurityGroup
<a name="CreateInputSecurityGroup-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/medialive-2017-10-14/CreateInputSecurityGroup)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/medialive-2017-10-14/CreateInputSecurityGroup)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/medialive-2017-10-14/CreateInputSecurityGroup)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/medialive-2017-10-14/CreateInputSecurityGroup)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/medialive-2017-10-14/CreateInputSecurityGroup)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/medialive-2017-10-14/CreateInputSecurityGroup)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/medialive-2017-10-14/CreateInputSecurityGroup)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/medialive-2017-10-14/CreateInputSecurityGroup)
+ [AWS SDK for Python](/goto/boto3/medialive-2017-10-14/CreateInputSecurityGroup)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/medialive-2017-10-14/CreateInputSecurityGroup)
