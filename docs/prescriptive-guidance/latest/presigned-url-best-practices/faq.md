---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/presigned-url-best-practices/faq.html
---

# FAQ
<a name="faq"></a>

## Can a presigned request be used multiple times? Is that a security risk?
<a name="can-a-presigned-request-be-used-multiple-times--is-that-a-security-risk-.7c081cba-afc8-535a-bf62-8944f4fb0a28"></a>

Yes, a signature in a presigned request could be used more than once. Whether this is a security risk is a contextual question. Other methods of accessing AWS services allow repetition as well. A user or workload with AWS credentials can send many requests to AWS services, and any of those requests could be duplicates.

If your use case requires once and only once execution, you should implement other mechanisms to enforce single use. Single use is not a feature of presigned requests. As a security engineer, you should review the use cases and implementations, but in many cases, multiple use will fit acceptable use.

## Can someone other than the intended user use a presigned request?
<a name="can-someone-other-than-the-intended-user-use-a-presigned-request-.d6c9762e-b148-5661-b55a-070a3dcd5f74"></a>

A signature in a presigned request can be sent by anyone in possession of it. It will be accepted only if it passes other forms of validation, such as [data perimeter controls](https://docs.aws.amazon.com/whitepapers/latest/building-a-data-perimeter-on-aws/building-a-data-perimeter-on-aws.html). If the signature has expired, the signing credentials have expired, or the signing credentials don't have access to the requested resources, the request will be denied.

The same is true for other methods of authenticating with AWS services. Credentials that are shared inappropriately allow inappropriate access. The core best practice is to share credentials and signatures only with the intended audience. If you can't trust your intended audience to keep private data secure and not share it with others, this will undermine any form of authentication.

## Can an authorized user use a presigned request to exfiltrate data?
<a name="can-an-authorized-user-use-a-presigned-request-to-exfiltrate-data-.64edbe1f-aeb3-51b8-8021-f77405e00a45"></a>

Securing data requires robust action. Enabling access for intended purposes while maintaining a data perimeter requires a comprehensive approach. [Least-privilege access](https://docs.aws.amazon.com/wellarchitected/latest/framework/sec_permissions_least_privileges.html), [data perimeter controls](https://docs.aws.amazon.com/whitepapers/latest/building-a-data-perimeter-on-aws/building-a-data-perimeter-on-aws.html), and [using only temporary access credentials](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_identities_unique.html) are general best practices that apply to securing data. The appropriate use of these controls also limits the ability of users to perform actions through the presigned requests they generate.

This is because the access provided by a presigned requests is a subset of the access granted to the credentials that are used to sign the request. In this context, best practices that apply to accessing data generally do apply to presigned requests, but presigned requests create no new access to data.
+ The maximum expiration is limited to the expiration of the signing credentials. If the signing credentials are revoked, signatures based upon the credentials are no longer valid.
+ If the permissions for the IAM principal that is associated with the signing credentials do not include the execution of the action associated with the presigned request, invoking a presigned request results in an "access denied" response. The response depends on the current state of permissions at the time of invocation, which has no relationship to the time that the presigned request's signature was generated.
+ [Properties of the principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-principal-properties) are evaluated based upon the principal that is associated with the signing credentials.
+ [Properties of a role session](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-role-session-properties) are evaluated based on the role session that is associated with the signing credentials.
+ [Properties of the network](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-network-properties) are evaluated based upon how the request was received, as with normal requests.

In this context, the examination of risks associated with presigned requests is constrained to areas where they are signed with credentials that are different from the user's credentials and provide access that was not part of a user's principal.  This examination should be applied to the design of the service, the workload, or the solution that generates signatures on a user's behalf, instead of the presigned request capability itself.

## Can I deny access from a presigned URL if I suspect it's been shared in an unauthorized way?
<a name="can-i-deny-access-from-a-presigned-url-if-i-suspect-it9999999999999999apos-s-been-shared-in-an-unauthorized-way-.e00afcde-41bb-5ca3-a776-4d986c090b36"></a>

Yes. This requires invalidating the credentials the URL was signed with. There are multiple ways to accomplish this:
+ Remove permissions from the IAM principal the credentials belong to. If that IAM principal no longer has access to the resource and operation that the URL is signed for, the URL can't execute that operation. This affects all matching use from that IAM principal.
+ If the credentials used to sign the URL are temporary AWS STS credentials, you can [revoke the session permissions for temporary credentials that were issued before a specific time](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_revoke-sessions.html#revoke-session-policy) for the IAM principal. Depending on the use case, there might be other valid sessions that become invalidated before their normal expiration time, but new sessions won't be affected. Revoking session permissions also invalidates any URLs that were signed by using credentials associated with those sessions, but new URLs associated with new sessions won't be affected.
+ If the credentials used to sign the URL are permanent credentials, [deactivate](https://docs.aws.amazon.com/cli/latest/reference/iam/update-access-key.html) the access key. This affects all usage tied to those credentials.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
