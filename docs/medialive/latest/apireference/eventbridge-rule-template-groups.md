---
source_url: https://docs.aws.amazon.com/medialive/latest/apireference/eventbridge-rule-template-groups.html
---

# Workflow monitor: EventBridge rule template groups
<a name="eventbridge-rule-template-groups"></a>

## URI
<a name="eventbridge-rule-template-groups-url"></a>

`/prod/eventbridge-rule-template-groups`

## HTTP methods
<a name="eventbridge-rule-template-groups-http-methods"></a>

### GET
<a name="eventbridge-rule-template-groupsget"></a>

**Operation ID:** `ListEventBridgeRuleTemplateGroups`

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| signalMapIdentifier | String | False |  |
| nextToken | String | False |  |
| maxResults | String | False |  |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | ListEventBridgeRuleTemplateGroupsResponseContent | 200 response |
| 400 | BadRequestExceptionResponseContent | 400 response |
| 403 | ForbiddenExceptionResponseContent | 403 response |
| 404 | NotFoundExceptionResponseContent | 404 response |
| 429 | TooManyRequestsExceptionResponseContent | 429 response |
| 500 | InternalServerErrorExceptionResponseContent | 500 response |

### OPTIONS
<a name="eventbridge-rule-template-groupsoptions"></a>

**Operation ID:** `CorsEventbridge_rule_template_groups`

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | 200 response |

### POST
<a name="eventbridge-rule-template-groupspost"></a>

**Operation ID:** `CreateEventBridgeRuleTemplateGroup`

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 201 | CreateEventBridgeRuleTemplateGroupResponseContent | 201 response |
| 400 | BadRequestExceptionResponseContent | 400 response |
| 403 | ForbiddenExceptionResponseContent | 403 response |
| 404 | NotFoundExceptionResponseContent | 404 response |
| 409 | ConflictExceptionResponseContent | 409 response |
| 429 | TooManyRequestsExceptionResponseContent | 429 response |
| 500 | InternalServerErrorExceptionResponseContent | 500 response |

## Schemas
<a name="eventbridge-rule-template-groups-schemas"></a>

### Request bodies
<a name="eventbridge-rule-template-groups-request-examples"></a>

#### POST schema
<a name="eventbridge-rule-template-groups-request-body-post-example"></a>

```
{
  "description": "string",
  "name": "string"
}
```

### Response bodies
<a name="eventbridge-rule-template-groups-response-examples"></a>

#### ListEventBridgeRuleTemplateGroupsResponseContent schema
<a name="eventbridge-rule-template-groups-response-body-listeventbridgeruletemplategroupsresponsecontent-example"></a>

```
{
  "eventBridgeRuleTemplateGroups": [
    {
      "arn": "string",
      "createdAt": "string",
      "description": "string",
      "id": "string",
      "modifiedAt": "string",
      "name": "string",
      "templateCount": number
    }
  ],
  "nextToken": "string"
}
```

#### CreateEventBridgeRuleTemplateGroupResponseContent schema
<a name="eventbridge-rule-template-groups-response-body-createeventbridgeruletemplategroupresponsecontent-example"></a>

```
{
  "arn": "string",
  "createdAt": "string",
  "description": "string",
  "id": "string",
  "modifiedAt": "string",
  "name": "string"
}
```

#### BadRequestExceptionResponseContent schema
<a name="eventbridge-rule-template-groups-response-body-badrequestexceptionresponsecontent-example"></a>

```
{
  "message": "string"
}
```

#### ForbiddenExceptionResponseContent schema
<a name="eventbridge-rule-template-groups-response-body-forbiddenexceptionresponsecontent-example"></a>

```
{
  "message": "string"
}
```

#### NotFoundExceptionResponseContent schema
<a name="eventbridge-rule-template-groups-response-body-notfoundexceptionresponsecontent-example"></a>

```
{
  "message": "string"
}
```

#### ConflictExceptionResponseContent schema
<a name="eventbridge-rule-template-groups-response-body-conflictexceptionresponsecontent-example"></a>

