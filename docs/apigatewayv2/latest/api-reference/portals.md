---
source_url: https://docs.aws.amazon.com/apigatewayv2/latest/api-reference/portals.html
---

# Portals
<a name="portals"></a>

Represents a collection of portals.

## URI
<a name="portals-url"></a>

`/v2/portals`

## HTTP methods
<a name="portals-http-methods"></a>

### GET
<a name="portalsget"></a>

**Operation ID:** `ListPortals`

Lists portals.

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| nextToken | String | False | The next page of elements from this collection. Not valid for the last element of the collection. |
| maxResults | String | False | The maximum number of elements to be returned for this resource. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | ListPortalsResponseContent | Success |
| 400 | BadRequestExceptionResponseContent | One of the parameters in the request is invalid. |
| 403 | AccessDeniedExceptionResponseContent | 403 response |
| 429 | LimitExceededExceptionResponseContent | The client is sending more than the allowed number of requests per unit of time. |

### POST
<a name="portalspost"></a>

**Operation ID:** `CreatePortal`

Creates a portal.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 201 | CreatePortalResponseContent | The request has succeeded and has resulted in the creation of a resource. |
| 400 | BadRequestExceptionResponseContent | One of the parameters in the request is invalid. |
| 403 | AccessDeniedExceptionResponseContent | 403 response |
| 429 | LimitExceededExceptionResponseContent | The client is sending more than the allowed number of requests per unit of time. |

## Schemas
<a name="portals-schemas"></a>

### Request bodies
<a name="portals-request-examples"></a>

