---
source_url: https://docs.aws.amazon.com/dtconsole/latest/userguide/repositorylinks-list.html
---

# List repository links
<a name="repositorylinks-list"></a>

You can use the **list-repository-links** command in the AWS Command Line Interface (AWS CLI) to list repository links for your account.

**To list repository links**

1. Open a terminal (Linux, macOS, or Unix) or command prompt (Windows). Use the AWS CLI to run the **list-repository-links ** command.

   ```
   aws codeconnections list-repository-links
   ```

1. This command returns the following output.

   ```
   {
       "RepositoryLinks": [
           {
               "ConnectionArn": "arn:aws:codestar-connections:us-east-1:{{account_id}}:connection/001f5be2-a661-46a4-b96b-4d277cac8b6e",
               "OwnerId": "{{owner_id}}",
               "ProviderType": "GitHub",
               "RepositoryLinkArn": "arn:aws:codestar-connections:us-east-1:{{account_id}}:repository-link/6053346f-8a33-4edb-9397-10394b695173",
               "RepositoryLinkId": "6053346f-8a33-4edb-9397-10394b695173",
               "RepositoryName": "MyRepo",
               "Tags": []
           }
       ]
   }
   ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Developer Tools Console. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dtconsole` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
