---
source_url: https://docs.aws.amazon.com/singlesignon/latest/userguide/tip-legacy-experience.html
---

# Legacy experience of trusted identity propagation

Your IAM Identity Center instance uses the *legacy experience* until you turn on the simplified experience. In the legacy experience, you must configure each AWS managed application and account in the trusted identity propagation call chain:
+ An IAM Identity Center application registration for each AWS managed application, in each account in the trusted identity propagation call chain.
+ The `sts:SetContext` permission in the trust policy of each role that forwards identity.
+ (Optional) OAuth scopes on the IAM Identity Center applications in the trusted identity propagation call chain, to restrict which AWS services each application can access on the user's behalf. For customer managed applications, you configure scopes in the IAM Identity Center console under **Trusted applications for identity propagation**, or with the `PutApplicationAccessScope` API. For more information, see [Specify trusted applications](trustedidentitypropagation-using-customermanagedapps-specify-trusted-apps.md).
+ (Optional) User and group assignments across different AWS managed applications, to restrict access.

In the legacy experience, the primary user identifier in the identity context is the user ID that IAM Identity Center generates. The identity context doesn't include the username.

For instructions on moving to the simplified experience, see [Moving from the legacy experience to the simplified experience](simplified-tip-migration.md). When you move, you can leave existing IAM Identity Center application registrations and `sts:SetContext` permissions in place.

## Enabling trusted identity propagation in the legacy experience
<a name="enabling-tip"></a>

In the legacy experience, enabling trusted identity propagation involves the following two steps:

1. **Enable IAM Identity Center and connect your existing source of identities to IAM Identity Center** - You'll continue to manage your workforce identities in your existing source of identities; connecting it to IAM Identity Center creates a reference to your workforce that all AWS services in your use case can share. It's also available for data owners to use in future use cases.

1. **Connect the AWS services in your use case to IAM Identity Center** - In the legacy experience, the administrator of each AWS service in the trusted identity propagation use case creates an IAM Identity Center integration for that service. The integration appears as an IAM Identity Center application in the service's console. To create it, follow the guidance in the respective service documentation.

**Note**
If your use case involves a *third-party* or *customer developed application*, you enable trusted identity propagation by configuring a trust relationship between the identity provider that authenticates the application users and IAM Identity Center. This allows your application to take advantage of the trusted identity propagation flow.
For more information, see [Using applications with a trusted token issuer](using-apps-with-trusted-token-issuer.md).

**Topics**
+ [Enabling trusted identity propagation in the legacy experience](#enabling-tip)
+ [Prerequisites and considerations](trustedidentitypropagation-overall-prerequisites.md)
