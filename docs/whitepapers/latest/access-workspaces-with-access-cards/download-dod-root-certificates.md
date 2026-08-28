---
source_url: https://docs.aws.amazon.com/whitepapers/latest/access-workspaces-with-access-cards/download-dod-root-certificates.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Download DoD root certificates
<a name="download-dod-root-certificates"></a>

 Export or download the third-party root certificate. How you obtain the party root certificate varies by vendor. The certificate must be in Base64 Encoded X.509 format.

The most current DoD certificates bundles can be downloaded from the DoD Cyber Exchange website. This zip file contains the DoD PKI CA certificates in PKCS\#7 certificate bundles containing either Privately Enhanced Mail (PEM)-encoded or Distinguished Encoding Rules (DER)-encoded certificates. Separate PKCS\#7 certificate bundles are also included for each root CA, for relying parties who may wish to accept only certificates issued with the key and signature hash combinations (for example, RSA-2048/SHA-256) issued by a given root. Instructions for verifying the integrity of all p7b files using the signed SHA-256 hashes file are included in the README.

 **To download the DOD root certificates**:

1.  Open a web browser and navigate to the [DoD Cyber Exchange Public Tools and Configuration Files](https://public.cyber.mil/pki-pke/tools-configuration-files/) page.

1.  Under the **Tools** heading, download the latest **PKI CA Certificate Bundles: PKCS\#7 For DoD PKI Only - Version 5.6**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
