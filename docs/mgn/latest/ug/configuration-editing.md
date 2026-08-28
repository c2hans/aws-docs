---
source_url: https://docs.aws.amazon.com/mgn/latest/ug/configuration-editing.html
---

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# Editing your configuration
<a name="configuration-editing"></a>

You can use the **Import and Export** feature to edit your server configuration, including bulk changes:

1. Export the data to a CSV file.

1. Edit your file.

1. Import the edited file back into the service.

**Note**
 When editing a CSV file in Microsoft Excel be sure to save it in the **MS-DOS** CSV data format.

When processing the inventory file import, values provided in the file overwrite existing values. *Cells that are empty are ignored*. This allows you, when editing the file, to include values only in the inventory columns that you want to overwrite.

To delete a value replace the existing value with the string `[RESET_VALUE]` and then save and upload the file. This clears the value in the MGN resource or the Amazon EC2 launch template.

Using `[RESET_VALUE]` is available for these parameters:
+ mgn:launch:iam-instance-profile:name
+ mgn:launch:nic:0:network-interface-id
+ mgn:launch:nic:0:private-ip:0
+ mgn:launch:nic:0:security-group-id:0
+ mgn:launch:nic:0:subnet-id
+ mgn:launch:tag:instance:key1
+ mgn:launch:volume:/dev/sda:type

You can also delete tag fields. To delete the tag value replace the existing value with the string `[RESET_VALUE]`. To delete both the key and the value replace the existing value with the string `[DELETE_TAG]`.

**Note**
Tags that are created by the service, such as `AWSApplicationMigrationServiceManaged`, can't be changed or deleted. Attempting to do so results in an error.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Transform MGN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mgn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
