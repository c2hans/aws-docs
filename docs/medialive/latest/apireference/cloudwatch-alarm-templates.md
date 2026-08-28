---
source_url: https://docs.aws.amazon.com/medialive/latest/apireference/cloudwatch-alarm-templates.html
---

# Workflow monitor: CloudWatch alarm templates
<a name="cloudwatch-alarm-templates"></a>

## URI
<a name="cloudwatch-alarm-templates-url"></a>

`/prod/cloudwatch-alarm-templates`

## HTTP methods
<a name="cloudwatch-alarm-templates-http-methods"></a>

### GET
<a name="cloudwatch-alarm-templatesget"></a>

**Operation ID:** `ListCloudWatchAlarmTemplates`

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| groupIdentifier | String | False |  |
| signalMapIdentifier | String | False |  |
| scope | String | False |  |
| nextToken | String | False |  |
| maxResults | String | False |  |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | ListCloudWatchAlarmTemplatesResponseContent | 200 response |
| 400 | BadRequestExceptionResponseContent | 400 response |
| 403 | ForbiddenExceptionResponseContent | 403 response |
| 404 | NotFoundExceptionResponseContent | 404 response |
| 429 | TooManyRequestsExceptionResponseContent | 429 response |
| 500 | InternalServerErrorExceptionResponseContent | 500 response |

### OPTIONS
<a name="cloudwatch-alarm-templatesoptions"></a>

**Operation ID:** `CorsCloudwatch_alarm_templates`

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | 200 response |

### POST
<a name="cloudwatch-alarm-templatespost"></a>

**Operation ID:** `CreateCloudWatchAlarmTemplate`

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 201 | CreateCloudWatchAlarmTemplateResponseContent | 201 response |
| 400 | BadRequestExceptionResponseContent | 400 response |
| 403 | ForbiddenExceptionResponseContent | 403 response |
| 404 | NotFoundExceptionResponseContent | 404 response |
| 409 | ConflictExceptionResponseContent | 409 response |
| 429 | TooManyRequestsExceptionResponseContent | 429 response |
| 500 | InternalServerErrorExceptionResponseContent | 500 response |

## Schemas
<a name="cloudwatch-alarm-templates-schemas"></a>

### Request bodies
<a name="cloudwatch-alarm-templates-request-examples"></a>

#### POST schema
<a name="cloudwatch-alarm-templates-request-body-post-example"></a>

```
{
  "comparisonOperator": enum,
  "datapointsToAlarm": number,
  "description": "string",
  "evaluationPeriods": number,
  "groupIdentifier": "string",
  "metricName": "string",
  "name": "string",
  "period": number,
  "standardDeviationThreshold": number,
  "statistic": enum,
  "targetResourceType": enum,
  "threshold": number,
  "treatMissingData": enum
}
```

### Response bodies
<a name="cloudwatch-alarm-templates-response-examples"></a>

#### ListCloudWatchAlarmTemplatesResponseContent schema
<a name="cloudwatch-alarm-templates-response-body-listcloudwatchalarmtemplatesresponsecontent-example"></a>

```
{
  "cloudWatchAlarmTemplates": [
    {
      "arn": "string",
      "comparisonOperator": enum,
      "createdAt": "string",
      "datapointsToAlarm": number,
      "description": "string",
      "evaluationPeriods": number,
      "groupId": "string",
      "id": "string",
      "metricName": "string",
      "modifiedAt": "string",
      "name": "string",
      "period": number,
      "standardDeviationThreshold": number,
      "statistic": enum,
      "targetResourceType": enum,
      "threshold": number,
      "treatMissingData": enum
    }
  ],
  "nextToken": "string"
}
```

#### CreateCloudWatchAlarmTemplateResponseContent schema
<a name="cloudwatch-alarm-templates-response-body-createcloudwatchalarmtemplateresponsecontent-example"></a>

