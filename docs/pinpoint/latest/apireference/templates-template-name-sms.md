---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference/templates-template-name-sms.html
---

**End of support notice:** On October 30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints, segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of support](https://docs.aws.amazon.com/console/pinpoint/migration-guide). **Note:** APIs related to SMS, voice, mobile push, OTP, and phone number validate are not impacted by this change and are supported by AWS End User Messaging.

# SMS Template
<a name="templates-template-name-sms"></a>

An *SMS template* is a type of message template that contains content and settings that you can define, save, and reuse in messages that you send through the SMS channel for any of your Amazon Pinpoint applications. You can use SMS templates in text messages that you send from campaigns, or to a limited audience as direct or test messages.

When you create an SMS template, you specify the settings and content that you want to reuse in the body of messages that are based on the template. This content can be static text or personalized content that you define by using the Handlebars template system and message variables. When you send a message that’s based on a template, Amazon Pinpoint populates the message with the settings and content that you defined in the template.

The SMS Template resource represents the repository of SMS templates that are associated with your Amazon Pinpoint account. You can use this resource to create, retrieve, update, or delete a message template for messages that you send through the SMS channel.

Amazon Pinpoint supports versioning for all types of message templates. When you use the SMS Template resource to work with a template, you can use supported parameters to specify whether your request applies to only a specific version of the template or to the overall template. For example, if you update a template, you can specify whether you want to save your updates as a new version of the template or save them to the latest existing version of the template. To retrieve information about all the versions of a template, use the [Template Versions](https://docs.aws.amazon.com/pinpoint/latest/apireference/templates-template-name-template-type-versions.html) resource.

## URI
<a name="templates-template-name-sms-url"></a>

`/v1/templates/{{template-name}}/sms`

## HTTP methods
<a name="templates-template-name-sms-http-methods"></a>

### GET
<a name="templates-template-name-smsget"></a>

**Operation ID:** `GetSmsTemplate`

Retrieves the content and settings of a message template for messages that are sent through the SMS channel.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{template-name}} | String | True | The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (\_), or hyphens (-). Template names are case sensitive. |

**Header parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| accept | String | False | Indicates which content types, expressed as MIME types, the client understands. |

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| version | String | False | The unique identifier for the version of the message template to update, retrieve information about, or delete. To retrieve identifiers and other information for all the versions of a template, use the [Template Versions](https://docs.aws.amazon.com/pinpoint/latest/apireference/templates-template-name-template-type-versions.html)resource.<br />If specified, this value must match the identifier for an existing template version. If specified for an update operation, this value must match the identifier for the latest existing version of the template. This restriction helps ensure that race conditions don't occur.<br />If you don't specify a value for this parameter, Amazon Pinpoint does the following:+  For a get operation, retrieves information about the active version of the template. <br />+  For an update operation, saves the updates to (overwrites) the latest existing version of the template, if the `create-new-version` parameter isn't used or is set to `false`. <br />+  For a delete operation, deletes the template, including all versions of the template.  |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | SMSTemplateResponse | The request succeeded. |
| 400 | MessageBody | The request contains a syntax error (BadRequestException). |
| 403 | MessageBody | The request was denied because access to the specified resource is forbidden (ForbiddenException). |
| 404 | MessageBody | The request failed because the specified resource was not found (NotFoundException). |
| 405 | MessageBody | The request failed because the method is not allowed for the specified resource (MethodNotAllowedException). |
| 413 | MessageBody | The request failed because the payload for the body of the request is too large (RequestEntityTooLargeException). |
| 429 | MessageBody | The request failed because too many requests were sent during a certain amount of time (TooManyRequestsException). |
| 500 | MessageBody | The request failed due to an unknown internal server error, exception, or failure (InternalServerErrorException). |

### POST
<a name="templates-template-name-smspost"></a>

**Operation ID:** `CreateSmsTemplate`

Creates a message template for messages that are sent through the SMS channel.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{template-name}} | String | True | The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (\_), or hyphens (-). Template names are case sensitive. |

**Header parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| accept | String | False | Indicates which content types, expressed as MIME types, the client understands. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 201 | CreateTemplateMessageBody | The request succeeded and the specified resource was created. |
| 400 | MessageBody | The request contains a syntax error (BadRequestException). |
| 403 | MessageBody | The request was denied because access to the specified resource is forbidden (ForbiddenException). |
| 405 | MessageBody | The request failed because the method is not allowed for the specified resource (MethodNotAllowedException). |
| 409 | MessageBody | The request failed due to a conflict with the current state of the specified resource (ConflictException). |
| 429 | MessageBody | The request failed because too many requests were sent during a certain amount of time (TooManyRequestsException). |
| 500 | MessageBody | The request failed due to an unknown internal server error, exception, or failure (InternalServerErrorException). |

### PUT
<a name="templates-template-name-smsput"></a>

**Operation ID:** `UpdateSmsTemplate`

Updates an existing message template for messages that are sent through the SMS channel.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{template-name}} | String | True | The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (\_), or hyphens (-). Template names are case sensitive. |

