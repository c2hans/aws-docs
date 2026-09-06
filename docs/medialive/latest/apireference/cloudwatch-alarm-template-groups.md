---
source_url: https://docs.aws.amazon.com/medialive/latest/apireference/cloudwatch-alarm-template-groups.html
---

# Workflow monitor: CloudWatch alarm template groups
<a name="cloudwatch-alarm-template-groups"></a>

## URI
<a name="cloudwatch-alarm-template-groups-url"></a>

`/prod/cloudwatch-alarm-template-groups`

## HTTP methods
<a name="cloudwatch-alarm-template-groups-http-methods"></a>

### GET
<a name="cloudwatch-alarm-template-groupsget"></a>

**Operation ID:** `ListCloudWatchAlarmTemplateGroups`

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| signalMapIdentifier | String | False |  |
| scope | String | False |  |
| nextToken | String | False |  |
| maxResults | String | False |  |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | ListCloudWatchAlarmTemplateGroupsResponseContent | 200 response |
| 400 | BadRequestExceptionResponseContent | 400 response |
| 403 | ForbiddenExceptionResponseContent | 403 response |
| 404 | NotFoundExceptionResponseContent | 404 response |
| 429 | TooManyRequestsExceptionResponseContent | 429 response |
| 500 | InternalServerErrorExceptionResponseContent | 500 response |

### OPTIONS
<a name="cloudwatch-alarm-template-groupsoptions"></a>

**Operation ID:** `CorsCloudwatch_alarm_template_groups`

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | 200 response |

### POST
<a name="cloudwatch-alarm-template-groupspost"></a>

**Operation ID:** `CreateCloudWatchAlarmTemplateGroup`

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 201 | CreateCloudWatchAlarmTemplateGroupResponseContent | 201 response |
| 400 | BadRequestExceptionResponseContent | 400 response |
| 403 | ForbiddenExceptionResponseContent | 403 response |
| 404 | NotFoundExceptionResponseContent | 404 response |
| 409 | ConflictExceptionResponseContent | 409 response |
| 429 | TooManyRequestsExceptionResponseContent | 429 response |
| 500 | InternalServerErrorExceptionResponseContent | 500 response |

## Schemas
<a name="cloudwatch-alarm-template-groups-schemas"></a>

### Request bodies
<a name="cloudwatch-alarm-template-groups-request-examples"></a>

#### POST schema
<a name="cloudwatch-alarm-template-groups-request-body-post-example"></a>

```
{
  "description": "string",
  "name": "string"
}
```

### Response bodies
<a name="cloudwatch-alarm-template-groups-response-examples"></a>

#### ListCloudWatchAlarmTemplateGroupsResponseContent schema
<a name="cloudwatch-alarm-template-groups-response-body-listcloudwatchalarmtemplategroupsresponsecontent-example"></a>

