---
source_url: https://docs.aws.amazon.com/iot/latest/developerguide/revoke-ca-cert.html
---

# Revoke a client certificate
<a name="revoke-ca-cert"></a>

If you detect suspicious activity on a registered client certificate, you can revoke it so that it can't be used again.

**Note**
Once a certificate is revoked, it's status can't be changed. That is, the certificate status can't be changed to `Active` or any other status.

## Revoke a client certificate (console)
<a name="revoke-device-cert-console"></a>

**To revoke a client certificate using the AWS IoT console**

1. Sign in to the AWS Management Console and open the [AWS IoT console](https://console.aws.amazon.com/iot/home).

1. In the left navigation pane, choose **Secure**, choose **Certificates**.

1. In the list of certificates, locate the certificate that you want to revoke, and open the option menu by using the ellipsis icon.

1. In the option menu, choose **Revoke**.

If the certificate was successfully revoked, it will show as **Revoked** in the list of certificates.

## Revoke a client certificate (CLI)
<a name="revoke-device-cert-cli"></a>

The AWS CLI provides the [**update-certificate**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/update-certificate.html) command to revoke a certificate.

```
aws iot update-certificate \
    --certificate-id {{certificateId}} \
    --new-status REVOKED
```

If the command was successful, the certificate's status will be `REVOKED`. Run [**describe-certificate**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-certificate.html) to see the certificate's status.

```
aws iot describe-certificate \
    --certificate-id {{certificateId}}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Core. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
