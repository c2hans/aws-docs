---
source_url: https://docs.aws.amazon.com/amplify-admin-ui/latest/APIReference/backend-appid-api-backendenvironmentname-getmodels.html
---

# Backend appId Api backendEnvironmentName GetModels
<a name="backend-appid-api-backendenvironmentname-getmodels"></a>

The generated datastore models for your Amplify app. Web clients can consume these to use the datastore.

## URI
<a name="backend-appid-api-backendenvironmentname-getmodels-url"></a>

`/prod/backend/{{appId}}/api/{{backendEnvironmentName}}/getModels`

## HTTP methods
<a name="backend-appid-api-backendenvironmentname-getmodels-http-methods"></a>

### POST
<a name="backend-appid-api-backendenvironmentname-getmodelspost"></a>

**Operation ID:** `GetBackendAPIModels`

Gets a model introspection schema for an existing backend API resource.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{appId}} | String | True | The app ID. |
| {{backendEnvironmentName}} | String | True | The name of the backend environment. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | GetBackendAPIModelsResponse | 200 response |
| 400 | BadRequestException | 400 response |
| 404 | NotFoundException | 404 response |
| 429 | LimitExceededException | 429 response |
| 504 | InternalServiceException | 504 response |

### OPTIONS
<a name="backend-appid-api-backendenvironmentname-getmodelsoptions"></a>

Enables CORS by returning the correct headers.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{appId}} | String | True | The app ID. |
| {{backendEnvironmentName}} | String | True | The name of the backend environment. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | 200 response |

## Schemas
<a name="backend-appid-api-backendenvironmentname-getmodels-schemas"></a>

### Request bodies
<a name="backend-appid-api-backendenvironmentname-getmodels-request-examples"></a>

#### POST schema
<a name="backend-appid-api-backendenvironmentname-getmodels-request-body-post-example"></a>

```
{
  "resourceName": "string"
}
```

### Response bodies
<a name="backend-appid-api-backendenvironmentname-getmodels-response-examples"></a>

#### GetBackendAPIModelsResponse schema
<a name="backend-appid-api-backendenvironmentname-getmodels-response-body-getbackendapimodelsresponse-example"></a>

```
{
  "models": "string",
  "modelIntrospectionSchema": "string",
  "status": enum
}
```

#### BadRequestException schema
<a name="backend-appid-api-backendenvironmentname-getmodels-response-body-badrequestexception-example"></a>

```
{
  "message": "string"
}
```

#### NotFoundException schema
<a name="backend-appid-api-backendenvironmentname-getmodels-response-body-notfoundexception-example"></a>

```
{
  "message": "string",
  "resourceType": "string"
}
```

#### LimitExceededException schema
<a name="backend-appid-api-backendenvironmentname-getmodels-response-body-limitexceededexception-example"></a>

```
{
  "message": "string",
  "limitType": "string"
}
```

#### InternalServiceException schema
<a name="backend-appid-api-backendenvironmentname-getmodels-response-body-internalserviceexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="backend-appid-api-backendenvironmentname-getmodels-properties"></a>

### BackendAPICodegenReqObj
<a name="backend-appid-api-backendenvironmentname-getmodels-model-backendapicodegenreqobj"></a>

The request object for this operation.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| resourceName | string | True | The name of this resource. |

### BadRequestException
<a name="backend-appid-api-backendenvironmentname-getmodels-model-badrequestexception"></a>

An error returned if a request is not formed properly.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | An error message to inform that the request failed. |

### GetBackendAPIModelsResponse
<a name="backend-appid-api-backendenvironmentname-getmodels-model-getbackendapimodelsresponse"></a>

The response object for this operation.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| modelIntrospectionSchema | string | False | Stringified JSON of the model introspection schema for an existing backend API resource. |
| models | string | False | Stringified JSON of the datastore model. |
| status | string<br />Values: `LATEST \| STALE` | False | The current status of the request. |

### InternalServiceException
<a name="backend-appid-api-backendenvironmentname-getmodels-model-internalserviceexception"></a>

An error returned if there's a temporary issue with the service.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | An error message to inform that the request failed. |

### LimitExceededException
<a name="backend-appid-api-backendenvironmentname-getmodels-model-limitexceededexception"></a>

An error that is returned when a limit of a specific type has been exceeded.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| limitType | string | False | The type of limit that was exceeded. |
| message | string | False | An error message to inform that the request has failed. |

### NotFoundException
<a name="backend-appid-api-backendenvironmentname-getmodels-model-notfoundexception"></a>

An error returned when a specific resource type is not found.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | An error message to inform that the request has failed. |
| resourceType | string | False | The type of resource that is not found. |

## See also
<a name="backend-appid-api-backendenvironmentname-getmodels-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### GetBackendAPIModels
<a name="GetBackendAPIModels-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/amplifybackend-2020-08-11/GetBackendAPIModels)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/amplifybackend-2020-08-11/GetBackendAPIModels)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/amplifybackend-2020-08-11/GetBackendAPIModels)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/amplifybackend-2020-08-11/GetBackendAPIModels)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/amplifybackend-2020-08-11/GetBackendAPIModels)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/amplifybackend-2020-08-11/GetBackendAPIModels)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/amplifybackend-2020-08-11/GetBackendAPIModels)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/amplifybackend-2020-08-11/GetBackendAPIModels)
+ [AWS SDK for Python](/goto/boto3/amplifybackend-2020-08-11/GetBackendAPIModels)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/amplifybackend-2020-08-11/GetBackendAPIModels)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Amplify Admin UI. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amplify-admin-ui` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
