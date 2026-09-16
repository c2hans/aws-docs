---
source_url: https://docs.aws.amazon.com/apigatewayv2/latest/api-reference/domainnames-domainname-routingrules-routingruleid.html
---

# RoutingRule
<a name="domainnames-domainname-routingrules-routingruleid"></a>

Represents a routing rule. When the incoming request to a domain name matches the conditions for a rule, API Gateway invokes a stage of a target API. Supported only for REST APIs.

## URI
<a name="domainnames-domainname-routingrules-routingruleid-url"></a>

`/v2/domainnames/{{domainName}}/routingrules/{{routingRuleId}}`

## HTTP methods
<a name="domainnames-domainname-routingrules-routingruleid-http-methods"></a>

### GET
<a name="domainnames-domainname-routingrules-routingruleidget"></a>

**Operation ID:** `GetRoutingRule`

Gets a routing rule.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{routingRuleId}} | String | True | The routing rule identifier. |
| {{domainName}} | String | True | The domain name. |

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| domainNameId | String | False | The identifier of the domain name. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | RoutingRule | Success |
| 400 | BadRequestException | One of the parameters in the request is invalid. |
| 404 | NotFoundException | The resource specified in the request was not found. |
| 429 | LimitExceededException | The client is sending more than the allowed number of requests per unit of time. |

### PUT
<a name="domainnames-domainname-routingrules-routingruleidput"></a>

**Operation ID:** `PutRoutingRule`

 Replaces an existing routing rule. When you replace an existing routing rule, the `RoutingRuleId` isn't changed.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{routingRuleId}} | String | True | The routing rule identifier. |
| {{domainName}} | String | True | The domain name. |

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| domainNameId | String | False | The identifier of the domain name. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | RoutingRule | Success |
| 400 | BadRequestException | One of the parameters in the request is invalid. |
| 404 | NotFoundException | The resource specified in the request was not found. |
| 409 | ConflictException | The resource already exists. |
| 429 | LimitExceededException | The client is sending more than the allowed number of requests per unit of time. |

### DELETE
<a name="domainnames-domainname-routingrules-routingruleiddelete"></a>

**Operation ID:** `DeleteRoutingRule`

Deletes a routing rule.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{routingRuleId}} | String | True | The routing rule identifier. |
| {{domainName}} | String | True | The domain name. |

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| domainNameId | String | False | The identifier of the domain name. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 204 | None | The request has succeeded, and there is no additional content to send in the response payload body. |
| 400 | BadRequestException | One of the parameters in the request is invalid. |
| 404 | NotFoundException | The resource specified in the request was not found. |
| 429 | LimitExceededException | The client is sending more than the allowed number of requests per unit of time. |

## Schemas
<a name="domainnames-domainname-routingrules-routingruleid-schemas"></a>

### Request bodies
<a name="domainnames-domainname-routingrules-routingruleid-request-examples"></a>

#### PUT schema
<a name="domainnames-domainname-routingrules-routingruleid-request-body-put-example"></a>

```
{
  "conditions": [
    {
      "matchHeaders": {
        "anyOf": [
          {
            "header": "string",
            "valueGlob": "string"
          }
        ]
      },
      "matchBasePaths": {
        "anyOf": [
          "string"
        ]
      }
    }
  ],
  "actions": [
    {
      "invokeApi": {
        "apiId": "string",
        "stage": "string",
        "stripBasePath": boolean
      }
    }
  ],
  "priority": integer
}
```

### Response bodies
<a name="domainnames-domainname-routingrules-routingruleid-response-examples"></a>

#### RoutingRule schema
<a name="domainnames-domainname-routingrules-routingruleid-response-body-routingrule-example"></a>

```
{
  "routingRuleId": "string",
  "routingRuleArn": "string",
  "actions": [
    {
      "invokeApi": {
        "apiId": "string",
        "stage": "string",
        "stripBasePath": boolean
      }
    }
  ],
  "conditions": [
    {
      "matchHeaders": {
        "anyOf": [
          {
            "header": "string",
            "valueGlob": "string"
          }
        ]
      },
      "matchBasePaths": {
        "anyOf": [
          "string"
        ]
      }
    }
  ],
  "priority": integer
}
```

#### BadRequestException schema
<a name="domainnames-domainname-routingrules-routingruleid-response-body-badrequestexception-example"></a>

