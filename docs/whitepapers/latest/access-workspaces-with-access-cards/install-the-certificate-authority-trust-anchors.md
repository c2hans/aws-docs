---
source_url: https://docs.aws.amazon.com/whitepapers/latest/access-workspaces-with-access-cards/install-the-certificate-authority-trust-anchors.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Install the Certificate Authority Trust Anchors
<a name="install-the-certificate-authority-trust-anchors"></a>

 The most current root certificates must be installed on both servers and workstations. InstallRoot is a utility that manages certificates for DoD and Network Security Services (NSS)-trusted root and intermediate CAs on Microsoft servers and workstations.

 **To download, install, and run the NIPRNet InstallRoot application**:

1.  Open a web browser and navigate to the [DoD Cyber Exchange Public Tools and Configuration Files](https://public.cyber.mil/pki-pke/tools-configuration-files/) page.

1.  Under the Tools heading, download the latest Windows Installer (MSI) version of InstallRoot.

1.  Run the InstallRoot installation tool.
**Note**
 Administrative rights are required when installing the InstallRoot application under the `C:\Program Files\` location on the system.

1.  Run the tool as an administrator to install the DoD certificates into the Windows/Internet Explorer local machine trust store.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
