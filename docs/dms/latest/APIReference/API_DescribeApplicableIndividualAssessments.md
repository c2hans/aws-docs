---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeApplicableIndividualAssessments.html
---

# DescribeApplicableIndividualAssessments
<a name="API_DescribeApplicableIndividualAssessments"></a>

Provides a list of individual assessments that you can specify for a new premigration assessment run, given one or more parameters.

If you specify an existing migration task, this operation provides the default individual assessments you can specify for that task. Otherwise, the specified parameters model elements of a possible migration task on which to base a premigration assessment run.

To use these migration task modeling parameters, you must specify an existing replication instance, a source database engine, a target database engine, and a migration type. This combination of parameters potentially limits the default individual assessments available for an assessment run created for a corresponding migration task.

If you specify no parameters, this operation provides a list of all possible individual assessments that you can specify for an assessment run. If you specify any one of the task modeling parameters, you must specify all of them or the operation cannot provide a list of individual assessments. The only parameter that you can specify alone is for an existing migration task. The specified task definition then determines the default list of individual assessments that you can specify in an assessment run for the task.

## Request Syntax
<a name="API_DescribeApplicableIndividualAssessments_RequestSyntax"></a>

```
{
   "Marker": "{{string}}",
   "MaxRecords": {{number}},
   "MigrationType": "{{string}}",
   "ReplicationConfigArn": "{{string}}",
   "ReplicationInstanceArn": "{{string}}",
   "ReplicationTaskArn": "{{string}}",
   "SourceEngineName": "{{string}}",
   "TargetEngineName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeApplicableIndividualAssessments_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Marker](#API_DescribeApplicableIndividualAssessments_RequestSyntax) **   <a name="DMS-DescribeApplicableIndividualAssessments-request-Marker"></a>
Optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.
Type: String
Required: No

 ** [MaxRecords](#API_DescribeApplicableIndividualAssessments_RequestSyntax) **   <a name="DMS-DescribeApplicableIndividualAssessments-request-MaxRecords"></a>
Maximum number of records to include in the response. If more records exist than the specified `MaxRecords` value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.
Type: Integer
Required: No

 ** [MigrationType](#API_DescribeApplicableIndividualAssessments_RequestSyntax) **   <a name="DMS-DescribeApplicableIndividualAssessments-request-MigrationType"></a>
Name of the migration type that each provided individual assessment must support.
Type: String
Valid Values: `full-load | cdc | full-load-and-cdc`
Required: No

 ** [ReplicationConfigArn](#API_DescribeApplicableIndividualAssessments_RequestSyntax) **   <a name="DMS-DescribeApplicableIndividualAssessments-request-ReplicationConfigArn"></a>
Amazon Resource Name (ARN) of a serverless replication on which you want to base the default list of individual assessments.
Type: String
Required: No

 ** [ReplicationInstanceArn](#API_DescribeApplicableIndividualAssessments_RequestSyntax) **   <a name="DMS-DescribeApplicableIndividualAssessments-request-ReplicationInstanceArn"></a>
ARN of a replication instance on which you want to base the default list of individual assessments.
Type: String
Required: No

 ** [ReplicationTaskArn](#API_DescribeApplicableIndividualAssessments_RequestSyntax) **   <a name="DMS-DescribeApplicableIndividualAssessments-request-ReplicationTaskArn"></a>
Amazon Resource Name (ARN) of a migration task on which you want to base the default list of individual assessments.
Type: String
Required: No

 ** [SourceEngineName](#API_DescribeApplicableIndividualAssessments_RequestSyntax) **   <a name="DMS-DescribeApplicableIndividualAssessments-request-SourceEngineName"></a>
Name of a database engine that the specified replication instance supports as a source.
Type: String
Required: No

 ** [TargetEngineName](#API_DescribeApplicableIndividualAssessments_RequestSyntax) **   <a name="DMS-DescribeApplicableIndividualAssessments-request-TargetEngineName"></a>
Name of a database engine that the specified replication instance supports as a target.
Type: String
Required: No

## Response Syntax
<a name="API_DescribeApplicableIndividualAssessments_ResponseSyntax"></a>

```
{
   "IndividualAssessmentNames": [ "string" ],
   "Marker": "string"
}
```

## Response Elements
<a name="API_DescribeApplicableIndividualAssessments_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [IndividualAssessmentNames](#API_DescribeApplicableIndividualAssessments_ResponseSyntax) **   <a name="DMS-DescribeApplicableIndividualAssessments-response-IndividualAssessmentNames"></a>
List of names for the individual assessments supported by the premigration assessment run that you start based on the specified request parameters. For more information on the available individual assessments, including compatibility with different migration task configurations, see [Working with premigration assessment runs](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.AssessmentReport.html) in the * AWS Database Migration Service User Guide.*
Type: Array of strings

 ** [Marker](#API_DescribeApplicableIndividualAssessments_ResponseSyntax) **   <a name="DMS-DescribeApplicableIndividualAssessments-response-Marker"></a>
Pagination token returned for you to pass to a subsequent request. If you pass this token as the `Marker` value in a subsequent request, the response includes only records beyond the marker, up to the value specified in the request by `MaxRecords`.
Type: String

## Errors
<a name="API_DescribeApplicableIndividualAssessments_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedFault **
 AWS DMS was denied access to the endpoint. Check that the role is correctly configured.
 ** message **

HTTP Status Code: 400

 ** InvalidResourceStateFault **
The resource is in a state that prevents it from being used for database migration.
 ** message **

HTTP Status Code: 400

 ** ResourceNotFoundFault **
The resource could not be found.
 ** message **

HTTP Status Code: 400

## Examples
<a name="API_DescribeApplicableIndividualAssessments_Examples"></a>

### Example
<a name="API_DescribeApplicableIndividualAssessments_Example_1"></a>

This example illustrates one usage of DescribeApplicableIndividualAssessments.

#### Sample Request
<a name="API_DescribeApplicableIndividualAssessments_Example_1_Request"></a>

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
X-Amz-Target: AmazonDMSv20160101.DescribeApplicableIndividualAssessments
{
  "SourceEngineName": "oracle",
  "TargetEngineName": "postgres",
  "MigrationType": "full-load",
  "ReplicationInstanceArn": "arn:aws:dms:us-east-1:123456789023:rep:LPIXGJNGKAMDWSAESJNDNECHHZMKBS5OG3H5RVB"
}
```

#### Sample Response
<a name="API_DescribeApplicableIndividualAssessments_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
  "IndividualAssessmentNames": [
    "full-lob-not-nullable-at-target",
    "table-with-lob-but-without-primary-key-or-unique-constraint",
    "unsupported-data-types-in-source"
  ]
}
```

## See Also
<a name="API_DescribeApplicableIndividualAssessments_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dms-2016-01-01/DescribeApplicableIndividualAssessments)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dms-2016-01-01/DescribeApplicableIndividualAssessments)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/DescribeApplicableIndividualAssessments)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dms-2016-01-01/DescribeApplicableIndividualAssessments)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/DescribeApplicableIndividualAssessments)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dms-2016-01-01/DescribeApplicableIndividualAssessments)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dms-2016-01-01/DescribeApplicableIndividualAssessments)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dms-2016-01-01/DescribeApplicableIndividualAssessments)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dms-2016-01-01/DescribeApplicableIndividualAssessments)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/DescribeApplicableIndividualAssessments)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Database Migration Service (DMS) Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
