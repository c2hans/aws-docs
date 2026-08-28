---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-key-unwrap.html
---

# The key unwrap command in CloudHSM CLI
<a name="cloudhsm_cli-key-unwrap"></a>

The **key unwrap** parent command in CloudHSM CLI imports an encrypted (wrapped) symmetric or asymmetric private key from a file and into the HSM. This command is designed to import encrypted keys that were wrapped by the [The key wrap command in CloudHSM CLI](cloudhsm_cli-key-wrap.md) command, but it can also be used to unwrap keys that were wrapped with other tools. However, in those situations, we recommend using the PKCS\#11 or JCE software libraries to unwrap the key.

**Note**
ML-DSA keys cannot be unwrapped. To use ML-DSA keys, generate them directly on the HSM using [key generate-asymmetric-pair ml-dsa](cloudhsm_cli-key-generate-asymmetric-pair-mldsa.md).
+ [aes-gcm](cloudhsm_cli-key-unwrap-aes-gcm.md)
+ [aes-no-pad](cloudhsm_cli-key-unwrap-aes-no-pad.md)
+ [aes-pkcs5-pad](cloudhsm_cli-key-unwrap-aes-pkcs5-pad.md)
+ [aes-zero-pad](cloudhsm_cli-key-unwrap-aes-zero-pad.md)
+ [cloudhsm-aes-gcm](cloudhsm_cli-key-unwrap-cloudhsm-aes-gcm.md)
+ [rsa-aes](cloudhsm_cli-key-unwrap-rsa-aes.md)
+ [rsa-oaep](cloudhsm_cli-key-unwrap-rsa-oaep.md)
+ [rsa-pkcs](cloudhsm_cli-key-unwrap-rsa-pkcs.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
