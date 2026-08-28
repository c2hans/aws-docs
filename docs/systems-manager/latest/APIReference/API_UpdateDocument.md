---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_UpdateDocument.html
---

# UpdateDocument
<a name="API_UpdateDocument"></a>

Updates one or more values for an SSM document.

## Request Syntax
<a name="API_UpdateDocument_RequestSyntax"></a>

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
   "DocumentVersion": "{{string}}",
   "Name": "{{string}}",
   "TargetType": "{{string}}",
   "VersionName": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateDocument_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Attachments](#API_UpdateDocument_RequestSyntax) **   <a name="systemsmanager-UpdateDocument-request-Attachments"></a>
A list of key-value pairs that describe attachments to a version of a document.
Type: Array of [AttachmentsSource](API_AttachmentsSource.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: No

 ** [Content](#API_UpdateDocument_RequestSyntax) **   <a name="systemsmanager-UpdateDocument-request-Content"></a>
A valid JSON or YAML string.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** [DisplayName](#API_UpdateDocument_RequestSyntax) **   <a name="systemsmanager-UpdateDocument-request-DisplayName"></a>
The friendly name of the SSM document that you want to update. This value can differ for each version of the document. If you don't specify a value for this parameter in your request, the existing value is applied to the new document version.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `^[\w\.\-\:\/ ]*$`
Required: No

 ** [DocumentFormat](#API_UpdateDocument_RequestSyntax) **   <a name="systemsmanager-UpdateDocument-request-DocumentFormat"></a>
Specify the document format for the new document version. The document format can be JSON, YAML, or TEXT. JSON is the default format.
Type: String
Valid Values: `YAML | JSON | TEXT`
Required: No

 ** [DocumentVersion](#API_UpdateDocument_RequestSyntax) **   <a name="systemsmanager-UpdateDocument-request-DocumentVersion"></a>
The version of the document that you want to update. Currently, Systems Manager supports updating only the latest version of the document. You can specify the version number of the latest version or use the `$LATEST` variable.
If you change a document version for a State Manager association, Systems Manager immediately runs the association unless you previously specifed the `apply-only-at-cron-interval` parameter.
Type: String
Pattern: `([$]LATEST|[$]DEFAULT|^[1-9][0-9]*$)`
Required: No

 ** [Name](#API_UpdateDocument_RequestSyntax) **   <a name="systemsmanager-UpdateDocument-request-Name"></a>
The name of the SSM document that you want to update.
Type: String
Pattern: `^[a-zA-Z0-9_\-.]{3,128}$`
Required: Yes

 ** [TargetType](#API_UpdateDocument_RequestSyntax) **   <a name="systemsmanager-UpdateDocument-request-TargetType"></a>
Specify a new target type for the document.
Type: String
Length Constraints: Maximum length of 200.
Pattern: `^\/[\w\.\-\:\/]*$`
Required: No

 ** [VersionName](#API_UpdateDocument_RequestSyntax) **   <a name="systemsmanager-UpdateDocument-request-VersionName"></a>
An optional field specifying the version of the artifact you are updating with the document. For example, 12.6. This value is unique across all versions of a document, and can't be changed.
Type: String
Pattern: `^[a-zA-Z0-9_\-.]{1,128}$`
Required: No

## Response Syntax
<a name="API_UpdateDocument_ResponseSyntax"></a>

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
<a name="API_UpdateDocument_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DocumentDescription](#API_UpdateDocument_ResponseSyntax) **   <a name="systemsmanager-UpdateDocument-response-DocumentDescription"></a>
A description of the document that was updated.
Type: [DocumentDescription](API_DocumentDescription.md) object

## Errors
<a name="API_UpdateDocument_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DocumentVersionLimitExceeded **
The document has too many versions. Delete one or more document versions and try again.
HTTP Status Code: 400

 ** DuplicateDocumentContent **
The content of the association document matches another document. Change the content of the document and try again.
HTTP Status Code: 400

 ** DuplicateDocumentVersionName **
The version name has already been used in this document. Specify a different version name, and then try again.
HTTP Status Code: 400

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** InvalidDocument **
The specified SSM document doesn't exist.
 ** Message **
The SSM document doesn't exist or the document isn't available to the user. This exception can be issued by various API operations.
HTTP Status Code: 400

 ** InvalidDocumentContent **
The content for the document isn't valid.
 ** Message **
A description of the validation error.
HTTP Status Code: 400

 ** InvalidDocumentOperation **
You attempted to delete a document while it is still shared. You must stop sharing the document before you can delete it.
HTTP Status Code: 400

 ** InvalidDocumentSchemaVersion **
The version of the document schema isn't supported.
HTTP Status Code: 400

 ** InvalidDocumentVersion **
The document version isn't valid or doesn't exist.
HTTP Status Code: 400

 ** MaxDocumentSizeExceeded **
The size limit of a document is 64 KB.
HTTP Status Code: 400

## Examples
<a name="API_UpdateDocument_Examples"></a>

### Example
<a name="API_UpdateDocument_Example_1"></a>

This example illustrates one usage of UpdateDocument.

#### Sample Request
<a name="API_UpdateDocument_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.UpdateDocument
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/1.17.12 Python/3.6.8 Darwin/18.7.0 botocore/1.14.12
X-Amz-Date: 20240325T180432Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240325/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 953

{
    "Content": "---\ndescription: \"CreateImage\"\nschemaVersion: '0.3'\nassumeRole: \"{{ AutomationAssumeRole }}\"--truncated--",
    "Name": "CreateImage",
    "DocumentVersion": "$LATEST",
    "DocumentFormat": "YAML"
}
```

#### Sample Response
<a name="API_UpdateDocument_Example_1_Response"></a>

```
{
    "DocumentDescription": {
        "CreatedDate": 1585159474.781,
        "DefaultVersion": "1",
        "Description": "Example",
        "DisplayName": "ExampleDoc",
        "DocumentFormat": "YAML",
        "DocumentType": "Automation",
        "DocumentVersion": "2",
        "Hash": "ff7430df11be00b0593ac116b2570d488bd37a2a2fa7ddf49da67976eEXAMPLE",
        "HashType": "Sha256",
        "LatestVersion": "2",
        "Name": "CreateImage",
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
                "Description": "(Required) The Instance Id whose root EBS volume you want to restore the latest Snapshot.",
                "Name": "InstanceId",
                "Type": "String"
            }
        ],
        "PlatformTypes": [
            "Windows",
            "Linux"
        ],
        "SchemaVersion": "0.3",
        "Status": "Updating",
        "Tags": []
    }
}
```

## See Also
<a name="API_UpdateDocument_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/UpdateDocument)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/UpdateDocument)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/UpdateDocument)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/UpdateDocument)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/UpdateDocument)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/UpdateDocument)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/UpdateDocument)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/UpdateDocument)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/UpdateDocument)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/UpdateDocument)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
