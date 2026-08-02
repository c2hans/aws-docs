---
source_url: https://docs.aws.amazon.com/medialive/latest/apireference/cloudwatch-alarm-template-groups-identifier.html
---

# Workflow monitor: CloudWatch alarm template groups ID
<a name="cloudwatch-alarm-template-groups-identifier"></a>

## URI
<a name="cloudwatch-alarm-template-groups-identifier-url"></a>

`/prod/cloudwatch-alarm-template-groups/{{identifier}}`

## HTTP methods
<a name="cloudwatch-alarm-template-groups-identifier-http-methods"></a>

### DELETE
<a name="cloudwatch-alarm-template-groups-identifierdelete"></a>

**Operation ID:** `DeleteCloudWatchAlarmTemplateGroup`

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
<a name="cloudwatch-alarm-template-groups-identifierget"></a>

**Operation ID:** `GetCloudWatchAlarmTemplateGroup`

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{identifier}} | String | True |  |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | GetCloudWatchAlarmTemplateGroupResponseContent | 200 response |
| 400 | BadRequestExceptionResponseContent | 400 response |
| 403 | ForbiddenExceptionResponseContent | 403 response |
| 404 | NotFoundExceptionResponseContent | 404 response |
| 429 | TooManyRequestsExceptionResponseContent | 429 response |
| 500 | InternalServerErrorExceptionResponseContent | 500 response |

### OPTIONS
<a name="cloudwatch-alarm-template-groups-identifieroptions"></a>

**Operation ID:** `CorsCloudwatch_alarm_template_groupsIdentifier`

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{identifier}} | String | True |  |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | 200 response |

### PATCH
<a name="cloudwatch-alarm-template-groups-identifierpatch"></a>

**Operation ID:** `UpdateCloudWatchAlarmTemplateGroup`

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{identifier}} | String | True |  |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | UpdateCloudWatchAlarmTemplateGroupResponseContent | 200 response |
| 400 | BadRequestExceptionResponseContent | 400 response |
| 403 | ForbiddenExceptionResponseContent | 403 response |
| 404 | NotFoundExceptionResponseContent | 404 response |
| 409 | ConflictExceptionResponseContent | 409 response |
| 429 | TooManyRequestsExceptionResponseContent | 429 response |
| 500 | InternalServerErrorExceptionResponseContent | 500 response |

## Schemas
<a name="cloudwatch-alarm-template-groups-identifier-schemas"></a>

### Request bodies
<a name="cloudwatch-alarm-template-groups-identifier-request-examples"></a>

#### PATCH schema
<a name="cloudwatch-alarm-template-groups-identifier-request-body-patch-example"></a>

```
{
  "description": "string"
}
```

### Response bodies
<a name="cloudwatch-alarm-template-groups-identifier-response-examples"></a>

#### GetCloudWatchAlarmTemplateGroupResponseContent schema
<a name="cloudwatch-alarm-template-groups-identifier-response-body-getcloudwatchalarmtemplategroupresponsecontent-example"></a>

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

#### UpdateCloudWatchAlarmTemplateGroupResponseContent schema
<a name="cloudwatch-alarm-template-groups-identifier-response-body-updatecloudwatchalarmtemplategroupresponsecontent-example"></a>

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
<a name="cloudwatch-alarm-template-groups-identifier-response-body-badrequestexceptionresponsecontent-example"></a>

```
{
  "message": "string"
}
```

#### ForbiddenExceptionResponseContent schema
<a name="cloudwatch-alarm-template-groups-identifier-response-body-forbiddenexceptionresponsecontent-example"></a>

```
{
  "message": "string"
}
```

#### NotFoundExceptionResponseContent schema
<a name="cloudwatch-alarm-template-groups-identifier-response-body-notfoundexceptionresponsecontent-example"></a>

```
{
  "message": "string"
}
```

#### ConflictExceptionResponseContent schema
<a name="cloudwatch-alarm-template-groups-identifier-response-body-conflictexceptionresponsecontent-example"></a>

```
{
  "message": "string"
}
```

#### TooManyRequestsExceptionResponseContent schema
<a name="cloudwatch-alarm-template-groups-identifier-response-body-toomanyrequestsexceptionresponsecontent-example"></a>

