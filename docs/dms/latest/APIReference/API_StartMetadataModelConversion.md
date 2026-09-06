---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_StartMetadataModelConversion.html
---

# StartMetadataModelConversion
<a name="API_StartMetadataModelConversion"></a>

Queues a conversion of the selected source metadata models (database objects such as tables, views, and procedures) to the target database format. If other requests created by `Start*` operations are already in the migration project's queue, the conversion begins after they complete.

The conversion request loads metadata models that are not yet in the metadata tree, but does not reload metadata models that are already present. If your source database has changed since the metadata was loaded, refresh the affected metadata models with [StartMetadataModelImport](https://docs.aws.amazon.com/dms/latest/APIReference/API_StartMetadataModelImport.html) before calling this operation.

**Note**
If converted objects already exist in the target metadata tree, the conversion overwrites them, including any manual edits.

To check the status of the conversion request, call [DescribeMetadataModelConversions](https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeMetadataModelConversions.html) using the returned `RequestIdentifier` as a filter.

To cancel a queued or in-progress request, call [CancelMetadataModelConversion](https://docs.aws.amazon.com/dms/latest/APIReference/API_CancelMetadataModelConversion.html) with the returned `RequestIdentifier`.

After the conversion completes successfully:
+ To export a post-conversion assessment report, call [ExportMetadataModelAssessment](https://docs.aws.amazon.com/dms/latest/APIReference/API_ExportMetadataModelAssessment.html).
+ To retrieve converted code, use any of the following options:
  +  [DescribeMetadataModel](https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeMetadataModel.html) and [DescribeMetadataModelChildren](https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeMetadataModelChildren.html) – navigate the target metadata tree and retrieve converted definitions.
  +  [StartMetadataModelExportAsScript](https://docs.aws.amazon.com/dms/latest/APIReference/API_StartMetadataModelExportAsScript.html) – export as data definition language (DDL) scripts to your Amazon S3 bucket.
  +  [StartMetadataModelExportToTarget](https://docs.aws.amazon.com/dms/latest/APIReference/API_StartMetadataModelExportToTarget.html) – apply directly to your target database.

 **Required permissions:** `dms:StartMetadataModelConversion`. For more information, see [Actions, resources, and condition keys for AWS Database Migration Service](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdatabasemigrationservice.html).

## Request Syntax
<a name="API_StartMetadataModelConversion_RequestSyntax"></a>

```
{
   "MigrationProjectIdentifier": "{{string}}",
   "SelectionRules": "{{string}}"
}
```

## Request Parameters
<a name="API_StartMetadataModelConversion_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MigrationProjectIdentifier](#API_StartMetadataModelConversion_RequestSyntax) **   <a name="DMS-StartMetadataModelConversion-request-MigrationProjectIdentifier"></a>
The migration project name or Amazon Resource Name (ARN).
Type: String
Length Constraints: Maximum length of 255.
Required: Yes

 ** [SelectionRules](#API_StartMetadataModelConversion_RequestSyntax) **   <a name="DMS-StartMetadataModelConversion-request-SelectionRules"></a>
A JSON string that identifies the metadata models to convert. For the selection rule format and examples, see [Selection rules in DMS Schema Conversion](https://docs.aws.amazon.com/dms/latest/userguide/sc-selection-rules.html).
Usage:
+ Accepts only source selection rules, where `server-name` in the object locator matches the source data provider.
+ Supports `explicit`, `include`, and `exclude` rule actions.
Type: String
Required: Yes

## Response Syntax
<a name="API_StartMetadataModelConversion_ResponseSyntax"></a>

```
{
   "RequestIdentifier": "string"
}
```

## Response Elements
<a name="API_StartMetadataModelConversion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [RequestIdentifier](#API_StartMetadataModelConversion_ResponseSyntax) **   <a name="DMS-StartMetadataModelConversion-response-RequestIdentifier"></a>
The identifier for the conversion request.
Type: String

## Errors
<a name="API_StartMetadataModelConversion_Errors"></a>

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
<a name="API_StartMetadataModelConversion_Examples"></a>

### Convert all objects in a schema
<a name="API_StartMetadataModelConversion_Example_1"></a>

The following example queues a conversion of all objects in the `ExampleSchema` schema to the target database format.

#### Sample Request
<a name="API_StartMetadataModelConversion_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: dms.<region>.<domain>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<SignedHeaders>, Signature=<Signature>
X-Amz-Date: <Date>
X-Amz-Target: AmazonDMSv20160101.StartMetadataModelConversion
{
    "MigrationProjectIdentifier": "arn:aws:dms:us-east-1:111122223333:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS",
    "SelectionRules": "{\"rules\": [{\"rule-type\": \"selection\",\"rule-id\": \"1\",\"rule-name\": \"1\",\"object-locator\": {\"server-name\": \"example-source-server.us-east-1.rds.amazonaws.com\", \"schema-name\": \"ExampleSchema\"},\"rule-action\": \"explicit\"}]}"
}
```

#### Sample Response
<a name="API_StartMetadataModelConversion_Example_1_Response"></a>

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
<a name="API_StartMetadataModelConversion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dms-2016-01-01/StartMetadataModelConversion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dms-2016-01-01/StartMetadataModelConversion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/StartMetadataModelConversion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dms-2016-01-01/StartMetadataModelConversion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/StartMetadataModelConversion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dms-2016-01-01/StartMetadataModelConversion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dms-2016-01-01/StartMetadataModelConversion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dms-2016-01-01/StartMetadataModelConversion)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dms-2016-01-01/StartMetadataModelConversion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/StartMetadataModelConversion)
