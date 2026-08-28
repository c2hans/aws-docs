---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_BatchDeleteThreatModels.html
---

# BatchDeleteThreatModels
<a name="API_BatchDeleteThreatModels"></a>

Deletes one or more threat models from an agent space.

## Request Syntax
<a name="API_BatchDeleteThreatModels_RequestSyntax"></a>

```
POST /BatchDeleteThreatModels HTTP/1.1
Content-type: application/json

{
   "agentSpaceId": "{{string}}",
   "threatModelIds": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_BatchDeleteThreatModels_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_BatchDeleteThreatModels_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [agentSpaceId](#API_BatchDeleteThreatModels_RequestSyntax) **   <a name="securityagent-BatchDeleteThreatModels-request-agentSpaceId"></a>
The unique identifier of the agent space that contains the threat models to delete.
Type: String
Required: Yes

 ** [threatModelIds](#API_BatchDeleteThreatModels_RequestSyntax) **   <a name="securityagent-BatchDeleteThreatModels-request-threatModelIds"></a>
The list of threat model identifiers to delete.
Type: Array of strings
Required: Yes

## Response Syntax
<a name="API_BatchDeleteThreatModels_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "deleted": [ "string" ],
   "failed": [
      {
         "reason": "string",
         "threatModelId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_BatchDeleteThreatModels_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [deleted](#API_BatchDeleteThreatModels_ResponseSyntax) **   <a name="securityagent-BatchDeleteThreatModels-response-deleted"></a>
The list of threat model identifiers that were successfully deleted.
Type: Array of strings

 ** [failed](#API_BatchDeleteThreatModels_ResponseSyntax) **   <a name="securityagent-BatchDeleteThreatModels-response-failed"></a>
The list of threat models that failed to delete, including the reason for each failure.
Type: Array of [DeleteThreatModelFailure](API_DeleteThreatModelFailure.md) objects

## Errors
<a name="API_BatchDeleteThreatModels_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_BatchDeleteThreatModels_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityagent-2025-09-06/BatchDeleteThreatModels)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityagent-2025-09-06/BatchDeleteThreatModels)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/BatchDeleteThreatModels)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityagent-2025-09-06/BatchDeleteThreatModels)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/BatchDeleteThreatModels)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityagent-2025-09-06/BatchDeleteThreatModels)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityagent-2025-09-06/BatchDeleteThreatModels)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityagent-2025-09-06/BatchDeleteThreatModels)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/securityagent-2025-09-06/BatchDeleteThreatModels)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/BatchDeleteThreatModels)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
