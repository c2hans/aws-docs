---
source_url: https://docs.aws.amazon.com/whitepapers/latest/replatform-dotnet-apps-with-windows-containers/change-your-dockerfile-to-support-windows-authentication.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Change your Dockerfile to support Windows authentication
<a name="change-your-dockerfile-to-support-windows-authentication"></a>

 The following snippet demonstrates how to configure your IIS application running inside a container to use a gMSA. The following Dockerfile instructions install and configure Windows authentication inside the container, and on IIS.

```
# Install Windows Auth in IIS Feature
RUN Install-WindowsFeature -Name Web-Windows-Auth –IncludeAllSubFeature

# Configure the IIS Application Pool account to use Network Service account.
That enables it to leverage gMSA.
RUN Import-Module WebAdministration; Set-ItemProperty IIS:\AppPools\SiteName
-name processModel.identityType -value 2

# Disable Anonymous authentication on IIS
RUN Import-Module WebAdministration; Set-WebConfigurationProperty
-Filter '/system.webServer/security/authentication/anonymousAuthentication'
-Name Enabled -Value False -PSPath 'IIS:\' -Location 'SiteName'

# Enable Windows Authentication
RUN Import-Module WebAdministration; Set-WebConfigurationProperty
-Filter '/system.webServer/security/authentication/windowsAuthentication'
-Name Enabled -Value True -PSPath 'IIS:\' -Location 'SiteName'
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
