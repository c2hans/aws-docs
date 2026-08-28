---
source_url: https://docs.aws.amazon.com/mediaconvert/latest/apireference/queues.html
---

# Queues
<a name="queues"></a>

## URI
<a name="queues-url"></a>

`/2017-08-29/queues`

## HTTP methods
<a name="queues-http-methods"></a>

### GET
<a name="queuesget"></a>

**Operation ID:** `ListQueues`

Retrieve a JSON array of up to twenty of your queues. This will return the queues themselves, not just a list of them. To retrieve the next twenty queues, use the nextToken string returned with the array.

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| listBy | String | False |  |
| nextToken | String | False |  |
| maxResults | String | False |  |
| order | String | False |  |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | ListQueuesResponse | 200 response |
| 400 | ExceptionBody | The service can't process your request because of a problem in the request. Please check your request form and syntax. |
| 402 | ExceptionBody | You attempted to create more resources than the service allows based on service quotas. |
| 403 | ExceptionBody | You don't have permissions for this action with the credentials you sent. |
| 404 | ExceptionBody | The resource you requested does not exist. |
| 409 | ExceptionBody | The service could not complete your request because there is a conflict with the current state of the resource. |
| 429 | ExceptionBody | Too many requests have been sent in too short of a time. The service limits the rate at which it will accept requests. |
| 500 | ExceptionBody | The service encountered an unexpected condition and cannot fulfill your request. |

### POST
<a name="queuespost"></a>

**Operation ID:** `CreateQueue`

Create a new transcoding queue. For information about queues, see Working With Queues in the User Guide at https://docs.aws.amazon.com/mediaconvert/latest/ug/working-with-queues.html

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 201 | CreateQueueResponse | 201 response |
| 400 | ExceptionBody | The service can't process your request because of a problem in the request. Please check your request form and syntax. |
| 402 | ExceptionBody | You attempted to create more resources than the service allows based on service quotas. |
| 403 | ExceptionBody | You don't have permissions for this action with the credentials you sent. |
| 404 | ExceptionBody | The resource you requested does not exist. |
| 409 | ExceptionBody | The service could not complete your request because there is a conflict with the current state of the resource. |
| 429 | ExceptionBody | Too many requests have been sent in too short of a time. The service limits the rate at which it will accept requests. |
| 500 | ExceptionBody | The service encountered an unexpected condition and cannot fulfill your request. |

### OPTIONS
<a name="queuesoptions"></a>

Supports CORS preflight requests.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | The request completed successfully. |

## Schemas
<a name="queues-schemas"></a>

### Request bodies
<a name="queues-request-examples"></a>

#### GET schema
<a name="queues-request-body-get-example"></a>

```
{
  "listBy": enum,
  "order": enum,
  "nextToken": "string",
  "maxResults": integer
}
```

#### POST schema
<a name="queues-request-body-post-example"></a>

```
{
  "description": "string",
  "tags": {
  },
  "name": "string",
  "pricingPlan": enum,
  "reservationPlanSettings": {
    "reservedSlots": integer,
    "renewalType": enum,
    "commitment": enum
  },
  "status": enum,
  "concurrentJobs": integer,
  "maximumConcurrentFeeds": integer
}
```

### Response bodies
<a name="queues-response-examples"></a>

#### ListQueuesResponse schema
<a name="queues-response-body-listqueuesresponse-example"></a>

```
{
  "queues": [
    {
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
  ],
  "nextToken": "string",
  "totalConcurrentJobs": integer,
  "unallocatedConcurrentJobs": integer
}
```

#### CreateQueueResponse schema
<a name="queues-response-body-createqueueresponse-example"></a>

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

#### ExceptionBody schema
<a name="queues-response-body-exceptionbody-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="queues-properties"></a>

### Commitment
<a name="queues-model-commitment"></a>

The length of the term of your reserved queue pricing plan commitment.
+ `ONE_YEAR`

### CreateQueueRequest
<a name="queues-model-createqueuerequest"></a>

