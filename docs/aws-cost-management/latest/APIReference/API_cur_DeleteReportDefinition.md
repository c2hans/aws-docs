---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_cur_DeleteReportDefinition.html
---

# DeleteReportDefinition
<a name="API_cur_DeleteReportDefinition"></a>

Deletes the specified report. Any tags associated with the report are also deleted.

## Request Syntax
<a name="API_cur_DeleteReportDefinition_RequestSyntax"></a>

```
{
   "ReportName": "{{string}}"
}
```

## Request Parameters
<a name="API_cur_DeleteReportDefinition_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ReportName](#API_cur_DeleteReportDefinition_RequestSyntax) **   <a name="awscostmanagement-cur_DeleteReportDefinition-request-ReportName"></a>
The name of the report that you want to delete. The name must be unique, is case sensitive, and can't include spaces.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `[0-9A-Za-z!\-_.*\'()]+`
Required: Yes

## Response Syntax
<a name="API_cur_DeleteReportDefinition_ResponseSyntax"></a>

```
{
   "ResponseMessage": "string"
}
```

## Response Elements
<a name="API_cur_DeleteReportDefinition_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ResponseMessage](#API_cur_DeleteReportDefinition_ResponseSyntax) **   <a name="awscostmanagement-cur_DeleteReportDefinition-response-ResponseMessage"></a>
Whether the deletion was successful or not.
Type: String

## Errors
<a name="API_cur_DeleteReportDefinition_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalErrorException **
An error on the server occurred during the processing of your request. Try again later.
 ** Message **
A message to show the detail of the exception.
HTTP Status Code: 500

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
 ** Message **
A message to show the detail of the exception.
HTTP Status Code: 400

## Examples
<a name="API_cur_DeleteReportDefinition_Examples"></a>

### The following is a sample request of the DeleteReportDefinition operation.
<a name="API_cur_DeleteReportDefinition_Example_1"></a>

This example illustrates one usage of DeleteReportDefinition.

#### Sample Request
<a name="API_cur_DeleteReportDefinition_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: api.cur.<region>.<domain>
x-amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=contenttype;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid,Signature=<Signature>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: AWSOrigamiServiceGateway.DeleteReportDefinition
{
        "ReportName": "ExampleReport"
}
```

## See Also
<a name="API_cur_DeleteReportDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cur-2017-01-06/DeleteReportDefinition)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cur-2017-01-06/DeleteReportDefinition)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cur-2017-01-06/DeleteReportDefinition)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cur-2017-01-06/DeleteReportDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cur-2017-01-06/DeleteReportDefinition)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cur-2017-01-06/DeleteReportDefinition)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cur-2017-01-06/DeleteReportDefinition)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cur-2017-01-06/DeleteReportDefinition)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cur-2017-01-06/DeleteReportDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cur-2017-01-06/DeleteReportDefinition)
