---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_ExportMetadataModelAssessment.html
---

# ExportMetadataModelAssessment
<a name="API_ExportMetadataModelAssessment"></a>

Saves a copy of a database migration assessment report to your Amazon S3 bucket. AWS DMS can save your assessment report as a comma-separated value (CSV) or a PDF file.

 **Required permissions:** `dms:ExportMetadataModelAssessment`. For more information, see [Actions, resources, and condition keys for AWS Database Migration Service](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdatabasemigrationservice.html).

## Request Syntax
<a name="API_ExportMetadataModelAssessment_RequestSyntax"></a>

```
{
   "AssessmentReportTypes": [ "{{string}}" ],
   "FileName": "{{string}}",
   "MigrationProjectIdentifier": "{{string}}",
   "SelectionRules": "{{string}}"
}
```

## Request Parameters
<a name="API_ExportMetadataModelAssessment_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AssessmentReportTypes](#API_ExportMetadataModelAssessment_RequestSyntax) **   <a name="DMS-ExportMetadataModelAssessment-request-AssessmentReportTypes"></a>
The file format of the assessment file.
Type: Array of strings
Array Members: Minimum number of 1 item.
Valid Values: `pdf | csv`
Required: No

 ** [FileName](#API_ExportMetadataModelAssessment_RequestSyntax) **   <a name="DMS-ExportMetadataModelAssessment-request-FileName"></a>
The name of the assessment file to create in your Amazon S3 bucket.
Type: String
Required: No

 ** [MigrationProjectIdentifier](#API_ExportMetadataModelAssessment_RequestSyntax) **   <a name="DMS-ExportMetadataModelAssessment-request-MigrationProjectIdentifier"></a>
The migration project name or Amazon Resource Name (ARN).
Type: String
Length Constraints: Maximum length of 255.
Required: Yes

 ** [SelectionRules](#API_ExportMetadataModelAssessment_RequestSyntax) **   <a name="DMS-ExportMetadataModelAssessment-request-SelectionRules"></a>
A JSON string that identifies the metadata models to export a conversion assessment report for. For the selection rule format and examples, see [Selection rules in DMS Schema Conversion](https://docs.aws.amazon.com/dms/latest/userguide/sc-selection-rules.html).
Usage:
+ Accepts only source selection rules, where `server-name` in the object locator matches the source data provider.
+ Supports only `explicit` rule actions.
Type: String
Required: Yes

## Response Syntax
<a name="API_ExportMetadataModelAssessment_ResponseSyntax"></a>

```
{
   "CsvReport": {
      "ObjectURL": "string",
      "S3ObjectKey": "string"
   },
   "PdfReport": {
      "ObjectURL": "string",
      "S3ObjectKey": "string"
   }
}
```

## Response Elements
<a name="API_ExportMetadataModelAssessment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CsvReport](#API_ExportMetadataModelAssessment_ResponseSyntax) **   <a name="DMS-ExportMetadataModelAssessment-response-CsvReport"></a>
The Amazon S3 details for an assessment exported in CSV format.
Type: [ExportMetadataModelAssessmentResultEntry](API_ExportMetadataModelAssessmentResultEntry.md) object

 ** [PdfReport](#API_ExportMetadataModelAssessment_ResponseSyntax) **   <a name="DMS-ExportMetadataModelAssessment-response-PdfReport"></a>
The Amazon S3 details for an assessment exported in PDF format.
Type: [ExportMetadataModelAssessmentResultEntry](API_ExportMetadataModelAssessmentResultEntry.md) object

## Errors
<a name="API_ExportMetadataModelAssessment_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFoundFault **
The resource could not be found.
 ** message **

HTTP Status Code: 400

## Examples
<a name="API_ExportMetadataModelAssessment_Examples"></a>

### Export a conversion assessment report
<a name="API_ExportMetadataModelAssessment_Example_1"></a>

The following example exports a conversion assessment report for all objects in the `ExampleSchema` schema.

#### Sample Request
<a name="API_ExportMetadataModelAssessment_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: dms.<region>.<domain>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<SignedHeaders>, Signature=<Signature>
X-Amz-Date: <Date>
X-Amz-Target: AmazonDMSv20160101.ExportMetadataModelAssessment
{
    "MigrationProjectIdentifier": "arn:aws:dms:us-east-1:111122223333:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS",
    "SelectionRules": "{\"rules\": [{\"rule-type\": \"selection\", \"rule-id\": \"1\", \"rule-name\": \"1\", \"object-locator\": {\"server-name\": \"example-source-server.us-east-1.rds.amazonaws.com\", \"schema-name\": \"ExampleSchema\"}, \"rule-action\": \"explicit\"}]}",
    "AssessmentReportTypes": [
        "pdf",
        "csv"
    ],
    "FileName": "example-assessment-report"
}
```

#### Sample Response
<a name="API_ExportMetadataModelAssessment_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
    "PdfReport": {
        "S3ObjectKey": "example-migration-project/example-assessment-report.pdf",
        "ObjectURL": "https://amzn-s3-demo-bucket.s3.amazonaws.com/example-migration-project/example-assessment-report.pdf"
    },
    "CsvReport": {
        "S3ObjectKey": "example-migration-project/example-assessment-report.zip",
        "ObjectURL": "https://amzn-s3-demo-bucket.s3.amazonaws.com/example-migration-project/example-assessment-report.zip"
    }
}
```

## See Also
<a name="API_ExportMetadataModelAssessment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dms-2016-01-01/ExportMetadataModelAssessment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dms-2016-01-01/ExportMetadataModelAssessment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/ExportMetadataModelAssessment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dms-2016-01-01/ExportMetadataModelAssessment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/ExportMetadataModelAssessment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dms-2016-01-01/ExportMetadataModelAssessment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dms-2016-01-01/ExportMetadataModelAssessment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dms-2016-01-01/ExportMetadataModelAssessment)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/dms-2016-01-01/ExportMetadataModelAssessment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/ExportMetadataModelAssessment)
