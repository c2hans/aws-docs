---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/userguide/manage-data-streams-method.html
---

# Associate a data stream to an asset property
<a name="manage-data-streams-method"></a>

Manage your data streams using the AWS IoT SiteWise console or AWS CLI.

------
#### [ Console ]

Use the AWS IoT SiteWise console to manage your data streams.

**To manage data streams (console)**

1. <a name="sitewise-open-console"></a>Navigate to the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/).

1. In the navigation pane, choose **Data streams**.

1. Choose a data stream by either filtering on data stream alias, or selecting **Disassociated data streams** in the filter drop down menu.

1. Select the data stream to update. You may select multiple data streams. Click **Manage data streams** on the upper right.

1. Select the data stream to be associated from **Update data stream associations**, and click the **Choose measurement** button.

1.  In the **Choose measurement** section, find the corresponding asset measurement property. Select the measurement then click **Choose**.

1.  Perform steps 4 and 5 for other data streams selected in step 3. Assign asset properties to all the data streams.

1.  Choose **Update** to commit the changes. A successful confirmation banner is displayed to confirm the update.

------
#### [ AWS CLI ]

 To associate a data stream (identified by its alias) to an asset property (identified by its IDs), run the following command:

```
aws iotsitewise associate-time-series-to-asset-property \
    --alias <data-stream-alias> \
    --assetId <asset-ID> \
    --propertyId <property-ID>
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
