---
source_url: https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/Welcome.html
---

# Welcome
<a name="Welcome"></a>

**Note**
 IAM Identity Center uses the `sso`, `sso-directory`, and `identitystore` API namespaces. The `sso-directory` and `identitystore` namespaces authorize access to data in the Identity Store. Make sure your policies with IAM actions from these two namespaces are consistent to avoid conflicting authorization to the same data.

The Identity Store service used by IAM Identity Center provides a single place to retrieve all of your identities (users and groups). You can use the identity store API operations in this guide to manage your identity data programmatically. The scope of these APIs allows you to create, read, update, delete, and list users, groups, and memberships.

This guide also describes identity store operations that you can call and includes detailed information about data types and errors.

**Important**
If you use an external identity provider or Active Directory as your identity source, we recommend that you use the `Create`, `Update`, and `Delete` APIs with caution. Because IAM Identity Center doesn't support outbound synchronization, your identity source won't automatically update with the changes that you make to users or groups using these APIs.

 AWS provides SDKs that consist of libraries and sample code for various programming languages and platforms (Java, Ruby, .Net, iOS, Android, and more). The SDKs provide a convenient way to programmatically access Directory Service and other AWS services. For more information about the AWS SDKs, including how to download and install them, see [AWS Builder Center Toolbox](http://aws.amazon.com/tools/).

This document was last published on August 18, 2026.
