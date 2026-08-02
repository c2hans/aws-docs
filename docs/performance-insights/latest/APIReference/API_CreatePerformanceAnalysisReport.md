---
source_url: https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_CreatePerformanceAnalysisReport.html
---

# CreatePerformanceAnalysisReport
<a name="API_CreatePerformanceAnalysisReport"></a>

Creates a new performance analysis report for a specific time period for the DB instance.

## Request Syntax
<a name="API_CreatePerformanceAnalysisReport_RequestSyntax"></a>

```
{
   "EndTime": {{number}},
   "Identifier": "{{string}}",
   "ServiceType": "{{string}}",
   "StartTime": {{number}},
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreatePerformanceAnalysisReport_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [Identifier](#API_CreatePerformanceAnalysisReport_RequestSyntax) **   <a name="performanceinsights-CreatePerformanceAnalysisReport-request-Identifier"></a>
An immutable, AWS Region-unique identifier for a data source. Performance Insights gathers metrics from this data source.
To use an Amazon RDS instance as a data source, you specify its `DbiResourceId` value. For example, specify `db-ADECBTYHKTSAUMUZQYPDS2GW4A`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `^[a-zA-Z0-9-]+$`
Required: Yes

 ** [ServiceType](#API_CreatePerformanceAnalysisReport_RequestSyntax) **   <a name="performanceinsights-CreatePerformanceAnalysisReport-request-ServiceType"></a>
The AWS service for which Performance Insights will return metrics. Valid value is `RDS`.
Type: String
Valid Values: `RDS | DOCDB`
Required: Yes

 ** [StartTime](#API_CreatePerformanceAnalysisReport_RequestSyntax) **   <a name="performanceinsights-CreatePerformanceAnalysisReport-request-StartTime"></a>
The start time defined for the analysis report.
Type: Timestamp
Required: Yes

 ** [EndTime](#API_CreatePerformanceAnalysisReport_RequestSyntax) **   <a name="performanceinsights-CreatePerformanceAnalysisReport-request-EndTime"></a>
The end time defined for the analysis report.
Type: Timestamp
Required: No

 ** [Tags](#API_CreatePerformanceAnalysisReport_RequestSyntax) **   <a name="performanceinsights-CreatePerformanceAnalysisReport-request-Tags"></a>
The metadata assigned to the analysis report consisting of a key-value pair.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

## Response Syntax
<a name="API_CreatePerformanceAnalysisReport_ResponseSyntax"></a>

```
{
   "AnalysisReportId": "string"
}
```

## Response Elements
<a name="API_CreatePerformanceAnalysisReport_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AnalysisReportId](#API_CreatePerformanceAnalysisReport_ResponseSyntax) **   <a name="performanceinsights-CreatePerformanceAnalysisReport-response-AnalysisReportId"></a>
A unique identifier for the created analysis report.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `report-[0-9a-f]{17}`

## Errors
<a name="API_CreatePerformanceAnalysisReport_Errors"></a>

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
<a name="API_CreatePerformanceAnalysisReport_Examples"></a>

### Create a performance analysis report
<a name="API_CreatePerformanceAnalysisReport_Example_1"></a>

The following example creates a performance analysis report for the specified time period and adds the specified tag to the report.

#### Sample Request
<a name="API_CreatePerformanceAnalysisReport_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: <Hostname>
Accept-Encoding: identity
X-Amz-Target: PerformanceInsightsv20180227.CreatePerformanceAnalysisReport
Content-Type: application/x-amz-json-1.1
User-Agent: <UserAgentString>
X-Amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>

{
    "ServiceType": "RDS",
    "Identifier": "db-ABC1DEFGHIJKL2MNOPQRSTUV3W",
    "StartTime": 1689280091,
    "EndTime": 1689282071,
    "Tags": [{
        "Key": "Name",
        "Value": "MyName"
    }]
}
```

#### Sample Response
<a name="API_CreatePerformanceAnalysisReport_Example_1_Response"></a>

```
                    HTTP/1.1 200 OK
Content-Type: application/x-amz-json-1.1
Date: <Date>
x-amzn-RequestId: <RequestId>
Content-Length: <PayloadSizeBytes>
Connection: keep-alive

{
    "AnalysisReportId": "report-01234567890abcdef"
}
```

## See Also
<a name="API_CreatePerformanceAnalysisReport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pi-2018-02-27/CreatePerformanceAnalysisReport)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pi-2018-02-27/CreatePerformanceAnalysisReport)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pi-2018-02-27/CreatePerformanceAnalysisReport)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pi-2018-02-27/CreatePerformanceAnalysisReport)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pi-2018-02-27/CreatePerformanceAnalysisReport)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pi-2018-02-27/CreatePerformanceAnalysisReport)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pi-2018-02-27/CreatePerformanceAnalysisReport)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pi-2018-02-27/CreatePerformanceAnalysisReport)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/pi-2018-02-27/CreatePerformanceAnalysisReport)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pi-2018-02-27/CreatePerformanceAnalysisReport)
