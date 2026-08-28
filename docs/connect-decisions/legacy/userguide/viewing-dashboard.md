---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/userguide/viewing-dashboard.html
---

# AWS Supply Chain dashboard
<a name="viewing-dashboard"></a>

You can view your data connections and inventory visibility, add users or groups, and monitor your watchlists and key performance indicators (KPIs) directly from the dashboard. Your default dashboard view depends on the permission the AWS Supply Chain administrator assigns you.

To customize your dashboard, complete the following procedure:

1. On the AWS Supply Chain dashboard, choose **Manage dashboard**.

   The **Build your dashboard** page appears.
![AWS Supply Chain Dashboard](http://docs.aws.amazon.com/connect-decisions/legacy/userguide/images/asc_dashboard.png)

1. Depending on your user permission role, you will see cards that you can use for customizing your dashboard. For each card that you want to add to your dashboard, select its check box.

1. Choose **Save**.

## Key Performance Indicators
<a name="about-kpis"></a>

Key performance indicators (KPIs) are metrics that can help measure the performance of a supply chain. AWS Supply Chain administrator supports the following KPIs:

### On-Time in-full
<a name="otif"></a>

On-time In-Full (OTIF) measures the effectiveness of customer fulfillment operations, such as, picking, packing and shipping orders on-time and in full. This metric is measured by adding the total number of orders shipped in-full, on or before the expected ship date divided by the total number of shipments with an expected ship date for the month.

OTIF requires the following entities to be populated and mapped in AWS Supply Chain Data lake:

| Dataset | Entity |
| --- | --- |
| Outbound\_Shipment | Shipped\_Qty |
| Outbound\_Order\_Line | Quantity\_Promised |
| Outbound\_Shipment\_Records | Actual\_Ship\_Date |
| Outbound\_Shipment | Expected\_Ship\_Date |

To calculate OTIF, AWS Supply Chain uses the following formula:

**SUM (outbound\_shipment.shipped\_qty = outbound\_order\_line.Quantity promised AND outbound\_shipment\_records.actual\_ship\_date ≤ outbound\_shipment.expected\_ship\_date) ÷ by total number of orders with outbound\_shipment.expected\_ship\_date for a given month. **

### Customer order cycle time
<a name="customer_order"></a>

Customer order cycle time measures the efficiency of the supply chain fulfillment process. This metric is calculated by the average number of days between the order date and when the order is shipped.

Customer order cycle time requires the following entities to be populated and mapped in AWS Supply Chain data lake.

| Dataset | Entity |
| --- | --- |
| Outbound\_Order\_Line | Order\_Date |
| Outbound\_Shipment\_Records | Actual\_Ship\_Date |

AWS Supply Chain uses the following formula to calculate customer order cycle time:

**Average number of days between Outbound\_order\_Line.order\_date and Outbound\_Shipment.actual\_ship\_date for all outbound order lines during a given month.**

### Supplier fill rate
<a name="supplier_fill_rate"></a>

The supplier fill rate measures your supplier’s commitment to your organization. This metric is calculated by adding all the inbound orders where the quantity received matches the quantity requested by the expected delivery date.

The supplier fill rate requires the following entities to be populated and mapped in AWS Supply Chain data lake.

| Dataset | Entity |
| --- | --- |
| Inbound\_Order\_Line | Quantity\_Submitted |
| Inbound\_Order\_Line | Quantity\_Received |
| Inbound\_Order\_Line | Received\_Date |
| Inbound\_Order\_Line | Expected\_Delivery\_Date |

To calculate supplier fill rate, AWS Supply Chain uses the following formula :

**Sum (inbound\_order\_line.Quantity Submitted = inbound\_order\_line.quantity\_recieved and inbound\_order\_line.order.recieve.date ≤ inbound\_order\_line.expected\_delivery\_date) ÷ by the total number of lines with inbound\_order\_line.expected\_delivery\_date within a given month.**

### Sell-through rate
<a name="sell_through_rate"></a>

A sell-through rate measures the percentage of available inventory sold in a given month. This metric is calculated by adding all outbound shipment quantities for a given month divided by the sum of current inventory at the beginning of the month and the inventory received during the month.

The sell-through rate requires the following entities to be populated and mapped in AWS Supply Chain data lake.

| Dataset | Entity |
| --- | --- |
| Outbound\_Shipment | Shipped\_Qty |
| Outbound\_Shipment\_Records | Actual\_Ship\_Date |
| Inventory\_Level\_Records | On\_Hand\_Inventory |
| Inbound\_Order\_Line | Expected\_Delivery\_Date |
| Inbound\_Order\_Line | Quantity\_Received |
| Inbound\_Order\_Line | Received\_Date |

To calculate sell-through rate, AWS Supply Chain uses the following formula:

**SUM outbound\_shipment\_records.quantity\_shipped for a given month ÷ by SUM( InventoryLevel\_records.on\_hand\_inventory at start of month\+ inbound\_order\_line.quantity\_recieved during the month).**

### Enabling KPIs
<a name="monitor-kpi"></a>

To enable KPIs in AWS Supply Chain, complete the following procedure:

1. On the AWS Supply Chain dashboard, under **Monitor KPIs**, choose **Enable**.

   The AWS Supply Chain dashboard updates to display the KPIs for the current dataset.

1. To view the actual value or percentage, hover over the KPI.

### Managing KPIs
<a name="enabling-kpi"></a>

To view or remove KPIs from the AWS Supply Chain dashboard, complete the following procedure:

1. On the AWS Supply Chain dashboard, choose **Manage dashboard**.

1. Choose the KPIs that you want to see or remove from the AWS Supply Chain dashboard.

1. Choose **Save**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Decisions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect-decisions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
