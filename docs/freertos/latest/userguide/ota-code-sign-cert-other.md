---
source_url: https://docs.aws.amazon.com/freertos/latest/userguide/ota-code-sign-cert-other.html
---

# Creating a code-signing certificate for custom hardware
<a name="ota-code-sign-cert-other"></a>

Using an appropriate toolset, create a self-signed certificate and private key for your hardware.

Use the AWS Command Line Interface to import your code-signing certificate, private key, and certificate chain into AWS Certificate Manager. For information about installing the AWS CLI, see [ Installing the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html).

After you create your code-signing certificate, you can use the AWS CLI to import it into ACM:

```
aws acm import-certificate --certificate fileb://code-sign.crt --private-key fileb://code-sign.key
```

The output from this command displays an ARN for your certificate. You need this ARN when you create an OTA update job.

ACM requires certificates to use specific algorithms and key sizes. For more information, see [Prerequisites for Importing Certificates](https://docs.aws.amazon.com/acm/latest/userguide/import-certificate-prerequisites.html). For more information about ACM, see [Importing Certificates into AWS Certificate Manager](https://docs.aws.amazon.com/acm/latest/userguide/import-certificate.html).

You must copy, paste, and format the contents of your code-signing certificate into the `vendors/{{vendor}}/boards/{{board}}/aws_demos/config_files/ota_demo_config.h` file that is part of the FreeRTOS code you download later.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for FreeRTOS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query freertos` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
