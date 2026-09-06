---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_UpdateDocumentDefaultVersion.html
---

# UpdateDocumentDefaultVersion
<a name="API_UpdateDocumentDefaultVersion"></a>

Set the default version of a document.

**Note**
If you change a document version for a State Manager association, Systems Manager immediately runs the association unless you previously specifed the `apply-only-at-cron-interval` parameter.

## Request Syntax
<a name="API_UpdateDocumentDefaultVersion_RequestSyntax"></a>

```
{
   "DocumentVersion": "{{string}}",
   "Name": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateDocumentDefaultVersion_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DocumentVersion](#API_UpdateDocumentDefaultVersion_RequestSyntax) **   <a name="systemsmanager-UpdateDocumentDefaultVersion-request-DocumentVersion"></a>
The version of a custom document that you want to set as the default version.
Type: String
Pattern: `(^[1-9][0-9]*$)`
Required: Yes

 ** [Name](#API_UpdateDocumentDefaultVersion_RequestSyntax) **   <a name="systemsmanager-UpdateDocumentDefaultVersion-request-Name"></a>
The name of a custom document that you want to set as the default version.
Type: String
Pattern: `^[a-zA-Z0-9_\-.]{3,128}$`
Required: Yes

## Response Syntax
<a name="API_UpdateDocumentDefaultVersion_ResponseSyntax"></a>

```
{
   "Description": {
      "DefaultVersion": "string",
      "DefaultVersionName": "string",
      "Name": "string"
   }
}
```

## Response Elements
<a name="API_UpdateDocumentDefaultVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Description](#API_UpdateDocumentDefaultVersion_ResponseSyntax) **   <a name="systemsmanager-UpdateDocumentDefaultVersion-response-Description"></a>
The description of a custom document that you want to set as the default version.
Type: [DocumentDefaultVersionDescription](API_DocumentDefaultVersionDescription.md) object

## Errors
<a name="API_UpdateDocumentDefaultVersion_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** InvalidDocument **
The specified SSM document doesn't exist.
 ** Message **
The SSM document doesn't exist or the document isn't available to the user. This exception can be issued by various API operations.
HTTP Status Code: 400

 ** InvalidDocumentSchemaVersion **
The version of the document schema isn't supported.
HTTP Status Code: 400

 ** InvalidDocumentVersion **
The document version isn't valid or doesn't exist.
HTTP Status Code: 400

## Examples
<a name="API_UpdateDocumentDefaultVersion_Examples"></a>

### Example
<a name="API_UpdateDocumentDefaultVersion_Example_1"></a>

This example illustrates one usage of UpdateDocumentDefaultVersion.

#### Sample Request
<a name="API_UpdateDocumentDefaultVersion_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.UpdateDocumentDefaultVersion
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/1.17.12 Python/3.6.8 Darwin/18.7.0 botocore/1.14.12
X-Amz-Date: 20240325T183926Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240325/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 47

{
    "Name": "Example",
    "DocumentVersion": "2"
}
```

#### Sample Response
<a name="API_UpdateDocumentDefaultVersion_Example_1_Response"></a>

```
{
    "Description": {
        "DefaultVersion": "2",
        "Name": "Example"
    }
}
```

## See Also
<a name="API_UpdateDocumentDefaultVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/UpdateDocumentDefaultVersion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/UpdateDocumentDefaultVersion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/UpdateDocumentDefaultVersion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/UpdateDocumentDefaultVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/UpdateDocumentDefaultVersion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/UpdateDocumentDefaultVersion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/UpdateDocumentDefaultVersion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/UpdateDocumentDefaultVersion)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/UpdateDocumentDefaultVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/UpdateDocumentDefaultVersion)
