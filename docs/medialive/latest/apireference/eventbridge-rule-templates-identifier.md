---
source_url: https://docs.aws.amazon.com/medialive/latest/apireference/eventbridge-rule-templates-identifier.html
---

# Workflow monitor: EventBridge rule templates ID
<a name="eventbridge-rule-templates-identifier"></a>

## URI
<a name="eventbridge-rule-templates-identifier-url"></a>

`/prod/eventbridge-rule-templates/{{identifier}}`

## HTTP methods
<a name="eventbridge-rule-templates-identifier-http-methods"></a>

### DELETE
<a name="eventbridge-rule-templates-identifierdelete"></a>

**Operation ID:** `DeleteEventBridgeRuleTemplate`

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{identifier}} | String | True |  |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 204 | None | 204 response |
| 400 | BadRequestExceptionResponseContent | 400 response |
| 403 | ForbiddenExceptionResponseContent | 403 response |
| 404 | NotFoundExceptionResponseContent | 404 response |
| 409 | ConflictExceptionResponseContent | 409 response |
| 429 | TooManyRequestsExceptionResponseContent | 429 response |
| 500 | InternalServerErrorExceptionResponseContent | 500 response |

### GET
<a name="eventbridge-rule-templates-identifierget"></a>

**Operation ID:** `GetEventBridgeRuleTemplate`

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{identifier}} | String | True |  |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | GetEventBridgeRuleTemplateResponseContent | 200 response |
| 400 | BadRequestExceptionResponseContent | 400 response |
| 403 | ForbiddenExceptionResponseContent | 403 response |
| 404 | NotFoundExceptionResponseContent | 404 response |
| 429 | TooManyRequestsExceptionResponseContent | 429 response |
| 500 | InternalServerErrorExceptionResponseContent | 500 response |

### OPTIONS
<a name="eventbridge-rule-templates-identifieroptions"></a>

**Operation ID:** `CorsEventbridge_rule_templatesIdentifier`

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{identifier}} | String | True |  |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | 200 response |

### PATCH
<a name="eventbridge-rule-templates-identifierpatch"></a>

**Operation ID:** `UpdateEventBridgeRuleTemplate`

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{identifier}} | String | True |  |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | UpdateEventBridgeRuleTemplateResponseContent | 200 response |
| 400 | BadRequestExceptionResponseContent | 400 response |
| 403 | ForbiddenExceptionResponseContent | 403 response |
| 404 | NotFoundExceptionResponseContent | 404 response |
| 409 | ConflictExceptionResponseContent | 409 response |
| 429 | TooManyRequestsExceptionResponseContent | 429 response |
| 500 | InternalServerErrorExceptionResponseContent | 500 response |

## Schemas
<a name="eventbridge-rule-templates-identifier-schemas"></a>

### Request bodies
<a name="eventbridge-rule-templates-identifier-request-examples"></a>

#### PATCH schema
<a name="eventbridge-rule-templates-identifier-request-body-patch-example"></a>

```
{
  "description": "string",
  "eventTargets": [
    {
      "arn": "string"
    }
  ],
  "eventType": enum,
  "groupIdentifier": "string",
  "name": "string"
}
```

### Response bodies
<a name="eventbridge-rule-templates-identifier-response-examples"></a>

#### GetEventBridgeRuleTemplateResponseContent schema
<a name="eventbridge-rule-templates-identifier-response-body-geteventbridgeruletemplateresponsecontent-example"></a>

```
{
  "arn": "string",
  "createdAt": "string",
  "description": "string",
  "eventTargets": [
    {
      "arn": "string"
    }
  ],
  "eventType": enum,
  "groupId": "string",
  "id": "string",
  "modifiedAt": "string",
  "name": "string"
}
```

#### UpdateEventBridgeRuleTemplateResponseContent schema
<a name="eventbridge-rule-templates-identifier-response-body-updateeventbridgeruletemplateresponsecontent-example"></a>

```
{
  "arn": "string",
  "createdAt": "string",
  "description": "string",
  "eventTargets": [
    {
      "arn": "string"
    }
  ],
  "eventType": enum,
  "groupId": "string",
  "id": "string",
  "modifiedAt": "string",
  "name": "string"
}
```

