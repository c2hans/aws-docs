---
source_url: https://docs.aws.amazon.com/apigatewayv2/latest/api-reference/apis-apiid-deployments.html
---

# Deployments
<a name="apis-apiid-deployments"></a>

Represents the collection of deployments for an API.

## URI
<a name="apis-apiid-deployments-url"></a>

`/v2/apis/{{apiId}}/deployments`

## HTTP methods
<a name="apis-apiid-deployments-http-methods"></a>

### GET
<a name="apis-apiid-deploymentsget"></a>

**Operation ID:** `GetDeployments`

Gets the `Deployments` for an API.

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
| 200 | Deployments | Success |
| 400 | BadRequestException | One of the parameters in the request is invalid. |
| 404 | NotFoundException | The resource specified in the request was not found. |
| 429 | LimitExceededException | The client is sending more than the allowed number of requests per unit of time. |

### POST
<a name="apis-apiid-deploymentspost"></a>

**Operation ID:** `CreateDeployment`

Creates a `Deployment` for an API.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{apiId}} | String | True | The API identifier. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 201 | Deployment | The request has succeeded and has resulted in the creation of a resource. |
| 400 | BadRequestException | One of the parameters in the request is invalid. |
| 404 | NotFoundException | The resource specified in the request was not found. |
| 409 | ConflictException | The resource already exists. |
| 429 | LimitExceededException | The client is sending more than the allowed number of requests per unit of time. |

## Schemas
<a name="apis-apiid-deployments-schemas"></a>

### Request bodies
<a name="apis-apiid-deployments-request-examples"></a>

#### POST schema
<a name="apis-apiid-deployments-request-body-post-example"></a>

```
{
  "description": "string",
  "stageName": "string"
}
```

### Response bodies
<a name="apis-apiid-deployments-response-examples"></a>

#### Deployments schema
<a name="apis-apiid-deployments-response-body-deployments-example"></a>

```
{
  "items": [
    {
      "deploymentId": "string",
      "description": "string",
      "createdDate": "string",
      "deploymentStatus": enum,
      "deploymentStatusMessage": "string",
      "autoDeployed": boolean
    }
  ],
  "nextToken": "string"
}
```

#### Deployment schema
<a name="apis-apiid-deployments-response-body-deployment-example"></a>

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
<a name="apis-apiid-deployments-response-body-badrequestexception-example"></a>

```
{
  "message": "string"
}
```

#### NotFoundException schema
<a name="apis-apiid-deployments-response-body-notfoundexception-example"></a>

```
{
  "message": "string",
  "resourceType": "string"
}
```

#### ConflictException schema
<a name="apis-apiid-deployments-response-body-conflictexception-example"></a>

```
{
  "message": "string"
}
```

#### LimitExceededException schema
<a name="apis-apiid-deployments-response-body-limitexceededexception-example"></a>

```
{
  "message": "string",
  "limitType": "string"
}
```

## Properties
<a name="apis-apiid-deployments-properties"></a>

### BadRequestException
<a name="apis-apiid-deployments-model-badrequestexception"></a>

The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Describes the error encountered. |

### ConflictException
<a name="apis-apiid-deployments-model-conflictexception"></a>

The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Describes the error encountered. |

### CreateDeploymentInput
<a name="apis-apiid-deployments-model-createdeploymentinput"></a>

Represents the input parameters for a `CreateDeployment` request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| description | string | False | The description for the deployment resource. |
| stageName | string | False | The name of an existing stage to associate with the deployment. |

### Deployment
<a name="apis-apiid-deployments-model-deployment"></a>

An immutable representation of an API that can be called by users. A `Deployment` must be associated with a `Stage` for it to be callable over the internet.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| autoDeployed | boolean | False | Specifies whether a deployment was automatically released. |
| createdDate | string<br />Format: date-time | False | The date and time when the `Deployment` resource was created. |
| deploymentId | string | False | The identifier for the deployment. |
| deploymentStatus | [DeploymentStatus](#apis-apiid-deployments-model-deploymentstatus) | False | The status of the deployment: `PENDING`, `FAILED`, or `SUCCEEDED`. |
| deploymentStatusMessage | string | False | May contain additional feedback on the status of an API deployment. |
| description | string | False | The description for the deployment. |

### DeploymentStatus
<a name="apis-apiid-deployments-model-deploymentstatus"></a>

Represents a deployment status.
+ `PENDING`
+ `FAILED`
+ `DEPLOYED`

### Deployments
<a name="apis-apiid-deployments-model-deployments"></a>

A collection resource that contains zero or more references to your existing deployments, and links that guide you on how to interact with your collection. The collection offers a paginated view of the contained deployments.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| items | Array of type [Deployment](#apis-apiid-deployments-model-deployment) | False | The elements from this collection. |
| nextToken | string | False | The next page of elements from this collection. Not valid for the last element of the collection. |

### LimitExceededException
<a name="apis-apiid-deployments-model-limitexceededexception"></a>

A limit has been exceeded. See the accompanying error message for details.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| limitType | string | False | The limit type. |
| message | string | False | Describes the error encountered. |

### NotFoundException
<a name="apis-apiid-deployments-model-notfoundexception"></a>

The resource specified in the request was not found. See the `message` field for more information.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Describes the error encountered. |
| resourceType | string | False | The resource type. |

## See also
<a name="apis-apiid-deployments-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### GetDeployments
<a name="GetDeployments-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/apigatewayv2-2018-11-29/GetDeployments)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/apigatewayv2-2018-11-29/GetDeployments)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/apigatewayv2-2018-11-29/GetDeployments)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/apigatewayv2-2018-11-29/GetDeployments)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/apigatewayv2-2018-11-29/GetDeployments)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/apigatewayv2-2018-11-29/GetDeployments)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/apigatewayv2-2018-11-29/GetDeployments)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/apigatewayv2-2018-11-29/GetDeployments)
+ [AWS SDK for Python](/goto/boto3/apigatewayv2-2018-11-29/GetDeployments)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/apigatewayv2-2018-11-29/GetDeployments)

### CreateDeployment
<a name="CreateDeployment-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/apigatewayv2-2018-11-29/CreateDeployment)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/apigatewayv2-2018-11-29/CreateDeployment)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/apigatewayv2-2018-11-29/CreateDeployment)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/apigatewayv2-2018-11-29/CreateDeployment)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/apigatewayv2-2018-11-29/CreateDeployment)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/apigatewayv2-2018-11-29/CreateDeployment)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/apigatewayv2-2018-11-29/CreateDeployment)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/apigatewayv2-2018-11-29/CreateDeployment)
+ [AWS SDK for Python](/goto/boto3/apigatewayv2-2018-11-29/CreateDeployment)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/apigatewayv2-2018-11-29/CreateDeployment)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon API Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apigatewayv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
