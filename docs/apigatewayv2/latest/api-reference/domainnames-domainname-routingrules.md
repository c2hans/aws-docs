---
source_url: https://docs.aws.amazon.com/apigatewayv2/latest/api-reference/domainnames-domainname-routingrules.html
---

# RoutingRules
<a name="domainnames-domainname-routingrules"></a>

Represents a collection of routing rules.

## URI
<a name="domainnames-domainname-routingrules-url"></a>

`/v2/domainnames/{{domainName}}/routingrules`

## HTTP methods
<a name="domainnames-domainname-routingrules-http-methods"></a>

### GET
<a name="domainnames-domainname-routingrulesget"></a>

**Operation ID:** `ListRoutingRules`

Lists routing rules.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{domainName}} | String | True | The domain name. |

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| nextToken | String | False | The next page of elements from this collection. Not valid for the last element of the collection. |
| maxResults | String | False | The maximum number of elements to be returned for this resource. |
| domainNameId | String | False | The identifier of the domain name. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | RoutingRules | Success |
| 400 | BadRequestException | One of the parameters in the request is invalid. |
| 404 | NotFoundException | The resource specified in the request was not found. |
| 429 | LimitExceededException | The client is sending more than the allowed number of requests per unit of time. |

### POST
<a name="domainnames-domainname-routingrulespost"></a>

**Operation ID:** `CreateRoutingRule`

Create a routing rule.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{domainName}} | String | True | The domain name. |

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| domainNameId | String | False | The identifier of the domain name. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 201 | RoutingRule | The request has succeeded and has resulted in the creation of a resource. |
| 400 | BadRequestException | One of the parameters in the request is invalid. |
| 404 | NotFoundException | The resource specified in the request was not found. |
| 409 | ConflictException | The resource already exists. |
| 429 | LimitExceededException | The client is sending more than the allowed number of requests per unit of time. |

## Schemas
<a name="domainnames-domainname-routingrules-schemas"></a>

### Request bodies
<a name="domainnames-domainname-routingrules-request-examples"></a>

#### POST schema
<a name="domainnames-domainname-routingrules-request-body-post-example"></a>

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
<a name="domainnames-domainname-routingrules-response-examples"></a>

#### RoutingRules schema
<a name="domainnames-domainname-routingrules-response-body-routingrules-example"></a>

```
{
  "items": [
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
  ],
  "nextToken": "string"
}
```

#### RoutingRule schema
<a name="domainnames-domainname-routingrules-response-body-routingrule-example"></a>

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
<a name="domainnames-domainname-routingrules-response-body-badrequestexception-example"></a>

```
{
  "message": "string"
}
```

#### NotFoundException schema
<a name="domainnames-domainname-routingrules-response-body-notfoundexception-example"></a>

```
{
  "message": "string",
  "resourceType": "string"
}
```

#### ConflictException schema
<a name="domainnames-domainname-routingrules-response-body-conflictexception-example"></a>

```
{
  "message": "string"
}
```

#### LimitExceededException schema
<a name="domainnames-domainname-routingrules-response-body-limitexceededexception-example"></a>

```
{
  "message": "string",
  "limitType": "string"
}
```

## Properties
<a name="domainnames-domainname-routingrules-properties"></a>

### BadRequestException
<a name="domainnames-domainname-routingrules-model-badrequestexception"></a>

The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Describes the error encountered. |

### ConflictException
<a name="domainnames-domainname-routingrules-model-conflictexception"></a>

The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Describes the error encountered. |

### LimitExceededException
<a name="domainnames-domainname-routingrules-model-limitexceededexception"></a>

A limit has been exceeded. See the accompanying error message for details.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| limitType | string | False | The limit type. |
| message | string | False | Describes the error encountered. |

### NotFoundException
<a name="domainnames-domainname-routingrules-model-notfoundexception"></a>

The resource specified in the request was not found. See the `message` field for more information.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Describes the error encountered. |
| resourceType | string | False | The resource type. |

### RoutingRule
<a name="domainnames-domainname-routingrules-model-routingrule"></a>

