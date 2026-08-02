---
source_url: https://docs.aws.amazon.com/apigatewayv2/latest/api-reference/apis-apiid-models-modelid.html
---

# Model
<a name="apis-apiid-models-modelid"></a>

Represents a data model for an API. Supported only for WebSocket APIs. See [Create Models and Mapping Templates for Request and Response Mappings](https://docs.aws.amazon.com/apigateway/latest/developerguide/models-mappings.html).

## URI
<a name="apis-apiid-models-modelid-url"></a>

`/v2/apis/{{apiId}}/models/{{modelId}}`

## HTTP methods
<a name="apis-apiid-models-modelid-http-methods"></a>

### GET
<a name="apis-apiid-models-modelidget"></a>

**Operation ID:** `GetModel`

Gets a `Model`.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{modelId}} | String | True | The model ID. |
| {{apiId}} | String | True | The API identifier. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | Model | Success |
| 404 | NotFoundException | The resource specified in the request was not found. |
| 429 | LimitExceededException | The client is sending more than the allowed number of requests per unit of time. |

### DELETE
<a name="apis-apiid-models-modeliddelete"></a>

**Operation ID:** `DeleteModel`

Deletes a `Model`.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{modelId}} | String | True | The model ID. |
| {{apiId}} | String | True | The API identifier. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 204 | None | The request has succeeded, and there is no additional content to send in the response payload body. |
| 404 | NotFoundException | The resource specified in the request was not found. |
| 429 | LimitExceededException | The client is sending more than the allowed number of requests per unit of time. |

### PATCH
<a name="apis-apiid-models-modelidpatch"></a>

**Operation ID:** `UpdateModel`

Updates a `Model`.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{modelId}} | String | True | The model ID. |
| {{apiId}} | String | True | The API identifier. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | Model | Success |
| 400 | BadRequestException | One of the parameters in the request is invalid. |
| 404 | NotFoundException | The resource specified in the request was not found. |
| 409 | ConflictException | The resource already exists. |
| 429 | LimitExceededException | The client is sending more than the allowed number of requests per unit of time. |

## Schemas
<a name="apis-apiid-models-modelid-schemas"></a>

### Request bodies
<a name="apis-apiid-models-modelid-request-examples"></a>

#### PATCH schema
<a name="apis-apiid-models-modelid-request-body-patch-example"></a>

```
{
  "name": "string",
  "description": "string",
  "schema": "string",
  "contentType": "string"
}
```

### Response bodies
<a name="apis-apiid-models-modelid-response-examples"></a>

#### Model schema
<a name="apis-apiid-models-modelid-response-body-model-example"></a>

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
<a name="apis-apiid-models-modelid-response-body-badrequestexception-example"></a>

```
{
  "message": "string"
}
```

#### NotFoundException schema
<a name="apis-apiid-models-modelid-response-body-notfoundexception-example"></a>

```
{
  "message": "string",
  "resourceType": "string"
}
```

#### ConflictException schema
<a name="apis-apiid-models-modelid-response-body-conflictexception-example"></a>

```
{
  "message": "string"
}
```

#### LimitExceededException schema
<a name="apis-apiid-models-modelid-response-body-limitexceededexception-example"></a>

```
{
  "message": "string",
  "limitType": "string"
}
```

## Properties
<a name="apis-apiid-models-modelid-properties"></a>

### BadRequestException
<a name="apis-apiid-models-modelid-model-badrequestexception"></a>

The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Describes the error encountered. |

### ConflictException
<a name="apis-apiid-models-modelid-model-conflictexception"></a>

The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Describes the error encountered. |

### LimitExceededException
<a name="apis-apiid-models-modelid-model-limitexceededexception"></a>

A limit has been exceeded. See the accompanying error message for details.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| limitType | string | False | The limit type. |
| message | string | False | Describes the error encountered. |

### Model
<a name="apis-apiid-models-modelid-model-model"></a>

Represents a data model for an API. Supported only for WebSocket APIs. See [Create Models and Mapping Templates for Request and Response Mappings](https://docs.aws.amazon.com/apigateway/latest/developerguide/models-mappings.html).

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| contentType | string | False | The content-type for the model, for example, "application/json". |
| description | string | False | The description of the model. |
| modelId | string | False | The model identifier. |
| name | string | True | The name of the model. Must be alphanumeric. |
| schema | string | False | The schema for the model. For application/json models, this should be JSON schema draft 4 model. |

### NotFoundException
<a name="apis-apiid-models-modelid-model-notfoundexception"></a>

The resource specified in the request was not found. See the `message` field for more information.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Describes the error encountered. |
| resourceType | string | False | The resource type. |

### UpdateModelInput
<a name="apis-apiid-models-modelid-model-updatemodelinput"></a>

Represents the input parameters for an `UpdateModel` request. Supported only for WebSocket APIs.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| contentType | string | False | The content-type for the model, for example, "application/json". |
| description | string | False | The description of the model. |
| name | string | False | The name of the model. |
| schema | string | False | The schema for the model. For application/json models, this should be JSON schema draft 4 model. |

## See also
<a name="apis-apiid-models-modelid-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### GetModel
<a name="GetModel-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/apigatewayv2-2018-11-29/GetModel)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/apigatewayv2-2018-11-29/GetModel)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/apigatewayv2-2018-11-29/GetModel)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/apigatewayv2-2018-11-29/GetModel)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/apigatewayv2-2018-11-29/GetModel)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/apigatewayv2-2018-11-29/GetModel)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/apigatewayv2-2018-11-29/GetModel)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/apigatewayv2-2018-11-29/GetModel)
+ [AWS SDK for Python](/goto/boto3/apigatewayv2-2018-11-29/GetModel)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/apigatewayv2-2018-11-29/GetModel)

### DeleteModel
<a name="DeleteModel-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/apigatewayv2-2018-11-29/DeleteModel)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/apigatewayv2-2018-11-29/DeleteModel)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/apigatewayv2-2018-11-29/DeleteModel)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/apigatewayv2-2018-11-29/DeleteModel)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/apigatewayv2-2018-11-29/DeleteModel)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/apigatewayv2-2018-11-29/DeleteModel)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/apigatewayv2-2018-11-29/DeleteModel)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/apigatewayv2-2018-11-29/DeleteModel)
+ [AWS SDK for Python](/goto/boto3/apigatewayv2-2018-11-29/DeleteModel)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/apigatewayv2-2018-11-29/DeleteModel)

### UpdateModel
<a name="UpdateModel-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/apigatewayv2-2018-11-29/UpdateModel)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/apigatewayv2-2018-11-29/UpdateModel)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/apigatewayv2-2018-11-29/UpdateModel)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/apigatewayv2-2018-11-29/UpdateModel)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/apigatewayv2-2018-11-29/UpdateModel)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/apigatewayv2-2018-11-29/UpdateModel)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/apigatewayv2-2018-11-29/UpdateModel)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/apigatewayv2-2018-11-29/UpdateModel)
+ [AWS SDK for Python](/goto/boto3/apigatewayv2-2018-11-29/UpdateModel)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/apigatewayv2-2018-11-29/UpdateModel)
