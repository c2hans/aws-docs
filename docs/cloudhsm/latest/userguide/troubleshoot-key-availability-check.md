---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/troubleshoot-key-availability-check.html
---

# AWS CloudHSM error seen during key availability check
<a name="troubleshoot-key-availability-check"></a>

**Problem**: An AWS CloudHSM hardware security module (HSM) is returning the following error:

```
Key {{<KEY HANDLE>}} does not meet the availability requirements - The key must be available on at least 2 HSMs before being used.
```

**Cause**: Key availability checks look for keys that, under rare but possible conditions, could be lost. This error usually occurs in clusters with only one HSM or in clusters with two HSMs during a period in which one of them is being replaced. In these situations, the following customer operations likely prompted the above error:
+ A new key was generated using a command like **[The generate-symmetric category in CloudHSM CLI](cloudhsm_cli-key-generate-symmetric.md)** or **[The generate-asymmetric-pair category in CloudHSM CLI](cloudhsm_cli-key-generate-asymmetric-pair.md)**.
+ A **[List keys for a user with CloudHSM CLI](cloudhsm_cli-key-list.md)** operation was started.
+ A new instance of the SDK was started.
**Note**
OpenSSL frequently forks new instances of the SDK.

**Resolution/recommendation**: Choose from the following actions to prevent this error from occurring:
+ Use the **--disable-key-availability-check** parameter to set key availability to false in the configure file of your [configure tool](configure-tool.md). For more information, see the [AWS CloudHSM Client SDK 5 configuration parameters](configure-tool-params5.md) section of the Configure tool.
+ If using a cluster with two HSMs, avoid using the operations that prompted the error, except during initialization code.
+ Increase the amount of HSMs in your cluster to at least three.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
