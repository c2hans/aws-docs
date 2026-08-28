---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-gen-ai-selling-partner-api/data-sp-api.html
---

# Data available through the Amazon Selling Partner API
<a name="data-sp-api"></a>

The [Amazon Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/welcome) (SP-API) is a REST-based API that helps Amazon sellers and vendors programmatically access their data on orders, shipments, payments, and much more. The data from this API can increase selling efficiency, reduce labor requirements, and improve the response time to customers. This guide focuses on the data that you can access through [Selling Partner API for Reports](https://developer-docs.amazon.com/sp-api/docs/reports-api-v2021-06-30-use-case-guide) (Reports API) and the [Selling Partner API for Data Kiosk](https://developer-docs.amazon.com/sp-api/docs/data-kiosk-workflow-guide) (Data Kiosk API).

## Reports API
<a name="data-reports-api"></a>

The data from the Reports API is designed to help you manage your business on the Amazon marketplace. The [analytics reports](https://developer-docs.amazon.com/sp-api/docs/report-type-values-analytics) provide valuable insights about your products, customers, and overall performance, such as:
+ **Sales performance** – Analyzing sales data can help you identify trends and customer buying patterns. You can use this information to optimize your sales strategy.
+ **Product performance** – Analyzing product data can help you identify which products are selling well and which ones are not. You can use this information to optimize your product offerings.
+ **Customer behavior** – Analyzing customer data can help you understand your customers' preferences and needs. You can use this information to personalize your marketing and sales strategies.

The following table explains each [brand analytics](https://developer-docs.amazon.com/sp-api/docs/report-type-values-analytics#brand-analytics-reports) report. The following reports are available to Amazon sellers and vendors who have the Brand Analytics Selling Partner API role and are registered in Amazon Brand Registry.

|
|
| **Report** | **Description** | **Parameters** |
| --- |--- |--- |
| [Market Basket Analysis Report](https://developer-docs.amazon.com/sp-api/docs/report-type-values-analytics#market-basket-analysis-report) | Provides data on the items that are most commonly purchased in combination with the items in the customer's basket (cart) at checkout | The report can be requested for different reporting periods (`DAY`, `WEEK`, `MONTH`, or `QUARTER`). The data is provided across those periods. |
| [Amazon Search Terms Report](https://developer-docs.amazon.com/sp-api/docs/report-type-values-analytics#amazon-search-terms-report) | Contains data on the most frequently selected Amazon Standard Identification Numbers (ASINs), by search keyword and department for a marketplace | The report can be requested for different reporting periods (`DAY`, `WEEK`, `MONTH`, or `QUARTER`). Requests cannot span multiple reporting periods. |
| [Repeat Purchase Report](https://developer-docs.amazon.com/sp-api/docs/report-type-values-analytics#repeat-purchase) | Contains data on the quantity of repeated purchases of the selling partner's items | The report can be requested for different reporting periods (`WEEK`, `MONTH`, or `QUARTER`). The data can span multiple reporting periods. |

The following table explains each [vendor retail analytics](https://developer-docs.amazon.com/sp-api/docs/report-type-values-analytics#vendor-retail-analytics-reports) and [seller retail analytics](https://developer-docs.amazon.com/sp-api/docs/report-type-values-analytics#seller-retail-analytics-reports) report.

|
|
| **Report** | **Description** | **Availability** | **Parameters** |
| --- |--- |--- |--- |
| [Rapid Retail Analytics Inventory Report](https://developer-docs.amazon.com/sp-api/docs/report-type-values-analytics#rapid-retail-analytics-inventory-report) | Contains inventory data at an ASIN level, aggregated to an hourly granularity | Vendors | The report can only be requested. The data can span multiple date range periods, including the current day. |
| [Rapid Retail Analytics Traffic Report](https://developer-docs.amazon.com/sp-api/docs/report-type-values-analytics#rapid-retail-analytics-traffic-report) | Contains data on the customer traffic to the detail pages of the vendor's items, with hourly granularity | Vendors | The report can only be requested. The data can span multiple date range periods. |
| [Rapid Retail Analytics Sales Report](https://developer-docs.amazon.com/sp-api/docs/report-type-values-analytics#rapid-retail-analytics-sales-report) | Contains sales data at an ASIN level, aggregated to an hourly granularity | Vendors | The report can only be requested. The data can span multiple date range periods. |
| [Vendor Sales Report](https://developer-docs.amazon.com/sp-api/docs/report-type-values-analytics#vendor-sales-report) | Contains key retail sales metrics (such as ordered and shipped revenue and units), reported at the catalog level and at the ASIN level | Vendors | The report can be requested for different:+ Reporting periods (`DAY`, `WEEK`, `MONTH`, `QUARTER`, or `YEAR`)<br />+ Distributor views (`MANUFACTURING` or `SOURCING`)<br />+ Selling programs (`RETAIL`, `BUSINESS`, or `FRESH`) |
| [Net Pure Product Margin Report](https://developer-docs.amazon.com/sp-api/docs/report-type-values-analytics#net-pure-product-margin-report) | Contains data on Amazon's net pure product margins for selling a vendor's items, reported at the catalog level and at the ASIN level | Vendors | The report can be requested for different reporting periods (`DAY`, `WEEK`, `MONTH`, `QUARTER`, or `YEAR`). |
| [Vendor Traffic Report](https://developer-docs.amazon.com/sp-api/docs/report-type-values-analytics#vendor-traffic-report) | Contains key retail traffic metrics, such as glance views, reported at the catalog level and at the ASIN level | Vendors | The report can be requested for different reporting periods (`DAY`, `WEEK`, `MONTH`, `QUARTER`, or `YEAR`). |
| [Vendor Forecasting Report](https://developer-docs.amazon.com/sp-api/docs/report-type-values-analytics#vendor-forecasting-report) | Contains forward-looking mean, prior 70, prior 80, and prior 90 weekly customer demand forecasts, reported at the ASIN level for the most recent weekly forecast generation date | Vendors | The report can be requested for different selling programs (`RETAIL` or `FRESH`). |
| [Vendor Inventory Report](https://developer-docs.amazon.com/sp-api/docs/report-type-values-analytics#vendor-inventory-report) | Contains inventory and operational health metrics (such as sellable on-hand units and vendor confirmation rate), reported at the catalog level and at the ASIN level | Vendors | The report can be requested for different:+ Reporting periods (`DAY`, `WEEK`, `MONTH`, `QUARTER`, or `YEAR`)<br />+ Distributor views (`MANUFACTURING` or `SOURCING`)<br />+ Selling programs (`RETAIL` or `FRESH`) |
| [Sales and Traffic Business Report](https://developer-docs.amazon.com/sp-api/docs/report-type-values-analytics#sales-and-traffic-business-report) | Contains key sales performance metrics (such as ordered product sales, revenue, units ordered, and claim amount) and page traffic metrics (such as page views and buy box percentage) for the seller's entire catalog, aggregated by date and ASIN | Sellers | The report can be requested or scheduled. The data can be provided for different date range aggregation levels (`DAY`, `WEEK`, or `MONTH`) and ASIN aggregation levels (`PARENT`, `CHILD`, or `SKU`). |

## Data Kiosk API
<a name="data-kiosk-api"></a>

The Data Kiosk API provides a [GraphQL](https://graphql.org/)-based dynamic reporting suite. It helps you generate custom GraphQL queries and access bulk data from Amazon's datasets. You can use this API to access a wide range of data, including:
+ Seller sales and traffic data
+ Vendor analytics data
+ Seller economics data

The following are the key capabilities of the Data Kiosk API:
+ **GraphQL-powered dynamic reporting** – The API supports GraphQL query operations, helping you to create custom queries to retrieve the specific data that you need.
+ **Bulk data access** – You can access large datasets through the API, facilitating comprehensive analysis and reporting.
+ **Flexible data exploration** – The GraphQL-based approach allows for dynamic, ad-hoc data exploration. This flexibility helps you iterate on queries and extract insights.
+ **Comprehensive data coverage** – The API provides access to a wide range of seller and vendor data, enabling holistic performance analysis and business intelligence.

The schemas and directives in the Data Kiosk API provide a structured way to access your data through a GraphQL API, with the ability to aggregate and filter the data based on your specific needs. By using the Data Kiosk API, you can gain deeper, more actionable insights into sales, traffic, and analytics data. This empowers you to make informed, data-driven decisions to optimize your business strategies.

|
|
| Note: The retention of a query varies based on the fields requested. Each field within a schema is annotated with a `@resultRetention` directive that defines how long a query containing that field will be retained. When a query contains multiple fields with different retentions, the shortest (minimum) retention is applied. The retention of a query's resulting documents always matches the retention of the query. |
| --- |

### Seller sales and traffic data
<a name="seller-sales-and-traffic-data.eb74a320-9b2d-5bf6-b163-f37a67fc5f04"></a>

In the Data Kiosk API, `Analytics_SalesAndTraffic_2024_04_24` is the root type for sales and traffic queries. Two queries are available for this root type:
+ `salesAndTrafficByAsin` retrieves sales and traffic data that is aggregated by ASIN (`PARENT`, `CHILD`, or `SKU`).
+ `salesAndTrafficByDate` retrieves sales and traffic data that is aggregated by date (`DAY`, `WEEK`, or `MONTH`).

Note the following about these queries:
+ Enumerated types (enums), such as `AsinGranularity` and `DateGranularity`, specify the level of aggregation.
+ Scalar types, such as [Date](https://the-guild.dev/graphql/scalars/docs/scalars/date), are used to represent the data.

### Vendor analytics data
<a name="vendor-analytics-data.6e47f4a0-6906-5a7c-843f-dc470ecc1dd2"></a>

In the Data Kiosk API, `Analytics_vendorAnalytics_2024_09_30` is the root type for vendor analytics queries. Two views are available for this root type:
+ `manufacturingView` retrieves metrics about products that you manufacture, aggregated by the specified date.
+ `sourcingView` retrieves metrics about products that you source directly to Amazon, aggregated by the specified date.

You access the relevant view and its associated metrics based on the role assigned to you as a vendor (`SOURCING` or `MANUFACTURING`). These queries include the start and end dates, the marketplace identifier, the aggregated metrics, and the total metrics. Note the following about these queries:
+ The metrics are grouped by various attributes (such as ASIN or brand) by using the `ManufacturingViewMetricsGroupedBy` and `SourcingViewMetricsGroupedBy` types.
+ Metric types, such as `costs`, `customerSatisfaction`, `orders`, and `productAvailability`, represent the different metric groups.
+ The `DateGranularity` enum specifies the level of date aggregation.

### Seller economics data
<a name="seller-economics-data.c5e3d65d-a66b-5a05-ab22-81c9670241ba"></a>

The seller economics report provides a comprehensive view of your performance and financials on the Amazon marketplace. It covers sales data, advertising spend, fees, costs, and net proceeds. You can aggregate the data by date and product identifier.

In the Data Kiosk API, `Analytics_Economics_2024_03_15` is the root type for seller economics queries. The seller economics data for a given product is represented by the `Economics` type. This type includes the following key aspects:
+ `ads` – The advertising spend data for the product within the specified date range.
+ `cost` – The off Amazon cost provided by the seller for this product (per unit).
+ `fees` – The fees applied to the product within the specified date range.
+ `fnsku` – The Fulfillment Network Stock Keeping Unit (FNSKU) of the product.
+ `msku` – The Merchant Stock Keeping Unit (MSKU) of the product.
+ `netProceeds` – The net proceeds for this product within the specified date range.
+ `sales` – The sales data for the product within the specified date range.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
