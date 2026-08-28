---
source_url: https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_DeleteExtensionAssociation.html
---

# DeleteExtensionAssociation
<a name="API_DeleteExtensionAssociation"></a>

Deletes an extension association. This action doesn't delete extensions defined in the association.

## Request Syntax
<a name="API_DeleteExtensionAssociation_RequestSyntax"></a>

```
DELETE /extensionassociations/{{ExtensionAssociationId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteExtensionAssociation_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ExtensionAssociationId](#API_DeleteExtensionAssociation_RequestSyntax) **   <a name="appconfig-DeleteExtensionAssociation-request-uri-ExtensionAssociationId"></a>
The ID of the extension association to delete.
Pattern: `[a-z0-9]{4,7}`
Required: Yes

## Request Body
<a name="API_DeleteExtensionAssociation_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteExtensionAssociation_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_DeleteExtensionAssociation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_DeleteExtensionAssociation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
The input fails to satisfy the constraints specified by an AWS service.
 ** Details **
Detailed information about the input that failed to satisfy the constraints specified by a call.
HTTP Status Code: 400

 ** InternalServerException **
There was an internal failure in the AWS AppConfig service.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested resource could not be found.
HTTP Status Code: 404

## Examples
<a name="API_DeleteExtensionAssociation_Examples"></a>

### Example
<a name="API_DeleteExtensionAssociation_Example_1"></a>

This example illustrates one usage of DeleteExtensionAssociation.

#### Sample Request
<a name="API_DeleteExtensionAssociation_Example_1_Request"></a>

```
DELETE /extensionassociations/rnekru4 HTTP/1.1
Host: appconfig.us-west-2.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/2.7.19 Python/3.9.11 Windows/10 exe/AMD64 prompt/off command/appconfig.delete-extension-association
X-Amz-Date: 20220803T223105Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20220803/us-west-2/appconfig/aws4_request, SignedHeaders=host;x-amz-date, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 0
```

#### Sample Response
<a name="API_DeleteExtensionAssociation_Example_1_Response"></a>

```
{}
```

## See Also
<a name="API_DeleteExtensionAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appconfig-2019-10-09/DeleteExtensionAssociation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appconfig-2019-10-09/DeleteExtensionAssociation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appconfig-2019-10-09/DeleteExtensionAssociation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appconfig-2019-10-09/DeleteExtensionAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appconfig-2019-10-09/DeleteExtensionAssociation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appconfig-2019-10-09/DeleteExtensionAssociation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appconfig-2019-10-09/DeleteExtensionAssociation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appconfig-2019-10-09/DeleteExtensionAssociation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appconfig-2019-10-09/DeleteExtensionAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appconfig-2019-10-09/DeleteExtensionAssociation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS AppConfig. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appconfig` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
