---
source_url: https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_RemovePermission.html
---

# RemovePermission
<a name="API_RemovePermission"></a>

 Removes permissions from a profiling group's resource-based policy that are provided using an action group. The one supported action group that can be removed is `agentPermission` which grants `ConfigureAgent` and `PostAgent` permissions. For more information, see [Resource-based policies in CodeGuru Profiler](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/resource-based-policies.html) in the *Amazon CodeGuru Profiler User Guide*, [https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ConfigureAgent.html](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ConfigureAgent.html), and [https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_PostAgentProfile.html](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_PostAgentProfile.html).

## Request Syntax
<a name="API_RemovePermission_RequestSyntax"></a>

```
DELETE /profilingGroups/{{profilingGroupName}}/policy/{{actionGroup}}?revisionId={{revisionId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_RemovePermission_RequestParameters"></a>

The request uses the following URI parameters.

 ** [actionGroup](#API_RemovePermission_RequestSyntax) **   <a name="profiler-RemovePermission-request-uri-actionGroup"></a>
 Specifies an action group that contains the permissions to remove from a profiling group's resource-based policy. One action group is supported, `agentPermissions`, which grants `ConfigureAgent` and `PostAgentProfile` permissions.
Valid Values: `agentPermissions`
Required: Yes

 ** [profilingGroupName](#API_RemovePermission_RequestSyntax) **   <a name="profiler-RemovePermission-request-uri-profilingGroupName"></a>
The name of the profiling group.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\w-]+`
Required: Yes

 ** [revisionId](#API_RemovePermission_RequestSyntax) **   <a name="profiler-RemovePermission-request-uri-revisionId"></a>
 A universally unique identifier (UUID) for the revision of the resource-based policy from which you want to remove permissions.
Pattern: `.*[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}.*`
Required: Yes

## Request Body
<a name="API_RemovePermission_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_RemovePermission_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "policy": "string",
   "revisionId": "string"
}
```

## Response Elements
<a name="API_RemovePermission_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [policy](#API_RemovePermission_ResponseSyntax) **   <a name="profiler-RemovePermission-response-policy"></a>
 The JSON-formatted resource-based policy on the profiling group after the specified permissions were removed.
Type: String

 ** [revisionId](#API_RemovePermission_ResponseSyntax) **   <a name="profiler-RemovePermission-response-revisionId"></a>
 A universally unique identifier (UUID) for the revision of the resource-based policy after the specified permissions were removed. The updated JSON-formatted policy is in the `policy` element of the response.
Type: String
Pattern: `.*[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}.*`

## Errors
<a name="API_RemovePermission_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request.
HTTP Status Code: 409

 ** InternalServerException **
The server encountered an internal error and is unable to complete the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource specified in the request does not exist.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The parameter is not valid.
HTTP Status Code: 400

## See Also
<a name="API_RemovePermission_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codeguruprofiler-2019-07-18/RemovePermission)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codeguruprofiler-2019-07-18/RemovePermission)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeguruprofiler-2019-07-18/RemovePermission)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codeguruprofiler-2019-07-18/RemovePermission)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeguruprofiler-2019-07-18/RemovePermission)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codeguruprofiler-2019-07-18/RemovePermission)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codeguruprofiler-2019-07-18/RemovePermission)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codeguruprofiler-2019-07-18/RemovePermission)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codeguruprofiler-2019-07-18/RemovePermission)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeguruprofiler-2019-07-18/RemovePermission)
