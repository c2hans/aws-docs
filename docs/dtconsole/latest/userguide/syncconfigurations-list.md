---
source_url: https://docs.aws.amazon.com/dtconsole/latest/userguide/syncconfigurations-list.html
---

# List sync configurations
<a name="syncconfigurations-list"></a>

You can use the **list-sync-configurations** command in the AWS Command Line Interface (AWS CLI) to list repository links for your account.

**To list repository links**

1. Open a terminal (Linux, macOS, or Unix) or command prompt (Windows). Use the AWS CLI to run the **list-sync-configurations** command, specifying the sync type and repository link ID.

   ```
   aws codeconnections list-sync-configurations --repository-link-id 6053346f-8a33-4edb-9397-10394b695173  --sync-type CFN_STACK_SYNC
   ```

1. This command returns the following output.

   ```
   {
       "SyncConfigurations": [
           {
               "Branch": "main",
               "ConfigFile": "filename.yaml",
               "OwnerId": "{{owner_id}}",
               "ProviderType": "GitHub",
               "RepositoryLinkId": "6053346f-8a33-4edb-9397-10394b695173",
               "RepositoryName": "MyRepo",
               "ResourceName": "mystack",
               "RoleArn": "arn:aws:iam::{{account_id}}:role/myrole",
               "SyncType": "CFN_STACK_SYNC"
           }
       ]
   }
   ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Developer Tools Console. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dtconsole` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
