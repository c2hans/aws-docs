---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/export_cert_using_keytool_5.html
---

# Export a certificate from AWS CloudHSM using keytool
<a name="export_cert_using_keytool_5"></a>

The following example generates a certificate in binary X.509 format. To export a human readable certificate from AWS CloudHSM, add `-rfc` to the `-exportcert` command.

------
#### [ Linux ]

```
$ keytool -exportcert -alias {{<key pair label>}} \
	-file my_exported_certificate.crt \
	-keystore example_keystore.store \
	-storetype CLOUDHSM \
	-J-classpath '-J/opt/cloudhsm/java/*'
```

------
#### [ Windows ]

```
PS C:\> keytool -exportcert -alias {{<key pair label>}} `
	-file my_exported_certificate.crt `
	-keystore example_keystore.store `
	-storetype CLOUDHSM `
	-J-classpath '-J"C:\Program Files\Amazon\CloudHSM\java\*"'
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
