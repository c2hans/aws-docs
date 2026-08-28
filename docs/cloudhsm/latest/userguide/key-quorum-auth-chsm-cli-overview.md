---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/key-quorum-auth-chsm-cli-overview.html
---

# Quorum authentication process for CloudHSM CLI
<a name="key-quorum-auth-chsm-cli-overview"></a>

The following steps summarize the quorum authentication processes for CloudHSM CLI. For the specific steps and tools, see [Key management and usage with quorum authentication enabled for AWS CloudHSM using CloudHSM CLI](key-quorum-auth-chsm-cli-crypto-user.md).

1. Each hardware security module (HSM) user creates an asymmetric key for signing. Users do this outside of the HSM, taking care to protect the key appropriately.

1. Each HSM user logs in to the HSM and registers the public part of their signing key (the public key) with the HSM.

1. When an HSM user wants to do a quorum-controlled operation, the same user logs in to the HSM and gets a *quorum token*.

1. The HSM user gives the quorum token to one or more other HSM users and asks for their approval.

1. The other HSM users approve by using their keys to cryptographically sign the quorum token. This occurs outside the HSM.

1. When the HSM user has the required number of approvals, the same user logs in to the HSM and runs the quorum-controlled operation with the **--approval** argument, supplying the signed quorum token file, which contains all necessary approvals (signatures).

1. The HSM uses the registered public keys of each signer to verify the signatures. If the signatures are valid, the HSM approves the token and the quorum-controlled operation is performed.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
