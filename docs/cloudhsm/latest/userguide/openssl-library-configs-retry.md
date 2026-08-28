---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/openssl-library-configs-retry.html
---

# Retry commands for OpenSSL for AWS CloudHSM
<a name="openssl-library-configs-retry"></a>

AWS CloudHSM Client SDK 5.8.0 and later have a built-in automatic retry strategy which will retry HSM-throttled operations from the client side. When an HSM throttles operations because it is too busy performing previous operations and cannot take more requests, client SDKs will attempt to retry throttled operations up to 3 times while exponentially backing off. This automatic retry strategy can be set to one of two modes: **off** and **standard**.
+ **off**: The Client SDK will not perform any retry strategy for any throttled operations by the HSM.
+ **standard**: This is the default mode for Client SDK 5.8.0 and later. In this mode, client SDKs will automatically retry throttled operations by exponentially backing off.

For more information, see [HSM throttling](troubleshoot-hsm-throttling.md).

## Set retry commands to off mode
<a name="w2aac25c21c19c19b7b9"></a>

You can use the following command to set retry commands to **off** mode:

```
$ sudo /opt/cloudhsm/bin/configure-dyn --default-retry-mode off
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
