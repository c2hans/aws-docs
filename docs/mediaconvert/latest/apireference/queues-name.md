---
source_url: https://docs.aws.amazon.com/mediaconvert/latest/apireference/queues-name.html
---

# Queues name
<a name="queues-name"></a>

## URI
<a name="queues-name-url"></a>

`/2017-08-29/queues/{{name}}`

## HTTP methods
<a name="queues-name-http-methods"></a>

### GET
<a name="queues-nameget"></a>

**Operation ID:** `GetQueue`

Retrieve the JSON for a specific queue.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{name}} | String | True |  |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | GetQueueResponse | 200 response |
| 400 | ExceptionBody | The service can't process your request because of a problem in the request. Please check your request form and syntax. |
| 402 | ExceptionBody | You attempted to create more resources than the service allows based on service quotas. |
| 403 | ExceptionBody | You don't have permissions for this action with the credentials you sent. |
| 404 | ExceptionBody | The resource you requested does not exist. |
| 409 | ExceptionBody | The service could not complete your request because there is a conflict with the current state of the resource. |
| 429 | ExceptionBody | Too many requests have been sent in too short of a time. The service limits the rate at which it will accept requests. |
| 500 | ExceptionBody | The service encountered an unexpected condition and cannot fulfill your request. |

### PUT
<a name="queues-nameput"></a>

**Operation ID:** `UpdateQueue`

Modify one of your existing queues.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{name}} | String | True |  |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | UpdateQueueResponse | 200 response |
| 400 | ExceptionBody | The service can't process your request because of a problem in the request. Please check your request form and syntax. |
| 402 | ExceptionBody | You attempted to create more resources than the service allows based on service quotas. |
| 403 | ExceptionBody | You don't have permissions for this action with the credentials you sent. |
| 404 | ExceptionBody | The resource you requested does not exist. |
| 409 | ExceptionBody | The service could not complete your request because there is a conflict with the current state of the resource. |
| 429 | ExceptionBody | Too many requests have been sent in too short of a time. The service limits the rate at which it will accept requests. |
| 500 | ExceptionBody | The service encountered an unexpected condition and cannot fulfill your request. |

### DELETE
<a name="queues-namedelete"></a>

**Operation ID:** `DeleteQueue`

Permanently delete a queue you have created.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{name}} | String | True |  |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 202 | DeleteQueueResponse | 202 response |
| 400 | ExceptionBody | The service can't process your request because of a problem in the request. Please check your request form and syntax. |
| 402 | ExceptionBody | You attempted to create more resources than the service allows based on service quotas. |
| 403 | ExceptionBody | You don't have permissions for this action with the credentials you sent. |
| 404 | ExceptionBody | The resource you requested does not exist. |
| 409 | ExceptionBody | The service could not complete your request because there is a conflict with the current state of the resource. |
| 429 | ExceptionBody | Too many requests have been sent in too short of a time. The service limits the rate at which it will accept requests. |
| 500 | ExceptionBody | The service encountered an unexpected condition and cannot fulfill your request. |

### OPTIONS
<a name="queues-nameoptions"></a>

Supports CORS preflight requests.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{name}} | String | True |  |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | The request completed successfully. |

## Schemas
<a name="queues-name-schemas"></a>

### Request bodies
<a name="queues-name-request-examples"></a>

#### GET schema
<a name="queues-name-request-body-get-example"></a>

```
{
  "name": "string"
}
```

#### PUT schema
<a name="queues-name-request-body-put-example"></a>

```
{
  "description": "string",
  "status": enum,
  "name": "string",
  "reservationPlanSettings": {
    "reservedSlots": integer,
    "renewalType": enum,
    "commitment": enum
  },
  "concurrentJobs": integer,
  "maximumConcurrentFeeds": integer
}
```

#### DELETE schema
<a name="queues-name-request-body-delete-example"></a>

```
{
  "name": "string"
}
```

### Response bodies
<a name="queues-name-response-examples"></a>

#### GetQueueResponse schema
<a name="queues-name-response-body-getqueueresponse-example"></a>

```
{
  "queue": {
    "arn": "string",
    "createdAt": "string",
    "lastUpdated": "string",
    "type": enum,
    "pricingPlan": enum,
    "status": enum,
    "description": "string",
    "name": "string",
    "submittedJobsCount": integer,
    "progressingJobsCount": integer,
    "reservationPlan": {
      "reservedSlots": integer,
      "renewalType": enum,
      "commitment": enum,
      "purchasedAt": "string",
      "expiresAt": "string",
      "status": enum
    },
    "concurrentJobs": integer,
    "serviceOverrides": [
      {
        "name": "string",
        "value": "string",
        "overrideValue": "string",
        "message": "string"
      }
    ],
    "maximumConcurrentFeeds": integer
  }
}
```

