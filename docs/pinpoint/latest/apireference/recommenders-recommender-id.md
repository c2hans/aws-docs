---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference/recommenders-recommender-id.html
---

**End of support notice:** On October 30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints, segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of support](https://docs.aws.amazon.com/console/pinpoint/migration-guide). **Note:** APIs related to SMS, voice, mobile push, OTP, and phone number validate are not impacted by this change and are supported by AWS End User Messaging.

# Recommender Model
<a name="recommenders-recommender-id"></a>

A *recommender model* is a type of machine learning (ML) model that generates predictions and recommendations by finding patterns in data. Based on the data that it receives, the model can dynamically predict and deliver a combination of personalized recommendations to add to messages. In Amazon Pinpoint, you can connect to these models, and send personalized recommendations to message recipients based on each recipient’s attributes and behavior.

To use a recommender model with Amazon Pinpoint, you start by creating an Amazon Personalize solution and deploying that solution as an Amazon Personalize campaign. Then you create a configuration for the recommender model in Amazon Pinpoint. In the configuration, you specify settings that determine where and how to retrieve and process data from the Amazon Personalize campaign. This includes: how to correlate user or endpoint identifiers in Amazon Pinpoint with user identifiers in the model; the number of recommended items to retrieve for each user or endpoint; and, where to store and how to process recommended items.

After you create a configuration, you can add recommendations from the model to messages that you send from campaigns and journeys. To do this, create an email, push notification, or SMS message template. In the template, specify the recommender model to use and add message variables that refer to recommended attributes for the model. A *recommended attribute* is a dynamic attribute that stores recommendation data. When you send a message that uses the template, Amazon Pinpoint retrieves the latest data from the recommender model, replaces each message variable with the recommendation data for each recipient, and then sends the message.

The Recommender Model resource represents the configuration settings for an individual recommender model that's associated with your Amazon Pinpoint account. This resource is available in the following AWS Regions: US East (N. Virginia); US West (Oregon); Asia Pacific (Mumbai); Asia Pacific (Sydney); and, Europe (Ireland).

You can use this resource to retrieve information about, update, or delete an Amazon Pinpoint configuration for a recommender model. To create a configuration for a recommender model, use the [Recommender Models](recommenders.md) resource.

## URI
<a name="recommenders-recommender-id-url"></a>

`/v1/recommenders/{{recommender-id}}`

## HTTP methods
<a name="recommenders-recommender-id-http-methods"></a>

### GET
<a name="recommenders-recommender-idget"></a>

**Operation ID:** `GetRecommenderConfiguration`

Retrieves information about an Amazon Pinpoint configuration for a recommender model.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{recommender-id}} | String | True | The unique identifier for the recommender model configuration. This identifier is displayed as the **Recommender ID** on the Amazon Pinpoint console. |

**Header parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| accept | String | False | Indicates which content types, expressed as MIME types, the client understands. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | RecommenderConfigurationResponse | The request succeeded. |
| 400 | MessageBody | The request contains a syntax error (BadRequestException). |
| 403 | MessageBody | The request was denied because access to the specified resource is forbidden (ForbiddenException). |
| 404 | MessageBody | The request failed because the specified resource was not found (NotFoundException). |
| 405 | MessageBody | The request failed because the method is not allowed for the specified resource (MethodNotAllowedException). |
| 413 | MessageBody | The request failed because the payload for the body of the request is too large (RequestEntityTooLargeException). |
| 429 | MessageBody | The request failed because too many requests were sent during a certain amount of time (TooManyRequestsException). |
| 500 | MessageBody | The request failed due to an unknown internal server error, exception, or failure (InternalServerErrorException). |

### PUT
<a name="recommenders-recommender-idput"></a>

**Operation ID:** `UpdateRecommenderConfiguration`

Updates an Amazon Pinpoint configuration for a recommender model.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{recommender-id}} | String | True | The unique identifier for the recommender model configuration. This identifier is displayed as the **Recommender ID** on the Amazon Pinpoint console. |

**Header parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| accept | String | False | Indicates which content types, expressed as MIME types, the client understands. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | RecommenderConfigurationResponse | The request succeeded. |
| 400 | MessageBody | The request contains a syntax error (BadRequestException). |
| 403 | MessageBody | The request was denied because access to the specified resource is forbidden (ForbiddenException). |
| 404 | MessageBody | The request failed because the specified resource was not found (NotFoundException). |
| 405 | MessageBody | The request failed because the method is not allowed for the specified resource (MethodNotAllowedException). |
| 413 | MessageBody | The request failed because the payload for the body of the request is too large (RequestEntityTooLargeException). |
| 429 | MessageBody | The request failed because too many requests were sent during a certain amount of time (TooManyRequestsException). |
| 500 | MessageBody | The request failed due to an unknown internal server error, exception, or failure (InternalServerErrorException). |

