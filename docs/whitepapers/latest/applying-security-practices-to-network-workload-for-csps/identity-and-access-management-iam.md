---
source_url: https://docs.aws.amazon.com/whitepapers/latest/applying-security-practices-to-network-workload-for-csps/identity-and-access-management-iam.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Identity and access management (IAM)
<a name="identity-and-access-management-iam"></a>

 This is a foundational element and requires a robust identity strategy that fits in with the overarching governance frameworks and supports business objectives.

## Identity management
<a name="identity-management"></a>

 There are two types of identities which must be managed when approaching the operation of secure network workloads on AWS: *human identities* and *machine identities*.
+  Implement identity management and permissions to verify that the right roles have access to the right resources under the right conditions. Apply the rule of least privilege, granting only the permissions required to complete a task.
+  Define distinct IAM principals, differentiating between human (administrators, developers, operators, and consumers) and machine identities (network workload components, tools) with diverse IAM policies and permissions.
+  Utilize a centralized and common Identity Provider (IdP), scoping multiple accounts in a common landing zone with services such as [AWS IAM Identity Center](https://aws.amazon.com/iam/identity-center/) and group their attributes appropriately.
+  Use strong sign-in mechanisms for human principals, with specific password policies and multi-factor authentication (MFA) with software or hardware mechanisms.
+  Require identities to dynamically acquire temporary credentials which have time-bound expiration, and engineer systems to require reauthentication once the session has expired.

## Permissions management
<a name="permissions-management"></a>

 Permissions control who can access what, and under what conditions. CSPs should assign permissions to specific human and machine identities to grant access to specific service actions on specific resources. Additionally, specify conditions that must be true for access to be granted.
+  Define access requirements, supporting the principle of least privilege: The principle of least privilege determines that only the permissions needed to complete an activity should be granted. CSPs should look to clearly understand what is required to be performed across their network workload and grant only those permissions.
+  Frequently review, refine, and reduce permissions: During early stages of design and test, permissions are often broad to allow for flexibility. Introduce a feedback cycle to review permissions and identify what has been used, and what permissions are not required.
+  The use of IAM Access Analyzer helps you review and analyze the policies applied to the supported resources in your zone of trust. The organization or account you choose is known as the zone of trust for the analyzer.
