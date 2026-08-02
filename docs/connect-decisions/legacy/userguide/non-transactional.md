---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/userguide/non-transactional.html
---

# Planning configuration data
<a name="non-transactional"></a>

This section lists all the required fields used by Supply Planning and describes how each field is used. For information on data fields required for Supply Planning, see [Supply Planning](entities-supply-planning.md).

**Topics**
+ [Product](#product)
+ [Site](#site)
+ [Trading partner](#trading-partners)
+ [Vendor product](#vendor-product)
+ [Vendor lead time](#vendor-leadtime)
+ [Sourcing rule](#sourcing-rule)
+ [Inventory policy](#inventory-policy)
+ [Sourcing schedule](#sourcing-schedule)
+ [Bill of Material (BOM)](#product-bom)
+ [Production process](#production-process)
+ [Supply planning parameters](#production-process2)
+ [Transactional data](transactional.md)

## Product
<a name="product"></a>

The product entity defines the list of items or products that must be included in the planning. The purchase order requests use *unit\_cost field* from the *Product* entity to determine the order value or amount. The *Product* entity also contains the product group corresponding to a specific product, which is a foreign key into a *product\_hierarchy* entity. Product groups can be used in configuring inventory policies, sourcing schedules, lead times, and so on, at the aggregate level.

## Site
<a name="site"></a>

The *Site* entity defines the list of sites or locations that must be included in the planning. The *Site* entity also contains Regions corresponding to a specific site, which is a foreign key into a Geography entity. Regions can be used in configuring inventory policies, sourcing schedules, lead times, and so on, at the aggregate level.

## Trading partner
<a name="trading-partners"></a>

The *Trading\_partner* entity defines the list of suppliers. *tpartner\_type* should be set to *Vendor* when uploading supplier information.

## Vendor product
<a name="vendor-product"></a>

Products supplied by each supplier are defined in the *vendor\_product* entity. This entity also contains vendor-specific cost information.

## Vendor lead time
<a name="vendor-leadtime"></a>

Vendor lead time is the time period between placing an order to a vendor and receiving the order. This data is defined in the *VendorMgmt* category under the *vendor\_lead\_time* data entity. Vendor lead time follows the following override logic:
+ Product level vendor lead time overrides product group level vendor lead time.
+ Site level vendor lead time overrides region level vendor lead time.
+ Region level vendor lead time overrides company level vendor lead time.

To look for a record, Supply Planning uses the following fields:
+ company\_id
+ region\_id
+ site\_id
+ product\_group\_id
+ product\_id

The following is an example of the override logic:

![Override logic example](http://docs.aws.amazon.com/connect-decisions/legacy/userguide/images/override_logic.png)

The following is an example of how Supply Planning calculates vendor lead time:

![Vendor lead time calculation](http://docs.aws.amazon.com/connect-decisions/legacy/userguide/images/vendor_lead_time.png)

Prioritization order is *product* > *product\_group* > *site* > *dest\_geo (region)* > *product segment* > *company*.

## Sourcing rule
<a name="sourcing-rule"></a>

Supply Planning generates a plan based on the supply chain network topology defined under the *sourcing\_rules* entity.

The supported sourcing rule types are transfer, buy, and manufacture.

Sourcing rules follow the *product\_id* > *product\_group\_id* > *company\_id* override logic.

Supply Planning retrieves the transportation lead time by referencing *transportation\_lane\_id* and accessing *transit\_time* in *transportation\_lane*. There are two steps to retrieve the transfer lead time.

1. Find *transportation\_lane\_id* in *sourcing\_rules*. Only the sourcing rules that have both *to\_site\_id* and *from\_site\_id* are eligible for retrieving *transfer\_lead\_time*.

1. Use *transportation\_lane\_id* to look up *transportation\_lane*.

When there are multiple records with the same *to\_site\_id* and *product\_id* (*product\_group\_id*) in the *sourcing\_rule* entity, only the records with the highest priority (the smallest number) will be used.

Sourcing rules example:

Based on the preceding definition, Supply Planning selects the following sourcing rule SR1: Laptop at site `TX0` is sourced from site `IL0` via `transportation_lane_9`.

|  sourcing\_rule\_id  |  product\_id  |  product\_group\_id  |  sourcing\_rule\_type  |  from\_site\_id  |  to\_site\_id  |  sourcing\_priority  |  transportation\_lane\_id  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  SR1  |  laptop  |  electronics  |  transfer  |  IL0  |  TX0  |  1  |  transportation\_lane\_9  |
|  SR2  |  laptop  |  electronics  |  transfer  |  NJ1  |  TX0  |  2  |  transportation\_lane\_21  |
|  SR3  |  laptop  |  electronics  |  transfer  |  IL0  |  TX0  |  1  |  transportation\_lane\_11  |

When multiple records with the same priority exist for the same combination of *to\_site\_id*, *product\_id* (or *product\_group\_id*), the reorder quantity will be distributed among the available sourcing options based on the *sourcing\_ratio* field. Note that multiple sourcing is currently only supported for the `buy` sourcing rule type.

Multi-sourcing example:

|  sourcing\_rule\_id  |  product\_id  |  product\_group\_id  |  sourcing\_rule\_type  |  tpartner\_id  |  to\_site\_id  |  sourcing\_priority  |  sourcing\_ratio  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  SR1  |  laptop  |  electronics  |  buy  |  supplier1  |  TX0  |  1  |  4  |
|  SR2  |  laptop  |  electronics  |  buy  |  supplier2  |  TX0  |  1  |  6  |

Both sourcing rules, SR1 and SR2, are selected, and the order quantity will be allocated between Supplier 1 and Supplier 2 in a 4:6 ratio.

## Inventory policy
<a name="inventory-policy"></a>

Supply Planning searches for a record in the dataset by using the following fields:
+ *site\_id*
+ *geodesic*
+ *company\_id*
+ *product\_id*
+ *product\_group\_id*
+ *segment\_id*

Supply Planning uses *ss\_policy* to determine the inventory policy. The override logic uses the following priority: *product\_id* > *product\_group\_id* > *site\_id* > ** and *dest\_geo\_id* > *segment\_id* > *company\_id*.

The supported *ss\_policy* values are *abs\_level*, *doc\_dem*, *doc\_fcst*, and *sl*.

The following example displays the override priority logic.

![Override logic](http://docs.aws.amazon.com/connect-decisions/legacy/userguide/images/override1.png)

The following is an example of the *ss\_policy* value based on the override logic.

![Override ride logic example for ss_policy value](http://docs.aws.amazon.com/connect-decisions/legacy/userguide/images/override2.png)

## Sourcing schedule
<a name="sourcing-schedule"></a>

**Note**
Sourcing schedule is an optional entity. If this entity is not provided, Supply Planning uses a continuous review process to generate *required\_date* based on when products are needed.

Supply Planning uses sourcing schedule to generate purchase plans by using the following steps:
+ Find *sourcing\_schedule\_id* in *sourcing\_schedule*.
+ Find the schedule by *using sourcing\_schedule\_id* in *sourcing\_schedule\_details*.

Supply Planning searches for the following fields in *sourcing\_schedule\_id* under *sourcing\_schedule*.
+ *to\_site\_id*
+ *tpartner\_id* or *from\_site\_id*

Based on the sourcing path in sourcing rules, Supply Planning determines whether to use* from\_site\_id* or *tpartner\_id*. Supply Planning reads the value in the *sourcing\_schedule\_id* field to determine the next step.

Supply Planning reads the schedule details under *sourcing\_schedule\_details* with the following fields:
+ *sourcing\_schedule\_id*
+ *company\_id*
+ *product\_group\_id*
+ *product\_id*

*sourcing\_schedule\_details* follows the override logic, *product\_id* > *product\_group\_id* > *company\_id*.

The following is an example of the override logic in *sourcing\_schedule\_details*.

![Sourcing schedule override logic](http://docs.aws.amazon.com/connect-decisions/legacy/userguide/images/sourcing_schedule2.png)

The following are the selected schedules after applying the override logic.

![Sourcing schedule override logic](http://docs.aws.amazon.com/connect-decisions/legacy/userguide/images/sourcing_schedule3.png)

The actual schedule can be from one row to multiple rows, based on the complexity of the schedule. For the field *week\_of\_month*, only one number is allowed in each row. For multiple weeks of the month, multiple records are required (see the following example). For the field *day\_of\_week*, both integer and name of day are allowed (Sun: 0, Mon: 1, Tue: 2, Wed: 3, Thu: 4, Fri: 5, Sat: 6). In the sourcing schedule details, weekly planning requires *week\_of\_month*. While in daily planning, *week\_of\_month* can be empty, which means every week. See the following examples.

![Sourcing schedule override logic](http://docs.aws.amazon.com/connect-decisions/legacy/userguide/images/sourcing_schedule4.png)

Note that for weekly planning, *week\_of\_month* is required if *day\_of\_week* is provided.

The following example shows the dates that can be used for daily planning.

| Date | Day of the week | Week of the month |
| --- | --- | --- |
| 8/1/2023 | NA | NA |
| 8/12/2023 | NA | NA |
| NA | 2 | NA |
| NA | 5 | NA |

The following example can be used for both daily and weekly planning.

| Date | Day of the week | Week of the month |
| --- | --- | --- |
| 8/1/2023 | NA | NA |
| 8/12/2023 | NA | NA |
| NA | 2 | 1 |
| NA | 2 | 2 |
| NA | 2 | 3 |
| NA | 2 | 4 |
| NA | 2 | 5 |
| NA | 5 | 1 |
| NA | 5 | 2 |
| NA | 5 | 3 |
| NA | 5 | 4 |
| NA | 5 | 5 |

## Bill of Material (BOM)
<a name="product-bom"></a>

Product BOM is used in Manufacturing Plans when *sourcing\_rule* is set to Manufacture. For information on how to ingest Product BOM, see the AWS Supply Chain API Reference document.

## Production process
<a name="production-process"></a>

*production\_process\_id* is referenced in the *sourcing\_rule* and *product\_bom* entities. These fields are used to consume lead time information to make or assemble a BOM.

## Supply planning parameters
<a name="production-process2"></a>

In *supply\_planning\_parameters* entity, *planner\_name* of the supply planner can be assigned at *product\_id* level. Planner name will be displayed on the planned orders generated by the supply planning engine.
