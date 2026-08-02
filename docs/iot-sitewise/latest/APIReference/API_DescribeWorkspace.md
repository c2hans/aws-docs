---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeWorkspace.html
---

# DescribeWorkspace
<a name="API_DescribeWorkspace"></a>

Retrieves information about a workspace.

## Request Syntax
<a name="API_DescribeWorkspace_RequestSyntax"></a>

```
GET /workspaces/{{workspaceName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeWorkspace_RequestParameters"></a>

The request uses the following URI parameters.

 ** [workspaceName](#API_DescribeWorkspace_RequestSyntax) **   <a name="iotsitewise-DescribeWorkspace-request-uri-workspaceName"></a>
The name of the workspace.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

## Request Body
<a name="API_DescribeWorkspace_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeWorkspace_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "createdAt": number,
   "encryptionConfiguration": {
      "encryptionType": "string",
      "kmsKeyArn": "string"
   },
   "updatedAt": number,
   "workspaceArn": "string",
   "workspaceDescription": "string",
   "workspaceName": "string",
   "workspaceStatus": {
      "error": {
         "code": "string",
         "message": "string"
      },
      "state": "string"
   }
}
```

## Response Elements
<a name="API_DescribeWorkspace_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_DescribeWorkspace_ResponseSyntax) **   <a name="iotsitewise-DescribeWorkspace-response-createdAt"></a>
The date the workspace was created, in Unix epoch time.
Type: Timestamp

 ** [encryptionConfiguration](#API_DescribeWorkspace_ResponseSyntax) **   <a name="iotsitewise-DescribeWorkspace-response-encryptionConfiguration"></a>
The encryption configuration information for the workspace.
Type: [WorkspaceEncryptionConfigurationInfo](API_WorkspaceEncryptionConfigurationInfo.md) object

 ** [updatedAt](#API_DescribeWorkspace_ResponseSyntax) **   <a name="iotsitewise-DescribeWorkspace-response-updatedAt"></a>
The date the workspace was last updated, in Unix epoch time.
Type: Timestamp

 ** [workspaceArn](#API_DescribeWorkspace_ResponseSyntax) **   <a name="iotsitewise-DescribeWorkspace-response-workspaceArn"></a>
The ARN of the workspace.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws(-cn|-us-gov)?:[a-zA-Z0-9-:\/_\.]+$`

 ** [workspaceDescription](#API_DescribeWorkspace_ResponseSyntax) **   <a name="iotsitewise-DescribeWorkspace-response-workspaceDescription"></a>
The description of the workspace.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\u0000-\u001F\u007F]+`

 ** [workspaceName](#API_DescribeWorkspace_ResponseSyntax) **   <a name="iotsitewise-DescribeWorkspace-response-workspaceName"></a>
The name of the workspace.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`

 ** [workspaceStatus](#API_DescribeWorkspace_ResponseSyntax) **   <a name="iotsitewise-DescribeWorkspace-response-workspaceStatus"></a>
The status of the workspace, which contains the state and any error message.
Type: [WorkspaceStatus](API_WorkspaceStatus.md) object

## Errors
<a name="API_DescribeWorkspace_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access is denied.
HTTP Status Code: 403

 ** InternalFailureException **
 AWS IoT SiteWise can't process your request right now. Try again later.
HTTP Status Code: 500

 ** InvalidRequestException **
The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The requested resource can't be found.
HTTP Status Code: 404

 ** ThrottlingException **
Your request exceeded a rate limit. For example, you might have exceeded the number of AWS IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.
For more information, see [Quotas](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html) in the * AWS IoT SiteWise User Guide*.
HTTP Status Code: 429

## See Also
<a name="API_DescribeWorkspace_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotsitewise-2019-12-02/DescribeWorkspace)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotsitewise-2019-12-02/DescribeWorkspace)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/DescribeWorkspace)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotsitewise-2019-12-02/DescribeWorkspace)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/DescribeWorkspace)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotsitewise-2019-12-02/DescribeWorkspace)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotsitewise-2019-12-02/DescribeWorkspace)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotsitewise-2019-12-02/DescribeWorkspace)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotsitewise-2019-12-02/DescribeWorkspace)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/DescribeWorkspace)
