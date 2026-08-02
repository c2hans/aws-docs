---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_StartMetadataModelAssessment.html
---

# StartMetadataModelAssessment
<a name="API_StartMetadataModelAssessment"></a>

Queues an assessment of the selected source metadata models (database objects such as tables, views, and procedures) to evaluate conversion complexity to the target database format. If other requests created by `Start*` operations are already in the migration project's queue, the assessment begins after they complete.

The assessment request loads metadata models that are not yet in the metadata tree, but does not reload metadata models that are already present. If your source database has changed since the metadata was loaded, refresh the affected metadata models with [StartMetadataModelImport](https://docs.aws.amazon.com/dms/latest/APIReference/API_StartMetadataModelImport.html) before calling this operation.

To check the status of the assessment request, call [DescribeMetadataModelAssessments](https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeMetadataModelAssessments.html) using the returned `RequestIdentifier` as a filter.

To export the conversion assessment report after the request completes successfully, call [ExportMetadataModelAssessment](https://docs.aws.amazon.com/dms/latest/APIReference/API_ExportMetadataModelAssessment.html).

 **Required permissions:** `dms:StartMetadataModelAssessment`. For more information, see [Actions, resources, and condition keys for AWS Database Migration Service](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdatabasemigrationservice.html).

## Request Syntax
<a name="API_StartMetadataModelAssessment_RequestSyntax"></a>

```
{
   "MigrationProjectIdentifier": "{{string}}",
   "SelectionRules": "{{string}}"
}
```

## Request Parameters
<a name="API_StartMetadataModelAssessment_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MigrationProjectIdentifier](#API_StartMetadataModelAssessment_RequestSyntax) **   <a name="DMS-StartMetadataModelAssessment-request-MigrationProjectIdentifier"></a>
The migration project name or Amazon Resource Name (ARN).
Type: String
Length Constraints: Maximum length of 255.
Required: Yes

 ** [SelectionRules](#API_StartMetadataModelAssessment_RequestSyntax) **   <a name="DMS-StartMetadataModelAssessment-request-SelectionRules"></a>
A JSON string that identifies the metadata models to assess. For the selection rule format and examples, see [Selection rules in DMS Schema Conversion](https://docs.aws.amazon.com/dms/latest/userguide/sc-selection-rules.html).
Usage:
+ Accepts only source selection rules, where `server-name` in the object locator matches the source data provider.
+ Supports `explicit`, `include`, and `exclude` rule actions.
Type: String
Required: Yes

## Response Syntax
<a name="API_StartMetadataModelAssessment_ResponseSyntax"></a>

```
{
   "RequestIdentifier": "string"
}
```

## Response Elements
<a name="API_StartMetadataModelAssessment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [RequestIdentifier](#API_StartMetadataModelAssessment_ResponseSyntax) **   <a name="DMS-StartMetadataModelAssessment-response-RequestIdentifier"></a>
The identifier for the assessment request.
Type: String

## Errors
<a name="API_StartMetadataModelAssessment_Errors"></a>

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
<a name="API_StartMetadataModelAssessment_Examples"></a>

### Assess all objects in a schema
<a name="API_StartMetadataModelAssessment_Example_1"></a>

The following example queues an assessment of the conversion complexity for all objects in the `ExampleSchema` schema.

#### Sample Request
<a name="API_StartMetadataModelAssessment_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: dms.<region>.<domain>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<SignedHeaders>, Signature=<Signature>
X-Amz-Date: <Date>
X-Amz-Target: AmazonDMSv20160101.StartMetadataModelAssessment
{
    "MigrationProjectIdentifier": "arn:aws:dms:us-east-1:111122223333:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS",
    "SelectionRules": "{\"rules\": [{\"rule-type\": \"selection\",\"rule-id\": \"1\",\"rule-name\": \"1\",\"object-locator\": {\"server-name\": \"example-source-server.us-east-1.rds.amazonaws.com\", \"schema-name\": \"ExampleSchema\"},\"rule-action\": \"explicit\"}]}"
}
```

#### Sample Response
<a name="API_StartMetadataModelAssessment_Example_1_Response"></a>

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
<a name="API_StartMetadataModelAssessment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dms-2016-01-01/StartMetadataModelAssessment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dms-2016-01-01/StartMetadataModelAssessment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/StartMetadataModelAssessment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dms-2016-01-01/StartMetadataModelAssessment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/StartMetadataModelAssessment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dms-2016-01-01/StartMetadataModelAssessment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dms-2016-01-01/StartMetadataModelAssessment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dms-2016-01-01/StartMetadataModelAssessment)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dms-2016-01-01/StartMetadataModelAssessment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/StartMetadataModelAssessment)
