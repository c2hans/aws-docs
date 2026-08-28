---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/reference-2fa.html
---

# Configuration reference for 2FA with AWS CloudHSM Management Utility
<a name="reference-2fa"></a>

The following is an example of the two-factor authentication (2FA) properties in the `authdata` file for both the AWS CloudHSM Management Utility (CMU) generated request and your responses.

```
{
    "Version": "1.0",
    "PublicKey": "{{-----BEGIN PUBLIC KEY----- ... -----END PUBLIC KEY-----}}",
    "Data": [
        {
            "HsmId": "hsm-lgavqitns2a",
            "Digest": "k5O1p3f6foQRVQH7S8Rrjcau6h3TYqsSdr16A54+qG8=",
            "Signature": "{{Kkdl ... rkrvJ6Q==}}"
        },
        {
            "HsmId": "hsm-lgavqitns2a",
            "Digest": "IyBcx4I5Vyx1jztwvXinCBQd9lDx8oQe7iRrWjBAi1w=",
            "Signature": "{{K1hxy ... Q261Q==}}"
        }
    ]
}
```

**Data**
Top-level node. Contains a subordinate node for each HSM in the cluster. Appears in requests and responses for all 2FA commands.

**Digest**
This is what you must sign to provide the second factor of authentication. CMU generated in requests for all 2FA commands.

**HsmId**
The ID of your HSM. Appears in requests and responses for all 2FA commands.

**PublicKey**
The public key portion of the key pair you generated inserted as PEM-formatted string. You enter this in responses for **createUser** and **changePswd**.

**Signature**
The Base 64 encoded signed digest. You enter this in responses for all 2FA commands.

**Version**
The version of the authentication data JSON formatted file. Appears in requests and responses for all 2FA commands.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
