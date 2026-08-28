---
source_url: https://docs.aws.amazon.com/privateca/latest/userguide/c4adTroubleshootingUpdatedTemplate.html
---

# Troubleshoot Connector for AD template update issues
<a name="c4adTroubleshootingUpdatedTemplate"></a>

If you made changes to your template or group access control entry, but you don't see the changes, this might be due to policy caching. AWS Private CA applies template to your policy when your client refreshes the policy cache, which is every eight hours. When your client refreshes the cache, it queries the connector for available templates. In the case of **auto-enrollment refresh, the client issues certificates that match either or both of the following conditions:
+ The certificate is within the renewal period.
+ The certificate isn't present on the client device.

For *manual refresh*, the client will query the connector, and you must set the template to issue.

If you're debugging, you can manually clear the policy cache to immediately see the template changes. To do so, run the following Powershell command on your client.

```
certutil -f -user -policyserver * -policycache delete
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Private Certificate Authority. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query privateca` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
