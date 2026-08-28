---
source_url: https://docs.aws.amazon.com/apigatewayv2/latest/api-reference/apis-apiid-models.html
---

# Models
<a name="apis-apiid-models"></a>

Represents the collection of data models for an API. Supported only for WebSocket APIs. See [Create Models and Mapping Templates for Request and Response Mappings](https://docs.aws.amazon.com/apigateway/latest/developerguide/models-mappings.html).

## URI
<a name="apis-apiid-models-url"></a>

`/v2/apis/{{apiId}}/models`

## HTTP methods
<a name="apis-apiid-models-http-methods"></a>

### GET
<a name="apis-apiid-modelsget"></a>

**Operation ID:** `GetModels`

Gets the `Models` for an API.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{apiId}} | String | True | The API identifier. |

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| nextToken | String | False | The next page of elements from this collection. Not valid for the last element of the collection. |
| maxResults | String | False | The maximum number of elements to be returned for this resource. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | Models | Success |
| 400 | BadRequestException | One of the parameters in the request is invalid. |
| 404 | NotFoundException | The resource specified in the request was not found. |
| 429 | LimitExceededException | The client is sending more than the allowed number of requests per unit of time. |

### POST
<a name="apis-apiid-modelspost"></a>

**Operation ID:** `CreateModel`

Creates a `Model` for an API.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{apiId}} | String | True | The API identifier. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 201 | Model | The request has succeeded and has resulted in the creation of a resource. |
| 400 | BadRequestException | One of the parameters in the request is invalid. |
| 404 | NotFoundException | The resource specified in the request was not found. |
| 409 | ConflictException | The resource already exists. |
| 429 | LimitExceededException | The client is sending more than the allowed number of requests per unit of time. |

## Schemas
<a name="apis-apiid-models-schemas"></a>

### Request bodies
<a name="apis-apiid-models-request-examples"></a>

#### POST schema
<a name="apis-apiid-models-request-body-post-example"></a>

```
{
  "name": "string",
  "description": "string",
  "schema": "string",
  "contentType": "string"
}
```

### Response bodies
<a name="apis-apiid-models-response-examples"></a>

#### Models schema
<a name="apis-apiid-models-response-body-models-example"></a>

```
{
  "items": [
    {
      "modelId": "string",
      "name": "string",
      "description": "string",
      "schema": "string",
      "contentType": "string"
    }
  ],
  "nextToken": "string"
}
```

#### Model schema
<a name="apis-apiid-models-response-body-model-example"></a>

```
{
  "modelId": "string",
  "name": "string",
  "description": "string",
  "schema": "string",
  "contentType": "string"
}
```

#### BadRequestException schema
<a name="apis-apiid-models-response-body-badrequestexception-example"></a>

```
{
  "message": "string"
}
```

#### NotFoundException schema
<a name="apis-apiid-models-response-body-notfoundexception-example"></a>

```
{
  "message": "string",
  "resourceType": "string"
}
```

#### ConflictException schema
<a name="apis-apiid-models-response-body-conflictexception-example"></a>

```
{
  "message": "string"
}
```

#### LimitExceededException schema
<a name="apis-apiid-models-response-body-limitexceededexception-example"></a>

```
{
  "message": "string",
  "limitType": "string"
}
```

## Properties
<a name="apis-apiid-models-properties"></a>

### BadRequestException
<a name="apis-apiid-models-model-badrequestexception"></a>

The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Describes the error encountered. |

### ConflictException
<a name="apis-apiid-models-model-conflictexception"></a>

The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Describes the error encountered. |

### CreateModelInput
<a name="apis-apiid-models-model-createmodelinput"></a>

Represents the input parameters for a `CreateModel` request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| contentType | string | False | The content-type for the model, for example, "application/json". |
| description | string | False | The description of the model. |
| name | string | True | The name of the model. Must be alphanumeric. |
| schema | string | True | The schema for the model. For application/json models, this should be JSON schema draft 4 model. |

### LimitExceededException
<a name="apis-apiid-models-model-limitexceededexception"></a>

A limit has been exceeded. See the accompanying error message for details.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| limitType | string | False | The limit type. |
| message | string | False | Describes the error encountered. |

### Model
<a name="apis-apiid-models-model-model"></a>

Represents a data model for an API. Supported only for WebSocket APIs. See [Create Models and Mapping Templates for Request and Response Mappings](https://docs.aws.amazon.com/apigateway/latest/developerguide/models-mappings.html).

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| contentType | string | False | The content-type for the model, for example, "application/json". |
| description | string | False | The description of the model. |
| modelId | string | False | The model identifier. |
| name | string | True | The name of the model. Must be alphanumeric. |
| schema | string | False | The schema for the model. For application/json models, this should be JSON schema draft 4 model. |

### Models
<a name="apis-apiid-models-model-models"></a>

Represents a collection of data models. See [Create Models and Mapping Templates for Request and Response Mappings](https://docs.aws.amazon.com/apigateway/latest/developerguide/models-mappings.html).

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| items | Array of type [Model](#apis-apiid-models-model-model) | False | The elements from this collection. |
| nextToken | string | False | The next page of elements from this collection. Not valid for the last element of the collection. |

### NotFoundException
<a name="apis-apiid-models-model-notfoundexception"></a>

The resource specified in the request was not found. See the `message` field for more information.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Describes the error encountered. |
| resourceType | string | False | The resource type. |

## See also
<a name="apis-apiid-models-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### GetModels
<a name="GetModels-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/apigatewayv2-2018-11-29/GetModels)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/apigatewayv2-2018-11-29/GetModels)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/apigatewayv2-2018-11-29/GetModels)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/apigatewayv2-2018-11-29/GetModels)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/apigatewayv2-2018-11-29/GetModels)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/apigatewayv2-2018-11-29/GetModels)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/apigatewayv2-2018-11-29/GetModels)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/apigatewayv2-2018-11-29/GetModels)
+ [AWS SDK for Python](/goto/boto3/apigatewayv2-2018-11-29/GetModels)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/apigatewayv2-2018-11-29/GetModels)

### CreateModel
<a name="CreateModel-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/apigatewayv2-2018-11-29/CreateModel)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/apigatewayv2-2018-11-29/CreateModel)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/apigatewayv2-2018-11-29/CreateModel)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/apigatewayv2-2018-11-29/CreateModel)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/apigatewayv2-2018-11-29/CreateModel)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/apigatewayv2-2018-11-29/CreateModel)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/apigatewayv2-2018-11-29/CreateModel)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/apigatewayv2-2018-11-29/CreateModel)
+ [AWS SDK for Python](/goto/boto3/apigatewayv2-2018-11-29/CreateModel)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/apigatewayv2-2018-11-29/CreateModel)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon API Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apigatewayv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
