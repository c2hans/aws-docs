---
source_url: https://docs.aws.amazon.com/amplify-admin-ui/latest/APIReference/backend-appid-challenge-sessionid.html
---

# Backend appId Challenge sessionId
<a name="backend-appid-challenge-sessionid"></a>

The one-time challenge code used to authenticate a user into your Amplify Admin UI.

## URI
<a name="backend-appid-challenge-sessionid-url"></a>

`/prod/backend/{{appId}}/challenge/{{sessionId}}`

## HTTP methods
<a name="backend-appid-challenge-sessionid-http-methods"></a>

### GET
<a name="backend-appid-challenge-sessionidget"></a>

**Operation ID:** `GetToken`

Gets the challenge token based on the given appId and sessionId.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{sessionId}} | String | True | The session ID. |
| {{appId}} | String | True | The app ID. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | GetTokenRespObj | 200 response |
| 400 | BadRequestException | 400 response |
| 404 | NotFoundException | 404 response |
| 429 | LimitExceededException | 429 response |
| 504 | InternalServiceException | 504 response |

### OPTIONS
<a name="backend-appid-challenge-sessionidoptions"></a>

Enables CORS by returning the correct headers.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{sessionId}} | String | True | The session ID. |
| {{appId}} | String | True | The app ID. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | 200 response |

## Schemas
<a name="backend-appid-challenge-sessionid-schemas"></a>

### Response bodies
<a name="backend-appid-challenge-sessionid-response-examples"></a>

#### GetTokenRespObj schema
<a name="backend-appid-challenge-sessionid-response-body-gettokenrespobj-example"></a>

```
{
  "appId": "string",
  "sessionId": "string",
  "ttl": "string",
  "challengeCode": "string"
}
```

#### BadRequestException schema
<a name="backend-appid-challenge-sessionid-response-body-badrequestexception-example"></a>

```
{
  "message": "string"
}
```

#### NotFoundException schema
<a name="backend-appid-challenge-sessionid-response-body-notfoundexception-example"></a>

```
{
  "message": "string",
  "resourceType": "string"
}
```

#### LimitExceededException schema
<a name="backend-appid-challenge-sessionid-response-body-limitexceededexception-example"></a>

```
{
  "message": "string",
  "limitType": "string"
}
```

#### InternalServiceException schema
<a name="backend-appid-challenge-sessionid-response-body-internalserviceexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="backend-appid-challenge-sessionid-properties"></a>

### BadRequestException
<a name="backend-appid-challenge-sessionid-model-badrequestexception"></a>

An error returned if a request is not formed properly.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | An error message to inform that the request failed. |

### GetTokenRespObj
<a name="backend-appid-challenge-sessionid-model-gettokenrespobj"></a>

The response object for this operation.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| appId | string | True | The app ID. |
| challengeCode | string | True | The one-time challenge code for authenticating into the Amplify Admin UI. |
| sessionId | string | True | A unique ID provided when creating a new challenge token. |
| ttl | string | True | The expiry time for the one-time generated token code. |

### InternalServiceException
<a name="backend-appid-challenge-sessionid-model-internalserviceexception"></a>

An error returned if there's a temporary issue with the service.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | An error message to inform that the request failed. |

### LimitExceededException
<a name="backend-appid-challenge-sessionid-model-limitexceededexception"></a>

An error that is returned when a limit of a specific type has been exceeded.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| limitType | string | False | The type of limit that was exceeded. |
| message | string | False | An error message to inform that the request has failed. |

### NotFoundException
<a name="backend-appid-challenge-sessionid-model-notfoundexception"></a>

An error returned when a specific resource type is not found.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | An error message to inform that the request has failed. |
| resourceType | string | False | The type of resource that is not found. |

## See also
<a name="backend-appid-challenge-sessionid-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### GetToken
<a name="GetToken-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/amplifybackend-2020-08-11/GetToken)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/amplifybackend-2020-08-11/GetToken)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/amplifybackend-2020-08-11/GetToken)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/amplifybackend-2020-08-11/GetToken)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/amplifybackend-2020-08-11/GetToken)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/amplifybackend-2020-08-11/GetToken)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/amplifybackend-2020-08-11/GetToken)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/amplifybackend-2020-08-11/GetToken)
+ [AWS SDK for Python (Boto3)](/goto/boto3/amplifybackend-2020-08-11/GetToken)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/amplifybackend-2020-08-11/GetToken)
