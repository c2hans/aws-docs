---
source_url: https://docs.aws.amazon.com/apigatewayv2/latest/api-reference/apis-apiid-deployments-deploymentid.html
---

# Deployment
<a name="apis-apiid-deployments-deploymentid"></a>

Represents an API deployment.

## URI
<a name="apis-apiid-deployments-deploymentid-url"></a>

`/v2/apis/{{apiId}}/deployments/{{deploymentId}}`

## HTTP methods
<a name="apis-apiid-deployments-deploymentid-http-methods"></a>

### GET
<a name="apis-apiid-deployments-deploymentidget"></a>

**Operation ID:** `GetDeployment`

Gets a `Deployment`.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{apiId}} | String | True | The API identifier. |
| {{deploymentId}} | String | True | The deployment ID. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | Deployment | Success |
| 404 | NotFoundException | The resource specified in the request was not found. |
| 429 | LimitExceededException | The client is sending more than the allowed number of requests per unit of time. |

### DELETE
<a name="apis-apiid-deployments-deploymentiddelete"></a>

**Operation ID:** `DeleteDeployment`

Deletes a `Deployment`.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{apiId}} | String | True | The API identifier. |
| {{deploymentId}} | String | True | The deployment ID. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 204 | None | The request has succeeded, and there is no additional content to send in the response payload body. |
| 404 | NotFoundException | The resource specified in the request was not found. |
| 429 | LimitExceededException | The client is sending more than the allowed number of requests per unit of time. |

### PATCH
<a name="apis-apiid-deployments-deploymentidpatch"></a>

**Operation ID:** `UpdateDeployment`

Updates a `Deployment`.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{apiId}} | String | True | The API identifier. |
| {{deploymentId}} | String | True | The deployment ID. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | Deployment | Success |
| 400 | BadRequestException | One of the parameters in the request is invalid. |
| 404 | NotFoundException | The resource specified in the request was not found. |
| 409 | ConflictException | The resource already exists. |
| 429 | LimitExceededException | The client is sending more than the allowed number of requests per unit of time. |

## Schemas
<a name="apis-apiid-deployments-deploymentid-schemas"></a>

### Request bodies
<a name="apis-apiid-deployments-deploymentid-request-examples"></a>

#### PATCH schema
<a name="apis-apiid-deployments-deploymentid-request-body-patch-example"></a>

```
{
  "description": "string"
}
```

### Response bodies
<a name="apis-apiid-deployments-deploymentid-response-examples"></a>

#### Deployment schema
<a name="apis-apiid-deployments-deploymentid-response-body-deployment-example"></a>

```
{
  "deploymentId": "string",
  "description": "string",
  "createdDate": "string",
  "deploymentStatus": enum,
  "deploymentStatusMessage": "string",
  "autoDeployed": boolean
}
```

#### BadRequestException schema
<a name="apis-apiid-deployments-deploymentid-response-body-badrequestexception-example"></a>

```
{
  "message": "string"
}
```

#### NotFoundException schema
<a name="apis-apiid-deployments-deploymentid-response-body-notfoundexception-example"></a>

```
{
  "message": "string",
  "resourceType": "string"
}
```

#### ConflictException schema
<a name="apis-apiid-deployments-deploymentid-response-body-conflictexception-example"></a>

```
{
  "message": "string"
}
```

#### LimitExceededException schema
<a name="apis-apiid-deployments-deploymentid-response-body-limitexceededexception-example"></a>

```
{
  "message": "string",
  "limitType": "string"
}
```

## Properties
<a name="apis-apiid-deployments-deploymentid-properties"></a>

### BadRequestException
<a name="apis-apiid-deployments-deploymentid-model-badrequestexception"></a>

The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Describes the error encountered. |

### ConflictException
<a name="apis-apiid-deployments-deploymentid-model-conflictexception"></a>

The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Describes the error encountered. |

### Deployment
<a name="apis-apiid-deployments-deploymentid-model-deployment"></a>

