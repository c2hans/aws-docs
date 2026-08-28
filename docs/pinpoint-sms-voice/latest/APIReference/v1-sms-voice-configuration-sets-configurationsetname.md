---
source_url: https://docs.aws.amazon.com/pinpoint-sms-voice/latest/APIReference/v1-sms-voice-configuration-sets-configurationsetname.html
---

**End of support notice:** On October 30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints, segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of support](https://docs.aws.amazon.com/console/pinpoint/migration-guide). **Note:** APIs related to SMS, voice, mobile push, OTP, and phone number validate are not impacted by this change and are supported by AWS End User Messaging.

# Configuration Set
<a name="v1-sms-voice-configuration-sets-configurationsetname"></a>

A *configuration set* is a set of rules that you apply to the voice messages that you send. In a configuration set, you can specify a destination for specific types of events related to voice messages. For example, when a message is successfully delivered, you can log that event to an Amazon CloudWatch destination, or send notifications to endpoints that are subscribed to an Amazon SNS topic.

When you send a voice message, you have to specify one (and only one) configuration set.

## URI
<a name="v1-sms-voice-configuration-sets-configurationsetname-url"></a>

`/v1/sms-voice/configuration-sets/{{ConfigurationSetName}}`

## HTTP methods
<a name="v1-sms-voice-configuration-sets-configurationsetname-http-methods"></a>

### DELETE
<a name="v1-sms-voice-configuration-sets-configurationsetnamedelete"></a>

**Operation ID:** `DeleteConfigurationSet`

Deletes an existing configuration set.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{ConfigurationSetName}} | String | True | The name of the configuration set that you want to delete. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | DeleteConfigurationSetResponse | An empty object that indicates that the configuration set was deleted successfully. |
| 400 | BadRequestException | The request contained syntax that the API couldn't interpret. Modify the request and try again. |
| 404 | NotFoundException | The requested resource wasn't found. |
| 429 | TooManyRequestsException | You've issued too many requests to the resource. Wait a few minutes, and then try again. |
| 500 | InternalServiceErrorException | The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future. |

### OPTIONS
<a name="v1-sms-voice-configuration-sets-configurationsetnameoptions"></a>

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | 200 response |

## Schemas
<a name="v1-sms-voice-configuration-sets-configurationsetname-schemas"></a>

### Response bodies
<a name="v1-sms-voice-configuration-sets-configurationsetname-response-examples"></a>

#### DeleteConfigurationSetResponse schema
<a name="v1-sms-voice-configuration-sets-configurationsetname-response-body-deleteconfigurationsetresponse-example"></a>

```
{
}
```

#### BadRequestException schema
<a name="v1-sms-voice-configuration-sets-configurationsetname-response-body-badrequestexception-example"></a>

```
{
  "Message": "string"
}
```

#### NotFoundException schema
<a name="v1-sms-voice-configuration-sets-configurationsetname-response-body-notfoundexception-example"></a>

```
{
  "Message": "string"
}
```

#### TooManyRequestsException schema
<a name="v1-sms-voice-configuration-sets-configurationsetname-response-body-toomanyrequestsexception-example"></a>

```
{
  "Message": "string"
}
```

#### InternalServiceErrorException schema
<a name="v1-sms-voice-configuration-sets-configurationsetname-response-body-internalserviceerrorexception-example"></a>

```
{
  "Message": "string"
}
```

## Properties
<a name="v1-sms-voice-configuration-sets-configurationsetname-properties"></a>

### BadRequestException
<a name="v1-sms-voice-configuration-sets-configurationsetname-model-badrequestexception"></a>

The input that you provided to the API is invalid.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Message | string | False | A description of the error that the API encountered. |

### DeleteConfigurationSetResponse
<a name="v1-sms-voice-configuration-sets-configurationsetname-model-deleteconfigurationsetresponse"></a>

An empty object that indicates that the configuration set was deleted successfully.

### InternalServiceErrorException
<a name="v1-sms-voice-configuration-sets-configurationsetname-model-internalserviceerrorexception"></a>

This error occurs when there is an unexpected issue with the Amazon Pinpoint SMS and Voice API service.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Message | string | False | A description of the error that the API encountered. |

### NotFoundException
<a name="v1-sms-voice-configuration-sets-configurationsetname-model-notfoundexception"></a>

The resource you attempted to access doesn't exist.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Message | string | False | A description of the error that the API encountered. |

### TooManyRequestsException
<a name="v1-sms-voice-configuration-sets-configurationsetname-model-toomanyrequestsexception"></a>

This error occurs when there is an unexpected issue with the Amazon Pinpoint SMS and Voice API service.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Message | string | False | A description of the error that the API encountered. |

## See also
<a name="v1-sms-voice-configuration-sets-configurationsetname-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### DeleteConfigurationSet
<a name="DeleteConfigurationSet-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/pinpoint-sms-voice-2018-09-05/DeleteConfigurationSet)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/pinpoint-sms-voice-2018-09-05/DeleteConfigurationSet)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/pinpoint-sms-voice-2018-09-05/DeleteConfigurationSet)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/pinpoint-sms-voice-2018-09-05/DeleteConfigurationSet)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/pinpoint-sms-voice-2018-09-05/DeleteConfigurationSet)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/pinpoint-sms-voice-2018-09-05/DeleteConfigurationSet)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/pinpoint-sms-voice-2018-09-05/DeleteConfigurationSet)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/pinpoint-sms-voice-2018-09-05/DeleteConfigurationSet)
+ [AWS SDK for Python](/goto/boto3/pinpoint-sms-voice-2018-09-05/DeleteConfigurationSet)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/pinpoint-sms-voice-2018-09-05/DeleteConfigurationSet)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Pinpoint SMS and Voice. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pinpoint-sms-voice` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
