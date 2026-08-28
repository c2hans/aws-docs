---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/topics-cli.html
---

# Work with Quick Sight Topics using the Amazon Quick Sight APIs
<a name="topics-cli"></a>

|  |
| --- |
|  Applies to:  Enterprise Edition  |

|  |
| --- |
|    Intended audience:  Amazon Quick developers  |

Use this section to learn how to work with Quick Sight Topics using the Amazon Quick Sight command line interface (CLI).

**Prerequisites**

Before you begin, make sure that you have an AWS Identity and Access Management (IAM) role that grants the CLI user access to call the Quick Sight API operations. The following table shows which permissions must be added to the IAM policy to use specific API operations.

| API operation | IAM policy |
| --- | --- |
| `CreateTopic` | `quicksight:CreateTopic`<br />`quicksight:PassDataSet` |
| `ListTopics` | `quicksight:ListTopics` |
| `DescribeTopic` | `quicksight:DescribeTopic` |
| `UpdateTopic` | `quicksight:UpdateTopic`<br />`quicksight:PassDataSet` |
| `DeleteTopic` | `quicksight:DeleteTopic` |
| `UpdateTopicPermissions` | `quicksight:UpdateTopicPermissions` |
| `DescribeTopicPermissions` | `quicksight:DescribeTopicPermissions` |
| `CreateTopicRefreshSchedule` | `quicksight:CreateTopicRefreshSchedule` |
| `ListTopicRefreshSchedules` | `quicksight:ListTopicRefreshSchedules` |
| `DescribeTopicRefreshSchedule` | `quicksight:DescribeTopicRefreshSchedule` |
| `UpdateTopicRefreshSchedule` | `quicksight:UpdateTopicRefreshSchedule` |
| `DeleteTopicRefreshSchedule` | `quicksight:DeleteTopicRefreshSchedule` |

The following example creates a new Topic.

```
aws quicksight create-topic
--aws-account-id {{AWSACCOUNTID}}
--topic-id {{TOPICID}}
--topic {{TOPIC}}
```

The following example updates a Topic.

```
aws quicksight update-topic
--aws-account-id {{AWSACCOUNTID}}
--topic-id {{TOPICID}}
--topic {{TOPIC}}
```

The following example provides a list of all Topics in an account.

```
aws quicksight list-topics
--aws-account-id {{AWSACCOUNTID}}
```

The following example deletes a Topic.

```
aws quicksight delete-topic
--aws-account-id {{AWSACCOUNTID}}
--topic-id {{TOPICID}}
```

The following example provides information about how a Topic was configured.

```
aws quicksight describe-topic
--aws-account-id {{AWSACCOUNTID}}
--topic-id {{TOPICID}}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quick` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
