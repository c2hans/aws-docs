---
source_url: https://docs.aws.amazon.com/apigatewayv2/latest/api-reference/portalproducts-portalproductid-sharingpolicy.html
---

# Sharing policy
<a name="portalproducts-portalproductid-sharingpolicy"></a>

Represents the sharing policy for a portal product.

## URI
<a name="portalproducts-portalproductid-sharingpolicy-url"></a>

`/v2/portalproducts/{{portalProductId}}/sharingpolicy`

## HTTP methods
<a name="portalproducts-portalproductid-sharingpolicy-http-methods"></a>

### GET
<a name="portalproducts-portalproductid-sharingpolicyget"></a>

**Operation ID:** `GetPortalProductSharingPolicy`

Gets the sharing policy for a portal product.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{portalProductId}} | String | True | The portal product identifier. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | GetPortalProductSharingPolicyResponseContent | Success |
| 400 | BadRequestExceptionResponseContent | One of the parameters in the request is invalid. |
| 403 | AccessDeniedExceptionResponseContent | 403 response |
| 404 | NotFoundExceptionResponseContent | The resource specified in the request was not found. |
| 429 | LimitExceededExceptionResponseContent | The client is sending more than the allowed number of requests per unit of time. |

### PUT
<a name="portalproducts-portalproductid-sharingpolicyput"></a>

**Operation ID:** `PutPortalProductSharingPolicy`

Updates the sharing policy for a portal product.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{portalProductId}} | String | True | The portal product identifier. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | 200 response |
| 400 | BadRequestExceptionResponseContent | One of the parameters in the request is invalid. |
| 403 | AccessDeniedExceptionResponseContent | 403 response |
| 404 | NotFoundExceptionResponseContent | The resource specified in the request was not found. |
| 429 | LimitExceededExceptionResponseContent | The client is sending more than the allowed number of requests per unit of time. |

### DELETE
<a name="portalproducts-portalproductid-sharingpolicydelete"></a>

**Operation ID:** `DeletePortalProductSharingPolicy`

Deletes the sharing policy for a portal product.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{portalProductId}} | String | True | The portal product identifier. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 204 | None | The request has succeeded, and there is no additional content to send in the response payload body. |
| 400 | BadRequestExceptionResponseContent | One of the parameters in the request is invalid. |
| 403 | AccessDeniedExceptionResponseContent | 403 response |
| 404 | NotFoundExceptionResponseContent | The resource specified in the request was not found. |
| 429 | LimitExceededExceptionResponseContent | The client is sending more than the allowed number of requests per unit of time. |

## Schemas
<a name="portalproducts-portalproductid-sharingpolicy-schemas"></a>

### Request bodies
<a name="portalproducts-portalproductid-sharingpolicy-request-examples"></a>

#### PUT schema
<a name="portalproducts-portalproductid-sharingpolicy-request-body-put-example"></a>

```
{
  "policyDocument": "string"
}
```

### Response bodies
<a name="portalproducts-portalproductid-sharingpolicy-response-examples"></a>

#### GetPortalProductSharingPolicyResponseContent schema
<a name="portalproducts-portalproductid-sharingpolicy-response-body-getportalproductsharingpolicyresponsecontent-example"></a>

```
{
  "policyDocument": "string",
  "portalProductId": "string"
}
```

#### BadRequestExceptionResponseContent schema
<a name="portalproducts-portalproductid-sharingpolicy-response-body-badrequestexceptionresponsecontent-example"></a>

```
{
  "message": "string"
}
```

#### AccessDeniedExceptionResponseContent schema
<a name="portalproducts-portalproductid-sharingpolicy-response-body-accessdeniedexceptionresponsecontent-example"></a>

```
{
  "message": "string"
}
```

#### NotFoundExceptionResponseContent schema
<a name="portalproducts-portalproductid-sharingpolicy-response-body-notfoundexceptionresponsecontent-example"></a>

```
{
  "message": "string",
  "resourceType": "string"
}
```

#### LimitExceededExceptionResponseContent schema
<a name="portalproducts-portalproductid-sharingpolicy-response-body-limitexceededexceptionresponsecontent-example"></a>

```
{
  "message": "string",
  "limitType": "string"
}
```

## Properties
<a name="portalproducts-portalproductid-sharingpolicy-properties"></a>

### AccessDeniedExceptionResponseContent
<a name="portalproducts-portalproductid-sharingpolicy-model-accessdeniedexceptionresponsecontent"></a>

The error message.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The message. |

