---
source_url: https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/self-signed-certificates.html
---

This guide provides documentation for Wickr Enterprise. If you're using AWS Wickr, see [AWS Wickr Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide/what-is-wickr.html).

# Wickr Federation with Untrusted/Self-Signed Certificates
<a name="self-signed-certificates"></a>

Super administrators can add self-signed/untrusted certificates in the Wickr admin panel to allow federation between Wickr Enterprise environments.

Complete the following procedure to add self-signed/untrusted certificates.

1. Sign in to the Wickr Super Administrator Console.
![Global federation navigation.](http://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/images/wickr-ent-global-cert.png)

1. In the navigation pane, choose **Global Federation**.

1. In the **Federation ID** section, enter the **Domain** and **API Key** for the infrastructure that needs to be federated.

1. Select the **Federated Cert** tab, and then choose **Add Cert**.

1. In the **Federated Cert** section, select the API key. You will be able to select from the API keys added in Step 3.

1. Enter the certificate description. Make sure the certificate fields are valid.

1. Choose **Save**. You can see the list of certificates in the **Federated Cert** tab.

   To add more certificates, repeat steps 3—7.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Wickr. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wickr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
