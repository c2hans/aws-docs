---
source_url: https://docs.aws.amazon.com/medialive/latest/apireference/signal-maps-identifier-monitor-deployment.html
---

# Workflow monitor: Signal map monitor deployment
<a name="signal-maps-identifier-monitor-deployment"></a>

## URI
<a name="signal-maps-identifier-monitor-deployment-url"></a>

`/prod/signal-maps/{{identifier}}/monitor-deployment`

## HTTP methods
<a name="signal-maps-identifier-monitor-deployment-http-methods"></a>

### DELETE
<a name="signal-maps-identifier-monitor-deploymentdelete"></a>

**Operation ID:** `StartDeleteMonitorDeployment`

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{identifier}} | String | True |  |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 202 | StartDeleteMonitorDeploymentResponseContent | 202 response |
| 400 | BadRequestExceptionResponseContent | 400 response |
| 403 | ForbiddenExceptionResponseContent | 403 response |
| 404 | NotFoundExceptionResponseContent | 404 response |
| 409 | ConflictExceptionResponseContent | 409 response |
| 429 | TooManyRequestsExceptionResponseContent | 429 response |
| 500 | InternalServerErrorExceptionResponseContent | 500 response |

### OPTIONS
<a name="signal-maps-identifier-monitor-deploymentoptions"></a>

**Operation ID:** `CorsSignal_mapsIdentifierMonitor_deployment`

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{identifier}} | String | True |  |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | 200 response |

### POST
<a name="signal-maps-identifier-monitor-deploymentpost"></a>

**Operation ID:** `StartMonitorDeployment`

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{identifier}} | String | True |  |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 202 | StartMonitorDeploymentResponseContent | 202 response |
| 400 | BadRequestExceptionResponseContent | 400 response |
| 403 | ForbiddenExceptionResponseContent | 403 response |
| 404 | NotFoundExceptionResponseContent | 404 response |
| 409 | ConflictExceptionResponseContent | 409 response |
| 429 | TooManyRequestsExceptionResponseContent | 429 response |
| 500 | InternalServerErrorExceptionResponseContent | 500 response |

## Schemas
<a name="signal-maps-identifier-monitor-deployment-schemas"></a>

### Request bodies
<a name="signal-maps-identifier-monitor-deployment-request-examples"></a>

#### POST schema
<a name="signal-maps-identifier-monitor-deployment-request-body-post-example"></a>

```
{
  "dryRun": boolean
}
```

### Response bodies
<a name="signal-maps-identifier-monitor-deployment-response-examples"></a>

#### StartDeleteMonitorDeploymentResponseContent schema
<a name="signal-maps-identifier-monitor-deployment-response-body-startdeletemonitordeploymentresponsecontent-example"></a>

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

#### StartMonitorDeploymentResponseContent schema
<a name="signal-maps-identifier-monitor-deployment-response-body-startmonitordeploymentresponsecontent-example"></a>

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
<a name="signal-maps-identifier-monitor-deployment-response-body-badrequestexceptionresponsecontent-example"></a>

```
{
  "message": "string"
}
```

#### ForbiddenExceptionResponseContent schema
<a name="signal-maps-identifier-monitor-deployment-response-body-forbiddenexceptionresponsecontent-example"></a>

```
{
  "message": "string"
}
```

#### NotFoundExceptionResponseContent schema
<a name="signal-maps-identifier-monitor-deployment-response-body-notfoundexceptionresponsecontent-example"></a>

```
{
  "message": "string"
}
```

#### ConflictExceptionResponseContent schema
<a name="signal-maps-identifier-monitor-deployment-response-body-conflictexceptionresponsecontent-example"></a>

```
{
  "message": "string"
}
```

#### TooManyRequestsExceptionResponseContent schema
<a name="signal-maps-identifier-monitor-deployment-response-body-toomanyrequestsexceptionresponsecontent-example"></a>

```
{
  "message": "string"
}
```

#### InternalServerErrorExceptionResponseContent schema
<a name="signal-maps-identifier-monitor-deployment-response-body-internalservererrorexceptionresponsecontent-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="signal-maps-identifier-monitor-deployment-properties"></a>

### BadRequestExceptionResponseContent
<a name="signal-maps-identifier-monitor-deployment-model-badrequestexceptionresponsecontent"></a>

