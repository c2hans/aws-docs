---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/glacier_example_glacier_DeleteVaultNotifications_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DeleteVaultNotifications` with an AWS SDK or CLI
<a name="glacier_example_glacier_DeleteVaultNotifications_section"></a>

The following code examples show how to use `DeleteVaultNotifications`.

------
#### [ CLI ]

**AWS CLI**
**To remove the SNS notifications for a vault**
The following `delete-vault-notifications` example removes notifications sent by Amazon Simple Notification Service (Amazon SNS) for the specified vault.

```
aws glacier delete-vault-notifications \
    --account-id {{111122223333}} \
    --vault-name {{example_vault}}
```
This command produces no output.
+  For API details, see [DeleteVaultNotifications](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/delete-vault-notifications.html) in *AWS CLI Command Reference*.

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

    @staticmethod
    def stop_notifications(notification):
        """
        Stops notifications to the configured Amazon SNS topic.

        :param notification: The notification configuration to remove.
        """
        try:
            notification.delete()
            logger.info("Notifications stopped.")
        except ClientError:
            logger.exception("Couldn't stop notifications.")
            raise
```
+  For API details, see [DeleteVaultNotifications](https://docs.aws.amazon.com/goto/boto3/glacier-2012-06-01/DeleteVaultNotifications) in *AWS SDK for Python (Boto3) API Reference*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