### DELETE
<a name="recommenders-recommender-iddelete"></a>

**Operation ID:** `DeleteRecommenderConfiguration`

Deletes an Amazon Pinpoint configuration for a recommender model.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{recommender-id}} | String | True | The unique identifier for the recommender model configuration. This identifier is displayed as the **Recommender ID** on the Amazon Pinpoint console. |

**Header parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| accept | String | False | Indicates which content types, expressed as MIME types, the client understands. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | RecommenderConfigurationResponse | The request succeeded. |
| 400 | MessageBody | The request contains a syntax error (BadRequestException). |
| 403 | MessageBody | The request was denied because access to the specified resource is forbidden (ForbiddenException). |
| 404 | MessageBody | The request failed because the specified resource was not found (NotFoundException). |
| 405 | MessageBody | The request failed because the method is not allowed for the specified resource (MethodNotAllowedException). |
| 413 | MessageBody | The request failed because the payload for the body of the request is too large (RequestEntityTooLargeException). |
| 429 | MessageBody | The request failed because too many requests were sent during a certain amount of time (TooManyRequestsException). |
| 500 | MessageBody | The request failed due to an unknown internal server error, exception, or failure (InternalServerErrorException). |

### OPTIONS
<a name="recommenders-recommender-idoptions"></a>

Retrieves information about the communication requirements and options that are available for the Recommender Model resource.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{recommender-id}} | String | True | The unique identifier for the recommender model configuration. This identifier is displayed as the **Recommender ID** on the Amazon Pinpoint console. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | The request succeeded. |

## Schemas
<a name="recommenders-recommender-id-schemas"></a>

### Request bodies
<a name="recommenders-recommender-id-request-examples"></a>

#### PUT schema
<a name="recommenders-recommender-id-request-body-put-example"></a>

```
{
  "Name": "string",
  "Description": "string",
  "RecommendationProviderUri": "string",
  "RecommendationTransformerUri": "string",
  "RecommendationProviderRoleArn": "string",
  "RecommendationsPerMessage": integer,
  "RecommendationProviderIdType": "string",
  "RecommendationsDisplayName": "string",
  "Attributes": {
  }
}
```

### Response bodies
<a name="recommenders-recommender-id-response-examples"></a>

#### RecommenderConfigurationResponse schema
<a name="recommenders-recommender-id-response-body-recommenderconfigurationresponse-example"></a>

```
{
  "Id": "string",
  "CreationDate": "string",
  "LastModifiedDate": "string",
  "Name": "string",
  "Description": "string",
  "RecommendationProviderUri": "string",
  "RecommendationTransformerUri": "string",
  "RecommendationProviderRoleArn": "string",
  "RecommendationsPerMessage": integer,
  "RecommendationProviderIdType": "string",
  "RecommendationsDisplayName": "string",
  "Attributes": {
  }
}
```

#### MessageBody schema
<a name="recommenders-recommender-id-response-body-messagebody-example"></a>

```
{
  "RequestID": "string",
  "Message": "string"
}
```

## Properties
<a name="recommenders-recommender-id-properties"></a>

### MessageBody
<a name="recommenders-recommender-id-model-messagebody"></a>

Provides information about an API request or response.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Message | string | False | The message that's returned from the API. |
| RequestID | string | False | The unique identifier for the request or response. |

### RecommenderConfigurationResponse
<a name="recommenders-recommender-id-model-recommenderconfigurationresponse"></a>

