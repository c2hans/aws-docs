---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/userguide/product-product-entity.html
---

# product
<a name="product-product-entity"></a>

**Primary key (PK)**

The table below lists the column names that are uniquely identified in the data entity.

| Name | Column |
| --- | --- |
| product | id |

The table below lists the column names supported by the data entity:

| Column | Data type | Required | Description |
| --- | --- | --- | --- |
| id | string | Yes | Displays the product ID. Referred to by other entities as product\_id. |
| description | string | Yes | Displays the description of the product. |
| company\_id1 | string | No | Displays the company ID. |
| product\_group\_id1 | string | No | Displays the product group ID that this product belongs to.  |
| product\_type | string | No | Type of product, for example, finished good, component, service, or packaging.  |
| hts\_code | string | No | Harmonized Tariff Schedule code. |
| is\_hazmat | string | No | Displays whether product is Hazmat compliant. |
| is\_flammable | string | No | Indicator of whether the product is flammable or not.  |
| is\_special\_handling | string | No | Displays if the product requires special handling. |
| is\_perishable | string | No | Displays if the product is perishable. |
| is\_digital | string | No | Displays if the product is digital. |
| is\_deleted | string | No | Indicates whether product is deleted ("true") or active ("false"). |
| is\_lot\_controlled | string | No | Indicates if the product is a lot-controlled product. |
| is\_expiry\_controlled | string | No | Indicates if the product is an expiry-date controlled product. |
| creation\_date | timestamp | No | Product launch or release date. |
| brand\_name | string | No | Product brand name. |
| parent\_product\_id1 | string | No | If the product is part of a bundle, lists the ID of the parent product. |
| display\_desc | string | No | External facing description of the product. |
| discontinue\_day | timestamp | No | Date when the product was discontinued. |
| base\_uom | string | No | Unit of measure for product. Default is Eaches. |
| unit\_cost | double | No | Average unit cost of the product. Measured in currency\_uom per base\_uom. |
| unit\_price | double | No | Unit price, standard price, or MSRP of the product. |
| inventory\_holding\_cost | double | No | Average yearly holding cost of the product. |
| currency\_uom | string | No | Currency unit of measure for the price and other economic variables of this product. |
| product\_available\_day | timestamp | No | Date when the product is available for fulfillment. |
| shipping\_weight | double | No | Default weight to be used by the carrier. |
| shipping\_dimension | double | No | Dimensional weight to be used by the carrier. |
| unit\_volume | double | No | Volume of product per base\_uom. |
| pkg\_length | double | No | Packaged length of the individual product. |
| pkg\_width | double | No | Packaged width of the individual product. |
| pkg\_height | double | No | Packaged height of the individual product. |
| weight\_uom | string | No | Unit of measure for product's weight. |
| dim\_uom | string | No | Unit of measure for product's dimensions. |
| volume\_uom | string | No | Product volume. |
| diameter | double | No | Diameter of an individual product. |
| color | string | No | Product color |
| casepack\_size | int | No | Number of products in each casepack. |
| gtin | string | No | Global Trade Item Number (GTIN). 14-digit number that includes various EAN/UCC numbering structures and is used to uniquely identify a product. |
| long\_term\_horizon | double | No | Long Term Horizon time window used to determine salvage value. |
| long\_term\_horizon\_uom | string | No | UOM for Long Term Horizon time window used to determine salvage value. |
| salvage\_value\_percentage | double | No | Product cost expected to recover at the end of Long Term Horizon. |
| sap\_0material\_attr\_\_prdha | string | No | Product hierarchy. Predicate key for SAP mapping. Upsert key for T179. |
| shelf\_life | double | No | Duration for which a product can be stored or kept fresh and safe for consumption or use before it spoils or expires. This information is crucial for managing inventory levels, determining reorder points, and ensuring that products are sold or consumed before their expiration dates.  |
| shelf\_life\_uom | string | No | Unit of measure of the shelf life. |
| un\_id | string | No | UN IDs are four-digit numbers that identify dangerous goods, hazardous substances and articles (such as explosives, flammable liquids, toxic substances, and so on.) in the framework of international transport. If this field is populated then the *is\_hazmat flag* must be true.  |
| demand\_planning\_enabled | string | No | Identifies parts used for demand planning. |
| inventory\_planning\_enabled | string | No | Identifies parts used for inventory planning. |
| mrp\_enabled | string | No | Identifies parts enabled for planning in MRP. |
| purchased\_item | string | No | Identifies parts that are purchased. |

1Foreign key

**Foreign key (FK)**

The table below lists the columns with the associated foreign key.

| Column | Category | FK/Data entity | FK/Column |
| --- | --- | --- | --- |
| company\_id | Organization | company | id |
| product\_group\_id | Product | product\_hierarchy | id |
| parent\_product\_id | Product | product | id |
| un\_id | Product | un\_details | un\_id |