Represents a routing rule.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| actions | Array of type [RoutingRuleAction](#domainnames-domainname-routingrules-model-routingruleaction) | False | The resulting action based on matching a routing rules condition. Only `InvokeApi` is supported. |
| conditions | Array of type [RoutingRuleCondition](#domainnames-domainname-routingrules-model-routingrulecondition) | False | The conditions of the routing rule. |
| priority | integer | False | The order in which API Gateway evaluates a rule. Priority is evaluated from the lowest value to the highest value. Rules can't have the same priority. Priority values 1-1,000,000 are supported. |
| routingRuleArn | string | False | The ARN of the routing rule. |
| routingRuleId | string | True | The ID of the routing rule. |

### RoutingRuleAction
<a name="domainnames-domainname-routingrules-model-routingruleaction"></a>

Represents a routing rule action. The only supported action is `invokeApi`.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| invokeApi | [RoutingRuleActionInvokeApi](#domainnames-domainname-routingrules-model-routingruleactioninvokeapi) | True | Action to invoke a stage of a target API. Only REST APIs are supported. |

### RoutingRuleActionInvokeApi
<a name="domainnames-domainname-routingrules-model-routingruleactioninvokeapi"></a>

Represents an `InvokeApi` action.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| apiId | string | True | The API identifier of the target API. |
| stage | string | True | The name of the target stage. |
| stripBasePath | boolean | False | The strip base path setting. When true, API Gateway strips the incoming matched base path when forwarding the request to the target API. |

### RoutingRuleCondition
<a name="domainnames-domainname-routingrules-model-routingrulecondition"></a>

Represents a condition. Conditions can contain up to two `matchHeaders` conditions and one `matchBasePaths` conditions. API Gateway evaluates header conditions and base path conditions together. You can only use `AND` between header and base path conditions.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| matchBasePaths | [RoutingRuleMatchBasePaths](#domainnames-domainname-routingrules-model-routingrulematchbasepaths) | False | The base path to be matched.  |
| matchHeaders | [RoutingRuleMatchHeaders](#domainnames-domainname-routingrules-model-routingrulematchheaders) | False | The headers to be matched.  |

### RoutingRuleInput
<a name="domainnames-domainname-routingrules-model-routingruleinput"></a>

Represents the input parameters for an `RoutingRule` request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| actions | Array of type [RoutingRuleAction](#domainnames-domainname-routingrules-model-routingruleaction) | True | The resulting action based on matching a routing rules condition. Only `InvokeApi` is supported. |
| conditions | Array of type [RoutingRuleCondition](#domainnames-domainname-routingrules-model-routingrulecondition) | True | The conditions of the routing rule. |
| priority | integer | True | The order in which API Gateway evaluates a rule. Priority is evaluated from the lowest value to the highest value. Rules can't have the same priority. Priority values 1-1,000,000 are supported. |

### RoutingRuleMatchBasePaths
<a name="domainnames-domainname-routingrules-model-routingrulematchbasepaths"></a>

Represents a `MatchBasePaths` condition.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| anyOf | Array of type string | True | The string of the case sensitive base path to be matched.  |

### RoutingRuleMatchHeaderValue
<a name="domainnames-domainname-routingrules-model-routingrulematchheadervalue"></a>

Represents a `MatchHeaderValue`.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| header | string | True | The case insensitive header name to be matched. The header name must be less than 40 characters and the only allowed characters are `a-z`, `A-Z`, `0-9`, and the following special characters: `*?-!#$%&'.^_`\|~`. |
| valueGlob | string | True | The case sensitive header glob value to be matched against entire header value. The header glob value must be less than 128 characters and the only allowed characters are `a-z`, `A-Z`, `0-9`, and the following special characters: `*?-!#$%&'.^_`\|~`. Wildcard matching is supported for header glob values but must be for `*prefix-match`, `suffix-match*`, or `*infix*-match`. |

### RoutingRuleMatchHeaders
<a name="domainnames-domainname-routingrules-model-routingrulematchheaders"></a>

Represents a `MatchHeaders` condition.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| anyOf | Array of type [RoutingRuleMatchHeaderValue](#domainnames-domainname-routingrules-model-routingrulematchheadervalue) | True | The header name and header value glob to be matched. The matchHeaders condition is matched if any of the header name and header value globs are matched. |

### RoutingRules
<a name="domainnames-domainname-routingrules-model-routingrules"></a>

Represents collection of routing rules.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| items | Array of type [RoutingRule](#domainnames-domainname-routingrules-model-routingrule) | False | The elements from this collection. |
| nextToken | string | False | The next page of elements from this collection. Not valid for the last element of the collection. |

## See also
<a name="domainnames-domainname-routingrules-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### ListRoutingRules
<a name="ListRoutingRules-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/apigatewayv2-2018-11-29/ListRoutingRules)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/apigatewayv2-2018-11-29/ListRoutingRules)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/apigatewayv2-2018-11-29/ListRoutingRules)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/apigatewayv2-2018-11-29/ListRoutingRules)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/apigatewayv2-2018-11-29/ListRoutingRules)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/apigatewayv2-2018-11-29/ListRoutingRules)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/apigatewayv2-2018-11-29/ListRoutingRules)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/apigatewayv2-2018-11-29/ListRoutingRules)
+ [AWS SDK for Python (Boto3)](/goto/boto3/apigatewayv2-2018-11-29/ListRoutingRules)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/apigatewayv2-2018-11-29/ListRoutingRules)

### CreateRoutingRule
<a name="CreateRoutingRule-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/apigatewayv2-2018-11-29/CreateRoutingRule)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/apigatewayv2-2018-11-29/CreateRoutingRule)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/apigatewayv2-2018-11-29/CreateRoutingRule)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/apigatewayv2-2018-11-29/CreateRoutingRule)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/apigatewayv2-2018-11-29/CreateRoutingRule)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/apigatewayv2-2018-11-29/CreateRoutingRule)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/apigatewayv2-2018-11-29/CreateRoutingRule)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/apigatewayv2-2018-11-29/CreateRoutingRule)
+ [AWS SDK for Python (Boto3)](/goto/boto3/apigatewayv2-2018-11-29/CreateRoutingRule)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/apigatewayv2-2018-11-29/CreateRoutingRule)
