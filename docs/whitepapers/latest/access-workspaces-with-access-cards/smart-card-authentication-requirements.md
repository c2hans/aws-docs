---
source_url: https://docs.aws.amazon.com/whitepapers/latest/access-workspaces-with-access-cards/smart-card-authentication-requirements.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Smart card authentication requirements
<a name="smart-card-authentication-requirements"></a>

## CA certificate requirements
<a name="ca-certificate-requirements"></a>

AD Connector requires a CA certificate, which represents the issuer of your user certificates, for smart card authentication. AD Connector matches CA certificates with the certificates presented by your users with their smart cards. Note the following CA certificate requirements:
+  Before you can register a CA certificate, it must be more than 90 days away from expiration.
+  CA certificates must be in Privacy-Enhanced Mail (PEM) format. If you export CA certificates from inside Active Directory, choose `Base64-encoded X.509 (.CER)` as the export file format.
+  All root and intermediary CA certificates that chain from an issuing CA to user certificates must be uploaded for smart card authentication to succeed.
+  A maximum of 100 CA certificates can be stored per AD Connector directory.
+  AD Connector does not support the `RSASSA-PSS` signature algorithm for CA certificates.

## Certificate revocation checking process
<a name="certificate-revocation-checking-process"></a>

To perform smart card authentication, AD Connector must check the revocation status of user certificates using Online Certificate Status Protocol (OCSP). To perform certificate revocation checking, an OCSP responder URL must be internet accessible.

## Obtain Department of Defense Certificates
<a name="obtain-department-of-defense-certificates"></a>

The most current DoD approved external PKI certificate trust chains can be downloaded from the DoD Cyber Exchange website. This zip file contains certificate trust chains for DoD Approved External PKIs. Version 7.3 adds a rekeyed Treasury PKI root and new NASA issuance chain and removes several expired CAs.

1.  Open a web browser and navigate to the [DoD Cyber Exchange Public Tools and Configuration Files](https://public.cyber.mil/pki-pke/tools-configuration-files/) page.

1.  Download the latest **DoD Approved External PKI Certificate Trust Chains - Version 7.3** under the **Tools** heading.

1.  All DoD certificates have a OCSP responder URL of `http://ocsp.disa.mil`.

 Alternatively, InstallRoot can extract certificates directly to `PEM` format (required for import to AWS Directory Services):

1.  Open the InstallRoot application.

1.  Choose the **Certificate** menu option.

1.  Choose all installed DoD root and intermediate certificates that are desired for export.

1.  Under **Export**, choose **PEM**.
![A screenshot showing exporting the root and intermediate certificates with InstallRoot.](http://docs.aws.amazon.com/whitepapers/latest/access-workspaces-with-access-cards/images/workspaces-smartcard15.png)

   * Export root and intermediate certificates with InstallRoot *

1.  Choose a directory to save the exported certificates, and click **OK**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
