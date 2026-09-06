---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_StartMetadataModelExportAsScript.html
---

# StartMetadataModelExportAsScript
<a name="API_StartMetadataModelExportAsScript"></a>

Queues an export of metadata models (database objects such as tables, views, and procedures) as a data definition language (DDL) script. The script is stored as a ZIP archive in the Amazon S3 bucket associated with the migration project. If other requests created by `Start*` operations are already in the migration project's queue, the export begins after they complete.

When exporting from the target metadata tree, the export applies only to metadata models created by conversion. Metadata models imported from the database are skipped.

To check the status of the export request, call [DescribeMetadataModelExportsAsScript](https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeMetadataModelExportsAsScript.html) using the returned `RequestIdentifier` as a filter.

 **Required permissions:** `dms:StartMetadataModelExportAsScripts`. For more information, see [Actions, resources, and condition keys for AWS Database Migration Service](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdatabasemigrationservice.html).

## Request Syntax
<a name="API_StartMetadataModelExportAsScript_RequestSyntax"></a>

```
{
   "FileName": "{{string}}",
   "MigrationProjectIdentifier": "{{string}}",
   "Origin": "{{string}}",
   "SelectionRules": "{{string}}"
}
```

## Request Parameters
<a name="API_StartMetadataModelExportAsScript_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [FileName](#API_StartMetadataModelExportAsScript_RequestSyntax) **   <a name="DMS-StartMetadataModelExportAsScript-request-FileName"></a>
The name for the exported file. When you omit this parameter, the service generates a name from the data provider engine name and an export timestamp.
Type: String
Required: No

 ** [MigrationProjectIdentifier](#API_StartMetadataModelExportAsScript_RequestSyntax) **   <a name="DMS-StartMetadataModelExportAsScript-request-MigrationProjectIdentifier"></a>
The migration project name or Amazon Resource Name (ARN).
Type: String
Length Constraints: Maximum length of 255.
Required: Yes

 ** [Origin](#API_StartMetadataModelExportAsScript_RequestSyntax) **   <a name="DMS-StartMetadataModelExportAsScript-request-Origin"></a>
Specifies the metadata tree to export from.
Type: String
Valid Values: `SOURCE | TARGET`
Required: Yes

 ** [SelectionRules](#API_StartMetadataModelExportAsScript_RequestSyntax) **   <a name="DMS-StartMetadataModelExportAsScript-request-SelectionRules"></a>
A JSON string that identifies the metadata models to export as a SQL script. For the selection rule format and examples, see [Selection rules in DMS Schema Conversion](https://docs.aws.amazon.com/dms/latest/userguide/sc-selection-rules.html).
Usage:
+ Accepts source or target selection rules depending on the `Origin` parameter. The `server-name` in the object locator must match the corresponding data provider.
+ Supports `explicit`, `include`, and `exclude` rule actions.
Type: String
Required: Yes

## Response Syntax
<a name="API_StartMetadataModelExportAsScript_ResponseSyntax"></a>

```
{
   "RequestIdentifier": "string"
}
```

## Response Elements
<a name="API_StartMetadataModelExportAsScript_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [RequestIdentifier](#API_StartMetadataModelExportAsScript_ResponseSyntax) **   <a name="DMS-StartMetadataModelExportAsScript-response-RequestIdentifier"></a>
The identifier for the export request.
Type: String

## Errors
<a name="API_StartMetadataModelExportAsScript_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedFault **
 AWS DMS was denied access to the endpoint. Check that the role is correctly configured.
 ** message **

HTTP Status Code: 400

 ** InvalidResourceStateFault **
The resource is in a state that prevents it from being used for database migration.
 ** message **

HTTP Status Code: 400

 ** KMSKeyNotAccessibleFault **
 AWS DMS cannot access the KMS key.
 ** message **

HTTP Status Code: 400

 ** ResourceAlreadyExistsFault **
The resource you are attempting to create already exists.
 ** message **

 ** resourceArn **

HTTP Status Code: 400

 ** ResourceNotFoundFault **
The resource could not be found.
 ** message **

HTTP Status Code: 400

 ** ResourceQuotaExceededFault **
The quota for this resource quota has been exceeded.
 ** message **

HTTP Status Code: 400

 ** S3AccessDeniedFault **
Insufficient privileges are preventing access to an Amazon S3 object.
HTTP Status Code: 400

 ** S3ResourceNotFoundFault **
A specified Amazon S3 bucket, bucket folder, or other object can't be found.
HTTP Status Code: 400

## Examples
<a name="API_StartMetadataModelExportAsScript_Examples"></a>

### Export converted metadata models as DDL scripts
<a name="API_StartMetadataModelExportAsScript_Example_1"></a>

The following example queues an export of converted metadata models for all objects in the `ExampleSchema` schema as data definition language (DDL) scripts to the Amazon S3 bucket associated with the migration project.

#### Sample Request
<a name="API_StartMetadataModelExportAsScript_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: dms.<region>.<domain>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<SignedHeaders>, Signature=<Signature>
X-Amz-Date: <Date>
X-Amz-Target: AmazonDMSv20160101.StartMetadataModelExportAsScript
{
    "MigrationProjectIdentifier": "arn:aws:dms:us-east-1:111122223333:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS",
    "SelectionRules": "{\"rules\": [{\"rule-type\": \"selection\",\"rule-id\": \"1\",\"rule-name\": \"1\",\"object-locator\": {\"server-name\": \"example-target-server.us-east-1.rds.amazonaws.com\", \"schema-name\": \"ExampleSchema\"},\"rule-action\": \"explicit\"}]}",
    "Origin": "TARGET",
    "FileName": "ExampleScript"
}
```

#### Sample Response
<a name="API_StartMetadataModelExportAsScript_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
    "RequestIdentifier": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
}
```

## See Also
<a name="API_StartMetadataModelExportAsScript_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dms-2016-01-01/StartMetadataModelExportAsScript)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dms-2016-01-01/StartMetadataModelExportAsScript)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/StartMetadataModelExportAsScript)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dms-2016-01-01/StartMetadataModelExportAsScript)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/StartMetadataModelExportAsScript)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dms-2016-01-01/StartMetadataModelExportAsScript)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dms-2016-01-01/StartMetadataModelExportAsScript)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dms-2016-01-01/StartMetadataModelExportAsScript)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dms-2016-01-01/StartMetadataModelExportAsScript)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/StartMetadataModelExportAsScript)
