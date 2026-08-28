---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_DelegationRequest.html
---

# DelegationRequest
<a name="API_DelegationRequest"></a>

Contains information about a delegation request, including its status, permissions, and associated metadata.

## Contents
<a name="API_DelegationRequest_Contents"></a>

 ** ApproverId **
The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.
For more information about ARNs, go to [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference*.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

 ** CreateDate **
Creation date (timestamp) of this delegation request.
Type: Timestamp
Required: No

 ** DelegationRequestId **
The unique identifier for the delegation request.
Type: String
Length Constraints: Minimum length of 16. Maximum length of 128.
Pattern: `[\w-]+`
Required: No

 ** Description **
Description of the delegation request. This is a message that is provided by the AWS partner that filed the delegation request.
Type: String
Length Constraints: Maximum length of 1000.
Pattern: `[\u0009\u000A\u000D\u0020-\u007E\u00A1-\u00FF]*`
Required: No

 ** ExpirationTime **
The expiry time of this delegation request
See the [Understanding the Request Lifecycle](https://docs.aws.amazon.com/IAM/latest/UserGuide/temporary-delegation-building-integration.html#temporary-delegation-request-lifecycle) for details on the life time of a delegation request at each state.
Type: Timestamp
Required: No

 ** Notes **
Notes added to this delegation request, if this request was updated via the [UpdateDelegationRequest](https://docs.aws.amazon.com/IAM/latest/APIReference/API_UpdateDelegationRequest.html) API.
Type: String
Length Constraints: Maximum length of 500.
Pattern: `[\u0009\u000A\u000D\u0020-\u007E\u00A1-\u00FF]*`
Required: No

 ** OnlySendByOwner **
A flag indicating whether the [SendDelegationToken](https://docs.aws.amazon.com/IAM/latest/APIReference/API_SendDelegationToken.html) must be called by the owner of this delegation request. This is set by the requesting partner.
Type: Boolean
Required: No

 ** OwnerAccountId **
 AWS account ID of the owner of the delegation request.
Type: String
Pattern: `\d{12}`
Required: No

 ** OwnerId **
ARN of the owner of this delegation request.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^[a-zA-Z0-9:/+=,.@_-]+$`
Required: No

 ** PermissionPolicy **
JSON content of the associated permission policy of this delegation request.
Type: String
Required: No

 ** Permissions **
Contains information about the permissions being delegated in a delegation request.
Type: [DelegationPermission](API_DelegationPermission.md) object
Required: No

 ** RedirectUrl **
A URL to be redirected to once the delegation request is approved. Partners provide this URL when creating the delegation request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^http(s?)://[a-zA-Z0-9._/-]*(\?[a-zA-Z0-9._=&-]*)?(#[a-zA-Z0-9._/-]*)?$`
Required: No

 ** RejectionReason **
Reasons for rejecting this delegation request, if this request was rejected. See also [RejectDelegationRequest](https://docs.aws.amazon.com/IAM/latest/APIReference/API_RejectDelegationRequest.html) API documentation.
Type: String
Length Constraints: Maximum length of 500.
Pattern: `[\u0009\u000A\u000D\u0020-\u007E\u00A1-\u00FF]*`
Required: No

 ** RequestMessage **
A custom message that is added to the delegation request by the partner.
This element is different from the `Description` element such that this is a request specific message injected by the partner. The `Description` is typically a generic explanation of what the delegation request is targeted to do.
Type: String
Length Constraints: Maximum length of 200.
Pattern: `[\u0009\u000A\u000D\u0020-\u007E\u00A1-\u00FF]*`
Required: No

 ** RequestorId **
Identity of the requestor of this delegation request. This will be an AWS account ID.
Type: String
Pattern: `\d{12}`
Required: No

 ** RequestorName **
A friendly name of the requestor.
Type: String
Length Constraints: Maximum length of 30.
Pattern: `[\u0009\u000A\u000D\u0020-\u007E\u00A1-\u00FF]*`
Required: No

 ** RolePermissionRestrictionArns.member.N **
If the `PermissionPolicy` includes role creation permissions, this element will include the list of permissions boundary policies associated with the role creation. See [Permissions boundaries for IAM entities](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html) for more details about IAM permission boundaries.
Type: Array of strings
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

 ** SessionDuration **
The life-time of the requested session credential.
Type: Integer
Valid Range: Minimum value of 300. Maximum value of 43200.
Required: No

 ** State **
The state of this delegation request.
See the [Understanding the Request Lifecycle](https://docs.aws.amazon.com/IAM/latest/UserGuide/temporary-delegation-building-integration.html#temporary-delegation-request-lifecycle) for an explanation of how these states are transitioned.
Type: String
Valid Values: `UNASSIGNED | ASSIGNED | PENDING_APPROVAL | FINALIZED | ACCEPTED | REJECTED | EXPIRED`
Required: No

 ** UpdatedTime **
Last updated timestamp of the request.
Type: Timestamp
Required: No

## See Also
<a name="API_DelegationRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/DelegationRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/DelegationRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/DelegationRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Identity and Access Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query IAM` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
