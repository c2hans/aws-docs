---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_StartMetadataModelImport.html
---

# StartMetadataModelImport
<a name="API_StartMetadataModelImport"></a>

Queues an import of metadata models (database objects such as tables, views, and procedures) from your data provider into the metadata tree. If other requests created by `Start*` operations are already in the migration project's queue, the import begins after they complete.

To check the status of the import request, call [DescribeMetadataModelImports](https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeMetadataModelImports.html) using the returned `RequestIdentifier` as a filter.

 **Required permissions:** `dms:StartMetadataModelImport`. For more information, see [Actions, resources, and condition keys for AWS Database Migration Service](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdatabasemigrationservice.html).

## Request Syntax
<a name="API_StartMetadataModelImport_RequestSyntax"></a>

```
{
   "MigrationProjectIdentifier": "{{string}}",
   "Origin": "{{string}}",
   "Refresh": {{boolean}},
   "SelectionRules": "{{string}}"
}
```

## Request Parameters
<a name="API_StartMetadataModelImport_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MigrationProjectIdentifier](#API_StartMetadataModelImport_RequestSyntax) **   <a name="DMS-StartMetadataModelImport-request-MigrationProjectIdentifier"></a>
The migration project name or Amazon Resource Name (ARN).
Type: String
Length Constraints: Maximum length of 255.
Required: Yes

 ** [Origin](#API_StartMetadataModelImport_RequestSyntax) **   <a name="DMS-StartMetadataModelImport-request-Origin"></a>
Specifies the metadata tree to import into.
You cannot import from a virtual target data provider.
Type: String
Valid Values: `SOURCE | TARGET`
Required: Yes

 ** [Refresh](#API_StartMetadataModelImport_RequestSyntax) **   <a name="DMS-StartMetadataModelImport-request-Refresh"></a>
Specifies whether to refresh the selected metadata models from the data provider.
When `true`, the import reloads the selected metadata models with current definitions and removes their existing subtree.
When `false` (default), the import loads the full subtree that has not yet been loaded into the metadata tree.
Type: Boolean
Required: No

 ** [SelectionRules](#API_StartMetadataModelImport_RequestSyntax) **   <a name="DMS-StartMetadataModelImport-request-SelectionRules"></a>
A JSON string that identifies the metadata models to import from the data provider. For the selection rule format and examples, see [Selection rules in DMS Schema Conversion](https://docs.aws.amazon.com/dms/latest/userguide/sc-selection-rules.html).
Usage:
+ Accepts source or target selection rules depending on the `Origin` parameter. The `server-name` in the object locator must match the corresponding data provider.
+ Supports `explicit`, `include`, and `exclude` rule actions.
Type: String
Required: Yes

## Response Syntax
<a name="API_StartMetadataModelImport_ResponseSyntax"></a>

```
{
   "RequestIdentifier": "string"
}
```

## Response Elements
<a name="API_StartMetadataModelImport_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [RequestIdentifier](#API_StartMetadataModelImport_ResponseSyntax) **   <a name="DMS-StartMetadataModelImport-response-RequestIdentifier"></a>
The identifier for the import request.
Type: String

## Errors
<a name="API_StartMetadataModelImport_Errors"></a>

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
<a name="API_StartMetadataModelImport_Examples"></a>

### Import metadata from the source database
<a name="API_StartMetadataModelImport_Example_1"></a>

The following example queues a metadata import for all objects in the `ExampleSchema` schema from the source database.

#### Sample Request
<a name="API_StartMetadataModelImport_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: dms.<region>.<domain>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<SignedHeaders>, Signature=<Signature>
X-Amz-Date: <Date>
X-Amz-Target: AmazonDMSv20160101.StartMetadataModelImport
{
    "MigrationProjectIdentifier": "arn:aws:dms:us-east-1:111122223333:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS",
    "SelectionRules": "{\"rules\": [{\"rule-type\": \"selection\",\"rule-id\": \"1\",\"rule-name\": \"1\",\"object-locator\": {\"server-name\": \"example-source-server.us-east-1.rds.amazonaws.com\", \"schema-name\": \"ExampleSchema\"},\"rule-action\": \"explicit\"}]}",
    "Origin": "SOURCE",
    "Refresh": false
}
```

#### Sample Response
<a name="API_StartMetadataModelImport_Example_1_Response"></a>

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
<a name="API_StartMetadataModelImport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dms-2016-01-01/StartMetadataModelImport)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dms-2016-01-01/StartMetadataModelImport)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/StartMetadataModelImport)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dms-2016-01-01/StartMetadataModelImport)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/StartMetadataModelImport)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dms-2016-01-01/StartMetadataModelImport)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dms-2016-01-01/StartMetadataModelImport)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dms-2016-01-01/StartMetadataModelImport)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dms-2016-01-01/StartMetadataModelImport)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/StartMetadataModelImport)
