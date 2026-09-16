---
source_url: https://docs.aws.amazon.com/datapipeline/latest/APIReference/API_PollForTask.html
---

# PollForTask
<a name="API_PollForTask"></a>

Task runners call `PollForTask` to receive a task to perform from AWS Data Pipeline. The task runner specifies which tasks it can perform by setting a value for the `workerGroup` parameter. The task returned can come from any of the pipelines that match the `workerGroup` value passed in by the task runner and that was launched using the user credentials specified by the task runner.

If tasks are ready in the work queue, `PollForTask` returns a response immediately. If no tasks are available in the queue, `PollForTask` uses long-polling and holds on to a poll connection for up to a 90 seconds, during which time the first newly scheduled task is handed to the task runner. To accomodate this, set the socket timeout in your task runner to 90 seconds. The task runner should not call `PollForTask` again on the same `workerGroup` until it receives a response, and this can take up to 90 seconds.

## Request Syntax
<a name="API_PollForTask_RequestSyntax"></a>

```
{
   "hostname": "{{string}}",
   "instanceIdentity": {
      "document": "{{string}}",
      "signature": "{{string}}"
   },
   "workerGroup": "{{string}}"
}
```

## Request Parameters
<a name="API_PollForTask_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [hostname](#API_PollForTask_RequestSyntax) **   <a name="DP-PollForTask-request-hostname"></a>
The public DNS name of the calling task runner.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\n\t]*`
Required: No

 ** [instanceIdentity](#API_PollForTask_RequestSyntax) **   <a name="DP-PollForTask-request-instanceIdentity"></a>
Identity information for the EC2 instance that is hosting the task runner. You can get this value from the instance using `http://169.254.169.254/latest/meta-data/instance-id`. For more information, see [Instance Metadata](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AESDG-chapter-instancedata.html) in the *Amazon Elastic Compute Cloud User Guide.* Passing in this value proves that your task runner is running on an EC2 instance, and ensures the proper AWS Data Pipeline service charges are applied to your pipeline.
Type: [InstanceIdentity](API_InstanceIdentity.md) object
Required: No

 ** [workerGroup](#API_PollForTask_RequestSyntax) **   <a name="DP-PollForTask-request-workerGroup"></a>
The type of task the task runner is configured to accept and process. The worker group is set as a field on objects in the pipeline when they are created. You can only specify a single value for `workerGroup` in the call to `PollForTask`. There are no wildcard values permitted in `workerGroup`; the string must be an exact, case-sensitive, match.
Type: String
Required: Yes

## Response Syntax
<a name="API_PollForTask_ResponseSyntax"></a>

```
{
   "taskObject": {
      "attemptId": "string",
      "objects": {
         "string" : {
            "fields": [
               {
                  "key": "string",
                  "refValue": "string",
                  "stringValue": "string"
               }
            ],
            "id": "string",
            "name": "string"
         }
      },
      "pipelineId": "string",
      "taskId": "string"
   }
}
```

## Response Elements
<a name="API_PollForTask_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [taskObject](#API_PollForTask_ResponseSyntax) **   <a name="DP-PollForTask-response-taskObject"></a>
The information needed to complete the task that is being assigned to the task runner. One of the fields returned in this object is `taskId`, which contains an identifier for the task being assigned. The calling task runner uses `taskId` in subsequent calls to [ReportTaskProgress](API_ReportTaskProgress.md) and [SetTaskStatus](API_SetTaskStatus.md).
Type: [TaskObject](API_TaskObject.md) object

## Errors
<a name="API_PollForTask_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceError **
An internal service error occurred.
 ** message **
Description of the error message.
HTTP Status Code: 500

 ** InvalidRequestException **
The request was not valid. Verify that your request was properly formatted, that the signature was generated with the correct credentials, and that you haven't exceeded any of the service limits for your account.
 ** message **
Description of the error message.
HTTP Status Code: 400

 ** TaskNotFoundException **
The specified task was not found.
 ** message **
Description of the error message.
HTTP Status Code: 400

## Examples
<a name="API_PollForTask_Examples"></a>

### Example
<a name="API_PollForTask_Example_1"></a>

This example illustrates one usage of PollForTask.

#### Sample Request
<a name="API_PollForTask_Example_1_Request"></a>

```
POST / HTTP/1.1
Content-Type: application/x-amz-json-1.1
X-Amz-Target: DataPipeline.PollForTask
Content-Length: 59
Host: datapipeline.us-east-1.amazonaws.com
X-Amz-Date: Mon, 12 Nov 2012 17:49:52 GMT
Authorization: AuthParams

{"workerGroup": "MyworkerGroup",
 "hostname": "example.com"}
```

#### Sample Response
<a name="API_PollForTask_Example_1_Response"></a>

```

x-amzn-RequestId: 41c713d2-0775-11e2-af6f-6bc7a6be60d9
Content-Type: application/x-amz-json-1.1
Content-Length: 39
Date: Mon, 12 Nov 2012 17:50:53 GMT

{"taskObject":
  {"attemptId": "@SayHello_2012-12-12T00:00:00_Attempt=1",
   "objects":
    {"@SayHello_2012-12-12T00:00:00_Attempt=1":
      {"fields":
        [
          {"key": "@componentParent",
           "refValue": "SayHello"},
          {"key": "@scheduledStartTime",
           "stringValue": "2012-12-12T00:00:00"},
          {"key": "parent",
           "refValue": "SayHello"},
          {"key": "@sphere",
           "stringValue": "ATTEMPT"},
          {"key": "workerGroup",
           "stringValue": "workerGroup"},
          {"key": "@instanceParent",
           "refValue": "@SayHello_2012-12-12T00:00:00"},
          {"key": "type",
           "stringValue": "ShellCommandActivity"},
          {"key": "@status",
           "stringValue": "WAITING_FOR_RUNNER"},
          {"key": "@version",
           "stringValue": "1"},
          {"key": "schedule",
           "refValue": "Schedule"},
          {"key": "@actualStartTime",
           "stringValue": "2012-12-13T01:40:50"},
          {"key": "command",
           "stringValue": "echo hello"},
          {"key": "@scheduledEndTime",
           "stringValue": "2012-12-12T01:00:00"},
          {"key": "@activeInstances",
           "refValue": "@SayHello_2012-12-12T00:00:00"},
          {"key": "@pipelineId",
           "stringValue": "df-0937003356ZJEXAMPLE"}
        ],
       "id": "@SayHello_2012-12-12T00:00:00_Attempt=1",
       "name": "@SayHello_2012-12-12T00:00:00_Attempt=1"}
    },
   "pipelineId": "df-0937003356ZJEXAMPLE",
   "taskId": "2xaM4wRs5zOsIH+g9U3oVHfAgAlbSqU6XduncB0HhZ3xMnmvfePZPn4dIbYXHyWyRK+cU15MqDHwdrvftx/4wv+sNS4w34vJfv7QA9aOoOazW28l1GYSb2ZRR0N0paiQp+d1MhSKo10hOTWOsVK5S5Lnx9Qm6omFgXHyIvZRIvTlrQMpr1xuUrflyGOfbFOGpOLpvPE172MYdqpZKnbSS4TcuqgQKSWV2833fEubI57DPOP7ghWa2TcYeSIv4pdLYG53fTuwfbnbdc98g2LNUQzSVhSnt7BoqyNwht2aQ6b/UHg9A80+KVpuXuqmz3m1MXwHFgxjdmuesXNOrrlGpeLCcRWD+aGo0RN1NqhQRzNAig8V4GlaPTQzMsRCljKqvrIyAoP3Tt2XEGsHkkQo12rEX8Z90957XX2qKRwhruwYzqGkSLWjINoLdAxUJdpRXRc5DJTrBd3D5mdzn7kY1l7NEh4kFHJDt3Cx4Z3Mk8MYCACyCk/CEyy9DwuPi66cLz0NBcgbCM5LKjTBOwo1m+am+pvM1kSposE9FPP1+RFGb8k6jQBTJx3TRz1yKilnGXQTZ5xvdOFpJrklIT0OXP1MG3+auM9FlJA+1dX90QoNJE5z7axmK//MOGXUdkqFe2kiDkorqjxwDvc0Js9pVKfKvAmW8YqUbmI9l0ERpWCXXnLVHNmPWz3jaPY+OBAmuJWDmxB/Z8p94aEDg4BVXQ7LvsKQ3DLYhaB7yJ390CJT+i0mm+EBqY60V6YikPSWDFrYQ/NPi2b1DgE19mX8zHqw8qprIl4yh1Ckx2Iige4En/N5ktOoIxnASxAw/TzcE2skxdw5KlHDF+UTj71m16CR/dIaKlXijlfNlNzUBo/bNSadCQn3G5NoO501wPKI:XO50TgDNyo8EXAMPLE/g==:1"}
}
```

## See Also
<a name="API_PollForTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datapipeline-2012-10-29/PollForTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datapipeline-2012-10-29/PollForTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datapipeline-2012-10-29/PollForTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datapipeline-2012-10-29/PollForTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datapipeline-2012-10-29/PollForTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datapipeline-2012-10-29/PollForTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datapipeline-2012-10-29/PollForTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datapipeline-2012-10-29/PollForTask)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/datapipeline-2012-10-29/PollForTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datapipeline-2012-10-29/PollForTask)
