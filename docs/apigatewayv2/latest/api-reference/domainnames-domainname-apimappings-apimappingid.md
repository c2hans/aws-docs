---
source_url: https://docs.aws.amazon.com/apigatewayv2/latest/api-reference/domainnames-domainname-apimappings-apimappingid.html
---

# ApiMapping
<a name="domainnames-domainname-apimappings-apimappingid"></a>

Represent an API mapping. An API mapping relates a path of your custom domain name to a stage of your API. A custom domain name can have multiple API mappings, but the paths can't overlap. To learn more, see [Set Up a Custom Domain Name for an API in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-custom-domains.html).

## URI
<a name="domainnames-domainname-apimappings-apimappingid-url"></a>

`/v2/domainnames/{{domainName}}/apimappings/{{apiMappingId}}`

## HTTP methods
<a name="domainnames-domainname-apimappings-apimappingid-http-methods"></a>

### GET
<a name="domainnames-domainname-apimappings-apimappingidget"></a>

**Operation ID:** `GetApiMapping`

Gets an API mapping.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{apiMappingId}} | String | True | The API mapping identifier. |
| {{domainName}} | String | True | The domain name. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | ApiMapping | Success |
| 400 | BadRequestException | One of the parameters in the request is invalid. |
| 404 | NotFoundException | The resource specified in the request was not found. |
| 429 | LimitExceededException | The client is sending more than the allowed number of requests per unit of time. |

### DELETE
<a name="domainnames-domainname-apimappings-apimappingiddelete"></a>

**Operation ID:** `DeleteApiMapping`

Deletes an API mapping.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{apiMappingId}} | String | True | The API mapping identifier. |
| {{domainName}} | String | True | The domain name. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 204 | None | The request has succeeded, and there is no additional content to send in the response payload body. |
| 400 | BadRequestException | One of the parameters in the request is invalid. |
| 404 | NotFoundException | The resource specified in the request was not found. |
| 429 | LimitExceededException | The client is sending more than the allowed number of requests per unit of time. |

### PATCH
<a name="domainnames-domainname-apimappings-apimappingidpatch"></a>

**Operation ID:** `UpdateApiMapping`

The API mapping.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{apiMappingId}} | String | True | The API mapping identifier. |
| {{domainName}} | String | True | The domain name. |

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| apiId | String | True | The identifier of the API. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | ApiMapping | Success |
| 400 | BadRequestException | One of the parameters in the request is invalid. |
| 404 | NotFoundException | The resource specified in the request was not found. |
| 409 | ConflictException | The resource already exists. |
| 429 | LimitExceededException | The client is sending more than the allowed number of requests per unit of time. |

## Schemas
<a name="domainnames-domainname-apimappings-apimappingid-schemas"></a>

### Request bodies
<a name="domainnames-domainname-apimappings-apimappingid-request-examples"></a>

#### PATCH schema
<a name="domainnames-domainname-apimappings-apimappingid-request-body-patch-example"></a>

```
{
  "apiMappingKey": "string",
  "apiId": "string",
  "stage": "string"
}
```

### Response bodies
<a name="domainnames-domainname-apimappings-apimappingid-response-examples"></a>

#### ApiMapping schema
<a name="domainnames-domainname-apimappings-apimappingid-response-body-apimapping-example"></a>

```
{
  "apiMappingId": "string",
  "apiMappingKey": "string",
  "apiId": "string",
  "stage": "string"
}
```

#### BadRequestException schema
<a name="domainnames-domainname-apimappings-apimappingid-response-body-badrequestexception-example"></a>

```
{
  "message": "string"
}
```

#### NotFoundException schema
<a name="domainnames-domainname-apimappings-apimappingid-response-body-notfoundexception-example"></a>

```
{
  "message": "string",
  "resourceType": "string"
}
```

#### ConflictException schema
<a name="domainnames-domainname-apimappings-apimappingid-response-body-conflictexception-example"></a>

```
{
  "message": "string"
}
```

#### LimitExceededException schema
<a name="domainnames-domainname-apimappings-apimappingid-response-body-limitexceededexception-example"></a>