#### UpdateQueueResponse schema
<a name="queues-name-response-body-updatequeueresponse-example"></a>

```
{
  "queue": {
    "arn": "string",
    "createdAt": "string",
    "lastUpdated": "string",
    "type": enum,
    "pricingPlan": enum,
    "status": enum,
    "description": "string",
    "name": "string",
    "submittedJobsCount": integer,
    "progressingJobsCount": integer,
    "reservationPlan": {
      "reservedSlots": integer,
      "renewalType": enum,
      "commitment": enum,
      "purchasedAt": "string",
      "expiresAt": "string",
      "status": enum
    },
    "concurrentJobs": integer,
    "serviceOverrides": [
      {
        "name": "string",
        "value": "string",
        "overrideValue": "string",
        "message": "string"
      }
    ],
    "maximumConcurrentFeeds": integer
  }
}
```

#### DeleteQueueResponse schema
<a name="queues-name-response-body-deletequeueresponse-example"></a>

```
{
}
```

#### ExceptionBody schema
<a name="queues-name-response-body-exceptionbody-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="queues-name-properties"></a>

### Commitment
<a name="queues-name-model-commitment"></a>

The length of the term of your reserved queue pricing plan commitment.
+ `ONE_YEAR`

### DeleteQueueRequest
<a name="queues-name-model-deletequeuerequest"></a>

Delete a queue by sending a request with the queue name. You can't delete a queue with an active pricing plan or one that has unprocessed jobs in it.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| name | string | False | The name of the queue that you want to delete. |

### DeleteQueueResponse
<a name="queues-name-model-deletequeueresponse"></a>

Delete queue requests return an OK message or error message with an empty body.

### ExceptionBody
<a name="queues-name-model-exceptionbody"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### GetQueueRequest
<a name="queues-name-model-getqueuerequest"></a>

Get information about a queue by sending a request with the queue name.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| name | string | False | The name of the queue that you want information about. |

### GetQueueResponse
<a name="queues-name-model-getqueueresponse"></a>