Create an on-demand queue by sending a CreateQueue request with the name of the queue. Create a reserved queue by sending a CreateQueue request with the pricing plan set to RESERVED and with values specified for the settings under reservationPlanSettings. When you create a reserved queue, you enter into a 12-month commitment to purchase the RTS that you specify. You can't cancel this commitment.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| concurrentJobs | integer<br />Format: int64 | False | Specify the maximum number of jobs your queue can process concurrently. For on-demand queues, the value you enter is constrained by your service quotas for Maximum concurrent jobs, per on-demand queue and Maximum concurrent jobs, per account. For reserved queues, specify the number of jobs you can process concurrently in your reservation plan instead. |
| description | string | False | Optional. A description of the queue that you are creating. |
| maximumConcurrentFeeds | integer<br />Format: int32<br />Minimum: 0 | False | Specify the maximum number of Elemental Inference feeds MediaConvert can process concurrently. |
| name | string | True | The name of the queue that you are creating. |
| pricingPlan | [PricingPlan](#queues-model-pricingplan) | False | Specifies whether the pricing plan for the queue is on-demand or reserved. For on-demand, you pay per minute, billed in increments of .01 minute. For reserved, you pay for the transcoding capacity of the entire queue, regardless of how much or how little you use it. Reserved pricing requires a 12-month commitment. When you use the API to create a queue, the default is on-demand. |
| reservationPlanSettings | [ReservationPlanSettings](#queues-model-reservationplansettings) | False | Details about the pricing plan for your reserved queue. Required for reserved queues and not applicable to on-demand queues. |
| status | [QueueStatus](#queues-model-queuestatus) | False | Initial state of the queue. If you create a paused queue, then jobs in that queue won't begin. |
| tags | object | False | The tags that you want to add to the resource. You can tag resources with a key-value pair or with only a key. |

### CreateQueueResponse
<a name="queues-model-createqueueresponse"></a>

Successful create queue requests return the name of the queue that you just created and information about it.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| queue | [Queue](#queues-model-queue) | False | You can use queues to manage the resources that are available to your AWS account for running multiple transcoding jobs at the same time. If you don't specify a queue, the service sends all jobs through the default queue. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/working-with-queues.html. |

### ExceptionBody
<a name="queues-model-exceptionbody"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### ListQueuesRequest
<a name="queues-model-listqueuesrequest"></a>

You can send list queues requests with an empty body. You can optionally specify the maximum number, up to twenty, of queues to be returned.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| listBy | [QueueListBy](#queues-model-queuelistby) | False | Optional. When you request a list of queues, you can choose to list them alphabetically by NAME or chronologically by CREATION\_DATE. If you don't specify, the service will list them by creation date. |
| maxResults | integer<br />Format: int32<br />Minimum: 1<br />Maximum: 20 | False | Optional. Number of queues, up to twenty, that will be returned at one time. |
| nextToken | string | False | Use this string, provided with the response to a previous request, to request the next batch of queues. |
| order | [Order](#queues-model-order) | False | Optional. When you request lists of resources, you can specify whether they are sorted in ASCENDING or DESCENDING order. Default varies by resource. |

### ListQueuesResponse
<a name="queues-model-listqueuesresponse"></a>

Successful list queues requests return a JSON array of queues. If you don't specify how they are ordered, you will receive them alphabetically by name.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| nextToken | string | False | Use this string to request the next batch of queues. |
| queues | Array of type [Queue](#queues-model-queue) | False | List of queues. |
| totalConcurrentJobs | integer<br />Format: int64 | False | The maximum number of jobs that MediaConvert can process at one time, across all of your on-demand queues in the current AWS Region. |
| unallocatedConcurrentJobs | integer<br />Format: int64 | False | The remaining number of concurrent jobs that are not associated with a queue and are available to allocate to a queue. You can allocate these jobs when you create or update a queue. |

### Order
<a name="queues-model-order"></a>

Optional. When you request lists of resources, you can specify whether they are sorted in ASCENDING or DESCENDING order. Default varies by resource.
+ `ASCENDING`
+ `DESCENDING`

### PricingPlan
<a name="queues-model-pricingplan"></a>

Specifies whether the pricing plan for the queue is on-demand or reserved. For on-demand, you pay per minute, billed in increments of .01 minute. For reserved, you pay for the transcoding capacity of the entire queue, regardless of how much or how little you use it. Reserved pricing requires a 12-month commitment.
+ `ON_DEMAND`
+ `RESERVED`

### Queue
<a name="queues-model-queue"></a>

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
| pricingPlan | [PricingPlan](#queues-model-pricingplan) | False | Specifies whether the pricing plan for the queue is on-demand or reserved. For on-demand, you pay per minute, billed in increments of .01 minute. For reserved, you pay for the transcoding capacity of the entire queue, regardless of how much or how little you use it. Reserved pricing requires a 12-month commitment. |
| progressingJobsCount | integer<br />Format: int64 | False | The estimated number of jobs with a PROGRESSING status. |
| reservationPlan | [ReservationPlan](#queues-model-reservationplan) | False | Details about the pricing plan for your reserved queue. Required for reserved queues and not applicable to on-demand queues. |
| serviceOverrides | Array of type [ServiceOverride](#queues-model-serviceoverride) | False | A list of any service overrides applied by MediaConvert to the settings that you have configured. If you see any overrides, we recommend that you contact Support. |
| status | [QueueStatus](#queues-model-queuestatus) | False | Queues can be ACTIVE or PAUSED. If you pause a queue, the service won't begin processing jobs in that queue. Jobs that are running when you pause the queue continue to run until they finish or result in an error. |
| submittedJobsCount | integer<br />Format: int64 | False | The estimated number of jobs with a SUBMITTED status. |
| type | [Type](#queues-model-type) | False | Specifies whether this on-demand queue is system or custom. System queues are built in. You can't modify or delete system queues. You can create and modify custom queues. |

### QueueListBy
<a name="queues-model-queuelistby"></a>

Optional. When you request a list of queues, you can choose to list them alphabetically by NAME or chronologically by CREATION\_DATE. If you don't specify, the service will list them by creation date.
+ `NAME`
+ `CREATION_DATE`

### QueueStatus
<a name="queues-model-queuestatus"></a>

Queues can be ACTIVE or PAUSED. If you pause a queue, jobs in that queue won't begin. Jobs that are running when you pause a queue continue to run until they finish or result in an error.
+ `ACTIVE`
+ `PAUSED`

### RenewalType
<a name="queues-model-renewaltype"></a>

Specifies whether the term of your reserved queue pricing plan is automatically extended (AUTO\_RENEW) or expires (EXPIRE) at the end of the term.
+ `AUTO_RENEW`
+ `EXPIRE`

### ReservationPlan
<a name="queues-model-reservationplan"></a>

Details about the pricing plan for your reserved queue. Required for reserved queues and not applicable to on-demand queues.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| commitment | [Commitment](#queues-model-commitment) | False | The length of the term of your reserved queue pricing plan commitment. |
| expiresAt | string<br />Format: date-time | False | The timestamp in epoch seconds for when the current pricing plan term for this reserved queue expires. |
| purchasedAt | string<br />Format: date-time | False | The timestamp in epoch seconds for when you set up the current pricing plan for this reserved queue. |
| renewalType | [RenewalType](#queues-model-renewaltype) | False | Specifies whether the term of your reserved queue pricing plan is automatically extended (AUTO\_RENEW) or expires (EXPIRE) at the end of the term. |
| reservedSlots | integer<br />Format: int32 | False | Specifies the number of reserved transcode slots (RTS) for this queue. The number of RTS determines how many jobs the queue can process in parallel; each RTS can process one job at a time. When you increase this number, you extend your existing commitment with a new 12-month commitment for a larger number of RTS. The new commitment begins when you purchase the additional capacity. You can't decrease the number of RTS in your reserved queue. |
| status | [ReservationPlanStatus](#queues-model-reservationplanstatus) | False | Specifies whether the pricing plan for your reserved queue is ACTIVE or EXPIRED. |

### ReservationPlanSettings
<a name="queues-model-reservationplansettings"></a>

Details about the pricing plan for your reserved queue. Required for reserved queues and not applicable to on-demand queues.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| commitment | [Commitment](#queues-model-commitment) | True | The length of the term of your reserved queue pricing plan commitment. |
| renewalType | [RenewalType](#queues-model-renewaltype) | True | Specifies whether the term of your reserved queue pricing plan is automatically extended (AUTO\_RENEW) or expires (EXPIRE) at the end of the term. When your term is auto renewed, you extend your commitment by 12 months from the auto renew date. You can cancel this commitment. |
| reservedSlots | integer<br />Format: int32 | True | Specifies the number of reserved transcode slots (RTS) for this queue. The number of RTS determines how many jobs the queue can process in parallel; each RTS can process one job at a time. You can't decrease the number of RTS in your reserved queue. You can increase the number of RTS by extending your existing commitment with a new 12-month commitment for the larger number. The new commitment begins when you purchase the additional capacity. You can't cancel your commitment or revert to your original commitment after you increase the capacity. |

### ReservationPlanStatus
<a name="queues-model-reservationplanstatus"></a>

Specifies whether the pricing plan for your reserved queue is ACTIVE or EXPIRED.
+ `ACTIVE`
+ `EXPIRED`

### ServiceOverride
<a name="queues-model-serviceoverride"></a>

A service override applied by MediaConvert to the settings that you have configured. If you see any overrides, we recommend that you contact Support.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Details about the service override that MediaConvert has applied. |
| name | string | False | The name of the setting that MediaConvert has applied an override to. |
| overrideValue | string | False | The current value of the service override that MediaConvert has applied. |
| value | string | False | The value of the setting that you configured, prior to any overrides that MediaConvert has applied. |

### Type
<a name="queues-model-type"></a>
+ `SYSTEM`
+ `CUSTOM`

## See also
<a name="queues-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### ListQueues
<a name="ListQueues-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/mediaconvert-2017-08-29/ListQueues)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/mediaconvert-2017-08-29/ListQueues)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/mediaconvert-2017-08-29/ListQueues)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/mediaconvert-2017-08-29/ListQueues)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/mediaconvert-2017-08-29/ListQueues)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/mediaconvert-2017-08-29/ListQueues)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/mediaconvert-2017-08-29/ListQueues)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/mediaconvert-2017-08-29/ListQueues)
+ [AWS SDK for Python](/goto/boto3/mediaconvert-2017-08-29/ListQueues)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/mediaconvert-2017-08-29/ListQueues)

### CreateQueue
<a name="CreateQueue-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/mediaconvert-2017-08-29/CreateQueue)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/mediaconvert-2017-08-29/CreateQueue)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/mediaconvert-2017-08-29/CreateQueue)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/mediaconvert-2017-08-29/CreateQueue)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/mediaconvert-2017-08-29/CreateQueue)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/mediaconvert-2017-08-29/CreateQueue)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/mediaconvert-2017-08-29/CreateQueue)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/mediaconvert-2017-08-29/CreateQueue)
+ [AWS SDK for Python](/goto/boto3/mediaconvert-2017-08-29/CreateQueue)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/mediaconvert-2017-08-29/CreateQueue)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConvert. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconvert` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
