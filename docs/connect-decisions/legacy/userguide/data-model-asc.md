---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/userguide/data-model-asc.html
---

# Data entities supported in AWS Supply Chain
<a name="data-model-asc"></a>

The following is an overview of the data entities supported in AWS Supply Chain.

**Note**
The data entities listed in this chapter are required for Data Lake ingestion. For data entities required for each AWS Supply Chain module, see [Data entities and columns used in AWS Supply Chain](data-model.md).
For information on application datasets displayed in AWS Supply Chain Analytics, see [Application datasets used in AWS Supply Chain Analytics](application_datasets.md).

- ** Organization **
  - **Category type:** Non-transactional data / **Data entity and description:** [company](organization-company-entity.md) - Entity to store the name and location of your company.
  - **Category type:** Non-transactional data / **Data entity and description:** [geography](organization-geography-entity.md) - Entity stores geographical hierarchy of your company.
  - **Category type:** Non-transactional data / **Data entity and description:** [trading\_partner](organization-trading-partner-entity.md) - Contains the partners that have trading relationship with your company, such as vendors, 3PLs, channel partners, or distributors.
  - **Category type:** Non-transactional data / **Data entity and description:** [trading\_partner\_poc](organization-trading-partner-poc-entity.md) - Contains information that can be identified about the point of contacts at the partners such as vendors, 3PLs, channel partners, or distributors, that have trading relationship with your company.

- ** Product **
  - **Category type:** Non-transactional data / **Data entity and description:** [product](product-product-entity.md) - Contains the key product attributes, including name, description, brand, codes, category, business group, and price.
  - **Category type:** Non-transactional data / **Data entity and description:** [product\_hierarchy](product-hierarchy-entity.md) - Contains the product categories and sub-categories.
  - **Category type:** Non-transactional data / **Data entity and description:** [product\_uom](product-uom-entity.md) - Contains the product packaging options and conversations between packages.
  - **Category type:** Non-transactional data / **Data entity and description:** [product\_alternate](product-alternate-entity.md) - Contains information about alternative products, including type of alternative.
  - **Category type:** Non-transactional data / **Data entity and description:** [un\_details](product-un-details-entity.md) - Contains information about hazardous products.

- ** Network **
  - **Category type:** Non-transactional data / **Data entity and description:** [site](network-site-entity.md) - Stores information for sites holding inventory such as Stores, Distribution Centers ,including ID, name, address, geographical region, and site type.
  - **Category type:** Non-transactional data / **Data entity and description:** [transportation\_lane](network-transporation-lane-entity.md) - Contains information about transportation lanes, including from and to sites, transportation mode, and transit time.

- ** Vendor management **
  - **Category type:** Non-transactional data / **Data entity and description:** [vendor\_product](vendor-management-product-entity.md) - Contains the product information per vendor, including price, lead-time, and inbound sites.
  - **Category type:** Non-transactional data / **Data entity and description:** [vendor\_lead\_time](vendor-management-lead-time-entity.md) - Contains the planned and actual lead times from the vendor.
  - **Category type:** Non-transactional data / **Data entity and description:** [vendor\_holiday](vendor-management-holiday-entity.md) - Displays information on vendor outages due to holidays and shutdowns.

- ** Planning **
  - **Category type:** Non-transactional data / **Data entity and description:** [inv\_policy](planning-inv-policy-entity.md) - Contains inventory policies such as minimum and maximum safety stock policy, target inventory quantity, minimum or ma maximum order quantity and so on, for product, product-site, and other possible combinations.
  - **Category type:** Non-transactional data / **Data entity and description:** [segmentation](planning-segmentation-entity.md) - Used to store segments. Segments are used in conjunction with product, site, and effective dates for uniqueness. For example, HV1 for High Value, HLW for Halloween Products, seasonal, volatile and so on.
  - **Category type:** Non-transactional data / **Data entity and description:** [sourcing\_rules](planning-sourcing-rules-entity.md) - Defines rules at product-site level to specify the sourcing related attributes (for example, rule type, to and from site, transportation lane, minimum and maximum quantity, priority, ratio, and so on).
  - **Category type:** Non-transactional data / **Data entity and description:** [sourcing\_schedule](planning-sourcing-schedule-entity.md) - Sourcing schedule determines when to source. For example, source from vendors or transfer between sites.
  - **Category type:** Non-transactional data / **Data entity and description:** [sourcing\_schedule\_details](planning-sourcing-schedule-details-entity.md) - Provides sourcing schedule details. For example, the days in a week, a product be sourced from a vendor.
  - **Category type:** Transactional data / **Data entity and description:** [reservation](planning-reservation-entity.md) - Provides details about inventory reservation. For example, reservation ID, type, date, quantity, product ID.
  - **Category type:** Transactional data / **Data entity and description:** [product\_bom](planning-product-bom-entity.md) - Displays bill of material for product with type, level, ratios, quantities, and cost attributes.

