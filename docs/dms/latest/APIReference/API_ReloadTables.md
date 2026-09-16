---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_ReloadTables.html
---

# ReloadTables
<a name="API_ReloadTables"></a>

Reloads the target database table with the source data.

You can only use this operation with a task in the `RUNNING` state, otherwise the service will throw an `InvalidResourceStateFault` exception.

## Request Syntax
<a name="API_ReloadTables_RequestSyntax"></a>

```
{
   "ReloadOption": "{{string}}",
   "ReplicationTaskArn": "{{string}}",
   "TablesToReload": [
      {
         "SchemaName": "{{string}}",
         "TableName": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_ReloadTables_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ReloadOption](#API_ReloadTables_RequestSyntax) **   <a name="DMS-ReloadTables-request-ReloadOption"></a>
Options for reload. Specify `data-reload` to reload the data and re-validate it if validation is enabled. Specify `validate-only` to re-validate the table. This option applies only when validation is enabled for the task.
Valid values: data-reload, validate-only
Default value is data-reload.
Type: String
Valid Values: `data-reload | validate-only`
Required: No

 ** [ReplicationTaskArn](#API_ReloadTables_RequestSyntax) **   <a name="DMS-ReloadTables-request-ReplicationTaskArn"></a>
The Amazon Resource Name (ARN) of the replication task.
Type: String
Required: Yes

 ** [TablesToReload](#API_ReloadTables_RequestSyntax) **   <a name="DMS-ReloadTables-request-TablesToReload"></a>
The name and schema of the table to be reloaded.
Type: Array of [TableToReload](API_TableToReload.md) objects
Required: Yes

## Response Syntax
<a name="API_ReloadTables_ResponseSyntax"></a>

```
{
   "ReplicationTaskArn": "string"
}
```

## Response Elements
<a name="API_ReloadTables_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ReplicationTaskArn](#API_ReloadTables_ResponseSyntax) **   <a name="DMS-ReloadTables-response-ReplicationTaskArn"></a>
The Amazon Resource Name (ARN) of the replication task.
Type: String

## Errors
<a name="API_ReloadTables_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidResourceStateFault **
The resource is in a state that prevents it from being used for database migration.
 ** message **

HTTP Status Code: 400

 ** ResourceNotFoundFault **
The resource could not be found.
 ** message **

HTTP Status Code: 400

## See Also
<a name="API_ReloadTables_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dms-2016-01-01/ReloadTables)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dms-2016-01-01/ReloadTables)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/ReloadTables)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dms-2016-01-01/ReloadTables)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/ReloadTables)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dms-2016-01-01/ReloadTables)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dms-2016-01-01/ReloadTables)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dms-2016-01-01/ReloadTables)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/dms-2016-01-01/ReloadTables)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/ReloadTables)
