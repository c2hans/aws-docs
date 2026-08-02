---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/update-values-secrets.html
---

# Update values in AWS Secrets Manager
<a name="update-values-secrets"></a>

You must sign the SAML requests and responses with SAML certificates to establish trust and verify authenticity. The certificate is created when you create the SAML 2.0 custom application. You will need to configure the solution application with the public key of this certificate.

1. From your AWS console, navigate to [AWS Secrets Manager](https://console.aws.amazon.com/secretsmanager/).

1. From the list of secrets, choose the secret named **/InnovationSandbox/<NAMESPACE>/Auth/IDPCert**.

1. On the secret details page, on the **Overview** tab, in the **Secret value** section, choose **Retrieve secret value** and choose **Edit**.

1. Choose **Plaintext**.

1. Copy the value of the IAM Identity Center certificate file (.pem) you downloaded. For more information, refer to the [Save application configuration values](update-auth-config.md#save-application-config-values) *Certificate* section.

1. Paste it into the Secrets Manager secret **Plaintext** field and choose **Save**. This will ensure that the application can use SAML authentication.

**Note**
The Innovation Sandbox on AWS solution is now ready for use. You can now [log in to the web UI](log-in-webui.md) and start using the solution.
