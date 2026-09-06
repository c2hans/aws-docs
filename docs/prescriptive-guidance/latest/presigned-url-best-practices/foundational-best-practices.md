---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/presigned-url-best-practices/foundational-best-practices.html
---

# Foundational best practices
<a name="foundational-best-practices"></a>

General best practices that are effective controls for other AWS API requests apply to presigned requests as well. This section reviews two of the most relevant practices: least privilege and data perimeters. These practices create a depth of controls that other practices extend.

## Apply the principle of least privilege
<a name="least-privilege"></a>

The first step in limiting the use of presigned requests is limiting access to Amazon S3 in general. A presigned URL cannot provide access to resources that weren't granted to the principal that generated the signature for the presigned URL. Nor can it provide access to a resource in a way that wasn't granted to that principal. As such, applying best practices to grant those principals least privilege is an effective guardrail.

The process of creating a presigned URL is an algorithmic operation that's based on a published standard (Signature Version 4) for signature generation. Therefore, it's not possible to place limits on the generation of presigned URLs. However, to be relevant, a presigned URL must be valid and provide access to resources, so the validity of a presigned URL is also an effective guardrail.

For more information about least privilege, see [Grant least privilege access](https://docs.aws.amazon.com/wellarchitected/latest/framework/sec_permissions_least_privileges.html) in the AWS Well-Architected Framework, Security pillar.

## Implement a data perimeter
<a name="data-perimeters"></a>

An extension of least privilege is to maintain a [data perimeter](https://docs.aws.amazon.com/whitepapers/latest/building-a-data-perimeter-on-aws/building-a-data-perimeter-on-aws.html) that's consistent your organization's needs. Presigned URLs are compatible with data perimeters. As with other requests, a presigned URL request's validity is evaluated at request time. If the [properties of the network, resource, role-session, and principal ](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html)change, they are evaluated at the time and by using the method by which a request is received.

For example, let's say that a service that's running in an Amazon Elastic Kubernetes Service (Amazon EKS) container signs a request. The request is later sent from a user's personal computer system that's connected to the internet. In this case, the [aws:SourceIp condition](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-sourceip) evaluates the visible public IP address of the request from the the user's personal system, not the IP address of the service in the Amazon EKS container.

Similarly, if the tags of the principal or resource change before the request is sent, the updated, not original, values will apply to the request through the [aws:PrincipalTag/tag-key](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-principaltag) and [aws:ResourceTag/tag-key](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag) conditions.