**Header parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| accept | String | False | Indicates which content types, expressed as MIME types, the client understands. |

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| create-new-version | String | False | Specifies whether to save the updates as a new version of the message template. Valid values are: `true`, save the updates as a new version; and, `false`, save the updates to (overwrite) the latest existing version of the template.<br />If you don't specify a value for this parameter, Amazon Pinpoint saves the updates to (overwrites) the latest existing version of the template. If you specify a value of `true` for this parameter, don't specify a value for the `version` parameter. Otherwise, an error will occur. |
| version | String | False | The unique identifier for the version of the message template to update, retrieve information about, or delete. To retrieve identifiers and other information for all the versions of a template, use the [Template Versions](https://docs.aws.amazon.com/pinpoint/latest/apireference/templates-template-name-template-type-versions.html)resource.<br />If specified, this value must match the identifier for an existing template version. If specified for an update operation, this value must match the identifier for the latest existing version of the template. This restriction helps ensure that race conditions don't occur.<br />If you don't specify a value for this parameter, Amazon Pinpoint does the following:+  For a get operation, retrieves information about the active version of the template. <br />+  For an update operation, saves the updates to (overwrites) the latest existing version of the template, if the `create-new-version` parameter isn't used or is set to `false`. <br />+  For a delete operation, deletes the template, including all versions of the template.  |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 202 | MessageBody | The request was accepted for processing. Processing may not be complete. |
| 400 | MessageBody | The request contains a syntax error (BadRequestException). |
| 403 | MessageBody | The request was denied because access to the specified resource is forbidden (ForbiddenException). |
| 404 | MessageBody | The request failed because the specified resource was not found (NotFoundException). |
| 405 | MessageBody | The request failed because the method is not allowed for the specified resource (MethodNotAllowedException). |
| 413 | MessageBody | The request failed because the payload for the body of the request is too large (RequestEntityTooLargeException). |
| 429 | MessageBody | The request failed because too many requests were sent during a certain amount of time (TooManyRequestsException). |
| 500 | MessageBody | The request failed due to an unknown internal server error, exception, or failure (InternalServerErrorException). |

### DELETE
<a name="templates-template-name-smsdelete"></a>

**Operation ID:** `DeleteSmsTemplate`

Deletes a message template for messages that were sent through the SMS channel.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{template-name}} | String | True | The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (\_), or hyphens (-). Template names are case sensitive. |

**Header parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| accept | String | False | Indicates which content types, expressed as MIME types, the client understands. |

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| version | String | False | The unique identifier for the version of the message template to update, retrieve information about, or delete. To retrieve identifiers and other information for all the versions of a template, use the [Template Versions](https://docs.aws.amazon.com/pinpoint/latest/apireference/templates-template-name-template-type-versions.html)resource.<br />If specified, this value must match the identifier for an existing template version. If specified for an update operation, this value must match the identifier for the latest existing version of the template. This restriction helps ensure that race conditions don't occur.<br />If you don't specify a value for this parameter, Amazon Pinpoint does the following:+  For a get operation, retrieves information about the active version of the template. <br />+  For an update operation, saves the updates to (overwrites) the latest existing version of the template, if the `create-new-version` parameter isn't used or is set to `false`. <br />+  For a delete operation, deletes the template, including all versions of the template.  |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 202 | MessageBody | The request was accepted for processing. Processing may not be complete. |
| 400 | MessageBody | The request contains a syntax error (BadRequestException). |
| 403 | MessageBody | The request was denied because access to the specified resource is forbidden (ForbiddenException). |
| 404 | MessageBody | The request failed because the specified resource was not found (NotFoundException). |
| 405 | MessageBody | The request failed because the method is not allowed for the specified resource (MethodNotAllowedException). |
| 413 | MessageBody | The request failed because the payload for the body of the request is too large (RequestEntityTooLargeException). |
| 429 | MessageBody | The request failed because too many requests were sent during a certain amount of time (TooManyRequestsException). |
| 500 | MessageBody | The request failed due to an unknown internal server error, exception, or failure (InternalServerErrorException). |

### OPTIONS
<a name="templates-template-name-smsoptions"></a>

Retrieves information about the communication requirements and options that are available for the SMS Template resource.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{template-name}} | String | True | The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (\_), or hyphens (-). Template names are case sensitive. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | The request succeeded. |

