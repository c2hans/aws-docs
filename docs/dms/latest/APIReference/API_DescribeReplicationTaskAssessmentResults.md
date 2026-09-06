---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeReplicationTaskAssessmentResults.html
---

# DescribeReplicationTaskAssessmentResults
<a name="API_DescribeReplicationTaskAssessmentResults"></a>

Returns the task assessment results from the Amazon S3 bucket that AWS DMS creates in your AWS account. This action always returns the latest results.

For more information about AWS DMS task assessments, see [Creating a task assessment report](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.AssessmentReport.html) in the * AWS Database Migration Service User Guide*.

## Request Syntax
<a name="API_DescribeReplicationTaskAssessmentResults_RequestSyntax"></a>

```
{
   "Marker": "{{string}}",
   "MaxRecords": {{number}},
   "ReplicationTaskArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeReplicationTaskAssessmentResults_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Marker](#API_DescribeReplicationTaskAssessmentResults_RequestSyntax) **   <a name="DMS-DescribeReplicationTaskAssessmentResults-request-Marker"></a>
 An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.
Type: String
Required: No

 ** [MaxRecords](#API_DescribeReplicationTaskAssessmentResults_RequestSyntax) **   <a name="DMS-DescribeReplicationTaskAssessmentResults-request-MaxRecords"></a>
 The maximum number of records to include in the response. If more records exist than the specified `MaxRecords` value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.
Default: 100
Constraints: Minimum 20, maximum 100.
Type: Integer
Required: No

 ** [ReplicationTaskArn](#API_DescribeReplicationTaskAssessmentResults_RequestSyntax) **   <a name="DMS-DescribeReplicationTaskAssessmentResults-request-ReplicationTaskArn"></a>
The Amazon Resource Name (ARN) string that uniquely identifies the task. When this input parameter is specified, the API returns only one result and ignore the values of the `MaxRecords` and `Marker` parameters.
Type: String
Required: No

## Response Syntax
<a name="API_DescribeReplicationTaskAssessmentResults_ResponseSyntax"></a>

```
{
   "BucketName": "string",
   "Marker": "string",
   "ReplicationTaskAssessmentResults": [
      {
         "AssessmentResults": "string",
         "AssessmentResultsFile": "string",
         "AssessmentStatus": "string",
         "ReplicationTaskArn": "string",
         "ReplicationTaskIdentifier": "string",
         "ReplicationTaskLastAssessmentDate": number,
         "S3ObjectUrl": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeReplicationTaskAssessmentResults_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [BucketName](#API_DescribeReplicationTaskAssessmentResults_ResponseSyntax) **   <a name="DMS-DescribeReplicationTaskAssessmentResults-response-BucketName"></a>
- The Amazon S3 bucket where the task assessment report is located.
Type: String

 ** [Marker](#API_DescribeReplicationTaskAssessmentResults_ResponseSyntax) **   <a name="DMS-DescribeReplicationTaskAssessmentResults-response-Marker"></a>
 An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.
Type: String

 ** [ReplicationTaskAssessmentResults](#API_DescribeReplicationTaskAssessmentResults_ResponseSyntax) **   <a name="DMS-DescribeReplicationTaskAssessmentResults-response-ReplicationTaskAssessmentResults"></a>
 The task assessment report.
Type: Array of [ReplicationTaskAssessmentResult](API_ReplicationTaskAssessmentResult.md) objects

## Errors
<a name="API_DescribeReplicationTaskAssessmentResults_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFoundFault **
The resource could not be found.
 ** message **

HTTP Status Code: 400

## See Also
<a name="API_DescribeReplicationTaskAssessmentResults_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dms-2016-01-01/DescribeReplicationTaskAssessmentResults)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dms-2016-01-01/DescribeReplicationTaskAssessmentResults)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/DescribeReplicationTaskAssessmentResults)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dms-2016-01-01/DescribeReplicationTaskAssessmentResults)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/DescribeReplicationTaskAssessmentResults)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dms-2016-01-01/DescribeReplicationTaskAssessmentResults)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dms-2016-01-01/DescribeReplicationTaskAssessmentResults)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dms-2016-01-01/DescribeReplicationTaskAssessmentResults)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dms-2016-01-01/DescribeReplicationTaskAssessmentResults)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/DescribeReplicationTaskAssessmentResults)
