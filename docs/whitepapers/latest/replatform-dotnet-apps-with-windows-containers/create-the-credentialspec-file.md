---
source_url: https://docs.aws.amazon.com/whitepapers/latest/replatform-dotnet-apps-with-windows-containers/create-the-credentialspec-file.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Create the CredentialSpec file
<a name="create-the-credentialspec-file"></a>

 In the previous sections, you joined your ECS instance to an Active Directory domain, created a gMSA, and configured your application to use the gMSA. In this section, you will configure your ECS Task Definition to use the gMSA using a credential spec file. A credential spec file is a JSON document that contains metadata about your gMSA account.

 To create the credential spec file, you can run the following PowerShell cmdlets. You will need to run these cmdlets on either the ECS instance, or a domain joined EC2 instance that has the RSAT AS PowerShell tools installed. For more information on how to create a credential spec file, refer to the [Create gMSAs for Windows containers](https://docs.microsoft.com/en-us/virtualization/windowscontainers/manage-containers/manage-serviceaccounts) documentation.

```
#Install the CredentialSpec module
Install-Module CredentialSpec

#Create a credential spec using the gMSA name at the provided path
New-CredentialSpec -AccountName gmsaecs -Path "C:\gmsa\gmsaecs_credspec.json"
```

 The following snippet shows an example credential spec file.

```
{
    "CmsPlugins": [
        "ActiveDirectory"
    ],
    "DomainJoinConfig": {
        "Sid": "S-1-5-21-2554468230-2647958158-2204241789",
        "MachineAccountName": "gmsaecs",
        "Guid": "8665abd4-e947-4dd0-9a51-f8254943c90b",
        "DnsTreeName": "example.com",
        "DnsName": "example.com",
        "NetBiosName": "example"
    },
    "ActiveDirectoryConfig": {
        "GroupManagedServiceAccounts": [
            {
                "Name": "gmsaecs",
                "Scope": "example.com"
            }
        ]
    }
}
```
