---
source_url: https://docs.aws.amazon.com/ses/latest/dg/setting-up-address-lists.html
---

# Create and manage Address Lists

Create an empty Address List, then add email addresses, domains, or supported wildcard patterns. You can add one member at a time or import members from a CSV or JSON file.

## Permissions for address lists
<a name="eb-addlist-permissions"></a>

The principal that manages an Address List needs permission for the API operations that it uses. In the following IAM policy, replace the AWS Region and account ID with your own values. The policy allows the principal to manage address lists and their members in one account and Region.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "ManageAddressLists",
      "Effect": "Allow",
      "Action": [
        "ses:CreateAddressList",
        "ses:GetAddressList",
        "ses:DeleteAddressList",
        "ses:GetMemberOfAddressList",
        "ses:ListMembersOfAddressList",
        "ses:RegisterMemberToAddressList",
        "ses:DeregisterMemberFromAddressList",
        "ses:CreateAddressListImportJob",
        "ses:GetAddressListImportJob",
        "ses:ListAddressListImportJobs",
        "ses:StartAddressListImportJob",
        "ses:StopAddressListImportJob",
        "ses:TagResource",
        "ses:UntagResource",
        "ses:ListTagsForResource"
      ],
      "Resource": "arn:aws:ses:{{us-east-1}}:{{123456789012}}:mailmanager-address-list/*"
    },
    {
      "Sid": "ListAddressLists",
      "Effect": "Allow",
      "Action": "ses:ListAddressLists",
      "Resource": "*"
    }
  ]
}
```

Address-list operations support resource-level permissions on the `mailmanager-address-list` resource type. You can use `aws:RequestTag`, `aws:ResourceTag`, and `aws:TagKeys` conditions to control access by tag.

## Creating and populating an Address List
<a name="creating-address-lists"></a>

**To create and populate an Address List in the SES console**

1. Sign in to the AWS Management Console and open the Amazon SES console at [https://console.aws.amazon.com/ses/](https://console.aws.amazon.com/ses/).

1. In the navigation pane, under **Mail Manager**, choose **Address Lists**.

1. Choose **Create address list**.

1. Enter a unique name for the list.

1. Choose **Manual entry** to enter members directly, or choose **Bulk upload** to upload a CSV or JSON file.

1. Choose **Create address list**.

To create an empty Address List with the AWS CLI, replace the AWS Region and list name with your own values.

```bash
PROMPT> aws mailmanager create-address-list \
  --region {{us-east-1}} \
  --address-list-name {{valid-inbound-recipients}}
```

The command returns an `AddressListId`. The following examples use `al-0123456789abcdef`.

### Choosing address-list member formats
<a name="eb-addlist-member-formats"></a>

The following table shows supported member formats and their matching boundaries.

| Member | Matches | Does not match |
| --- | --- | --- |
| mary\_major@example.com | The exact mailbox | Other mailboxes or subaddress extensions |
| example.com | Any mailbox at the exact domain | Mailboxes at subdomains such as user@dept.example.com |
| \*@example.com | Any mailbox at the exact domain | Mailboxes at subdomains |
| orders\*@example.com | orders@example.com, orders\+tag@example.com, and orders-archive@example.com | A local part that does not start with orders |
| \*.example.com | Any mailbox at a subdomain such as user@dept.example.com | A mailbox at the parent domain, such as user@example.com |
| orders@\*.example.com | The orders mailbox at a subdomain | Other local parts or the parent domain |

A member can contain one asterisk (`*`). For a local-part prefix such as `orders*@example.com`, the prefix before the asterisk can contain up to 19 characters. For `*.example.com` or `orders@*.example.com`, the suffix after `*.` can contain 2–9 domain labels.

**A local-part wildcard is not limited to plus addressing**
`orders*@example.com` matches every local part that starts with `orders`. It matches `orders+tag@example.com`, but it also matches `orders-archive@example.com` and `ordersbackup@example.com`. Use an exact address when those additional matches are not intended.

### Adding and removing individual members
<a name="eb-addlist-add-remove-members"></a>

In the following commands, replace the AWS Region, Address List ID, and member with your own values.

```bash
PROMPT> aws mailmanager register-member-to-address-list \
  --region {{us-east-1}} \
  --address-list-id {{al-0123456789abcdef}} \
  --address {{orders@example.com}}
