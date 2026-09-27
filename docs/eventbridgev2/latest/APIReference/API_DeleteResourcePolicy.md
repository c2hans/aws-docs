---
source_url: https://docs.aws.amazon.com/eventbridgev2/latest/APIReference/API_DeleteResourcePolicy.html
---

# DeleteResourcePolicy
<a name="API_DeleteResourcePolicy"></a>

Deletes the named resource policy attached to an event bus.

## Request Parameters
<a name="API_DeleteResourcePolicy_RequestParameters"></a>

 ** ExpectedRevisionId **
The delete succeeds only if the named policy's current revision ID matches this value; if it differs or the policy does not exist, the operation fails with ConflictException. The "NO\_POLICY" sentinel is not valid here. When omitted, deleting an absent policy is an idempotent success. Supplying this value makes the delete non-idempotent: once it succeeds the expected revision no longer exists, so retrying an unanswered request fails with ConflictException even though the policy was deleted. To establish the outcome, read the policy back: ResourceNotFoundException means the delete took effect.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** PolicyName **
Which named policy to delete. Defaults to "default" when omitted (a delete AWS Resource Access Manager makes on the owner's behalf resolves to "AWS\_RAM" instead). The two writers are exclusive in both directions — only Resource Access Manager can delete "AWS\_RAM", and only the bus owner can delete "default" — so naming the other party's policy fails with AccessDeniedException. A well-formed name that is neither of the two fails with InvalidInputException.
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
<a name="API_DeleteResourcePolicy_ResponseElements"></a>

The following element is returned by the service.

 ** RevisionId **
Revision ID of the policy that was deleted. Absent when no policy was deleted.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

## Errors
<a name="API_DeleteResourcePolicy_Errors"></a>

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

 ** ResourceNotFoundException **
The resource does not exist.
HTTP Status Code: 404

 ** ThrottlingException **
The request was throttled because it exceeds a request rate limit. Retry the request with backoff.
HTTP Status Code: 429

## See Also
<a name="API_DeleteResourcePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eventbridgev2-2025-05-15/DeleteResourcePolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eventbridgev2-2025-05-15/DeleteResourcePolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridgev2-2025-05-15/DeleteResourcePolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eventbridgev2-2025-05-15/DeleteResourcePolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridgev2-2025-05-15/DeleteResourcePolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eventbridgev2-2025-05-15/DeleteResourcePolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eventbridgev2-2025-05-15/DeleteResourcePolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eventbridgev2-2025-05-15/DeleteResourcePolicy)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/eventbridgev2-2025-05-15/DeleteResourcePolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridgev2-2025-05-15/DeleteResourcePolicy)