An immutable representation of an API that can be called by users. A `Deployment` must be associated with a `Stage` for it to be callable over the internet.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| autoDeployed | boolean | False | Specifies whether a deployment was automatically released. |
| createdDate | string<br />Format: date-time | False | The date and time when the `Deployment` resource was created. |
| deploymentId | string | False | The identifier for the deployment. |
| deploymentStatus | [DeploymentStatus](#apis-apiid-deployments-deploymentid-model-deploymentstatus) | False | The status of the deployment: `PENDING`, `FAILED`, or `SUCCEEDED`. |
| deploymentStatusMessage | string | False | May contain additional feedback on the status of an API deployment. |
| description | string | False | The description for the deployment. |

### DeploymentStatus
<a name="apis-apiid-deployments-deploymentid-model-deploymentstatus"></a>

Represents a deployment status.
+ `PENDING`
+ `FAILED`
+ `DEPLOYED`

### LimitExceededException
<a name="apis-apiid-deployments-deploymentid-model-limitexceededexception"></a>

A limit has been exceeded. See the accompanying error message for details.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| limitType | string | False | The limit type. |
| message | string | False | Describes the error encountered. |

### NotFoundException
<a name="apis-apiid-deployments-deploymentid-model-notfoundexception"></a>

The resource specified in the request was not found. See the `message` field for more information.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Describes the error encountered. |
| resourceType | string | False | The resource type. |

### UpdateDeploymentInput
<a name="apis-apiid-deployments-deploymentid-model-updatedeploymentinput"></a>

Represents the input parameters for an `UpdateDeployment` request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| description | string | False | The description for the deployment resource. |

## See also
<a name="apis-apiid-deployments-deploymentid-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### GetDeployment
<a name="GetDeployment-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/apigatewayv2-2018-11-29/GetDeployment)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/apigatewayv2-2018-11-29/GetDeployment)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/apigatewayv2-2018-11-29/GetDeployment)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/apigatewayv2-2018-11-29/GetDeployment)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/apigatewayv2-2018-11-29/GetDeployment)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/apigatewayv2-2018-11-29/GetDeployment)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/apigatewayv2-2018-11-29/GetDeployment)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/apigatewayv2-2018-11-29/GetDeployment)
+ [AWS SDK for Python (Boto3)](/goto/boto3/apigatewayv2-2018-11-29/GetDeployment)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/apigatewayv2-2018-11-29/GetDeployment)

### DeleteDeployment
<a name="DeleteDeployment-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/apigatewayv2-2018-11-29/DeleteDeployment)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/apigatewayv2-2018-11-29/DeleteDeployment)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/apigatewayv2-2018-11-29/DeleteDeployment)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/apigatewayv2-2018-11-29/DeleteDeployment)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/apigatewayv2-2018-11-29/DeleteDeployment)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/apigatewayv2-2018-11-29/DeleteDeployment)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/apigatewayv2-2018-11-29/DeleteDeployment)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/apigatewayv2-2018-11-29/DeleteDeployment)
+ [AWS SDK for Python (Boto3)](/goto/boto3/apigatewayv2-2018-11-29/DeleteDeployment)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/apigatewayv2-2018-11-29/DeleteDeployment)

### UpdateDeployment
<a name="UpdateDeployment-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/apigatewayv2-2018-11-29/UpdateDeployment)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/apigatewayv2-2018-11-29/UpdateDeployment)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/apigatewayv2-2018-11-29/UpdateDeployment)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/apigatewayv2-2018-11-29/UpdateDeployment)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/apigatewayv2-2018-11-29/UpdateDeployment)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/apigatewayv2-2018-11-29/UpdateDeployment)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/apigatewayv2-2018-11-29/UpdateDeployment)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/apigatewayv2-2018-11-29/UpdateDeployment)
+ [AWS SDK for Python (Boto3)](/goto/boto3/apigatewayv2-2018-11-29/UpdateDeployment)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/apigatewayv2-2018-11-29/UpdateDeployment)
