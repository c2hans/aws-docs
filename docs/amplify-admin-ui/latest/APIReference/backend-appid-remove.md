---
source_url: https://docs.aws.amazon.com/amplify-admin-ui/latest/APIReference/backend-appid-remove.html
---

# Backend appId Remove
<a name="backend-appid-remove"></a>

All Amplify apps have a backend. The backend has settings and configurations for data storage, security, and other important logic that your app's users don't see. The easiest way to manage your Amplify app backend is by using the Amplify Admin UI for your app.

## URI
<a name="backend-appid-remove-url"></a>

`/prod/backend/{{appId}}/remove`

## HTTP methods
<a name="backend-appid-remove-http-methods"></a>

### POST
<a name="backend-appid-removepost"></a>

**Operation ID:** `RemoveAllBackends`

Removes all backend environments from your Amplify project.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{appId}} | String | True | The app ID. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | RemoveAllBackendsRespObj | 200 response |
| 400 | BadRequestException | 400 response |
| 404 | NotFoundException | 404 response |
| 429 | LimitExceededException | 429 response |
| 504 | InternalServiceException | 504 response |

### OPTIONS
<a name="backend-appid-removeoptions"></a>

Enables CORS by returning the correct headers.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{appId}} | String | True | The app ID. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | 200 response |

## Schemas
<a name="backend-appid-remove-schemas"></a>

### Request bodies
<a name="backend-appid-remove-request-examples"></a>

#### POST schema
<a name="backend-appid-remove-request-body-post-example"></a>

```
{
  "cleanAmplifyApp": boolean
}
```

### Response bodies
<a name="backend-appid-remove-response-examples"></a>

#### RemoveAllBackendsRespObj schema
<a name="backend-appid-remove-response-body-removeallbackendsrespobj-example"></a>

```
{
  "jobId": "string",
  "appId": "string",
  "error": "string",
  "operation": "string",
  "status": "string"
}
```

#### BadRequestException schema
<a name="backend-appid-remove-response-body-badrequestexception-example"></a>

```
{
  "message": "string"
}
```

#### NotFoundException schema
<a name="backend-appid-remove-response-body-notfoundexception-example"></a>

```
{
  "message": "string",
  "resourceType": "string"
}
```

#### LimitExceededException schema
<a name="backend-appid-remove-response-body-limitexceededexception-example"></a>

```
{
  "message": "string",
  "limitType": "string"
}
```

#### InternalServiceException schema
<a name="backend-appid-remove-response-body-internalserviceexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="backend-appid-remove-properties"></a>

### BadRequestException
<a name="backend-appid-remove-model-badrequestexception"></a>

An error returned if a request is not formed properly.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | An error message to inform that the request failed. |

### InternalServiceException
<a name="backend-appid-remove-model-internalserviceexception"></a>

An error returned if there's a temporary issue with the service.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | An error message to inform that the request failed. |

### LimitExceededException
<a name="backend-appid-remove-model-limitexceededexception"></a>

An error that is returned when a limit of a specific type has been exceeded.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| limitType | string | False | The type of limit that was exceeded. |
| message | string | False | An error message to inform that the request has failed. |

### NotFoundException
<a name="backend-appid-remove-model-notfoundexception"></a>

An error returned when a specific resource type is not found.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | An error message to inform that the request has failed. |
| resourceType | string | False | The type of resource that is not found. |

### RemoveAllBackendsReqObj
<a name="backend-appid-remove-model-removeallbackendsreqobj"></a>

The request object for this operation.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| cleanAmplifyApp | boolean | False | Cleans up the Amplify Console app if this value is set to true. |

### RemoveAllBackendsRespObj
<a name="backend-appid-remove-model-removeallbackendsrespobj"></a>

The response object for this operation.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| appId | string | True | The app ID. |
| error | string | False | If the request fails, this error is returned. |
| jobId | string | False | The ID for the job. |
| operation | string | False | The name of the operation. |
| status | string | False | The current status of the request. |

## See also
<a name="backend-appid-remove-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### RemoveAllBackends
<a name="RemoveAllBackends-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/amplifybackend-2020-08-11/RemoveAllBackends)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/amplifybackend-2020-08-11/RemoveAllBackends)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/amplifybackend-2020-08-11/RemoveAllBackends)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/amplifybackend-2020-08-11/RemoveAllBackends)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/amplifybackend-2020-08-11/RemoveAllBackends)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/amplifybackend-2020-08-11/RemoveAllBackends)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/amplifybackend-2020-08-11/RemoveAllBackends)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/amplifybackend-2020-08-11/RemoveAllBackends)
+ [AWS SDK for Python](/goto/boto3/amplifybackend-2020-08-11/RemoveAllBackends)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/amplifybackend-2020-08-11/RemoveAllBackends)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Amplify Admin UI. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amplify-admin-ui` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
