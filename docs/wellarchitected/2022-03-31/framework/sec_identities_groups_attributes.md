---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/sec_identities_groups_attributes.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SEC02-BP06 Leverage user groups and attributes
<a name="sec_identities_groups_attributes"></a>

 As the number of users you manage grows, you will need to determine ways to organize them so that you can manage them at scale. Place users with common security requirements in groups defined by your identity provider, and put mechanisms in place to ensure that user attributes that may be used for access control (for example, department or location) are correct and updated. Use these groups and attributes to control access, rather than individual users. This allows you to manage access centrally by changing a user’s group membership or attributes once with a [permission set](https://docs.aws.amazon.com/singlesignon/latest/userguide/permissionsets.html), rather than updating many individual policies when a user’s access needs change.

You can use AWS IAM Identity Center (IAM Identity Center) to manage user groups and attributes. IAM Identity Center supports most commonly used attributes whether they are entered manually during user creation or automatically provisioned using a synchronization engine, such as defined in the System for Cross-Domain Identity Management (SCIM) specification.

 **Level of risk exposed if this best practice is not established:** Low

## Implementation guidance
<a name="implementation-guidance"></a>
+  If you are using AWS IAM Identity Center (IAM Identity Center), configure groups: IAM Identity Center provides you with the ability to configure groups of users, and assign groups the desired level of permission.
  +  [AWS Single Sign-On - Manage Identities](https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-identity-source-sso.html)
+  Learn about attribute-based access control (ABAC): ABAC is an authorization strategy that defines permissions based on attributes.
  +  [What Is ABAC for AWS?](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html)
  +  [Lab: IAM Tag Based Access Control for EC2](https://www.wellarchitectedlabs.com/Security/300_IAM_Tag_Based_Access_Control_for_EC2/README.html)

## Resources
<a name="resources"></a>

 **Related documents:**
+  [Getting Started with AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/getting-started.html)
+  [IAM Best Practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)
+  [Identity Providers and Federation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers.html)
+  [The AWS Account Root User](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html)

 **Related videos:**
+  [Best Practices for Managing, Retrieving, and Rotating Secrets at Scale](https://youtu.be/qoxxRlwJKZ4)
+  [Managing user permissions at scale with AWS IAM Identity Center](https://youtu.be/aEIqeFCcK7E)
+  [Mastering identity at every layer of the cake](https://www.youtube.com/watch?v=vbjFjMNVEpc)

 **Related examples:**
+  [Lab: IAM Tag Based Access Control for EC2](https://www.wellarchitectedlabs.com/Security/300_IAM_Tag_Based_Access_Control_for_EC2/README.html)
