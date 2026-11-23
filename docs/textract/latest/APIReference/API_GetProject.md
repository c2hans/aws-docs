---
source_url: https://docs.aws.amazon.com/textract/latest/APIReference/API_GetProject.html
---

# GetProject

Gets the details of a project, including its configuration, status, and timestamps.

## Request Syntax
<a name="API_GetProject_RequestSyntax"></a>

```
{
   "ProjectArn": "{{string}}"
}
```

## Request Parameters
<a name="API_GetProject_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ProjectArn](#API_GetProject_RequestSyntax) **   <a name="Textract-GetProject-request-ProjectArn"></a>
The Amazon Resource Name (ARN) of the project to retrieve.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^arn:aws(|-cn|-iso|-iso-[a-z]|-us-gov):textract:[a-zA-Z0-9-]*:(aws|[0-9]{12}):project/[a-zA-Z0-9-]{12,36}$`
Required: Yes

## Response Syntax
<a name="API_GetProject_ResponseSyntax"></a>

```
{
   "CreationTime": number,
   "CustomConfiguration": {
      "Blueprints": [
         {
            "BlueprintArn": "string",
            "BlueprintVersion": "string"
         }
      ],
      "FallbackBlueprints": [
         {
            "BlueprintArn": "string",
            "BlueprintVersion": "string"
         }
      ]
   },
   "EncryptionConfiguration": {
      "KmsEncryptionContext": {
         "string" : "string"
      },
      "KmsKeyId": "string"
   },
   "ExtractionConfiguration": {
      "BoundingBox": {
         "State": "string"
      },
      "Granularity": {
         "Types": [ "string" ]
      },
      "OutputFormat": {
         "AdditionalFileFormat": {
            "State": "string"
         },
         "TextFormat": {
            "Types": [ "string" ]
         }
      }
   },
   "GenerativeConfiguration": {
      "FigureCaption": {
         "State": "string"
      },
      "Summarization": {
         "State": "string"
      }
   },
   "LastModifiedTime": number,
   "ProjectArn": "string",
   "ProjectDescription": "string",
   "ProjectName": "string",
   "SensitiveDataConfiguration": {
      "DetectionMode": "string",
      "PiiEntitiesConfiguration": {
         "PiiEntityTypes": [ "string" ],
         "RedactionMaskMode": "string"
      }
   },
   "SplitterConfiguration": {
      "State": "string"
   },
   "Status": "string"
}
```

## Response Elements
<a name="API_GetProject_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreationTime](#API_GetProject_ResponseSyntax) **   <a name="Textract-GetProject-response-CreationTime"></a>
The date and time that the project was created.
Type: Timestamp

 ** [CustomConfiguration](#API_GetProject_ResponseSyntax) **   <a name="Textract-GetProject-response-CustomConfiguration"></a>
The configuration that associates blueprints with the project for custom output extraction.
Type: [CustomConfiguration](API_CustomConfiguration.md) object

 ** [EncryptionConfiguration](#API_GetProject_ResponseSyntax) **   <a name="Textract-GetProject-response-EncryptionConfiguration"></a>
The AWS KMS encryption configuration used to encrypt the project at rest.
Type: [EncryptionConfiguration](API_EncryptionConfiguration.md) object

 ** [ExtractionConfiguration](#API_GetProject_ResponseSyntax) **   <a name="Textract-GetProject-response-ExtractionConfiguration"></a>
The configuration that controls how Amazon Textract extracts content from the document, including bounding boxes, granularity, and output format.
Type: [ExtractionConfiguration](API_ExtractionConfiguration.md) object

 ** [GenerativeConfiguration](#API_GetProject_ResponseSyntax) **   <a name="Textract-GetProject-response-GenerativeConfiguration"></a>
The configuration that controls generative capabilities such as summarization and figure captioning.
Type: [GenerativeConfiguration](API_GenerativeConfiguration.md) object

 ** [LastModifiedTime](#API_GetProject_ResponseSyntax) **   <a name="Textract-GetProject-response-LastModifiedTime"></a>
The date and time that the project was last modified.
Type: Timestamp

 ** [ProjectArn](#API_GetProject_ResponseSyntax) **   <a name="Textract-GetProject-response-ProjectArn"></a>
The Amazon Resource Name (ARN) of the project.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^arn:aws(|-cn|-iso|-iso-[a-z]|-us-gov):textract:[a-zA-Z0-9-]*:(aws|[0-9]{12}):project/[a-zA-Z0-9-]{12,36}$`

 ** [ProjectDescription](#API_GetProject_ResponseSyntax) **   <a name="Textract-GetProject-response-ProjectDescription"></a>
The description of the project.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 300.
Pattern: `^[a-zA-Z0-9\s!"\#\$%'&\(\)\*\+\,\-\./:;=\?@\[\\\]\^_`\{\|\}~><À-ÖØ-Üßà-öø-üẞ¿¡Œ-œ°£¥₹€§©ª®™¹±-µ✓⑆-⑉฿₽₱₦₣₩₫₺]*$`

 ** [ProjectName](#API_GetProject_ResponseSyntax) **   <a name="Textract-GetProject-response-ProjectName"></a>
The name of the project.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[a-zA-Z0-9-_]+$`

 ** [SensitiveDataConfiguration](#API_GetProject_ResponseSyntax) **   <a name="Textract-GetProject-response-SensitiveDataConfiguration"></a>
The configuration that controls detection and redaction of sensitive data, such as personally identifiable information (PII).
Type: [SensitiveDataConfiguration](API_SensitiveDataConfiguration.md) object

 ** [SplitterConfiguration](#API_GetProject_ResponseSyntax) **   <a name="Textract-GetProject-response-SplitterConfiguration"></a>
The configuration that controls whether multi-document packets are split into individual documents.
Type: [SplitterConfiguration](API_SplitterConfiguration.md) object

 ** [Status](#API_GetProject_ResponseSyntax) **   <a name="Textract-GetProject-response-Status"></a>
The status of the project, indicating whether it was created successfully or failed.
Type: String
Valid Values: `COMPLETED | FAILED`

## Errors
<a name="API_GetProject_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You aren't authorized to perform the action. Use the Amazon Resource Name (ARN) of an authorized user or IAM role to perform the operation.
HTTP Status Code: 400

 ** InternalServerError **
Amazon Textract experienced a service issue. Try your call again.
HTTP Status Code: 500

 ** InvalidParameterException **
An input parameter violated a constraint. For example, in synchronous operations, an `InvalidParameterException` exception occurs when neither of the `S3Object` or `Bytes` values are supplied in the `Document` request parameter. Validate your parameter before calling the API operation again.
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
<a name="API_GetProject_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/textract-2018-06-27/GetProject)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/textract-2018-06-27/GetProject)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/textract-2018-06-27/GetProject)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/textract-2018-06-27/GetProject)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/textract-2018-06-27/GetProject)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/textract-2018-06-27/GetProject)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/textract-2018-06-27/GetProject)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/textract-2018-06-27/GetProject)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/textract-2018-06-27/GetProject)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/textract-2018-06-27/GetProject)