Successful get queue requests return an OK message and information about the queue in JSON.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| queue | [Queue](#queues-name-model-queue) | False | You can use queues to manage the resources that are available to your AWS account for running multiple transcoding jobs at the same time. If you don't specify a queue, the service sends all jobs through the default queue. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/working-with-queues.html. |

### PricingPlan
<a name="queues-name-model-pricingplan"></a>

Specifies whether the pricing plan for the queue is on-demand or reserved. For on-demand, you pay per minute, billed in increments of .01 minute. For reserved, you pay for the transcoding capacity of the entire queue, regardless of how much or how little you use it. Reserved pricing requires a 12-month commitment.
+ `ON_DEMAND`
+ `RESERVED`

### Queue
<a name="queues-name-model-queue"></a>

You can use queues to manage the resources that are available to your AWS account for running multiple transcoding jobs at the same time. If you don't specify a queue, the service sends all jobs through the default queue. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/working-with-queues.html.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| arn | string | False | An identifier for this resource that is unique within all of AWS. |
| concurrentJobs | integer<br />Format: int64 | False | The maximum number of jobs your queue can process concurrently. |
| createdAt | string<br />Format: date-time | False | The timestamp in epoch seconds for when you created the queue. |
| description | string | False | An optional description that you create for each queue. |
| lastUpdated | string<br />Format: date-time | False | The timestamp in epoch seconds for when you most recently updated the queue. |
| maximumConcurrentFeeds | integer<br />Format: int32<br />Minimum: 0 | False | Specify the maximum number of Elemental Inference feeds MediaConvert can process concurrently. |
| name | string | True | A name that you create for each queue. Each name must be unique within your account. |
| pricingPlan | [PricingPlan](#queues-name-model-pricingplan) | False | Specifies whether the pricing plan for the queue is on-demand or reserved. For on-demand, you pay per minute, billed in increments of .01 minute. For reserved, you pay for the transcoding capacity of the entire queue, regardless of how much or how little you use it. Reserved pricing requires a 12-month commitment. |
| progressingJobsCount | integer<br />Format: int64 | False | The estimated number of jobs with a PROGRESSING status. |
| reservationPlan | [ReservationPlan](#queues-name-model-reservationplan) | False | Details about the pricing plan for your reserved queue. Required for reserved queues and not applicable to on-demand queues. |
| serviceOverrides | Array of type [ServiceOverride](#queues-name-model-serviceoverride) | False | A list of any service overrides applied by MediaConvert to the settings that you have configured. If you see any overrides, we recommend that you contact Support. |
| status | [QueueStatus](#queues-name-model-queuestatus) | False | Queues can be ACTIVE or PAUSED. If you pause a queue, the service won't begin processing jobs in that queue. Jobs that are running when you pause the queue continue to run until they finish or result in an error. |
| submittedJobsCount | integer<br />Format: int64 | False | The estimated number of jobs with a SUBMITTED status. |
| type | [Type](#queues-name-model-type) | False | Specifies whether this on-demand queue is system or custom. System queues are built in. You can't modify or delete system queues. You can create and modify custom queues. |

### QueueStatus
<a name="queues-name-model-queuestatus"></a>

Queues can be ACTIVE or PAUSED. If you pause a queue, jobs in that queue won't begin. Jobs that are running when you pause a queue continue to run until they finish or result in an error.
+ `ACTIVE`
+ `PAUSED`

### RenewalType
<a name="queues-name-model-renewaltype"></a>

Specifies whether the term of your reserved queue pricing plan is automatically extended (AUTO\_RENEW) or expires (EXPIRE) at the end of the term.
+ `AUTO_RENEW`
+ `EXPIRE`

### ReservationPlan
<a name="queues-name-model-reservationplan"></a>

Details about the pricing plan for your reserved queue. Required for reserved queues and not applicable to on-demand queues.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| commitment | [Commitment](#queues-name-model-commitment) | False | The length of the term of your reserved queue pricing plan commitment. |
| expiresAt | string<br />Format: date-time | False | The timestamp in epoch seconds for when the current pricing plan term for this reserved queue expires. |
| purchasedAt | string<br />Format: date-time | False | The timestamp in epoch seconds for when you set up the current pricing plan for this reserved queue. |
| renewalType | [RenewalType](#queues-name-model-renewaltype) | False | Specifies whether the term of your reserved queue pricing plan is automatically extended (AUTO\_RENEW) or expires (EXPIRE) at the end of the term. |
| reservedSlots | integer<br />Format: int32 | False | Specifies the number of reserved transcode slots (RTS) for this queue. The number of RTS determines how many jobs the queue can process in parallel; each RTS can process one job at a time. When you increase this number, you extend your existing commitment with a new 12-month commitment for a larger number of RTS. The new commitment begins when you purchase the additional capacity. You can't decrease the number of RTS in your reserved queue. |
| status | [ReservationPlanStatus](#queues-name-model-reservationplanstatus) | False | Specifies whether the pricing plan for your reserved queue is ACTIVE or EXPIRED. |

### ReservationPlanSettings
<a name="queues-name-model-reservationplansettings"></a>

Details about the pricing plan for your reserved queue. Required for reserved queues and not applicable to on-demand queues.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| commitment | [Commitment](#queues-name-model-commitment) | True | The length of the term of your reserved queue pricing plan commitment. |
| renewalType | [RenewalType](#queues-name-model-renewaltype) | True | Specifies whether the term of your reserved queue pricing plan is automatically extended (AUTO\_RENEW) or expires (EXPIRE) at the end of the term. When your term is auto renewed, you extend your commitment by 12 months from the auto renew date. You can cancel this commitment. |
| reservedSlots | integer<br />Format: int32 | True | Specifies the number of reserved transcode slots (RTS) for this queue. The number of RTS determines how many jobs the queue can process in parallel; each RTS can process one job at a time. You can't decrease the number of RTS in your reserved queue. You can increase the number of RTS by extending your existing commitment with a new 12-month commitment for the larger number. The new commitment begins when you purchase the additional capacity. You can't cancel your commitment or revert to your original commitment after you increase the capacity. |

### ReservationPlanStatus
<a name="queues-name-model-reservationplanstatus"></a>

Specifies whether the pricing plan for your reserved queue is ACTIVE or EXPIRED.
+ `ACTIVE`
+ `EXPIRED`

### ServiceOverride
<a name="queues-name-model-serviceoverride"></a>

A service override applied by MediaConvert to the settings that you have configured. If you see any overrides, we recommend that you contact Support.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Details about the service override that MediaConvert has applied. |
| name | string | False | The name of the setting that MediaConvert has applied an override to. |
| overrideValue | string | False | The current value of the service override that MediaConvert has applied. |
| value | string | False | The value of the setting that you configured, prior to any overrides that MediaConvert has applied. |

### Type
<a name="queues-name-model-type"></a>
+ `SYSTEM`
+ `CUSTOM`

### UpdateQueueRequest
<a name="queues-name-model-updatequeuerequest"></a>

Modify a queue by sending a request with the queue name and any changes to the queue.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| concurrentJobs | integer<br />Format: int64 | False | Specify the maximum number of jobs your queue can process concurrently. For on-demand queues, the value you enter is constrained by your service quotas for Maximum concurrent jobs, per on-demand queue and Maximum concurrent jobs, per account. For reserved queues, update your reservation plan instead in order to increase your yearly commitment. |
| description | string | False | The new description for the queue, if you are changing it. |
| maximumConcurrentFeeds | integer<br />Format: int32<br />Minimum: 0 | False | Specify the maximum number of Elemental Inference feeds MediaConvert can process concurrently. |
| name | string | False | The name of the queue that you are modifying. |
| reservationPlanSettings | [ReservationPlanSettings](#queues-name-model-reservationplansettings) | False | The new details of your pricing plan for your reserved queue. When you set up a new pricing plan to replace an expired one, you enter into another 12-month commitment. When you add capacity to your queue by increasing the number of RTS, you extend the term of your commitment to 12 months from when you add capacity. After you make these commitments, you can't cancel them. |
| status | [QueueStatus](#queues-name-model-queuestatus) | False | Pause or activate a queue by changing its status between ACTIVE and PAUSED. If you pause a queue, jobs in that queue won't begin. Jobs that are running when you pause the queue continue to run until they finish or result in an error. |

### UpdateQueueResponse
<a name="queues-name-model-updatequeueresponse"></a>

Successful update queue requests return the new queue information in JSON format.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| queue | [Queue](#queues-name-model-queue) | False | You can use queues to manage the resources that are available to your AWS account for running multiple transcoding jobs at the same time. If you don't specify a queue, the service sends all jobs through the default queue. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/working-with-queues.html. |

## See also
<a name="queues-name-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### GetQueue
<a name="GetQueue-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/mediaconvert-2017-08-29/GetQueue)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/mediaconvert-2017-08-29/GetQueue)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/mediaconvert-2017-08-29/GetQueue)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/mediaconvert-2017-08-29/GetQueue)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/mediaconvert-2017-08-29/GetQueue)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/mediaconvert-2017-08-29/GetQueue)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/mediaconvert-2017-08-29/GetQueue)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/mediaconvert-2017-08-29/GetQueue)
+ [AWS SDK for Python](/goto/boto3/mediaconvert-2017-08-29/GetQueue)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/mediaconvert-2017-08-29/GetQueue)

### UpdateQueue
<a name="UpdateQueue-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/mediaconvert-2017-08-29/UpdateQueue)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/mediaconvert-2017-08-29/UpdateQueue)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/mediaconvert-2017-08-29/UpdateQueue)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/mediaconvert-2017-08-29/UpdateQueue)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/mediaconvert-2017-08-29/UpdateQueue)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/mediaconvert-2017-08-29/UpdateQueue)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/mediaconvert-2017-08-29/UpdateQueue)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/mediaconvert-2017-08-29/UpdateQueue)
+ [AWS SDK for Python](/goto/boto3/mediaconvert-2017-08-29/UpdateQueue)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/mediaconvert-2017-08-29/UpdateQueue)

### DeleteQueue
<a name="DeleteQueue-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/mediaconvert-2017-08-29/DeleteQueue)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/mediaconvert-2017-08-29/DeleteQueue)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/mediaconvert-2017-08-29/DeleteQueue)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/mediaconvert-2017-08-29/DeleteQueue)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/mediaconvert-2017-08-29/DeleteQueue)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/mediaconvert-2017-08-29/DeleteQueue)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/mediaconvert-2017-08-29/DeleteQueue)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/mediaconvert-2017-08-29/DeleteQueue)
+ [AWS SDK for Python](/goto/boto3/mediaconvert-2017-08-29/DeleteQueue)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/mediaconvert-2017-08-29/DeleteQueue)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConvert. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconvert` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