#### BadRequestExceptionResponseContent schema
<a name="eventbridge-rule-templates-identifier-response-body-badrequestexceptionresponsecontent-example"></a>

```
{
  "message": "string"
}
```

#### ForbiddenExceptionResponseContent schema
<a name="eventbridge-rule-templates-identifier-response-body-forbiddenexceptionresponsecontent-example"></a>

```
{
  "message": "string"
}
```

#### NotFoundExceptionResponseContent schema
<a name="eventbridge-rule-templates-identifier-response-body-notfoundexceptionresponsecontent-example"></a>

```
{
  "message": "string"
}
```

#### ConflictExceptionResponseContent schema
<a name="eventbridge-rule-templates-identifier-response-body-conflictexceptionresponsecontent-example"></a>

```
{
  "message": "string"
}
```

#### TooManyRequestsExceptionResponseContent schema
<a name="eventbridge-rule-templates-identifier-response-body-toomanyrequestsexceptionresponsecontent-example"></a>

```
{
  "message": "string"
}
```

#### InternalServerErrorExceptionResponseContent schema
<a name="eventbridge-rule-templates-identifier-response-body-internalservererrorexceptionresponsecontent-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="eventbridge-rule-templates-identifier-properties"></a>

### BadRequestExceptionResponseContent
<a name="eventbridge-rule-templates-identifier-model-badrequestexceptionresponsecontent"></a>

The input fails to satisfy the constraints specified by an Amazon Web Services service.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Exception error message. |

### ConflictExceptionResponseContent
<a name="eventbridge-rule-templates-identifier-model-conflictexceptionresponsecontent"></a>

Updating or deleting a resource can cause an inconsistent state.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Exception error message. |

### EventBridgeRuleTemplateEventType
<a name="eventbridge-rule-templates-identifier-model-eventbridgeruletemplateeventtype"></a>

The type of event to match with the rule.
+ `MEDIALIVE_MULTIPLEX_ALERT`
+ `MEDIALIVE_MULTIPLEX_STATE_CHANGE`
+ `MEDIALIVE_CHANNEL_ALERT`
+ `MEDIALIVE_CHANNEL_INPUT_CHANGE`
+ `MEDIALIVE_CHANNEL_STATE_CHANGE`
+ `MEDIAPACKAGE_INPUT_NOTIFICATION`
+ `MEDIAPACKAGE_KEY_PROVIDER_NOTIFICATION`
+ `MEDIAPACKAGE_HARVEST_JOB_NOTIFICATION`
+ `SIGNAL_MAP_ACTIVE_ALARM`
+ `MEDIACONNECT_ALERT`
+ `MEDIACONNECT_SOURCE_HEALTH`
+ `MEDIACONNECT_OUTPUT_HEALTH`
+ `MEDIACONNECT_FLOW_STATUS_CHANGE`

### EventBridgeRuleTemplateTarget
<a name="eventbridge-rule-templates-identifier-model-eventbridgeruletemplatetarget"></a>

The target to which to send matching events.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| arn | string<br />Pattern: `^arn.+$`<br />MinLength: 1<br />MaxLength: 2048 | True | Target ARNs must be either an SNS topic or CloudWatch log group. |

### ForbiddenExceptionResponseContent
<a name="eventbridge-rule-templates-identifier-model-forbiddenexceptionresponsecontent"></a>

User does not have sufficient access to perform this action.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Exception error message. |

