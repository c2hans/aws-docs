---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_CreateApplication.html
---

# CreateApplication
<a name="API_CreateApplication"></a>

Creates a new application. An application is the top-level organizational unit that supports IAM Identity Center integration.

## Request Syntax
<a name="API_CreateApplication_RequestSyntax"></a>

```
POST /CreateApplication HTTP/1.1
Content-type: application/json

{
   "defaultKmsKeyId": "{{string}}",
   "idcInstanceArn": "{{string}}",
   "roleArn": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateApplication_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateApplication_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [defaultKmsKeyId](#API_CreateApplication_RequestSyntax) **   <a name="securityagent-CreateApplication-request-defaultKmsKeyId"></a>
The identifier of the default AWS KMS key to use for encrypting data in the application.
Type: String
Required: No

 ** [idcInstanceArn](#API_CreateApplication_RequestSyntax) **   <a name="securityagent-CreateApplication-request-idcInstanceArn"></a>
The Amazon Resource Name (ARN) of the IAM Identity Center instance to associate with the application.
Type: String
Required: No

 ** [roleArn](#API_CreateApplication_RequestSyntax) **   <a name="securityagent-CreateApplication-request-roleArn"></a>
The Amazon Resource Name (ARN) of the IAM role to associate with the application.
Type: String
Required: No

 ** [tags](#API_CreateApplication_RequestSyntax) **   <a name="securityagent-CreateApplication-request-tags"></a>
The tags to associate with the application.
Type: String to string map
Required: No

## Response Syntax
<a name="API_CreateApplication_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "applicationId": "string"
}
```

## Response Elements
<a name="API_CreateApplication_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [applicationId](#API_CreateApplication_ResponseSyntax) **   <a name="securityagent-CreateApplication-response-applicationId"></a>
The unique identifier of the created application.
Type: String

## Errors
<a name="API_CreateApplication_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_CreateApplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityagent-2025-09-06/CreateApplication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityagent-2025-09-06/CreateApplication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/CreateApplication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityagent-2025-09-06/CreateApplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/CreateApplication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityagent-2025-09-06/CreateApplication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityagent-2025-09-06/CreateApplication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityagent-2025-09-06/CreateApplication)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/securityagent-2025-09-06/CreateApplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/CreateApplication)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
