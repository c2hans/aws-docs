---
source_url: https://docs.aws.amazon.com/apigatewayv2/latest/api-reference/portals-portalid.html
---

# Portal
<a name="portals-portalid"></a>

Represents a portal.

## URI
<a name="portals-portalid-url"></a>

`/v2/portals/{{portalId}}`

## HTTP methods
<a name="portals-portalid-http-methods"></a>

### GET
<a name="portals-portalidget"></a>

**Operation ID:** `GetPortal`

Gets a portal.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{portalId}} | String | True | The portal identifier. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | GetPortalResponseContent | Success |
| 400 | BadRequestExceptionResponseContent | One of the parameters in the request is invalid. |
| 403 | AccessDeniedExceptionResponseContent | 403 response |
| 404 | NotFoundExceptionResponseContent | The resource specified in the request was not found. |
| 429 | LimitExceededExceptionResponseContent | The client is sending more than the allowed number of requests per unit of time. |

### DELETE
<a name="portals-portaliddelete"></a>

**Operation ID:** `DeletePortal`

Deletes a portal.

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
| 429 | LimitExceededExceptionResponseContent | The client is sending more than the allowed number of requests per unit of time. |

### PATCH
<a name="portals-portalidpatch"></a>

**Operation ID:** `UpdatePortal`

Updates a portal.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{portalId}} | String | True | The portal identifier. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | UpdatePortalResponseContent | 200 response |
| 400 | BadRequestExceptionResponseContent | One of the parameters in the request is invalid. |
| 403 | AccessDeniedExceptionResponseContent | 403 response |
| 404 | NotFoundExceptionResponseContent | The resource specified in the request was not found. |
| 409 | ConflictExceptionResponseContent | The resource already exists. |
| 429 | LimitExceededExceptionResponseContent | The client is sending more than the allowed number of requests per unit of time. |

## Schemas
<a name="portals-portalid-schemas"></a>

### Request bodies
<a name="portals-portalid-request-examples"></a>

#### PATCH schema
<a name="portals-portalid-request-body-patch-example"></a>

```
{
  "authorization": {
    "cognitoConfig": {
      "userPoolArn": "string",
      "userPoolDomain": "string",
      "appClientId": "string"
    },
    "none": {
    }
  },
  "portalContent": {
    "displayName": "string",
    "description": "string",
    "theme": {
      "logoLastUploaded": "string",
      "customColors": {
        "errorValidationColor": "string",
        "headerColor": "string",
        "backgroundColor": "string",
        "accentColor": "string",
        "navigationColor": "string",
        "textColor": "string"
      }
    }
  },
  "endpointConfiguration": {
    "acmManaged": {
      "certificateArn": "string",
      "domainName": "string"
    },
    "none": {
    }
  },
  "logoUri": "string",
  "includedPortalProductArns": [
    "string"
  ],
  "rumAppMonitorName": "string"
}
```

### Response bodies
<a name="portals-portalid-response-examples"></a>

#### GetPortalResponseContent schema
<a name="portals-portalid-response-body-getportalresponsecontent-example"></a>

```
{
  "preview": {
    "previewUrl": "string",
    "statusException": {
      "exception": "string",
      "message": "string"
    },
    "previewStatus": enum
  },
  "statusException": {
    "exception": "string",
    "message": "string"
  },
  "portalArn": "string",
  "lastPublished": "string",
  "rumAppMonitorName": "string",
  "tags": {
  },
  "authorization": {
    "cognitoConfig": {
      "userPoolArn": "string",
      "userPoolDomain": "string",
      "appClientId": "string"
    },
    "none": {
    }
  },
  "portalId": "string",
  "endpointConfiguration": {
    "certificateArn": "string",
    "domainName": "string",
    "portalDefaultDomainName": "string",
    "portalDomainHostedZoneId": "string"
  },
  "portalContent": {
    "displayName": "string",
    "description": "string",
    "theme": {
      "logoLastUploaded": "string",
      "customColors": {
        "errorValidationColor": "string",
        "headerColor": "string",
        "backgroundColor": "string",
        "accentColor": "string",
        "navigationColor": "string",
        "textColor": "string"
      }
    }
  },
  "lastPublishedDescription": "string",
  "lastModified": "string",
  "includedPortalProductArns": [
    "string"
  ],
  "publishStatus": enum
}
```

