---
source_url: https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_ListPerformanceAnalysisReports.html
---

# ListPerformanceAnalysisReports
<a name="API_ListPerformanceAnalysisReports"></a>

Lists all the analysis reports created for the DB instance. The reports are sorted based on the start time of each report.

## Request Syntax
<a name="API_ListPerformanceAnalysisReports_RequestSyntax"></a>

```
{
   "Identifier": "{{string}}",
   "ListTags": {{boolean}},
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "ServiceType": "{{string}}"
}
```

## Request Parameters
<a name="API_ListPerformanceAnalysisReports_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [Identifier](#API_ListPerformanceAnalysisReports_RequestSyntax) **   <a name="performanceinsights-ListPerformanceAnalysisReports-request-Identifier"></a>
An immutable identifier for a data source that is unique for an AWS Region. Performance Insights gathers metrics from this data source. In the console, the identifier is shown as *ResourceID*. When you call `DescribeDBInstances`, the identifier is returned as `DbiResourceId`.
To use a DB instance as a data source, specify its `DbiResourceId` value. For example, specify `db-ABCDEFGHIJKLMNOPQRSTU1VW2X`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `^[a-zA-Z0-9-]+$`
Required: Yes

 ** [ServiceType](#API_ListPerformanceAnalysisReports_RequestSyntax) **   <a name="performanceinsights-ListPerformanceAnalysisReports-request-ServiceType"></a>
The AWS service for which Performance Insights returns metrics. Valid value is `RDS`.
Type: String
Valid Values: `RDS | DOCDB`
Required: Yes

 ** [ListTags](#API_ListPerformanceAnalysisReports_RequestSyntax) **   <a name="performanceinsights-ListPerformanceAnalysisReports-request-ListTags"></a>
Specifies whether or not to include the list of tags in the response.
Type: Boolean
Required: No

 ** [MaxResults](#API_ListPerformanceAnalysisReports_RequestSyntax) **   <a name="performanceinsights-ListPerformanceAnalysisReports-request-MaxResults"></a>
The maximum number of items to return in the response. If more items exist than the specified `MaxResults` value, a pagination token is included in the response so that the remaining results can be retrieved.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 25.
Required: No

 ** [NextToken](#API_ListPerformanceAnalysisReports_RequestSyntax) **   <a name="performanceinsights-ListPerformanceAnalysisReports-request-NextToken"></a>
An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the token, up to the value specified by `MaxResults`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Pattern: `^[a-zA-Z0-9_=-]+$`
Required: No

## Response Syntax
<a name="API_ListPerformanceAnalysisReports_ResponseSyntax"></a>

```
{
   "AnalysisReports": [
      {
         "AnalysisReportId": "string",
         "CreateTime": number,
         "EndTime": number,
         "StartTime": number,
         "Status": "string",
         "Tags": [
            {
               "Key": "string",
               "Value": "string"
            }
         ]
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListPerformanceAnalysisReports_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AnalysisReports](#API_ListPerformanceAnalysisReports_ResponseSyntax) **   <a name="performanceinsights-ListPerformanceAnalysisReports-response-AnalysisReports"></a>
List of reports including the report identifier, start and end time, creation time, and status.
Type: Array of [AnalysisReportSummary](API_AnalysisReportSummary.md) objects

 ** [NextToken](#API_ListPerformanceAnalysisReports_ResponseSyntax) **   <a name="performanceinsights-ListPerformanceAnalysisReports-response-NextToken"></a>
An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the token, up to the value specified by `MaxResults`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Pattern: `^[a-zA-Z0-9_=-]+$`

## Errors
<a name="API_ListPerformanceAnalysisReports_Errors"></a>

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
<a name="API_ListPerformanceAnalysisReports_Examples"></a>

### List of analysis reports for a DB instance
<a name="API_ListPerformanceAnalysisReports_Example_1"></a>

The following example lists all the analysis reports for the DB instance `db-ABC1DEFGHIJKL2MNOPQRSTUV3W` along with tags for each report.

#### Sample Request
<a name="API_ListPerformanceAnalysisReports_Example_1_Request"></a>

```
                    POST / HTTP/1.1
Host: <Hostname>
Accept-Encoding: identity
X-Amz-Target: PerformanceInsightsv20180227.ListPerformanceAnalysisReports
Content-Type: application/x-amz-json-1.1
User-Agent: <UserAgentString>
X-Amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>

{
    "Identifier": "db-ABC1DEFGHIJKL2MNOPQRSTUV3W",
    "ServiceType": "RDS",
    "ListTags": true,
    "MaxResults": 5
}
```

#### Sample Response
<a name="API_ListPerformanceAnalysisReports_Example_1_Response"></a>

```
                    HTTP/1.1 200 OK
Content-Type: application/x-amz-json-1.1
Date: <Date>
x-amzn-RequestId: <RequestId>
Content-Length: <PayloadSizeBytes>
Connection: keep-alive

{
    "AnalysisReports": [
        {
            "AnalysisReportId": "report-01234567890abcdef",
            "CreateTime": 1690561641.014,
            "EndTime": 1689356407,
            "StartTime": 1689161030,
            "Status": "SUCCEEDED",
            "Tags": [
                {
                    "Key": "Name",
                    "Value": "MyName1"
                }
            ]
        },
        {
            "AnalysisReportId": "report-01234567891abcdef",
            "CreateTime": 1690487582.167,
            "EndTime": 1689339840,
            "StartTime": 1689176864,
            "Status": "SUCCEEDED",
            "Tags": [
                {
                    "Key": "MyKey",
                    "Value": "MyValue"
                },
                {
                    "Key": "Name",
                    "Value": "MyName2"
                }
            ]
        },
        {
            "AnalysisReportId": "report-01234567892abcdef",
            "CreateTime": 1690551889.941,
            "EndTime": 1689324849,
            "StartTime": 1689177272,
            "Status": "SUCCEEDED",
            "Tags": [
                {
                    "Key": "Name",
                    "Value": ""
                }
            ]
        }
    ]
}
```

## See Also
<a name="API_ListPerformanceAnalysisReports_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pi-2018-02-27/ListPerformanceAnalysisReports)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pi-2018-02-27/ListPerformanceAnalysisReports)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pi-2018-02-27/ListPerformanceAnalysisReports)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pi-2018-02-27/ListPerformanceAnalysisReports)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pi-2018-02-27/ListPerformanceAnalysisReports)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pi-2018-02-27/ListPerformanceAnalysisReports)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pi-2018-02-27/ListPerformanceAnalysisReports)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pi-2018-02-27/ListPerformanceAnalysisReports)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/pi-2018-02-27/ListPerformanceAnalysisReports)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pi-2018-02-27/ListPerformanceAnalysisReports)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS Performance Insights. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query performance-insights` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