```
{
  "message": "string"
}
```

#### InternalServerErrorExceptionResponseContent schema
<a name="cloudwatch-alarm-template-groups-identifier-response-body-internalservererrorexceptionresponsecontent-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="cloudwatch-alarm-template-groups-identifier-properties"></a>

### BadRequestExceptionResponseContent
<a name="cloudwatch-alarm-template-groups-identifier-model-badrequestexceptionresponsecontent"></a>

The input fails to satisfy the constraints specified by an Amazon Web Services service.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Exception error message. |

### ConflictExceptionResponseContent
<a name="cloudwatch-alarm-template-groups-identifier-model-conflictexceptionresponsecontent"></a>

Updating or deleting a resource can cause an inconsistent state.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Exception error message. |

### ForbiddenExceptionResponseContent
<a name="cloudwatch-alarm-template-groups-identifier-model-forbiddenexceptionresponsecontent"></a>

User does not have sufficient access to perform this action.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Exception error message. |

### GetCloudWatchAlarmTemplateGroupResponseContent
<a name="cloudwatch-alarm-template-groups-identifier-model-getcloudwatchalarmtemplategroupresponsecontent"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| arn | string<br />Pattern: `^arn:.+:medialive:.+:cloudwatch-alarm-template-group:.+$` | True | A cloudwatch alarm template group's ARN (Amazon Resource Name) |
| createdAt | string<br />Format: date-time | True | The date and time of resource creation. |
| description | string<br />MinLength: 0<br />MaxLength: 1024 | False | A resource's optional description. |
| id | string<br />Pattern: `^(aws-)?[0-9]{7}$`<br />MinLength: 7<br />MaxLength: 11 | True | A CloudWatch alarm template group's id. Amazon Web Services provided template groups have ids that start with <code>`aws-`</code> |
| modifiedAt | string<br />Format: date-time | False | The date and time of latest resource modification. |
| name | string<br />Pattern: `^[^\s]+$`<br />MinLength: 1<br />MaxLength: 255 | True | A resource's name. Names must be unique within the scope of a resource type in a specific region. |

### InternalServerErrorExceptionResponseContent
<a name="cloudwatch-alarm-template-groups-identifier-model-internalservererrorexceptionresponsecontent"></a>

Unexpected error during processing of request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Exception error message. |

### NotFoundExceptionResponseContent
<a name="cloudwatch-alarm-template-groups-identifier-model-notfoundexceptionresponsecontent"></a>

Request references a resource which does not exist.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Exception error message. |

### TooManyRequestsExceptionResponseContent
<a name="cloudwatch-alarm-template-groups-identifier-model-toomanyrequestsexceptionresponsecontent"></a>

Request was denied due to request throttling.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Exception error message. |

### UpdateCloudWatchAlarmTemplateGroupRequestContent
<a name="cloudwatch-alarm-template-groups-identifier-model-updatecloudwatchalarmtemplategrouprequestcontent"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| description | string<br />MinLength: 0<br />MaxLength: 1024 | False | A resource's optional description. |

### UpdateCloudWatchAlarmTemplateGroupResponseContent
<a name="cloudwatch-alarm-template-groups-identifier-model-updatecloudwatchalarmtemplategroupresponsecontent"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| arn | string<br />Pattern: `^arn:.+:medialive:.+:cloudwatch-alarm-template-group:.+$` | True | A cloudwatch alarm template group's ARN (Amazon Resource Name) |
| createdAt | string<br />Format: date-time | True | The date and time of resource creation. |
| description | string<br />MinLength: 0<br />MaxLength: 1024 | False | A resource's optional description. |
| id | string<br />Pattern: `^(aws-)?[0-9]{7}$`<br />MinLength: 7<br />MaxLength: 11 | True | A CloudWatch alarm template group's id. Amazon Web Services provided template groups have ids that start with <code>`aws-`</code> |
| modifiedAt | string<br />Format: date-time | False | The date and time of latest resource modification. |
| name | string<br />Pattern: `^[^\s]+$`<br />MinLength: 1<br />MaxLength: 255 | True | A resource's name. Names must be unique within the scope of a resource type in a specific region. |