### GetEventBridgeRuleTemplateResponseContent
<a name="eventbridge-rule-templates-identifier-model-geteventbridgeruletemplateresponsecontent"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| arn | string<br />Pattern: `^arn:.+:medialive:.+:eventbridge-rule-template:.+$` | True | An eventbridge rule template's ARN (Amazon Resource Name) |
| createdAt | string<br />Format: date-time | True | The date and time of resource creation. |
| description | string<br />MinLength: 0<br />MaxLength: 1024 | False | A resource's optional description. |
| eventTargets | Array of type [EventBridgeRuleTemplateTarget](#eventbridge-rule-templates-identifier-model-eventbridgeruletemplatetarget) | True | The destinations that will receive the event notifications. |
| eventType | [EventBridgeRuleTemplateEventType](#eventbridge-rule-templates-identifier-model-eventbridgeruletemplateeventtype) | True | The type of event to match with the rule. |
| groupId | string<br />Pattern: `^(aws-)?[0-9]{7}$`<br />MinLength: 7<br />MaxLength: 11 | True | An eventbridge rule template group's id. Amazon Web Services provided template groups have ids that start with <code>`aws-`</code>. |
| id | string<br />Pattern: `^(aws-)?[0-9]{7}$`<br />MinLength: 7<br />MaxLength: 11 | True | An eventbridge rule template's id. Amazon Web Services provided templates have ids that start with <code>`aws-`</code> |
| modifiedAt | string<br />Format: date-time | False | The date and time of latest resource modification. |
| name | string<br />Pattern: `^[^\s]+$`<br />MinLength: 1<br />MaxLength: 255 | True | A resource's name. Names must be unique within the scope of a resource type in a specific region. |

### InternalServerErrorExceptionResponseContent
<a name="eventbridge-rule-templates-identifier-model-internalservererrorexceptionresponsecontent"></a>

Unexpected error during processing of request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Exception error message. |

### NotFoundExceptionResponseContent
<a name="eventbridge-rule-templates-identifier-model-notfoundexceptionresponsecontent"></a>

Request references a resource which does not exist.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Exception error message. |

### TooManyRequestsExceptionResponseContent
<a name="eventbridge-rule-templates-identifier-model-toomanyrequestsexceptionresponsecontent"></a>

Request was denied due to request throttling.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Exception error message. |

### UpdateEventBridgeRuleTemplateRequestContent
<a name="eventbridge-rule-templates-identifier-model-updateeventbridgeruletemplaterequestcontent"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| description | string<br />MinLength: 0<br />MaxLength: 1024 | False | A resource's optional description. |
| eventTargets | Array of type [EventBridgeRuleTemplateTarget](#eventbridge-rule-templates-identifier-model-eventbridgeruletemplatetarget) | False | The destinations that will receive the event notifications. |
| eventType | [EventBridgeRuleTemplateEventType](#eventbridge-rule-templates-identifier-model-eventbridgeruletemplateeventtype) | False | The type of event to match with the rule. |
| groupIdentifier | string<br />Pattern: `^[^\s]+$` | False | An eventbridge rule template group's identifier. Can be either be its id or current name. |
| name | string<br />Pattern: `^[^\s]+$`<br />MinLength: 1<br />MaxLength: 255 | False | A resource's name. Names must be unique within the scope of a resource type in a specific region. |

### UpdateEventBridgeRuleTemplateResponseContent
<a name="eventbridge-rule-templates-identifier-model-updateeventbridgeruletemplateresponsecontent"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| arn | string<br />Pattern: `^arn:.+:medialive:.+:eventbridge-rule-template:.+$` | True | An eventbridge rule template's ARN (Amazon Resource Name) |
| createdAt | string<br />Format: date-time | True | The date and time of resource creation. |
| description | string<br />MinLength: 0<br />MaxLength: 1024 | False | A resource's optional description. |
| eventTargets | Array of type [EventBridgeRuleTemplateTarget](#eventbridge-rule-templates-identifier-model-eventbridgeruletemplatetarget) | True | The destinations that will receive the event notifications. |
| eventType | [EventBridgeRuleTemplateEventType](#eventbridge-rule-templates-identifier-model-eventbridgeruletemplateeventtype) | True | The type of event to match with the rule. |
| groupId | string<br />Pattern: `^(aws-)?[0-9]{7}$`<br />MinLength: 7<br />MaxLength: 11 | True | An eventbridge rule template group's id. Amazon Web Services provided template groups have ids that start with <code>`aws-`</code>. |
| id | string<br />Pattern: `^(aws-)?[0-9]{7}$`<br />MinLength: 7<br />MaxLength: 11 | True | An eventbridge rule template's id. Amazon Web Services provided templates have ids that start with <code>`aws-`</code> |
| modifiedAt | string<br />Format: date-time | False | The date and time of latest resource modification. |
| name | string<br />Pattern: `^[^\s]+$`<br />MinLength: 1<br />MaxLength: 255 | True | A resource's name. Names must be unique within the scope of a resource type in a specific region. |

## See also
<a name="eventbridge-rule-templates-identifier-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### DeleteEventBridgeRuleTemplate
<a name="DeleteEventBridgeRuleTemplate-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/medialive-2017-10-14/DeleteEventBridgeRuleTemplate)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/medialive-2017-10-14/DeleteEventBridgeRuleTemplate)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/medialive-2017-10-14/DeleteEventBridgeRuleTemplate)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/medialive-2017-10-14/DeleteEventBridgeRuleTemplate)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/medialive-2017-10-14/DeleteEventBridgeRuleTemplate)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/medialive-2017-10-14/DeleteEventBridgeRuleTemplate)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/medialive-2017-10-14/DeleteEventBridgeRuleTemplate)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/medialive-2017-10-14/DeleteEventBridgeRuleTemplate)
+ [AWS SDK for Python](/goto/boto3/medialive-2017-10-14/DeleteEventBridgeRuleTemplate)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/medialive-2017-10-14/DeleteEventBridgeRuleTemplate)

### GetEventBridgeRuleTemplate
<a name="GetEventBridgeRuleTemplate-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/medialive-2017-10-14/GetEventBridgeRuleTemplate)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/medialive-2017-10-14/GetEventBridgeRuleTemplate)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/medialive-2017-10-14/GetEventBridgeRuleTemplate)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/medialive-2017-10-14/GetEventBridgeRuleTemplate)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/medialive-2017-10-14/GetEventBridgeRuleTemplate)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/medialive-2017-10-14/GetEventBridgeRuleTemplate)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/medialive-2017-10-14/GetEventBridgeRuleTemplate)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/medialive-2017-10-14/GetEventBridgeRuleTemplate)
+ [AWS SDK for Python](/goto/boto3/medialive-2017-10-14/GetEventBridgeRuleTemplate)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/medialive-2017-10-14/GetEventBridgeRuleTemplate)

### CorsEventbridge\_rule\_templatesIdentifier
<a name="CorsEventbridge_rule_templatesIdentifier-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/medialive-2017-10-14/CorsEventbridge_rule_templatesIdentifier)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/medialive-2017-10-14/CorsEventbridge_rule_templatesIdentifier)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/medialive-2017-10-14/CorsEventbridge_rule_templatesIdentifier)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/medialive-2017-10-14/CorsEventbridge_rule_templatesIdentifier)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/medialive-2017-10-14/CorsEventbridge_rule_templatesIdentifier)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/medialive-2017-10-14/CorsEventbridge_rule_templatesIdentifier)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/medialive-2017-10-14/CorsEventbridge_rule_templatesIdentifier)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/medialive-2017-10-14/CorsEventbridge_rule_templatesIdentifier)
+ [AWS SDK for Python](/goto/boto3/medialive-2017-10-14/CorsEventbridge_rule_templatesIdentifier)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/medialive-2017-10-14/CorsEventbridge_rule_templatesIdentifier)

### UpdateEventBridgeRuleTemplate
<a name="UpdateEventBridgeRuleTemplate-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/medialive-2017-10-14/UpdateEventBridgeRuleTemplate)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/medialive-2017-10-14/UpdateEventBridgeRuleTemplate)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/medialive-2017-10-14/UpdateEventBridgeRuleTemplate)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/medialive-2017-10-14/UpdateEventBridgeRuleTemplate)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/medialive-2017-10-14/UpdateEventBridgeRuleTemplate)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/medialive-2017-10-14/UpdateEventBridgeRuleTemplate)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/medialive-2017-10-14/UpdateEventBridgeRuleTemplate)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/medialive-2017-10-14/UpdateEventBridgeRuleTemplate)
+ [AWS SDK for Python](/goto/boto3/medialive-2017-10-14/UpdateEventBridgeRuleTemplate)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/medialive-2017-10-14/UpdateEventBridgeRuleTemplate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
