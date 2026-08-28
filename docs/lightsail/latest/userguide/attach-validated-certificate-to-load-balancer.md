---
source_url: https://docs.aws.amazon.com/lightsail/latest/userguide/attach-validated-certificate-to-load-balancer.html
---

# Attach a validated SSL/TLS certificate to your Lightsail load balancer
<a name="attach-validated-certificate-to-load-balancer"></a>

After you verify that you control your domain, the certificate's status will change to **Valid**.

![Successful validation of domain](http://docs.aws.amazon.com/lightsail/latest/userguide/images/example-com-verified-and-ready-to-use.png)

Your next step is to attach the certificate to your Lightsail load balancer.

1. From the Lightsail home page, choose **Networking**.

1. Choose your load balancer.

1. Choose the **Custom domains** tab.

1. In the **Certificates** section, choose **Attach certificate**.

1. Select a certificate from the dropdown list.

1. Choose **Attach**, to attach the certificate.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lightsail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lightsail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