```
{
  "message": "string"
}
```

#### NotFoundException schema
<a name="domainnames-domainname-routingrules-routingruleid-response-body-notfoundexception-example"></a>

```
{
  "message": "string",
  "resourceType": "string"
}
```

#### ConflictException schema
<a name="domainnames-domainname-routingrules-routingruleid-response-body-conflictexception-example"></a>

```
{
  "message": "string"
}
```

#### LimitExceededException schema
<a name="domainnames-domainname-routingrules-routingruleid-response-body-limitexceededexception-example"></a>

```
{
  "message": "string",
  "limitType": "string"
}
```

## Properties
<a name="domainnames-domainname-routingrules-routingruleid-properties"></a>

### BadRequestException
<a name="domainnames-domainname-routingrules-routingruleid-model-badrequestexception"></a>

The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Describes the error encountered. |

### ConflictException
<a name="domainnames-domainname-routingrules-routingruleid-model-conflictexception"></a>

The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Describes the error encountered. |

### LimitExceededException
<a name="domainnames-domainname-routingrules-routingruleid-model-limitexceededexception"></a>

A limit has been exceeded. See the accompanying error message for details.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| limitType | string | False | The limit type. |
| message | string | False | Describes the error encountered. |

### NotFoundException
<a name="domainnames-domainname-routingrules-routingruleid-model-notfoundexception"></a>

The resource specified in the request was not found. See the `message` field for more information.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Describes the error encountered. |
| resourceType | string | False | The resource type. |

### RoutingRule
<a name="domainnames-domainname-routingrules-routingruleid-model-routingrule"></a>

