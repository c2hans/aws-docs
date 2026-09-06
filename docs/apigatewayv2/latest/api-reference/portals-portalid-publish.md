---
source_url: https://docs.aws.amazon.com/apigatewayv2/latest/api-reference/portals-portalid-publish.html
---

# Publish
<a name="portals-portalid-publish"></a>

Represents publishing a portal.

## URI
<a name="portals-portalid-publish-url"></a>

`/v2/portals/{{portalId}}/publish`

## HTTP methods
<a name="portals-portalid-publish-http-methods"></a>

### POST
<a name="portals-portalid-publishpost"></a>

**Operation ID:** `PublishPortal`

Publishes a portal.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{portalId}} | String | True | The portal identifier. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 202 | None | 202 response |
| 400 | BadRequestExceptionResponseContent | One of the parameters in the request is invalid. |
| 403 | AccessDeniedExceptionResponseContent | 403 response |
| 404 | NotFoundExceptionResponseContent | The resource specified in the request was not found. |
| 409 | ConflictExceptionResponseContent | The resource already exists. |
| 429 | LimitExceededExceptionResponseContent | The client is sending more than the allowed number of requests per unit of time. |

### DELETE
<a name="portals-portalid-publishdelete"></a>

**Operation ID:** `DisablePortal`

Deletes the publication of a portal portal.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{portalId}} | String | True | The portal identifier. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 204 | None | The request has succeeded, and there is no additional content to send in the response payload body. |
| 400 | BadRequestExceptionResponseContent | One of the parameters in the request is invalid. |
| 403 | AccessDeniedExceptionResponseContent | 403 response |
| 404 | NotFoundExceptionResponseContent | The resource specified in the request was not found. |
| 409 | ConflictExceptionResponseContent | The resource already exists. |
| 429 | LimitExceededExceptionResponseContent | The client is sending more than the allowed number of requests per unit of time. |

## Schemas
<a name="portals-portalid-publish-schemas"></a>

### Request bodies
<a name="portals-portalid-publish-request-examples"></a>

#### POST schema
<a name="portals-portalid-publish-request-body-post-example"></a>

```
{
  "description": "string"
}
```

### Response bodies
<a name="portals-portalid-publish-response-examples"></a>

#### BadRequestExceptionResponseContent schema
<a name="portals-portalid-publish-response-body-badrequestexceptionresponsecontent-example"></a>

```
{
  "message": "string"
}
```

#### AccessDeniedExceptionResponseContent schema
<a name="portals-portalid-publish-response-body-accessdeniedexceptionresponsecontent-example"></a>

```
{
  "message": "string"
}
```

#### NotFoundExceptionResponseContent schema
<a name="portals-portalid-publish-response-body-notfoundexceptionresponsecontent-example"></a>

```
{
  "message": "string",
  "resourceType": "string"
}
```

#### ConflictExceptionResponseContent schema
<a name="portals-portalid-publish-response-body-conflictexceptionresponsecontent-example"></a>

```
{
  "message": "string"
}
```

#### LimitExceededExceptionResponseContent schema
<a name="portals-portalid-publish-response-body-limitexceededexceptionresponsecontent-example"></a>

```
{
  "message": "string",
  "limitType": "string"
}
```

## Properties
<a name="portals-portalid-publish-properties"></a>

### AccessDeniedExceptionResponseContent
<a name="portals-portalid-publish-model-accessdeniedexceptionresponsecontent"></a>

The error message.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The message. |

### BadRequestExceptionResponseContent
<a name="portals-portalid-publish-model-badrequestexceptionresponsecontent"></a>

The response content for bad request exception.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The message of the bad request exception response content. |

### ConflictExceptionResponseContent
<a name="portals-portalid-publish-model-conflictexceptionresponsecontent"></a>

The resource identifier.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The error message. |

### LimitExceededExceptionResponseContent
<a name="portals-portalid-publish-model-limitexceededexceptionresponsecontent"></a>

The response content for limit exceeded exception.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| limitType | string | False | The limit type of the limit exceeded exception response content. |
| message | string | False | The message of the limit exceeded exception response content. |

### NotFoundExceptionResponseContent
<a name="portals-portalid-publish-model-notfoundexceptionresponsecontent"></a>

The response content for not found exception.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The message of the not found exception response content. |
| resourceType | string | False | The resource type of the not found exception response content. |

### PublishPortalRequestContent
<a name="portals-portalid-publish-model-publishportalrequestcontent"></a>

Publish a portal.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| description | string<br />MinLength: 0<br />MaxLength: 1024 | False | The description of the portal. When the portal is published, this description becomes the last published description. |

## See also
<a name="portals-portalid-publish-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### PublishPortal
<a name="PublishPortal-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/apigatewayv2-2018-11-29/PublishPortal)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/apigatewayv2-2018-11-29/PublishPortal)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/apigatewayv2-2018-11-29/PublishPortal)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/apigatewayv2-2018-11-29/PublishPortal)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/apigatewayv2-2018-11-29/PublishPortal)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/apigatewayv2-2018-11-29/PublishPortal)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/apigatewayv2-2018-11-29/PublishPortal)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/apigatewayv2-2018-11-29/PublishPortal)
+ [AWS SDK for Python](/goto/boto3/apigatewayv2-2018-11-29/PublishPortal)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/apigatewayv2-2018-11-29/PublishPortal)

### DisablePortal
<a name="DisablePortal-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/apigatewayv2-2018-11-29/DisablePortal)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/apigatewayv2-2018-11-29/DisablePortal)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/apigatewayv2-2018-11-29/DisablePortal)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/apigatewayv2-2018-11-29/DisablePortal)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/apigatewayv2-2018-11-29/DisablePortal)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/apigatewayv2-2018-11-29/DisablePortal)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/apigatewayv2-2018-11-29/DisablePortal)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/apigatewayv2-2018-11-29/DisablePortal)
+ [AWS SDK for Python](/goto/boto3/apigatewayv2-2018-11-29/DisablePortal)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/apigatewayv2-2018-11-29/DisablePortal)
