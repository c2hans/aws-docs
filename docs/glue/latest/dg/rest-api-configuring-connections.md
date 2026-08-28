---
source_url: https://docs.aws.amazon.com/glue/latest/dg/rest-api-configuring-connections.html
---

# Configuring a REST API connection
<a name="rest-api-configuring-connections"></a>

 In order to configure an AWS Glue REST API connector, you need to configure an AWS Glue connection type. This connection type contains details about the properties of how the REST data source operates and interprets things like authentication, requests, responses, pagination, validations, and entities/ metadata. For a comprehensive list of the required properties for an AWS Glue REST connection type, see the [ RegisterConnectionType](https://docs.aws.amazon.com/glue/latest/webapi/API_DescribeConnectionType.html) API and the steps for [Connecting to REST APIs](https://docs.aws.amazon.com/glue/latest/dg/rest-api-connections.html).

 When creating the REST API connector, the following policy is needed to allow relevant actions:

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "glue:RegisterConnectionType",
                "glue:ListConnectionTypes",
                "glue:DescribeConnectionType",
                "glue:CreateConnection",
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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