```
{
  "message": "string"
}
```

#### TooManyRequestsExceptionResponseContent schema
<a name="eventbridge-rule-template-groups-response-body-toomanyrequestsexceptionresponsecontent-example"></a>

```
{
  "message": "string"
}
```

#### InternalServerErrorExceptionResponseContent schema
<a name="eventbridge-rule-template-groups-response-body-internalservererrorexceptionresponsecontent-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="eventbridge-rule-template-groups-properties"></a>

### BadRequestExceptionResponseContent
<a name="eventbridge-rule-template-groups-model-badrequestexceptionresponsecontent"></a>

The input fails to satisfy the constraints specified by an Amazon Web Services service.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Exception error message. |

### ConflictExceptionResponseContent
<a name="eventbridge-rule-template-groups-model-conflictexceptionresponsecontent"></a>

Updating or deleting a resource can cause an inconsistent state.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Exception error message. |

### CreateEventBridgeRuleTemplateGroupRequestContent
<a name="eventbridge-rule-template-groups-model-createeventbridgeruletemplategrouprequestcontent"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| description | string<br />MinLength: 0<br />MaxLength: 1024 | False | A resource's optional description. |
| name | string<br />Pattern: `^[^\s]+$`<br />MinLength: 1<br />MaxLength: 255 | True | A resource's name. Names must be unique within the scope of a resource type in a specific region. |

### CreateEventBridgeRuleTemplateGroupResponseContent
<a name="eventbridge-rule-template-groups-model-createeventbridgeruletemplategroupresponsecontent"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| arn | string<br />Pattern: `^arn:.+:medialive:.+:eventbridge-rule-template-group:.+$` | True | An eventbridge rule template group's ARN (Amazon Resource Name) |
| createdAt | string<br />Format: date-time | True | The date and time of resource creation. |
| description | string<br />MinLength: 0<br />MaxLength: 1024 | False | A resource's optional description. |
| id | string<br />Pattern: `^(aws-)?[0-9]{7}$`<br />MinLength: 7<br />MaxLength: 11 | True | An eventbridge rule template group's id. Amazon Web Services provided template groups have ids that start with <code>`aws-`</code>. |
| modifiedAt | string<br />Format: date-time | False | The date and time of latest resource modification. |
| name | string<br />Pattern: `^[^\s]+$`<br />MinLength: 1<br />MaxLength: 255 | True | A resource's name. Names must be unique within the scope of a resource type in a specific region. |

### EventBridgeRuleTemplateGroupSummary
<a name="eventbridge-rule-template-groups-model-eventbridgeruletemplategroupsummary"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| arn | string<br />Pattern: `^arn:.+:medialive:.+:eventbridge-rule-template-group:.+$` | True | An eventbridge rule template group's ARN (Amazon Resource Name) |
| createdAt | string<br />Format: date-time | True | The date and time of resource creation. |
| description | string<br />MinLength: 0<br />MaxLength: 1024 | False | A resource's optional description. |
| id | string<br />Pattern: `^(aws-)?[0-9]{7}$`<br />MinLength: 7<br />MaxLength: 11 | True | An eventbridge rule template group's id. Amazon Web Services provided template groups have ids that start with <code>`aws-`</code>. |
| modifiedAt | string<br />Format: date-time | False | The date and time of latest resource modification. |
| name | string<br />Pattern: `^[^\s]+$`<br />MinLength: 1<br />MaxLength: 255 | True | A resource's name. Names must be unique within the scope of a resource type in a specific region. |
| templateCount | number | True | The number of templates in the group. |

### ForbiddenExceptionResponseContent
<a name="eventbridge-rule-template-groups-model-forbiddenexceptionresponsecontent"></a>

User does not have sufficient access to perform this action.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Exception error message. |

### InternalServerErrorExceptionResponseContent
<a name="eventbridge-rule-template-groups-model-internalservererrorexceptionresponsecontent"></a>

