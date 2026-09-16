---
source_url: https://docs.aws.amazon.com/apigatewayv2/latest/api-reference/domainnames-domainname-apimappings.html
---

# ApiMappings
<a name="domainnames-domainname-apimappings"></a>

Represents a collection of API mappings.

## URI
<a name="domainnames-domainname-apimappings-url"></a>

`/v2/domainnames/{{domainName}}/apimappings`

## HTTP methods
<a name="domainnames-domainname-apimappings-http-methods"></a>

### GET
<a name="domainnames-domainname-apimappingsget"></a>

**Operation ID:** `GetApiMappings`

Gets API mappings.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{domainName}} | String | True | The domain name. |

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| nextToken | String | False | The next page of elements from this collection. Not valid for the last element of the collection. |
| maxResults | String | False | The maximum number of elements to be returned for this resource. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | ApiMappings | Success |
| 400 | BadRequestException | One of the parameters in the request is invalid. |
| 404 | NotFoundException | The resource specified in the request was not found. |
| 429 | LimitExceededException | The client is sending more than the allowed number of requests per unit of time. |

### POST
<a name="domainnames-domainname-apimappingspost"></a>

**Operation ID:** `CreateApiMapping`

Creates an API mapping.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{domainName}} | String | True | The domain name. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 201 | ApiMapping | The request has succeeded and has resulted in the creation of a resource. |
| 400 | BadRequestException | One of the parameters in the request is invalid. |
| 404 | NotFoundException | The resource specified in the request was not found. |
| 409 | ConflictException | The resource already exists. |
| 429 | LimitExceededException | The client is sending more than the allowed number of requests per unit of time. |

## Schemas
<a name="domainnames-domainname-apimappings-schemas"></a>

### Request bodies
<a name="domainnames-domainname-apimappings-request-examples"></a>

#### POST schema
<a name="domainnames-domainname-apimappings-request-body-post-example"></a>

```
{
  "apiMappingKey": "string",
  "apiId": "string",
  "stage": "string"
}
```

### Response bodies
<a name="domainnames-domainname-apimappings-response-examples"></a>

#### ApiMappings schema
<a name="domainnames-domainname-apimappings-response-body-apimappings-example"></a>

```
{
  "items": [
    {
      "apiMappingId": "string",
      "apiMappingKey": "string",
      "apiId": "string",
      "stage": "string"
    }
  ],
  "nextToken": "string"
}
```

#### ApiMapping schema
<a name="domainnames-domainname-apimappings-response-body-apimapping-example"></a>

```
{
  "apiMappingId": "string",
  "apiMappingKey": "string",
  "apiId": "string",
  "stage": "string"
}
```

#### BadRequestException schema
<a name="domainnames-domainname-apimappings-response-body-badrequestexception-example"></a>

```
{
  "message": "string"
}
```

#### NotFoundException schema
<a name="domainnames-domainname-apimappings-response-body-notfoundexception-example"></a>

```
{
  "message": "string",
  "resourceType": "string"
}
```

#### ConflictException schema
<a name="domainnames-domainname-apimappings-response-body-conflictexception-example"></a>

```
{
  "message": "string"
}
```

#### LimitExceededException schema
<a name="domainnames-domainname-apimappings-response-body-limitexceededexception-example"></a>

```
{
  "message": "string",
  "limitType": "string"
}
```

## Properties
<a name="domainnames-domainname-apimappings-properties"></a>

### ApiMapping
<a name="domainnames-domainname-apimappings-model-apimapping"></a>

Represents an API mapping.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| apiId | string | True | The API identifier. |
| apiMappingId | string | False | The API mapping identifier. |
| apiMappingKey | string | False | The API mapping key. |
| stage | string | True | The API stage. |

### ApiMappings
<a name="domainnames-domainname-apimappings-model-apimappings"></a>

Represents a collection of `ApiMappings` resources.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| items | Array of type [ApiMapping](#domainnames-domainname-apimappings-model-apimapping) | False | The elements from this collection. |
| nextToken | string | False | The next page of elements from this collection. Not valid for the last element of the collection. |

### BadRequestException
<a name="domainnames-domainname-apimappings-model-badrequestexception"></a>

The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Describes the error encountered. |

### ConflictException
<a name="domainnames-domainname-apimappings-model-conflictexception"></a>

The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Describes the error encountered. |

### CreateApiMappingInput
<a name="domainnames-domainname-apimappings-model-createapimappinginput"></a>

Represents the input parameters for a `CreateApiMapping` request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| apiId | string | True | The API identifier. |
| apiMappingKey | string | False | The API mapping key. |
| stage | string | True | The API stage. |

### LimitExceededException
<a name="domainnames-domainname-apimappings-model-limitexceededexception"></a>

A limit has been exceeded. See the accompanying error message for details.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| limitType | string | False | The limit type. |
| message | string | False | Describes the error encountered. |

### NotFoundException
<a name="domainnames-domainname-apimappings-model-notfoundexception"></a>

The resource specified in the request was not found. See the `message` field for more information.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Describes the error encountered. |
| resourceType | string | False | The resource type. |

## See also
<a name="domainnames-domainname-apimappings-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### GetApiMappings
<a name="GetApiMappings-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/apigatewayv2-2018-11-29/GetApiMappings)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/apigatewayv2-2018-11-29/GetApiMappings)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/apigatewayv2-2018-11-29/GetApiMappings)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/apigatewayv2-2018-11-29/GetApiMappings)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/apigatewayv2-2018-11-29/GetApiMappings)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/apigatewayv2-2018-11-29/GetApiMappings)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/apigatewayv2-2018-11-29/GetApiMappings)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/apigatewayv2-2018-11-29/GetApiMappings)
+ [AWS SDK for Python (Boto3)](/goto/boto3/apigatewayv2-2018-11-29/GetApiMappings)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/apigatewayv2-2018-11-29/GetApiMappings)

### CreateApiMapping
<a name="CreateApiMapping-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/apigatewayv2-2018-11-29/CreateApiMapping)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/apigatewayv2-2018-11-29/CreateApiMapping)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/apigatewayv2-2018-11-29/CreateApiMapping)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/apigatewayv2-2018-11-29/CreateApiMapping)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/apigatewayv2-2018-11-29/CreateApiMapping)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/apigatewayv2-2018-11-29/CreateApiMapping)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/apigatewayv2-2018-11-29/CreateApiMapping)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/apigatewayv2-2018-11-29/CreateApiMapping)
+ [AWS SDK for Python (Boto3)](/goto/boto3/apigatewayv2-2018-11-29/CreateApiMapping)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/apigatewayv2-2018-11-29/CreateApiMapping)
