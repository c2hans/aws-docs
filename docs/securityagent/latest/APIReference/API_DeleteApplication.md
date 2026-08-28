---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_DeleteApplication.html
---

# DeleteApplication
<a name="API_DeleteApplication"></a>

Deletes an application and its associated configuration, including IAM Identity Center settings.

## Request Syntax
<a name="API_DeleteApplication_RequestSyntax"></a>

```
POST /DeleteApplication HTTP/1.1
Content-type: application/json

{
   "applicationId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DeleteApplication_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DeleteApplication_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [applicationId](#API_DeleteApplication_RequestSyntax) **   <a name="securityagent-DeleteApplication-request-applicationId"></a>
The unique identifier of the application to delete.
Type: String
Required: Yes

## Response Syntax
<a name="API_DeleteApplication_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteApplication_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteApplication_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_DeleteApplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityagent-2025-09-06/DeleteApplication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityagent-2025-09-06/DeleteApplication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/DeleteApplication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityagent-2025-09-06/DeleteApplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/DeleteApplication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityagent-2025-09-06/DeleteApplication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityagent-2025-09-06/DeleteApplication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityagent-2025-09-06/DeleteApplication)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/securityagent-2025-09-06/DeleteApplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/DeleteApplication)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
