---
source_url: https://docs.aws.amazon.com/apigatewayv2/latest/api-reference/apis-apiid-stages-stagename.html
---

# Stage
<a name="apis-apiid-stages-stagename"></a>

Represents an API stage.

## URI
<a name="apis-apiid-stages-stagename-url"></a>

`/v2/apis/{{apiId}}/stages/{{stageName}}`

## HTTP methods
<a name="apis-apiid-stages-stagename-http-methods"></a>

### GET
<a name="apis-apiid-stages-stagenameget"></a>

**Operation ID:** `GetStage`

Gets a `Stage`.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{stageName}} | String | True | The stage name. Stage names can contain only alphanumeric characters, hyphens, and underscores, or be `$default`. Maximum length is 128 characters. |
| {{apiId}} | String | True | The API identifier. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | Stage | Success |
| 404 | NotFoundException | The resource specified in the request was not found. |
| 429 | LimitExceededException | The client is sending more than the allowed number of requests per unit of time. |

### DELETE
<a name="apis-apiid-stages-stagenamedelete"></a>

**Operation ID:** `DeleteStage`

Deletes a `Stage`.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{stageName}} | String | True | The stage name. Stage names can contain only alphanumeric characters, hyphens, and underscores, or be `$default`. Maximum length is 128 characters. |
| {{apiId}} | String | True | The API identifier. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 204 | None | The request has succeeded, and there is no additional content to send in the response payload body. |
| 404 | NotFoundException | The resource specified in the request was not found. |
| 429 | LimitExceededException | The client is sending more than the allowed number of requests per unit of time. |

### PATCH
<a name="apis-apiid-stages-stagenamepatch"></a>

**Operation ID:** `UpdateStage`

Updates a `Stage`.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{stageName}} | String | True | The stage name. Stage names can contain only alphanumeric characters, hyphens, and underscores, or be `$default`. Maximum length is 128 characters. |
| {{apiId}} | String | True | The API identifier. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | Stage | Success |
| 400 | BadRequestException | One of the parameters in the request is invalid. |
| 404 | NotFoundException | The resource specified in the request was not found. |
| 409 | ConflictException | The resource already exists. |
| 429 | LimitExceededException | The client is sending more than the allowed number of requests per unit of time. |

## Schemas
<a name="apis-apiid-stages-stagename-schemas"></a>

### Request bodies
<a name="apis-apiid-stages-stagename-request-examples"></a>

#### PATCH schema
<a name="apis-apiid-stages-stagename-request-body-patch-example"></a>

```
{
  "description": "string",
  "deploymentId": "string",
  "clientCertificateId": "string",
  "defaultRouteSettings": {
    "detailedMetricsEnabled": boolean,
    "loggingLevel": enum,
    "dataTraceEnabled": boolean,
    "throttlingBurstLimit": integer,
    "throttlingRateLimit": number
  },
  "routeSettings": {
  },
  "stageVariables": {
  },
  "accessLogSettings": {
    "format": "string",
    "destinationArn": "string"
  },
  "autoDeploy": boolean
}
```

### Response bodies
<a name="apis-apiid-stages-stagename-response-examples"></a>

#### Stage schema
<a name="apis-apiid-stages-stagename-response-body-stage-example"></a>

```
{
  "stageName": "string",
  "description": "string",
  "deploymentId": "string",
  "clientCertificateId": "string",
  "defaultRouteSettings": {
    "detailedMetricsEnabled": boolean,
    "loggingLevel": enum,
    "dataTraceEnabled": boolean,
    "throttlingBurstLimit": integer,
    "throttlingRateLimit": number
  },
  "routeSettings": {
  },
  "stageVariables": {
  },
  "accessLogSettings": {
    "format": "string",
    "destinationArn": "string"
  },
  "autoDeploy": boolean,
  "lastDeploymentStatusMessage": "string",
  "createdDate": "string",
  "lastUpdatedDate": "string",
  "tags": {
  },
  "apiGatewayManaged": boolean
}
```

#### BadRequestException schema
<a name="apis-apiid-stages-stagename-response-body-badrequestexception-example"></a>

```
{
  "message": "string"
}
```

#### NotFoundException schema
<a name="apis-apiid-stages-stagename-response-body-notfoundexception-example"></a>

