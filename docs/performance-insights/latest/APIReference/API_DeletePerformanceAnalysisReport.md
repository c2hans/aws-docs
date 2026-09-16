---
source_url: https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_DeletePerformanceAnalysisReport.html
---

# DeletePerformanceAnalysisReport
<a name="API_DeletePerformanceAnalysisReport"></a>

Deletes a performance analysis report.

## Request Syntax
<a name="API_DeletePerformanceAnalysisReport_RequestSyntax"></a>

```
{
   "AnalysisReportId": "{{string}}",
   "Identifier": "{{string}}",
   "ServiceType": "{{string}}"
}
```

## Request Parameters
<a name="API_DeletePerformanceAnalysisReport_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [AnalysisReportId](#API_DeletePerformanceAnalysisReport_RequestSyntax) **   <a name="performanceinsights-DeletePerformanceAnalysisReport-request-AnalysisReportId"></a>
The unique identifier of the analysis report for deletion.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `report-[0-9a-f]{17}`
Required: Yes

 ** [Identifier](#API_DeletePerformanceAnalysisReport_RequestSyntax) **   <a name="performanceinsights-DeletePerformanceAnalysisReport-request-Identifier"></a>
An immutable identifier for a data source that is unique for an AWS Region. Performance Insights gathers metrics from this data source. In the console, the identifier is shown as *ResourceID*. When you call `DescribeDBInstances`, the identifier is returned as `DbiResourceId`.
To use a DB instance as a data source, specify its `DbiResourceId` value. For example, specify `db-ABCDEFGHIJKLMNOPQRSTU1VW2X`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `^[a-zA-Z0-9-]+$`
Required: Yes

 ** [ServiceType](#API_DeletePerformanceAnalysisReport_RequestSyntax) **   <a name="performanceinsights-DeletePerformanceAnalysisReport-request-ServiceType"></a>
The AWS service for which Performance Insights will return metrics. Valid value is `RDS`.
Type: String
Valid Values: `RDS | DOCDB`
Required: Yes

## Response Elements
<a name="API_DeletePerformanceAnalysisReport_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeletePerformanceAnalysisReport_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceError **
The request failed due to an unknown error.
HTTP Status Code: 500

 ** InvalidArgumentException **
One of the arguments provided is invalid for this request.
HTTP Status Code: 400

 ** NotAuthorizedException **
The user is not authorized to perform this request.
HTTP Status Code: 400

## Examples
<a name="API_DeletePerformanceAnalysisReport_Examples"></a>

### Delete a perfornamce analysis report
<a name="API_DeletePerformanceAnalysisReport_Example_1"></a>

The following example deletes the performance analysis report `report-01234567890abcdef`.

#### Sample Request
<a name="API_DeletePerformanceAnalysisReport_Example_1_Request"></a>

```
                    POST / HTTP/1.1
Host: <Hostname>
Accept-Encoding: identity
X-Amz-Target: PerformanceInsightsv20180227.GetPerformanceAnalysisReport
Content-Type: application/x-amz-json-1.1
User-Agent: <UserAgentString>
X-Amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>

{
    "AnalysisReportId": "report-01234567890abcdef",
    "Identifier": "db-ABC1DEFGHIJKL2MNOPQRSTUV3W",
    "ServiceType": "RDS"
}
```

#### Sample Response
<a name="API_DeletePerformanceAnalysisReport_Example_1_Response"></a>

```
                    HTTP/1.1 200 OK
Content-Type: application/x-amz-json-1.1
Date: <Date>
x-amzn-RequestId: <RequestId>
Content-Length: <PayloadSizeBytes>
Connection: keep-alive
```

## See Also
<a name="API_DeletePerformanceAnalysisReport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pi-2018-02-27/DeletePerformanceAnalysisReport)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pi-2018-02-27/DeletePerformanceAnalysisReport)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pi-2018-02-27/DeletePerformanceAnalysisReport)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pi-2018-02-27/DeletePerformanceAnalysisReport)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pi-2018-02-27/DeletePerformanceAnalysisReport)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pi-2018-02-27/DeletePerformanceAnalysisReport)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pi-2018-02-27/DeletePerformanceAnalysisReport)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pi-2018-02-27/DeletePerformanceAnalysisReport)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/pi-2018-02-27/DeletePerformanceAnalysisReport)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pi-2018-02-27/DeletePerformanceAnalysisReport)