```
{
  "arn": "string",
  "comparisonOperator": enum,
  "createdAt": "string",
  "datapointsToAlarm": number,
  "description": "string",
  "evaluationPeriods": number,
  "groupId": "string",
  "id": "string",
  "metricName": "string",
  "modifiedAt": "string",
  "name": "string",
  "period": number,
  "standardDeviationThreshold": number,
  "statistic": enum,
  "targetResourceType": enum,
  "threshold": number,
  "treatMissingData": enum
}
```

#### BadRequestExceptionResponseContent schema
<a name="cloudwatch-alarm-templates-response-body-badrequestexceptionresponsecontent-example"></a>

```
{
  "message": "string"
}
```

#### ForbiddenExceptionResponseContent schema
<a name="cloudwatch-alarm-templates-response-body-forbiddenexceptionresponsecontent-example"></a>

```
{
  "message": "string"
}
```

#### NotFoundExceptionResponseContent schema
<a name="cloudwatch-alarm-templates-response-body-notfoundexceptionresponsecontent-example"></a>

```
{
  "message": "string"
}
```

#### ConflictExceptionResponseContent schema
<a name="cloudwatch-alarm-templates-response-body-conflictexceptionresponsecontent-example"></a>

```
{
  "message": "string"
}
```

#### TooManyRequestsExceptionResponseContent schema
<a name="cloudwatch-alarm-templates-response-body-toomanyrequestsexceptionresponsecontent-example"></a>

```
{
  "message": "string"
}
```

#### InternalServerErrorExceptionResponseContent schema
<a name="cloudwatch-alarm-templates-response-body-internalservererrorexceptionresponsecontent-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="cloudwatch-alarm-templates-properties"></a>

### BadRequestExceptionResponseContent
<a name="cloudwatch-alarm-templates-model-badrequestexceptionresponsecontent"></a>

The input fails to satisfy the constraints specified by an Amazon Web Services service.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Exception error message. |

### CloudWatchAlarmTemplateComparisonOperator
<a name="cloudwatch-alarm-templates-model-cloudwatchalarmtemplatecomparisonoperator"></a>

The comparison operator used to compare the specified statistic and the threshold.
+ `GreaterThanOrEqualToThreshold`
+ `GreaterThanThreshold`
+ `LessThanThreshold`
+ `LessThanOrEqualToThreshold`
+ `LessThanLowerOrGreaterThanUpperThreshold`
+ `LessThanLowerThreshold`
+ `GreaterThanUpperThreshold`

### CloudWatchAlarmTemplateStatistic
<a name="cloudwatch-alarm-templates-model-cloudwatchalarmtemplatestatistic"></a>

The statistic to apply to the alarm's metric data.
+ `SampleCount`
+ `Average`
+ `Sum`
+ `Minimum`
+ `Maximum`

### CloudWatchAlarmTemplateSummary
<a name="cloudwatch-alarm-templates-model-cloudwatchalarmtemplatesummary"></a>

