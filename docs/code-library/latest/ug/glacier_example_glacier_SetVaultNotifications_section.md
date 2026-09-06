---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/glacier_example_glacier_SetVaultNotifications_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `SetVaultNotifications` with an AWS SDK or CLI
<a name="glacier_example_glacier_SetVaultNotifications_section"></a>

The following code examples show how to use `SetVaultNotifications`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example:
+  [Archive a file, get notifications, and initiate a job](glacier_example_glacier_Usage_UploadNotifyInitiate_section.md)

------
#### [ CLI ]

**AWS CLI**
The following command configures SNS notifications for a vault named `my-vault`:

```
aws glacier set{{-}}vault-notifications --account-id - --vault-name {{my-vault}} --vault-notification-config {{file://notificationconfig.json}}
```
`notificationconfig.json` is a JSON file in the current folder that specifies an SNS topic and the events to publish:

```
{
  "SNSTopic": "arn:aws:sns:us-west-2:0123456789012:my-vault",
  "Events": ["ArchiveRetrievalCompleted", "InventoryRetrievalCompleted"]
}
```
Amazon Glacier requires an account ID argument when performing operations, but you can use a hyphen to specify the in-use account.
+  For API details, see [SetVaultNotifications](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/set-vault-notifications.html) in *AWS CLI Command Reference*.

------
#### [ Python ]

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/glacier#code-examples).

```
class GlacierWrapper:
    """Encapsulates Amazon S3 Glacier API operations."""

    def __init__(self, glacier_resource):
        """
        :param glacier_resource: A Boto3 Amazon S3 Glacier resource.
        """
        self.glacier_resource = glacier_resource

    def set_notifications(self, vault, sns_topic_arn):
        """
        Sets an Amazon Simple Notification Service (Amazon SNS) topic as a target
        for notifications. Amazon S3 Glacier publishes messages to this topic for
        the configured list of events.

        :param vault: The vault to set up to publish notifications.
        :param sns_topic_arn: The Amazon Resource Name (ARN) of the topic that
                              receives notifications.
        :return: Data about the new notification configuration.
        """
        try:
            notification = self.glacier_resource.Notification("-", vault.name)
            notification.set(
                vaultNotificationConfig={
                    "SNSTopic": sns_topic_arn,
                    "Events": [
                        "ArchiveRetrievalCompleted",
                        "InventoryRetrievalCompleted",
                    ],
                }
            )
            logger.info(
                "Notifications will be sent to %s for events %s from %s.",
                notification.sns_topic,
                notification.events,
                notification.vault_name,
            )
        except ClientError:
            logger.exception(
                "Couldn't set notifications to %s on %s.", sns_topic_arn, vault.name
            )
            raise
        else:
            return notification
```
+  For API details, see [SetVaultNotifications](https://docs.aws.amazon.com/goto/boto3/glacier-2012-06-01/SetVaultNotifications) in *AWS SDK for Python (Boto3) API Reference*.

------
