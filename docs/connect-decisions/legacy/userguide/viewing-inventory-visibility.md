---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/userguide/viewing-inventory-visibility.html
---

# Viewing inventory visibility
<a name="viewing-inventory-visibility"></a>

You can use inventory visibility to view the inventory projections for all the ingested products and site combinations. You can change the projections view by product or location.

To view the inventory visibility, perform the following procedure.

1. In the left navigation pane on the AWS Supply Chain dashboard, choose **Inventory Visibility**.
![Inventory Visibility](http://docs.aws.amazon.com/connect-decisions/legacy/userguide/images/inventory_visibility.png)

1. To know when the inventory visibility page was last updated, see **Date updated** on the top right corner of the page. The page is refreshed when you ingest data into data lake. By default, Insights are generated every 24 hours or when data is ingested into data lake.

1. Choose **Filters** to filter inventory projections based on *Products*, *Locations*, or *Inventory Risks*. Under **All Products**, you can select a group of products based on their product hierarchy, that are stored under the *product-hierarchy* data entity upto one level. Under **All Locations**, you can select a group of sites based on their regions, that are stored under the *geography* data entity upto one level.

   Under **Inventory Risks - Current Day Locations**, select *Excess*, *Balanced*, or *Stock Out* to view projections with specific inventory risk for the current date.

1. Select the **Pivot by** dropdown to filter the inventory by **Location** or **Product**.

   **Pivot by Location** – When you pivot by location, the inventory projections are grouped by location. At a high-level, for a given location, you can view the site type (for example, RDC, DC, and so on), number of products at the location, number of products that are balanced(that is, well within their safety stock range), number of products that are stocked out, and the number of products that are excess in stock.
![Inventory Visibility by location](http://docs.aws.amazon.com/connect-decisions/legacy/userguide/images/pivot_by_location.png)

   **Pivot by Product** – When you pivot by product, the projections are grouped by product. At a high-level, for a given product, you can view the category (that is, one level up), the total number of available products, the total number of products on order, and the total number of products currently in transit across locations.
![Inventory Visibility by product](http://docs.aws.amazon.com/connect-decisions/legacy/userguide/images/pivot_by_product.png)
