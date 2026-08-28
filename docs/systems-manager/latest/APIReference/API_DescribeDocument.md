---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribeDocument.html
---

# DescribeDocument
<a name="API_DescribeDocument"></a>

Describes the specified AWS Systems Manager document (SSM document).

## Request Syntax
<a name="API_DescribeDocument_RequestSyntax"></a>

```
{
   "DocumentVersion": "{{string}}",
   "Name": "{{string}}",
   "VersionName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeDocument_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DocumentVersion](#API_DescribeDocument_RequestSyntax) **   <a name="systemsmanager-DescribeDocument-request-DocumentVersion"></a>
The document version for which you want information. Can be a specific version or the default version.
Type: String
Pattern: `([$]LATEST|[$]DEFAULT|^[1-9][0-9]*$)`
Required: No

 ** [Name](#API_DescribeDocument_RequestSyntax) **   <a name="systemsmanager-DescribeDocument-request-Name"></a>
The name of the SSM document.
If you're calling a shared SSM document from a different AWS account, `Name` is the full Amazon Resource Name (ARN) of the document.
Type: String
Pattern: `^[a-zA-Z0-9_\-.:/]{3,128}$`
Required: Yes

 ** [VersionName](#API_DescribeDocument_RequestSyntax) **   <a name="systemsmanager-DescribeDocument-request-VersionName"></a>
An optional field specifying the version of the artifact associated with the document. For example, 12.6. This value is unique across all versions of a document, and can't be changed.
Type: String
Pattern: `^[a-zA-Z0-9_\-.]{1,128}$`
Required: No

## Response Syntax
<a name="API_DescribeDocument_ResponseSyntax"></a>

```
{
   "Document": {
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
<a name="API_DescribeDocument_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Document](#API_DescribeDocument_ResponseSyntax) **   <a name="systemsmanager-DescribeDocument-response-Document"></a>
Information about the SSM document.
Type: [DocumentDescription](API_DocumentDescription.md) object

## Errors
<a name="API_DescribeDocument_Errors"></a>

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
<a name="API_DescribeDocument_Examples"></a>

### Example
<a name="API_DescribeDocument_Example_1"></a>

This example illustrates one usage of DescribeDocument.

#### Sample Request
<a name="API_DescribeDocument_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.DescribeDocument
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/1.17.12 Python/3.6.8 Darwin/18.7.0 botocore/1.14.12
X-Amz-Date: 20240324T182134Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240324/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 23

{
    "Name": "Example"
}
```

#### Sample Response
<a name="API_DescribeDocument_Example_1_Response"></a>

```
{
    "Document": {
        "CreatedDate": 1585061514.204,
        "DefaultVersion": "1",
        "Description": "Example",
        "DocumentFormat": "YAML",
        "DocumentType": "Automation",
        "DocumentVersion": "1",
        "DisplayName": "ExampleDoc",
        "Hash": "68b196e538f5a895f87a0cc15eb74614021f44b47329aa95ccc0f4f71EXAMPLE",
        "HashType": "Sha256",
        "LatestVersion": "1",
        "Name": "Example",
        "Owner": "111122223333",
        "Parameters": [
            {
                "DefaultValue": "",
                "Description": "(Required) The ARN of the role that allows Automation to perform the actions on your behalf. If no role is specified, Systems Manager Automation uses your IAM permissions to execute this document.",
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
        "Status": "Active",
        "Tags": []
    }
}
```

## See Also
<a name="API_DescribeDocument_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/DescribeDocument)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/DescribeDocument)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/DescribeDocument)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/DescribeDocument)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/DescribeDocument)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/DescribeDocument)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/DescribeDocument)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/DescribeDocument)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/DescribeDocument)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/DescribeDocument)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