#### UpdatePortalResponseContent schema
<a name="portals-portalid-response-body-updateportalresponsecontent-example"></a>

```
{
  "preview": {
    "previewUrl": "string",
    "statusException": {
      "exception": "string",
      "message": "string"
    },
    "previewStatus": enum
  },
  "statusException": {
    "exception": "string",
    "message": "string"
  },
  "portalArn": "string",
  "lastPublished": "string",
  "rumAppMonitorName": "string",
  "tags": {
  },
  "authorization": {
    "cognitoConfig": {
      "userPoolArn": "string",
      "userPoolDomain": "string",
      "appClientId": "string"
    },
    "none": {
    }
  },
  "portalId": "string",
  "endpointConfiguration": {
    "certificateArn": "string",
    "domainName": "string",
    "portalDefaultDomainName": "string",
    "portalDomainHostedZoneId": "string"
  },
  "portalContent": {
    "displayName": "string",
    "description": "string",
    "theme": {
      "logoLastUploaded": "string",
      "customColors": {
        "errorValidationColor": "string",
        "headerColor": "string",
        "backgroundColor": "string",
        "accentColor": "string",
        "navigationColor": "string",
        "textColor": "string"
      }
    }
  },
  "lastPublishedDescription": "string",
  "lastModified": "string",
  "includedPortalProductArns": [
    "string"
  ],
  "publishStatus": enum
}
```

#### BadRequestExceptionResponseContent schema
<a name="portals-portalid-response-body-badrequestexceptionresponsecontent-example"></a>

```
{
  "message": "string"
}
```

#### AccessDeniedExceptionResponseContent schema
<a name="portals-portalid-response-body-accessdeniedexceptionresponsecontent-example"></a>

```
{
  "message": "string"
}
```

#### NotFoundExceptionResponseContent schema
<a name="portals-portalid-response-body-notfoundexceptionresponsecontent-example"></a>

```
{
  "message": "string",
  "resourceType": "string"
}
```

#### ConflictExceptionResponseContent schema
<a name="portals-portalid-response-body-conflictexceptionresponsecontent-example"></a>

```
{
  "message": "string"
}
```

#### LimitExceededExceptionResponseContent schema
<a name="portals-portalid-response-body-limitexceededexceptionresponsecontent-example"></a>

```
{
  "message": "string",
  "limitType": "string"
}
```

## Properties
<a name="portals-portalid-properties"></a>

### ACMManaged
<a name="portals-portalid-model-acmmanaged"></a>

Represents a domain name and certificate for a portal.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| certificateArn | string<br />MinLength: 10<br />MaxLength: 2048 | True | The certificate ARN. |
| domainName | string<br />MinLength: 3<br />MaxLength: 256 | True | The domain name. |

### AccessDeniedExceptionResponseContent
<a name="portals-portalid-model-accessdeniedexceptionresponsecontent"></a>

The error message.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The message. |

### Authorization
<a name="portals-portalid-model-authorization"></a>

