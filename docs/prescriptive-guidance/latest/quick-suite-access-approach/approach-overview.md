---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/quick-suite-access-approach/approach-overview.html
---

# Overview of the approaches
<a name="approach-overview"></a>

While there are many different approaches that can be used to manage access to Amazon Quick, the recommended approach is to use [AWS IAM Identity Center integration](https://aws.amazon.com/blogs/business-intelligence/simplify-business-intelligence-identity-management-with-amazon-quicksight-and-aws-iam-identity-center/). In some cases, a different approach may be considered if you have specific requirements that are discussed further in this guide.

You can use the following approaches to configure access to Quick:
+ [IAM Identity Center integration](iam-identity-center-integration.md) – Use the built-in service integration between Quick and IAM Identity Center, a feature released August 2023. This approach requires the Enterprise edition of Quick.
+ [Federated users](federated-users.md) – Manage users with an enterprise identity provider (IdP) to authenticate users when they sign in to Quick.
+ [Active Directory users](active-directory-users.md) – Grant access to a directory group in Microsoft Active Directory. This approach requires the Enterprise edition of Quick. The following are the available options:
  + AWS Directory Service for Microsoft Active Directory
  + AD Connector pointing to AWS Managed Microsoft AD
  + AD Connector pointing to a self-managed directory
+ [IAM users](iam-users.md) – Grant access for existing AWS Identity and Access Management (IAM) users. The following are the available options:
  + Send the IAM users an email invitation
  + Grant IAM users or user groups permissions to self-provision access
+ [Quick users](quick-suite-users.md) – Create local users within Quick.

There are many options to choose from when configuring user access to Quick. By understanding the advantages and limitations of each approach, you can determine the right approach for your organization. It is also possible to adopt more than one approach for your organization, depending on certain circumstances. However, this increases the complexity of the provisioning operations.

## Differences between Quick editions
<a name="editions"></a>

Access management options vary between the Standard and Enterprise editions of Quick. The following table compares the access options for each. For more information, see [User management between editions](https://docs.aws.amazon.com/quicksuite/latest/userguide/editions.html#edition-user-management) in the Quick documentation.

|
|
| Access approach | Standard edition | Enterprise edition |
| --- |--- |--- |
| Quick user | Yes | Yes |
| IAM user | Yes | Yes |
| Active Directory user | No | Yes |
| IAM Identity Center integration | No | Yes |
| Federated user | Yes | Yes |