```
{
  "cloudWatchAlarmTemplateGroups": [
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

#### CreateCloudWatchAlarmTemplateGroupResponseContent schema
<a name="cloudwatch-alarm-template-groups-response-body-createcloudwatchalarmtemplategroupresponsecontent-example"></a>

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
<a name="cloudwatch-alarm-template-groups-response-body-badrequestexceptionresponsecontent-example"></a>

```
{
  "message": "string"
}
```

#### ForbiddenExceptionResponseContent schema
<a name="cloudwatch-alarm-template-groups-response-body-forbiddenexceptionresponsecontent-example"></a>

```
{
  "message": "string"
}
```

#### NotFoundExceptionResponseContent schema
<a name="cloudwatch-alarm-template-groups-response-body-notfoundexceptionresponsecontent-example"></a>

```
{
  "message": "string"
}
```

#### ConflictExceptionResponseContent schema
<a name="cloudwatch-alarm-template-groups-response-body-conflictexceptionresponsecontent-example"></a>

```
{
  "message": "string"
}
```

#### TooManyRequestsExceptionResponseContent schema
<a name="cloudwatch-alarm-template-groups-response-body-toomanyrequestsexceptionresponsecontent-example"></a>

```
{
  "message": "string"
}
```

#### InternalServerErrorExceptionResponseContent schema
<a name="cloudwatch-alarm-template-groups-response-body-internalservererrorexceptionresponsecontent-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="cloudwatch-alarm-template-groups-properties"></a>

### BadRequestExceptionResponseContent
<a name="cloudwatch-alarm-template-groups-model-badrequestexceptionresponsecontent"></a>

The input fails to satisfy the constraints specified by an Amazon Web Services service.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Exception error message. |

### CloudWatchAlarmTemplateGroupSummary
<a name="cloudwatch-alarm-template-groups-model-cloudwatchalarmtemplategroupsummary"></a>

A summary of the alarm template groups.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| arn | string<br />Pattern: `^arn:.+:medialive:.+:cloudwatch-alarm-template-group:.+$` | True | A cloudwatch alarm template group's ARN (Amazon Resource Name) |
| createdAt | string<br />Format: date-time | True | The date and time of resource creation. |
| description | string<br />MinLength: 0<br />MaxLength: 1024 | False | A resource's optional description. |
| id | string<br />Pattern: `^(aws-)?[0-9]{7}$`<br />MinLength: 7<br />MaxLength: 11 | True | A CloudWatch alarm template group's id. Amazon Web Services provided template groups have ids that start with <code>`aws-`</code> |
| modifiedAt | string<br />Format: date-time | False | The date and time of latest resource modification. |
| name | string<br />Pattern: `^[^\s]+$`<br />MinLength: 1<br />MaxLength: 255 | True | A resource's name. Names must be unique within the scope of a resource type in a specific region. |
| templateCount | number | True | The number of templates in the group. |

### ConflictExceptionResponseContent
<a name="cloudwatch-alarm-template-groups-model-conflictexceptionresponsecontent"></a>

Updating or deleting a resource can cause an inconsistent state.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Exception error message. |

### CreateCloudWatchAlarmTemplateGroupRequestContent
<a name="cloudwatch-alarm-template-groups-model-createcloudwatchalarmtemplategrouprequestcontent"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| description | string<br />MinLength: 0<br />MaxLength: 1024 | False | A resource's optional description. |
| name | string<br />Pattern: `^[^\s]+$`<br />MinLength: 1<br />MaxLength: 255 | True | A resource's name. Names must be unique within the scope of a resource type in a specific region. |

### CreateCloudWatchAlarmTemplateGroupResponseContent
<a name="cloudwatch-alarm-template-groups-model-createcloudwatchalarmtemplategroupresponsecontent"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| arn | string<br />Pattern: `^arn:.+:medialive:.+:cloudwatch-alarm-template-group:.+$` | True | A cloudwatch alarm template group's ARN (Amazon Resource Name) |
| createdAt | string<br />Format: date-time | True | The date and time of resource creation. |
| description | string<br />MinLength: 0<br />MaxLength: 1024 | False | A resource's optional description. |
| id | string<br />Pattern: `^(aws-)?[0-9]{7}$`<br />MinLength: 7<br />MaxLength: 11 | True | A CloudWatch alarm template group's id. Amazon Web Services provided template groups have ids that start with <code>`aws-`</code> |
| modifiedAt | string<br />Format: date-time | False | The date and time of latest resource modification. |
| name | string<br />Pattern: `^[^\s]+$`<br />MinLength: 1<br />MaxLength: 255 | True | A resource's name. Names must be unique within the scope of a resource type in a specific region. |

### ForbiddenExceptionResponseContent
<a name="cloudwatch-alarm-template-groups-model-forbiddenexceptionresponsecontent"></a>

User does not have sufficient access to perform this action.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Exception error message. |

### InternalServerErrorExceptionResponseContent
<a name="cloudwatch-alarm-template-groups-model-internalservererrorexceptionresponsecontent"></a>

Unexpected error during processing of request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Exception error message. |

### ListCloudWatchAlarmTemplateGroupsResponseContent
<a name="cloudwatch-alarm-template-groups-model-listcloudwatchalarmtemplategroupsresponsecontent"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| cloudWatchAlarmTemplateGroups | Array of type [CloudWatchAlarmTemplateGroupSummary](#cloudwatch-alarm-template-groups-model-cloudwatchalarmtemplategroupsummary) | True | A summary of the alarm template groups. |
| nextToken | string<br />MinLength: 1<br />MaxLength: 2048 | False | A token used to retrieve the next set of results in paginated list responses. |

### NotFoundExceptionResponseContent
<a name="cloudwatch-alarm-template-groups-model-notfoundexceptionresponsecontent"></a>

Request references a resource which does not exist.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Exception error message. |

### TooManyRequestsExceptionResponseContent
<a name="cloudwatch-alarm-template-groups-model-toomanyrequestsexceptionresponsecontent"></a>

Request was denied due to request throttling.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Exception error message. |

## See also
<a name="cloudwatch-alarm-template-groups-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### ListCloudWatchAlarmTemplateGroups
<a name="ListCloudWatchAlarmTemplateGroups-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/medialive-2017-10-14/ListCloudWatchAlarmTemplateGroups)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/medialive-2017-10-14/ListCloudWatchAlarmTemplateGroups)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/medialive-2017-10-14/ListCloudWatchAlarmTemplateGroups)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/medialive-2017-10-14/ListCloudWatchAlarmTemplateGroups)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/medialive-2017-10-14/ListCloudWatchAlarmTemplateGroups)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/medialive-2017-10-14/ListCloudWatchAlarmTemplateGroups)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/medialive-2017-10-14/ListCloudWatchAlarmTemplateGroups)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/medialive-2017-10-14/ListCloudWatchAlarmTemplateGroups)
+ [AWS SDK for Python](/goto/boto3/medialive-2017-10-14/ListCloudWatchAlarmTemplateGroups)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/medialive-2017-10-14/ListCloudWatchAlarmTemplateGroups)

### CorsCloudwatch\_alarm\_template\_groups
<a name="CorsCloudwatch_alarm_template_groups-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/medialive-2017-10-14/CorsCloudwatch_alarm_template_groups)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/medialive-2017-10-14/CorsCloudwatch_alarm_template_groups)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/medialive-2017-10-14/CorsCloudwatch_alarm_template_groups)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/medialive-2017-10-14/CorsCloudwatch_alarm_template_groups)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/medialive-2017-10-14/CorsCloudwatch_alarm_template_groups)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/medialive-2017-10-14/CorsCloudwatch_alarm_template_groups)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/medialive-2017-10-14/CorsCloudwatch_alarm_template_groups)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/medialive-2017-10-14/CorsCloudwatch_alarm_template_groups)
+ [AWS SDK for Python](/goto/boto3/medialive-2017-10-14/CorsCloudwatch_alarm_template_groups)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/medialive-2017-10-14/CorsCloudwatch_alarm_template_groups)

### CreateCloudWatchAlarmTemplateGroup
<a name="CreateCloudWatchAlarmTemplateGroup-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/medialive-2017-10-14/CreateCloudWatchAlarmTemplateGroup)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/medialive-2017-10-14/CreateCloudWatchAlarmTemplateGroup)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/medialive-2017-10-14/CreateCloudWatchAlarmTemplateGroup)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/medialive-2017-10-14/CreateCloudWatchAlarmTemplateGroup)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/medialive-2017-10-14/CreateCloudWatchAlarmTemplateGroup)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/medialive-2017-10-14/CreateCloudWatchAlarmTemplateGroup)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/medialive-2017-10-14/CreateCloudWatchAlarmTemplateGroup)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/medialive-2017-10-14/CreateCloudWatchAlarmTemplateGroup)
+ [AWS SDK for Python](/goto/boto3/medialive-2017-10-14/CreateCloudWatchAlarmTemplateGroup)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/medialive-2017-10-14/CreateCloudWatchAlarmTemplateGroup)
