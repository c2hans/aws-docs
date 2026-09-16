---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference/templates-template-name-template-type-active-version.html
---

**End of support notice:** On October 30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints, segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of support](https://docs.aws.amazon.com/console/pinpoint/migration-guide). **Note:** APIs related to SMS, voice, mobile push, OTP, and phone number validate are not impacted by this change and are supported by AWS End User Messaging.

# Active Template Version
<a name="templates-template-name-template-type-active-version"></a>

A *message template* is a set of content and settings that you can define, save, and reuse in email messages, push notifications, SMS text messages, and voice messages for any of your Amazon Pinpoint applications.

To help you develop and maintain templates, Amazon Pinpoint supports versioning for all types of message templates. Each time you update a template, Amazon Pinpoint automatically saves your changes to (overwrites) the latest existing version of the template, unless you choose to create a new version of the template. Each version of a template is a snapshot of the template that you can use in a message.

Of the template versions, you can designate one version as the *active version*. The *active version* is the version that Amazon Pinpoint uses by default for any new messages that are based on the template. Depending on your organization's workflow for managing message templates, the active version is typically the version that's been most recently reviewed and approved for use in messages. It isn't necessarily the latest version of a template. To determine which version of a template is currently the active version, send a GET request to the appropriate resource for the template's type, and omit the `version` query parameter from your request. In response to your request, Amazon Pinpoint returns the version identifier and other information about the active version of the template.

You can use the Active Template Version resource to change the status of a specific version of a template to *active*.

## URI
<a name="templates-template-name-template-type-active-version-url"></a>

`/v1/templates/{{template-name}}/{{template-type}}/active-version`

## HTTP methods
<a name="templates-template-name-template-type-active-version-http-methods"></a>

### PUT
<a name="templates-template-name-template-type-active-versionput"></a>

**Operation ID:** `UpdateTemplateActiveVersion`

Changes the status of a specific version of a message template to *active*.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{template-name}} | String | True | The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (\_), or hyphens (-). Template names are case sensitive. |
| {{template-type}} | String | True | The type of channel that the message template is designed for. Valid values are: `EMAIL`, `PUSH`, `SMS`, and `VOICE`. |

**Header parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| accept | String | False | Indicates which content types, expressed as MIME types, the client understands. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | MessageBody | The request succeeded. |
| 400 | MessageBody | The request contains a syntax error (BadRequestException). |
| 403 | MessageBody | The request was denied because access to the specified resource is forbidden (ForbiddenException). |
| 404 | MessageBody | The request failed because the specified resource was not found (NotFoundException). |
| 405 | MessageBody | The request failed because the method is not allowed for the specified resource (MethodNotAllowedException). |
| 413 | MessageBody | The request failed because the payload for the body of the request is too large (RequestEntityTooLargeException). |
| 429 | MessageBody | The request failed because too many requests were sent during a certain amount of time (TooManyRequestsException). |
| 500 | MessageBody | The request failed due to an unknown internal server error, exception, or failure (InternalServerErrorException). |

### OPTIONS
<a name="templates-template-name-template-type-active-versionoptions"></a>

Retrieves information about the communication requirements and options that are available for the Active Template Version resource.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{template-name}} | String | True | The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (\_), or hyphens (-). Template names are case sensitive. |
| {{template-type}} | String | True | The type of channel that the message template is designed for. Valid values are: `EMAIL`, `PUSH`, `SMS`, and `VOICE`. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | The request succeeded. |

## Schemas
<a name="templates-template-name-template-type-active-version-schemas"></a>

### Request bodies
<a name="templates-template-name-template-type-active-version-request-examples"></a>

#### PUT schema
<a name="templates-template-name-template-type-active-version-request-body-put-example"></a>

```
{
  "Version": "string"
}
```

### Response bodies
<a name="templates-template-name-template-type-active-version-response-examples"></a>

#### MessageBody schema
<a name="templates-template-name-template-type-active-version-response-body-messagebody-example"></a>

```
{
  "RequestID": "string",
  "Message": "string"
}
```

## Properties
<a name="templates-template-name-template-type-active-version-properties"></a>

### MessageBody
<a name="templates-template-name-template-type-active-version-model-messagebody"></a>

Provides information about an API request or response.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Message | string | False | The message that's returned from the API. |
| RequestID | string | False | The unique identifier for the request or response. |

### TemplateActiveVersionRequest
<a name="templates-template-name-template-type-active-version-model-templateactiveversionrequest"></a>

Specifies which version of a message template to use as the active version of the template.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Version | string | False | The version of the message template to use as the active version of the template. Valid values are: `latest`, for the most recent version of the template; or, the unique identifier for any existing version of the template. If you specify an identifier, the value must match the identifier for an existing template version. To retrieve a list of versions and version identifiers for a template, use the [Template Versions](https://docs.aws.amazon.com/pinpoint/latest/apireference/templates-template-name-template-type-versions.html) resource. |

## See also
<a name="templates-template-name-template-type-active-version-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### UpdateTemplateActiveVersion
<a name="UpdateTemplateActiveVersion-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/pinpoint-2016-12-01/UpdateTemplateActiveVersion)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/pinpoint-2016-12-01/UpdateTemplateActiveVersion)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/pinpoint-2016-12-01/UpdateTemplateActiveVersion)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/pinpoint-2016-12-01/UpdateTemplateActiveVersion)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/pinpoint-2016-12-01/UpdateTemplateActiveVersion)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/pinpoint-2016-12-01/UpdateTemplateActiveVersion)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/pinpoint-2016-12-01/UpdateTemplateActiveVersion)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/pinpoint-2016-12-01/UpdateTemplateActiveVersion)
+ [AWS SDK for Python (Boto3)](/goto/boto3/pinpoint-2016-12-01/UpdateTemplateActiveVersion)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/pinpoint-2016-12-01/UpdateTemplateActiveVersion)
