---
source_url: https://docs.aws.amazon.com/whitepapers/latest/access-workspaces-with-access-cards/generate-the-issuing-ca-certificate.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Generate the issuing CA certificate
<a name="generate-the-issuing-ca-certificate"></a>

 **To generate the third party issuing the CA to the Group Policy object and the NTAuth store in AD**:

1.  Log into the Root Certification Authority server with an Administrator account.

1.  Select **Start** > **Run** >, enter **Cmd**, and choose **Enter**.

1.  To export the Root Certification Authority server to a new file name called ca\_name.cer, enter:

```
certutil -ca.cert ca_name.cer
```

 The following figure shows the certificate successfully installed into the NTAuth store.

![A screenshot showing the installation of the issuing CA certificate into the NTAuth store using certutil](http://docs.aws.amazon.com/whitepapers/latest/access-workspaces-with-access-cards/images/workspaces-smartcard10.png)

 *Use certutil to install the issuing CA certificate into NTAuth store *

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
