---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/userguide/entities-work-order-insights.html
---

# Order Planning and Tracking
<a name="entities-work-order-insights"></a>

**Note**
To generate an order insight, in addition to ingesting the required data entities and columns, you must configure your milestone and process definitions. For more information on configuring orders, see [Configuring Order Planning and Tracking for the first time](setting-up-work-orders.md).

The table below lists the required data entities and columns to generate a order planning and tracking process.

- ** [site](network-site-entity.md) The *site* data entity columns not listed in this table are *optional* for order planning and tracking. AWS Supply Chain highly recommends ingesting data for the *optional* columns to enhance the feature output. When data is ingested for the *optional* columns, you can use them to configure rules to evaluate the process milestones. **
  - **Column:** id
  - **Is the column used by Order Planning and Tracking?:**  Required. When you ingest data from SAP or EDI, the default value for string is SCN\_RESERVED\_NO\_VALUE\_PROVIDED. When you upload data using the Amazon S3 connector, you must enter a value or use SCN\_RESERVED\_NO\_VALUE\_PROVIDED for successful ingestion.

- ** [product](product-product-entity.md) The *product* data entity columns not listed in this table are *optional* for order planning and tracking. AWS Supply Chain highly recommends ingesting data for the *optional* columns to enhance the feature output. When data is ingested for the *optional* columns, you can use them to configure rules to evaluate the process milestones. **
  - **Column:** id

- ** [vendor\_product](vendor-management-product-entity.md) The *vendor\_product* data entity columns not listed in this table are *optional* for order planning and tracking. AWS Supply Chain highly recommends ingesting data for the *optional* columns to enhance the feature output. When data is ingested for the *optional* columns, you can use them to configure rules to evaluate the process milestones. **
  - **Column:**
    - vendor\_tpartner\_id
    - product\_id
    - eff\_start\_date
    - eff\_end\_date

- ** [geography](organization-geography-entity.md) **
  - **Column:** id
  - **Is the column used by Order Planning and Tracking?:** Required – This column is used by conditional filters to display regions or country.

- ** [inbound\_order](replenishment-inbound-order-entity.md) The *inbound\_order* data entity columns not listed in this table are *optional* for order planning and tracking. AWS Supply Chain highly recommends ingesting data for the *optional* columns to enhance the feature output. When data is ingested for the *optional* columns, you can use them to configure rules to evaluate the process milestones. **
  - **Column:** id / **Is the column used by Order Planning and Tracking?:** Required
  - **Column:** tpartner\_id / **Is the column used by Order Planning and Tracking?:** Required

- ** [inbound\_order\_line](replenishment-inbound-order-line-entity.md) The *inbound\_order\_line* data entity columns not listed in this table are *optional* for order planning and tracking. AWS Supply Chain highly recommends ingesting data for the *optional* columns to enhance the feature output. When data is ingested for the *optional* columns, you can use them to configure rules to evaluate the process milestones. **
  - **Column:**
    - id
    - order\_id
    - tpartner\_id
    - product\_id
  - **Is the column used by Order Planning and Tracking?:**  Required. When you ingest data from SAP or EDI, the default value for string is SCN\_RESERVED\_NO\_VALUE\_PROVIDED. When you upload data using the Amazon S3 connector, you must enter a value or use SCN\_RESERVED\_NO\_VALUE\_PROVIDED for successful ingestion.

- ** [shipment](replenishment-shipment-entity.md) The *shipment* data entity columns not listed in this table are *optional* for order planning and tracking. AWS Supply Chain highly recommends ingesting data for the *optional* columns to enhance the feature output. When data is ingested for the *optional* columns, you can use them to configure rules to evaluate the process milestones. **
  - **Column:**
    - id
    - supplier\_tpartner\_id
    - product\_id
    - order\_id
    - order\_line\_id
    - package\_id

