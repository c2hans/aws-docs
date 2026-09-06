---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/userguide/configuring-logistics.html
---

# Logistics
<a name="configuring-logistics"></a>

You can view the logistics details for all the items ordered as part of a order. You can select the **Material Name** to view the corresponding material summary for any supply chain process.

In the left navigation pane on the AWS Supply Chain dashboard, choose **Order Planning and Tracking**.

The **Order Planning and Tracking** page appears. Choose the **Logistics** tab.

![Viewing the logistics details](http://docs.aws.amazon.com/connect-decisions/legacy/userguide/images/Logistics.png)

You can choose **Filters** to filter the orders based on **Country/Location**, **Campaign**, **Revision** , **Main Work Center**, **Process Name**, and **Planner Group**. Once you set your filters, choose **Apply**. You can also choose **Save filter group** to save your filters.

You can also filter the orders by **All**, **On Time**, **Delivered**, **Watch**, **At Risk**, and **Late** status. For example. if you choose **Late**, you will see all the orders that are currently late or delayed.

You can use the **Search** field to search for the required orders. You can sort them by any of the headers but by default, the orders are sorted first by **Site Delivery Forecast** and second by **Work Priority**.

You can use the expandable **Comments** feature to do the following:
+ Add a comment (under 400 characters).
+ Edit or delete a comment.
+ See other users' comments.

![Comments feature on the Logistics page](http://docs.aws.amazon.com/connect-decisions/legacy/userguide/images/comments-logistics.PNG)

The **Logistics** page, displays the following from your ERP or source system:

- ** Order **
  - **Description:** Display the order number. You can select the order to view your ERP or source system.
  - **Data entity:** process\_product / **Column:** process\_id
  - **Data entity:** process\_header / **Column:** process\_url

- ** Revision **
  - **Description:** Displays the material revision.
  - **Data entity:** process\_header
  - **Column:** revision

- ** Order type **
  - **Description:** Displays the order type.
  - **Data entity:** process\_header
  - **Column:** type

- ** PR/Line **
  - **Description:** You can select the procurement or line number to view in your ERP or source system.
  - **Data entity:** reservation / **Column:** requisition\_id
  - **Data entity:** reservation / **Column:** requisition\_line\_id
  - **Data entity:** inbound\_order\_line / **Column:** inbound\_order\_line\_url

- ** PO/Line **
  - **Description:**  You can select the purchase order (PO) or line number to view in your ERP or source system.
  - **Data entity:** reservation / **Column:** order\_id
  - **Data entity:** reservation / **Column:** order\_line\_id
  - **Data entity:** inbound\_order\_line / **Column:** inbound\_order\_line\_url

- ** STO/Line **
  - **Description:** You can select the standard transfer order (STO) or line number to view in your ERP or source system.
  - **Data entity:** reservation / **Column:** stock\_transfer\_1\_order\_id
  - **Data entity:** reservation / **Column:** stock\_transfer\_1\_order\_line\_id
  - **Data entity:** reservation / **Column:** stock\_transfer\_2\_order\_id
  - **Data entity:** reservation / **Column:** stock\_transfer\_2\_order\_line\_id

- ** Order Priority **
  - **Description:** Displays the priority of the order. Supply Chain will only accept a numerical value for this field. For example, 1,2,3, and so on. If your ERP system doesn't contain a numerical value for this field, you will not be able to sort the order by priority.
  - **Data entity:** process\_header
  - **Column:** priority

- ** Material Name **
  - **Description:** Displays the name of material that is being procured. If a material is marked Hazmat in your ERP system, AWS Supply Chain will display the Hazmat sign next to the material.<br />You can select the material name to view the current order milestone. Slide the Show Completed Milestones button to view all the completed milestones for a material.
  - **Data entity:** process\_product
  - **Column:** product\_id

- ** QTY/UoM **
  - **Description:** Displays the quantity of the material that is being procured.
  - **Data entity:** reservation / **Column:** quantity
  - **Data entity:** reservation / **Column:** quantity\_uom

- ** Source **
  - **Description:** Display the source from which the material is being procured.
  - **Data entity:** trading\_partner / **Column:** description
  - **Data entity:** inbound\_order / **Column:** tpartner\_id

- ** Required on Site **
  - **Description:** Displays the date on which the material is required on-site.
  - **Data entity:** process\_header / **Column:** planned\_start\_date
  - **Data entity:** process\_product / **Column:** request\_availability\_date

- ** Site Delivery Forecast **
  - **Description:** Displays the current process of the order.+ **Late** – Displayed when the order is running late due to the underlying order material with the latest delivery date estimated to arrive late. This item is displayed in Red.<br />+ **On-time** – Displayed when the materials under the order is reaching the site within the required on-site date. This item is displayed in Green.<br />+ **At risk** – Displayed when the material with the latest arrival date has a process that is either delayed or is in a blocked milestone. This item can still make the required date and is displayed in Yellow.<br />+ **Watch** – Displayed when the material with the latest date is either blocked or late in a current supply chain process.<br />+ **Delivered** – Displayed after the last milestone of the last process is initiated indicating the completion of the process.
  - **Data entity:** Calculated by order planning and tracking.
  - **Column:** Calculated by order planning and tracking.

- ** Current Process **
  - **Description:** Displays the current milestone.

- ** Recommended Action Due Date **
  - **Description:** Displays the current process of the order.

- ** Recommendation **
  - **Description:** Displays all actionable items and is linked to a milestone.
