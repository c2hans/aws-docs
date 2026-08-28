---
source_url: https://docs.aws.amazon.com/tnb/latest/APIReference/API_DeleteSolNetworkInstance.html
---

# DeleteSolNetworkInstance
<a name="API_DeleteSolNetworkInstance"></a>

Deletes a network instance.

A network instance is a single network created in AWS TNB that can be deployed and on which life-cycle operations (like terminate, update, and delete) can be performed.

To delete a network instance, the instance must be in a stopped or terminated state. To terminate a network instance, see [TerminateSolNetworkInstance](https://docs.aws.amazon.com/tnb/latest/APIReference/API_TerminateSolNetworkInstance.html).

## Request Syntax
<a name="API_DeleteSolNetworkInstance_RequestSyntax"></a>

```
DELETE /sol/nslcm/v1/ns_instances/{{nsInstanceId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteSolNetworkInstance_RequestParameters"></a>

The request uses the following URI parameters.

 ** [nsInstanceId](#API_DeleteSolNetworkInstance_RequestSyntax) **   <a name="TNB-DeleteSolNetworkInstance-request-uri-nsInstanceId"></a>
Network instance ID.
Pattern: `ni-[a-f0-9]{17}`
Required: Yes

## Request Body
<a name="API_DeleteSolNetworkInstance_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteSolNetworkInstance_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_DeleteSolNetworkInstance_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_DeleteSolNetworkInstance_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Insufficient permissions to make request.
HTTP Status Code: 403

 ** InternalServerException **
Unexpected error occurred. Problem on the server.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Request references a resource that doesn't exist.
HTTP Status Code: 404

 ** ThrottlingException **
Exception caused by throttling.
HTTP Status Code: 429

 ** ValidationException **
Unable to process the request because the client provided input failed to satisfy request constraints.
HTTP Status Code: 400

## See Also
<a name="API_DeleteSolNetworkInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/tnb-2008-10-21/DeleteSolNetworkInstance)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/tnb-2008-10-21/DeleteSolNetworkInstance)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/tnb-2008-10-21/DeleteSolNetworkInstance)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/tnb-2008-10-21/DeleteSolNetworkInstance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/tnb-2008-10-21/DeleteSolNetworkInstance)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/tnb-2008-10-21/DeleteSolNetworkInstance)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/tnb-2008-10-21/DeleteSolNetworkInstance)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/tnb-2008-10-21/DeleteSolNetworkInstance)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/tnb-2008-10-21/DeleteSolNetworkInstance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/tnb-2008-10-21/DeleteSolNetworkInstance)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Telco Network Builder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query tnb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