- ** [reservation](planning-reservation-entity.md) The *reservation* data entity columns not listed in this table are *optional* for order planning and tracking. AWS Supply Chain highly recommends ingesting data for the *optional* columns to enhance the feature output. When data is ingested for the *optional* columns, you can use them to configure rules to evaluate the process milestones. **
  - **Column:** reservation\_id / **Is the column used by Order Planning and Tracking?:** Required – This column is a required key for the reservation\_id column in the process\_product data entity.
  - **Column:** reservation\_type / **Is the column used by Order Planning and Tracking?:** Required – This column is used when defining a default order plan.
  - **Column:** reservation\_detail\_id / **Is the column used by Order Planning and Tracking?:** Required – This column is a required key for the reservation\_detail\_id column in the process\_product data entity.

- ** [process\_header](operation-process-header-entity.md) The *process\_header* data entity columns not listed in this table are *optional* for order planning and tracking. AWS Supply Chain highly recommends ingesting data for the *optional* columns to enhance the feature output. When data is ingested for the *optional* columns, you can use them to configure rules to evaluate the process milestones. **
  - **Column:** process\_id / **Is the column used by Order Planning and Tracking?:** Required
  - **Column:** site\_id / **Is the column used by Order Planning and Tracking?:** Required – This column is used by the site\_id column in the process\_header data entity. For example, this column can be referenced in the milestone rules for specific processes.
  - **Column:** status / **Is the column used by Order Planning and Tracking?:** Required
  - **Column:** required\_on\_site / **Is the column used by Order Planning and Tracking?:** Required – This date is required to calculate the forecast completion date and to determine the Order line status.

- ** [process\_product](operation-process-product-entity.md) The *process\_product* data entity columns not listed in this table are *optional* for order planning and tracking. AWS Supply Chain highly recommends ingesting data for the *optional* columns to enhance the feature output. When data is ingested for the *optional* columns, you can use them to configure rules to evaluate the process milestones. **
  - **Column:** process\_product\_id / **Is the column used by Order Planning and Tracking?:** Required – This column is part of the primary key in the process\_product data entity and is used as a reference in other entities.
  - **Column:** process\_id / **Is the column used by Order Planning and Tracking?:** Required – This column is part of the primary key in the process\_product data entity and is used to associate the header with the line.
  - **Column:** product\_id / **Is the column used by Order Planning and Tracking?:** Required
  - **Column:** reservation\_id / **Is the column used by Order Planning and Tracking?:** Required
  - **Column:** reservation\_detail\_id / **Is the column used by Order Planning and Tracking?:** Required
  - **Column:** requested\_availability\_date / **Is the column used by Order Planning and Tracking?:** Required – The field is displayed as Required on site date in the AWS Supply Chain web application. This date is required to calculate the forecast completion date and to determine the Order line status. When you ingest data, you must enter a value for requested\_availability\_date. When information is not available for the requested\_availability\_date column, order planning and tracking will use the column values from process\_header > planned\_start\_date to calculate the forecast completion date.

- ** [work\_order\_plan](work-order-plan-entity.md) **
  - **Column:** process\_id / **Is the column used by Order Planning and Tracking?:** Required
  - **Column:** product\_id / **Is the column used by Order Planning and Tracking?:** Required
  - **Column:** business\_process\_id / **Is the column used by Order Planning and Tracking?:** Required
  - **Column:** business\_process\_sequence / **Is the column used by Order Planning and Tracking?:** Required
  - **Column:** preferred\_source / **Is the column used by Order Planning and Tracking?:** Required
  - **Column:** duration / **Is the column used by Order Planning and Tracking?:** Required – This column provides the process lead time to determine the target date of the process completion.

The following table describes the data entities that are *not* required to generate order planning and tracking. If these data entities are included in your dataset, the required columns are listed in the table below.

- ** [trading\_partner](organization-trading-partner-entity.md) **
  - **Column:**
    - id
    - tpartner\_type
    - geo\_id
    - eff\_start\_date
    - eff\_end\_date
  - **Is the column used by Order Planning and Tracking?:** Required – This column is used to link the trading partner.

- ** [process\_operation](operation-process-operation-entity.md) The *process\_operation* data entity columns not listed in this table are *optional* for order planning and tracking. AWS Supply Chain highly recommends ingesting data for the *optional* columns to enhance the feature output. When data is ingested for the *optional* columns, you can use them to configure rules to evaluate the process milestones. **
  - **Column:**
    - process\_operation\_id
    - process\_id
  - **Is the column used by Order Planning and Tracking?:** Required

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Decisions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect-decisions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
