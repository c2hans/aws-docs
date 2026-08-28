---
source_url: https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-ranger-admin.html
---

# Set up a Ranger Admin server to integrate with Amazon EMR
<a name="emr-ranger-admin"></a>

For Amazon EMR integration, the Apache Ranger application plugins must communicate with the Admin server using TLS/SSL.

**Prerequisite: Ranger Admin Server SSL Enablement**

Apache Ranger on Amazon EMR requires two-way SSL communication between plugins and the Ranger Admin server. To ensure that plugins communicate with the Apache Ranger server over SSL, enable the following attribute within ranger-admin-site.xml on the Ranger Admin server.

```
<property>
    <name>ranger.service.https.attrib.ssl.enabled</name>
    <value>true</value>
</property>
```

In addition, the following configurations are needed.

```
<property>
    <name>ranger.https.attrib.keystore.file</name>
    <value>_{{<PATH_TO_KEYSTORE>}}_</value>
</property>

<property>
    <name>ranger.service.https.attrib.keystore.file</name>
    <value>_{{<PATH_TO_KEYSTORE>}}_</value>
</property>

<property>
    <name>ranger.service.https.attrib.keystore.pass</name>
    <value>_{{<KEYSTORE_PASSWORD>}}_</value>
</property>

<property>
    <name>ranger.service.https.attrib.keystore.keyalias</name>
    <value>{{<PRIVATE_CERTIFICATE_KEY_ALIAS>}}</value>
</property>

<property>
    <name>ranger.service.https.attrib.clientAuth</name>
    <value>want</value>
</property>

<property>
    <name>ranger.service.https.port</name>
    <value>6182</value>
</property>
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
