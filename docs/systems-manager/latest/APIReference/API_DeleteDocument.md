---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DeleteDocument.html
---

# DeleteDocument
<a name="API_DeleteDocument"></a>

Deletes the AWS Systems Manager document (SSM document) and all managed node associations to the document.

Before you delete the document, we recommend that you use [DeleteAssociation](API_DeleteAssociation.md) to disassociate all managed nodes that are associated with the document.

## Request Syntax
<a name="API_DeleteDocument_RequestSyntax"></a>

```
{
   "DocumentVersion": "{{string}}",
   "Force": {{boolean}},
   "Name": "{{string}}",
   "VersionName": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteDocument_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DocumentVersion](#API_DeleteDocument_RequestSyntax) **   <a name="systemsmanager-DeleteDocument-request-DocumentVersion"></a>
The version of the document that you want to delete. If not provided, all versions of the document are deleted.
Type: String
Pattern: `([$]LATEST|[$]DEFAULT|^[1-9][0-9]*$)`
Required: No

 ** [Force](#API_DeleteDocument_RequestSyntax) **   <a name="systemsmanager-DeleteDocument-request-Force"></a>
Some SSM document types require that you specify a `Force` flag before you can delete the document. For example, you must specify a `Force` flag to delete a document of type `ApplicationConfigurationSchema`. You can restrict access to the `Force` flag in an AWS Identity and Access Management (IAM) policy.
Type: Boolean
Required: No

 ** [Name](#API_DeleteDocument_RequestSyntax) **   <a name="systemsmanager-DeleteDocument-request-Name"></a>
The name of the document.
Type: String
Pattern: `^[a-zA-Z0-9_\-.]{3,128}$`
Required: Yes

 ** [VersionName](#API_DeleteDocument_RequestSyntax) **   <a name="systemsmanager-DeleteDocument-request-VersionName"></a>
The version name of the document that you want to delete. If not provided, all versions of the document are deleted.
Type: String
Pattern: `^[a-zA-Z0-9_\-.]{1,128}$`
Required: No

## Response Elements
<a name="API_DeleteDocument_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteDocument_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AssociatedInstances **
You must disassociate a document from all managed nodes before you can delete it.
HTTP Status Code: 400

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** InvalidDocument **
The specified SSM document doesn't exist.
 ** Message **
The SSM document doesn't exist or the document isn't available to the user. This exception can be issued by various API operations.
HTTP Status Code: 400

 ** InvalidDocumentOperation **
You attempted to delete a document while it is still shared. You must stop sharing the document before you can delete it.
HTTP Status Code: 400

 ** TooManyUpdates **
There are concurrent updates for a resource that supports one update at a time.
HTTP Status Code: 400

## Examples
<a name="API_DeleteDocument_Examples"></a>

### Example
<a name="API_DeleteDocument_Example_1"></a>

This example illustrates one usage of DeleteDocument.

#### Sample Request
<a name="API_DeleteDocument_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.DeleteDocument
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/1.17.12 Python/3.6.8 Darwin/18.7.0 botocore/1.14.12
X-Amz-Date: 20240324T151532Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240324/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 19

{
    "Name": "Example"
}
```

#### Sample Response
<a name="API_DeleteDocument_Example_1_Response"></a>

```
{}
```

## See Also
<a name="API_DeleteDocument_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/DeleteDocument)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/DeleteDocument)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/DeleteDocument)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/DeleteDocument)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/DeleteDocument)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/DeleteDocument)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/DeleteDocument)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/DeleteDocument)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/DeleteDocument)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/DeleteDocument)
