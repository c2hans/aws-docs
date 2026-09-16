---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_StartMetadataModelExportToTarget.html
---

# StartMetadataModelExportToTarget
<a name="API_StartMetadataModelExportToTarget"></a>

Queues an export of the selected converted metadata models (database objects such as tables, views, and procedures) to your target database. If other requests created by `Start*` operations are already in the migration project's queue, the export begins after they complete.

This operation requires a non-virtual target data provider.

The export applies only metadata models created by conversion. Metadata models imported from the database are skipped.

**Note**
If objects with the same name already exist on the target database, the export overwrites them.

The operation installs the extension pack on the target database. For more information, see [Using extension packs in DMS Schema Conversion](https://docs.aws.amazon.com/dms/latest/userguide/extension-pack.html).

To check the status of the export request, call [DescribeMetadataModelExportsToTarget](https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeMetadataModelExportsToTarget.html) using the returned `RequestIdentifier` as a filter.

 **Required permissions:** `dms:StartMetadataModelExportToTarget`. For more information, see [Actions, resources, and condition keys for AWS Database Migration Service](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdatabasemigrationservice.html).

## Request Syntax
<a name="API_StartMetadataModelExportToTarget_RequestSyntax"></a>

```
{
   "MigrationProjectIdentifier": "{{string}}",
   "OverwriteExtensionPack": {{boolean}},
   "SelectionRules": "{{string}}"
}
```

## Request Parameters
<a name="API_StartMetadataModelExportToTarget_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MigrationProjectIdentifier](#API_StartMetadataModelExportToTarget_RequestSyntax) **   <a name="DMS-StartMetadataModelExportToTarget-request-MigrationProjectIdentifier"></a>
The migration project name or Amazon Resource Name (ARN).
Type: String
Length Constraints: Maximum length of 255.
Required: Yes

 ** [OverwriteExtensionPack](#API_StartMetadataModelExportToTarget_RequestSyntax) **   <a name="DMS-StartMetadataModelExportToTarget-request-OverwriteExtensionPack"></a>
Specifies whether to overwrite the extension pack if one already exists on the target database. The default value is `true`.
Type: Boolean
Required: No

 ** [SelectionRules](#API_StartMetadataModelExportToTarget_RequestSyntax) **   <a name="DMS-StartMetadataModelExportToTarget-request-SelectionRules"></a>
A JSON string that identifies the metadata models to export to the target database. For the selection rule format and examples, see [Selection rules in DMS Schema Conversion](https://docs.aws.amazon.com/dms/latest/userguide/sc-selection-rules.html).
Usage:
+ Accepts only target selection rules, where `server-name` in the object locator matches the target data provider.
+ Supports `explicit`, `include`, and `exclude` rule actions.
Type: String
Required: Yes

## Response Syntax
<a name="API_StartMetadataModelExportToTarget_ResponseSyntax"></a>

```
{
   "RequestIdentifier": "string"
}
```

## Response Elements
<a name="API_StartMetadataModelExportToTarget_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [RequestIdentifier](#API_StartMetadataModelExportToTarget_ResponseSyntax) **   <a name="DMS-StartMetadataModelExportToTarget-response-RequestIdentifier"></a>
The identifier for the export request.
Type: String

## Errors
<a name="API_StartMetadataModelExportToTarget_Errors"></a>

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
<a name="API_StartMetadataModelExportToTarget_Examples"></a>

### Export converted metadata models to the target database
<a name="API_StartMetadataModelExportToTarget_Example_1"></a>

The following example queues an export of converted metadata models for all objects in the `ExampleSchema` schema to the target database.

#### Sample Request
<a name="API_StartMetadataModelExportToTarget_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: dms.<region>.<domain>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<SignedHeaders>, Signature=<Signature>
X-Amz-Date: <Date>
X-Amz-Target: AmazonDMSv20160101.StartMetadataModelExportToTarget
{
    "MigrationProjectIdentifier": "arn:aws:dms:us-east-1:111122223333:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS",
    "SelectionRules": "{\"rules\": [{\"rule-type\": \"selection\",\"rule-id\": \"1\",\"rule-name\": \"1\",\"object-locator\": {\"server-name\": \"example-target-server.us-east-1.rds.amazonaws.com\", \"schema-name\": \"ExampleSchema\"},\"rule-action\": \"explicit\"}]}",
    "OverwriteExtensionPack": true
}
```

#### Sample Response
<a name="API_StartMetadataModelExportToTarget_Example_1_Response"></a>

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
<a name="API_StartMetadataModelExportToTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dms-2016-01-01/StartMetadataModelExportToTarget)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dms-2016-01-01/StartMetadataModelExportToTarget)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/StartMetadataModelExportToTarget)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dms-2016-01-01/StartMetadataModelExportToTarget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/StartMetadataModelExportToTarget)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dms-2016-01-01/StartMetadataModelExportToTarget)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dms-2016-01-01/StartMetadataModelExportToTarget)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dms-2016-01-01/StartMetadataModelExportToTarget)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/dms-2016-01-01/StartMetadataModelExportToTarget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/StartMetadataModelExportToTarget)
