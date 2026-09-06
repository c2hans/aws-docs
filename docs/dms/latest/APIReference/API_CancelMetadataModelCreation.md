---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_CancelMetadataModelCreation.html
---

# CancelMetadataModelCreation
<a name="API_CancelMetadataModelCreation"></a>

Cancels a single metadata model creation operation that was started with `StartMetadataModelCreation`.

 **Required permissions:** `dms:CancelMetadataModelCreation`. For more information, see [Actions, resources, and condition keys for AWS Database Migration Service](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdatabasemigrationservice.html).

## Request Syntax
<a name="API_CancelMetadataModelCreation_RequestSyntax"></a>

```
{
   "MigrationProjectIdentifier": "{{string}}",
   "RequestIdentifier": "{{string}}"
}
```

## Request Parameters
<a name="API_CancelMetadataModelCreation_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MigrationProjectIdentifier](#API_CancelMetadataModelCreation_RequestSyntax) **   <a name="DMS-CancelMetadataModelCreation-request-MigrationProjectIdentifier"></a>
The migration project name or Amazon Resource Name (ARN).
Type: String
Length Constraints: Maximum length of 255.
Required: Yes

 ** [RequestIdentifier](#API_CancelMetadataModelCreation_RequestSyntax) **   <a name="DMS-CancelMetadataModelCreation-request-RequestIdentifier"></a>
The identifier for the metadata model creation operation to cancel. This operation was initiated by `StartMetadataModelCreation`.
Type: String
Required: Yes

## Response Syntax
<a name="API_CancelMetadataModelCreation_ResponseSyntax"></a>

```
{
   "Request": {
      "Error": { ... },
      "ExportSqlDetails": {
         "ObjectURL": "string",
         "S3ObjectKey": "string"
      },
      "MigrationProjectArn": "string",
      "Progress": {
         "ProcessedObject": {
            "EndpointType": "string",
            "Name": "string",
            "Type": "string"
         },
         "ProgressPercent": number,
         "ProgressStep": "string",
         "TotalObjects": number
      },
      "RequestIdentifier": "string",
      "Status": "string"
   }
}
```

## Response Elements
<a name="API_CancelMetadataModelCreation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Request](#API_CancelMetadataModelCreation_ResponseSyntax) **   <a name="DMS-CancelMetadataModelCreation-response-Request"></a>
The metadata model creation request.
 AWS DMS never populates the `ExportSqlDetails` field for this operation.
Type: [SchemaConversionRequest](API_SchemaConversionRequest.md) object

## Errors
<a name="API_CancelMetadataModelCreation_Errors"></a>

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
<a name="API_CancelMetadataModelCreation_Examples"></a>

### Cancel a metadata model creation
<a name="API_CancelMetadataModelCreation_Example_1"></a>

The following example cancels a metadata model creation operation.

#### Sample Request
<a name="API_CancelMetadataModelCreation_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: dms.<region>.<domain>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<SignedHeaders>, Signature=<Signature>
X-Amz-Date: <Date>
X-Amz-Target: AmazonDMSv20160101.CancelMetadataModelCreation
{
    "MigrationProjectIdentifier": "arn:aws:dms:us-east-1:111122223333:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS",
    "RequestIdentifier": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
}
```

#### Sample Response
<a name="API_CancelMetadataModelCreation_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
    "Request": {
        "Status": "CANCELING",
        "RequestIdentifier": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
        "MigrationProjectArn": "arn:aws:dms:us-east-1:111122223333:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS"
    }
}
```

## See Also
<a name="API_CancelMetadataModelCreation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dms-2016-01-01/CancelMetadataModelCreation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dms-2016-01-01/CancelMetadataModelCreation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/CancelMetadataModelCreation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dms-2016-01-01/CancelMetadataModelCreation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/CancelMetadataModelCreation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dms-2016-01-01/CancelMetadataModelCreation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dms-2016-01-01/CancelMetadataModelCreation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dms-2016-01-01/CancelMetadataModelCreation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dms-2016-01-01/CancelMetadataModelCreation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/CancelMetadataModelCreation)
