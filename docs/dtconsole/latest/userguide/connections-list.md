---
source_url: https://docs.aws.amazon.com/dtconsole/latest/userguide/connections-list.html
---

# List connections
<a name="connections-list"></a>

You can use the Developer Tools console or the **list-connections** command in the AWS Command Line Interface (AWS CLI) to view a list of connections in your account.

## List connections (console)
<a name="connections-list-console"></a>

**To list connections**

1. Open the Developer Tools console at [https://console.aws.amazon.com/codesuite/settings/connections](https://console.aws.amazon.com/codesuite/settings/connections).

1. Choose **Settings > Connections**.

1. View the name, status, and ARN for your connections.

## List connections (CLI)
<a name="connections-list-cli"></a>

You can use the AWS CLI to list your connections to third-party code repositories. For a connection associated to a host resource, such as connections to GitHub Enteprise Server, the output additionally returns the host ARN.

To do this, use the **list-connections** command.

**To list connections**
+ Open a terminal (Linux, macOS, or Unix) or command prompt (Windows), and use the AWS CLI to run the **list-connections** command.

  ```
  aws codeconnections list-connections --provider-type Bitbucket
  --max-results 5 --next-token: {{next-token}}
  ```

  This command returns the following output.

  ```
  {
       "Connections": [
           {
               "ConnectionName": "my-connection",
               "ProviderType": "Bitbucket",
               "Status": "PENDING",
               "ARN": "arn:aws:codeconnections:us-west-2:{{account_id}}:connection/aEXAMPLE-8aad-4d5d-8878-dfcab0bc441f",
               "OwnerAccountId": "{{account_id}}"
           },
           {
               "ConnectionName": "my-other-connection",
               "ProviderType": "Bitbucket",
               "Status": "AVAILABLE",
               "ARN": "arn:aws:codeconnections:us-west-2:{{account_id}}:connection/aEXAMPLE-8aad-4d5d-8878-dfcab0bc441f",
               "OwnerAccountId": "{{account_id}}"
            },
        ],
       "NextToken": "{{next-token}}"
  }
  ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Developer Tools Console. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dtconsole` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
