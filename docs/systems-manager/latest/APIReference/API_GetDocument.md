---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetDocument.html
---

# GetDocument
<a name="API_GetDocument"></a>

Gets the contents of the specified AWS Systems Manager document (SSM document).

## Request Syntax
<a name="API_GetDocument_RequestSyntax"></a>

```
{
   "DocumentFormat": "{{string}}",
   "DocumentVersion": "{{string}}",
   "Name": "{{string}}",
   "VersionName": "{{string}}"
}
```

## Request Parameters
<a name="API_GetDocument_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DocumentFormat](#API_GetDocument_RequestSyntax) **   <a name="systemsmanager-GetDocument-request-DocumentFormat"></a>
Returns the document in the specified format. The document format can be either JSON or YAML. JSON is the default format.
Type: String
Valid Values: `YAML | JSON | TEXT`
Required: No

 ** [DocumentVersion](#API_GetDocument_RequestSyntax) **   <a name="systemsmanager-GetDocument-request-DocumentVersion"></a>
The document version for which you want information.
Type: String
Pattern: `([$]LATEST|[$]DEFAULT|^[1-9][0-9]*$)`
Required: No

 ** [Name](#API_GetDocument_RequestSyntax) **   <a name="systemsmanager-GetDocument-request-Name"></a>
The name of the SSM document.
Type: String
Pattern: `^[a-zA-Z0-9_\-.:/]{3,128}$`
Required: Yes

 ** [VersionName](#API_GetDocument_RequestSyntax) **   <a name="systemsmanager-GetDocument-request-VersionName"></a>
An optional field specifying the version of the artifact associated with the document. For example, 12.6. This value is unique across all versions of a document and can't be changed.
Type: String
Pattern: `^[a-zA-Z0-9_\-.]{1,128}$`
Required: No

## Response Syntax
<a name="API_GetDocument_ResponseSyntax"></a>

```
{
   "AttachmentsContent": [
      {
         "Hash": "string",
         "HashType": "string",
         "Name": "string",
         "Size": number,
         "Url": "string"
      }
   ],
   "Content": "string",
   "CreatedDate": number,
   "DisplayName": "string",
   "DocumentFormat": "string",
   "DocumentType": "string",
   "DocumentVersion": "string",
   "Name": "string",
   "Requires": [
      {
         "Name": "string",
         "RequireType": "string",
         "Version": "string",
         "VersionName": "string"
      }
   ],
   "ReviewStatus": "string",
   "Status": "string",
   "StatusInformation": "string",
   "VersionName": "string"
}
```

## Response Elements
<a name="API_GetDocument_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AttachmentsContent](#API_GetDocument_ResponseSyntax) **   <a name="systemsmanager-GetDocument-response-AttachmentsContent"></a>
A description of the document attachments, including names, locations, sizes, and so on.
Type: Array of [AttachmentContent](API_AttachmentContent.md) objects

 ** [Content](#API_GetDocument_ResponseSyntax) **   <a name="systemsmanager-GetDocument-response-Content"></a>
The contents of the SSM document.
Type: String
Length Constraints: Minimum length of 1.

 ** [CreatedDate](#API_GetDocument_ResponseSyntax) **   <a name="systemsmanager-GetDocument-response-CreatedDate"></a>
The date the SSM document was created.
Type: Timestamp

 ** [DisplayName](#API_GetDocument_ResponseSyntax) **   <a name="systemsmanager-GetDocument-response-DisplayName"></a>
The friendly name of the SSM document. This value can differ for each version of the document. If you want to update this value, see [UpdateDocument](API_UpdateDocument.md).
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `^[\w\.\-\:\/ ]*$`

 ** [DocumentFormat](#API_GetDocument_ResponseSyntax) **   <a name="systemsmanager-GetDocument-response-DocumentFormat"></a>
The document format, either JSON or YAML.
Type: String
Valid Values: `YAML | JSON | TEXT`

 ** [DocumentType](#API_GetDocument_ResponseSyntax) **   <a name="systemsmanager-GetDocument-response-DocumentType"></a>
The document type.
Type: String
Valid Values: `Command | Policy | Automation | Session | Package | ApplicationConfiguration | ApplicationConfigurationSchema | DeploymentStrategy | ChangeCalendar | Automation.ChangeTemplate | ProblemAnalysis | ProblemAnalysisTemplate | CloudFormation | ConformancePackTemplate | QuickSetup | ManualApprovalPolicy | AutoApprovalPolicy`

 ** [DocumentVersion](#API_GetDocument_ResponseSyntax) **   <a name="systemsmanager-GetDocument-response-DocumentVersion"></a>
The document version.
Type: String
Pattern: `([$]LATEST|[$]DEFAULT|^[1-9][0-9]*$)`

 ** [Name](#API_GetDocument_ResponseSyntax) **   <a name="systemsmanager-GetDocument-response-Name"></a>
The name of the SSM document.
Type: String
Pattern: `^[a-zA-Z0-9_\-.:/]{3,128}$`

 ** [Requires](#API_GetDocument_ResponseSyntax) **   <a name="systemsmanager-GetDocument-response-Requires"></a>
A list of SSM documents required by a document. For example, an `ApplicationConfiguration` document requires an `ApplicationConfigurationSchema` document.
Type: Array of [DocumentRequires](API_DocumentRequires.md) objects
Array Members: Minimum number of 1 item.

 ** [ReviewStatus](#API_GetDocument_ResponseSyntax) **   <a name="systemsmanager-GetDocument-response-ReviewStatus"></a>
The current review status of a new custom Systems Manager document (SSM document) created by a member of your organization, or of the latest version of an existing SSM document.
Only one version of an SSM document can be in the APPROVED state at a time. When a new version is approved, the status of the previous version changes to REJECTED.
Only one version of an SSM document can be in review, or PENDING, at a time.
Type: String
Valid Values: `APPROVED | NOT_REVIEWED | PENDING | REJECTED`

 ** [Status](#API_GetDocument_ResponseSyntax) **   <a name="systemsmanager-GetDocument-response-Status"></a>
The status of the SSM document, such as `Creating`, `Active`, `Updating`, `Failed`, and `Deleting`.
Type: String
Valid Values: `Creating | Active | Updating | Deleting | Failed`

 ** [StatusInformation](#API_GetDocument_ResponseSyntax) **   <a name="systemsmanager-GetDocument-response-StatusInformation"></a>
A message returned by AWS Systems Manager that explains the `Status` value. For example, a `Failed` status might be explained by the `StatusInformation` message, "The specified S3 bucket doesn't exist. Verify that the URL of the S3 bucket is correct."
Type: String

 ** [VersionName](#API_GetDocument_ResponseSyntax) **   <a name="systemsmanager-GetDocument-response-VersionName"></a>
The version of the artifact associated with the document. For example, 12.6. This value is unique across all versions of a document, and can't be changed.
Type: String
Pattern: `^[a-zA-Z0-9_\-.]{1,128}$`

## Errors
<a name="API_GetDocument_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** InvalidDocument **
The specified SSM document doesn't exist.
 ** Message **
The SSM document doesn't exist or the document isn't available to the user. This exception can be issued by various API operations.
HTTP Status Code: 400

 ** InvalidDocumentVersion **
The document version isn't valid or doesn't exist.
HTTP Status Code: 400

## Examples
<a name="API_GetDocument_Examples"></a>

### Example
<a name="API_GetDocument_Example_1"></a>

This example illustrates one usage of GetDocument.

#### Sample Request
<a name="API_GetDocument_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.GetDocument
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/1.17.12 Python/3.6.8 Darwin/18.7.0 botocore/1.14.12
X-Amz-Date: 20240324T190721Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240324/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 30

{
    "Name": "AWS-UpdateSSMAgent"
}
```

#### Sample Response
<a name="API_GetDocument_Example_1_Response"></a>

```
{
   "Content":"{\n    \"schemaVersion\": \"1.2\",\n  \"description\": \"Update the Amazon SSM Agent to the latest version or specified version.\",--truncated--n",
   "DocumentFormat":"JSON",
   "DocumentType":"Command",
   "DocumentVersion":"1",
   "Name":"AWS-UpdateSSMAgent",
   "Status":"Active"
}
```

## See Also
<a name="API_GetDocument_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/GetDocument)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/GetDocument)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/GetDocument)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/GetDocument)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/GetDocument)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/GetDocument)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/GetDocument)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/GetDocument)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/GetDocument)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/GetDocument)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
