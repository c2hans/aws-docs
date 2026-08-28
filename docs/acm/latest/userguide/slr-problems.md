---
source_url: https://docs.aws.amazon.com/acm/latest/userguide/slr-problems.html
---

# Problems with the ACM service-linked role (SLR)
<a name="slr-problems"></a>

When you issue a certificate signed by a private CA that has been shared with you by another account, ACM attempts on first use to set up a service-linked role (SLR) to interact as a principal with an AWS Private CA [resource-based access policy](https://docs.aws.amazon.com/privateca/latest/userguide/pca-resource-sharing.html#pca-rbp). If you issue a private certificate from a shared CA and the SLR is not in place, ACM will be unable to automatically renew that certificate for you.

ACM might alert you that it cannot determine whether an SLR exists on your account. If the required `iam:GetRole` permission has already been granted to the ACM SLR for your account, then the alert will not recur after the SLR is created. If it does recur, then you or your account administrator might need to grant the `iam:GetRole` permission to ACM, or associate your account with the ACM-managed policy `AWSCertificateManagerFullAccess`.

For more information, see [Service-Linked Role Permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#service-linked-role-permissions) in the *IAM User Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Certificate Manager (ACM). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query acm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