```
{
  "message": "string",
  "resourceType": "string"
}
```

#### ConflictException schema
<a name="apis-apiid-stages-stagename-response-body-conflictexception-example"></a>

```
{
  "message": "string"
}
```

#### LimitExceededException schema
<a name="apis-apiid-stages-stagename-response-body-limitexceededexception-example"></a>

```
{
  "message": "string",
  "limitType": "string"
}
```

## Properties
<a name="apis-apiid-stages-stagename-properties"></a>

### AccessLogSettings
<a name="apis-apiid-stages-stagename-model-accesslogsettings"></a>

Settings for logging access in a stage.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| destinationArn | string | False | The ARN of the CloudWatch Logs log group to receive access logs. |
| format | string | False | A single line format of the access logs of data, as specified by selected $context variables. The format must include at least $context.requestId. |

### BadRequestException
<a name="apis-apiid-stages-stagename-model-badrequestexception"></a>

The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Describes the error encountered. |

### ConflictException
<a name="apis-apiid-stages-stagename-model-conflictexception"></a>

The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Describes the error encountered. |

### LimitExceededException
<a name="apis-apiid-stages-stagename-model-limitexceededexception"></a>

A limit has been exceeded. See the accompanying error message for details.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| limitType | string | False | The limit type. |
| message | string | False | Describes the error encountered. |

### LoggingLevel
<a name="apis-apiid-stages-stagename-model-logginglevel"></a>

The logging level.
+ `ERROR`
+ `INFO`
+ `false`

### NotFoundException
<a name="apis-apiid-stages-stagename-model-notfoundexception"></a>

The resource specified in the request was not found. See the `message` field for more information.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Describes the error encountered. |
| resourceType | string | False | The resource type. |

### RouteSettings
<a name="apis-apiid-stages-stagename-model-routesettings"></a>

