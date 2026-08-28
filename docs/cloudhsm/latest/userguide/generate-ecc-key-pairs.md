---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/generate-ecc-key-pairs.html
---

# Generate ECC (elliptic curve cryptography) key pairs using the AWS CloudHSM KMU
<a name="generate-ecc-key-pairs"></a>

To generate an ECC key pair for AWS CloudHSM, use the [genECCKeyPair](key_mgmt_util-genECCKeyPair.md) command in AWS CloudHSM key\_mgmt\_util. To see all available options, including a list of the supported elliptic curves, use the **genECCKeyPair -h** command.

The following example generates an ECC key pair using the P-384 elliptic curve defined in [NIST FIPS publication 186-4](http://dx.doi.org/10.6028/NIST.FIPS.186-4).

```
Command: genECCKeyPair -i 14 -l ecc-p384
Cfm3GenerateKeyPair returned: 0x00 : HSM Return: SUCCESS

Cfm3GenerateKeyPair:    public key handle: 524297    private key handle: 524298

Cluster Error Status
Node id 0 and err state 0x00000000 : HSM Return: SUCCESS
Node id 1 and err state 0x00000000 : HSM Return: SUCCESS
Node id 2 and err state 0x00000000 : HSM Return: SUCCESS
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
