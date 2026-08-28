---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/generate_csr_using_keytool_5.html
---

# Generate an AWS CloudHSM CSR using keytool
<a name="generate_csr_using_keytool_5"></a>

You receive the greatest flexibility in generating a certificate signing request (CSR) if you use the [OpenSSL Dynamic Engine for AWS CloudHSM Client SDK 5](openssl-library.md). The following command uses keytool to generate a CSR for a key pair with the alias, `example-key-pair`.

------
#### [ Linux ]

```
$ keytool -certreq -alias {{<key pair label>}} \
	-file my_csr.csr \
	-keystore example_keystore.store \
	-storetype CLOUDHSM \
	-J-classpath '-J/opt/cloudhsm/java/*'
```

------
#### [ Windows ]

```
PS C:\> keytool -certreq -alias {{<key pair label>}} `
	-file my_csr.csr `
	-keystore example_keystore.store `
	-storetype CLOUDHSM `
	-J-classpath '-J"C:\Program Files\Amazon\CloudHSM\java\*"'
```

------

**Note**
To use a key pair from keytool, that key pair must have an entry in the specified key store file. If you want to use a key pair that was generated outside of keytool, you must import the key and certificate metadata into the key store. For instructions on importing the keystore data see [Use keytool to import intermediate and root certificates into AWS CloudHSM key store](import_cert_using_keytool_5.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