```
{
  "message": "string",
  "limitType": "string"
}
```

## Properties
<a name="domainnames-domainname-apimappings-apimappingid-properties"></a>

### ApiMapping
<a name="domainnames-domainname-apimappings-apimappingid-model-apimapping"></a>

Represents an API mapping.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| apiId | string | True | The API identifier. |
| apiMappingId | string | False | The API mapping identifier. |
| apiMappingKey | string | False | The API mapping key. |
| stage | string | True | The API stage. |

### BadRequestException
<a name="domainnames-domainname-apimappings-apimappingid-model-badrequestexception"></a>

The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Describes the error encountered. |

### ConflictException
<a name="domainnames-domainname-apimappings-apimappingid-model-conflictexception"></a>

The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Describes the error encountered. |

### LimitExceededException
<a name="domainnames-domainname-apimappings-apimappingid-model-limitexceededexception"></a>

A limit has been exceeded. See the accompanying error message for details.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| limitType | string | False | The limit type. |
| message | string | False | Describes the error encountered. |

### NotFoundException
<a name="domainnames-domainname-apimappings-apimappingid-model-notfoundexception"></a>

The resource specified in the request was not found. See the `message` field for more information.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Describes the error encountered. |
| resourceType | string | False | The resource type. |

### UpdateApiMappingInput
<a name="domainnames-domainname-apimappings-apimappingid-model-updateapimappinginput"></a>

Represents the input parameters for an `UpdateApiMapping` request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| apiId | string | False | The API identifier. |
| apiMappingKey | string | False | The API mapping key. |
| stage | string | False | The API stage. |

## See also
<a name="domainnames-domainname-apimappings-apimappingid-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### GetApiMapping
<a name="GetApiMapping-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/apigatewayv2-2018-11-29/GetApiMapping)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/apigatewayv2-2018-11-29/GetApiMapping)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/apigatewayv2-2018-11-29/GetApiMapping)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/apigatewayv2-2018-11-29/GetApiMapping)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/apigatewayv2-2018-11-29/GetApiMapping)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/apigatewayv2-2018-11-29/GetApiMapping)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/apigatewayv2-2018-11-29/GetApiMapping)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/apigatewayv2-2018-11-29/GetApiMapping)
+ [AWS SDK for Python (Boto3)](/goto/boto3/apigatewayv2-2018-11-29/GetApiMapping)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/apigatewayv2-2018-11-29/GetApiMapping)

### DeleteApiMapping
<a name="DeleteApiMapping-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/apigatewayv2-2018-11-29/DeleteApiMapping)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/apigatewayv2-2018-11-29/DeleteApiMapping)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/apigatewayv2-2018-11-29/DeleteApiMapping)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/apigatewayv2-2018-11-29/DeleteApiMapping)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/apigatewayv2-2018-11-29/DeleteApiMapping)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/apigatewayv2-2018-11-29/DeleteApiMapping)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/apigatewayv2-2018-11-29/DeleteApiMapping)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/apigatewayv2-2018-11-29/DeleteApiMapping)
+ [AWS SDK for Python (Boto3)](/goto/boto3/apigatewayv2-2018-11-29/DeleteApiMapping)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/apigatewayv2-2018-11-29/DeleteApiMapping)

### UpdateApiMapping
<a name="UpdateApiMapping-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/apigatewayv2-2018-11-29/UpdateApiMapping)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/apigatewayv2-2018-11-29/UpdateApiMapping)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/apigatewayv2-2018-11-29/UpdateApiMapping)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/apigatewayv2-2018-11-29/UpdateApiMapping)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/apigatewayv2-2018-11-29/UpdateApiMapping)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/apigatewayv2-2018-11-29/UpdateApiMapping)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/apigatewayv2-2018-11-29/UpdateApiMapping)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/apigatewayv2-2018-11-29/UpdateApiMapping)
+ [AWS SDK for Python (Boto3)](/goto/boto3/apigatewayv2-2018-11-29/UpdateApiMapping)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/apigatewayv2-2018-11-29/UpdateApiMapping)
