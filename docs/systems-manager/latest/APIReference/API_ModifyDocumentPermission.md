---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_ModifyDocumentPermission.html
---

# ModifyDocumentPermission
<a name="API_ModifyDocumentPermission"></a>

Shares a AWS Systems Manager document (SSM document)publicly or privately. If you share a document privately, you must specify the Amazon Web Services user IDs for those people who can use the document. If you share a document publicly, you must specify *All* as the account ID.

## Request Syntax
<a name="API_ModifyDocumentPermission_RequestSyntax"></a>

```
{
   "AccountIdsToAdd": [ "{{string}}" ],
   "AccountIdsToRemove": [ "{{string}}" ],
   "Name": "{{string}}",
   "PermissionType": "{{string}}",
   "SharedDocumentVersion": "{{string}}"
}
```

## Request Parameters
<a name="API_ModifyDocumentPermission_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AccountIdsToAdd](#API_ModifyDocumentPermission_RequestSyntax) **   <a name="systemsmanager-ModifyDocumentPermission-request-AccountIdsToAdd"></a>
The Amazon Web Services users that should have access to the document. The account IDs can either be a group of account IDs or *All*. You must specify a value for this parameter or the `AccountIdsToRemove` parameter.
Type: Array of strings
Array Members: Maximum number of 20 items.
Pattern: `(?i)all|[0-9]{12}`
Required: No

 ** [AccountIdsToRemove](#API_ModifyDocumentPermission_RequestSyntax) **   <a name="systemsmanager-ModifyDocumentPermission-request-AccountIdsToRemove"></a>
The Amazon Web Services users that should no longer have access to the document. The Amazon Web Services user can either be a group of account IDs or *All*. This action has a higher priority than `AccountIdsToAdd`. If you specify an ID to add and the same ID to remove, the system removes access to the document. You must specify a value for this parameter or the `AccountIdsToAdd` parameter.
Type: Array of strings
Array Members: Maximum number of 20 items.
Pattern: `(?i)all|[0-9]{12}`
Required: No

 ** [Name](#API_ModifyDocumentPermission_RequestSyntax) **   <a name="systemsmanager-ModifyDocumentPermission-request-Name"></a>
The name of the document that you want to share.
Type: String
Pattern: `^[a-zA-Z0-9_\-.]{3,128}$`
Required: Yes

 ** [PermissionType](#API_ModifyDocumentPermission_RequestSyntax) **   <a name="systemsmanager-ModifyDocumentPermission-request-PermissionType"></a>
The permission type for the document. The permission type can be *Share*.
Type: String
Valid Values: `Share`
Required: Yes

 ** [SharedDocumentVersion](#API_ModifyDocumentPermission_RequestSyntax) **   <a name="systemsmanager-ModifyDocumentPermission-request-SharedDocumentVersion"></a>
(Optional) The version of the document to share. If it isn't specified, the system choose the `Default` version to share.
Type: String
Length Constraints: Maximum length of 8.
Pattern: `([$]LATEST|[$]DEFAULT|[$]ALL)`
Required: No

## Response Elements
<a name="API_ModifyDocumentPermission_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_ModifyDocumentPermission_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DocumentLimitExceeded **
You can have at most 500 active SSM documents.
HTTP Status Code: 400

 ** DocumentPermissionLimit **
The document can't be shared with more AWS accounts. You can specify a maximum of 20 accounts per API operation to share a private document.
By default, you can share a private document with a maximum of 1,000 accounts and publicly share up to five documents.
If you need to increase the quota for privately or publicly shared Systems Manager documents, contact AWS Support.
HTTP Status Code: 400

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** InvalidDocument **
The specified SSM document doesn't exist.
 ** Message **
The SSM document doesn't exist or the document isn't available to the user. This exception can be issued by various API operations.
HTTP Status Code: 400

 ** InvalidPermissionType **
The permission type isn't supported. *Share* is the only supported permission type.
HTTP Status Code: 400

## Examples
<a name="API_ModifyDocumentPermission_Examples"></a>

### Example
<a name="API_ModifyDocumentPermission_Example_1"></a>

This example illustrates one usage of ModifyDocumentPermission.

#### Sample Request
<a name="API_ModifyDocumentPermission_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.ModifyDocumentPermission
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/1.17.12 Python/3.6.8 Darwin/18.7.0 botocore/1.14.12
X-Amz-Date: 20240325T152441Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240325/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 78

{
    "Name": "Example",
    "PermissionType": "Share",
    "AccountIdsToAdd": [
        "444455556666"
    ]
}
```

#### Sample Response
<a name="API_ModifyDocumentPermission_Example_1_Response"></a>

```
{}
```

## See Also
<a name="API_ModifyDocumentPermission_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/ModifyDocumentPermission)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/ModifyDocumentPermission)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/ModifyDocumentPermission)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/ModifyDocumentPermission)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/ModifyDocumentPermission)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/ModifyDocumentPermission)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/ModifyDocumentPermission)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/ModifyDocumentPermission)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/ModifyDocumentPermission)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/ModifyDocumentPermission)
