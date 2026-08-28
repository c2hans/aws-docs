---
source_url: https://docs.aws.amazon.com/whitepapers/latest/replatform-dotnet-apps-with-windows-containers/configure-a-group-managed-service-account-in-the-active-directory-domain.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Configure a group Managed Service Account in the Active Directory domain
<a name="configure-a-group-managed-service-account-in-the-active-directory-domain"></a>

 A group Managed Service Account (gMSA) is a type of service account available in Windows Server 2012 and later. When a container is configured to use a gMSA, it does not know the password for the account. The gMSA password is configured on the Active Directory domain controller. When a container using gMSA runs on a domain-joined ECS instance, the ECS instance retrieves the password for the gMSA from the Active Directory domain controller and passes it to the container. It is recommended to create a security group for each gMSA account and add ECS instances (that will use the gMSA account) to the security group. This limits access to the gMSA to only the ECS instances that need it.

 The following PowerShell snippet demonstrates how to create a security group, create a gMSA, and add the ECS Container Instance to the security group. To run the following commands, you will need to use an account that belongs to the Domain Admins security group or has been delegated the Create the `msDS-GroupManagedServiceAccount` objects permission. On the machine that you are running these commands on, you will need to install Remote Server Administration Tools.

```
# Create the AD group
New-ADGroup -Name "Amazon ECS Authorized Container instances"
-SamAccountName "ECSContainerInstances" -GroupScope DomainLocal

# Create the gMSA
New-ADServiceAccount -Name "gmsaecs" -DnsHostName "gmsaecs.YOURDOMAIN_FQDN"
-ServicePrincipalNames "host/gmsaecs", "host/gmsaecs.YOURDOMAIN_FQDN"
-PrincipalsAllowedToRetrieveManagedPassword "ECSContainerInstances"

# Add your ECS Container Instance to the AD group
Add-ADGroupMember -Identity "ECSContainerInstances"
-Members "ECSContainerInstances01$", "ECSContainerInstances02$",
"ECSContainerInstances03$"
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
