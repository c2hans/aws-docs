---
source_url: https://docs.aws.amazon.com/appsync/latest/eventapi/adding-a-data-source.html
---

# Adding a data source
<a name="adding-a-data-source"></a>

The following instructions describe how to add a data source to an Event API. To learn how to use event handlers to interact with your data source, see [Writing event handlers](writing-event-handlers.md).

------
#### [ Console ]

1. Sign in to the AWS Management Console and open the [AppSync console](https://console.aws.amazon.com/appsync/).

   1. Choose your API in the **Dashboard**.

   1. In the **Sidebar**, choose **Data Sources**.

1. Choose **Create data source**.

   1. Give your data source a name. You can also give it a description, but that's optional.

   1. Choose your **Data source type**.

   1. For DynamoDB, you'll have to choose your Region, then the table in the Region. You can dictate interaction rules with your table by choosing to make a new generic table role or importing an existing role for the table. You can enable [versioning](https://docs.aws.amazon.com/appsync/latest/devguide/conflict-detection-and-sync.html), which can automatically create versions of data for each request when multiple clients are trying to update data at the same time. Versioning is used to keep and maintain multiple variants of data for conflict detection and resolution purposes. You can also enable automatic schema generation, which takes your data source and generates some of the CRUD, `List`, and `Query` operations needed to access it in your schema.

      For OpenSearch Service, you'll have to choose your Region, then the domain (cluster) in the Region. You can dictate interaction rules with your domain by choosing to make a new generic table role or importing an existing role for the table.

      For Lambda, you'll have to choose your Region, then the ARN of the Lambda function in the Region. You can dictate interaction rules with your Lambda function by choosing to make a new generic table role or importing an existing role for the table.

      For HTTP, you'll have to enter your HTTP endpoint.

      For EventBridge, you'll have to choose your Region, then the event bus in the Region. You can dictate interaction rules with your event bus by choosing to make a new generic table role or importing an existing role for the table.

      For Amazon RDS, you'll have to choose your Region, then the secret store (username and password), database name, and schema.
**Note**
If you're importing existing roles, they need a trust policy. For more information, see the [IAM trust policy](#iam-trust-policy.title).

1. Choose **Create**.
**Note**
Alternatively, if you're creating a DynamoDB data source, you can go to the **Schema** page in the console, choose **Create Resources** at the top of the page, then fill out a predefined model to convert into a table. In this option, you will fill out or import the base type, configure the basic table data including the partition key, and review the schema changes.

------
#### [ CLI ]
+ Create your data source by running the [`create-data-source`](https://docs.aws.amazon.com/cli/latest/reference/appsync/create-data-source.html) command.

  You'll need to enter the following parameters for this command:

  1. The `api-id` of your API.

  1. The `name` of your table.

  1. The `type` of data source. Depending on the data source type you choose, you might need to enter a `service-role-arn` and a `-config` tag.

  An example command will look like the following:

  ```
   aws appsync create-data-source --api-id abcdefghijklmnopqrstuvwxyz --name data_source_name --type data_source_type --service-role-arn arn:aws:iam::107289374856:role/role_name --[data_source_type]-config {params}
  ```

------

## Creating an IAM trust policy for a data source
<a name="iam-trust-policy"></a>

If you’re using an existing IAM role for your data source, you need to grant that role the appropriate permissions to perform operations on your AWS resource, such as `PutItem` on an Amazon DynamoDB table. You also need to modify the trust policy on that role to allow AWS AppSync to use it for resource access as shown in the following example policy:

------
#### [ JSON ]

****

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
        "Effect": "Allow",
        "Principal": {
            "Service": "appsync.amazonaws.com"
        },
        "Action": "sts:AssumeRole"
        }
    ]
}
```

------

You can also add conditions to your trust policy to limit access to the data source as desired. Currently, `SourceArn` and `SourceAccount` keys can be used in these conditions. For example, the following policy limits access to your data source to the account `123456789012`:

------
#### [ JSON ]

****

```
{
  "Version":"2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "appsync.amazonaws.com"
      },
      "Action": "sts:AssumeRole",
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "123456789012"
        }
      }
    }
  ]
}
```

------

Alternatively, you can limit access to a data source to a specific API, such as `abcdefghijklmnopq`, using the following policy:

------
#### [ JSON ]

****

```
{
  "Version":"2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "appsync.amazonaws.com"
      },
      "Action": "sts:AssumeRole",
      "Condition": {
        "ArnEquals": {
          "aws:SourceArn": "arn:aws:appsync:us-west-2:123456789012:apis/abcdefghijklmnopq"
        }
      }
    }
  ]
}
```

------

You can limit access to all AWS AppSync APIs from a specific region, such as `us-east-1`, using the following policy:

------
#### [ JSON ]

****

```
{
  "Version":"2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "appsync.amazonaws.com"
      },
      "Action": "sts:AssumeRole",
      "Condition": {
        "ArnEquals": {
          "aws:SourceArn": "arn:aws:appsync:us-east-1:123456789012:apis/*"
        }
      }
    }
  ]
}
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS AppSync. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appsync` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
