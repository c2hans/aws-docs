---
source_url: https://docs.aws.amazon.com/textract/latest/APIReference/API_CreateProject.html
---

# CreateProject

Creates a project that groups the configuration used to run document insights jobs.

## Request Syntax
<a name="API_CreateProject_RequestSyntax"></a>

```
{
   "ClientRequestToken": "{{string}}",
   "CustomConfiguration": {
      "Blueprints": [
         {
            "BlueprintArn": "{{string}}",
            "BlueprintVersion": "{{string}}"
         }
      ],
      "FallbackBlueprints": [
         {
            "BlueprintArn": "{{string}}",
            "BlueprintVersion": "{{string}}"
         }
      ]
   },
   "EncryptionConfiguration": {
      "KmsEncryptionContext": {
         "{{string}}" : "{{string}}"
      },
      "KmsKeyId": "{{string}}"
   },
   "ExtractionConfiguration": {
      "BoundingBox": {
         "State": "{{string}}"
      },
      "Granularity": {
         "Types": [ "{{string}}" ]
      },
      "OutputFormat": {
         "AdditionalFileFormat": {
            "State": "{{string}}"
         },
         "TextFormat": {
            "Types": [ "{{string}}" ]
         }
      }
   },
   "GenerativeConfiguration": {
      "FigureCaption": {
         "State": "{{string}}"
      },
      "Summarization": {
         "State": "{{string}}"
      }
   },
   "ProjectDescription": "{{string}}",
   "ProjectName": "{{string}}",
   "SensitiveDataConfiguration": {
      "DetectionMode": "{{string}}",
      "PiiEntitiesConfiguration": {
         "PiiEntityTypes": [ "{{string}}" ],
         "RedactionMaskMode": "{{string}}"
      }
   },
   "SplitterConfiguration": {
      "State": "{{string}}"
   },
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## Request Parameters
<a name="API_CreateProject_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientRequestToken](#API_CreateProject_RequestSyntax) **   <a name="Textract-CreateProject-request-ClientRequestToken"></a>
A unique, case-sensitive identifier that you provide to ensure that the operation completes no more than one time. If you use the same token for a request that matches a previous request, the service ignores the request, but does not return an error.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9-_]+$`
Required: No

 ** [CustomConfiguration](#API_CreateProject_RequestSyntax) **   <a name="Textract-CreateProject-request-CustomConfiguration"></a>
The configuration that associates blueprints with the project for custom output extraction.
Type: [CustomConfiguration](API_CustomConfiguration.md) object
Required: No

 ** [EncryptionConfiguration](#API_CreateProject_RequestSyntax) **   <a name="Textract-CreateProject-request-EncryptionConfiguration"></a>
The AWS KMS encryption configuration used to encrypt the project at rest. If you don't specify a value, Amazon Textract encrypts the project using an AWS owned key.
Type: [EncryptionConfiguration](API_EncryptionConfiguration.md) object
Required: No

 ** [ExtractionConfiguration](#API_CreateProject_RequestSyntax) **   <a name="Textract-CreateProject-request-ExtractionConfiguration"></a>
The configuration that controls how Amazon Textract extracts content from the document, including bounding boxes, granularity, and output format.
Type: [ExtractionConfiguration](API_ExtractionConfiguration.md) object
Required: Yes

 ** [GenerativeConfiguration](#API_CreateProject_RequestSyntax) **   <a name="Textract-CreateProject-request-GenerativeConfiguration"></a>
The configuration that controls generative capabilities such as summarization and figure captioning.
Type: [GenerativeConfiguration](API_GenerativeConfiguration.md) object
Required: No

 ** [ProjectDescription](#API_CreateProject_RequestSyntax) **   <a name="Textract-CreateProject-request-ProjectDescription"></a>
A description of the project.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 300.
Pattern: `^[a-zA-Z0-9\s!"\#\$%'&\(\)\*\+\,\-\./:;=\?@\[\\\]\^_`\{\|\}~><À-ÖØ-Üßà-öø-üẞ¿¡Œ-œ°£¥₹€§©ª®™¹±-µ✓⑆-⑉฿₽₱₦₣₩₫₺]*$`
Required: No

 ** [ProjectName](#API_CreateProject_RequestSyntax) **   <a name="Textract-CreateProject-request-ProjectName"></a>
A unique name for the project.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[a-zA-Z0-9-_]+$`
Required: Yes

 ** [SensitiveDataConfiguration](#API_CreateProject_RequestSyntax) **   <a name="Textract-CreateProject-request-SensitiveDataConfiguration"></a>
The configuration that controls detection and redaction of sensitive data, such as personally identifiable information (PII).
Type: [SensitiveDataConfiguration](API_SensitiveDataConfiguration.md) object
Required: No

 ** [SplitterConfiguration](#API_CreateProject_RequestSyntax) **   <a name="Textract-CreateProject-request-SplitterConfiguration"></a>
The configuration that controls whether multi-document packets are split into individual documents.
Type: [SplitterConfiguration](API_SplitterConfiguration.md) object
Required: No

 ** [Tags](#API_CreateProject_RequestSyntax) **   <a name="Textract-CreateProject-request-Tags"></a>
A set of tags (key-value pairs) to assign to the project.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^[\p{L}\p{Z}\p{N}_.:/=+\-@]*$`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

## Response Syntax
<a name="API_CreateProject_ResponseSyntax"></a>

```
{
   "ProjectArn": "string",
   "Status": "string"
}
```

## Response Elements
<a name="API_CreateProject_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ProjectArn](#API_CreateProject_ResponseSyntax) **   <a name="Textract-CreateProject-response-ProjectArn"></a>
The Amazon Resource Name (ARN) of the project that was created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^arn:aws(|-cn|-iso|-iso-[a-z]|-us-gov):textract:[a-zA-Z0-9-]*:(aws|[0-9]{12}):project/[a-zA-Z0-9-]{12,36}$`

 ** [Status](#API_CreateProject_ResponseSyntax) **   <a name="Textract-CreateProject-response-Status"></a>
The status of the project, indicating whether creation completed successfully or failed.
Type: String
Valid Values: `COMPLETED | FAILED`

## Errors
<a name="API_CreateProject_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You aren't authorized to perform the action. Use the Amazon Resource Name (ARN) of an authorized user or IAM role to perform the operation.
HTTP Status Code: 400

 ** ConflictException **
Updating or deleting a resource can cause an inconsistent state.
HTTP Status Code: 400

 ** InternalServerError **
Amazon Textract experienced a service issue. Try your call again.
HTTP Status Code: 500

 ** InvalidParameterException **
An input parameter violated a constraint. For example, in synchronous operations, an `InvalidParameterException` exception occurs when neither of the `S3Object` or `Bytes` values are supplied in the `Document` request parameter. Validate your parameter before calling the API operation again.
HTTP Status Code: 400

 ** LimitExceededException **
An Amazon Textract service limit was exceeded. For example, if you start too many asynchronous jobs concurrently, calls to start operations (`StartDocumentTextDetection`, for example) raise a LimitExceededException exception (HTTP status code: 400) until the number of concurrently running jobs is below the Amazon Textract service limit.
HTTP Status Code: 400

 ** ProvisionedThroughputExceededException **
The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Textract.
HTTP Status Code: 400

 ** ResourceNotFoundException **
 Returned when an operation tried to access a nonexistent resource.
HTTP Status Code: 400

 ** ValidationException **
 Indicates that a request was not valid. Check request for proper formatting.
HTTP Status Code: 400

## See Also
<a name="API_CreateProject_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/textract-2018-06-27/CreateProject)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/textract-2018-06-27/CreateProject)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/textract-2018-06-27/CreateProject)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/textract-2018-06-27/CreateProject)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/textract-2018-06-27/CreateProject)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/textract-2018-06-27/CreateProject)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/textract-2018-06-27/CreateProject)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/textract-2018-06-27/CreateProject)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/textract-2018-06-27/CreateProject)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/textract-2018-06-27/CreateProject)
