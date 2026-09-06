---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_CreateDocument.html
---

# CreateDocument
<a name="API_CreateDocument"></a>

Creates a AWS Systems Manager (SSM document). An SSM document defines the actions that Systems Manager performs on your managed nodes. For more information about SSM documents, including information about supported schemas, features, and syntax, see [AWS Systems Manager Documents](https://docs.aws.amazon.com/systems-manager/latest/userguide/documents.html) in the * AWS Systems Manager User Guide*.

## Request Syntax
<a name="API_CreateDocument_RequestSyntax"></a>

```
{
   "Attachments": [
      {
         "Key": "{{string}}",
         "Name": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "Content": "{{string}}",
   "DisplayName": "{{string}}",
   "DocumentFormat": "{{string}}",
   "DocumentType": "{{string}}",
   "Name": "{{string}}",
   "Requires": [
      {
         "Name": "{{string}}",
         "RequireType": "{{string}}",
         "Version": "{{string}}",
         "VersionName": "{{string}}"
      }
   ],
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "TargetType": "{{string}}",
   "VersionName": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateDocument_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Attachments](#API_CreateDocument_RequestSyntax) **   <a name="systemsmanager-CreateDocument-request-Attachments"></a>
A list of key-value pairs that describe attachments to a version of a document.
Type: Array of [AttachmentsSource](API_AttachmentsSource.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: No

 ** [Content](#API_CreateDocument_RequestSyntax) **   <a name="systemsmanager-CreateDocument-request-Content"></a>
The content for the new SSM document in JSON or YAML format. The content of the document must not exceed 64KB. This quota also includes the content specified for input parameters at runtime. We recommend storing the contents for your new document in an external JSON or YAML file and referencing the file in a command.
For examples, see the following topics in the * AWS Systems Manager User Guide*.
+  [Create an SSM document (console)](https://docs.aws.amazon.com/systems-manager/latest/userguide/documents-using.html#create-ssm-console)
+  [Create an SSM document (command line)](https://docs.aws.amazon.com/systems-manager/latest/userguide/documents-using.html#create-ssm-document-cli)
+  [Create an SSM document (API)](https://docs.aws.amazon.com/systems-manager/latest/userguide/documents-using.html#create-ssm-document-api)
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** [DisplayName](#API_CreateDocument_RequestSyntax) **   <a name="systemsmanager-CreateDocument-request-DisplayName"></a>
An optional field where you can specify a friendly name for the SSM document. This value can differ for each version of the document. You can update this value at a later time using the [UpdateDocument](API_UpdateDocument.md) operation.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `^[\w\.\-\:\/ ]*$`
Required: No

 ** [DocumentFormat](#API_CreateDocument_RequestSyntax) **   <a name="systemsmanager-CreateDocument-request-DocumentFormat"></a>
Specify the document format for the request. The document format can be JSON, YAML, or TEXT. JSON is the default format.
Type: String
Valid Values: `YAML | JSON | TEXT`
Required: No

 ** [DocumentType](#API_CreateDocument_RequestSyntax) **   <a name="systemsmanager-CreateDocument-request-DocumentType"></a>
The type of document to create.
The `DeploymentStrategy` document type is an internal-use-only document type reserved for AWS AppConfig.
Type: String
Valid Values: `Command | Policy | Automation | Session | Package | ApplicationConfiguration | ApplicationConfigurationSchema | DeploymentStrategy | ChangeCalendar | Automation.ChangeTemplate | ProblemAnalysis | ProblemAnalysisTemplate | CloudFormation | ConformancePackTemplate | QuickSetup | ManualApprovalPolicy | AutoApprovalPolicy`
Required: No

 ** [Name](#API_CreateDocument_RequestSyntax) **   <a name="systemsmanager-CreateDocument-request-Name"></a>
A name for the SSM document.
You can't use the following strings as document name prefixes. These are reserved by AWS for use as document name prefixes:
+  `aws`
+  `amazon`
+  `amzn`
+  `AWSEC2`
+  `AWSConfigRemediation`
+  `AWSSupport`
Type: String
Pattern: `^[a-zA-Z0-9_\-.]{3,128}$`
Required: Yes

 ** [Requires](#API_CreateDocument_RequestSyntax) **   <a name="systemsmanager-CreateDocument-request-Requires"></a>
A list of SSM documents required by a document. This parameter is used exclusively by AWS AppConfig. When a user creates an AWS AppConfig configuration in an SSM document, the user must also specify a required document for validation purposes. In this case, an `ApplicationConfiguration` document requires an `ApplicationConfigurationSchema` document for validation purposes. For more information, see [What is AWS AppConfig?](https://docs.aws.amazon.com/appconfig/latest/userguide/what-is-appconfig.html) in the * AWS AppConfig User Guide*.
Type: Array of [DocumentRequires](API_DocumentRequires.md) objects
Array Members: Minimum number of 1 item.
Required: No

 ** [Tags](#API_CreateDocument_RequestSyntax) **   <a name="systemsmanager-CreateDocument-request-Tags"></a>
Optional metadata that you assign to a resource. Tags enable you to categorize a resource in different ways, such as by purpose, owner, or environment. For example, you might want to tag an SSM document to identify the types of targets or the environment where it will run. In this case, you could specify the following key-value pairs:
+  `Key=OS,Value=Windows`
+  `Key=Environment,Value=Production`
To add tags to an existing SSM document, use the [AddTagsToResource](API_AddTagsToResource.md) operation.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Maximum number of 1000 items.
Required: No

 ** [TargetType](#API_CreateDocument_RequestSyntax) **   <a name="systemsmanager-CreateDocument-request-TargetType"></a>
Specify a target type to define the kinds of resources the document can run on. For example, to run a document on EC2 instances, specify the following value: `/AWS::EC2::Instance`. If you specify a value of '/' the document can run on all types of resources. If you don't specify a value, the document can't run on any resources. For a list of valid resource types, see [AWS resource and property types reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html) in the * AWS CloudFormation User Guide*.
Type: String
Length Constraints: Maximum length of 200.
Pattern: `^\/[\w\.\-\:\/]*$`
Required: No

 ** [VersionName](#API_CreateDocument_RequestSyntax) **   <a name="systemsmanager-CreateDocument-request-VersionName"></a>
An optional field specifying the version of the artifact you are creating with the document. For example, `Release12.1`. This value is unique across all versions of a document, and can't be changed.
Type: String
Pattern: `^[a-zA-Z0-9_\-.]{1,128}$`
Required: No

## Response Syntax
<a name="API_CreateDocument_ResponseSyntax"></a>

```
{
   "DocumentDescription": {
      "ApprovedVersion": "string",
      "AttachmentsInformation": [
         {
            "Name": "string"
         }
      ],
      "Author": "string",
      "Category": [ "string" ],
      "CategoryEnum": [ "string" ],
      "CreatedDate": number,
      "DefaultVersion": "string",
      "Description": "string",
      "DisplayName": "string",
      "DocumentFormat": "string",
      "DocumentType": "string",
      "DocumentVersion": "string",
      "Hash": "string",
      "HashType": "string",
      "LatestVersion": "string",
      "Name": "string",
      "Owner": "string",
      "Parameters": [
         {
            "DefaultValue": "string",
            "Description": "string",
            "Name": "string",
            "Type": "string"
         }
      ],
      "PendingReviewVersion": "string",
      "PlatformTypes": [ "string" ],
      "Requires": [
         {
            "Name": "string",
            "RequireType": "string",
            "Version": "string",
            "VersionName": "string"
         }
      ],
      "ReviewInformation": [
         {
            "ReviewedTime": number,
            "Reviewer": "string",
            "Status": "string"
         }
      ],
      "ReviewStatus": "string",
      "SchemaVersion": "string",
      "Sha1": "string",
      "Status": "string",
      "StatusInformation": "string",
      "Tags": [
         {
            "Key": "string",
            "Value": "string"
         }
      ],
      "TargetType": "string",
      "VersionName": "string"
   }
}
```

## Response Elements
<a name="API_CreateDocument_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DocumentDescription](#API_CreateDocument_ResponseSyntax) **   <a name="systemsmanager-CreateDocument-response-DocumentDescription"></a>
Information about the SSM document.
Type: [DocumentDescription](API_DocumentDescription.md) object

## Errors
<a name="API_CreateDocument_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DocumentAlreadyExists **
The specified document already exists.
HTTP Status Code: 400

 ** DocumentLimitExceeded **
You can have at most 500 active SSM documents.
HTTP Status Code: 400

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** InvalidDocumentContent **
The content for the document isn't valid.
 ** Message **
A description of the validation error.
HTTP Status Code: 400

 ** InvalidDocumentSchemaVersion **
The version of the document schema isn't supported.
HTTP Status Code: 400

 ** MaxDocumentSizeExceeded **
The size limit of a document is 64 KB.
HTTP Status Code: 400

 ** NoLongerSupportedException **
The requested operation is no longer supported by Systems Manager.
HTTP Status Code: 400

 ** TooManyUpdates **
There are concurrent updates for a resource that supports one update at a time.
HTTP Status Code: 400

## Examples
<a name="API_CreateDocument_Examples"></a>

### Example
<a name="API_CreateDocument_Example_1"></a>

This example illustrates one usage of CreateDocument.

#### Sample Request
<a name="API_CreateDocument_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.CreateDocument
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/1.17.12 Python/3.6.8 Darwin/18.7.0 botocore/1.14.12
X-Amz-Date: 20240324T145550Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240324/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 963

{
    "Content": "---\ndescription: \"Example\"\nschemaVersion: '0.3'\nassumeRole: \"{{ AutomationAssumeRole }}\"--truncated--",
    "Name": "Example",
    "DocumentType": "Automation",
    "DocumentFormat": "YAML"
}
```

#### Sample Response
<a name="API_CreateDocument_Example_1_Response"></a>

```
{
    "DocumentDescription": {
        "CreatedDate": 1585061751.738,
        "DefaultVersion": "1",
        "Description": "Custom Automation Example",
        "DocumentFormat": "YAML",
        "DocumentType": "Automation",
        "DocumentVersion": "1",
        "Hash": "0d3d879b3ca072e03c12638d0255ebd004d2c65bd318f8354fcde820dEXAMPLE",
        "HashType": "Sha256",
        "LatestVersion": "1",
        "Name": "Example",
        "Owner": "111122223333",
        "Parameters": [
            {
                "DefaultValue": "",
                "Description": "(Optional) The ARN of the role that allows Automation to perform the actions on your behalf. If no role is specified, Systems Manager Automation uses your IAM permissions to execute this document.",
                "Name": "AutomationAssumeRole",
                "Type": "String"
            },
            {
                "DefaultValue": "",
                "Description": "(Required) The Instance Id to create an image of.",
                "Name": "InstanceId",
                "Type": "String"
            }
        ],
        "PlatformTypes": [
            "Windows",
            "Linux"
        ],
        "SchemaVersion": "0.3",
        "Status": "Creating",
        "Tags": []
    }
}
```

## See Also
<a name="API_CreateDocument_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/CreateDocument)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/CreateDocument)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/CreateDocument)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/CreateDocument)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/CreateDocument)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/CreateDocument)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/CreateDocument)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/CreateDocument)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/CreateDocument)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/CreateDocument)
