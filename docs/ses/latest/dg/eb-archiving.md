---
source_url: https://docs.aws.amazon.com/ses/latest/dg/eb-archiving.html
---

# Email archiving

Email archiving stores copies of selected inbound and outbound email in managed, searchable storage. You can retain messages for a configured period, find messages with header and SMTP envelope filters, download individual messages, and export matching messages to an S3 bucket.

An archive can contain both sent and received email. Create the archive before you reference it from a Mail Manager rule or an SES configuration set.

You can add email to an archive from the following paths.
+ **Sent email archiving** – Archiving options on an SES configuration set submit a copy of each email sent with that configuration set.
+ **Received email archiving** – After an ingress endpoint's traffic policy accepts a recipient, the assigned rule set processes the email. An Archive action submits a copy of email selected by the rule's conditions to its target archive.

## How email enters an archive
<a name="eb-archiving-how-it-works"></a>

For inbound email, a traffic policy first accepts the recipient. The assigned rule set then evaluates its conditions and runs its actions in order. An Archive action submits a copy of the current message to its target archive. For outbound email, the archiving options on the configuration set submit a copy of each email sent with that configuration set.

The following diagram shows recommended patterns for using Archive with other rule actions.

![Three Mail Manager rule patterns process accepted email. The first matches recipients in example.com, adds a compliance header, archives the email, and relays it. The second matches suspicious email, archives it, and then drops it. The third uses one common Archive action before later rules route sales and support recipients. Archive action completion means Mail Manager accepted the archive request. It does not confirm durable storage.](https://docs.aws.amazon.com/ses/latest/dg/images/archiving-with-rules.png)

+ Place Add header before Archive when the archived copy must contain the added header.
+ Place Archive before Drop. Drop stops processing for the selected recipients, so later actions do not run for those recipients.
+ Use one Archive action in a common rule when every accepted message has the same retention requirements. Each Archive action that runs submits a separate archive request.
+ Use separate archives when email needs different retention periods or customer managed AWS KMS keys.

**Note**
Archive is asynchronous. Completion of the Archive action confirms that Mail Manager accepted the archive request. It does not confirm that durable storage has completed. `ActionFailurePolicy` does not cover a storage failure that occurs after the request is accepted. Verify customer managed AWS KMS key access and test representative searches before relying on the archive.

For Archive action fields and a complete rule-set example, see [Archive](eb-rules-actions.md#eb-rules-actions-archive). To configure outbound email archiving, see [Create a configuration set (console)](creating-configuration-sets.md#config-sets-create-console) and [Create a configuration set (AWS CLI)](creating-configuration-sets.md#config-sets-create-cli).

## Permissions for archives, searches, and exports
<a name="eb-archiving-permissions"></a>

Grant the calling principal the Mail Manager action that corresponds to each command. For example, archive creation uses `ses:CreateArchive`, search uses `ses:StartArchiveSearch`, `ses:GetArchiveSearch`, and `ses:GetArchiveSearchResults`, and export uses `ses:StartArchiveExport` and `ses:GetArchiveExport`. Grant `ses:GetArchiveMessage` and `ses:GetArchiveMessageContent` when the principal must retrieve message data.

A customer managed AWS KMS key and an export destination bucket require additional key and bucket permissions. For the required policies, see [Permission policies for Email archiving](eb-policies.md#eb-policies-archiving).

## Creating an archive with the AWS CLI
<a name="eb-archiving-create-cli"></a>

The following command creates an archive that retains email for seven years. Replace the AWS Region, archive name, account ID, and key ID with your values. Omit `--kms-key-arn` if you are not using a customer managed AWS KMS key.

```bash
PROMPT> aws mailmanager create-archive \
  --region {{us-east-1}} \
  --archive-name {{compliance-archive}} \
  --retention RetentionPeriod=SEVEN_YEARS \
  --kms-key-arn arn:aws:kms:{{us-east-1}}:{{123456789012}}:key/{{1234abcd-12ab-34cd-56ef-1234567890ab}}
```

The response contains the archive ID. Use this ID in Archive actions, searches, and exports.

```json
{
  "ArchiveId": "a-1a2b3c4d5e6f"
}
```

For all request members, retention values, and response fields, see [CreateArchive](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_CreateArchive.html) in the *SES Mail Manager API Reference*.

## Searching archived email with the AWS CLI
<a name="eb-archiving-search-api"></a>

The following diagram shows the search and export job flow. Both operations use the same time range and filter model.

![A search starts with StartArchiveSearch and returns a SearchId. The caller checks GetArchiveSearch until the state is COMPLETED, then calls GetArchiveSearchResults and uses an ArchivedMessageId with GetArchiveMessage or GetArchiveMessageContent. An export starts with StartArchiveExport and returns an ExportId. The caller checks GetArchiveExport until the state is COMPLETED, then reads EML files and optional metadata JSON files under an ExportId folder in Amazon S3.](https://docs.aws.amazon.com/ses/latest/dg/images/archive-search-export.png)

### Choosing search filters
<a name="eb-archiving-search-filters"></a>

Every condition in `Include` must match. Values within one string expression are alternatives. If any `Unless` condition matches, the message is excluded. `CONTAINS` performs a case-insensitive substring match.

The following table maps the available filter attributes to common search purposes.

| Attribute | Use it to search | Example |
| --- | --- | --- |
| TO, FROM, CC, or SUBJECT | Values in the corresponding message header. | SUBJECT contains invoice. |
| ENVELOPE\_TO | Actual SMTP envelope recipients, including a recipient that does not appear in the To or CC header. | ENVELOPE\_TO contains accounts-payable@example.com. |
| ENVELOPE\_FROM | The SMTP envelope sender. | ENVELOPE\_FROM contains bounces@example.net. |
| HAS\_ATTACHMENTS | Messages that have or do not have attachments. | HAS\_ATTACHMENTS IS\_TRUE. |

**Note**
Message ID is not an available search attribute. To locate a known message, narrow the time range with the available attributes and inspect the `MessageId` values returned in the result rows.

For the complete filter shape, see [ArchiveFilters](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_ArchiveFilters.html) and [ArchiveStringToEvaluate](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_ArchiveStringToEvaluate.html).

### Search examples
<a name="eb-archiving-search-examples"></a>

**Find messages from a sender that have attachments**
The following command finds up to 100 messages received during a seven-day period. Both Include conditions must match.

```bash
PROMPT> aws mailmanager start-archive-search \
  --region {{us-east-1}} \
  --archive-id {{a-1a2b3c4d5e6f}} \
  --from-timestamp 2026-11-16T00:00:00Z \
  --to-timestamp 2026-11-23T00:00:00Z \
  --max-results 100 \
  --filters '{
    "Include": [
      {
        "StringExpression": {
          "Evaluate": {"Attribute": "FROM"},
          "Operator": "CONTAINS",
          "Values": ["billing@example.com"]
        }
      },
      {
        "BooleanExpression": {
          "Evaluate": {"Attribute": "HAS_ATTACHMENTS"},
          "Operator": "IS_TRUE"
        }
      }
    ]
  }'
```

`StartArchiveSearch` returns a search ID.

```json
{
  "SearchId": "search-0123456789abcdef"
}
```

**Find email for either of two SMTP recipients**
Use one `ENVELOPE_TO` expression with two values. A message matches when either value occurs in an envelope recipient.

```json
{
  "Include": [{
    "StringExpression": {
      "Evaluate": {"Attribute": "ENVELOPE_TO"},
      "Operator": "CONTAINS",
      "Values": [
        "accounts-payable@example.com",
        "invoices@example.org"
      ]
    }
  }]
}
```

**Find invoice subjects but exclude automatic replies**
The Include condition requires `invoice`. Either Unless value excludes the message.

```json
{
  "Include": [{
    "StringExpression": {
      "Evaluate": {"Attribute": "SUBJECT"},
      "Operator": "CONTAINS",
      "Values": ["invoice"]
    }
  }],
  "Unless": [{
    "StringExpression": {
      "Evaluate": {"Attribute": "SUBJECT"},
      "Operator": "CONTAINS",
      "Values": ["out of office", "automatic reply"]
    }
  }]
}
```

To search only by time, omit `--filters` and provide the required `--from-timestamp`, `--to-timestamp`, and `--max-results` values.

### Checking search status and retrieving results
<a name="eb-archiving-search-results"></a>

Archive searches are asynchronous. Use the search ID with `get-archive-search` until `Status.State` is `COMPLETED`.

```bash
PROMPT> aws mailmanager get-archive-search \
  --region {{us-east-1}} \
  --search-id {{search-0123456789abcdef}} \
  --query Status
```

A completed search returns a status similar to the following.

```json
{
  "SubmissionTimestamp": "2026-11-23T20:10:00Z",
  "CompletionTimestamp": "2026-11-23T20:10:08Z",
  "State": "COMPLETED",
  "ErrorMessage": null
}
```

Valid search states are `QUEUED`, `RUNNING`, `COMPLETED`, `FAILED`, and `CANCELLED`. Calling `GetArchiveSearchResults` before completion returns a `ConflictException`.

The following command returns selected fields from each result row. Results are ordered from newest to oldest by the time the message entered the archive.

```bash
PROMPT> aws mailmanager get-archive-search-results \
  --region {{us-east-1}} \
  --search-id {{search-0123456789abcdef}} \
  --query 'Rows[].{ArchivedMessageId:ArchivedMessageId,ReceivedTimestamp:ReceivedTimestamp,From:From,EnvelopeTo:Envelope.To,Subject:Subject,HasAttachments:HasAttachments}'
```

The response has one object for each matching archived message.

```json
[
  {
    "ArchivedMessageId": "example-archived-message-id",
    "ReceivedTimestamp": "2026-11-20T15:42:18Z",
    "From": "Billing <billing@example.com>",
    "EnvelopeTo": ["accounts-payable@example.com"],
    "Subject": "November invoice",
    "HasAttachments": true
  }
]
```

For all result fields, see [GetArchiveSearchResults](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_GetArchiveSearchResults.html).

### Downloading or reading one message
<a name="eb-archiving-get-message"></a>

Use the `ArchivedMessageId` from a result row with `get-archive-message`. The response contains a temporary download link for the full message, its SMTP envelope, and source metadata.

```bash
PROMPT> aws mailmanager get-archive-message \
  --region {{us-east-1}} \
  --archived-message-id {{example-archived-message-id}}
```

```json
{
  "Envelope": {
    "From": "bounce-handler@example.com",
    "Helo": "mail.example.com",
    "To": ["accounts-payable@example.com"]
  },
  "MessageDownloadLink": "https://example.com/temporary-download-link",
  "Metadata": {
    "RuleSetId": "rs-0123456789abcdef01234567",
    "SourceArn": "arn:aws:ses:us-east-1:123456789012:mailmanager-rule-set/rs-0123456789abcdef01234567"
  }
}
```

To return the parsed text and HTML body without attachments, use `get-archive-message-content`. For response fields, see [GetArchiveMessage](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_GetArchiveMessage.html) and [GetArchiveMessageContent](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_GetArchiveMessageContent.html).

## Exporting archived email with the AWS CLI
<a name="eb-archiving-export-api"></a>

Export uses the same `Include` and `Unless` filter logic as search. The destination bucket must be in the same AWS Region as the archive. Configure the bucket and key policies described in [Permission policies for Email archiving](eb-policies.md#eb-policies-archiving) before you start the export.

The following command exports invoice messages while excluding automatic replies. It also requests a metadata JSON object for each exported message.

```bash
PROMPT> aws mailmanager start-archive-export \
  --region {{us-east-1}} \
  --archive-id {{a-1a2b3c4d5e6f}} \
  --from-timestamp 2026-11-16T00:00:00Z \
  --to-timestamp 2026-11-23T00:00:00Z \
  --max-results 1000 \
  --export-destination-configuration '{
    "S3": {
      "S3Location": "s3://amzn-s3-demo-bucket/audit/"
    }
  }' \
  --include-metadata \
  --filters '{
    "Include": [{
      "StringExpression": {
        "Evaluate": {"Attribute": "SUBJECT"},
        "Operator": "CONTAINS",
        "Values": ["invoice"]
      }
    }],
    "Unless": [{
      "StringExpression": {
        "Evaluate": {"Attribute": "SUBJECT"},
        "Operator": "CONTAINS",
        "Values": ["out of office", "automatic reply"]
      }
    }]
  }'
```

`StartArchiveExport` returns an export ID.

```json
{
  "ExportId": "export-0123456789abcdef"
}
```

Use the export ID with `get-archive-export` until `Status.State` is `COMPLETED`.

```bash
PROMPT> aws mailmanager get-archive-export \
  --region {{us-east-1}} \
  --export-id {{export-0123456789abcdef}} \
  --query Status
```

```json
{
  "SubmissionTimestamp": "2026-11-23T20:15:00Z",
  "CompletionTimestamp": "2026-11-23T20:16:12Z",
  "State": "COMPLETED",
  "ErrorMessage": null
}
```

Valid export states are `QUEUED`, `PREPROCESSING`, `PROCESSING`, `COMPLETED`, `FAILED`, and `CANCELLED`. A completed export creates a folder named with the export ID under the requested S3 prefix. The folder contains one `.eml` object for each exported message. If `IncludeMetadata` is `true`, the folder also contains a corresponding `-meta.json` object when metadata is available. The export uses the destination bucket's encryption configuration.

```
s3://amzn-s3-demo-bucket/audit/export-0123456789abcdef/
├── example-message.eml
└── example-message-meta.json
```

For all request and response members, see [StartArchiveExport](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_StartArchiveExport.html) and [GetArchiveExport](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_GetArchiveExport.html).

## Recommendations
<a name="eb-archiving-recommendations"></a>
+ Use `ENVELOPE_TO` when you must find the actual SMTP recipient, including a recipient not shown in the message headers.
+ Use narrow time ranges and specific Include conditions before increasing `MaxResults`.
+ Use one common Archive action when multiple later rules route the same email. Repeating Archive actions can create multiple archived copies.
+ Verify customer managed AWS KMS key access before applying a rule or configuration set to production traffic.
+ Run representative searches and exports after setup. Action order and `ActionFailurePolicy` do not confirm durable archive storage.

## Using email archiving in the Amazon SES console
<a name="eb-archiving-console"></a>

The **Email archiving** page in the SES console consists of four interactive tables, **Search archive**, **Search history**, **Export history**, and **Manage archives**, that you can use to search for email in your archives, export the results, and manage your archives. In the following procedures, instructions are provided for each table.

**To use the **Email archiving** page to search, export, and manage your archives**

1. Sign in to the AWS Management Console and open the Amazon SES console at [https://console.aws.amazon.com/ses/](https://console.aws.amazon.com/ses/).

1. In the left navigation panel, choose **Email archiving** under **Mail Manager**.

1. The **Email archiving** page consists of four tables **Search archive**, **Search history**, **Export history**, and **Manage archives**. For instructions specific to each of these tables, select its corresponding tab below:

------
#### [ Search archive ]

**Search archive** is an interactive table that provides a way for you to search and find your archived messages with a rich filter and date set offering detailed search criteria to find anything from a specific email to many emails matching a broader category. Messages matching your search criteria can be downloaded individually or can be exported in bulk to an S3 bucket.

**To search, download, or export archived email**

1. On the **Email archiving** page, choose the **Search archive** tab to display the **Search archive** table.

1. Click inside the **Archive** field and choose an archive from the list followed by **Search**, or refine your search using the following steps.

1. Select the **Date range** field to expand date range options for your search:
   + **Relative range** (default) – Select the radio button that corresponds with the number of days desired, or choose a **Custom range** by selecting a time unit and a date range up to 30 days.
   + **Absolute range** – Enter a **Start date** and an **End date** *(and time if desired)* up to 30 days.
**Note**
 Searching within an archive is limited to 30 days at a time. For example, if you want to search for messages from June 1 through July 31, divide the range into the following three searches.
30 days in June.
The first 30 days in July.
The 31st day of July.
For **Relative range** dates, the last day ends at midnight. For example, if you choose *Last 7 days*, the seventh day is yesterday and ends at midnight.

1. (Optional) Select the **Filters** field to choose from among the following filters: *From*, *To *, *CC*, *Subject line*, and *Has attachments*—the following properties apply:
   + You can create up to 10 filters.
   + A filter can be edited by clicking on it, or removed by selecting the **X**.

1. Choose **Search** and the archived email matching your search criteria will be populated in the **Search results** table.
   + The **Message ID** column is hidden by default, but can be displayed by selecting the gear icon to customize how you view the table.
   + Every search you execute is automatically saved with a unique search id and will be listed in the **Search history** table.

1. To view the text of a message along with its envelope and header information, select the message’s radio button followed by **View details** to open the **Message details** sidebar.

1. To create a local file of the message, select the message’s radio button followed by **Download message**.

1. Your filtered search can be saved to an Amazon S3 bucket by selecting **Export to S3**.

   1. If you know the URI of the S3 bucket you want to use, enter it in the **S3 URI** field; otherwise, choose **Browse S3** and select an S3 bucket and folder to use on the S3 page.

   1. Review the destination bucket's encryption configuration. Exported objects use the destination bucket's encryption settings. The export does not accept a separate AWS KMS key setting.

   1. Choose **Export** and all the messages found in your filtered search will be saved as individual files in the S3 folder you selected.

**Note**
While there's no limit on how many messages your archive can contain, search results are limited to 1000 rows in the **Search results** table.

------
#### [ Search history ]

A history of your searches is listed in this table so that you can restore the result set or access complex filter sets created previously. You can also create new searches based on the original search by editing the filters and dates. Any new searches are automatically saved with a unique search ID and will be listed in this table.

**To view and work with your previous searches**

1. On the **Email archiving** page, choose the **Search history** tab to display the **Search history** table which lists a history of all your archived email searches with the most recent on top. *This table loads data the first time you visit it—if you switch tabs and come back, use the refresh icon to retrieve the latest data.*

1. Click inside the **Archive** field and choose an archive from the list—all the searches belonging to that archive will be populated in the table. You can view and do more with individual searches in the steps below.

1. Select the radio button of a previous search followed by **View search results** to restore its original search results—the **Search archive** page will open displaying the filter set and date range used for the original search along with all the messages previously found based on that criteria. You can expand upon the original search in the following ways:
   + Create a new search by modifying the date range and filters followed by **Search**.
   + Any new searches you perform are automatically saved with a unique search ID and will be listed in the **Search history** table.

------
#### [ Export history ]

A history of your exports is listed in this table enabling easy access to the contents of the export folder in the S3 console.

**To view your recent exports**

1. On the **Email archiving** page, choose the **Export history** tab to display the **Export history** table which lists all of the archived email searches you exported to an S3 bucket within the last 30 days. *This table loads data the first time you visit it—if you switch tabs and come back, use the refresh icon to retrieve the latest data.*

1. If the status of an export is *Queued* or *Preprocessing*, you can cancel it by choosing **Cancel**.

1. Select an **S3 URI** to open the export's bucket folder in the S3 console where you can see the files it contains.

------
#### [ Manage archives ]

This table lists your archives where you have options to create a new archive, search for a particular archive and view its details, edit an archive, or delete an archive.

**To create and manage archives**

1. On the **Email archiving** page, choose the **Manage archives** tab to display the **Archives** table which lists all of your email archives. *This table loads data the first time you visit it—if you switch tabs and come back, use the refresh icon to retrieve the latest data.*

1. To search for a particular archive, begin typing in the **Archives** field.

1. To view details of an archive, select its name in the **Archive name** column.

1. To create an archive, select **Create archive**.

   1. Enter a unique name in the **Archive name** field.

   1. (Optional) Select a retention period in the **Retention period** field to override the default retention period of 180 days.

   1. (Optional) You can encrypt your archive either by entering your own AWS KMS key into the **KMS key ARN** field, or by selecting **Create new key**.

   Choose **Create archive**.

1. Now that you've created an archive, you can use it in a [rule set](eb-rules-setup.md#eb-rules-create-console) to archive received (inbound) email, or designate it in a [configuration set](creating-configuration-sets.md#config-sets-create-console) to archive sent (outbound) email.

1. To edit an archive, select its radio button followed by **Edit**.

   1. Edit or change the name in the **Archive name** field.

   1. Change the retention period in the **Retention period** field.

   Choose **Update archive**.

1. To delete an archive, select its radio button followed by **Delete**.

   1. Type `delete` in the **Confirm** field followed by **Delete**.

     The archive state will switch to *Pending deletion* in the **Archives** table and will be automatically deleted after 30 days.

------