Provides information about Amazon Pinpoint configuration settings for retrieving and processing data from a recommender model.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Attributes | object | False | A map that defines 1-10 custom endpoint or user attributes, depending on the value for the `RecommendationProviderIdType` property. Each of these attributes temporarily stores a recommended item that's retrieved from the recommender model and sent to an AWS Lambda function for additional processing. Each attribute can be used as a message variable in a message template.<br />This value is null if the configuration doesn't invoke an AWS Lambda function (`RecommendationTransformerUri`) to perform additional processing of recommendation data. |
| CreationDate | string | True | The date, in extended ISO 8601 format, when the configuration was created for the recommender model. |
| Description | string | False | The custom description of the configuration for the recommender model. |
| Id | string | True | The unique identifier for the recommender model configuration. |
| LastModifiedDate | string | True | The date, in extended ISO 8601 format, when the configuration for the recommender model was last modified. |
| Name | string | False | The custom name of the configuration for the recommender model. |
| RecommendationProviderIdType | string | False | The type of Amazon Pinpoint ID that's associated with unique user IDs in the recommender model. This value enables the model to use attribute and event data that’s specific to a particular endpoint or user in an Amazon Pinpoint application. Possible values are:   `PINPOINT_ENDPOINT_ID` – Each user in the model is associated with a particular endpoint in Amazon Pinpoint. The data is correlated based on endpoint IDs in Amazon Pinpoint. This is the default value.    `PINPOINT_USER_ID` – Each user in the model is associated with a particular user and endpoint in Amazon Pinpoint. The data is correlated based on user IDs in Amazon Pinpoint. If this value is specified, an endpoint definition in Amazon Pinpoint has to specify both a user ID (`UserId`) and an endpoint ID. Otherwise, messages won’t be sent to the user's endpoint.    |
| RecommendationProviderRoleArn | string | True | The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that authorizes Amazon Pinpoint to retrieve recommendation data from the recommender model. |
| RecommendationProviderUri | string | True | The Amazon Resource Name (ARN) of the recommender model that Amazon Pinpoint retrieves the recommendation data from. This value is the ARN of an Amazon Personalize campaign. |
| RecommendationsDisplayName | string | False | The custom display name for the standard endpoint or user attribute (`RecommendationItems`) that temporarily stores recommended items for each endpoint or user, depending on the value for the `RecommendationProviderIdType` property. This name appears in the **Attribute finder** of the template editor on the Amazon Pinpoint console.<br />This value is null if the configuration doesn't invoke an AWS Lambda function (`RecommendationTransformerUri`) to perform additional processing of recommendation data. |
| RecommendationsPerMessage | integer | False | The number of recommended items that are retrieved from the model for each endpoint or user, depending on the value for the `RecommendationProviderIdType` property. This number determines how many recommended items are available for use in message variables. |
| RecommendationTransformerUri | string | False | The name or Amazon Resource Name (ARN) of the AWS Lambda function that Amazon Pinpoint invokes to perform additional processing of recommendation data that it retrieves from the recommender model. |

### UpdateRecommenderConfiguration
<a name="recommenders-recommender-id-model-updaterecommenderconfiguration"></a>

Specifies Amazon Pinpoint configuration settings for retrieving and processing recommendation data from a recommender model.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Attributes | object | False | A map of key-value pairs that defines 1-10 custom endpoint or user attributes, depending on the value for the `RecommendationProviderIdType` property. Each of these attributes temporarily stores a recommended item that's retrieved from the recommender model and sent to an AWS Lambda function for additional processing. Each attribute can be used as a message variable in a message template.<br />In the map, the key is the name of a custom attribute and the value is a custom display name for that attribute. The display name appears in the **Attribute finder** of the template editor on the Amazon Pinpoint console. The following restrictions apply to these names:  An attribute name must start with a letter or number and it can contain up to 50 characters. The characters can be letters, numbers, underscores (\_), or hyphens (-). Attribute names are case sensitive and must be unique.   An attribute display name must start with a letter or number and it can contain up to 25 characters. The characters can be letters, numbers, spaces, underscores (\_), or hyphens (-).  <br />This object is required if the configuration invokes an AWS Lambda function (`RecommendationTransformerUri`) to process recommendation data. Otherwise, don't include this object in your request. |
| Description | string | False | A custom description of the configuration for the recommender model. The description can contain up to 128 characters. The characters can be letters, numbers, spaces, or the following symbols: \_ ; () , ‐. |
| Name | string | False | A custom name of the configuration for the recommender model. The name must start with a letter or number and it can contain up to 128 characters. The characters can be letters, numbers, spaces, underscores (\_), or hyphens (-). |
| RecommendationProviderIdType | string | False | The type of Amazon Pinpoint ID to associate with unique user IDs in the recommender model. This value enables the model to use attribute and event data that’s specific to a particular endpoint or user in an Amazon Pinpoint application. Valid values are:   `PINPOINT_ENDPOINT_ID` – Associate each user in the model with a particular endpoint in Amazon Pinpoint. The data is correlated based on endpoint IDs in Amazon Pinpoint. This is the default value.    `PINPOINT_USER_ID` – Associate each user in the model with a particular user and endpoint in Amazon Pinpoint. The data is correlated based on user IDs in Amazon Pinpoint. If you specify this value, an endpoint definition in Amazon Pinpoint has to specify both a user ID (`UserId`) and an endpoint ID. Otherwise, messages won’t be sent to the user's endpoint.   |
| RecommendationProviderRoleArn | string | True | The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that authorizes Amazon Pinpoint to retrieve recommendation data from the recommender model. |
| RecommendationProviderUri | string | True | The Amazon Resource Name (ARN) of the recommender model to retrieve recommendation data from. This value must match the ARN of an Amazon Personalize campaign. |
| RecommendationsDisplayName | string | False | A custom display name for the standard endpoint or user attribute (`RecommendationItems`) that temporarily stores recommended items for each endpoint or user, depending on the value for the `RecommendationProviderIdType` property. This value is required if the configuration doesn't invoke an AWS Lambda function (`RecommendationTransformerUri`) to perform additional processing of recommendation data.<br />This name appears in the **Attribute finder** of the template editor on the Amazon Pinpoint console. The name can contain up to 25 characters. The characters can be letters, numbers, spaces, underscores (\_), or hyphens (-). These restrictions don't apply to attribute values. |
| RecommendationsPerMessage | integer | False | The number of recommended items to retrieve from the model for each endpoint or user, depending on the value for the `RecommendationProviderIdType` property. This number determines how many recommended items are available for use in message variables. The minimum value is 1. The maximum value is 5. The default value is 5.<br />To use multiple recommended items and custom attributes with message variables, you have to use an AWS Lambda function (`RecommendationTransformerUri`) to perform additional processing of recommendation data. |
| RecommendationTransformerUri | string | False | The name or Amazon Resource Name (ARN) of the AWS Lambda function to invoke for additional processing of recommendation data that's retrieved from the recommender model. |

