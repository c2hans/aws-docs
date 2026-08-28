---
source_url: https://docs.aws.amazon.com/pinpoint-sms-voice/latest/APIReference/v1-sms-voice-configuration-sets.html
---

**End of support notice:** On October 30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints, segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of support](https://docs.aws.amazon.com/console/pinpoint/migration-guide). **Note:** APIs related to SMS, voice, mobile push, OTP, and phone number validate are not impacted by this change and are supported by AWS End User Messaging.

# Configuration Sets
<a name="v1-sms-voice-configuration-sets"></a>

A *configuration set* is a set of rules that you apply to the voice messages that you send. In a configuration set, you can specify a destination for specific types of events related to voice messages. For example, when a message is successfully delivered, you can log that event to an Amazon CloudWatch destination, or send notifications to endpoints that are subscribed to an Amazon SNS topic.

When you send a voice message, you have to specify one (and only one) configuration set.

## URI
<a name="v1-sms-voice-configuration-sets-url"></a>

`/v1/sms-voice/configuration-sets`

## HTTP methods
<a name="v1-sms-voice-configuration-sets-http-methods"></a>

### GET
<a name="v1-sms-voice-configuration-setsget"></a>

**Operation ID:** `ListConfigurationSets`

Retrieves a list of configuration sets that are associated with your account in the current AWS Region.

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| PageSize | String | False | Used to specify the number of items that should be returned in the response. |
| NextToken | String | False | A token returned from a previous call to the API that indicates the position in the list of results. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | ListConfigurationSetsResponse | An object that contains information about the configuration sets for your account in the current AWS Region. |
| 400 | BadRequestException | The request contained syntax that the API couldn't interpret. Modify the request and try again. |
| 429 | TooManyRequestsException | You've issued too many requests to the resource. Wait a few minutes, and then try again. |
| 500 | InternalServiceErrorException | The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future. |

### POST
<a name="v1-sms-voice-configuration-setspost"></a>

**Operation ID:** `CreateConfigurationSet`

Creates a new configuration set. After you create the configuration set, you can add one or more event destinations to it.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | CreateConfigurationSetResponse | An empty object that indicates that the configuration set was successfully created. |
| 400 | BadRequestException | The request contained syntax that the API couldn't interpret. Modify the request and try again. |
| 409 | AlreadyExistsException | The resource you tried to create already exists. |
| 412 | LimitExceededException | You've tried to create a number of resources that exceeds the maximum number of resources for your account. For more information, see [Amazon Pinpoint Quotas](https://docs.aws.amazon.com/pinpoint/latest/developerguide/limits.html) in the *Amazon Pinpoint Developer Guide*. |
| 429 | TooManyRequestsException | You've issued too many requests to the resource. Wait a few minutes, and then try again. |
| 500 | InternalServiceErrorException | The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future. |

### OPTIONS
<a name="v1-sms-voice-configuration-setsoptions"></a>

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | Indicates that the API successfully received the request. |

## Schemas
<a name="v1-sms-voice-configuration-sets-schemas"></a>

### Request bodies
<a name="v1-sms-voice-configuration-sets-request-examples"></a>

#### POST schema
<a name="v1-sms-voice-configuration-sets-request-body-post-example"></a>

```
{
  "ConfigurationSetName": "string"
}
```

### Response bodies
<a name="v1-sms-voice-configuration-sets-response-examples"></a>

#### ListConfigurationSetsResponse schema
<a name="v1-sms-voice-configuration-sets-response-body-listconfigurationsetsresponse-example"></a>

```
{
  "NextToken": "string",
  "ConfigurationSets": [
    "string"
  ]
}
```

#### CreateConfigurationSetResponse schema
<a name="v1-sms-voice-configuration-sets-response-body-createconfigurationsetresponse-example"></a>

```
{
}
```

#### BadRequestException schema
<a name="v1-sms-voice-configuration-sets-response-body-badrequestexception-example"></a>

```
{
  "Message": "string"
}
```

#### AlreadyExistsException schema
<a name="v1-sms-voice-configuration-sets-response-body-alreadyexistsexception-example"></a>

```
{
  "Message": "string"
}
```

#### LimitExceededException schema
<a name="v1-sms-voice-configuration-sets-response-body-limitexceededexception-example"></a>

```
{
  "Message": "string"
}
```

#### TooManyRequestsException schema
<a name="v1-sms-voice-configuration-sets-response-body-toomanyrequestsexception-example"></a>

```
{
  "Message": "string"
}
```

#### InternalServiceErrorException schema
<a name="v1-sms-voice-configuration-sets-response-body-internalserviceerrorexception-example"></a>

```
{
  "Message": "string"
}
```

## Properties
<a name="v1-sms-voice-configuration-sets-properties"></a>

### AlreadyExistsException
<a name="v1-sms-voice-configuration-sets-model-alreadyexistsexception"></a>

The resource that you specified in your request already exists.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Message | string | False | A description of the error that the API encountered. |

### BadRequestException
<a name="v1-sms-voice-configuration-sets-model-badrequestexception"></a>

The input that you provided to the API is invalid.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Message | string | False | A description of the error that the API encountered. |

### CreateConfigurationSetRequest
<a name="v1-sms-voice-configuration-sets-model-createconfigurationsetrequest"></a>

A request to create a new configuration set.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| ConfigurationSetName | string | True | The name that you want to give the configuration set. |

### CreateConfigurationSetResponse
<a name="v1-sms-voice-configuration-sets-model-createconfigurationsetresponse"></a>

An empty object that indicates that the configuration set was successfully created.

### InternalServiceErrorException
<a name="v1-sms-voice-configuration-sets-model-internalserviceerrorexception"></a>

This error occurs when there is an unexpected issue with the Amazon Pinpoint SMS and Voice API service.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Message | string | False | A description of the error that the API encountered. |

### LimitExceededException
<a name="v1-sms-voice-configuration-sets-model-limitexceededexception"></a>

There are too many instances of the specified resource type.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Message | string | False | A description of the error that the API encountered. |

### ListConfigurationSetsResponse
<a name="v1-sms-voice-configuration-sets-model-listconfigurationsetsresponse"></a>

An object that contains information about configuration sets.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| ConfigurationSets | Array of type string | False | An object that contains a list of configuration sets for your account in the current AWS Region. |
| NextToken | string | False | A token returned from a previous call to ListConfigurationSets to indicate the position in the list of configuration sets. |

### TooManyRequestsException
<a name="v1-sms-voice-configuration-sets-model-toomanyrequestsexception"></a>

This error occurs when there is an unexpected issue with the Amazon Pinpoint SMS and Voice API service.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Message | string | False | A description of the error that the API encountered. |

## See also
<a name="v1-sms-voice-configuration-sets-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### ListConfigurationSets
<a name="ListConfigurationSets-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/pinpoint-sms-voice-2018-09-05/ListConfigurationSets)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/pinpoint-sms-voice-2018-09-05/ListConfigurationSets)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/pinpoint-sms-voice-2018-09-05/ListConfigurationSets)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/pinpoint-sms-voice-2018-09-05/ListConfigurationSets)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/pinpoint-sms-voice-2018-09-05/ListConfigurationSets)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/pinpoint-sms-voice-2018-09-05/ListConfigurationSets)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/pinpoint-sms-voice-2018-09-05/ListConfigurationSets)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/pinpoint-sms-voice-2018-09-05/ListConfigurationSets)
+ [AWS SDK for Python](/goto/boto3/pinpoint-sms-voice-2018-09-05/ListConfigurationSets)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/pinpoint-sms-voice-2018-09-05/ListConfigurationSets)

### CreateConfigurationSet
<a name="CreateConfigurationSet-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/pinpoint-sms-voice-2018-09-05/CreateConfigurationSet)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/pinpoint-sms-voice-2018-09-05/CreateConfigurationSet)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/pinpoint-sms-voice-2018-09-05/CreateConfigurationSet)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/pinpoint-sms-voice-2018-09-05/CreateConfigurationSet)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/pinpoint-sms-voice-2018-09-05/CreateConfigurationSet)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/pinpoint-sms-voice-2018-09-05/CreateConfigurationSet)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/pinpoint-sms-voice-2018-09-05/CreateConfigurationSet)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/pinpoint-sms-voice-2018-09-05/CreateConfigurationSet)
+ [AWS SDK for Python](/goto/boto3/pinpoint-sms-voice-2018-09-05/CreateConfigurationSet)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/pinpoint-sms-voice-2018-09-05/CreateConfigurationSet)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Pinpoint SMS and Voice. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pinpoint-sms-voice` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
