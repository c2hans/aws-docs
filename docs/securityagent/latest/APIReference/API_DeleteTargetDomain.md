---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_DeleteTargetDomain.html
---

# DeleteTargetDomain
<a name="API_DeleteTargetDomain"></a>

Deletes a target domain registration. After deletion, the domain can no longer be used for penetration testing.

## Request Syntax
<a name="API_DeleteTargetDomain_RequestSyntax"></a>

```
POST /DeleteTargetDomain HTTP/1.1
Content-type: application/json

{
   "targetDomainId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DeleteTargetDomain_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DeleteTargetDomain_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [targetDomainId](#API_DeleteTargetDomain_RequestSyntax) **   <a name="securityagent-DeleteTargetDomain-request-targetDomainId"></a>
The unique identifier of the target domain to delete.
Type: String
Required: Yes

## Response Syntax
<a name="API_DeleteTargetDomain_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "targetDomainId": "string"
}
```

## Response Elements
<a name="API_DeleteTargetDomain_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [targetDomainId](#API_DeleteTargetDomain_ResponseSyntax) **   <a name="securityagent-DeleteTargetDomain-response-targetDomainId"></a>
The unique identifier of the deleted target domain.
Type: String

## Errors
<a name="API_DeleteTargetDomain_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_DeleteTargetDomain_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityagent-2025-09-06/DeleteTargetDomain)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityagent-2025-09-06/DeleteTargetDomain)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/DeleteTargetDomain)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityagent-2025-09-06/DeleteTargetDomain)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/DeleteTargetDomain)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityagent-2025-09-06/DeleteTargetDomain)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityagent-2025-09-06/DeleteTargetDomain)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityagent-2025-09-06/DeleteTargetDomain)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/securityagent-2025-09-06/DeleteTargetDomain)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/DeleteTargetDomain)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
