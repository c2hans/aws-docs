---
source_url: https://docs.aws.amazon.com/solutions/latest/modular-cloud-studio-on-aws/identity-modules.html
---

# Identity modules
<a name="identity-modules"></a>

Identity modules create the necessary resources to allow users to interact with MCS and the post production environment.

The following Identity modules are available in MCS after deployment:
+ Managed Active Directory module - Deploys a new Microsoft Active Directory instance under standard edition
+ Unmanaged Active Directory module - Receives existing Microsoft Active Directory information from an input form

## Managed Active Directory module
<a name="managed-active-directory-module"></a>

![managed active directory module](http://docs.aws.amazon.com/solutions/latest/modular-cloud-studio-on-aws/images/managed-active-directory-module.png)

1.  [Directory Service](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/what_is.html) deploys an instance of [AWS Managed Microsoft AD](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/directory_microsoft_ad.html) under standard edition.

1. The Active Directory module deploys a temporary EC2 instance that:
   + Joins to the [AWS Managed Microsoft AD](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/launching_instance.html) domain
   + Sets password policy for domain users (90-day expiration)
   + Self-terminates after approximately 5 minutes

1. User credentials generated during deployment are automatically stored in [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html).

## Spoke Managed Identity module
<a name="spoke-managed-identity-module"></a>

1.  [Directory Service](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/what_is.html) deploys an [AD Connector](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/directory_ad_connector.html) instance that establishes a connection to the Microsoft AD instance in the Hub environment.
