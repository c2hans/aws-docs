---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/userguide/work-order-dashboard.html
---

# Orders
<a name="work-order-dashboard"></a>

You can view all the orders that are at-risk, delivered, early, late, on time, or watch. You can expand the order to view the materials under each order.

In the left navigation pane on the AWS Supply Chain dashboard, choose **Order Planning and Tracking**. The **Order Planning and Tracking** page appears.

![Orders](https://docs.aws.amazon.com/connect-decisions/legacy/userguide/images/Work_order.png)

Choose **Filters** to filter the orders based on **Country/Location**, **Campaign**, **Revision** , **Main Work Center**, **Process Name**, and **Planner Group**. Once you set your filters, choose **Apply**. You can also choose **Save filter group** to save your filters.

You can also filter the orders by **All**, **On Time/Early**, **Watch**, **At Risk**, **Late**, **Delivered**, and **Site Delivery Forecast** status. For example, if you choose **Late**, you will see all the orders that are currently late or delayed.

You can use the **Search** field to search by order or material number and use the *Sort* option to sort the orders. You can sort them by any of the headers but by default, the orders are sorted first by **Site Delivery Forecast** and second by **Order Priority**.

The **Orders** page, displays the following from your ERP or source system:

- ** Order **
  - **Description:** Display the order number. You can select the order to view your ERP or source system. You can expand each order to view the materials in the order.
  - **Data entity:** process\_header
  - **Column:** process\_id

- ** Campaign/Revision **
  - **Description:** Displays the campaign and/or the revision of the order.
  - **Data entity:** process\_header / **Column:** program\_group
  - **Data entity:** process\_header / **Column:** revision

- ** Main Work Center **
  - **Description:** Displays the main work center defined in the source system.
  - **Data entity:** process\_header
  - **Column:** execution\_group

- ** Planner Group **
  - **Description:** Displays the planning group for each order.
  - **Data entity:** process\_header
  - **Column:** planning\_group

- ** Order Description **
  - **Description:** Displays a brief reasoning of the order.
  - **Data entity:** process\_header
  - **Column:** description

- ** Order End Date **
  - **Description:** Displays the date by which the order should me completed.
  - **Data entity:** process\_header
  - **Column:** planned\_completion\_date

- ** Order Priority **
  - **Description:** Displays the priority of the order. Supply Chain will only accept a numerical value for this field. For example, 1,2,3, and so on. If your ERP system doesn't contain a numerical value for this field, you will not be able to sort the order by priority.
  - **Data entity:** process\_header
  - **Column:** priority

- ** Planned Start Date **
  - **Description:** The date when all the materials are required on-site before starting the work.
  - **Data entity:** process\_header
  - **Column:** planned\_start\_date

- ** Flex 1 to 5 **
  - **Description:** Custom fields that can be renamed and populated with any data.
  - **Data entity:** process\_header
  - **Column:** flex\_1, flex\_2, flex\_3, flex\_4, flex\_5

- **Recommendation**
  - **Description:** Displays all actionable items and is linked to a milestone. For example, if the order is blocked with a PO blocked milestone, the recommendation text will display to look for alternate products.
  - **Data entity:** Calculated by Order Planning and Tracking
  - **Column:** Calculated by Order Planning and Tracking

- **Site Delivery Forecast**
  - **Description:** Displays one of the following:+ **At risk** – Displayed when the material with the latest arrival date has a process that is either delayed or is in a blocked milestone. This item can still make the required date and is displayed in Yellow.<br />+ **Delivered** – Displayed after the last milestone of the last process is initiated indicating the completion of the process.<br />+ **Early** – Displayed in green when all the order lines are early and includes the count of days of the earliest line.<br />+ **Late** – Displayed when the order is running late due to the underlying order material with the latest delivery date estimated to arrive late. This item is displayed in Red.<br />+ **On-time** – Displayed when the materials under the order is reaching the site within the required on-site date. This item is displayed in Green.<br />+ **Watch** – Displayed when the material with the latest date is either blocked or late in a current supply chain process.

## Viewing order materials
<a name="materials"></a>

You can view all the materials related to a order.

1. In the left navigation pane on the AWS Supply Chain dashboard, choose **Order Planning and Tracking**.

   The **Order Planning and Tracking** page appears.

1. Use the expandable **Comments** feature to do the following:
   + Add a comment (under 400 characters).
   + Edit or delete a comment.
   + See other users' comments.
![Comments feature on the Orders page](https://docs.aws.amazon.com/connect-decisions/legacy/userguide/images/comments-orders.png)

1. Expand the order you would like to view.

   The **Materials in Order** page appears.

<table>
<thead>
  <tr><th>Order Lines</th><th>Description</th><th>Data entity</th><th>Column</th></tr>
</thead>
<tbody>
  <tr><td>Material</td><td>Displays the material number.</td><td>process_product</td><td>product_id</td></tr>
  <tr><td>Material Description</td><td>Provides a description of the material.</td><td>product</td><td>description</td></tr>
  <tr><td rowspan="2">Quantity/UoM</td><td rowspan="2">Lists the quantity of the material. If UoM is available, UoM value is displayed. For example, 2 eaches.</td><td rowspan="2">reservation</td><td>quantity</td></tr>
  <tr><td>quantity_uom</td></tr>
  <tr><td rowspan="3">Material Source</td><td rowspan="3">Displays if the material is in inventory or direct purchase.</td><td>site</td><td>description</td></tr>
  <tr><td>inbound_order</td><td>tpartner_id</td></tr>
  <tr><td>trading_partner</td><td>description</td></tr>
  <tr><td rowspan="2">Required on Site</td><td rowspan="2">Displays the date on which the material is required on-site.</td><td>process_header</td><td>planned_start_date</td></tr>
  <tr><td>process_product</td><td>requested_availability_date</td></tr>
  <tr><td>Brand name</td><td>Provides a name of the brand.</td><td>product</td><td>brand_name</td></tr>
  <tr><td>Product status</td><td>Provides the status of the product.</td><td>process_product</td><td>status</td></tr>
  <tr><td>Product type</td><td>Provides the type of the product.</td><td>process_product</td><td>type</td></tr>
  <tr><td>Reservation type</td><td>Provides the type of the reservation.</td><td>reservation</td><td>reservation_type</td></tr>
  <tr><td>Process product allocation type</td><td>Displays the allocation type for the product. .</td><td>process_product</td><td>overallocation</td></tr>
  <tr><td>Process product allocation status</td><td>Displays the allocation status for the product. .</td><td>process_product</td><td>allocation_status</td></tr>
  <tr><td>Product flexible field 1 to 5</td><td>Custom fields that can be renamed and populated with any data.</td><td>process_product</td><td>flex_1, flex_2, flex_3, flex_4, flex_5</td></tr>
  <tr><td>Reservation flexible field 1 to 5</td><td>Displays the reservation type of the product.</td><td>reservation</td><td>flex_1, flex_2, flex_3, flex_4, flex_5</td></tr>
  <tr><td>Revision</td><td>Displays the material revision.</td><td>process_header</td><td>revision</td></tr>
  <tr><td>Order type</td><td>Displays the order type.</td><td>process_header</td><td>type</td></tr>
  <tr><td>Current Process</td><td>Displays the current supply chain process for the order material.</td><td rowspan="3">Calculated by order planning and tracking.</td><td rowspan="3">Calculated by order planning and tracking.</td></tr>
  <tr><td>Recommendation</td><td>Displays all actionable items and is linked to a milestone.</td></tr>
  <tr><td>Site Delivery Forecast</td><td>Displays the site delivery forecast and status.</td></tr>
</tbody>
</table>

1. Choose the **Material** you would like to view in-detail. The **Material Summary** page appears and displays the summary of the material. You can use the same **Comments** feature mentioned in step 2 to add, update, and view comments.
![Order material summary - working forwards process](https://docs.aws.amazon.com/connect-decisions/legacy/userguide/images/Insights_order.png)
![Order material summary - forecasted completion](https://docs.aws.amazon.com/connect-decisions/legacy/userguide/images/working_backwards.png)
![Order material summary - working backwards process](https://docs.aws.amazon.com/connect-decisions/legacy/userguide/images/working_backwards_new.png)
![Comments feature on the Procurement page](https://docs.aws.amazon.com/connect-decisions/legacy/userguide/images/comments1.PNG)
![Comments feature on the Procurement page](https://docs.aws.amazon.com/connect-decisions/legacy/userguide/images/comments2.PNG)

   You can view the current milestone for the material and the recommendation AWS Supply Chain provides for each milestone.

<table>
<thead>
  <tr><th>Material</th><th>Description</th><th>Data entity</th><th>Column</th></tr>
</thead>
<tbody>
  <tr><td>Material name</td><td>Displays the name of the material.</td><td>product</td><td>description</td></tr>
  <tr><td>Material</td><td>Provides a description of the material.</td><td>process_product</td><td>product_id</td></tr>
  <tr><td rowspan="2">Quantity/UoM</td><td rowspan="2">Lists the quantity of the material. If UoM is available, UoM value is displayed. For example, 2 eaches.</td><td>reservation</td><td>quantity</td></tr>
  <tr><td>reservation</td><td>quantity_uom</td></tr>
  <tr><td rowspan="2">Required on Site</td><td rowspan="2">Displays the date on which the material is required on-site.</td><td>process_header</td><td>planned_start_date</td></tr>
  <tr><td>process_product</td><td>requested_availability_date</td></tr>
  <tr><td rowspan="2">Vendor</td><td rowspan="2">Display the vendor from which the material is being procured.</td><td>inbound_order</td><td>tpartner_id</td></tr>
  <tr><td>trading_partner</td><td>description</td></tr>
  <tr><td>PO Delivery Date</td><td>Displays the purchase order delivery date.</td><td>inbound_order_line</td><td>expected_delivery_date</td></tr>
  <tr><td>Site Delivery Forecast</td><td>Displays the site delivery forecast and status.</td><td rowspan="4">Calculated by order planning and tracking.</td><td rowspan="4"></td></tr>
  <tr><td>Updated PO Delivery Date</td><td>Displays the updated PO delivery date.</td></tr>
  <tr><td>Update Quantity</td><td>Displays the updated product quantity.</td></tr>
  <tr><td>Supplier Delivery Date Confirmation</td><td>Displays the delivery date confirmation from the supplier.</td></tr>
  <tr><td>Process product allocation type</td><td>Displays the allocation type for the product. .</td><td>process_product</td><td>allocation_type</td></tr>
  <tr><td>Process product allocation status</td><td>Displays the allocation status for the product. .</td><td>process_product</td><td>allocation_status</td></tr>
  <tr><td>Inventory Location</td><td>Displays the inventory location.</td><td>site</td><td>description</td></tr>
  <tr><td>Inco Terms</td><td>Displays the incoterm code.</td><td>inbound_order_line</td><td>incoterm</td></tr>
  <tr><td>Reservation Type</td><td>Displays the type of reservation.</td><td>reservation</td><td>reservation_type</td></tr>
  <tr><td>Brand Name</td><td>Displays the brand name of the product.</td><td>product</td><td>brand_name</td></tr>
  <tr><td>Product Status</td><td>Displays the product status.</td><td>process_product</td><td>status</td></tr>
  <tr><td>Product Type</td><td>Displays the product type.</td><td>process_product</td><td>type</td></tr>
  <tr><td>Campaign</td><td>Displays the campaign of the order. </td><td>process_header</td><td>program_group</td></tr>
  <tr><td rowspan="2">Order</td><td rowspan="2">Display the order number. You can select the order to view your ERP or source system. </td><td>process_product</td><td>process_id</td></tr>
  <tr><td>process_header</td><td>process_url</td></tr>
  <tr><td rowspan="3">PR/Line Number</td><td rowspan="3">You can select the procurement or line number to view in your ERP or source system. </td><td>reservation</td><td>requisition_id</td></tr>
  <tr><td>reservation</td><td>requisition_line_id</td></tr>
  <tr><td>inbound_order_line</td><td>inbound_order_line_url</td></tr>
  <tr><td rowspan="3">PO/Line Number</td><td rowspan="3">You can select the purchase order (PO) or line number to view in your ERP or source system. </td><td>reservation</td><td>order_id</td></tr>
  <tr><td>reservation</td><td>order_line_id</td></tr>
  <tr><td>inbound_order_line</td><td>inbound_order_line_url</td></tr>
  <tr><td rowspan="5">STO/Line Number</td><td rowspan="5">You can select the STO or line number to view in your ERP or source system. </td><td>reservation</td><td>stock_transfer_1_order_id</td></tr>
  <tr><td>reservation</td><td>stock_transfer_1_order_line_id</td></tr>
  <tr><td>reservation</td><td>stock_transfer_2_order_id</td></tr>
  <tr><td>reservation</td><td>stock_transfer_2_order_line_id</td></tr>
  <tr><td>inbound_order_line</td><td>inbound_order_line_url</td></tr>
  <tr><td rowspan="3">RFQ/Line Number</td><td rowspan="3">You can select the RFQ or line number to view in your ERP or source system. </td><td>reservation</td><td>rfq_id</td></tr>
  <tr><td>reservation</td><td>rfq_line_id</td></tr>
  <tr><td>inbound_order_line</td><td>inbound_order_line_url</td></tr>
  <tr><td>Product Type</td><td>Displays the type of the product. </td><td>product</td><td>product_type</td></tr>
  <tr><td>Currency UOM</td><td>Displays the currency unit of measure for the price and other economic variables of this product. . </td><td>process_product</td><td>currency_uom</td></tr>
  <tr><td>Danger</td><td>Displays the products that are hazardous. </td><td>product</td><td>un_id</td></tr>
  <tr><td>Hazmat Class</td><td>Displays the products that contain hazardous materials. </td><td>un_details</td><td>un_class</td></tr>
  <tr><td>UN Class</td><td>Displays the products that are under the hazardous category. </td><td>un_details</td><td>hazmat_class</td></tr>
  <tr><td>UN Description</td><td>Displays the description of the products that are under the hazardous category. </td><td>un_details</td><td>un_description</td></tr>
  <tr><td>Image</td><td>Displays an image of the products that are under the hazardous category. </td><td>un_details</td><td>image_url</td></tr>
</tbody>
</table>

1. Choose **Copy shareable link to clipboard** to share the material summary dashboard.

1. Choose the **Edit** icon to edit the material summary view. Slide the data entity button to view the data field on the material summary page.
![Edit material summary page](https://docs.aws.amazon.com/connect-decisions/legacy/userguide/images/edit_material_summary.png)

   You can drag and drop the data entities to rearrange the date entity view on the material summary page.

1. Choose **Save Changes**.

1. Slide the **Show Completed Milestones** button to view all the completed milestones for a material.
![Viewing completed milestones](https://docs.aws.amazon.com/connect-decisions/legacy/userguide/images/completed_milestones.png)
