---
source_url: https://docs.aws.amazon.com/firehose/latest/dev/secrets-manager-whats-secret.html
---

# Understand secrets
<a name="secrets-manager-whats-secret"></a>

A secret can be a password, a set of credentials such as a user name and password, an OAuth token, or other secret information that you store in an encrypted form in Secrets Manager.

For each destination, you must specify the secret key-value pair in the correct JSON format as shown in the following section. Amazon Data Firehose will fail to connect to your destination if your secret doesn't have the correct JSON format as per the destination.

**Format of secret for databases such as MySQL and PostgreSQL**

```
{
    "username":  "<{{username}}>",
    "password":  "<{{password}}>"
}
```

**Format of secret for Amazon Redshift Provisioned cluster and Amazon Redshift Serverless workgroup**

```
{
    "username":  "<{{username}}>",
    "password":  "<{{password}}>"
}
```

**Format of secret for Splunk**

```
{
    "hec_token":  "<{{hec token}}>"
}
```

**Format of secret for Snowflake**

```
{
    "user":  "<{{snowflake-username}}>",
    "private_key":  "<{{snowflake-private-key}}>", // without the beginning and ending private key, remove all spaces and newlines
    "key_passphrase":  "<{{snowflake-private-key-passphrase}}>" // optional
}
```

**Format of secret for HTTP endpoint, Coralogix, Datadog, Dynatrace, Elastic, Honeycomb, LogicMonitor, Logz.io, MongoDB Cloud, and New Relic**

```
{
    "api_key":  "<{{apikey}}>"
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Data Firehose. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query firehose` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
