---
source_url: https://docs.aws.amazon.com/medialive/latest/apireference/signal-maps.html
---

# Workflow monitor: Signal maps
<a name="signal-maps"></a>

## URI
<a name="signal-maps-url"></a>

`/prod/signal-maps`

## HTTP methods
<a name="signal-maps-http-methods"></a>

### GET
<a name="signal-mapsget"></a>

**Operation ID:** `ListSignalMaps`

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| eventBridgeRuleTemplateGroupIdentifier | String | False |  |
| nextToken | String | False |  |
| cloudWatchAlarmTemplateGroupIdentifier | String | False |  |
| maxResults | String | False |  |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | ListSignalMapsResponseContent | 200 response |
| 400 | BadRequestExceptionResponseContent | 400 response |
| 403 | ForbiddenExceptionResponseContent | 403 response |
| 404 | NotFoundExceptionResponseContent | 404 response |
| 429 | TooManyRequestsExceptionResponseContent | 429 response |
| 500 | InternalServerErrorExceptionResponseContent | 500 response |

### OPTIONS
<a name="signal-mapsoptions"></a>

**Operation ID:** `CorsSignal_maps`

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | 200 response |

### POST
<a name="signal-mapspost"></a>

**Operation ID:** `CreateSignalMap`

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 201 | CreateSignalMapResponseContent | 201 response |
| 400 | BadRequestExceptionResponseContent | 400 response |
| 403 | ForbiddenExceptionResponseContent | 403 response |
| 404 | NotFoundExceptionResponseContent | 404 response |
| 409 | ConflictExceptionResponseContent | 409 response |
| 429 | TooManyRequestsExceptionResponseContent | 429 response |
| 500 | InternalServerErrorExceptionResponseContent | 500 response |

## Schemas
<a name="signal-maps-schemas"></a>

### Request bodies
<a name="signal-maps-request-examples"></a>

#### POST schema
<a name="signal-maps-request-body-post-example"></a>

```
{
  "cloudWatchAlarmTemplateGroupIdentifiers": [
    "string"
  ],
  "description": "string",
  "discoveryEntryPointArn": "string",
  "eventBridgeRuleTemplateGroupIdentifiers": [
    "string"
  ],
  "name": "string"
}
```

### Response bodies
<a name="signal-maps-response-examples"></a>

#### ListSignalMapsResponseContent schema
<a name="signal-maps-response-body-listsignalmapsresponsecontent-example"></a>

```
{
  "nextToken": "string",
  "signalMaps": [
    {
      "arn": "string",
      "createdAt": "string",
      "description": "string",
      "id": "string",
      "modifiedAt": "string",
      "monitorDeploymentStatus": enum,
      "name": "string",
      "status": enum
    }
  ]
}
```

#### CreateSignalMapResponseContent schema
<a name="signal-maps-response-body-createsignalmapresponsecontent-example"></a>

```
{
  "arn": "string",
  "cloudWatchAlarmTemplateGroupIds": [
    "string"
  ],
  "createdAt": "string",
  "description": "string",
  "discoveryEntryPointArn": "string",
  "errorMessage": "string",
  "eventBridgeRuleTemplateGroupIds": [
    "string"
  ],
  "failedMediaResourceMap": {
  },
  "id": "string",
  "lastDiscoveredAt": "string",
  "lastSuccessfulMonitorDeployment": {
    "detailsUri": "string",
    "status": enum
  },
  "mediaResourceMap": {
  },
  "modifiedAt": "string",
  "monitorChangesPendingDeployment": boolean,
  "monitorDeployment": {
    "detailsUri": "string",
    "errorMessage": "string",
    "status": enum
  },
  "name": "string",
  "status": enum
}
```

#### BadRequestExceptionResponseContent schema
<a name="signal-maps-response-body-badrequestexceptionresponsecontent-example"></a>

```
{
  "message": "string"
}
```

#### ForbiddenExceptionResponseContent schema
<a name="signal-maps-response-body-forbiddenexceptionresponsecontent-example"></a>

```
{
  "message": "string"
}
```

#### NotFoundExceptionResponseContent schema
<a name="signal-maps-response-body-notfoundexceptionresponsecontent-example"></a>

```
{
  "message": "string"
}
```

