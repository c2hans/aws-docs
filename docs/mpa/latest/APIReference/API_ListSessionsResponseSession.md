---
source_url: https://docs.aws.amazon.com/mpa/latest/APIReference/API_ListSessionsResponseSession.html
---

# ListSessionsResponseSession
<a name="API_ListSessionsResponseSession"></a>

Contains details for an approval session. For more information, see [Session](https://docs.aws.amazon.com/mpa/latest/userguide/mpa-health.html) in the *Multi-party approval User Guide*

## Contents
<a name="API_ListSessionsResponseSession_Contents"></a>

 ** ActionCompletionStrategy **   <a name="mpa-Type-ListSessionsResponseSession-ActionCompletionStrategy"></a>
Strategy for executing the protected operation. `AUTO_COMPLETION_UPON_APPROVAL` means the operation is executed automatically using the requester's permissions, if approved.
Type: String
Valid Values: `AUTO_COMPLETION_UPON_APPROVAL`
Required: No

 ** ActionName **   <a name="mpa-Type-ListSessionsResponseSession-ActionName"></a>
Name of the protected operation.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: No

 ** AdditionalSecurityRequirements **   <a name="mpa-Type-ListSessionsResponseSession-AdditionalSecurityRequirements"></a>
A list of `AdditionalSecurityRequirement` applied to the session.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Valid Values: `APPROVER_VERIFICATION_REQUIRED`
Required: No

 ** ApprovalTeamArn **   <a name="mpa-Type-ListSessionsResponseSession-ApprovalTeamArn"></a>
Amazon Resource Name (ARN) for the approval team.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws(-[^:]+)?:mpa:[a-z0-9-]{1,20}:[0-9]{12}:approval-team/[a-zA-Z0-9._-]+`
Required: No

 ** ApprovalTeamName **   <a name="mpa-Type-ListSessionsResponseSession-ApprovalTeamName"></a>
Name of the approval team.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `[a-zA-Z0-9._-]+`
Required: No

 ** CompletionTime **   <a name="mpa-Type-ListSessionsResponseSession-CompletionTime"></a>
Timestamp when the session was completed.
Type: Timestamp
Required: No

 ** Description **   <a name="mpa-Type-ListSessionsResponseSession-Description"></a>
Description for the team.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** ExpirationTime **   <a name="mpa-Type-ListSessionsResponseSession-ExpirationTime"></a>
Timestamp when the session was expire.
Type: Timestamp
Required: No

 ** InitiationTime **   <a name="mpa-Type-ListSessionsResponseSession-InitiationTime"></a>
Timestamp when the session was initiated.
Type: Timestamp
Required: No

 ** ProtectedResourceArn **   <a name="mpa-Type-ListSessionsResponseSession-ProtectedResourceArn"></a>
Amazon Resource Name (ARN) for the protected operation.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Required: No

 ** RequesterAccountId **   <a name="mpa-Type-ListSessionsResponseSession-RequesterAccountId"></a>
ID for the account that made the operation request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 12.
Pattern: `\d{12}`
Required: No

 ** RequesterPrincipalArn **   <a name="mpa-Type-ListSessionsResponseSession-RequesterPrincipalArn"></a>
 [IAM principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/intro-structure.html#intro-structure-request) that made the operation request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Required: No

 ** RequesterRegion **   <a name="mpa-Type-ListSessionsResponseSession-RequesterRegion"></a>
 AWS Region where the operation request originated.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Required: No

 ** RequesterServicePrincipal **   <a name="mpa-Type-ListSessionsResponseSession-RequesterServicePrincipal"></a>
 [Service principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html#principal-services) for the service associated with the protected operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** SessionArn **   <a name="mpa-Type-ListSessionsResponseSession-SessionArn"></a>
Amazon Resource Name (ARN) for the session.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws(-[^:]+)?:mpa:[a-z0-9-]{1,20}:[0-9]{12}:session/[a-zA-Z0-9._-]+/[a-zA-Z0-9_-]+`
Required: No

 ** Status **   <a name="mpa-Type-ListSessionsResponseSession-Status"></a>
Status for the protected operation. For example, if the operation is `PENDING`.
Type: String
Valid Values: `PENDING | CANCELLED | APPROVED | FAILED | CREATING`
Required: No

 ** StatusCode **   <a name="mpa-Type-ListSessionsResponseSession-StatusCode"></a>
Status code of the session.
Type: String
Valid Values: `REJECTED | EXPIRED | CONFIGURATION_CHANGED | ALL_APPROVERS_IN_SESSION`
Required: No

 ** StatusMessage **   <a name="mpa-Type-ListSessionsResponseSession-StatusMessage"></a>
Message describing the status for session.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: No

## See Also
<a name="API_ListSessionsResponseSession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mpa-2022-07-26/ListSessionsResponseSession)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mpa-2022-07-26/ListSessionsResponseSession)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mpa-2022-07-26/ListSessionsResponseSession)
