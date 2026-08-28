---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/sec_permissions_share_securely_third_party.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SEC03-BP09 Share resources securely with a third party
<a name="sec_permissions_share_securely_third_party"></a>

 The security of your cloud environment doesn’t stop at your organization. Your organization might rely on a third party to manage a portion of your data. The permission management for the third-party managed system should follow the practice of just-in-time access using the principle of least privilege with temporary credentials. By working closely with a third party, you can reduce the scope of impact and risk of unintended access together.

 **Desired outcome:** Long-term AWS Identity and Access Management (IAM) credentials, IAM access keys, and secret keys that are associated with a user can be used by anyone as long as the credentials are valid and active. Using an IAM role and temporary credentials helps you improve your overall security stance by reducing the effort to maintain long-term credentials, including the management and operational overhead of those sensitive details. By using a universally unique identifier (UUID) for the external ID in the IAM trust policy, and keeping the IAM policies attached to the IAM role under your control, you can audit and verify that the access granted to the third party is not too permissive. For prescriptive guidance on analyzing externally shared resources, see [SEC03-BP07 Analyze public and cross-account access](sec_permissions_analyze_cross_account.md).

 **Common anti-patterns:**
+  Using the default IAM trust policy without any conditions.
+  Using long-term IAM credentials and access keys.
+  Reusing external IDs.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>

 You might want to allow sharing resources outside of AWS Organizations or grant a third party access to your account. For example, a third party might provide a monitoring solution that needs to access resources within your account. In those cases, create an IAM cross-account role with only the privileges needed by the third party. Additionally, define a trust policy using the [external ID condition](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user_externalid.html). When using an external ID, you or the third party can generate a unique ID for each customer, third party, or tenancy. The unique ID should not be controlled by anyone but you after it’s created. The third party must implement a process to relate the external ID to the customer in a secure, auditable, and reproduceable manner.

 You can also use [IAM Roles Anywhere](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html) to manage IAM roles for applications outside of AWS that use AWS APIs.

 If the third party no longer requires access to your environment, remove the role. Avoid providing long-term credentials to a third party. Maintain awareness of other AWS services that support sharing. For example, the AWS Well-Architected Tool allows [sharing a workload](https://docs.aws.amazon.com/wellarchitected/latest/userguide/workloads-sharing.html) with other AWS accounts, and [AWS Resource Access Manager](https://docs.aws.amazon.com/ram/latest/userguide/what-is.html) helps you securely share an AWS resource you own with other accounts.

 **Implementation steps**

1.  **Use cross-account roles to provide access to external accounts.**

    [Cross-account roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_third-party.html) reduce the amount of sensitive information that is stored by external accounts and third parties for servicing their customers. Cross-account roles allow you to grant access to AWS resources in your account securely to a third party, such as AWS Partners or other accounts in your organization, while maintaining the ability to manage and audit that access.

    The third party might be providing service to you from a hybrid infrastructure or alternatively pulling data into an offsite location. [IAM Roles Anywhere](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html) helps you allow third party workloads to securely interact with your AWS workloads and further reduce the need for long-term credentials.

    You should not use long-term credentials, or access keys associated with users, to provide external account access. Instead, use cross-account roles to provide the cross-account access.

1.  **Use an external ID with third parties.**

    Using an [external ID](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user_externalid.html) allows you to designate who can assume a role in an IAM trust policy. The trust policy can require that the user assuming the role assert the condition and target in which they are operating. It also provides a way for the account owner to permit the role to be assumed only under specific circumstances. The primary function of the external ID is to address and prevent the [confused deputy](https://aws.amazon.com/blogs/security/how-to-use-external-id-when-granting-access-to-your-aws-resources/) problem.

    Use an external ID if you are an AWS account owner and you have configured a role for a third party that accesses other AWS accounts in addition to yours, or when you are in the position of assuming roles on behalf of different customers. Work with your third party or AWS Partner to establish an external ID condition to include in IAM trust policy.

1.  **Use universally unique external IDs.**

    Implement a process that generates random unique value for an external ID, such as a universally unique identifier (UUID). A third party reusing external IDs across different customers does not address the confused deputy problem, because customer A might be able to view data of customer B by using the role ARN of customer B along with the duplicated external ID. In a multi-tenant environment, where a third party supports multiple customers with different AWS accounts, the third party must use a different unique ID as the external ID for each AWS account. The third party is responsible for detecting duplicate external IDs and securely mapping each customer to their respective external ID. The third party should test to verify that they can only assume the role when specifying the external ID. The third party should refrain from storing the customer role ARN and the external ID until the external ID is required.

    The external ID is not treated as a secret, but the external ID must not be an easily guessable value, such as a phone number, name, or account ID. Make the external ID a read-only field so that the external ID cannot be changed for the purpose of impersonating the setup.

    You or the third party can generate the external ID. Define a process to determine who is responsible for generating the ID. Regardless of the entity creating the external ID, the third party enforces uniqueness and formats consistently across customers.

1.  **Deprecate customer-provided long-term credentials.**

    Deprecate the use of long-term credentials and use cross-account roles or IAM Roles Anywhere. If you must use long-term credentials, establish a plan to migrate to role-based access. For details on managing keys, see [Identity Management](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_identities_audit.html). Also work with your AWS account team and the third party to establish risk mitigation runbook. For prescriptive guidance on responding to and mitigating the potential impact of security incident, see [Incident response](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/incident-response.html).

1.  **Verify that setup has prescriptive guidance or is automated.**

    The policy created for cross-account access in your accounts must follow the [least-privilege principle](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege). The third party must provide a role policy document or automated setup mechanism that uses an AWS CloudFormation template or an equivalent for you. This reduces the chance of errors associated with manual policy creation and offers an auditable trail. For more information on using a CloudFormation template to create cross-account roles, see [Cross-Account Roles](https://aws.amazon.com/blogs/apn/tag/cross-account-roles/).

    The third party should provide an automated, auditable setup mechanism. However, by using the role policy document outlining the access needed, you should automate the setup of the role. Using a CloudFormation template or equivalent, you should monitor for changes with drift detection as part of the audit practice.

1.  **Account for changes.**

    Your account structure, your need for the third party, or their service offering being provided might change. You should anticipate changes and failures, and plan accordingly with the right people, process, and technology. Audit the level of access you provide on a periodic basis, and implement detection methods to alert you to unexpected changes. Monitor and audit the use of the role and the datastore of the external IDs. You should be prepared to revoke third-party access, either temporarily or permanently, as a result of unexpected changes or access patterns. Also, measure the impact to your revocation operation, including the time it takes to perform, the people involved, the cost, and the impact to other resources.

    For prescriptive guidance on detection methods, see the [Detection best practices](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/detection.html).

## Resources
<a name="resources"></a>

 **Related best practices:**
+  [SEC02-BP02 Use temporary credentials](sec_identities_unique.md)
+  [SEC03-BP05 Define permission guardrails for your organization](sec_permissions_define_guardrails.md)
+  [SEC03-BP06 Manage access based on lifecycle](sec_permissions_lifecycle.md)
+  [SEC03-BP07 Analyze public and cross-account access](sec_permissions_analyze_cross_account.md)
+ [ SEC04 Detection ](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/detection.html)

 **Related documents:**
+ [ Bucket owner granting cross-account permission to objects it does not own ](https://docs.aws.amazon.com/AmazonS3/latest/userguide/example-walkthroughs-managing-access-example4.html)
+ [ How to use trust policies with IAM roles ](https://aws.amazon.com/blogs/security/how-to-use-trust-policies-with-iam-roles/)
+ [ Delegate access across AWS accounts using IAM roles ](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_cross-account-with-roles.html)
+ [ How do I access resources in another AWS account using IAM? ](https://aws.amazon.com/premiumsupport/knowledge-center/cross-account-access-iam/)
+ [ Security best practices in IAM ](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)
+ [ Cross-account policy evaluation logic ](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic-cross-account.html)
+ [ How to use an external ID when granting access to your AWS resources to a third party ](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user_externalid.html)
+ [ Collecting Information from AWS CloudFormation Resources Created in External Accounts with Custom Resources ](https://aws.amazon.com/blogs/apn/collecting-information-from-aws-cloudformation-resources-created-in-external-accounts-with-custom-resources/)
+ [ Securely Using External ID for Accessing AWS Accounts Owned by Others ](https://aws.amazon.com/blogs/apn/securely-using-external-id-for-accessing-aws-accounts-owned-by-others/)
+ [ Extend IAM roles to workloads outside of IAM with IAM Roles Anywhere ](https://aws.amazon.com/blogs/security/extend-aws-iam-roles-to-workloads-outside-of-aws-with-iam-roles-anywhere/)

 **Related videos:**
+ [ How do I allow users or roles in a separate AWS account access to my AWS account? ](https://www.youtube.com/watch?v=20tr9gUY4i0)
+ [AWS re:Invent 2018: Become an IAM Policy Master in 60 Minutes or Less ](https://www.youtube.com/watch?v=YQsK4MtsELU)
+ [AWS Knowledge Center Live: IAM Best Practices and Design Decisions ](https://www.youtube.com/watch?v=xzDFPIQy4Ks)

 **Related examples:**
+ [ Well-Architected Lab - Lambda cross account IAM role assumption (Level 300) ](https://www.wellarchitectedlabs.com/security/300_labs/300_lambda_cross_account_iam_role_assumption/)
+ [ Configure cross-account access to Amazon DynamoDB ](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/configure-cross-account-access-to-amazon-dynamodb.html)
+ [AWS STS Network Query Tool ](https://github.com/aws-samples/aws-sts-network-query-tool)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