## Schemas
<a name="templates-template-name-sms-schemas"></a>

### Request bodies
<a name="templates-template-name-sms-request-examples"></a>

#### POST schema
<a name="templates-template-name-sms-request-body-post-example"></a>

```
{
  "TemplateDescription": "string",
  "DefaultSubstitutions": "string",
  "tags": {
  },
  "Body": "string",
  "RecommenderId": "string"
}
```

#### PUT schema
<a name="templates-template-name-sms-request-body-put-example"></a>

```
{
  "TemplateDescription": "string",
  "DefaultSubstitutions": "string",
  "tags": {
  },
  "Body": "string",
  "RecommenderId": "string"
}
```

### Response bodies
<a name="templates-template-name-sms-response-examples"></a>

#### SMSTemplateResponse schema
<a name="templates-template-name-sms-response-body-smstemplateresponse-example"></a>

```
{
  "CreationDate": "string",
  "LastModifiedDate": "string",
  "TemplateType": enum,
  "TemplateName": "string",
  "TemplateDescription": "string",
  "DefaultSubstitutions": "string",
  "Version": "string",
  "tags": {
  },
  "Arn": "string",
  "Body": "string",
  "RecommenderId": "string"
}
```

#### CreateTemplateMessageBody schema
<a name="templates-template-name-sms-response-body-createtemplatemessagebody-example"></a>

```
{
  "RequestID": "string",
  "Message": "string",
  "Arn": "string"
}
```

#### MessageBody schema
<a name="templates-template-name-sms-response-body-messagebody-example"></a>

```
{
  "RequestID": "string",
  "Message": "string"
}
```

## Properties
<a name="templates-template-name-sms-properties"></a>

### CreateTemplateMessageBody
<a name="templates-template-name-sms-model-createtemplatemessagebody"></a>

Provides information about a request to create a message template.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Arn | string | False | The Amazon Resource Name (ARN) of the message template that was created. |
| Message | string | False | The message that's returned from the API for the request to create the message template. |
| RequestID | string | False | The unique identifier for the request to create the message template. |

### MessageBody
<a name="templates-template-name-sms-model-messagebody"></a>

Provides information about an API request or response.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Message | string | False | The message that's returned from the API. |
| RequestID | string | False | The unique identifier for the request or response. |

### SMSTemplateRequest
<a name="templates-template-name-sms-model-smstemplaterequest"></a>