## See also
<a name="cloudwatch-alarm-template-groups-identifier-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### DeleteCloudWatchAlarmTemplateGroup
<a name="DeleteCloudWatchAlarmTemplateGroup-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/medialive-2017-10-14/DeleteCloudWatchAlarmTemplateGroup)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/medialive-2017-10-14/DeleteCloudWatchAlarmTemplateGroup)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/medialive-2017-10-14/DeleteCloudWatchAlarmTemplateGroup)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/medialive-2017-10-14/DeleteCloudWatchAlarmTemplateGroup)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/medialive-2017-10-14/DeleteCloudWatchAlarmTemplateGroup)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/medialive-2017-10-14/DeleteCloudWatchAlarmTemplateGroup)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/medialive-2017-10-14/DeleteCloudWatchAlarmTemplateGroup)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/medialive-2017-10-14/DeleteCloudWatchAlarmTemplateGroup)
+ [AWS SDK for Python](/goto/boto3/medialive-2017-10-14/DeleteCloudWatchAlarmTemplateGroup)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/medialive-2017-10-14/DeleteCloudWatchAlarmTemplateGroup)

### GetCloudWatchAlarmTemplateGroup
<a name="GetCloudWatchAlarmTemplateGroup-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/medialive-2017-10-14/GetCloudWatchAlarmTemplateGroup)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/medialive-2017-10-14/GetCloudWatchAlarmTemplateGroup)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/medialive-2017-10-14/GetCloudWatchAlarmTemplateGroup)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/medialive-2017-10-14/GetCloudWatchAlarmTemplateGroup)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/medialive-2017-10-14/GetCloudWatchAlarmTemplateGroup)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/medialive-2017-10-14/GetCloudWatchAlarmTemplateGroup)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/medialive-2017-10-14/GetCloudWatchAlarmTemplateGroup)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/medialive-2017-10-14/GetCloudWatchAlarmTemplateGroup)
+ [AWS SDK for Python](/goto/boto3/medialive-2017-10-14/GetCloudWatchAlarmTemplateGroup)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/medialive-2017-10-14/GetCloudWatchAlarmTemplateGroup)

### CorsCloudwatch\_alarm\_template\_groupsIdentifier
<a name="CorsCloudwatch_alarm_template_groupsIdentifier-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/medialive-2017-10-14/CorsCloudwatch_alarm_template_groupsIdentifier)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/medialive-2017-10-14/CorsCloudwatch_alarm_template_groupsIdentifier)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/medialive-2017-10-14/CorsCloudwatch_alarm_template_groupsIdentifier)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/medialive-2017-10-14/CorsCloudwatch_alarm_template_groupsIdentifier)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/medialive-2017-10-14/CorsCloudwatch_alarm_template_groupsIdentifier)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/medialive-2017-10-14/CorsCloudwatch_alarm_template_groupsIdentifier)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/medialive-2017-10-14/CorsCloudwatch_alarm_template_groupsIdentifier)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/medialive-2017-10-14/CorsCloudwatch_alarm_template_groupsIdentifier)
+ [AWS SDK for Python](/goto/boto3/medialive-2017-10-14/CorsCloudwatch_alarm_template_groupsIdentifier)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/medialive-2017-10-14/CorsCloudwatch_alarm_template_groupsIdentifier)

### UpdateCloudWatchAlarmTemplateGroup
<a name="UpdateCloudWatchAlarmTemplateGroup-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/medialive-2017-10-14/UpdateCloudWatchAlarmTemplateGroup)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/medialive-2017-10-14/UpdateCloudWatchAlarmTemplateGroup)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/medialive-2017-10-14/UpdateCloudWatchAlarmTemplateGroup)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/medialive-2017-10-14/UpdateCloudWatchAlarmTemplateGroup)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/medialive-2017-10-14/UpdateCloudWatchAlarmTemplateGroup)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/medialive-2017-10-14/UpdateCloudWatchAlarmTemplateGroup)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/medialive-2017-10-14/UpdateCloudWatchAlarmTemplateGroup)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/medialive-2017-10-14/UpdateCloudWatchAlarmTemplateGroup)
+ [AWS SDK for Python](/goto/boto3/medialive-2017-10-14/UpdateCloudWatchAlarmTemplateGroup)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/medialive-2017-10-14/UpdateCloudWatchAlarmTemplateGroup)
