---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/cloudhsm_cli-key.html
---

# The key category in CloudHSM CLI
<a name="cloudhsm_cli-key"></a>

In the CloudHSM CLI, **key** is a parent category for a group of commands that, when combined with the parent category, create a command specific to keys. Currently, this category consists of the following commands:
+ [delete](cloudhsm_cli-key-delete.md)
+ [generate-file](cloudhsm_cli-key-generate-file.md)
+ [key generate-asymmetric-pair](cloudhsm_cli-key-generate-asymmetric-pair.md)
  + [key generate-asymmetric-pair rsa](cloudhsm_cli-key-generate-asymmetric-pair-rsa.md)
  + [key generate-asymmetric-pair ec](cloudhsm_cli-key-generate-asymmetric-pair-ec.md)
  + [key generate-asymmetric-pair ml-dsa](cloudhsm_cli-key-generate-asymmetric-pair-mldsa.md)
+ [key generate-symmetric](cloudhsm_cli-key-generate-symmetric.md)
  + [key generate-symmetric aes](cloudhsm_cli-key-generate-symmetric-aes.md)
  + [key generate-symmetric generic-secret](cloudhsm_cli-key-generate-symmetric-generic-secret.md)
+ [import pem](cloudhsm_cli-key-import-pem.md)
+ [list](cloudhsm_cli-key-list.md)
+ [replicate](cloudhsm_cli-key-replicate.md)
+ [set-attribute](cloudhsm_cli-key-set-attribute.md)
+ [share](cloudhsm_cli-key-share.md)
+ [unshare](cloudhsm_cli-key-unshare.md)
+ [unwrap](cloudhsm_cli-key-unwrap.md)
+ [wrap](cloudhsm_cli-key-wrap.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