Unexpected error during processing of request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Exception error message. |

### ListEventBridgeRuleTemplateGroupsResponseContent
<a name="eventbridge-rule-template-groups-model-listeventbridgeruletemplategroupsresponsecontent"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| eventBridgeRuleTemplateGroups | Array of type [EventBridgeRuleTemplateGroupSummary](#eventbridge-rule-template-groups-model-eventbridgeruletemplategroupsummary) | True | A list of EventBridge rule template groups. |
| nextToken | string<br />MinLength: 1<br />MaxLength: 2048 | False | A token used to retrieve the next set of results in paginated list responses. |

### NotFoundExceptionResponseContent
<a name="eventbridge-rule-template-groups-model-notfoundexceptionresponsecontent"></a>

Request references a resource which does not exist.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Exception error message. |

### TooManyRequestsExceptionResponseContent
<a name="eventbridge-rule-template-groups-model-toomanyrequestsexceptionresponsecontent"></a>

Request was denied due to request throttling.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Exception error message. |

## See also
<a name="eventbridge-rule-template-groups-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### ListEventBridgeRuleTemplateGroups
<a name="ListEventBridgeRuleTemplateGroups-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/medialive-2017-10-14/ListEventBridgeRuleTemplateGroups)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/medialive-2017-10-14/ListEventBridgeRuleTemplateGroups)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/medialive-2017-10-14/ListEventBridgeRuleTemplateGroups)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/medialive-2017-10-14/ListEventBridgeRuleTemplateGroups)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/medialive-2017-10-14/ListEventBridgeRuleTemplateGroups)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/medialive-2017-10-14/ListEventBridgeRuleTemplateGroups)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/medialive-2017-10-14/ListEventBridgeRuleTemplateGroups)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/medialive-2017-10-14/ListEventBridgeRuleTemplateGroups)
+ [AWS SDK for Python](/goto/boto3/medialive-2017-10-14/ListEventBridgeRuleTemplateGroups)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/medialive-2017-10-14/ListEventBridgeRuleTemplateGroups)

### CorsEventbridge\_rule\_template\_groups
<a name="CorsEventbridge_rule_template_groups-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/medialive-2017-10-14/CorsEventbridge_rule_template_groups)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/medialive-2017-10-14/CorsEventbridge_rule_template_groups)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/medialive-2017-10-14/CorsEventbridge_rule_template_groups)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/medialive-2017-10-14/CorsEventbridge_rule_template_groups)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/medialive-2017-10-14/CorsEventbridge_rule_template_groups)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/medialive-2017-10-14/CorsEventbridge_rule_template_groups)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/medialive-2017-10-14/CorsEventbridge_rule_template_groups)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/medialive-2017-10-14/CorsEventbridge_rule_template_groups)
+ [AWS SDK for Python](/goto/boto3/medialive-2017-10-14/CorsEventbridge_rule_template_groups)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/medialive-2017-10-14/CorsEventbridge_rule_template_groups)

### CreateEventBridgeRuleTemplateGroup
<a name="CreateEventBridgeRuleTemplateGroup-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/medialive-2017-10-14/CreateEventBridgeRuleTemplateGroup)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/medialive-2017-10-14/CreateEventBridgeRuleTemplateGroup)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/medialive-2017-10-14/CreateEventBridgeRuleTemplateGroup)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/medialive-2017-10-14/CreateEventBridgeRuleTemplateGroup)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/medialive-2017-10-14/CreateEventBridgeRuleTemplateGroup)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/medialive-2017-10-14/CreateEventBridgeRuleTemplateGroup)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/medialive-2017-10-14/CreateEventBridgeRuleTemplateGroup)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/medialive-2017-10-14/CreateEventBridgeRuleTemplateGroup)
+ [AWS SDK for Python](/goto/boto3/medialive-2017-10-14/CreateEventBridgeRuleTemplateGroup)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/medialive-2017-10-14/CreateEventBridgeRuleTemplateGroup)