The input fails to satisfy the constraints specified by an Amazon Web Services service.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Exception error message. |

### ConflictExceptionResponseContent
<a name="signal-maps-identifier-monitor-deployment-model-conflictexceptionresponsecontent"></a>

Updating or deleting a resource can cause an inconsistent state.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Exception error message. |

### FailedMediaResourceMap
<a name="signal-maps-identifier-monitor-deployment-model-failedmediaresourcemap"></a>

A map representing an incomplete Amazon Web Services media workflow as a graph.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| `*` | object | False |  |

### ForbiddenExceptionResponseContent
<a name="signal-maps-identifier-monitor-deployment-model-forbiddenexceptionresponsecontent"></a>

User does not have sufficient access to perform this action.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Exception error message. |

### InternalServerErrorExceptionResponseContent
<a name="signal-maps-identifier-monitor-deployment-model-internalservererrorexceptionresponsecontent"></a>

Unexpected error during processing of request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Exception error message. |

### MediaResource
<a name="signal-maps-identifier-monitor-deployment-model-mediaresource"></a>

An Amazon Web Services resource used in media workflows.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| destinations | Array of type [MediaResourceNeighbor](#signal-maps-identifier-monitor-deployment-model-mediaresourceneighbor) | False | A direct destination neighbor to an Amazon Web Services media resource. |
| name | string<br />MinLength: 1<br />MaxLength: 256 | False | The logical name of an Amazon Web Services media resource. |
| sources | Array of type [MediaResourceNeighbor](#signal-maps-identifier-monitor-deployment-model-mediaresourceneighbor) | False | A direct source neighbor to an Amazon Web Services media resource. |

### MediaResourceMap
<a name="signal-maps-identifier-monitor-deployment-model-mediaresourcemap"></a>

A map representing an Amazon Web Services media workflow as a graph.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| `*` | object | False |  |

### MediaResourceNeighbor
<a name="signal-maps-identifier-monitor-deployment-model-mediaresourceneighbor"></a>

A direct source or destination neighbor to an Amazon Web Services media resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| arn | string<br />Pattern: `^arn.+$`<br />MinLength: 1<br />MaxLength: 2048 | True | The ARN of a resource used in Amazon Web Services media workflows. |
| name | string<br />MinLength: 1<br />MaxLength: 256 | False | The logical name of an Amazon Web Services media resource. |

### MonitorDeployment
<a name="signal-maps-identifier-monitor-deployment-model-monitordeployment"></a>

Represents the latest monitor deployment of a signal map.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| detailsUri | string<br />MinLength: 1<br />MaxLength: 2048 | False | URI associated with a signal map's monitor deployment. |
| errorMessage | string<br />MinLength: 1<br />MaxLength: 2048 | False | Error message associated with a failed monitor deployment of a signal map. |
| status | [SignalMapMonitorDeploymentStatus](#signal-maps-identifier-monitor-deployment-model-signalmapmonitordeploymentstatus) | True | The signal map monitor deployment status. |

### NotFoundExceptionResponseContent
<a name="signal-maps-identifier-monitor-deployment-model-notfoundexceptionresponsecontent"></a>

Request references a resource which does not exist.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Exception error message. |

### SignalMapMonitorDeploymentStatus
<a name="signal-maps-identifier-monitor-deployment-model-signalmapmonitordeploymentstatus"></a>

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
<a name="signal-maps-identifier-monitor-deployment-model-signalmapstatus"></a>

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

### StartDeleteMonitorDeploymentResponseContent
<a name="signal-maps-identifier-monitor-deployment-model-startdeletemonitordeploymentresponsecontent"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| arn | string<br />Pattern: `^arn:.+:medialive:.+:signal-map:.+$` | True | A signal map's ARN (Amazon Resource Name) |
| cloudWatchAlarmTemplateGroupIds | Array of type string<br />Pattern: `^(aws-)?[0-9]{7}$`<br />MinLength: 7<br />MaxLength: 11 | False | An alarm template group's id. |
| createdAt | string<br />Format: date-time | True | The date and time of resource creation. |
| description | string<br />MinLength: 0<br />MaxLength: 1024 | False | A resource's optional description. |
| discoveryEntryPointArn | string<br />MinLength: 1<br />MaxLength: 2048 | True | A top-level supported Amazon Web Services resource ARN to discover a signal map from. |
| errorMessage | string<br />MinLength: 1<br />MaxLength: 2048 | False | Error message associated with a failed creation or failed update attempt of a signal map. |
| eventBridgeRuleTemplateGroupIds | Array of type string<br />Pattern: `^(aws-)?[0-9]{7}$`<br />MinLength: 7<br />MaxLength: 11 | False | An eventbridge rule template group's id. |
| failedMediaResourceMap | [FailedMediaResourceMap](#signal-maps-identifier-monitor-deployment-model-failedmediaresourcemap) | False | A map representing an incomplete Amazon Web Services media workflow as a graph. |
| id | string<br />Pattern: `^(aws-)?[0-9]{7}$`<br />MinLength: 7<br />MaxLength: 11 | True | A signal map's id. |
| lastDiscoveredAt | string<br />Format: date-time | False | The date and time of latest discovery. |
| lastSuccessfulMonitorDeployment | [SuccessfulMonitorDeployment](#signal-maps-identifier-monitor-deployment-model-successfulmonitordeployment) | False | The date and time of latest successful deployment. |
| mediaResourceMap | [MediaResourceMap](#signal-maps-identifier-monitor-deployment-model-mediaresourcemap) | False | A map representing an Amazon Web Services media workflow as a graph. |
| modifiedAt | string<br />Format: date-time | False | The date and time of latest resource modification. |
| monitorChangesPendingDeployment | boolean | True | If true, there are pending monitor changes for this signal map that can be deployed. |
| monitorDeployment | [MonitorDeployment](#signal-maps-identifier-monitor-deployment-model-monitordeployment) | False | Represents the latest monitor deployment of a signal map. |
| name | string<br />Pattern: `^[^\s]+$`<br />MinLength: 1<br />MaxLength: 255 | True | A resource's name. Names must be unique within the scope of a resource type in a specific region. |
| status | [SignalMapStatus](#signal-maps-identifier-monitor-deployment-model-signalmapstatus) | True | A signal map's current status, which is dependent on its lifecycle actions or associated jobs. |

### StartMonitorDeploymentRequestContent
<a name="signal-maps-identifier-monitor-deployment-model-startmonitordeploymentrequestcontent"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| dryRun | boolean | False |  |

### StartMonitorDeploymentResponseContent
<a name="signal-maps-identifier-monitor-deployment-model-startmonitordeploymentresponsecontent"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| arn | string<br />Pattern: `^arn:.+:medialive:.+:signal-map:.+$` | True | A signal map's ARN (Amazon Resource Name) |
| cloudWatchAlarmTemplateGroupIds | Array of type string<br />Pattern: `^(aws-)?[0-9]{7}$`<br />MinLength: 7<br />MaxLength: 11 | False | An alarm template group's id. |
| createdAt | string<br />Format: date-time | True | The date and time of resource creation. |
| description | string<br />MinLength: 0<br />MaxLength: 1024 | False | A resource's optional description. |
| discoveryEntryPointArn | string<br />MinLength: 1<br />MaxLength: 2048 | True | A top-level supported Amazon Web Services resource ARN to discover a signal map from. |
| errorMessage | string<br />MinLength: 1<br />MaxLength: 2048 | False | Error message associated with a failed creation or failed update attempt of a signal map. |
| eventBridgeRuleTemplateGroupIds | Array of type string<br />Pattern: `^(aws-)?[0-9]{7}$`<br />MinLength: 7<br />MaxLength: 11 | False | An eventbridge rule template group's id. |
| failedMediaResourceMap | [FailedMediaResourceMap](#signal-maps-identifier-monitor-deployment-model-failedmediaresourcemap) | False | A map representing an incomplete Amazon Web Services media workflow as a graph. |
| id | string<br />Pattern: `^(aws-)?[0-9]{7}$`<br />MinLength: 7<br />MaxLength: 11 | True | A signal map's id. |
| lastDiscoveredAt | string<br />Format: date-time | False | The date and time of latest discovery. |
| lastSuccessfulMonitorDeployment | [SuccessfulMonitorDeployment](#signal-maps-identifier-monitor-deployment-model-successfulmonitordeployment) | False | The date and time of latest successful deployment. |
| mediaResourceMap | [MediaResourceMap](#signal-maps-identifier-monitor-deployment-model-mediaresourcemap) | False | A map representing an Amazon Web Services media workflow as a graph. |
| modifiedAt | string<br />Format: date-time | False | The date and time of latest resource modification. |
| monitorChangesPendingDeployment | boolean | True | If true, there are pending monitor changes for this signal map that can be deployed. |
| monitorDeployment | [MonitorDeployment](#signal-maps-identifier-monitor-deployment-model-monitordeployment) | False | Represents the latest monitor deployment of a signal map. |
| name | string<br />Pattern: `^[^\s]+$`<br />MinLength: 1<br />MaxLength: 255 | True | A resource's name. Names must be unique within the scope of a resource type in a specific region. |
| status | [SignalMapStatus](#signal-maps-identifier-monitor-deployment-model-signalmapstatus) | True | A signal map's current status, which is dependent on its lifecycle actions or associated jobs. |

### SuccessfulMonitorDeployment
<a name="signal-maps-identifier-monitor-deployment-model-successfulmonitordeployment"></a>

Represents the latest successful monitor deployment of a signal map.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| detailsUri | string<br />MinLength: 1<br />MaxLength: 2048 | True | URI associated with a signal map's monitor deployment. |
| status | [SignalMapMonitorDeploymentStatus](#signal-maps-identifier-monitor-deployment-model-signalmapmonitordeploymentstatus) | True | A signal map's monitor deployment status. |

### TooManyRequestsExceptionResponseContent
<a name="signal-maps-identifier-monitor-deployment-model-toomanyrequestsexceptionresponsecontent"></a>

Request was denied due to request throttling.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Exception error message. |

## See also
<a name="signal-maps-identifier-monitor-deployment-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### StartDeleteMonitorDeployment
<a name="StartDeleteMonitorDeployment-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/medialive-2017-10-14/StartDeleteMonitorDeployment)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/medialive-2017-10-14/StartDeleteMonitorDeployment)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/medialive-2017-10-14/StartDeleteMonitorDeployment)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/medialive-2017-10-14/StartDeleteMonitorDeployment)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/medialive-2017-10-14/StartDeleteMonitorDeployment)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/medialive-2017-10-14/StartDeleteMonitorDeployment)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/medialive-2017-10-14/StartDeleteMonitorDeployment)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/medialive-2017-10-14/StartDeleteMonitorDeployment)
+ [AWS SDK for Python](/goto/boto3/medialive-2017-10-14/StartDeleteMonitorDeployment)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/medialive-2017-10-14/StartDeleteMonitorDeployment)

### CorsSignal\_mapsIdentifierMonitor\_deployment
<a name="CorsSignal_mapsIdentifierMonitor_deployment-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/medialive-2017-10-14/CorsSignal_mapsIdentifierMonitor_deployment)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/medialive-2017-10-14/CorsSignal_mapsIdentifierMonitor_deployment)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/medialive-2017-10-14/CorsSignal_mapsIdentifierMonitor_deployment)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/medialive-2017-10-14/CorsSignal_mapsIdentifierMonitor_deployment)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/medialive-2017-10-14/CorsSignal_mapsIdentifierMonitor_deployment)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/medialive-2017-10-14/CorsSignal_mapsIdentifierMonitor_deployment)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/medialive-2017-10-14/CorsSignal_mapsIdentifierMonitor_deployment)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/medialive-2017-10-14/CorsSignal_mapsIdentifierMonitor_deployment)
+ [AWS SDK for Python](/goto/boto3/medialive-2017-10-14/CorsSignal_mapsIdentifierMonitor_deployment)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/medialive-2017-10-14/CorsSignal_mapsIdentifierMonitor_deployment)

### StartMonitorDeployment
<a name="StartMonitorDeployment-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/medialive-2017-10-14/StartMonitorDeployment)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/medialive-2017-10-14/StartMonitorDeployment)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/medialive-2017-10-14/StartMonitorDeployment)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/medialive-2017-10-14/StartMonitorDeployment)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/medialive-2017-10-14/StartMonitorDeployment)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/medialive-2017-10-14/StartMonitorDeployment)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/medialive-2017-10-14/StartMonitorDeployment)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/medialive-2017-10-14/StartMonitorDeployment)
+ [AWS SDK for Python](/goto/boto3/medialive-2017-10-14/StartMonitorDeployment)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/medialive-2017-10-14/StartMonitorDeployment)
