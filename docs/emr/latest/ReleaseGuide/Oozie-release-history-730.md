---
source_url: https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Oozie-release-history-730.html
---

# Amazon EMR 7.3.0 - Oozie release notes
<a name="Oozie-release-history-730"></a>

## Amazon EMR 7.3.0 - Oozie changes
<a name="Oozie-release-history-changes-730"></a>

| Type | Description |
| --- | --- |
| Upgrade | [OOZIE-3675](https://issues.apache.org/jira/browse/OOZIE-3675): Upgrade Mockito from 2 to 3.11.2 |
| Improvement | [OOZIE-3674](https://issues.apache.org/jira/browse/OOZIE-3674): Add a --insecure like parameter to Oozie client so it can ignore certificate errors |
| Improvement | [OOZIE-3673](https://issues.apache.org/jira/browse/OOZIE-3673): Add possibility to configure custom SSL/TLS protocols when executing an email action |
| Improvement | [OOZIE-3677](https://issues.apache.org/jira/browse/OOZIE-3677): Oozie should accept a keyStoreType and trustStoreType property in oozie-site.xml |

## Amazon EMR 7.3.0 - New configurations
<a name="Oozie-release-history-changes-730-new-configs"></a>

| Classification | Name | Default | Description |
| --- | --- | --- | --- |
| oozie-site | oozie.email.smtp.ssl.protocols |  | String property that has the supported protocols enumerated separate by space. The default empty value has no effect. e.g. "TLSv1 TLSv1.1 TLSv1.2" |
| oozie-site | oozie.https.truststore.type |  | Truststore file type e.g. jks |
| oozie-site | oozie.https.keystore.type |  | Keystore file type e.g. jks |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
