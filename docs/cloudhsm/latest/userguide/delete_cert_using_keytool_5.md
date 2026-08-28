---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/delete_cert_using_keytool_5.html
---

# Use keytool to delete certificates from AWS CloudHSM key store
<a name="delete_cert_using_keytool_5"></a>

The following command shows an example of how to delete a AWS CloudHSM certificate from a Java keytool key store.

------
#### [ Linux ]

```
$ keytool -delete -alias mydomain \
	-keystore example_keystore.store \
	-storetype CLOUDHSM \
	-J-classpath '-J/opt/cloudhsm/java/*'
```

------
#### [ Windows ]

```
PS C:\> keytool -delete -alias mydomain `
	-keystore example_keystore.store `
	-storetype CLOUDHSM `
	-J-classpath '-J"C:\Program Files\Amazon\CloudHSM\java\*"'
```

------

If you connect multiple client instances to your AWS CloudHSM cluster, deleting a certificate on one client instance’s key store won't automatically remove the certificate from other client instances. You must delete the certificate on each client instance.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