### BadRequestExceptionResponseContent
<a name="portalproducts-portalproductid-sharingpolicy-model-badrequestexceptionresponsecontent"></a>

The response content for bad request exception.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The message of the bad request exception response content. |

### GetPortalProductSharingPolicyResponseContent
<a name="portalproducts-portalproductid-sharingpolicy-model-getportalproductsharingpolicyresponsecontent"></a>

Gets a product sharing policy.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| policyDocument | string<br />MinLength: 1<br />MaxLength: 307200 | True | The product sharing policy. |
| portalProductId | string<br />Pattern: `^[a-z0-9]+$`<br />MinLength: 10<br />MaxLength: 30 | True | The portal product identifier. |

### LimitExceededExceptionResponseContent
<a name="portalproducts-portalproductid-sharingpolicy-model-limitexceededexceptionresponsecontent"></a>

The response content for limit exceeded exception.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| limitType | string | False | The limit type of the limit exceeded exception response content. |
| message | string | False | The message of the limit exceeded exception response content. |

### NotFoundExceptionResponseContent
<a name="portalproducts-portalproductid-sharingpolicy-model-notfoundexceptionresponsecontent"></a>

The response content for not found exception.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The message of the not found exception response content. |
| resourceType | string | False | The resource type of the not found exception response content. |

### PutPortalProductSharingPolicyRequestContent
<a name="portalproducts-portalproductid-sharingpolicy-model-putportalproductsharingpolicyrequestcontent"></a>

The request content.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| policyDocument | string<br />MinLength: 1<br />MaxLength: 307200 | True | The product sharing policy. |

## See also
<a name="portalproducts-portalproductid-sharingpolicy-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### GetPortalProductSharingPolicy
<a name="GetPortalProductSharingPolicy-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/apigatewayv2-2018-11-29/GetPortalProductSharingPolicy)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/apigatewayv2-2018-11-29/GetPortalProductSharingPolicy)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/apigatewayv2-2018-11-29/GetPortalProductSharingPolicy)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/apigatewayv2-2018-11-29/GetPortalProductSharingPolicy)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/apigatewayv2-2018-11-29/GetPortalProductSharingPolicy)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/apigatewayv2-2018-11-29/GetPortalProductSharingPolicy)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/apigatewayv2-2018-11-29/GetPortalProductSharingPolicy)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/apigatewayv2-2018-11-29/GetPortalProductSharingPolicy)
+ [AWS SDK for Python (Boto3)](/goto/boto3/apigatewayv2-2018-11-29/GetPortalProductSharingPolicy)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/apigatewayv2-2018-11-29/GetPortalProductSharingPolicy)

### PutPortalProductSharingPolicy
<a name="PutPortalProductSharingPolicy-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/apigatewayv2-2018-11-29/PutPortalProductSharingPolicy)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/apigatewayv2-2018-11-29/PutPortalProductSharingPolicy)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/apigatewayv2-2018-11-29/PutPortalProductSharingPolicy)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/apigatewayv2-2018-11-29/PutPortalProductSharingPolicy)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/apigatewayv2-2018-11-29/PutPortalProductSharingPolicy)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/apigatewayv2-2018-11-29/PutPortalProductSharingPolicy)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/apigatewayv2-2018-11-29/PutPortalProductSharingPolicy)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/apigatewayv2-2018-11-29/PutPortalProductSharingPolicy)
+ [AWS SDK for Python (Boto3)](/goto/boto3/apigatewayv2-2018-11-29/PutPortalProductSharingPolicy)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/apigatewayv2-2018-11-29/PutPortalProductSharingPolicy)

### DeletePortalProductSharingPolicy
<a name="DeletePortalProductSharingPolicy-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/apigatewayv2-2018-11-29/DeletePortalProductSharingPolicy)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/apigatewayv2-2018-11-29/DeletePortalProductSharingPolicy)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/apigatewayv2-2018-11-29/DeletePortalProductSharingPolicy)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/apigatewayv2-2018-11-29/DeletePortalProductSharingPolicy)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/apigatewayv2-2018-11-29/DeletePortalProductSharingPolicy)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/apigatewayv2-2018-11-29/DeletePortalProductSharingPolicy)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/apigatewayv2-2018-11-29/DeletePortalProductSharingPolicy)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/apigatewayv2-2018-11-29/DeletePortalProductSharingPolicy)
+ [AWS SDK for Python (Boto3)](/goto/boto3/apigatewayv2-2018-11-29/DeletePortalProductSharingPolicy)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/apigatewayv2-2018-11-29/DeletePortalProductSharingPolicy)
