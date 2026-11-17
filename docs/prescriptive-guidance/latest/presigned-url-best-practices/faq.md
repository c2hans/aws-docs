---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/presigned-url-best-practices/faq.html
---

# FAQ
<a name="faq"></a>

## Can a presigned request be used multiple times? Is that a security risk?
<a name="can-a-presigned-request-be-used-multiple-times--is-that-a-security-risk-.1c00d6ea-f0b5-592e-9f67-48e86af7e169"></a>

Yes, a signature in a presigned request could be used more than once. Whether this is a security risk is a contextual question. Other methods of accessing AWS services allow repetition as well. A user or workload with AWS credentials can send many requests to AWS services, and any of those requests could be duplicates.

If your use case requires a request to run only once, implement other mechanisms to enforce single use. Presigned requests don't provide a single-use feature. Review your use cases and implementations. In many cases, multiple use is acceptable.

## Can someone other than the intended user use a presigned request?
<a name="can-someone-other-than-the-intended-user-use-a-presigned-request-.82b83e07-0824-506a-a6d1-a092df77fe63"></a>

A signature in a presigned request can be sent by anyone in possession of it. It will be accepted only if it passes other forms of validation, such as [data perimeter controls](https://docs.aws.amazon.com/whitepapers/latest/building-a-data-perimeter-on-aws/building-a-data-perimeter-on-aws.html). If the signature has expired, the signing credentials have expired, or the signing credentials don't have access to the requested resources, the request will be denied.

The same is true for other methods of authenticating with AWS services. Sharing credentials with unintended parties can result in unauthorized access. A core best practice is to share credentials and signatures only with the intended audience. If you can't trust your intended audience to keep private data secure and not share it with others, any form of authentication is undermined.

## Can an authorized user use a presigned request to exfiltrate data?
<a name="can-an-authorized-user-use-a-presigned-request-to-exfiltrate-data-.f518db72-d722-5c8e-b487-0b57388fc46c"></a>

Enabling access for intended purposes while maintaining a data perimeter requires a comprehensive approach. [Least-privilege access](https://docs.aws.amazon.com/wellarchitected/latest/framework/sec_permissions_least_privileges.html), [data perimeter controls](https://docs.aws.amazon.com/whitepapers/latest/building-a-data-perimeter-on-aws/building-a-data-perimeter-on-aws.html), and [using only temporary access credentials](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_identities_unique.html) are general best practices that apply to securing data. Implementing these controls also limits the ability of users to perform actions through the presigned requests they generate.

This is because the access provided by a presigned request is a subset of the access granted to the credentials that sign the request. In this context, best practices that apply to accessing data also apply to presigned requests, but presigned requests create no new access to data.
+ The maximum expiration is limited to the expiration of the signing credentials. If the signing credentials are revoked, signatures based upon the credentials are no longer valid.
+ If the permissions for the IAM principal that is associated with the signing credentials don't allow the action associated with the presigned request, invoking the presigned request results in an "access denied" response. The response depends on the current state of permissions at the time of invocation, regardless of when the presigned request's signature was generated.
+ [Properties of the principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-principal-properties) are evaluated based upon the principal that is associated with the signing credentials.
+ [Properties of a role session](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-role-session-properties) are evaluated based on the role session that is associated with the signing credentials.
+ [Properties of the network](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-network-properties) are evaluated based upon how the request was received, as with normal requests.

In this context, focus your risk examination on cases where credentials that differ from the user's credentials sign the presigned request and provide access that isn't part of the user's principal permissions.  Apply this examination to the design of the service, workload, or solution that generates signatures on a user's behalf, instead of the presigned request capability itself.

## Can I deny access from a presigned URL if I suspect it's been shared in an unauthorized way?
<a name="can-i-deny-access-from-a-presigned-url-if-i-suspect-it-s-been-shared-in-an-unauthorized-way-.52176953-ccc6-5d4e-92cc-2a6971581635"></a>

Yes. This requires invalidating the credentials the URL was signed with. There are multiple ways to accomplish this:
+ Remove permissions from the IAM principal the credentials belong to. If that IAM principal no longer has access to the resource and operation that the URL is signed for, the URL can't run that operation. This affects all matching use from that IAM principal.
+ If the credentials used to sign the URL are temporary AWS STS credentials, you can [revoke the session permissions for temporary credentials that were issued before a specific time](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_revoke-sessions.html#revoke-session-policy) for the IAM principal. Depending on the use case, there might be other valid sessions that become invalidated before their normal expiration time, but new sessions won't be affected. Revoking session permissions also invalidates any URLs that were signed by using credentials associated with those sessions, but new URLs associated with new sessions won't be affected.
+ If the credentials used to sign the URL are permanent credentials, [deactivate](https://docs.aws.amazon.com/cli/latest/reference/iam/update-access-key.html) the access key. This affects all usage tied to those credentials.
