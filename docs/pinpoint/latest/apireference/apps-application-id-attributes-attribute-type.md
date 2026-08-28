---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-attributes-attribute-type.html
---

**End of support notice:** On October 30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints, segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of support](https://docs.aws.amazon.com/console/pinpoint/migration-guide). **Note:** APIs related to SMS, voice, mobile push, OTP, and phone number validate are not impacted by this change and are supported by AWS End User Messaging.

# Attributes
<a name="apps-application-id-attributes-attribute-type"></a>

An *attribute* is a characteristic of a user or an endpoint. It can be a standard attribute that Amazon Pinpoint defines or a custom attribute that you define. For example, you might create custom attributes that capture your users' contact information, their preferences, and the dates when they opted in or out of receiving specific types of messages from you.

The Attributes resource represents custom attributes that you've defined for users and endpoints that are associated with a specific application. You can use this resource to remove one or more custom attributes from the Amazon Pinpoint application. Existing endpoints continue to persist these attributes and these existing values continue to appear on the Amazon Pinpoint console and in export jobs. However, Amazon Pinpoint stops capturing new or changed values for a custom attribute. For information about the attributes that you can use to define an endpoint, see the [Endpoint](apps-application-id-endpoints-endpoint-id.md) resource.

To retrieve a list of custom attributes and attribute values for a specific user, use the [User](apps-application-id-users-user-id.md) resource. To add or retrieve custom attributes and attribute values for endpoints, use the [Endpoints](apps-application-id-endpoints.md) or [Endpoint](apps-application-id-endpoints-endpoint-id.md) resource.

## URI
<a name="apps-application-id-attributes-attribute-type-url"></a>

`/v1/apps/{{application-id}}/attributes/{{attribute-type}}`

## HTTP methods
<a name="apps-application-id-attributes-attribute-type-http-methods"></a>

### PUT
<a name="apps-application-id-attributes-attribute-typeput"></a>

**Operation ID:** `RemoveAttributes`

Removes one or more custom attributes, of the same attribute type, from the application. Existing endpoints still have the attributes but Amazon Pinpoint will stop capturing new or changed values for these attributes.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{attribute-type}} | String | True | The type of attribute or attributes to remove. Valid values are:+   `endpoint-custom-attributes` – Custom attributes that describe endpoints, such as the date when an associated user opted in or out of receiving communications from you through a specific type of channel. <br />+   `endpoint-metric-attributes` – Custom metrics that your app reports to Amazon Pinpoint for endpoints, such as the number of app sessions or the number of items left in a cart. <br />+   `endpoint-user-attributes` – Custom attributes that describe users, such as first name, last name, and age.  |
| {{application-id}} | String | True | The unique identifier for the application. This identifier is displayed as the **Project ID** on the Amazon Pinpoint console. |

**Header parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| accept | String | False | Indicates which content types, expressed as MIME types, the client understands. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | AttributesResource | The request succeeded. |
| 400 | MessageBody | The request contains a syntax error (BadRequestException). |
| 403 | MessageBody | The request was denied because access to the specified resource is forbidden (ForbiddenException). |
| 404 | MessageBody | The request failed because the specified resource was not found (NotFoundException). |
| 405 | MessageBody | The request failed because the method is not allowed for the specified resource (MethodNotAllowedException). |
| 413 | MessageBody | The request failed because the payload for the body of the request is too large (RequestEntityTooLargeException). |
| 429 | MessageBody | The request failed because too many requests were sent during a certain amount of time (TooManyRequestsException). |
| 500 | MessageBody | The request failed due to an unknown internal server error, exception, or failure (InternalServerErrorException). |

### OPTIONS
<a name="apps-application-id-attributes-attribute-typeoptions"></a>

Retrieves information about the communication requirements and options that are available for the Attributes resource.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{attribute-type}} | String | True | The type of attribute or attributes to remove. Valid values are:+   `endpoint-custom-attributes` – Custom attributes that describe endpoints, such as the date when an associated user opted in or out of receiving communications from you through a specific type of channel. <br />+   `endpoint-metric-attributes` – Custom metrics that your app reports to Amazon Pinpoint for endpoints, such as the number of app sessions or the number of items left in a cart. <br />+   `endpoint-user-attributes` – Custom attributes that describe users, such as first name, last name, and age.  |
| {{application-id}} | String | True | The unique identifier for the application. This identifier is displayed as the **Project ID** on the Amazon Pinpoint console. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | The request succeeded. |

## Schemas
<a name="apps-application-id-attributes-attribute-type-schemas"></a>

### Request bodies
<a name="apps-application-id-attributes-attribute-type-request-examples"></a>

#### PUT schema
<a name="apps-application-id-attributes-attribute-type-request-body-put-example"></a>

```
{
  "Blacklist": [
    "string"
  ]
}
```

### Response bodies
<a name="apps-application-id-attributes-attribute-type-response-examples"></a>

#### AttributesResource schema
<a name="apps-application-id-attributes-attribute-type-response-body-attributesresource-example"></a>

```
{
  "ApplicationId": "string",
  "AttributeType": "string",
  "Attributes": [
    "string"
  ]
}
```

#### MessageBody schema
<a name="apps-application-id-attributes-attribute-type-response-body-messagebody-example"></a>

```
{
  "RequestID": "string",
  "Message": "string"
}
```

## Properties
<a name="apps-application-id-attributes-attribute-type-properties"></a>

### AttributesResource
<a name="apps-application-id-attributes-attribute-type-model-attributesresource"></a>

Provides information about the type and the names of attributes that were removed from all the endpoints that are associated with an application.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| ApplicationId | string | True | The unique identifier for the application. |
| Attributes | Array of type string | False | An array that specifies the names of the remaining attributes after any attributes were removed from the endpoints. |
| AttributeType | string | True | The type of attribute or attributes that were removed from the endpoints. Valid values are:+   `endpoint-custom-attributes` – Custom attributes that describe endpoints. <br />+   `endpoint-metric-attributes` – Custom metrics that your app reports to Amazon Pinpoint for endpoints. <br />+   `endpoint-user-attributes` – Custom attributes that describe users.  |

### MessageBody
<a name="apps-application-id-attributes-attribute-type-model-messagebody"></a>

Provides information about an API request or response.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Message | string | False | The message that's returned from the API. |
| RequestID | string | False | The unique identifier for the request or response. |

### UpdateAttributesRequest
<a name="apps-application-id-attributes-attribute-type-model-updateattributesrequest"></a>

Specifies one or more attributes to remove from all the endpoints that are associated with an application.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Blacklist | Array of type string | False | An array of the attributes to remove from all the endpoints that are associated with the application. The array can specify the complete, exact name of each attribute to remove or it can specify a glob pattern that an attribute name must match in order for the attribute to be removed. |

## See also
<a name="apps-application-id-attributes-attribute-type-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### RemoveAttributes
<a name="RemoveAttributes-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/pinpoint-2016-12-01/RemoveAttributes)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/pinpoint-2016-12-01/RemoveAttributes)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/pinpoint-2016-12-01/RemoveAttributes)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/pinpoint-2016-12-01/RemoveAttributes)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/pinpoint-2016-12-01/RemoveAttributes)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/pinpoint-2016-12-01/RemoveAttributes)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/pinpoint-2016-12-01/RemoveAttributes)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/pinpoint-2016-12-01/RemoveAttributes)
+ [AWS SDK for Python](/goto/boto3/pinpoint-2016-12-01/RemoveAttributes)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/pinpoint-2016-12-01/RemoveAttributes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Pinpoint. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pinpoint` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
