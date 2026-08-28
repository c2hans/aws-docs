---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_ListPrivateConnections.html
---

# ListPrivateConnections
<a name="API_ListPrivateConnections"></a>

Lists all Private Connections in the caller's account.

## Request Syntax
<a name="API_ListPrivateConnections_RequestSyntax"></a>

```
GET /v1/private-connections HTTP/1.1
```

## URI Request Parameters
<a name="API_ListPrivateConnections_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListPrivateConnections_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListPrivateConnections_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "privateConnections": [
      {
         "certificateExpiryTime": "string",
         "dnsResolution": "string",
         "failureMessage": "string",
         "hostAddress": "string",
         "name": "string",
         "resourceConfigurationId": "string",
         "resourceGatewayId": "string",
         "status": "string",
         "type": "string",
         "vpcId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListPrivateConnections_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [privateConnections](#API_ListPrivateConnections_ResponseSyntax) **   <a name="devopsagent-ListPrivateConnections-response-privateConnections"></a>
The list of Private Connections.
Type: Array of [PrivateConnectionSummary](API_PrivateConnectionSummary.md) objects

## Errors
<a name="API_ListPrivateConnections_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to the requested resource is denied due to insufficient permissions.
 ** message **
Detailed error message describing why access was denied.
HTTP Status Code: 403

 ** ConflictException **
The request conflicts with the current state of the resource.
 ** message **
Detailed error message describing the conflict.
HTTP Status Code: 409

 ** ContentSizeExceededException **
This exception is thrown when the content size exceeds the allowed limit.
HTTP Status Code: 413

 ** InternalServerException **
This exception is thrown when an unexpected error occurs in the processing of a request.
HTTP Status Code: 500

 ** InvalidParameterException **
One or more parameters provided in the request are invalid.
 ** message **
Detailed error message describing which parameter is invalid and why.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The requested resource could not be found.
 ** message **
Detailed error message describing which resource was not found.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The request would exceed the service quota limit.
 ** message **
Detailed error message describing which quota was exceeded.
HTTP Status Code: 402

 ** ThrottlingException **
The request was throttled due to too many requests. Please slow down and try again.
 ** message **
Detailed error message describing the throttling condition.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by the service.
 ** fieldList **
A list of specific failures encountered while validating the input. A member can appear in this list more than once if it failed to satisfy multiple constraints.
 ** message **
A summary of the validation failure.
HTTP Status Code: 400

## See Also
<a name="API_ListPrivateConnections_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/devops-agent-2026-01-01/ListPrivateConnections)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/devops-agent-2026-01-01/ListPrivateConnections)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/ListPrivateConnections)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/devops-agent-2026-01-01/ListPrivateConnections)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/ListPrivateConnections)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/devops-agent-2026-01-01/ListPrivateConnections)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/devops-agent-2026-01-01/ListPrivateConnections)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/devops-agent-2026-01-01/ListPrivateConnections)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/devops-agent-2026-01-01/ListPrivateConnections)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/ListPrivateConnections)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS DevOps Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devopsagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
