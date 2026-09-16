---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_ListReportPlans.html
---

# ListReportPlans
<a name="API_ListReportPlans"></a>

Returns a list of your report plans. For detailed information about a single report plan, use `DescribeReportPlan`.

## Request Syntax
<a name="API_ListReportPlans_RequestSyntax"></a>

```
GET /audit/report-plans?MaxResults={{MaxResults}}&NextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListReportPlans_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_ListReportPlans_RequestSyntax) **   <a name="Backup-ListReportPlans-request-uri-MaxResults"></a>
The number of desired results from 1 to 1000. Optional. If unspecified, the query will return 1 MB of data.
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [NextToken](#API_ListReportPlans_RequestSyntax) **   <a name="Backup-ListReportPlans-request-uri-NextToken"></a>
An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

## Request Body
<a name="API_ListReportPlans_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListReportPlans_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "ReportPlans": [
      {
         "CreationTime": number,
         "DeploymentStatus": "string",
         "LastAttemptedExecutionTime": number,
         "LastSuccessfulExecutionTime": number,
         "ReportDeliveryChannel": {
            "Formats": [ "string" ],
            "S3BucketName": "string",
            "S3KeyPrefix": "string"
         },
         "ReportPlanArn": "string",
         "ReportPlanDescription": "string",
         "ReportPlanName": "string",
         "ReportSetting": {
            "Accounts": [ "string" ],
            "FrameworkArns": [ "string" ],
            "NumberOfFrameworks": number,
            "OrganizationUnits": [ "string" ],
            "Regions": [ "string" ],
            "ReportTemplate": "string"
         }
      }
   ]
}
```

## Response Elements
<a name="API_ListReportPlans_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListReportPlans_ResponseSyntax) **   <a name="Backup-ListReportPlans-response-NextToken"></a>
An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.
Type: String

 ** [ReportPlans](#API_ListReportPlans_ResponseSyntax) **   <a name="Backup-ListReportPlans-response-ReportPlans"></a>
The report plans with detailed information for each plan. This information includes the Amazon Resource Name (ARN), report plan name, description, settings, delivery channel, deployment status, creation time, and last times the report plan attempted to and successfully ran.
Type: Array of [ReportPlan](API_ReportPlan.md) objects

## Errors
<a name="API_ListReportPlans_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterValueException **
Indicates that something is wrong with a parameter's value. For example, the value is out of range.
 ** Context **

 ** Type **

HTTP Status Code: 400

 ** ServiceUnavailableException **
The request failed due to a temporary failure of the server.
 ** Context **

 ** Type **

HTTP Status Code: 500

## See Also
<a name="API_ListReportPlans_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/backup-2018-11-15/ListReportPlans)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/backup-2018-11-15/ListReportPlans)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/ListReportPlans)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/backup-2018-11-15/ListReportPlans)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/ListReportPlans)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/backup-2018-11-15/ListReportPlans)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/backup-2018-11-15/ListReportPlans)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/backup-2018-11-15/ListReportPlans)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/backup-2018-11-15/ListReportPlans)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/ListReportPlans)