#### ConflictExceptionResponseContent schema
<a name="signal-maps-response-body-conflictexceptionresponsecontent-example"></a>

```
{
  "message": "string"
}
```

#### TooManyRequestsExceptionResponseContent schema
<a name="signal-maps-response-body-toomanyrequestsexceptionresponsecontent-example"></a>

```
{
  "message": "string"
}
```

#### InternalServerErrorExceptionResponseContent schema
<a name="signal-maps-response-body-internalservererrorexceptionresponsecontent-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="signal-maps-properties"></a>

### BadRequestExceptionResponseContent
<a name="signal-maps-model-badrequestexceptionresponsecontent"></a>

The input fails to satisfy the constraints specified by an Amazon Web Services service.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Exception error message. |

### ConflictExceptionResponseContent
<a name="signal-maps-model-conflictexceptionresponsecontent"></a>

Updating or deleting a resource can cause an inconsistent state.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Exception error message. |

### CreateSignalMapRequestContent
<a name="signal-maps-model-createsignalmaprequestcontent"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| cloudWatchAlarmTemplateGroupIdentifiers | Array of type string<br />Pattern: `^[^\s]+$` | False | A cloudwatch alarm template group's identifier. Can be either be its id or current name. |
| description | string<br />MinLength: 0<br />MaxLength: 1024 | False | A resource's optional description. |
| discoveryEntryPointArn | string<br />MinLength: 1<br />MaxLength: 2048 | True | A top-level supported Amazon Web Services resource ARN to discover a signal map from. |
| eventBridgeRuleTemplateGroupIdentifiers | Array of type string<br />Pattern: `^[^\s]+$` | False | An eventbridge rule template group's identifier. Can be either be its id or current name. |
| name | string<br />Pattern: `^[^\s]+$`<br />MinLength: 1<br />MaxLength: 255 | True | A resource's name. Names must be unique within the scope of a resource type in a specific region. |

