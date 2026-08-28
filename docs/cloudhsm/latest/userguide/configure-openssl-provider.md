---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/configure-openssl-provider.html
---

# Bootstrap OpenSSL Provider
<a name="configure-openssl-provider"></a>

Use the configure-openssl-provider tool to bootstrap your OpenSSL Provider installation and connect it to your AWS CloudHSM cluster.

**To bootstrap the OpenSSL Provider**

1. Run the configure-openssl-provider command with the IP address of an HSM in your cluster:

   ```
   $ sudo /opt/cloudhsm/bin/configure-openssl-provider -a {{<HSM IP address>}}
   ```

   Replace {{<HSM IP address>}} with the IP address of any HSM in your cluster.

1. Verify the configuration by checking that the OpenSSL Provider can connect to your cluster:

   ```
   $ openssl list -providers -provider-path /opt/cloudhsm/lib -provider cloudhsm
   ```

For more information about the configuration parameters, see [AWS CloudHSM Client SDK 5 configuration parameters](configure-tool-params5.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