#### POST schema
<a name="portals-request-body-post-example"></a>

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
  "rumAppMonitorName": "string",
  "tags": {
  }
}
```

### Response bodies
<a name="portals-response-examples"></a>

#### ListPortalsResponseContent schema
<a name="portals-response-body-listportalsresponsecontent-example"></a>

```
{
  "nextToken": "string",
  "items": [
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
  ]
}
```

#### CreatePortalResponseContent schema
<a name="portals-response-body-createportalresponsecontent-example"></a>

```
{
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
<a name="portals-response-body-badrequestexceptionresponsecontent-example"></a>

```
{
  "message": "string"
}
```

#### AccessDeniedExceptionResponseContent schema
<a name="portals-response-body-accessdeniedexceptionresponsecontent-example"></a>

```
{
  "message": "string"
}
```

#### LimitExceededExceptionResponseContent schema
<a name="portals-response-body-limitexceededexceptionresponsecontent-example"></a>

```
{
  "message": "string",
  "limitType": "string"
}
```

## Properties
<a name="portals-properties"></a>

### ACMManaged
<a name="portals-model-acmmanaged"></a>

Represents a domain name and certificate for a portal.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| certificateArn | string<br />MinLength: 10<br />MaxLength: 2048 | True | The certificate ARN. |
| domainName | string<br />MinLength: 3<br />MaxLength: 256 | True | The domain name. |

### AccessDeniedExceptionResponseContent
<a name="portals-model-accessdeniedexceptionresponsecontent"></a>

The error message.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The message. |

### Authorization
<a name="portals-model-authorization"></a>

Represents an authorization configuration for a portal.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| cognitoConfig | [CognitoConfig](#portals-model-cognitoconfig) | False | The Amazon Cognito configuration. |
| none | [None](#portals-model-none) | False | Provide no authorization for your portal. This makes your portal publicly accesible on the web. |

### BadRequestExceptionResponseContent
<a name="portals-model-badrequestexceptionresponsecontent"></a>

The response content for bad request exception.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | The message of the bad request exception response content. |

### CognitoConfig
<a name="portals-model-cognitoconfig"></a>

The configuration for using Amazon Cognito user pools to control access to your portal.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| appClientId | string<br />MinLength: 1<br />MaxLength: 256 | True | The app client ID. |
| userPoolArn | string<br />MinLength: 20<br />MaxLength: 2048 | True | The user pool ARN. |
| userPoolDomain | string<br />MinLength: 20<br />MaxLength: 2048 | True | The user pool domain. |

### CreatePortalRequestContent
<a name="portals-model-createportalrequestcontent"></a>

Creates a portal.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| authorization | [Authorization](#portals-model-authorization) | True | The authentication configuration for the portal. |
| endpointConfiguration | [EndpointConfigurationRequest](#portals-model-endpointconfigurationrequest) | True | The domain configuration for the portal. Use a default domain provided by API Gateway or provide a fully-qualified domain name that you own. |
| includedPortalProductArns | Array of type string<br />MinLength: 20<br />MaxLength: 2048 | False | The ARNs of the portal products included in the portal. |
| logoUri | string<br />MinLength: 0<br />MaxLength: 1092 | False | The URI for the portal logo image that is displayed in the portal header. |
| portalContent | [PortalContent](#portals-model-portalcontent) | True | The content of the portal. |
| rumAppMonitorName | string<br />MinLength: 0<br />MaxLength: 255 | False | The name of the Amazon CloudWatch RUM app monitor for the portal. |
| tags | [Tags](#portals-model-tags) | False | The collection of tags. Each tag element is associated with a given resource. |

### CreatePortalResponseContent
<a name="portals-model-createportalresponsecontent"></a>

Creates a portal.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| authorization | [Authorization](#portals-model-authorization) | True | The authorization for the portal. Supports Cognito-based user authentication or no authentication. |
| endpointConfiguration | [EndpointConfigurationResponse](#portals-model-endpointconfigurationresponse) | True | The endpoint configuration. |
| includedPortalProductArns | Array of type string<br />MinLength: 20<br />MaxLength: 2048 | True | The ARNs of the portal products included in the portal. |
| lastModified | string<br />Format: date-time | True | The timestamp when the portal configuration was last modified. |
| lastPublished | string<br />Format: date-time | False | The timestamp when the portal was last published. |
| lastPublishedDescription | string<br />MinLength: 0<br />MaxLength: 1024 | False | A user-written description of the changes made in the last published version of the portal. |
| portalArn | string<br />MinLength: 20<br />MaxLength: 2048 | True | The ARN of the portal. |
| portalContent | [PortalContent](#portals-model-portalcontent) | True | The name, description, and theme for the portal. |
| portalId | string<br />Pattern: `^[a-z0-9]+$`<br />MinLength: 10<br />MaxLength: 30 | True | The portal identifier. |
| publishStatus | [PublishStatus](#portals-model-publishstatus) | False | The current publishing status of the portal. |
| rumAppMonitorName | string<br />MinLength: 0<br />MaxLength: 255 | False | The name of the Amazon CloudWatch RUM app monitor. |
| statusException | [StatusException](#portals-model-statusexception) | False | Error information for failed portal operations. Contains details about any issues encountered during portal creation or publishing. |
| tags | [Tags](#portals-model-tags) | False | The collection of tags. Each tag element is associated with a given resource. |

### CustomColors
<a name="portals-model-customcolors"></a>

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
<a name="portals-model-endpointconfigurationrequest"></a>

Represents an endpoint configuration.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| acmManaged | [ACMManaged](#portals-model-acmmanaged) | False | Represents a domain name and certificate for a portal. |
| none | [None](#portals-model-none) | False | Use the default portal domain name that is generated and managed by API Gateway.  |

### EndpointConfigurationResponse
<a name="portals-model-endpointconfigurationresponse"></a>

Represents an endpoint configuration.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| certificateArn | string<br />MinLength: 10<br />MaxLength: 2048 | False | The ARN of the ACM certificate. |
| domainName | string<br />MinLength: 3<br />MaxLength: 256 | False | The domain name. |
| portalDefaultDomainName | string<br />MinLength: 3<br />MaxLength: 256 | True | The portal default domain name. This domain name is generated and managed by API Gateway. |
| portalDomainHostedZoneId | string<br />MinLength: 1<br />MaxLength: 64 | True | The portal domain hosted zone identifier. |

### LimitExceededExceptionResponseContent
<a name="portals-model-limitexceededexceptionresponsecontent"></a>

The response content for limit exceeded exception.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| limitType | string | False | The limit type of the limit exceeded exception response content. |
| message | string | False | The message of the limit exceeded exception response content. |

### ListPortalsResponseContent
<a name="portals-model-listportalsresponsecontent"></a>

Lists portals.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| items | Array of type [PortalSummary](#portals-model-portalsummary) | False | The elements from this collection. |
| nextToken | string<br />MinLength: 1<br />MaxLength: 2048 | False | The next page of elements from this collection. Not valid for the last element of the collection. |

### None
<a name="portals-model-none"></a>

The none option.

### PortalContent
<a name="portals-model-portalcontent"></a>

Contains the content that is visible to portal consumers including the themes, display names, and description.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| description | string<br />MinLength: 0<br />MaxLength: 1024 | False | A description of the portal. |
| displayName | string<br />MinLength: 3<br />MaxLength: 255 | True | The display name for the portal. |
| theme | [PortalTheme](#portals-model-portaltheme) | True | The theme for the portal. |

### PortalSummary
<a name="portals-model-portalsummary"></a>

Represents a portal summary.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| authorization | [Authorization](#portals-model-authorization) | True | The authorization of the portal. |
| endpointConfiguration | [EndpointConfigurationResponse](#portals-model-endpointconfigurationresponse) | True | The endpoint configuration of the portal. |
| includedPortalProductArns | Array of type string<br />MinLength: 20<br />MaxLength: 2048 | True | The ARNs of the portal products included in the portal. |
| lastModified | string<br />Format: date-time | True | The timestamp when the portal was last modified. |
| lastPublished | string<br />Format: date-time | False | The timestamp when the portal was last published. |
| lastPublishedDescription | string<br />MinLength: 0<br />MaxLength: 1024 | False | The description of the portal the last time it was published. |
| portalArn | string<br />MinLength: 20<br />MaxLength: 2048 | True | The ARN of the portal. |
| portalContent | [PortalContent](#portals-model-portalcontent) | True | Contains the content that is visible to portal consumers including the themes, display names, and description. |
| portalId | string<br />Pattern: `^[a-z0-9]+$`<br />MinLength: 10<br />MaxLength: 30 | True | The portal identifier. |
| preview | [Preview](#portals-model-preview) | False | Represents the preview endpoint and the any possible error messages during preview generation. |
| publishStatus | [PublishStatus](#portals-model-publishstatus) | False | The publish status. |
| rumAppMonitorName | string<br />MinLength: 0<br />MaxLength: 255 | False | The CloudWatch RUM app monitor name. |
| statusException | [StatusException](#portals-model-statusexception) | False | The status exception information. |
| tags | [Tags](#portals-model-tags) | False | The collection of tags. Each tag element is associated with a given resource. |

### PortalTheme
<a name="portals-model-portaltheme"></a>

Defines the theme for a portal.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| customColors | [CustomColors](#portals-model-customcolors) | True | Defines custom color values. |
| logoLastUploaded | string<br />Format: date-time | False | The timestamp when the logo was last uploaded. |

### Preview
<a name="portals-model-preview"></a>

Contains the preview status and preview URL.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| previewStatus | [PreviewStatus](#portals-model-previewstatus) | True | The status of the preview. |
| previewUrl | string | False | The URL of the preview. |
| statusException | [StatusException](#portals-model-statusexception) | False | The status exception information. |

### PreviewStatus
<a name="portals-model-previewstatus"></a>

Represents the preview status.
+ `PREVIEW_IN_PROGRESS`
+ `PREVIEW_FAILED`
+ `PREVIEW_READY`

### PublishStatus
<a name="portals-model-publishstatus"></a>

Represents a publish status.
+ `PUBLISHED`
+ `PUBLISH_IN_PROGRESS`
+ `PUBLISH_FAILED`
+ `DISABLED`

### StatusException
<a name="portals-model-statusexception"></a>

Represents a StatusException.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| exception | string<br />MinLength: 1<br />MaxLength: 256 | False | The exception. |
| message | string<br />MinLength: 1<br />MaxLength: 2048 | False | The error message. |

### Tags
<a name="portals-model-tags"></a>

Represents a collection of tags associated with the resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| `*` | string | False |  |

## See also
<a name="portals-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### ListPortals
<a name="ListPortals-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/apigatewayv2-2018-11-29/ListPortals)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/apigatewayv2-2018-11-29/ListPortals)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/apigatewayv2-2018-11-29/ListPortals)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/apigatewayv2-2018-11-29/ListPortals)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/apigatewayv2-2018-11-29/ListPortals)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/apigatewayv2-2018-11-29/ListPortals)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/apigatewayv2-2018-11-29/ListPortals)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/apigatewayv2-2018-11-29/ListPortals)
+ [AWS SDK for Python](/goto/boto3/apigatewayv2-2018-11-29/ListPortals)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/apigatewayv2-2018-11-29/ListPortals)

### CreatePortal
<a name="CreatePortal-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/apigatewayv2-2018-11-29/CreatePortal)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/apigatewayv2-2018-11-29/CreatePortal)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/apigatewayv2-2018-11-29/CreatePortal)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/apigatewayv2-2018-11-29/CreatePortal)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/apigatewayv2-2018-11-29/CreatePortal)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/apigatewayv2-2018-11-29/CreatePortal)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/apigatewayv2-2018-11-29/CreatePortal)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/apigatewayv2-2018-11-29/CreatePortal)
+ [AWS SDK for Python](/goto/boto3/apigatewayv2-2018-11-29/CreatePortal)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/apigatewayv2-2018-11-29/CreatePortal)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon API Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apigatewayv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
