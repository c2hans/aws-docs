---
source_url: https://docs.aws.amazon.com/datapipeline/latest/APIReference/API_SetTaskStatus.html
---

# SetTaskStatus
<a name="API_SetTaskStatus"></a>

Task runners call `SetTaskStatus` to notify AWS Data Pipeline that a task is completed and provide information about the final status. A task runner makes this call regardless of whether the task was sucessful. A task runner does not need to call `SetTaskStatus` for tasks that are canceled by the web service during a call to [ReportTaskProgress](API_ReportTaskProgress.md).

## Request Syntax
<a name="API_SetTaskStatus_RequestSyntax"></a>

```
{
   "errorId": "{{string}}",
   "errorMessage": "{{string}}",
   "errorStackTrace": "{{string}}",
   "taskId": "{{string}}",
   "taskStatus": "{{string}}"
}
```

## Request Parameters
<a name="API_SetTaskStatus_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [errorId](#API_SetTaskStatus_RequestSyntax) **   <a name="DP-SetTaskStatus-request-errorId"></a>
If an error occurred during the task, this value specifies the error code. This value is set on the physical attempt object. It is used to display error information to the user. It should not start with string "Service\_" which is reserved by the system.
Type: String
Required: No

 ** [errorMessage](#API_SetTaskStatus_RequestSyntax) **   <a name="DP-SetTaskStatus-request-errorMessage"></a>
If an error occurred during the task, this value specifies a text description of the error. This value is set on the physical attempt object. It is used to display error information to the user. The web service does not parse this value.
Type: String
Required: No

 ** [errorStackTrace](#API_SetTaskStatus_RequestSyntax) **   <a name="DP-SetTaskStatus-request-errorStackTrace"></a>
If an error occurred during the task, this value specifies the stack trace associated with the error. This value is set on the physical attempt object. It is used to display error information to the user. The web service does not parse this value.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4095.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** [taskId](#API_SetTaskStatus_RequestSyntax) **   <a name="DP-SetTaskStatus-request-taskId"></a>
The ID of the task assigned to the task runner. This value is provided in the response for [PollForTask](API_PollForTask.md).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: Yes

 ** [taskStatus](#API_SetTaskStatus_RequestSyntax) **   <a name="DP-SetTaskStatus-request-taskStatus"></a>
If `FINISHED`, the task successfully completed. If `FAILED`, the task ended unsuccessfully. Preconditions use false.
Type: String
Valid Values: `FINISHED | FAILED | FALSE`
Required: Yes

## Response Elements
<a name="API_SetTaskStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_SetTaskStatus_Errors"></a>

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
<a name="API_SetTaskStatus_Examples"></a>

### Example
<a name="API_SetTaskStatus_Example_1"></a>

This example illustrates one usage of SetTaskStatus.

#### Sample Request
<a name="API_SetTaskStatus_Example_1_Request"></a>

```
POST / HTTP/1.1
Content-Type: application/x-amz-json-1.1
X-Amz-Target: DataPipeline.SetTaskStatus
Content-Length: 847
Host: datapipeline.us-east-1.amazonaws.com
X-Amz-Date: Mon, 12 Nov 2012 17:49:52 GMT
Authorization: AuthParams

{"taskId": "aaGgHT4LuH0T0Y0oLrJRjas5qH0d8cDPADxqq3tn+zCWGELkCdV2JprLreXm1oxeP5EFZHFLJ69kjSsLYE0iYHYBYVGBrB+E/pYq7ANEEeGJFnSBMRiXZVA+8UJ3OzcInvXeinqBmBaKwii7hnnKb/AXjXiNTXyxgydX1KAyg1AxkwBYG4cfPYMZbuEbQJFJvv5C/2+GVXz1w94nKYTeUeepwUOFOuRLS6JVtZoYwpF56E+Yfk1IcGpFOvCZ01B4Bkuu7x3J+MD/j6kJgZLAgbCJQtI3eiW3kdGmX0p0I2BdY1ZsX6b4UiSvM3OMj6NEHJCJL4E0ZfitnhCoe24Kvjo6C2hFbZq+ei/HPgSXBQMSagkr4vS9c0ChzxH2+LNYvec6bY4kymkaZI1dvOzmpa0FcnGf5AjSK4GpsViZ/ujz6zxFv81qBXzjF0/4M1775rjV1VUdyKaixiA/sJiACNezqZqETidp8d24BDPRhGsj6pBCrnelqGFrk/gXEXUsJ+xwMifRC8UVwiKekpAvHUywVk7Ku4jH/n3i2VoLRP6FXwpUbelu34iiZ9czpXyLtyPKwxa87dlrnRVURwkcVjOt2Mcrcaqe+cbWHvNRhyrPkkdfSF3ac8/wfgVbXvLEB2k9mKc67aD9rvdc1PKX09Tk8BKklsMTpZ3TRCd4NzQlJKigMe8Jat9+1tKj4Ole5ZzW6uyTu2s2iFjEV8KXu4MaiRJyNKCdKeGhhZWY37Qk4NBK4Ppgu+C6Y41dpfOh288SLDEVx0/UySlqOEdhba7c6BiPp5r3hKj3mk9lFy5OYp1aoGLeeFmjXveTnPdf2gkWqXXg7AUbJ7jEs1F0lKZQg4szep2gcKyAJXgvXLfJJHcha8Lfb/Ee7wYmyOcAaRpDBoFNSbtoVXar46teIrpho+ZDvynUXvU0grHWGOk=:wn3SgymHZM99bEXAMPLE",
 "taskStatus": "FINISHED"}
```

#### Sample Response
<a name="API_SetTaskStatus_Example_1_Response"></a>

```
x-amzn-RequestId: 8c8deb53-0788-11e2-af9c-6bc7a6be6qr8
Content-Type: application/x-amz-json-1.1
Content-Length: 0
Date: Mon, 12 Nov 2012 17:50:53 GMT

{}
```

## See Also
<a name="API_SetTaskStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datapipeline-2012-10-29/SetTaskStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datapipeline-2012-10-29/SetTaskStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datapipeline-2012-10-29/SetTaskStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datapipeline-2012-10-29/SetTaskStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datapipeline-2012-10-29/SetTaskStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datapipeline-2012-10-29/SetTaskStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datapipeline-2012-10-29/SetTaskStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datapipeline-2012-10-29/SetTaskStatus)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datapipeline-2012-10-29/SetTaskStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datapipeline-2012-10-29/SetTaskStatus)