Represents a collection of route settings.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| dataTraceEnabled | boolean | False | Specifies whether (`true`) or not (`false`) data trace logging is enabled for this route. This property affects the log entries pushed to Amazon CloudWatch Logs. Supported only for WebSocket APIs. |
| detailedMetricsEnabled | boolean | False | Specifies whether detailed metrics are enabled. |
| loggingLevel | [LoggingLevel](#apis-apiid-stages-stagename-model-logginglevel) | False | Specifies the logging level for this route: `INFO`, `ERROR`, or `OFF`. This property affects the log entries pushed to Amazon CloudWatch Logs. Supported only for WebSocket APIs. |
| throttlingBurstLimit | integer<br />Format: int32 | False | Specifies the throttling burst limit. |
| throttlingRateLimit | number<br />Format: double | False | Specifies the throttling rate limit. |

### RouteSettingsMap
<a name="apis-apiid-stages-stagename-model-routesettingsmap"></a>

The route settings map.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| `*` | object | False |  |

### Stage
<a name="apis-apiid-stages-stagename-model-stage"></a>

Represents an API stage.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| accessLogSettings | [AccessLogSettings](#apis-apiid-stages-stagename-model-accesslogsettings) | False | Settings for logging access in this stage. |
| apiGatewayManaged | boolean | False | Specifies whether a stage is managed by API Gateway. If you created an API using quick create, the `$default` stage is managed by API Gateway. You can't modify the `$default` stage. |
| autoDeploy | boolean | False | Specifies whether updates to an API automatically trigger a new deployment. The default value is `false`. |
| clientCertificateId | string | False | The identifier of a client certificate for a `Stage`. Supported only for WebSocket APIs. |
| createdDate | string<br />Format: date-time | False | The timestamp when the stage was created. |
| defaultRouteSettings | [RouteSettings](#apis-apiid-stages-stagename-model-routesettings) | False | Default route settings for the stage. |
| deploymentId | string | False | The identifier of the `Deployment` that the `Stage` is associated with. Can't be updated if `autoDeploy` is enabled. |
| description | string | False | The description of the stage. |
| lastDeploymentStatusMessage | string | False | Describes the status of the last deployment of a stage. Supported only for stages with `autoDeploy` enabled. |
| lastUpdatedDate | string<br />Format: date-time | False | The timestamp when the stage was last updated. |
| routeSettings | [RouteSettingsMap](#apis-apiid-stages-stagename-model-routesettingsmap) | False | Route settings for the stage, by `routeKey`. |
| stageName | string | True | The name of the stage. |
| stageVariables | [StageVariablesMap](#apis-apiid-stages-stagename-model-stagevariablesmap) | False | A map that defines the stage variables for a stage resource. Variable names can have alphanumeric and underscore characters, and the values must match [A-Za-z0-9-.\_\~:/?\#&=,]\+. |
| tags | [Tags](#apis-apiid-stages-stagename-model-tags) | False | The collection of tags. Each tag element is associated with a given resource. |

### StageVariablesMap
<a name="apis-apiid-stages-stagename-model-stagevariablesmap"></a>

The stage variable map.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| `*` | string | False |  |

### Tags
<a name="apis-apiid-stages-stagename-model-tags"></a>

Represents a collection of tags associated with the resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| `*` | string | False |  |

### UpdateStageInput
<a name="apis-apiid-stages-stagename-model-updatestageinput"></a>

Represents the input parameters for an `UpdateStage` request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| accessLogSettings | [AccessLogSettings](#apis-apiid-stages-stagename-model-accesslogsettings) | False | Settings for logging access in this stage. |
| autoDeploy | boolean | False | Specifies whether updates to an API automatically trigger a new deployment. The default value is `false`. |
| clientCertificateId | string | False | The identifier of a client certificate for a `Stage`. |
| defaultRouteSettings | [RouteSettings](#apis-apiid-stages-stagename-model-routesettings) | False | The default route settings for the stage. |
| deploymentId | string | False | The deployment identifier for the API stage. Can't be updated if `autoDeploy` is enabled. |
| description | string | False | The description for the API stage. |
| routeSettings | [RouteSettingsMap](#apis-apiid-stages-stagename-model-routesettingsmap) | False | Route settings for the stage. |
| stageVariables | [StageVariablesMap](#apis-apiid-stages-stagename-model-stagevariablesmap) | False | A map that defines the stage variables for a `Stage`. Variable names can have alphanumeric and underscore characters, and the values must match [A-Za-z0-9-.\_\~:/?\#&=,]\+. |

## See also
<a name="apis-apiid-stages-stagename-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### GetStage
<a name="GetStage-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/apigatewayv2-2018-11-29/GetStage)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/apigatewayv2-2018-11-29/GetStage)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/apigatewayv2-2018-11-29/GetStage)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/apigatewayv2-2018-11-29/GetStage)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/apigatewayv2-2018-11-29/GetStage)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/apigatewayv2-2018-11-29/GetStage)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/apigatewayv2-2018-11-29/GetStage)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/apigatewayv2-2018-11-29/GetStage)
+ [AWS SDK for Python (Boto3)](/goto/boto3/apigatewayv2-2018-11-29/GetStage)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/apigatewayv2-2018-11-29/GetStage)

### DeleteStage
<a name="DeleteStage-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/apigatewayv2-2018-11-29/DeleteStage)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/apigatewayv2-2018-11-29/DeleteStage)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/apigatewayv2-2018-11-29/DeleteStage)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/apigatewayv2-2018-11-29/DeleteStage)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/apigatewayv2-2018-11-29/DeleteStage)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/apigatewayv2-2018-11-29/DeleteStage)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/apigatewayv2-2018-11-29/DeleteStage)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/apigatewayv2-2018-11-29/DeleteStage)
+ [AWS SDK for Python (Boto3)](/goto/boto3/apigatewayv2-2018-11-29/DeleteStage)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/apigatewayv2-2018-11-29/DeleteStage)

### UpdateStage
<a name="UpdateStage-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/apigatewayv2-2018-11-29/UpdateStage)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/apigatewayv2-2018-11-29/UpdateStage)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/apigatewayv2-2018-11-29/UpdateStage)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/apigatewayv2-2018-11-29/UpdateStage)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/apigatewayv2-2018-11-29/UpdateStage)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/apigatewayv2-2018-11-29/UpdateStage)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/apigatewayv2-2018-11-29/UpdateStage)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/apigatewayv2-2018-11-29/UpdateStage)
+ [AWS SDK for Python (Boto3)](/goto/boto3/apigatewayv2-2018-11-29/UpdateStage)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/apigatewayv2-2018-11-29/UpdateStage)
