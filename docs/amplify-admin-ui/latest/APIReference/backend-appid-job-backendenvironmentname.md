---
source_url: https://docs.aws.amazon.com/amplify-admin-ui/latest/APIReference/backend-appid-job-backendenvironmentname.html
---

# Backend appId Job backendEnvironmentName
<a name="backend-appid-job-backendenvironmentname"></a>

Jobs perform backend API actions on your behalf based on your choices in the Amplify Admin UI. The actions that the jobs perform depend on the underlying API request sent from the Amplify Admin UI.

This resource is associated with the `ListBackendJobs` operation.

## URI
<a name="backend-appid-job-backendenvironmentname-url"></a>

`/prod/backend/{{appId}}/job/{{backendEnvironmentName}}`

## HTTP methods
<a name="backend-appid-job-backendenvironmentname-http-methods"></a>

### POST
<a name="backend-appid-job-backendenvironmentnamepost"></a>

**Operation ID:** `ListBackendJobs`

Lists the jobs for the backend of an Amplify app.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{appId}} | String | True | The app ID. |
| {{backendEnvironmentName}} | String | True | The name of the backend environment. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | ListBackendJobRespObj | 200 response |
| 400 | BadRequestException | 400 response |
| 404 | NotFoundException | 404 response |
| 429 | LimitExceededException | 429 response |
| 504 | InternalServiceException | 504 response |

### OPTIONS
<a name="backend-appid-job-backendenvironmentnameoptions"></a>

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
<a name="backend-appid-job-backendenvironmentname-schemas"></a>

### Request bodies
<a name="backend-appid-job-backendenvironmentname-request-examples"></a>

#### POST schema
<a name="backend-appid-job-backendenvironmentname-request-body-post-example"></a>

```
{
  "jobId": "string",
  "nextToken": "string",
  "maxResults": integer,
  "operation": "string",
  "status": "string"
}
```

### Response bodies
<a name="backend-appid-job-backendenvironmentname-response-examples"></a>

#### ListBackendJobRespObj schema
<a name="backend-appid-job-backendenvironmentname-response-body-listbackendjobrespobj-example"></a>

```
{
  "nextToken": "string",
  "jobs": [
    {
      "jobId": "string",
      "createTime": "string",
      "appId": "string",
      "updateTime": "string",
      "error": "string",
      "operation": "string",
      "backendEnvironmentName": "string",
      "status": "string"
    }
  ]
}
```

#### BadRequestException schema
<a name="backend-appid-job-backendenvironmentname-response-body-badrequestexception-example"></a>

```
{
  "message": "string"
}
```

#### NotFoundException schema
<a name="backend-appid-job-backendenvironmentname-response-body-notfoundexception-example"></a>

```
{
  "message": "string",
  "resourceType": "string"
}
```

#### LimitExceededException schema
<a name="backend-appid-job-backendenvironmentname-response-body-limitexceededexception-example"></a>

```
{
  "message": "string",
  "limitType": "string"
}
```

#### InternalServiceException schema
<a name="backend-appid-job-backendenvironmentname-response-body-internalserviceexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="backend-appid-job-backendenvironmentname-properties"></a>

### BackendJobRespObj
<a name="backend-appid-job-backendenvironmentname-model-backendjobrespobj"></a>

The response object for this operation.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| appId | string | True | The app ID. |
| backendEnvironmentName | string | True | The name of the backend environment. |
| createTime | string | False | The time when the job was created. |
| error | string | False | If the request fails, this error is returned. |
| jobId | string | False | The ID for the job. |
| operation | string | False | The name of the operation. |
| status | string | False | The current status of the request. |
| updateTime | string | False | The time when the job was last updated. |

### BadRequestException
<a name="backend-appid-job-backendenvironmentname-model-badrequestexception"></a>

An error returned if a request is not formed properly.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | An error message to inform that the request failed. |

### InternalServiceException
<a name="backend-appid-job-backendenvironmentname-model-internalserviceexception"></a>

An error returned if there's a temporary issue with the service.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | An error message to inform that the request failed. |

### LimitExceededException
<a name="backend-appid-job-backendenvironmentname-model-limitexceededexception"></a>

An error that is returned when a limit of a specific type has been exceeded.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| limitType | string | False | The type of limit that was exceeded. |
| message | string | False | An error message to inform that the request has failed. |

### ListBackendJobReqObj
<a name="backend-appid-job-backendenvironmentname-model-listbackendjobreqobj"></a>

The request object for this operation.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| jobId | string | False | The ID for the job. |
| maxResults | integer<br />Format: int32<br />Minimum: 1<br />Maximum: 25 | False | The maximum number of results that you want in the response. |
| nextToken | string | False | The token for the next set of results. |
| operation | string | False | Filters the list of response objects to include only those with the specified operation name. |
| status | string | False | Filters the list of response objects to include only those with the specified status. |

### ListBackendJobRespObj
<a name="backend-appid-job-backendenvironmentname-model-listbackendjobrespobj"></a>

The returned list of backend jobs.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| jobs | Array of type [BackendJobRespObj](#backend-appid-job-backendenvironmentname-model-backendjobrespobj) | False | An array of jobs and their properties. |
| nextToken | string | False | The token for the next set of results. |

### NotFoundException
<a name="backend-appid-job-backendenvironmentname-model-notfoundexception"></a>

An error returned when a specific resource type is not found.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | An error message to inform that the request has failed. |
| resourceType | string | False | The type of resource that is not found. |

## See also
<a name="backend-appid-job-backendenvironmentname-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### ListBackendJobs
<a name="ListBackendJobs-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/amplifybackend-2020-08-11/ListBackendJobs)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/amplifybackend-2020-08-11/ListBackendJobs)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/amplifybackend-2020-08-11/ListBackendJobs)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/amplifybackend-2020-08-11/ListBackendJobs)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/amplifybackend-2020-08-11/ListBackendJobs)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/amplifybackend-2020-08-11/ListBackendJobs)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/amplifybackend-2020-08-11/ListBackendJobs)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/amplifybackend-2020-08-11/ListBackendJobs)
+ [AWS SDK for Python](/goto/boto3/amplifybackend-2020-08-11/ListBackendJobs)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/amplifybackend-2020-08-11/ListBackendJobs)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Amplify Admin UI. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amplify-admin-ui` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
