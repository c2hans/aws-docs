---
source_url: https://docs.aws.amazon.com/glue/latest/dg/smartsheet-configuring-connections.html
---

# Configuring Smartsheet connections
<a name="smartsheet-configuring-connections"></a>

 Smartsheet supports `AUTHORIZATION_CODE` grant type for OAuth2.

This grant type is considered “three-legged” `OAuth` as it relies on redirecting users to the third-party authorization server to authenticate the user. Users may opt to create their own connected app in Smartsheet and provide their own client ID and client secret when creating connections through the AWS Glue console. In this scenario, they will still be redirected to Smartsheet to login and authorize AWS Glue to access their resources.

This grant type results in a refresh token and access token. The access token is short lived, and may be refreshed automatically without user interaction using the refresh token.

For public Smartsheet documentation on creating a connected app for AUTHORIZATION\_CODE OAuth flow, see [Smartsheet APIs](https://smartsheet.redoc.ly/#section/OAuth-Walkthrough) .

To configure a Smartsheet connection:

1. In AWS Secrets Manager, create a secret with the following details:

   For customer managed connected app – Secret should contain the connected app Consumer Secret with `USER_MANAGED_CLIENT_APPLICATION_CLIENT_SECRET` as key.
**Note**
It is a must to create a secret per connection in AWS Glue.

1. In the AWS Glue Studio, create a connection under **Data Connections** by following the steps below:

   1. When selecting a **Connection type**, select Smartsheet.

   1. Provide the `instanceUrl` of the Smartsheet you want to connect to.

   1. Select the IAM role for which AWS Glue can assume and has permissions for following actions:

------
#### [ JSON ]

****

      ```
      {
        "Version":"2012-10-17",
        "Statement": [
          {
            "Effect": "Allow",
            "Action": [
              "secretsmanager:DescribeSecret",
              "secretsmanager:GetSecretValue",
              "secretsmanager:PutSecretValue",
              "ec2:CreateNetworkInterface",
              "ec2:DescribeNetworkInterfaces",
              "ec2:DeleteNetworkInterface"
            ],
            "Resource": "*"
          }
        ]
      }
      ```

------

   1. Select the `secretName` which you want to use for this connection in AWS Glue to put the tokens.

   1.  Select the network options if you want to use your network.

1. Grant the IAM role associated with your AWS Glue job permission to read `secretName`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
