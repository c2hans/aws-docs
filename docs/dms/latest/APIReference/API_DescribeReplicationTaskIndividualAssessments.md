---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeReplicationTaskIndividualAssessments.html
---

# DescribeReplicationTaskIndividualAssessments
<a name="API_DescribeReplicationTaskIndividualAssessments"></a>

Returns a paginated list of individual assessments based on filter settings.

These filter settings can specify a combination of premigration assessment runs, migration tasks, and assessment status values.

## Request Syntax
<a name="API_DescribeReplicationTaskIndividualAssessments_RequestSyntax"></a>

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
<a name="API_DescribeReplicationTaskIndividualAssessments_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_DescribeReplicationTaskIndividualAssessments_RequestSyntax) **   <a name="DMS-DescribeReplicationTaskIndividualAssessments-request-Filters"></a>
Filters applied to the individual assessments described in the form of key-value pairs.
Valid filter names: `replication-task-assessment-run-arn`, `replication-task-arn`, `status`
Type: Array of [Filter](API_Filter.md) objects
Required: No

 ** [Marker](#API_DescribeReplicationTaskIndividualAssessments_RequestSyntax) **   <a name="DMS-DescribeReplicationTaskIndividualAssessments-request-Marker"></a>
An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.
Type: String
Required: No

 ** [MaxRecords](#API_DescribeReplicationTaskIndividualAssessments_RequestSyntax) **   <a name="DMS-DescribeReplicationTaskIndividualAssessments-request-MaxRecords"></a>
The maximum number of records to include in the response. If more records exist than the specified `MaxRecords` value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.
Type: Integer
Required: No

## Response Syntax
<a name="API_DescribeReplicationTaskIndividualAssessments_ResponseSyntax"></a>

```
{
   "Marker": "string",
   "ReplicationTaskIndividualAssessments": [
      {
         "IndividualAssessmentName": "string",
         "ReplicationTaskAssessmentRunArn": "string",
         "ReplicationTaskIndividualAssessmentArn": "string",
         "ReplicationTaskIndividualAssessmentStartDate": number,
         "Status": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeReplicationTaskIndividualAssessments_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Marker](#API_DescribeReplicationTaskIndividualAssessments_ResponseSyntax) **   <a name="DMS-DescribeReplicationTaskIndividualAssessments-response-Marker"></a>
A pagination token returned for you to pass to a subsequent request. If you pass this token as the `Marker` value in a subsequent request, the response includes only records beyond the marker, up to the value specified in the request by `MaxRecords`.
Type: String

 ** [ReplicationTaskIndividualAssessments](#API_DescribeReplicationTaskIndividualAssessments_ResponseSyntax) **   <a name="DMS-DescribeReplicationTaskIndividualAssessments-response-ReplicationTaskIndividualAssessments"></a>
One or more individual assessments as specified by `Filters`.
Type: Array of [ReplicationTaskIndividualAssessment](API_ReplicationTaskIndividualAssessment.md) objects

## Errors
<a name="API_DescribeReplicationTaskIndividualAssessments_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFoundFault **
The resource could not be found.
 ** message **

HTTP Status Code: 400

## Examples
<a name="API_DescribeReplicationTaskIndividualAssessments_Examples"></a>

### Example
<a name="API_DescribeReplicationTaskIndividualAssessments_Example_1"></a>

This example illustrates one usage of DescribeReplicationTaskIndividualAssessments.

#### Sample Request
<a name="API_DescribeReplicationTaskIndividualAssessments_Example_1_Request"></a>

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
X-Amz-Target: AmazonDMSv20160101.DescribeReplicationTaskIndividualAssessments
{
  "Filters": [
    {
      "Name": "replication-task-assessment-run-arn",
      "Values": [
        "arn:aws:dms:us-west-2:123456789012:assessment-run:TSUXVACQ2UUMXUS5OYQOGXB6FXSAZ4LE3FXRNII",
        "arn:aws:dms:us-west-2:123456789012:assessment-run:ZQ3KWJEUM7SW2Q2BH5BFMPS525KH56C3G5DHMTQ",
        "arn:aws:dms:us-west-2:123456789012:assessment-run:3GOFKWZXGIT7ZWBBZOXDDBUS4VPAV63PPOQGFHQ"
      ]
    }
  ]
}
```

#### Sample Response
<a name="API_DescribeReplicationTaskIndividualAssessments_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
  "ReplicationTaskIndividualAssessments": [
    {
      "IndividualAssessmentName": "unsupported-data-types-in-source",
      "ReplicationTaskAssessmentRunArn": "arn:aws:dms:us-west-2:123456789012:assessment-run:3GOFKWZXGIT7ZWBBZOXDDBUS4VPAV63PPOQGFHQ",
      "ReplicationTaskIndividualAssessmentArn": "arn:aws:dms:us-west-2:123456789012:individual-assessment:TSUXVACQ2UUMXUS5OYQOGXB6FXSAZ4LE3FXRNII",
      "ReplicationTaskIndividualAssessmentStartDate": 1594066482.995,
      "Status": "passed"
    },
    {
      "IndividualAssessmentName": "full-lob-not-nullable-at-target",
      "ReplicationTaskAssessmentRunArn": "arn:aws:dms:us-west-2:123456789012:assessment-run:3GOFKWZXGIT7ZWBBZOXDDBUS4VPAV63PPOQGFHQ",
      "ReplicationTaskIndividualAssessmentArn": "arn:aws:dms:us-west-2:123456789012:individual-assessment:ZQ3KWJEUM7SW2Q2BH5BFMPS525KH56C3G5DHMTQ",
      "ReplicationTaskIndividualAssessmentStartDate": 1594066482.989,
      "Status": "passed"
    },
    {
      "IndividualAssessmentName": "table-with-no-primary-key-or-unique-constraint",
      "ReplicationTaskAssessmentRunArn": "arn:aws:dms:us-west-2:123456789012:assessment-run:3GOFKWZXGIT7ZWBBZOXDDBUS4VPAV63PPOQGFHQ",
      "ReplicationTaskIndividualAssessmentArn": "arn:aws:dms:us-west-2:123456789012:individual-assessment:3GOFKWZXGIT7ZWBBZOXDDBUS4VPAV63PPOQGFHQ",
      "ReplicationTaskIndividualAssessmentStartDate": 1594066591.595,
      "Status": "passed"
    }
  ]
}
```

## See Also
<a name="API_DescribeReplicationTaskIndividualAssessments_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dms-2016-01-01/DescribeReplicationTaskIndividualAssessments)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dms-2016-01-01/DescribeReplicationTaskIndividualAssessments)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/DescribeReplicationTaskIndividualAssessments)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dms-2016-01-01/DescribeReplicationTaskIndividualAssessments)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/DescribeReplicationTaskIndividualAssessments)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dms-2016-01-01/DescribeReplicationTaskIndividualAssessments)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dms-2016-01-01/DescribeReplicationTaskIndividualAssessments)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dms-2016-01-01/DescribeReplicationTaskIndividualAssessments)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dms-2016-01-01/DescribeReplicationTaskIndividualAssessments)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/DescribeReplicationTaskIndividualAssessments)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Database Migration Service (DMS) Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