Represents an authorization configuration for a portal.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| cognitoConfig | [CognitoConfig](#portals-portalid-model-cognitoconfig) | False | The Amazon Cognito configuration. |
| none | [None](#portals-portalid-model-none) | False | Provide no authorization for your portal. This makes your portal publicly accesible on the web. |

### BadRequestExceptionResponseContent
<a name="portals-portalid-model-badrequestexceptionresponsecontent"></a>

The response content for bad request exception.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The message of the bad request exception response content. |

### CognitoConfig
<a name="portals-portalid-model-cognitoconfig"></a>

The configuration for using Amazon Cognito user pools to control access to your portal.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| appClientId | string<br />MinLength: 1<br />MaxLength: 256 | True | The app client ID. |
| userPoolArn | string<br />MinLength: 20<br />MaxLength: 2048 | True | The user pool ARN. |
| userPoolDomain | string<br />MinLength: 20<br />MaxLength: 2048 | True | The user pool domain. |

### ConflictExceptionResponseContent
<a name="portals-portalid-model-conflictexceptionresponsecontent"></a>

The resource identifier.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The error message. |

### CustomColors
<a name="portals-portalid-model-customcolors"></a>

Represents custom colors for a published portal.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| accentColor | string<br />MinLength: 1<br />MaxLength: 16 | True | Represents the accent color. |
| backgroundColor | string<br />MinLength: 1<br />MaxLength: 16 | True | Represents the background color. |
| errorValidationColor | string<br />MinLength: 1<br />MaxLength: 16 | True | The errorValidationColor. |
| headerColor | string<br />MinLength: 1<br />MaxLength: 16 | True | Represents the header color. |
| navigationColor | string<br />MinLength: 1<br />MaxLength: 16 | True | Represents the navigation color. |
| textColor | string<br />MinLength: 1<br />MaxLength: 16 | True | Represents the text color. |

### EndpointConfigurationRequest
<a name="portals-portalid-model-endpointconfigurationrequest"></a>

Represents an endpoint configuration.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| acmManaged | [ACMManaged](#portals-portalid-model-acmmanaged) | False | Represents a domain name and certificate for a portal. |
| none | [None](#portals-portalid-model-none) | False | Use the default portal domain name that is generated and managed by API Gateway.  |

### EndpointConfigurationResponse
<a name="portals-portalid-model-endpointconfigurationresponse"></a>

Represents an endpoint configuration.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| certificateArn | string<br />MinLength: 10<br />MaxLength: 2048 | False | The ARN of the ACM certificate. |
| domainName | string<br />MinLength: 3<br />MaxLength: 256 | False | The domain name. |
| portalDefaultDomainName | string<br />MinLength: 3<br />MaxLength: 256 | True | The portal default domain name. This domain name is generated and managed by API Gateway. |
| portalDomainHostedZoneId | string<br />MinLength: 1<br />MaxLength: 64 | True | The portal domain hosted zone identifier. |

### GetPortalResponseContent
<a name="portals-portalid-model-getportalresponsecontent"></a>

Gets a portal.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| authorization | [Authorization](#portals-portalid-model-authorization) | True | The authorization for the portal. |
| endpointConfiguration | [EndpointConfigurationResponse](#portals-portalid-model-endpointconfigurationresponse) | True | The endpoint configuration. |
| includedPortalProductArns | Array of type string<br />MinLength: 20<br />MaxLength: 2048 | True | The ARNs of the portal products included in the portal. |
| lastModified | string<br />Format: date-time | True | The timestamp when the portal was last modified. |
| lastPublished | string<br />Format: date-time | False | The timestamp when the portal was last published. |
| lastPublishedDescription | string<br />MinLength: 0<br />MaxLength: 1024 | False | The publish description used when the portal was last published. |
| portalArn | string<br />MinLength: 20<br />MaxLength: 2048 | True | The ARN of the portal. |
| portalContent | [PortalContent](#portals-portalid-model-portalcontent) | True | Contains the content that is visible to portal consumers including the themes, display names, and description. |
| portalId | string<br />Pattern: `^[a-z0-9]+$`<br />MinLength: 10<br />MaxLength: 30 | True | The portal identifier. |
| preview | [Preview](#portals-portalid-model-preview) | False | Represents the preview endpoint and the any possible error messages during preview generation. |
| publishStatus | [PublishStatus](#portals-portalid-model-publishstatus) | False | The publish status of a portal. |
| rumAppMonitorName | string<br />MinLength: 0<br />MaxLength: 255 | False | The CloudWatch RUM app monitor name. |
| statusException | [StatusException](#portals-portalid-model-statusexception) | False | The status exception information. |
| tags | [Tags](#portals-portalid-model-tags) | False | The collection of tags. Each tag element is associated with a given resource. |

### LimitExceededExceptionResponseContent
<a name="portals-portalid-model-limitexceededexceptionresponsecontent"></a>

The response content for limit exceeded exception.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| limitType | string | False | The limit type of the limit exceeded exception response content. |
| message | string | False | The message of the limit exceeded exception response content. |

### None
<a name="portals-portalid-model-none"></a>

The none option.

### NotFoundExceptionResponseContent
<a name="portals-portalid-model-notfoundexceptionresponsecontent"></a>

The response content for not found exception.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The message of the not found exception response content. |
| resourceType | string | False | The resource type of the not found exception response content. |

### PortalContent
<a name="portals-portalid-model-portalcontent"></a>

Contains the content that is visible to portal consumers including the themes, display names, and description.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| description | string<br />MinLength: 0<br />MaxLength: 1024 | False | A description of the portal. |
| displayName | string<br />MinLength: 3<br />MaxLength: 255 | True | The display name for the portal. |
| theme | [PortalTheme](#portals-portalid-model-portaltheme) | True | The theme for the portal. |

### PortalTheme
<a name="portals-portalid-model-portaltheme"></a>

Defines the theme for a portal.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| customColors | [CustomColors](#portals-portalid-model-customcolors) | True | Defines custom color values. |
| logoLastUploaded | string<br />Format: date-time | False | The timestamp when the logo was last uploaded. |

### Preview
<a name="portals-portalid-model-preview"></a>

Contains the preview status and preview URL.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| previewStatus | [PreviewStatus](#portals-portalid-model-previewstatus) | True | The status of the preview. |
| previewUrl | string | False | The URL of the preview. |
| statusException | [StatusException](#portals-portalid-model-statusexception) | False | The status exception information. |

### PreviewStatus
<a name="portals-portalid-model-previewstatus"></a>

Represents the preview status.
+ `PREVIEW_IN_PROGRESS`
+ `PREVIEW_FAILED`
+ `PREVIEW_READY`

### PublishStatus
<a name="portals-portalid-model-publishstatus"></a>

Represents a publish status.
+ `PUBLISHED`
+ `PUBLISH_IN_PROGRESS`
+ `PUBLISH_FAILED`
+ `DISABLED`

### StatusException
<a name="portals-portalid-model-statusexception"></a>

Represents a StatusException.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| exception | string<br />MinLength: 1<br />MaxLength: 256 | False | The exception. |
| message | string<br />MinLength: 1<br />MaxLength: 2048 | False | The error message. |

### Tags
<a name="portals-portalid-model-tags"></a>

Represents a collection of tags associated with the resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| `*` | string | False |  |

### UpdatePortalRequestContent
<a name="portals-portalid-model-updateportalrequestcontent"></a>

Updates a portal.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| authorization | [Authorization](#portals-portalid-model-authorization) | False | The authorization of the portal. |
| endpointConfiguration | [EndpointConfigurationRequest](#portals-portalid-model-endpointconfigurationrequest) | False | Represents an endpoint configuration. |
| includedPortalProductArns | Array of type string<br />MinLength: 20<br />MaxLength: 2048 | False | The ARNs of the portal products included in the portal. |
| logoUri | string<br />MinLength: 0<br />MaxLength: 1092 | False | The logo URI. |
| portalContent | [PortalContent](#portals-portalid-model-portalcontent) | False | Contains the content that is visible to portal consumers including the themes, display names, and description. |
| rumAppMonitorName | string<br />MinLength: 0<br />MaxLength: 255 | False | The CloudWatch RUM app monitor name. |

### UpdatePortalResponseContent
<a name="portals-portalid-model-updateportalresponsecontent"></a>

Updates a portal.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| authorization | [Authorization](#portals-portalid-model-authorization) | True | The authorization for the portal. |
| endpointConfiguration | [EndpointConfigurationResponse](#portals-portalid-model-endpointconfigurationresponse) | True | The endpoint configuration. |
| includedPortalProductArns | Array of type string<br />MinLength: 20<br />MaxLength: 2048 | True | The ARNs of the portal products included in the portal. |
| lastModified | string<br />Format: date-time | True | The timestamp when the portal was last modified. |
| lastPublished | string<br />Format: date-time | False | The timestamp when the portal was last published. |
| lastPublishedDescription | string<br />MinLength: 0<br />MaxLength: 1024 | False | The description associated with the last time the portal was published. |
| portalArn | string<br />MinLength: 20<br />MaxLength: 2048 | True | The ARN of the portal. |
| portalContent | [PortalContent](#portals-portalid-model-portalcontent) | True | Contains the content that is visible to portal consumers including the themes, display names, and description. |
| portalId | string<br />Pattern: `^[a-z0-9]+$`<br />MinLength: 10<br />MaxLength: 30 | True | The portal identifier. |
| preview | [Preview](#portals-portalid-model-preview) | False | Represents the preview endpoint and the any possible error messages during preview generation. |
| publishStatus | [PublishStatus](#portals-portalid-model-publishstatus) | False | The publishStatus. |
| rumAppMonitorName | string<br />MinLength: 0<br />MaxLength: 255 | False | The CloudWatch RUM app monitor name. |
| statusException | [StatusException](#portals-portalid-model-statusexception) | False | The status exception information. |
| tags | [Tags](#portals-portalid-model-tags) | False | The collection of tags. Each tag element is associated with a given resource. |

## See also
<a name="portals-portalid-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### GetPortal
<a name="GetPortal-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/apigatewayv2-2018-11-29/GetPortal)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/apigatewayv2-2018-11-29/GetPortal)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/apigatewayv2-2018-11-29/GetPortal)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/apigatewayv2-2018-11-29/GetPortal)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/apigatewayv2-2018-11-29/GetPortal)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/apigatewayv2-2018-11-29/GetPortal)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/apigatewayv2-2018-11-29/GetPortal)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/apigatewayv2-2018-11-29/GetPortal)
+ [AWS SDK for Python (Boto3)](/goto/boto3/apigatewayv2-2018-11-29/GetPortal)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/apigatewayv2-2018-11-29/GetPortal)

### DeletePortal
<a name="DeletePortal-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/apigatewayv2-2018-11-29/DeletePortal)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/apigatewayv2-2018-11-29/DeletePortal)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/apigatewayv2-2018-11-29/DeletePortal)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/apigatewayv2-2018-11-29/DeletePortal)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/apigatewayv2-2018-11-29/DeletePortal)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/apigatewayv2-2018-11-29/DeletePortal)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/apigatewayv2-2018-11-29/DeletePortal)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/apigatewayv2-2018-11-29/DeletePortal)
+ [AWS SDK for Python (Boto3)](/goto/boto3/apigatewayv2-2018-11-29/DeletePortal)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/apigatewayv2-2018-11-29/DeletePortal)

### UpdatePortal
<a name="UpdatePortal-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/apigatewayv2-2018-11-29/UpdatePortal)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/apigatewayv2-2018-11-29/UpdatePortal)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/apigatewayv2-2018-11-29/UpdatePortal)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/apigatewayv2-2018-11-29/UpdatePortal)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/apigatewayv2-2018-11-29/UpdatePortal)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/apigatewayv2-2018-11-29/UpdatePortal)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/apigatewayv2-2018-11-29/UpdatePortal)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/apigatewayv2-2018-11-29/UpdatePortal)
+ [AWS SDK for Python (Boto3)](/goto/boto3/apigatewayv2-2018-11-29/UpdatePortal)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/apigatewayv2-2018-11-29/UpdatePortal)
