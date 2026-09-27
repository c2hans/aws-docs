---
source_url: https://docs.aws.amazon.com/eventbridgev2/latest/APIReference/API_PutResourcePolicy.html
---

# PutResourcePolicy
<a name="API_PutResourcePolicy"></a>

Attaches a named resource policy to an event bus — the only resource type that supports policies; other resource ARNs are rejected. Each bus holds two named policies: "default" (customer-managed, full IAM policy language including Deny) and "AWS\_RAM" (written exclusively by AWS Resource Access Manager to reflect resource shares). Both policies are evaluated on cross-account authorization; an explicit Deny in either overrides an Allow in the other. Operations that omit PolicyName target "default". A "default" policy that would grant public access is rejected with PublicPolicyException and is not attached; this check is always on and cannot be disabled.

## Request Parameters
<a name="API_PutResourcePolicy_RequestParameters"></a>

 ** ExpectedRevisionId **
The write succeeds only if the named policy's current revision ID matches this value; a policy that does not exist yet matches only the sentinel "NO\_POLICY" (create-only). On mismatch the operation fails with ConflictException. When omitted, the write is unconditional. Every attempt stores a newly generated revision ID, so retrying an unanswered request can conflict with the caller's own earlier attempt; read the policy back and compare it with the one you intended before treating a conflict as another writer's change.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** PolicyDocument **
A resource policy document, as a JSON string. The maximum size is 389,120 bytes of UTF-8; the byte limit is enforced by the service.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 389120.
Required: Yes

 ** PolicyName **
Which named policy to write. Defaults to "default", the customer-managed policy, when omitted (a write AWS Resource Access Manager makes on the owner's behalf resolves to "AWS\_RAM" instead). The two writers are exclusive in both directions — only Resource Access Manager can write "AWS\_RAM", and only the bus owner can write "default" — so naming the other party's policy fails with AccessDeniedException. A well-formed name that is neither of the two fails with InvalidInputException.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[A-Za-z0-9_]+`
Required: No

 ** ResourceArn **
The Amazon Resource Name (ARN) that uniquely identifies an event bus.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:aws(-[a-z0-9]+)*:events:[a-z][a-z0-9]*(-[a-z0-9]+)*:([0-9]{12}):event-busv2\/[A-Za-z0-9][\.\-_A-Za-z0-9]{0,255}\/[a-z0-9]{25}`
Required: Yes

## Response Elements
<a name="API_PutResourcePolicy_ResponseElements"></a>

The following elements are returned by the service.

 ** PolicyName **
Name of a policy attached to a resource. Valid values: "default" (the customer-managed policy) and "AWS\_RAM" (managed exclusively by AWS Resource Access Manager). Any other value is rejected.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[A-Za-z0-9_]+`

 ** ResourceArn **
The Amazon Resource Name (ARN) that uniquely identifies an event bus.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:aws(-[a-z0-9]+)*:events:[a-z][a-z0-9]*(-[a-z0-9]+)*:([0-9]{12}):event-busv2\/[A-Za-z0-9][\.\-_A-Za-z0-9]{0,255}\/[a-z0-9]{25}`

 ** RevisionId **
Absent when the write removed the policy; a removal produces no new revision.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

## Errors
<a name="API_PutResourcePolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The caller does not have the permissions required to perform the operation. This error is also returned when the operation cannot use the AWS KMS key for the event bus.
HTTP Status Code: 403

 ** ConcurrentModificationException **
Another change to the resource is already in progress. Retry the request.
HTTP Status Code: 409

 ** ConflictException **
A client-supplied precondition (e.g. ExpectedRevisionId on a resource-policy write) did not match the current state of the resource. Retrying the same request will fail again; re-read the resource and re-evaluate before retrying.
A conditional request is not retry-safe on its own. If an earlier attempt committed but its response never reached the caller, retrying fails with this error, which is indistinguishable from another writer having won. Compare the resource's current contents with what the request intended: a successful attempt stores a revision ID the caller never saw, so the revision alone cannot tell the two apart, but matching contents mean the change took effect.
HTTP Status Code: 409

 ** InternalException **
The request failed because of an internal service error. Retry the request.
HTTP Status Code: 500

 ** InvalidInputException **
A request parameter is missing or not valid.
HTTP Status Code: 400

 ** PolicyLengthExceededException **
The policy document exceeds the maximum allowed size.
HTTP Status Code: 400

 ** PublicPolicyException **
The policy was rejected because it would grant public access to the event bus. A statement grants public access when its principal is a wildcard and no condition limits the callers to specific AWS accounts or principals. To fix it, replace the wildcard principal with specific principals, or add a condition that limits the callers to specific AWS accounts. Conditions on event content (events:source, events:detail-type, events:Metadata/\*) do not identify the caller and do not make a wildcard principal non-public. Returned only for the "default" policy; the "AWS\_RAM" policy is composed by AWS Resource Access Manager and never grants public access.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The resource does not exist.
HTTP Status Code: 404

 ** ThrottlingException **
The request was throttled because it exceeds a request rate limit. Retry the request with backoff.
HTTP Status Code: 429

## See Also
<a name="API_PutResourcePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eventbridgev2-2025-05-15/PutResourcePolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eventbridgev2-2025-05-15/PutResourcePolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridgev2-2025-05-15/PutResourcePolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eventbridgev2-2025-05-15/PutResourcePolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridgev2-2025-05-15/PutResourcePolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eventbridgev2-2025-05-15/PutResourcePolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eventbridgev2-2025-05-15/PutResourcePolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eventbridgev2-2025-05-15/PutResourcePolicy)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/eventbridgev2-2025-05-15/PutResourcePolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridgev2-2025-05-15/PutResourcePolicy)