Represents a routing rule.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| actions | Array of type [RoutingRuleAction](#domainnames-domainname-routingrules-routingruleid-model-routingruleaction) | False | The resulting action based on matching a routing rules condition. Only `InvokeApi` is supported. |
| conditions | Array of type [RoutingRuleCondition](#domainnames-domainname-routingrules-routingruleid-model-routingrulecondition) | False | The conditions of the routing rule. |
| priority | integer | False | The order in which API Gateway evaluates a rule. Priority is evaluated from the lowest value to the highest value. Rules can't have the same priority. Priority values 1-1,000,000 are supported. |
| routingRuleArn | string | False | The ARN of the routing rule. |
| routingRuleId | string | True | The ID of the routing rule. |

### RoutingRuleAction
<a name="domainnames-domainname-routingrules-routingruleid-model-routingruleaction"></a>

Represents a routing rule action. The only supported action is `invokeApi`.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| invokeApi | [RoutingRuleActionInvokeApi](#domainnames-domainname-routingrules-routingruleid-model-routingruleactioninvokeapi) | True | Action to invoke a stage of a target API. Only REST APIs are supported. |

### RoutingRuleActionInvokeApi
<a name="domainnames-domainname-routingrules-routingruleid-model-routingruleactioninvokeapi"></a>

Represents an `InvokeApi` action.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| apiId | string | True | The API identifier of the target API. |
| stage | string | True | The name of the target stage. |
| stripBasePath | boolean | False | The strip base path setting. When true, API Gateway strips the incoming matched base path when forwarding the request to the target API. |

### RoutingRuleCondition
<a name="domainnames-domainname-routingrules-routingruleid-model-routingrulecondition"></a>

Represents a condition. Conditions can contain up to two `matchHeaders` conditions and one `matchBasePaths` conditions. API Gateway evaluates header conditions and base path conditions together. You can only use `AND` between header and base path conditions.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| matchBasePaths | [RoutingRuleMatchBasePaths](#domainnames-domainname-routingrules-routingruleid-model-routingrulematchbasepaths) | False | The base path to be matched.  |
| matchHeaders | [RoutingRuleMatchHeaders](#domainnames-domainname-routingrules-routingruleid-model-routingrulematchheaders) | False | The headers to be matched.  |

### RoutingRuleInput
<a name="domainnames-domainname-routingrules-routingruleid-model-routingruleinput"></a>

Represents the input parameters for an `RoutingRule` request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| actions | Array of type [RoutingRuleAction](#domainnames-domainname-routingrules-routingruleid-model-routingruleaction) | True | The resulting action based on matching a routing rules condition. Only `InvokeApi` is supported. |
| conditions | Array of type [RoutingRuleCondition](#domainnames-domainname-routingrules-routingruleid-model-routingrulecondition) | True | The conditions of the routing rule. |
| priority | integer | True | The order in which API Gateway evaluates a rule. Priority is evaluated from the lowest value to the highest value. Rules can't have the same priority. Priority values 1-1,000,000 are supported. |

### RoutingRuleMatchBasePaths
<a name="domainnames-domainname-routingrules-routingruleid-model-routingrulematchbasepaths"></a>

Represents a `MatchBasePaths` condition.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| anyOf | Array of type string | True | The string of the case sensitive base path to be matched.  |

### RoutingRuleMatchHeaderValue
<a name="domainnames-domainname-routingrules-routingruleid-model-routingrulematchheadervalue"></a>

Represents a `MatchHeaderValue`.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| header | string | True | The case insensitive header name to be matched. The header name must be less than 40 characters and the only allowed characters are `a-z`, `A-Z`, `0-9`, and the following special characters: `*?-!#$%&'.^_`\|~`. |
| valueGlob | string | True | The case sensitive header glob value to be matched against entire header value. The header glob value must be less than 128 characters and the only allowed characters are `a-z`, `A-Z`, `0-9`, and the following special characters: `*?-!#$%&'.^_`\|~`. Wildcard matching is supported for header glob values but must be for `*prefix-match`, `suffix-match*`, or `*infix*-match`. |

### RoutingRuleMatchHeaders
<a name="domainnames-domainname-routingrules-routingruleid-model-routingrulematchheaders"></a>

Represents a `MatchHeaders` condition.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| anyOf | Array of type [RoutingRuleMatchHeaderValue](#domainnames-domainname-routingrules-routingruleid-model-routingrulematchheadervalue) | True | The header name and header value glob to be matched. The matchHeaders condition is matched if any of the header name and header value globs are matched. |

## See also
<a name="domainnames-domainname-routingrules-routingruleid-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### GetRoutingRule
<a name="GetRoutingRule-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/apigatewayv2-2018-11-29/GetRoutingRule)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/apigatewayv2-2018-11-29/GetRoutingRule)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/apigatewayv2-2018-11-29/GetRoutingRule)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/apigatewayv2-2018-11-29/GetRoutingRule)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/apigatewayv2-2018-11-29/GetRoutingRule)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/apigatewayv2-2018-11-29/GetRoutingRule)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/apigatewayv2-2018-11-29/GetRoutingRule)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/apigatewayv2-2018-11-29/GetRoutingRule)
+ [AWS SDK for Python (Boto3)](/goto/boto3/apigatewayv2-2018-11-29/GetRoutingRule)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/apigatewayv2-2018-11-29/GetRoutingRule)

### PutRoutingRule
<a name="PutRoutingRule-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/apigatewayv2-2018-11-29/PutRoutingRule)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/apigatewayv2-2018-11-29/PutRoutingRule)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/apigatewayv2-2018-11-29/PutRoutingRule)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/apigatewayv2-2018-11-29/PutRoutingRule)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/apigatewayv2-2018-11-29/PutRoutingRule)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/apigatewayv2-2018-11-29/PutRoutingRule)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/apigatewayv2-2018-11-29/PutRoutingRule)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/apigatewayv2-2018-11-29/PutRoutingRule)
+ [AWS SDK for Python (Boto3)](/goto/boto3/apigatewayv2-2018-11-29/PutRoutingRule)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/apigatewayv2-2018-11-29/PutRoutingRule)

### DeleteRoutingRule
<a name="DeleteRoutingRule-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/apigatewayv2-2018-11-29/DeleteRoutingRule)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/apigatewayv2-2018-11-29/DeleteRoutingRule)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/apigatewayv2-2018-11-29/DeleteRoutingRule)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/apigatewayv2-2018-11-29/DeleteRoutingRule)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/apigatewayv2-2018-11-29/DeleteRoutingRule)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/apigatewayv2-2018-11-29/DeleteRoutingRule)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/apigatewayv2-2018-11-29/DeleteRoutingRule)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/apigatewayv2-2018-11-29/DeleteRoutingRule)
+ [AWS SDK for Python (Boto3)](/goto/boto3/apigatewayv2-2018-11-29/DeleteRoutingRule)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/apigatewayv2-2018-11-29/DeleteRoutingRule)
