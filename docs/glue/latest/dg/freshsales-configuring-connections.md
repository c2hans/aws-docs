---
source_url: https://docs.aws.amazon.com/glue/latest/dg/freshsales-configuring-connections.html
---

# Configuring Freshsales connections
<a name="freshsales-configuring-connections"></a>

Freshsales supports custom authentication.

For public Freshsales documentation on generating the required API keys for custom authentication, see [Authentication](https://developer.freshsales.io/api/#authentication).

To configure a Freshsales connection:

1. In AWS Secrets Manager, create a secret with the following details:

   1. For the customer managed connected app, the Secret should contain the connected app API key with `{{apiSecretKey}}` as key. The Secret also needs to contain another key-value pair with `{{apiKey}}` as key and `{{token}}` as value.

   1. Note: you must create a secret for your connections in AWS Glue.

1. In AWS Glue Glue Studio, create a connection under **Data Connections** by following the steps below:

   1. When selecting a **Data Source**, select Freshsales.

   1. Provide the `INSTANCE_URL` of the Freshsales account you want to connect to.

   1. Select the AWS IAM role which AWS Glue can assume and has permissions for following actions:

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

   1. Select the network options if you want to use your network.

1. Grant the IAM role associated with your AWS Glue job permission to read `secretName`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
