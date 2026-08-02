---
source_url: https://docs.aws.amazon.com/amplify-admin-ui/latest/APIReference/backend-appid-challenge.html
---

# Backend appId Challenge
<a name="backend-appid-challenge"></a>

The one-time challenge code used to authenticate a user into your Amplify Admin UI.

## URI
<a name="backend-appid-challenge-url"></a>

`/prod/backend/{{appId}}/challenge`

## HTTP methods
<a name="backend-appid-challenge-http-methods"></a>

### POST
<a name="backend-appid-challengepost"></a>

**Operation ID:** `CreateToken`

Generates a one-time challenge code to authenticate a user into your Amplify Admin UI.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{appId}} | String | True | The app ID. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | CreateTokenRespObj | 200 response |
| 400 | BadRequestException | 400 response |
| 404 | NotFoundException | 404 response |
| 429 | LimitExceededException | 429 response |
| 504 | InternalServiceException | 504 response |

### OPTIONS
<a name="backend-appid-challengeoptions"></a>

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
<a name="backend-appid-challenge-schemas"></a>

### Response bodies
<a name="backend-appid-challenge-response-examples"></a>

#### CreateTokenRespObj schema
<a name="backend-appid-challenge-response-body-createtokenrespobj-example"></a>

```
{
  "appId": "string",
  "sessionId": "string",
  "ttl": "string",
  "challengeCode": "string"
}
```

#### BadRequestException schema
<a name="backend-appid-challenge-response-body-badrequestexception-example"></a>

```
{
  "message": "string"
}
```

#### NotFoundException schema
<a name="backend-appid-challenge-response-body-notfoundexception-example"></a>

```
{
  "message": "string",
  "resourceType": "string"
}
```

#### LimitExceededException schema
<a name="backend-appid-challenge-response-body-limitexceededexception-example"></a>

```
{
  "message": "string",
  "limitType": "string"
}
```

#### InternalServiceException schema
<a name="backend-appid-challenge-response-body-internalserviceexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="backend-appid-challenge-properties"></a>

### BadRequestException
<a name="backend-appid-challenge-model-badrequestexception"></a>

An error returned if a request is not formed properly.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | An error message to inform that the request failed. |

### CreateTokenRespObj
<a name="backend-appid-challenge-model-createtokenrespobj"></a>

The response object for this operation.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| appId | string | True | The app ID. |
| challengeCode | string | True | One-time challenge code for authenticating into the Amplify Admin UI. |
| sessionId | string | True | A unique ID provided when creating a new challenge token. |
| ttl | string | True | The expiry time for the one-time generated token code. |

### InternalServiceException
<a name="backend-appid-challenge-model-internalserviceexception"></a>

An error returned if there's a temporary issue with the service.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | An error message to inform that the request failed. |

### LimitExceededException
<a name="backend-appid-challenge-model-limitexceededexception"></a>

An error that is returned when a limit of a specific type has been exceeded.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| limitType | string | False | The type of limit that was exceeded. |
| message | string | False | An error message to inform that the request has failed. |

### NotFoundException
<a name="backend-appid-challenge-model-notfoundexception"></a>

An error returned when a specific resource type is not found.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | An error message to inform that the request has failed. |
| resourceType | string | False | The type of resource that is not found. |

## See also
<a name="backend-appid-challenge-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### CreateToken
<a name="CreateToken-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/amplifybackend-2020-08-11/CreateToken)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/amplifybackend-2020-08-11/CreateToken)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/amplifybackend-2020-08-11/CreateToken)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/amplifybackend-2020-08-11/CreateToken)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/amplifybackend-2020-08-11/CreateToken)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/amplifybackend-2020-08-11/CreateToken)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/amplifybackend-2020-08-11/CreateToken)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/amplifybackend-2020-08-11/CreateToken)
+ [AWS SDK for Python](/goto/boto3/amplifybackend-2020-08-11/CreateToken)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/amplifybackend-2020-08-11/CreateToken)