Specifies the content and settings for a message template that can be used in text messages that are sent through the SMS channel.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Body | string | False | The message body to use in text messages that are based on the message template. |
| DefaultSubstitutions | string | False | A JSON object that specifies the default values to use for message variables in the message template. This object is a set of key-value pairs. Each key defines a message variable in the template. The corresponding value defines the default value for that variable. When you create a message that's based on the template, you can override these defaults with message-specific and address-specific variables and values. |
| RecommenderId | string | False | The unique identifier for the recommender model to use for the message template. Amazon Pinpoint uses this value to determine how to retrieve and process data from a recommender model when it sends messages that use the template, if the template contains message variables for recommendation data. |
| tags | object | False |  As of **22-05-2023** the tags attribute has been deprecated. After this date any value in the PUT UpdateSmsTemplate tags attribute is not processed and an error code is not returned. The POST CreateSmsTemplate tags attribute is processed. Use the [Tags](https://docs.aws.amazon.com/pinpoint/latest/apireference/tags-resource-arn.html) resource to add or modify tags. (Deprecated) A string-to-string map of key-value pairs that defines the tags to associate with the message template. Each tag consists of a required tag key and an associated tag value. |
| TemplateDescription | string | False | A custom description of the message template. |

### SMSTemplateResponse
<a name="templates-template-name-sms-model-smstemplateresponse"></a>

Provides information about the content and settings for a message template that can be used in text messages that are sent through the SMS channel.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Arn | string | False | The Amazon Resource Name (ARN) of the message template. |
| Body | string | False | The message body that's used in text messages that are based on the message template. |
| CreationDate | string | True | The date, in ISO 8601 format, when the message template was created. |
| DefaultSubstitutions | string | False | The JSON object that specifies the default values that are used for message variables in the message template. This object is a set of key-value pairs. Each key defines a message variable in the template. The corresponding value defines the default value for that variable. |
| LastModifiedDate | string | True | The date, in ISO 8601 format, when the message template was last modified. |
| RecommenderId | string | False | The unique identifier for the recommender model that's used by the message template. |
| tags | object | False | A string-to-string map of key-value pairs that identifies the tags that are associated with the message template. Each tag consists of a required tag key and an associated tag value. |
| TemplateDescription | string | False | The custom description of the message template. |
| TemplateName | string | True | The name of the message template. |
| TemplateType | string<br />Values: `EMAIL \| SMS \| VOICE \| PUSH \| INAPP` | True | The type of channel that the message template is designed for. For an SMS template, this value is `SMS`. |
| Version | string | False | The unique identifier, as an integer, for the active version of the message template, or the version of the template that you specified by using the `version` parameter in your request. |

## See also
<a name="templates-template-name-sms-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### GetSmsTemplate
<a name="GetSmsTemplate-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/pinpoint-2016-12-01/GetSmsTemplate)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/pinpoint-2016-12-01/GetSmsTemplate)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/pinpoint-2016-12-01/GetSmsTemplate)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/pinpoint-2016-12-01/GetSmsTemplate)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/pinpoint-2016-12-01/GetSmsTemplate)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/pinpoint-2016-12-01/GetSmsTemplate)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/pinpoint-2016-12-01/GetSmsTemplate)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/pinpoint-2016-12-01/GetSmsTemplate)
+ [AWS SDK for Python](/goto/boto3/pinpoint-2016-12-01/GetSmsTemplate)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/pinpoint-2016-12-01/GetSmsTemplate)

### CreateSmsTemplate
<a name="CreateSmsTemplate-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/pinpoint-2016-12-01/CreateSmsTemplate)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/pinpoint-2016-12-01/CreateSmsTemplate)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/pinpoint-2016-12-01/CreateSmsTemplate)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/pinpoint-2016-12-01/CreateSmsTemplate)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/pinpoint-2016-12-01/CreateSmsTemplate)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/pinpoint-2016-12-01/CreateSmsTemplate)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/pinpoint-2016-12-01/CreateSmsTemplate)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/pinpoint-2016-12-01/CreateSmsTemplate)
+ [AWS SDK for Python](/goto/boto3/pinpoint-2016-12-01/CreateSmsTemplate)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/pinpoint-2016-12-01/CreateSmsTemplate)

### UpdateSmsTemplate
<a name="UpdateSmsTemplate-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/pinpoint-2016-12-01/UpdateSmsTemplate)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/pinpoint-2016-12-01/UpdateSmsTemplate)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/pinpoint-2016-12-01/UpdateSmsTemplate)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/pinpoint-2016-12-01/UpdateSmsTemplate)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/pinpoint-2016-12-01/UpdateSmsTemplate)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/pinpoint-2016-12-01/UpdateSmsTemplate)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/pinpoint-2016-12-01/UpdateSmsTemplate)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/pinpoint-2016-12-01/UpdateSmsTemplate)
+ [AWS SDK for Python](/goto/boto3/pinpoint-2016-12-01/UpdateSmsTemplate)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/pinpoint-2016-12-01/UpdateSmsTemplate)

### DeleteSmsTemplate
<a name="DeleteSmsTemplate-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/pinpoint-2016-12-01/DeleteSmsTemplate)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/pinpoint-2016-12-01/DeleteSmsTemplate)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/pinpoint-2016-12-01/DeleteSmsTemplate)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/pinpoint-2016-12-01/DeleteSmsTemplate)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/pinpoint-2016-12-01/DeleteSmsTemplate)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/pinpoint-2016-12-01/DeleteSmsTemplate)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/pinpoint-2016-12-01/DeleteSmsTemplate)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/pinpoint-2016-12-01/DeleteSmsTemplate)
+ [AWS SDK for Python](/goto/boto3/pinpoint-2016-12-01/DeleteSmsTemplate)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/pinpoint-2016-12-01/DeleteSmsTemplate)
