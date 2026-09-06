---
source_url: https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_PutPermission.html
---

# PutPermission
<a name="API_PutPermission"></a>

 Adds permissions to a profiling group's resource-based policy that are provided using an action group. If a profiling group doesn't have a resource-based policy, one is created for it using the permissions in the action group and the roles and users in the `principals` parameter.

 The one supported action group that can be added is `agentPermission` which grants `ConfigureAgent` and `PostAgent` permissions. For more information, see [Resource-based policies in CodeGuru Profiler](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/resource-based-policies.html) in the *Amazon CodeGuru Profiler User Guide*, [`ConfigureAgent`](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ConfigureAgent.html), and [`PostAgentProfile`](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_PostAgentProfile.html).

 The first time you call `PutPermission` on a profiling group, do not specify a `revisionId` because it doesn't have a resource-based policy. Subsequent calls must provide a `revisionId` to specify which revision of the resource-based policy to add the permissions to.

 The response contains the profiling group's JSON-formatted resource policy.

## Request Syntax
<a name="API_PutPermission_RequestSyntax"></a>

```
PUT /profilingGroups/{{profilingGroupName}}/policy/{{actionGroup}} HTTP/1.1
Content-type: application/json

{
   "principals": [ "{{string}}" ],
   "revisionId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_PutPermission_RequestParameters"></a>

The request uses the following URI parameters.

 ** [actionGroup](#API_PutPermission_RequestSyntax) **   <a name="profiler-PutPermission-request-uri-actionGroup"></a>
 Specifies an action group that contains permissions to add to a profiling group resource. One action group is supported, `agentPermissions`, which grants permission to perform actions required by the profiling agent, `ConfigureAgent` and `PostAgentProfile` permissions.
Valid Values: `agentPermissions`
Required: Yes

 ** [profilingGroupName](#API_PutPermission_RequestSyntax) **   <a name="profiler-PutPermission-request-uri-profilingGroupName"></a>
The name of the profiling group to grant access to.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\w-]+`
Required: Yes

## Request Body
<a name="API_PutPermission_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [principals](#API_PutPermission_RequestSyntax) **   <a name="profiler-PutPermission-request-principals"></a>
 A list ARNs for the roles and users you want to grant access to the profiling group. Wildcards are not are supported in the ARNs.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: Yes

 ** [revisionId](#API_PutPermission_RequestSyntax) **   <a name="profiler-PutPermission-request-revisionId"></a>
 A universally unique identifier (UUID) for the revision of the policy you are adding to the profiling group. Do not specify this when you add permissions to a profiling group for the first time. If a policy already exists on the profiling group, you must specify the `revisionId`.
Type: String
Pattern: `.*[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}.*`
Required: No

## Response Syntax
<a name="API_PutPermission_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "policy": "string",
   "revisionId": "string"
}
```

## Response Elements
<a name="API_PutPermission_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [policy](#API_PutPermission_ResponseSyntax) **   <a name="profiler-PutPermission-response-policy"></a>
 The JSON-formatted resource-based policy on the profiling group that includes the added permissions.
Type: String

 ** [revisionId](#API_PutPermission_ResponseSyntax) **   <a name="profiler-PutPermission-response-revisionId"></a>
 A universally unique identifier (UUID) for the revision of the resource-based policy that includes the added permissions. The JSON-formatted policy is in the `policy` element of the response.
Type: String
Pattern: `.*[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}.*`

## Errors
<a name="API_PutPermission_Errors"></a>

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
<a name="API_PutPermission_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codeguruprofiler-2019-07-18/PutPermission)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codeguruprofiler-2019-07-18/PutPermission)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeguruprofiler-2019-07-18/PutPermission)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codeguruprofiler-2019-07-18/PutPermission)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeguruprofiler-2019-07-18/PutPermission)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codeguruprofiler-2019-07-18/PutPermission)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codeguruprofiler-2019-07-18/PutPermission)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codeguruprofiler-2019-07-18/PutPermission)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codeguruprofiler-2019-07-18/PutPermission)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeguruprofiler-2019-07-18/PutPermission)
