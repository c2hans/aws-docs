---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/userguide/configuring-procurement.html
---

# Procurement
<a name="configuring-procurement"></a>

You can view the procurement details for all the items ordered as part of a order. By default, you can view the supply chain processes for procurement and you can use the filters to view a subset of procurement processes. You can select the **Material Name** to view the corresponding procurement summary.

In the left navigation pane on the AWS Supply Chain dashboard, choose **Order Planning and Tracking**. The **Order Planning and Tracking** page appears. Choose the **Procurement** tab.

![Viewing the procurement details](http://docs.aws.amazon.com/connect-decisions/legacy/userguide/images/Procurement.png)

You can choose **Filters** to filter the orders based on **Country/Location**, **Campaign**, **Revision** , **Main Work Center**, **Process Name**, and **Planner Group**. Once you set your filters, choose **Apply**. You can also choose **Save filter group** to save your filters.

You can also filter the orders by **All**, **On Time**, **Delivered**, **Watch**, **At Risk**, and **Late** status. For example, if you choose **Late**, you will see all the orders that are currently late or delayed.

You can use the **Search** field to search for the required orders. You can sort them by any of the headers but by default, the orders are sorted first by **Site Delivery Forecast** and second by **Work Priority**.

You can use the expandable **Comments** feature to do the following:
+ Add a comment (under 400 characters).
+ Edit or delete a comment.
+ See other users' comments.

![Comments feature on the Procurement page](http://docs.aws.amazon.com/connect-decisions/legacy/userguide/images/comments-procurement.PNG)

The **Procurement** page, displays the following from your ERP or source system:

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

- ** RFQ/Line **
  - **Description:** You can select the RFQ or line number to view in your ERP or source system.
  - **Data entity:** reservation / **Column:** rfq\_id
  - **Data entity:** reservation / **Column:** rfq\_line\_id
  - **Data entity:** inbound\_order\_line / **Column:** inbound\_order\_line\_url

- ** PO/Line **
  - **Description:** You can select the purchase order (PO) or line number to view in your ERP or source system.
  - **Data entity:** reservation / **Column:** order\_id
  - **Data entity:** reservation / **Column:** order\_line\_id
  - **Data entity:** inbound\_order\_line / **Column:** inbound\_order\_line\_url

- ** Order Priority **
  - **Description:** Displays the priority of the order. AWS Supply Chain will only accept a numerical value for this field. For example, 1,2,3, and so on. If your ERP system doesn't contain a numerical value for this field, you will not be able to sort the order by priority.
  - **Data entity:** process\_header
  - **Column:** priority

- ** Material Name **
  - **Description:** Displays the name of material that is being procured. If a material is marked Hazmat in your ERP system, AWS Supply Chain will display the Hazmat sign next to the material.<br />You can select the material name to view the current order milestone. Slide the Show Completed Milestones button to view all the completed milestones for a material.
  - **Data entity:** process\_product
  - **Column:** product\_id

- ** Process product allocation type **
  - **Description:** Displays the allocation type for the product. .
  - **Data entity:** process\_product
  - **Column:** allocation\_type

- ** QTY/UoM **
  - **Description:** Displays the quantity of the material that is being procured.
  - **Data entity:** reservation / **Column:** quantity
  - **Data entity:** reservation / **Column:** quantity\_uom

- ** Source **
  - **Description:** Display the source from which the material is being procured.
  - **Data entity:** trading\_partner / **Column:** description
  - **Data entity:** inbound\_order / **Column:** tpartner\_id

- ** Required on Site **
  - **Description:** Displays the date the product is required at the order site.
  - **Data entity:** process\_header / **Column:** planned\_start\_date
  - **Data entity:** process\_product / **Column:** request\_availability\_date

- ** Current Process **
  - **Description:** Displays the current process of the order.
  - **Data entity:** Calculated by order planning and tracking.
  - **Column:** Calculated by order planning and tracking.

- ** Site Delivery Forecast **
  - **Description:** Displays the current process of the order.[See the AWS documentation website for more details](http://docs.aws.amazon.com/connect-decisions/legacy/userguide/configuring-procurement.html)

- ** Recommended Action Due Date **
  - **Description:** Displays the current process of the order.

- ** Recommendation **
  - **Description:** Displays all actionable items and is linked to a milestone.
