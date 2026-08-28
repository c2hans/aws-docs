---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeReplicationInstanceTaskLogs.html
---

# DescribeReplicationInstanceTaskLogs
<a name="API_DescribeReplicationInstanceTaskLogs"></a>

Returns information about the task logs for the specified task.

## Request Syntax
<a name="API_DescribeReplicationInstanceTaskLogs_RequestSyntax"></a>

```
{
   "Marker": "{{string}}",
   "MaxRecords": {{number}},
   "ReplicationInstanceArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeReplicationInstanceTaskLogs_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Marker](#API_DescribeReplicationInstanceTaskLogs_RequestSyntax) **   <a name="DMS-DescribeReplicationInstanceTaskLogs-request-Marker"></a>
 An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.
Type: String
Required: No

 ** [MaxRecords](#API_DescribeReplicationInstanceTaskLogs_RequestSyntax) **   <a name="DMS-DescribeReplicationInstanceTaskLogs-request-MaxRecords"></a>
 The maximum number of records to include in the response. If more records exist than the specified `MaxRecords` value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.
Default: 100
Constraints: Minimum 20, maximum 100.
Type: Integer
Required: No

 ** [ReplicationInstanceArn](#API_DescribeReplicationInstanceTaskLogs_RequestSyntax) **   <a name="DMS-DescribeReplicationInstanceTaskLogs-request-ReplicationInstanceArn"></a>
The Amazon Resource Name (ARN) of the replication instance.
Type: String
Required: Yes

## Response Syntax
<a name="API_DescribeReplicationInstanceTaskLogs_ResponseSyntax"></a>

```
{
   "Marker": "string",
   "ReplicationInstanceArn": "string",
   "ReplicationInstanceTaskLogs": [
      {
         "ReplicationInstanceTaskLogSize": number,
         "ReplicationTaskArn": "string",
         "ReplicationTaskName": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeReplicationInstanceTaskLogs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Marker](#API_DescribeReplicationInstanceTaskLogs_ResponseSyntax) **   <a name="DMS-DescribeReplicationInstanceTaskLogs-response-Marker"></a>
 An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.
Type: String

 ** [ReplicationInstanceArn](#API_DescribeReplicationInstanceTaskLogs_ResponseSyntax) **   <a name="DMS-DescribeReplicationInstanceTaskLogs-response-ReplicationInstanceArn"></a>
The Amazon Resource Name (ARN) of the replication instance.
Type: String

 ** [ReplicationInstanceTaskLogs](#API_DescribeReplicationInstanceTaskLogs_ResponseSyntax) **   <a name="DMS-DescribeReplicationInstanceTaskLogs-response-ReplicationInstanceTaskLogs"></a>
An array of replication task log metadata. Each member of the array contains the replication task name, ARN, and task log size (in bytes).
Type: Array of [ReplicationInstanceTaskLog](API_ReplicationInstanceTaskLog.md) objects

## Errors
<a name="API_DescribeReplicationInstanceTaskLogs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidResourceStateFault **
The resource is in a state that prevents it from being used for database migration.
 ** message **

HTTP Status Code: 400

 ** ResourceNotFoundFault **
The resource could not be found.
 ** message **

HTTP Status Code: 400

## Examples
<a name="API_DescribeReplicationInstanceTaskLogs_Examples"></a>

### Example
<a name="API_DescribeReplicationInstanceTaskLogs_Example_1"></a>

This example illustrates one usage of DescribeReplicationInstanceTaskLogs.

#### Sample Request
<a name="API_DescribeReplicationInstanceTaskLogs_Example_1_Request"></a>

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
X-Amz-Target: AmazonDMSv20160101.DescribeReplicationInstanceTaskLogs
{
   "Filters":[
      {
         "Name":"replication-task-arn",
         "Values":[
            "arn:aws:dms:us-east-
1:237565436:task:MY34U6Z4MSY52GRTIX3O4AY"
         ]
      }
   ],
   "MaxRecords":0,
   "Marker":""
}
```

#### Sample Response
<a name="API_DescribeReplicationInstanceTaskLogs_Example_1_Response"></a>

```
 HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
     "ReplicationInstanceTaskLogs": [
         {
             "ReplicationTaskArn": "arn:aws:dms:useast-
              1:237565436:task:MY34U6Z4MSY52GRTIX3O4AY",
             "ReplicationTaskName": "mysql-to-ddb",
             "ReplicationInstanceTaskLogSize": 3726134
         }
      ],
      "ReplicationInstanceArn": "arn:aws:dms:us-east-1:237565436:rep:CDSFSFSFFFSSUFCAY"
}
```

## See Also
<a name="API_DescribeReplicationInstanceTaskLogs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dms-2016-01-01/DescribeReplicationInstanceTaskLogs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dms-2016-01-01/DescribeReplicationInstanceTaskLogs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/DescribeReplicationInstanceTaskLogs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dms-2016-01-01/DescribeReplicationInstanceTaskLogs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/DescribeReplicationInstanceTaskLogs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dms-2016-01-01/DescribeReplicationInstanceTaskLogs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dms-2016-01-01/DescribeReplicationInstanceTaskLogs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dms-2016-01-01/DescribeReplicationInstanceTaskLogs)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dms-2016-01-01/DescribeReplicationInstanceTaskLogs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/DescribeReplicationInstanceTaskLogs)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Database Migration Service (DMS) Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
