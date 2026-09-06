---
source_url: https://docs.aws.amazon.com/datapipeline/latest/APIReference/API_ReportTaskProgress.html
---

# ReportTaskProgress
<a name="API_ReportTaskProgress"></a>

Task runners call `ReportTaskProgress` when assigned a task to acknowledge that it has the task. If the web service does not receive this acknowledgement within 2 minutes, it assigns the task in a subsequent [PollForTask](API_PollForTask.md) call. After this initial acknowledgement, the task runner only needs to report progress every 15 minutes to maintain its ownership of the task. You can change this reporting time from 15 minutes by specifying a `reportProgressTimeout` field in your pipeline.

## Request Syntax
<a name="API_ReportTaskProgress_RequestSyntax"></a>

```
{
   "fields": [
      {
         "key": "{{string}}",
         "refValue": "{{string}}",
         "stringValue": "{{string}}"
      }
   ],
   "taskId": "{{string}}"
}
```

## Request Parameters
<a name="API_ReportTaskProgress_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [fields](#API_ReportTaskProgress_RequestSyntax) **   <a name="DP-ReportTaskProgress-request-fields"></a>
Key-value pairs that define the properties of the ReportTaskProgressInput object.
Type: Array of [Field](API_Field.md) objects
Required: No

 ** [taskId](#API_ReportTaskProgress_RequestSyntax) **   <a name="DP-ReportTaskProgress-request-taskId"></a>
The ID of the task assigned to the task runner. This value is provided in the response for [PollForTask](API_PollForTask.md).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: Yes

## Response Syntax
<a name="API_ReportTaskProgress_ResponseSyntax"></a>

```
{
   "canceled": boolean
}
```

## Response Elements
<a name="API_ReportTaskProgress_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [canceled](#API_ReportTaskProgress_ResponseSyntax) **   <a name="DP-ReportTaskProgress-response-canceled"></a>
If true, the calling task runner should cancel processing of the task. The task runner does not need to call [SetTaskStatus](API_SetTaskStatus.md) for canceled tasks.
Type: Boolean

## Errors
<a name="API_ReportTaskProgress_Errors"></a>

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

 ** PipelineDeletedException **
The specified pipeline has been deleted.
 ** message **
Description of the error message.
HTTP Status Code: 400

 ** PipelineNotFoundException **
The specified pipeline was not found. Verify that you used the correct user and account identifiers.
 ** message **
Description of the error message.
HTTP Status Code: 400

 ** TaskNotFoundException **
The specified task was not found.
 ** message **
Description of the error message.
HTTP Status Code: 400

## Examples
<a name="API_ReportTaskProgress_Examples"></a>

### Example
<a name="API_ReportTaskProgress_Example_1"></a>

This example illustrates one usage of ReportTaskProgress.

#### Sample Request
<a name="API_ReportTaskProgress_Example_1_Request"></a>

```
POST / HTTP/1.1
Content-Type: application/x-amz-json-1.1
X-Amz-Target: DataPipeline.ReportTaskProgress
Content-Length: 832
Host: datapipeline.us-east-1.amazonaws.com
X-Amz-Date: Mon, 12 Nov 2012 17:49:52 GMT
Authorization: AuthParams

{"taskId": "aaGgHT4LuH0T0Y0oLrJRjas5qH0d8cDPADxqq3tn+zCWGELkCdV2JprLreXm1oxeP5EFZHFLJ69kjSsLYE0iYHYBYVGBrB+E/pYq7ANEEeGJFnSBMRiXZVA+8UJ3OzcInvXeinqBmBaKwii7hnnKb/AXjXiNTXyxgydX1KAyg1AxkwBYG4cfPYMZbuEbQJFJvv5C/2+GVXz1w94nKYTeUeepwUOFOuRLS6JVtZoYwpF56E+Yfk1IcGpFOvCZ01B4Bkuu7x3J+MD/j6kJgZLAgbCJQtI3eiW3kdGmX0p0I2BdY1ZsX6b4UiSvM3OMj6NEHJCJL4E0ZfitnhCoe24Kvjo6C2hFbZq+ei/HPgSXBQMSagkr4vS9c0ChzxH2+LNYvec6bY4kymkaZI1dvOzmpa0FcnGf5AjSK4GpsViZ/ujz6zxFv81qBXzjF0/4M1775rjV1VUdyKaixiA/sJiACNezqZqETidp8d24BDPRhGsj6pBCrnelqGFrk/gXEXUsJ+xwMifRC8UVwiKekpAvHUywVk7Ku4jH/n3i2VoLRP6FXwpUbelu34iiZ9czpXyLtyPKwxa87dlrnRVURwkcVjOt2Mcrcaqe+cbWHvNRhyrPkkdfSF3ac8/wfgVbXvLEB2k9mKc67aD9rvdc1PKX09Tk8BKklsMTpZ3TRCd4NzQlJKigMe8Jat9+1tKj4Ole5ZzW6uyTu2s2iFjEV8KXu4MaiRJyNKCdKeGhhZWY37Qk4NBK4Ppgu+C6Y41dpfOh288SLDEVx0/UySlqOEdhba7c6BiPp5r3hKj3mk9lFy5OYp1aoGLeeFmjXveTnPdf2gkWqXXg7AUbJ7jEs1F0lKZQg4szep2gcKyAJXgvXLfJJHcha8Lfb/Ee7wYmyOcAaRpDBoFNSbtoVXar46teIrpho+ZDvynUXvU0grHWGOk=:wn3SgymHZM99bEXAMPLE",
 "fields":
  [
    {"key": "percentComplete",
     "stringValue": "50"}
  ]
}
```

#### Sample Response
<a name="API_ReportTaskProgress_Example_1_Response"></a>

```
x-amzn-RequestId: 640bd023-0775-11e2-af6f-6bc7a6be60d9
Content-Type: application/x-amz-json-1.1
Content-Length: 18
Date: Mon, 12 Nov 2012 17:50:53 GMT

{"canceled": false}
```

## See Also
<a name="API_ReportTaskProgress_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datapipeline-2012-10-29/ReportTaskProgress)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datapipeline-2012-10-29/ReportTaskProgress)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datapipeline-2012-10-29/ReportTaskProgress)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datapipeline-2012-10-29/ReportTaskProgress)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datapipeline-2012-10-29/ReportTaskProgress)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datapipeline-2012-10-29/ReportTaskProgress)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datapipeline-2012-10-29/ReportTaskProgress)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datapipeline-2012-10-29/ReportTaskProgress)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datapipeline-2012-10-29/ReportTaskProgress)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datapipeline-2012-10-29/ReportTaskProgress)
