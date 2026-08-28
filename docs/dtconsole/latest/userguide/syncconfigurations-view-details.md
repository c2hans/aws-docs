---
source_url: https://docs.aws.amazon.com/dtconsole/latest/userguide/syncconfigurations-view-details.html
---

# View sync configuration details
<a name="syncconfigurations-view-details"></a>

You can use the **get-sync-configuration** command in the AWS Command Line Interface (AWS CLI) to view details for a sync configuration.

**To view details for a sync configuration**

1. Open a terminal (Linux, macOS, or Unix) or command prompt (Windows). Use the AWS CLI to run the **get-sync-configuration** command, specifying the repository link ID.

   ```
   aws codeconnections get-sync-configuration --sync-type CFN_STACK_SYNC --resource-name mystack
   ```

1. This command returns the following output.

   ```
   {
       "SyncConfiguration": {
           "Branch": "main",
           "ConfigFile": "filename",
           "OwnerId": "{{owner_id}}",
           "ProviderType": "GitHub",
           "RepositoryLinkId": "be8f2017-b016-4a77-87b4-608054f70e77",
           "RepositoryName": "MyRepo",
           "ResourceName": "mystack",
           "RoleArn": "arn:aws:iam::{{account_id}}:role/myrole",
           "SyncType": "CFN_STACK_SYNC"
       }
   }
   ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Developer Tools Console. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dtconsole` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