A summary of the alarm templates.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| arn | string<br />Pattern: `^arn:.+:medialive:.+:cloudwatch-alarm-template:.+$` | True | A cloudwatch alarm template's ARN (Amazon Resource Name) |
| comparisonOperator | [CloudWatchAlarmTemplateComparisonOperator](#cloudwatch-alarm-templates-model-cloudwatchalarmtemplatecomparisonoperator) | True | The comparison operator used to compare the specified statistic and the threshold. |
| createdAt | string<br />Format: date-time | True | The date and time of resource creation. |
| datapointsToAlarm | number<br />Minimum: 1 | False | The number of datapoints within the evaluation period that must be breaching to trigger the alarm. |
| description | string<br />MinLength: 0<br />MaxLength: 1024 | False | A resource's optional description. |
| evaluationPeriods | number<br />Minimum: 1 | True | The number of periods over which data is compared to the specified threshold. |
| groupId | string<br />Pattern: `^(aws-)?[0-9]{7}$`<br />MinLength: 7<br />MaxLength: 11 | True | A CloudWatch alarm template group's id. Amazon Web Services provided template groups have ids that start with <code>`aws-`</code> |
| id | string<br />Pattern: `^(aws-)?[0-9]{7}$`<br />MinLength: 7<br />MaxLength: 11 | True | A cloudwatch alarm template's id. Amazon Web Services provided templates have ids that start with <code>`aws-`</code>. |
| metricName | string<br />MaxLength: 64 | True | The name of the metric associated with the alarm. Must be compatible with targetResourceType. |
| modifiedAt | string<br />Format: date-time | False | The date and time of latest resource modification. |
| name | string<br />Pattern: `^[^\s]+$`<br />MinLength: 1<br />MaxLength: 255 | True | A resource's name. Names must be unique within the scope of a resource type in a specific region. |
| period | number<br />Minimum: 10<br />Maximum: 86400 | True | The period, in seconds, over which the specified statistic is applied. |
| standardDeviationThreshold | number<br />Minimum: 1 | False | The number of standard deviations by which the metric value can deviate from the expected value before the alarm is triggered. |
| statistic | [CloudWatchAlarmTemplateStatistic](#cloudwatch-alarm-templates-model-cloudwatchalarmtemplatestatistic) | True | The statistic to apply to the alarm's metric data. |
| targetResourceType | [CloudWatchAlarmTemplateTargetResourceType](#cloudwatch-alarm-templates-model-cloudwatchalarmtemplatetargetresourcetype) | True | The resource type this template should dynamically generate CloudWatch metric alarms for. |
| threshold | number<br />Format: double | False | The threshold value to compare with the specified statistic. |
| treatMissingData | [CloudWatchAlarmTemplateTreatMissingData](#cloudwatch-alarm-templates-model-cloudwatchalarmtemplatetreatmissingdata) | True | Specifies how missing data points are treated when evaluating the alarm's condition. |

### CloudWatchAlarmTemplateTargetResourceType
<a name="cloudwatch-alarm-templates-model-cloudwatchalarmtemplatetargetresourcetype"></a>

The resource type this template should dynamically generate cloudwatch metric alarms for.
+ `CLOUDFRONT_DISTRIBUTION`
+ `MEDIALIVE_MULTIPLEX`
+ `MEDIALIVE_CHANNEL`
+ `MEDIALIVE_INPUT_DEVICE`
+ `MEDIAPACKAGE_CHANNEL`
+ `MEDIAPACKAGE_ORIGIN_ENDPOINT`
+ `MEDIACONNECT_FLOW`
+ `S3_BUCKET`

### CloudWatchAlarmTemplateTreatMissingData
<a name="cloudwatch-alarm-templates-model-cloudwatchalarmtemplatetreatmissingdata"></a>

Specifies how missing data points are treated when evaluating the alarm's condition.
+ `notBreaching`
+ `breaching`
+ `ignore`
+ `missing`

### ConflictExceptionResponseContent
<a name="cloudwatch-alarm-templates-model-conflictexceptionresponsecontent"></a>

Updating or deleting a resource can cause an inconsistent state.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Exception error message. |

### CreateCloudWatchAlarmTemplateRequestContent
<a name="cloudwatch-alarm-templates-model-createcloudwatchalarmtemplaterequestcontent"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| comparisonOperator | [CloudWatchAlarmTemplateComparisonOperator](#cloudwatch-alarm-templates-model-cloudwatchalarmtemplatecomparisonoperator) | True | The comparison operator used to compare the specified statistic and the threshold. |
| datapointsToAlarm | number<br />Minimum: 1 | False | The number of datapoints within the evaluation period that must be breaching to trigger the alarm. |
| description | string<br />MinLength: 0<br />MaxLength: 1024 | False | A resource's optional description. |
| evaluationPeriods | number<br />Minimum: 1 | True | The number of periods over which data is compared to the specified threshold. |
| groupIdentifier | string<br />Pattern: `^[^\s]+$` | True | A cloudwatch alarm template group's identifier. Can be either be its id or current name. |
| metricName | string<br />MaxLength: 64 | True | The name of the metric associated with the alarm. Must be compatible with targetResourceType. |
| name | string<br />Pattern: `^[^\s]+$`<br />MinLength: 1<br />MaxLength: 255 | True | A resource's name. Names must be unique within the scope of a resource type in a specific region. |
| period | number<br />Minimum: 10<br />Maximum: 86400 | True | The period, in seconds, over which the specified statistic is applied. |
| standardDeviationThreshold | number<br />Minimum: 1 | False | The number of standard deviations by which the metric value can deviate from the expected value before the alarm is triggered. |
| statistic | [CloudWatchAlarmTemplateStatistic](#cloudwatch-alarm-templates-model-cloudwatchalarmtemplatestatistic) | True | The statistic to apply to the alarm's metric data. |
| targetResourceType | [CloudWatchAlarmTemplateTargetResourceType](#cloudwatch-alarm-templates-model-cloudwatchalarmtemplatetargetresourcetype) | True | The resource type this template should dynamically generate CloudWatch metric alarms for. |
| threshold | number<br />Format: double | False | The threshold value to compare with the specified statistic. |
| treatMissingData | [CloudWatchAlarmTemplateTreatMissingData](#cloudwatch-alarm-templates-model-cloudwatchalarmtemplatetreatmissingdata) | True | Specifies how missing data points are treated when evaluating the alarm's condition. |

### CreateCloudWatchAlarmTemplateResponseContent
<a name="cloudwatch-alarm-templates-model-createcloudwatchalarmtemplateresponsecontent"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| arn | string<br />Pattern: `^arn:.+:medialive:.+:cloudwatch-alarm-template:.+$` | True | A cloudwatch alarm template's ARN (Amazon Resource Name) |
| comparisonOperator | [CloudWatchAlarmTemplateComparisonOperator](#cloudwatch-alarm-templates-model-cloudwatchalarmtemplatecomparisonoperator) | True | The comparison operator used to compare the specified statistic and the threshold. |
| createdAt | string<br />Format: date-time | True | The date and time of resource creation. |
| datapointsToAlarm | number<br />Minimum: 1 | False | The number of datapoints within the evaluation period that must be breaching to trigger the alarm. |
| description | string<br />MinLength: 0<br />MaxLength: 1024 | False | A resource's optional description. |
| evaluationPeriods | number<br />Minimum: 1 | True | The number of periods over which data is compared to the specified threshold. |
| groupId | string<br />Pattern: `^(aws-)?[0-9]{7}$`<br />MinLength: 7<br />MaxLength: 11 | True | A CloudWatch alarm template group's id. Amazon Web Services provided template groups have ids that start with <code>`aws-`</code> |
| id | string<br />Pattern: `^(aws-)?[0-9]{7}$`<br />MinLength: 7<br />MaxLength: 11 | True | A cloudwatch alarm template's id. Amazon Web Services provided templates have ids that start with <code>`aws-`</code>. |
| metricName | string<br />MaxLength: 64 | True | The name of the metric associated with the alarm. Must be compatible with targetResourceType. |
| modifiedAt | string<br />Format: date-time | False | The date and time of latest resource modification. |
| name | string<br />Pattern: `^[^\s]+$`<br />MinLength: 1<br />MaxLength: 255 | True | A resource's name. Names must be unique within the scope of a resource type in a specific region. |
| period | number<br />Minimum: 10<br />Maximum: 86400 | True | The period, in seconds, over which the specified statistic is applied. |
| standardDeviationThreshold | number<br />Minimum: 1 | False | The number of standard deviations by which the metric value can deviate from the expected value before the alarm is triggered. |
| statistic | [CloudWatchAlarmTemplateStatistic](#cloudwatch-alarm-templates-model-cloudwatchalarmtemplatestatistic) | True | The statistic to apply to the alarm's metric data. |
| targetResourceType | [CloudWatchAlarmTemplateTargetResourceType](#cloudwatch-alarm-templates-model-cloudwatchalarmtemplatetargetresourcetype) | True | The resource type this template should dynamically generate CloudWatch metric alarms for. |
| threshold | number<br />Format: double | False | The threshold value to compare with the specified statistic. |
| treatMissingData | [CloudWatchAlarmTemplateTreatMissingData](#cloudwatch-alarm-templates-model-cloudwatchalarmtemplatetreatmissingdata) | True | Specifies how missing data points are treated when evaluating the alarm's condition. |

### ForbiddenExceptionResponseContent
<a name="cloudwatch-alarm-templates-model-forbiddenexceptionresponsecontent"></a>

User does not have sufficient access to perform this action.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Exception error message. |

### InternalServerErrorExceptionResponseContent
<a name="cloudwatch-alarm-templates-model-internalservererrorexceptionresponsecontent"></a>

Unexpected error during processing of request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Exception error message. |

### ListCloudWatchAlarmTemplatesResponseContent
<a name="cloudwatch-alarm-templates-model-listcloudwatchalarmtemplatesresponsecontent"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| cloudWatchAlarmTemplates | Array of type [CloudWatchAlarmTemplateSummary](#cloudwatch-alarm-templates-model-cloudwatchalarmtemplatesummary) | True | A summary of the alarm templates. |
| nextToken | string<br />MinLength: 1<br />MaxLength: 2048 | False | A token used to retrieve the next set of results in paginated list responses. |

### NotFoundExceptionResponseContent
<a name="cloudwatch-alarm-templates-model-notfoundexceptionresponsecontent"></a>

Request references a resource which does not exist.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Exception error message. |

### TooManyRequestsExceptionResponseContent
<a name="cloudwatch-alarm-templates-model-toomanyrequestsexceptionresponsecontent"></a>

Request was denied due to request throttling.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Exception error message. |

## See also
<a name="cloudwatch-alarm-templates-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### ListCloudWatchAlarmTemplates
<a name="ListCloudWatchAlarmTemplates-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/medialive-2017-10-14/ListCloudWatchAlarmTemplates)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/medialive-2017-10-14/ListCloudWatchAlarmTemplates)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/medialive-2017-10-14/ListCloudWatchAlarmTemplates)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/medialive-2017-10-14/ListCloudWatchAlarmTemplates)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/medialive-2017-10-14/ListCloudWatchAlarmTemplates)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/medialive-2017-10-14/ListCloudWatchAlarmTemplates)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/medialive-2017-10-14/ListCloudWatchAlarmTemplates)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/medialive-2017-10-14/ListCloudWatchAlarmTemplates)
+ [AWS SDK for Python](/goto/boto3/medialive-2017-10-14/ListCloudWatchAlarmTemplates)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/medialive-2017-10-14/ListCloudWatchAlarmTemplates)

### CorsCloudwatch\_alarm\_templates
<a name="CorsCloudwatch_alarm_templates-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/medialive-2017-10-14/CorsCloudwatch_alarm_templates)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/medialive-2017-10-14/CorsCloudwatch_alarm_templates)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/medialive-2017-10-14/CorsCloudwatch_alarm_templates)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/medialive-2017-10-14/CorsCloudwatch_alarm_templates)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/medialive-2017-10-14/CorsCloudwatch_alarm_templates)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/medialive-2017-10-14/CorsCloudwatch_alarm_templates)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/medialive-2017-10-14/CorsCloudwatch_alarm_templates)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/medialive-2017-10-14/CorsCloudwatch_alarm_templates)
+ [AWS SDK for Python](/goto/boto3/medialive-2017-10-14/CorsCloudwatch_alarm_templates)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/medialive-2017-10-14/CorsCloudwatch_alarm_templates)

### CreateCloudWatchAlarmTemplate
<a name="CreateCloudWatchAlarmTemplate-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/medialive-2017-10-14/CreateCloudWatchAlarmTemplate)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/medialive-2017-10-14/CreateCloudWatchAlarmTemplate)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/medialive-2017-10-14/CreateCloudWatchAlarmTemplate)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/medialive-2017-10-14/CreateCloudWatchAlarmTemplate)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/medialive-2017-10-14/CreateCloudWatchAlarmTemplate)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/medialive-2017-10-14/CreateCloudWatchAlarmTemplate)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/medialive-2017-10-14/CreateCloudWatchAlarmTemplate)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/medialive-2017-10-14/CreateCloudWatchAlarmTemplate)
+ [AWS SDK for Python](/goto/boto3/medialive-2017-10-14/CreateCloudWatchAlarmTemplate)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/medialive-2017-10-14/CreateCloudWatchAlarmTemplate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
