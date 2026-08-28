---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeReplicationTaskAssessmentRuns.html
---

# DescribeReplicationTaskAssessmentRuns
<a name="API_DescribeReplicationTaskAssessmentRuns"></a>

Returns a paginated list of premigration assessment runs based on filter settings.

These filter settings can specify a combination of premigration assessment runs, migration tasks, replication instances, and assessment run status values.

**Note**
This operation doesn't return information about individual assessments. For this information, see the `DescribeReplicationTaskIndividualAssessments` operation.

## Request Syntax
<a name="API_DescribeReplicationTaskAssessmentRuns_RequestSyntax"></a>

```
{
   "Filters": [
      {
         "Name": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "Marker": "{{string}}",
   "MaxRecords": {{number}}
}
```

## Request Parameters
<a name="API_DescribeReplicationTaskAssessmentRuns_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_DescribeReplicationTaskAssessmentRuns_RequestSyntax) **   <a name="DMS-DescribeReplicationTaskAssessmentRuns-request-Filters"></a>
Filters applied to the premigration assessment runs described in the form of key-value pairs.
Valid filter names: `replication-task-assessment-run-arn`, `replication-task-arn`, `replication-instance-arn`, `status`
Type: Array of [Filter](API_Filter.md) objects
Required: No

 ** [Marker](#API_DescribeReplicationTaskAssessmentRuns_RequestSyntax) **   <a name="DMS-DescribeReplicationTaskAssessmentRuns-request-Marker"></a>
An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.
Type: String
Required: No

 ** [MaxRecords](#API_DescribeReplicationTaskAssessmentRuns_RequestSyntax) **   <a name="DMS-DescribeReplicationTaskAssessmentRuns-request-MaxRecords"></a>
The maximum number of records to include in the response. If more records exist than the specified `MaxRecords` value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.
Type: Integer
Required: No

## Response Syntax
<a name="API_DescribeReplicationTaskAssessmentRuns_ResponseSyntax"></a>

```
{
   "Marker": "string",
   "ReplicationTaskAssessmentRuns": [
      {
         "AssessmentProgress": {
            "IndividualAssessmentCompletedCount": number,
            "IndividualAssessmentCount": number
         },
         "AssessmentRunName": "string",
         "IsLatestTaskAssessmentRun": boolean,
         "LastFailureMessage": "string",
         "ReplicationTaskArn": "string",
         "ReplicationTaskAssessmentRunArn": "string",
         "ReplicationTaskAssessmentRunCreationDate": number,
         "ResultEncryptionMode": "string",
         "ResultKmsKeyArn": "string",
         "ResultLocationBucket": "string",
         "ResultLocationFolder": "string",
         "ResultStatistic": {
            "Cancelled": number,
            "Error": number,
            "Failed": number,
            "Passed": number,
            "Skipped": number,
            "Warning": number
         },
         "ServiceAccessRoleArn": "string",
         "Status": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeReplicationTaskAssessmentRuns_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Marker](#API_DescribeReplicationTaskAssessmentRuns_ResponseSyntax) **   <a name="DMS-DescribeReplicationTaskAssessmentRuns-response-Marker"></a>
A pagination token returned for you to pass to a subsequent request. If you pass this token as the `Marker` value in a subsequent request, the response includes only records beyond the marker, up to the value specified in the request by `MaxRecords`.
Type: String

 ** [ReplicationTaskAssessmentRuns](#API_DescribeReplicationTaskAssessmentRuns_ResponseSyntax) **   <a name="DMS-DescribeReplicationTaskAssessmentRuns-response-ReplicationTaskAssessmentRuns"></a>
One or more premigration assessment runs as specified by `Filters`.
Type: Array of [ReplicationTaskAssessmentRun](API_ReplicationTaskAssessmentRun.md) objects

## Errors
<a name="API_DescribeReplicationTaskAssessmentRuns_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFoundFault **
The resource could not be found.
 ** message **

HTTP Status Code: 400

## Examples
<a name="API_DescribeReplicationTaskAssessmentRuns_Examples"></a>

### Example
<a name="API_DescribeReplicationTaskAssessmentRuns_Example_1"></a>

This example illustrates one usage of DescribeReplicationTaskAssessmentRuns.

#### Sample Request
<a name="API_DescribeReplicationTaskAssessmentRuns_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: dms.<region>.<domain>
x-amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256
Credential=<Credential>,
SignedHeaders=contenttype;date;host;user-
agent;x-amz-date;x-amz-target;x-amzn-
requestid,Signature=<Signature>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: AmazonDMSv20160101.DescribeReplicationTaskAssessmentRuns
{
  "Filters": [
    {
      "Name": "replication-task-arn",
      "Values": [
        "arn:aws:dms:us-west-2:123456789012:task:Z5GKNMVRGGFINESYJIQHG4RLONJGRSRVLCBTECQ"
      ]
    }
  ]
}
```

#### Sample Response
<a name="API_DescribeReplicationTaskAssessmentRuns_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
  "ReplicationTaskAssessmentRuns": [
    {
      "AssessmentProgress": {
        "IndividualAssessmentCompletedCount": 3,
        "IndividualAssessmentCount": 3
      },
      "AssessmentRunName": "Assessment-run-2020-07-07-18-15-03",
      "ReplicationTaskArn": "arn:aws:dms:us-west-2:123456789012:task:Z5GKNMVRGGFINESYJIQHG4RLONJGRSRVLCBTECQ",
      "ReplicationTaskAssessmentRunArn": "arn:aws:dms:us-west-2:123456789012:assessment-run:OGH64BOBSW535SPB5RFJAU7OCYEHXZTWWUGCXZA",
      "ReplicationTaskAssessmentRunCreationDate": 1594170933.203,
      "ResultEncryptionMode": "NONE",
      "ResultLocationBucket": "amzn-s3-demo-bucket",
      "ResultLocationFolder": "myFolder",
      "ServiceAccessRoleArn": "arn:aws:iam::123456789012:role/Admin",
      "Status": "passed"
    }
  ]
}
```

## See Also
<a name="API_DescribeReplicationTaskAssessmentRuns_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dms-2016-01-01/DescribeReplicationTaskAssessmentRuns)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dms-2016-01-01/DescribeReplicationTaskAssessmentRuns)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/DescribeReplicationTaskAssessmentRuns)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dms-2016-01-01/DescribeReplicationTaskAssessmentRuns)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/DescribeReplicationTaskAssessmentRuns)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dms-2016-01-01/DescribeReplicationTaskAssessmentRuns)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dms-2016-01-01/DescribeReplicationTaskAssessmentRuns)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dms-2016-01-01/DescribeReplicationTaskAssessmentRuns)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dms-2016-01-01/DescribeReplicationTaskAssessmentRuns)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/DescribeReplicationTaskAssessmentRuns)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Database Migration Service (DMS) Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
