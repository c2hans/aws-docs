---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_ReloadReplicationTables.html
---

# ReloadReplicationTables
<a name="API_ReloadReplicationTables"></a>

Reloads the target database table with the source data for a given AWS DMS Serverless replication configuration.

You can only use this operation with a task in the RUNNING state, otherwise the service will throw an `InvalidResourceStateFault` exception.

## Request Syntax
<a name="API_ReloadReplicationTables_RequestSyntax"></a>

```
{
   "ReloadOption": "{{string}}",
   "ReplicationConfigArn": "{{string}}",
   "TablesToReload": [
      {
         "SchemaName": "{{string}}",
         "TableName": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_ReloadReplicationTables_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ReloadOption](#API_ReloadReplicationTables_RequestSyntax) **   <a name="DMS-ReloadReplicationTables-request-ReloadOption"></a>
Options for reload. Specify `data-reload` to reload the data and re-validate it if validation is enabled. Specify `validate-only` to re-validate the table. This option applies only when validation is enabled for the replication.
Type: String
Valid Values: `data-reload | validate-only`
Required: No

 ** [ReplicationConfigArn](#API_ReloadReplicationTables_RequestSyntax) **   <a name="DMS-ReloadReplicationTables-request-ReplicationConfigArn"></a>
The Amazon Resource Name of the replication config for which to reload tables.
Type: String
Required: Yes

 ** [TablesToReload](#API_ReloadReplicationTables_RequestSyntax) **   <a name="DMS-ReloadReplicationTables-request-TablesToReload"></a>
The list of tables to reload.
Type: Array of [TableToReload](API_TableToReload.md) objects
Required: Yes

## Response Syntax
<a name="API_ReloadReplicationTables_ResponseSyntax"></a>

```
{
   "ReplicationConfigArn": "string"
}
```

## Response Elements
<a name="API_ReloadReplicationTables_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ReplicationConfigArn](#API_ReloadReplicationTables_ResponseSyntax) **   <a name="DMS-ReloadReplicationTables-response-ReplicationConfigArn"></a>
The Amazon Resource Name of the replication config for which to reload tables.
Type: String

## Errors
<a name="API_ReloadReplicationTables_Errors"></a>

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
<a name="API_ReloadReplicationTables_Examples"></a>

### Example
<a name="API_ReloadReplicationTables_Example_1"></a>

This example illustrates one usage of ReloadReplicationTables.

#### Sample Request
<a name="API_ReloadReplicationTables_Example_1_Request"></a>

```

POST / HTTP/1.1
Host: dms.<region>.<domain>
x-amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>,
 SignedHeaders=contenttype;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid,Signature=<Signature>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: AmazonDMSv20160101.ReloadReplicationTables
{
   "ReplicationConfigArn": "arn:aws:dms:us-east-
1:123456789012:replication-config:WZVIPF3D4AJSNJASB42D4Z7GBE",
   "TablesToReload": [ { "SchemaName": "string", "TableName": "string" } ]
}
```

#### Sample Response
<a name="API_ReloadReplicationTables_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
   "ReplicationConfigArn": "arn:aws:dms:us-east-
1:123456789012:replication-config:WZVIPF3D4AJSNJASB42D4Z7GBE"
}
```

## See Also
<a name="API_ReloadReplicationTables_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dms-2016-01-01/ReloadReplicationTables)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dms-2016-01-01/ReloadReplicationTables)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/ReloadReplicationTables)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dms-2016-01-01/ReloadReplicationTables)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/ReloadReplicationTables)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dms-2016-01-01/ReloadReplicationTables)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dms-2016-01-01/ReloadReplicationTables)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dms-2016-01-01/ReloadReplicationTables)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dms-2016-01-01/ReloadReplicationTables)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/ReloadReplicationTables)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Database Migration Service (DMS) Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
