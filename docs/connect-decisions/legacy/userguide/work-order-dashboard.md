---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/userguide/work-order-dashboard.html
---

# Orders
<a name="work-order-dashboard"></a>

You can view all the orders that are at-risk, delivered, early, late, on time, or watch. You can expand the order to view the materials under each order.

In the left navigation pane on the AWS Supply Chain dashboard, choose **Order Planning and Tracking**. The **Order Planning and Tracking** page appears.

![Orders](http://docs.aws.amazon.com/connect-decisions/legacy/userguide/images/Work_order.png)

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
![Comments feature on the Orders page](http://docs.aws.amazon.com/connect-decisions/legacy/userguide/images/comments-orders.png)

1. Expand the order you would like to view.

   The **Materials in Order** page appears.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/connect-decisions/legacy/userguide/work-order-dashboard.html)

1. Choose the **Material** you would like to view in-detail. The **Material Summary** page appears and displays the summary of the material. You can use the same **Comments** feature mentioned in step 2 to add, update, and view comments.
![Order material summary - working forwards process](http://docs.aws.amazon.com/connect-decisions/legacy/userguide/images/Insights_order.png)
![Order material summary - forecasted completion](http://docs.aws.amazon.com/connect-decisions/legacy/userguide/images/working_backwards.png)
![Order material summary - working backwards process](http://docs.aws.amazon.com/connect-decisions/legacy/userguide/images/working_backwards_new.png)
![Comments feature on the Procurement page](http://docs.aws.amazon.com/connect-decisions/legacy/userguide/images/comments1.PNG)
![Comments feature on the Procurement page](http://docs.aws.amazon.com/connect-decisions/legacy/userguide/images/comments2.PNG)

   You can view the current milestone for the material and the recommendation AWS Supply Chain provides for each milestone.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/connect-decisions/legacy/userguide/work-order-dashboard.html)

1. Choose **Copy shareable link to clipboard** to share the material summary dashboard.

1. Choose the **Edit** icon to edit the material summary view. Slide the data entity button to view the data field on the material summary page.
![Edit material summary page](http://docs.aws.amazon.com/connect-decisions/legacy/userguide/images/edit_material_summary.png)

   You can drag and drop the data entities to rearrange the date entity view on the material summary page.

1. Choose **Save Changes**.

1. Slide the **Show Completed Milestones** button to view all the completed milestones for a material.
![Viewing completed milestones](http://docs.aws.amazon.com/connect-decisions/legacy/userguide/images/completed_milestones.png)
