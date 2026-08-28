---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/import_cert_using_keytool_5.html
---

# Use keytool to import intermediate and root certificates into AWS CloudHSM key store
<a name="import_cert_using_keytool_5"></a>

To import a CA certificate in AWS CloudHSM, you must enable verification of a full certificate chain on a newly imported certificate. The following command shows an example.

------
#### [ Linux ]

```
$ keytool -import -trustcacerts -alias rootCAcert \
	-file rootCAcert.cert -keystore example_keystore.store \
	-storetype CLOUDHSM \
	-J-classpath '-J/opt/cloudhsm/java/*'
```

------
#### [ Windows ]

```
PS C:\> keytool -import -trustcacerts -alias rootCAcert `
	-file rootCAcert.cert -keystore example_keystore.store `
	-storetype CLOUDHSM `
	-J-classpath '-J"C:\Program Files\Amazon\CloudHSM\java\*"'
```

------

If you connect multiple client instances to your AWS CloudHSM cluster, importing a certificate on one client instance’s key store won't automatically make the certificate available on other client instances. You must import the certificate on each client instance.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