```

```bash
PROMPT> aws mailmanager deregister-member-from-address-list \
  --region {{us-east-1}} \
  --address-list-id {{al-0123456789abcdef}} \
  --address {{orders@example.com}}
```

### Importing members in bulk
<a name="eb-addlist-bulk-import"></a>

A CSV file requires an `address` header.

```
address
orders@example.com
*@partner.example
*.customer.example
```

A JSON file requires an `items` list containing an `address` for each member.

```json
{
  "items": [
    {"address": "orders@example.com"},
    {"address": "*@partner.example"},
    {"address": "*.customer.example"}
  ]
}
```

In the following commands, replace the AWS Region, Address List ID, job name, input path, pre-signed URL, and job ID with your own values.

```bash
PROMPT> aws mailmanager create-address-list-import-job \
  --region {{us-east-1}} \
  --address-list-id {{al-0123456789abcdef}} \
  --name {{november-domain-import}} \
  --import-data-format ImportDataType=CSV
```

The command returns a `JobId` and `PreSignedUrl`. Upload the input file to that URL.

```bash
PROMPT> curl --request PUT \
  --upload-file {{./approved-domains.csv}} \
  '{{pre-signed-url}}'
```

```bash
PROMPT> aws mailmanager start-address-list-import-job \
  --region {{us-east-1}} \
  --job-id {{job-0123456789abcdef}}
```

Run the following command until `Status` is `COMPLETED`, `FAILED`, or `STOPPED`.

```bash
PROMPT> aws mailmanager get-address-list-import-job \
  --region {{us-east-1}} \
  --job-id {{job-0123456789abcdef}} \
  --query '{Status:Status,Imported:ImportedItemsCount,Failed:FailedItemsCount,Error:Error}'
```

**Note**
The pre-signed upload URL expires after 15 minutes. Treat the URL as sensitive because it authorizes an upload. The import file can be up to 10 MiB. Only one import job can process a given Address List at a time.

A completed job can report both imported and failed items. Review `FailedItemsCount` and `Error` before using the list in a traffic policy or rule.

## Managing Address Lists
<a name="managing-address-lists"></a>

### Updating an Address List
<a name="updating-address-lists"></a>

Add and remove members with the procedures in [Adding and removing individual members](#eb-addlist-add-remove-members). To add or remove tags in the SES console, open the list and choose **Manage tags**.

### Viewing Address List details and members
<a name="viewing-address-lists"></a>

In the following commands, replace the AWS Region and Address List ID with your own values.

```bash
PROMPT> aws mailmanager get-address-list \
  --region {{us-east-1}} \
  --address-list-id {{al-0123456789abcdef}}
```

```bash
PROMPT> aws mailmanager list-members-of-address-list \
  --region {{us-east-1}} \
  --address-list-id {{al-0123456789abcdef}} \
  --filter AddressPrefix={{orders}}
```

### Deleting an Address List
<a name="deleting-address-lists"></a>

You cannot delete an Address List while a rule condition, an `Unless` condition, or a traffic-policy condition references it. Remove every reference before deleting the list.

In the following command, replace the AWS Region and Address List ID with your own values.

```bash
PROMPT> aws mailmanager delete-address-list \
  --region {{us-east-1}} \
  --address-list-id {{al-0123456789abcdef}}
```

## Address-list constraints
<a name="eb-addlist-constraints"></a>
+ A member can contain 3–320 characters.
+ An address-list membership condition can reference one Address List.
+ Nested Address Lists are not supported.