- ** Operation **
  - **Category type:** Transactional data / **Data entity and description:** [process\_header](operation-process-header-entity.md) - Track execution activities within a plant or site. For example, manufacturing, maintenance or repairs.
  - **Category type:** Transactional data / **Data entity and description:** [process\_operation](operation-process-operation-entity.md) - Defines operation associated with an activity. For example, Stop machine, Oiling, and so on.
  - **Category type:** Transactional data / **Data entity and description:** [process\_product](operation-process-product-entity.md) - Define the product or material associated with an activity.
  - **Category type:** Transactional data / **Data entity and description:** [production\_process](operation-production-process-entity.md) - Defines attributes associated with the manufacturing or production process.

- ** Inventory Management **
  - **Category type:** Transactional data
  - **Data entity and description:** [inv\_level](inventory_mgmnt-inv-level-entity.md) - A snapshot of the product’s inventory condition in each site. For example, snapshot date, on-hand inventory, condition of the product.

- ** Inbound **
  - **Category type:** Transactional data / **Data entity and description:** [inbound\_order](replenishment-inbound-order-entity.md) - Contains information about inbound orders into your companies locations. For example, for example, purchase orders (POs), blanket POs, production orders, or stock transfer orders).
  - **Category type:** Transactional data / **Data entity and description:** [inbound\_order\_line](replenishment-inbound-order-line-entity.md) - Stores line level information for inbound\_order, including product\_id, and quantity.
  - **Category type:** Transactional data / **Data entity and description:** [inbound\_order\_line\_schedule](replenishment-inbound-order-line-schedule-entity.md) - Stores schedule-line level data within an inbound\_order\_line and is relevant only when schedules are used.
  - **Category type:** Transactional data / **Data entity and description:** [shipment](replenishment-shipment-entity.md) - Stores shipment information like origin, carrier code, ship date, product, quantity, ship from site, expected delivery date, and actual delivery date, or inbound orders (PO,TO and so on) including ship date, product, quantity, ship from site, expected delivery date, and actual delivery date.
  - **Category type:** Transactional data / **Data entity and description:** [shipment\_stop](replenishment-shipment-stop-entity.md) - Contains list of shipment stops with corresponding date and time. This field is used when there are multiple stops for shipments.
  - **Category type:** Transactional data / **Data entity and description:** [shipment\_stop\_order](replenishment-shipment-stop-order-entity.md) - Contains list of orders picked and dropped per shipment stop.
  - **Category type:** Transactional data / **Data entity and description:** [shipment\_lot](replenishment-shipment-lot-entity.md) - Contains the shipment details per shipment lot.

- ** Outbound fulfillment **
  - **Category type:** Transactional data / **Data entity and description:** [outbound\_order\_line](outbound-fulfillment-order-line-entity.md) - Contains orders originating from your company and shipped to locations outside of the your network. Outbound\_order\_line contains order date, customer location, incoterms, and so on. It also includes product, price, discount, and units.
  - **Category type:** Transactional data / **Data entity and description:** [outbound\_shipment](outbound-fulfillment-shipment-entity.md) - Stores shipment information for outbound orders, including ship date, product, quantity, ship from site, expected delivery date, and actual delivery date.

- ** Cost management **
  - **Category type:** Transactional data
  - **Data entity and description:** [customer\_cost](customer-cost-entity.md) - Displays the information about the costs incurred by you during the supply chain operations.

- ** Plan **
  - **Category type:** Transactional data
  - **Data entity and description:** [supply\_plan](supply-plan-entity.md) - Displays the supply plan generated by AWS Supply Chain Supply Planning.

- ** Forecast **
  - **Category type:** Transactional data / **Data entity and description:** [forecast](forecast-forecast-entity.md) - Stores forecast over forecast horizon for product, product-site, or other combinations.
  - **Category type:** Transactional data / **Data entity and description:** [supplementary\_time\_series](forecast-supp-timeseries-entity.md) - Displays additional demand driver time series information such as price, promotions, and out-of-stock indicator to improve forecast quality.

- ** Reference **
  - **Category type:** Non-transactional data / **Data entity and description:** [reference\_field](reference-fields-entity.md) - Contains mapping of any entity-field-value combination to a corresponding description, such as mapping specific inbound\_order status code to status description.
  - **Category type:** Non-transactional data / **Data entity and description:** [calendar](reference-calendar-entity.md) - Calendars can be used for many purposes by the application, such as planning, execution, and reporting.
  - **Category type:** Non-transactional data / **Data entity and description:** [uom\_conversion](reference-uom-conversion-entity.md) - Contains conversions for unit of measure (UOM).

- ** Insights **
  - **Category type:** Transactional data
  - **Data entity and description:** [work\_order\_plan](work-order-plan-entity.md) - Provides the supply chain process plan for a work order along with source type and duration to finish each supply chain process.

**Note**
All fields marked as type *timestamp* should be in ISO 8601 format.
The dataset that you ingest into AWS Supply Chain can only include the following special characters: ASCII 35 (number sign: \#), 36 (dollar sign: $), 37 (percent sign: %), 45 (hyphen: -), 46 (period: .), 47 (slash: /), 94 (caret), 95 (underscore: \_), 123 (left curly brace: { ), and 125 (right curly brace: }).
