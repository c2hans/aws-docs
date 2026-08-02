---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_UpdateDocumentMetadata.html
---

# UpdateDocumentMetadata
<a name="API_UpdateDocumentMetadata"></a>

**Important**
 AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Systems Manager Change Manager availability change](https://docs.aws.amazon.com/systems-manager/latest/userguide/change-manager-availability-change.html).

Updates information related to approval reviews for a specific version of a change template in Change Manager.

## Request Syntax
<a name="API_UpdateDocumentMetadata_RequestSyntax"></a>

```
{
   "DocumentReviews": {
      "Action": "{{string}}",
      "Comment": [
         {
            "Content": "{{string}}",
            "Type": "{{string}}"
         }
      ]
   },
   "DocumentVersion": "{{string}}",
   "Name": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateDocumentMetadata_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DocumentReviews](#API_UpdateDocumentMetadata_RequestSyntax) **   <a name="systemsmanager-UpdateDocumentMetadata-request-DocumentReviews"></a>
The change template review details to update.
Type: [DocumentReviews](API_DocumentReviews.md) object
Required: Yes

 ** [DocumentVersion](#API_UpdateDocumentMetadata_RequestSyntax) **   <a name="systemsmanager-UpdateDocumentMetadata-request-DocumentVersion"></a>
The version of a change template in which to update approval metadata.
Type: String
Pattern: `([$]LATEST|[$]DEFAULT|^[1-9][0-9]*$)`
Required: No

 ** [Name](#API_UpdateDocumentMetadata_RequestSyntax) **   <a name="systemsmanager-UpdateDocumentMetadata-request-Name"></a>
The name of the change template for which a version's metadata is to be updated.
Type: String
Pattern: `^[a-zA-Z0-9_\-.]{3,128}$`
Required: Yes

## Response Elements
<a name="API_UpdateDocumentMetadata_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateDocumentMetadata_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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

 ** InvalidDocumentVersion **
The document version isn't valid or doesn't exist.
HTTP Status Code: 400

 ** TooManyUpdates **
There are concurrent updates for a resource that supports one update at a time.
HTTP Status Code: 400

## Examples
<a name="API_UpdateDocumentMetadata_Examples"></a>

### Example
<a name="API_UpdateDocumentMetadata_Example_1"></a>

This example illustrates one usage of UpdateDocumentMetadata.

#### Sample Request
<a name="API_UpdateDocumentMetadata_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.UpdateDocumentMetadata
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/1.17.12 Python/3.6.8 Darwin/18.7.0 botocore/1.14.12
X-Amz-Date: 20240730T154930Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240730/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 68

{
    "DocumentReviews": [
        {
            "Action": "Approve",
            "Comment": [
                {
                    "Type": "Comment",
                    "Content": "Approved!"
                }
            ]
        }
    ]
}
```

#### Sample Response
<a name="API_UpdateDocumentMetadata_Example_1_Response"></a>

```
{}
```

## See Also
<a name="API_UpdateDocumentMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/UpdateDocumentMetadata)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/UpdateDocumentMetadata)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/UpdateDocumentMetadata)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/UpdateDocumentMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/UpdateDocumentMetadata)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/UpdateDocumentMetadata)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/UpdateDocumentMetadata)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/UpdateDocumentMetadata)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/UpdateDocumentMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/UpdateDocumentMetadata)