## See also
<a name="recommenders-recommender-id-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### GetRecommenderConfiguration
<a name="GetRecommenderConfiguration-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/pinpoint-2016-12-01/GetRecommenderConfiguration)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/pinpoint-2016-12-01/GetRecommenderConfiguration)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/pinpoint-2016-12-01/GetRecommenderConfiguration)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/pinpoint-2016-12-01/GetRecommenderConfiguration)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/pinpoint-2016-12-01/GetRecommenderConfiguration)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/pinpoint-2016-12-01/GetRecommenderConfiguration)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/pinpoint-2016-12-01/GetRecommenderConfiguration)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/pinpoint-2016-12-01/GetRecommenderConfiguration)
+ [AWS SDK for Python](/goto/boto3/pinpoint-2016-12-01/GetRecommenderConfiguration)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/pinpoint-2016-12-01/GetRecommenderConfiguration)

### UpdateRecommenderConfiguration
<a name="UpdateRecommenderConfiguration-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/pinpoint-2016-12-01/UpdateRecommenderConfiguration)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/pinpoint-2016-12-01/UpdateRecommenderConfiguration)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/pinpoint-2016-12-01/UpdateRecommenderConfiguration)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/pinpoint-2016-12-01/UpdateRecommenderConfiguration)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/pinpoint-2016-12-01/UpdateRecommenderConfiguration)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/pinpoint-2016-12-01/UpdateRecommenderConfiguration)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/pinpoint-2016-12-01/UpdateRecommenderConfiguration)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/pinpoint-2016-12-01/UpdateRecommenderConfiguration)
+ [AWS SDK for Python](/goto/boto3/pinpoint-2016-12-01/UpdateRecommenderConfiguration)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/pinpoint-2016-12-01/UpdateRecommenderConfiguration)

### DeleteRecommenderConfiguration
<a name="DeleteRecommenderConfiguration-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/pinpoint-2016-12-01/DeleteRecommenderConfiguration)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/pinpoint-2016-12-01/DeleteRecommenderConfiguration)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/pinpoint-2016-12-01/DeleteRecommenderConfiguration)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/pinpoint-2016-12-01/DeleteRecommenderConfiguration)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/pinpoint-2016-12-01/DeleteRecommenderConfiguration)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/pinpoint-2016-12-01/DeleteRecommenderConfiguration)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/pinpoint-2016-12-01/DeleteRecommenderConfiguration)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/pinpoint-2016-12-01/DeleteRecommenderConfiguration)
+ [AWS SDK for Python](/goto/boto3/pinpoint-2016-12-01/DeleteRecommenderConfiguration)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/pinpoint-2016-12-01/DeleteRecommenderConfiguration)