### CreateSignalMapResponseContent
<a name="signal-maps-model-createsignalmapresponsecontent"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| arn | string<br />Pattern: `^arn:.+:medialive:.+:signal-map:.+$` | True | A signal map's ARN (Amazon Resource Name) |
| cloudWatchAlarmTemplateGroupIds | Array of type string<br />Pattern: `^(aws-)?[0-9]{7}$`<br />MinLength: 7<br />MaxLength: 11 | False | An alarm template group's id. |
| createdAt | string<br />Format: date-time | True | The date and time of resource creation. |
| description | string<br />MinLength: 0<br />MaxLength: 1024 | False | A resource's optional description. |
| discoveryEntryPointArn | string<br />MinLength: 1<br />MaxLength: 2048 | True | A top-level supported Amazon Web Services resource ARN to discover a signal map from. |
| errorMessage | string<br />MinLength: 1<br />MaxLength: 2048 | False | Error message associated with a failed creation or failed update attempt of a signal map. |
| eventBridgeRuleTemplateGroupIds | Array of type string<br />Pattern: `^(aws-)?[0-9]{7}$`<br />MinLength: 7<br />MaxLength: 11 | False | An eventbridge rule template group's id. Amazon Web Services provided template groups have ids that start with `aws-`. |
| failedMediaResourceMap | [FailedMediaResourceMap](#signal-maps-model-failedmediaresourcemap) | False | A map representing an incomplete Amazon Web Services media workflow as a graph. |
| id | string<br />Pattern: `^(aws-)?[0-9]{7}$`<br />MinLength: 7<br />MaxLength: 11 | True | A signal map's id. |
| lastDiscoveredAt | string<br />Format: date-time | False | The date and time of latest discovery. |
| lastSuccessfulMonitorDeployment | [SuccessfulMonitorDeployment](#signal-maps-model-successfulmonitordeployment) | False | The date and time of latest successful deployment. |
| mediaResourceMap | [MediaResourceMap](#signal-maps-model-mediaresourcemap) | False | A map representing an Amazon Web Services media workflow as a graph. |
| modifiedAt | string<br />Format: date-time | False | The date and time of latest resource modification. |
| monitorChangesPendingDeployment | boolean | True | If true, there are pending monitor changes for this signal map that can be deployed. |
| monitorDeployment | [MonitorDeployment](#signal-maps-model-monitordeployment) | False | Represents the latest monitor deployment of a signal map. |
| name | string<br />Pattern: `^[^\s]+$`<br />MinLength: 1<br />MaxLength: 255 | True | A resource's name. Names must be unique within the scope of a resource type in a specific region. |
| status | [SignalMapStatus](#signal-maps-model-signalmapstatus) | True | A signal map's current status, which is dependent on its lifecycle actions or associated jobs. |

### FailedMediaResourceMap
<a name="signal-maps-model-failedmediaresourcemap"></a>

A map representing an incomplete Amazon Web Services media workflow as a graph.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| `*` | object | False |  |

### ForbiddenExceptionResponseContent
<a name="signal-maps-model-forbiddenexceptionresponsecontent"></a>

User does not have sufficient access to perform this action.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Exception error message. |

### InternalServerErrorExceptionResponseContent
<a name="signal-maps-model-internalservererrorexceptionresponsecontent"></a>

Unexpected error during processing of request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Exception error message. |

### ListSignalMapsResponseContent
<a name="signal-maps-model-listsignalmapsresponsecontent"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| nextToken | string<br />MinLength: 1<br />MaxLength: 2048 | False | A token used to retrieve the next set of results in paginated list responses. |
| signalMaps | Array of type [SignalMapSummary](#signal-maps-model-signalmapsummary) | True | Details of the signal map |

### MediaResource
<a name="signal-maps-model-mediaresource"></a>

An Amazon Web Services resource used in media workflows.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| destinations | Array of type [MediaResourceNeighbor](#signal-maps-model-mediaresourceneighbor) | False | A direct destination neighbor to an Amazon Web Services media resource. |
| name | string<br />MinLength: 1<br />MaxLength: 256 | False | The logical name of an Amazon Web Services media resource. |
| sources | Array of type [MediaResourceNeighbor](#signal-maps-model-mediaresourceneighbor) | False | A direct source neighbor to an Amazon Web Services media resource. |

### MediaResourceMap
<a name="signal-maps-model-mediaresourcemap"></a>

A map representing an Amazon Web Services media workflow as a graph.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| `*` | object | False |  |

### MediaResourceNeighbor
<a name="signal-maps-model-mediaresourceneighbor"></a>

A direct source or destination neighbor to an Amazon Web Services media resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| arn | string<br />Pattern: `^arn.+$`<br />MinLength: 1<br />MaxLength: 2048 | True | The ARN of a resource used in Amazon Web Services media workflows. |
| name | string<br />MinLength: 1<br />MaxLength: 256 | False | The logical name of an Amazon Web Services media resource. |

### MonitorDeployment
<a name="signal-maps-model-monitordeployment"></a>

Represents the latest monitor deployment of a signal map.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| detailsUri | string<br />MinLength: 1<br />MaxLength: 2048 | False | URI associated with a signal map's monitor deployment. |
| errorMessage | string<br />MinLength: 1<br />MaxLength: 2048 | False | Error message associated with a failed monitor deployment of a signal map. |
| status | [SignalMapMonitorDeploymentStatus](#signal-maps-model-signalmapmonitordeploymentstatus) | True | The signal map monitor deployment status. |

### NotFoundExceptionResponseContent
<a name="signal-maps-model-notfoundexceptionresponsecontent"></a>

Request references a resource which does not exist.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Exception error message. |

### SignalMapMonitorDeploymentStatus
<a name="signal-maps-model-signalmapmonitordeploymentstatus"></a>

A signal map's monitor deployment status.
+ `NOT_DEPLOYED`
+ `DRY_RUN_DEPLOYMENT_COMPLETE`
+ `DRY_RUN_DEPLOYMENT_FAILED`
+ `DRY_RUN_DEPLOYMENT_IN_PROGRESS`
+ `DEPLOYMENT_COMPLETE`
+ `DEPLOYMENT_FAILED`
+ `DEPLOYMENT_IN_PROGRESS`
+ `DELETE_COMPLETE`
+ `DELETE_FAILED`
+ `DELETE_IN_PROGRESS`

### SignalMapStatus
<a name="signal-maps-model-signalmapstatus"></a>

A signal map's current status which is dependent on its lifecycle actions or associated jobs.
+ `CREATE_IN_PROGRESS`
+ `CREATE_COMPLETE`
+ `CREATE_FAILED`
+ `UPDATE_IN_PROGRESS`
+ `UPDATE_COMPLETE`
+ `UPDATE_REVERTED`
+ `UPDATE_FAILED`
+ `READY`
+ `NOT_READY`

### SignalMapSummary
<a name="signal-maps-model-signalmapsummary"></a>

Details of the signal map

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| arn | string<br />Pattern: `^arn:.+:medialive:.+:signal-map:.+$` | True | A signal map's ARN (Amazon Resource Name) |
| createdAt | string<br />Format: date-time | True | The date and time of resource creation. |
| description | string<br />MinLength: 0<br />MaxLength: 1024 | False | A resource's optional description. |
| id | string<br />Pattern: `^(aws-)?[0-9]{7}$`<br />MinLength: 7<br />MaxLength: 11 | True | A signal map's id. |
| modifiedAt | string<br />Format: date-time | False | The date and time of latest resource modification. |
| monitorDeploymentStatus | [SignalMapMonitorDeploymentStatus](#signal-maps-model-signalmapmonitordeploymentstatus) | True | A signal map's monitor deployment status. |
| name | string<br />Pattern: `^[^\s]+$`<br />MinLength: 1<br />MaxLength: 255 | True | A resource's name. Names must be unique within the scope of a resource type in a specific region. |
| status | [SignalMapStatus](#signal-maps-model-signalmapstatus) | True | A signal map's current status, which is dependent on its lifecycle actions or associated jobs. |

### SuccessfulMonitorDeployment
<a name="signal-maps-model-successfulmonitordeployment"></a>

Represents the latest successful monitor deployment of a signal map.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| detailsUri | string<br />MinLength: 1<br />MaxLength: 2048 | True | URI associated with a signal map's monitor deployment. |
| status | [SignalMapMonitorDeploymentStatus](#signal-maps-model-signalmapmonitordeploymentstatus) | True | A signal map's monitor deployment status. |

### TooManyRequestsExceptionResponseContent
<a name="signal-maps-model-toomanyrequestsexceptionresponsecontent"></a>

Request was denied due to request throttling.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Exception error message. |

## See also
<a name="signal-maps-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### ListSignalMaps
<a name="ListSignalMaps-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/medialive-2017-10-14/ListSignalMaps)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/medialive-2017-10-14/ListSignalMaps)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/medialive-2017-10-14/ListSignalMaps)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/medialive-2017-10-14/ListSignalMaps)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/medialive-2017-10-14/ListSignalMaps)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/medialive-2017-10-14/ListSignalMaps)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/medialive-2017-10-14/ListSignalMaps)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/medialive-2017-10-14/ListSignalMaps)
+ [AWS SDK for Python](/goto/boto3/medialive-2017-10-14/ListSignalMaps)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/medialive-2017-10-14/ListSignalMaps)

### CorsSignal\_maps
<a name="CorsSignal_maps-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/medialive-2017-10-14/CorsSignal_maps)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/medialive-2017-10-14/CorsSignal_maps)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/medialive-2017-10-14/CorsSignal_maps)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/medialive-2017-10-14/CorsSignal_maps)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/medialive-2017-10-14/CorsSignal_maps)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/medialive-2017-10-14/CorsSignal_maps)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/medialive-2017-10-14/CorsSignal_maps)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/medialive-2017-10-14/CorsSignal_maps)
+ [AWS SDK for Python](/goto/boto3/medialive-2017-10-14/CorsSignal_maps)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/medialive-2017-10-14/CorsSignal_maps)

### CreateSignalMap
<a name="CreateSignalMap-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/medialive-2017-10-14/CreateSignalMap)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/medialive-2017-10-14/CreateSignalMap)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/medialive-2017-10-14/CreateSignalMap)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/medialive-2017-10-14/CreateSignalMap)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/medialive-2017-10-14/CreateSignalMap)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/medialive-2017-10-14/CreateSignalMap)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/medialive-2017-10-14/CreateSignalMap)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/medialive-2017-10-14/CreateSignalMap)
+ [AWS SDK for Python](/goto/boto3/medialive-2017-10-14/CreateSignalMap)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/medialive-2017-10-14/CreateSignalMap)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
