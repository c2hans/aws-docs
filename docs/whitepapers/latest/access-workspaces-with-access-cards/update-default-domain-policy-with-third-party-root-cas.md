---
source_url: https://docs.aws.amazon.com/whitepapers/latest/access-workspaces-with-access-cards/update-default-domain-policy-with-third-party-root-cas.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Update default domain policy with third party root CAs
<a name="update-default-domain-policy-with-third-party-root-cas"></a>

 Add the Department of Defense third-party root CAs to the trusted roots in an Active Directory Group Policy object.

 **To configure Group Policy in the Windows domain to distribute the third-party CAs to the trusted root store of all domain computers**:

1.  Open **Group Policy Management**, choose your domain root in the navigation tree, and expand the **Group Policy Objects** container.

1.  Choose the **Default Domain Policy Group Policy** object, and then choose **Edit**. A new window opens.

1.  In the left pane, choose **Computer Configuration**, **Policies**, **Windows Settings**, **Security Settings**, **Public Key Policies**.
![A screenshot showing the expanded folder structure to navigate to Trusted Root Certification Authorities.](http://docs.aws.amazon.com/whitepapers/latest/access-workspaces-with-access-cards/images/navigate-to-trusted-root-certification-authorities.png)

1.  Right-click **Trusted Root Certification Authorities**.

1.  Select **All Tasks**, and then choose **Import**.

1.  Follow the instructions in the wizard to import the certificate file `Certificates_PKCS7_v5.6_DoD.der`.

1.  A confirmation window appears when the import is complete. Choose **OK**.

1.  Drag and drop all of the **intermediate DoD certificate authorities** to the **Trusted Intermediate Certification Authorities** folder.

1.  Close the **Group Policy** window.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
