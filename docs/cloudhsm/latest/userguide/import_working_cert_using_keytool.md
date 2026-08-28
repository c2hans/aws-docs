---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/import_working_cert_using_keytool.html
---

# Import a working certificate into AWS CloudHSM key store using keytool
<a name="import_working_cert_using_keytool"></a>

Once a certificate signing request (CSR) is signed, you can import it into the AWS CloudHSM key store and associate it with the appropriate key pair. The following command provides an example.

```
keytool -importcert -noprompt -alias {{<key pair label>}} \
        -file example_certificate.crt \
        -keystore example_keystore.store
        -storetype CLOUDHSM \
        -J-classpath '-J/opt/cloudhsm/java/*' \
        -J-Djava.library.path=/opt/cloudhsm/lib/
```

The alias should be a key pair with an associated certificate in the key store. If the key is generated outside of keytool, or is generated on a different client instance, you must first import the key and certificate metadata into the key store. For instructions on importing the certificate metadata, see the code sample in [Registering Pre-existing Keys with AWS CloudHSM Key Store](register-pre-existing-keys-with-keystore.md).

The certificate chain must be verifiable. If you can't verify the certificate, you might need to import the signing (certificate authority) certificate into the key store so the chain can be verified.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
