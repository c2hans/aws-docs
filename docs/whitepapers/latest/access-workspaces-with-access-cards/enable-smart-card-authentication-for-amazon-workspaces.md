---
source_url: https://docs.aws.amazon.com/whitepapers/latest/access-workspaces-with-access-cards/enable-smart-card-authentication-for-amazon-workspaces.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Enable smart card authentication for Amazon WorkSpaces
<a name="enable-smart-card-authentication-for-amazon-workspaces"></a>

To enable smart card authentication for Amazon WorkSpaces in AD Connector, use the following CLI command:

```
     aws ds enable-client-authentication --directory-id your_directory_id --type SmartCard
```

If successful, AD Connector returns an HTTP 200 response with an empty HTTP body.

![A screenshot showing enabled smart card authentication on AD Connector.](http://docs.aws.amazon.com/whitepapers/latest/access-workspaces-with-access-cards/images/workspaces-smartcard17.png)

*Enable smart card authentication on AD Connector *

For details about enabling smart card authentication in AD Connector, see [Enable smart card authentication in AD Connector](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ad_connector_clientauth.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
