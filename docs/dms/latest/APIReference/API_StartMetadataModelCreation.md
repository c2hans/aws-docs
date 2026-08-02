---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_StartMetadataModelCreation.html
---

# StartMetadataModelCreation
<a name="API_StartMetadataModelCreation"></a>

Queues the creation of a metadata model in the source metadata tree. If other requests created by `Start*` operations are already in the migration project's queue, the creation begins after they complete.

**Note**
This operation supports only Microsoft SQL Server to Aurora PostgreSQL and Microsoft SQL Server to Amazon RDS for PostgreSQL conversion paths.

To check the status of the creation request, call [DescribeMetadataModelCreations](https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeMetadataModelCreations.html) using the returned `RequestIdentifier` as a filter.

To cancel a queued or in-progress request, call [CancelMetadataModelCreation](https://docs.aws.amazon.com/dms/latest/APIReference/API_CancelMetadataModelCreation.html) with the returned `RequestIdentifier`.

**Important**
Calling [StartMetadataModelImport](https://docs.aws.amazon.com/dms/latest/APIReference/API_StartMetadataModelImport.html) with `Refresh` deletes metadata models created by this operation.

After the creation completes successfully:
+ To evaluate conversion complexity, call [StartMetadataModelAssessment](https://docs.aws.amazon.com/dms/latest/APIReference/API_StartMetadataModelAssessment.html).
+ To convert to the target database format, call [StartMetadataModelConversion](https://docs.aws.amazon.com/dms/latest/APIReference/API_StartMetadataModelConversion.html).

 **Required permissions:** `dms:StartMetadataModelCreation`. For more information, see [Actions, resources, and condition keys for AWS Database Migration Service](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdatabasemigrationservice.html).

## Request Syntax
<a name="API_StartMetadataModelCreation_RequestSyntax"></a>

```
{
   "MetadataModelName": "{{string}}",
   "MigrationProjectIdentifier": "{{string}}",
   "Properties": { ... },
   "SelectionRules": "{{string}}"
}
```

## Request Parameters
<a name="API_StartMetadataModelCreation_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MetadataModelName](#API_StartMetadataModelCreation_RequestSyntax) **   <a name="DMS-StartMetadataModelCreation-request-MetadataModelName"></a>
The name for the metadata model to use in subsequent operations.
Type: String
Required: Yes

 ** [MigrationProjectIdentifier](#API_StartMetadataModelCreation_RequestSyntax) **   <a name="DMS-StartMetadataModelCreation-request-MigrationProjectIdentifier"></a>
The migration project name or Amazon Resource Name (ARN).
Type: String
Length Constraints: Maximum length of 255.
Required: Yes

 ** [Properties](#API_StartMetadataModelCreation_RequestSyntax) **   <a name="DMS-StartMetadataModelCreation-request-Properties"></a>
The properties of the metadata model.
Type: [MetadataModelProperties](API_MetadataModelProperties.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [SelectionRules](#API_StartMetadataModelCreation_RequestSyntax) **   <a name="DMS-StartMetadataModelCreation-request-SelectionRules"></a>
A JSON string that identifies the source schema for the metadata model. For the selection rule format and examples, see [Selection rules in DMS Schema Conversion](https://docs.aws.amazon.com/dms/latest/userguide/sc-selection-rules.html).
Usage:
+ Accepts only source selection rules, where `server-name` in the object locator matches the source data provider.
+ Supports only `explicit` rule actions.
+ Exactly one rule is allowed.
Type: String
Required: Yes

## Response Syntax
<a name="API_StartMetadataModelCreation_ResponseSyntax"></a>

```
{
   "RequestIdentifier": "string"
}
```

## Response Elements
<a name="API_StartMetadataModelCreation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [RequestIdentifier](#API_StartMetadataModelCreation_ResponseSyntax) **   <a name="DMS-StartMetadataModelCreation-response-RequestIdentifier"></a>
The identifier for the creation request.
Type: String

## Errors
<a name="API_StartMetadataModelCreation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedFault **
 AWS DMS was denied access to the endpoint. Check that the role is correctly configured.
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

## Examples
<a name="API_StartMetadataModelCreation_Examples"></a>

### Create a metadata model for a SQL statement
<a name="API_StartMetadataModelCreation_Example_1"></a>

The following example queues the creation of a metadata model for a SQL statement. The selection rule specifies the schema where the metadata model is placed, and `MetadataModelName` provides a unique identifier for use in subsequent operations.

#### Sample Request
<a name="API_StartMetadataModelCreation_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: dms.<region>.<domain>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<SignedHeaders>, Signature=<Signature>
X-Amz-Date: <Date>
X-Amz-Target: AmazonDMSv20160101.StartMetadataModelCreation
{
    "MigrationProjectIdentifier": "arn:aws:dms:us-east-1:111122223333:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS",
    "SelectionRules": "{\"rules\": [{\"rule-type\": \"selection\", \"rule-id\": \"1\", \"rule-name\": \"1\", \"object-locator\": {\"server-name\": \"example-source-server.us-east-1.rds.amazonaws.com\", \"database-name\": \"ExampleDatabase\", \"schema-name\": \"ExampleSchema\"}, \"rule-action\": \"explicit\"}]}",
    "MetadataModelName": "ExampleStatement",
    "Properties": {
        "StatementProperties": {
            "Definition": "SELECT * FROM ExampleTable;"
        }
    }
}
```

#### Sample Response
<a name="API_StartMetadataModelCreation_Example_1_Response"></a>

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
<a name="API_StartMetadataModelCreation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dms-2016-01-01/StartMetadataModelCreation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dms-2016-01-01/StartMetadataModelCreation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/StartMetadataModelCreation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dms-2016-01-01/StartMetadataModelCreation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/StartMetadataModelCreation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dms-2016-01-01/StartMetadataModelCreation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dms-2016-01-01/StartMetadataModelCreation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dms-2016-01-01/StartMetadataModelCreation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dms-2016-01-01/StartMetadataModelCreation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/StartMetadataModelCreation)
