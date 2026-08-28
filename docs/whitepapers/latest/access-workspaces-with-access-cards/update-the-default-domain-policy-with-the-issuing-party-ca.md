---
source_url: https://docs.aws.amazon.com/whitepapers/latest/access-workspaces-with-access-cards/update-the-default-domain-policy-with-the-issuing-party-ca.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Update the default domain policy with the issuing party CA
<a name="update-the-default-domain-policy-with-the-issuing-party-ca"></a>

 Add the issuing CA to the trusted roots in an Active Directory Group Policy object.

 **To configure Group Policy in the Windows domain to distribute the issuing CA to the trusted root store of all domain computers**:

1.  Open **Group Policy Management**, select your domain root in the navigation tree, and expand the **Group Policy Objects** container.

1.  Choose the **Default Domain Policy Group Policy** object, and then choose **Edit**. A new window opens.

1.  In the left navigation pane, expand the following items:
   +  **Computer Configuration**
   +  **Policies**
   +  **Windows Settings**
   +  **Security Settings**
   +  **Public Key Policy**

1.  Right-click **Trusted Root Certification Authorities**.

1.  Select **All Tasks**, then choose **Import**.

1.  Follow the instructions in the wizard to import the certificate file generated in the [Generate the issuing CA certificate](generate-the-issuing-ca-certificate.md), ca\_name.cer.

1.  A confirmation window appears when the import is complete. Choose **OK**.

1.  Close the **Group Policy** window.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
