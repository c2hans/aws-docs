---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/userguide/doc-forecast.html
---

# Days of Cover
<a name="doc-forecast"></a>

If you use Days of Cover (DoC) to manage your inventory levels, then this would be an appropriate policy setting to drive the calculation of target inventory levels and RoQ. DoC inventory policy uses the configured days of coverage. This policy doesn’t consider sourcing schedule (vendor review calendar) or vendor lead times to compute DOC. DOC is based on the *target\_doc\_limit* field in the *inventory\_policy* data entity. Note that, for weekly planning, *target\_doc\_limit* still uses unit of day. A coverage of 2 weeks translates to 14 days. DoC policy can be used with forecast (*doc\_fcst*) or demand (*doc\_dem*). The difference between *doc\_fcst* and *doc\_dem* is the forecast source. *doc\_fcst* is based on forecast, while *doc\_dem* is based on the demand history in *outbound\_order\_line*. The forecast based days of coverage uses P50 of forecast, while the demand based planning uses the last 30 days of demand history to calculate average consumption rate.

## Inputs and defaults
<a name="target-inventory-level"></a>

Target inventory level or Target inventory position (TIP) is the desired inventory position or level on a given date. Inventory position includes inventory on hand, in-transit, or on-order, while the inventory level is only the inventory on-hand. Inventory position is used for service level (sl) inventory policy, and inventory level is used for *doc\_fcst*, *doc\_dem*, and *abs\_level* inventory policies. DOC policy requires forecast, lead time, and configuration for inventory policy.

For *doc\_fcst* policy, you must provide the following information:

| Data required 1 | Entity | Field | Value | Notes |
| --- | --- | --- | --- | --- |
| Inventory policy | inventory\_policy | ss\_policy | doc\_fcst | NA>  |
| Inventory policy | inventory\_policy | target\_doc\_limit | Number of days | NA>  |
| Forecast | forecast | NA | NA | Mean or forecast quantities.>  |
| Lead time | transportation\_lane | NA | NA | Lead time from a source location to a destination. |
| Lead time | vendor\_lead\_time | NA | NA | Lead time from a vendor to a destination location. |

For inventory policy based on days of coverage, the days to cover is the *target\_doc\_limit* value.

## Calculation logic for DOC\_fcst policy
<a name="reorder-quantity"></a>

![Calculation logic for DOC_fcst policy](http://docs.aws.amazon.com/connect-decisions/legacy/userguide/images/doc_fcst.png)

## Calculation Logic for doc\_dem policy
<a name="calculation-logic"></a>

![Calculation logic for doc_dem policy](http://docs.aws.amazon.com/connect-decisions/legacy/userguide/images/doc_dem.png)

The goal of days of coverage policy is to make sure on each review date that there is enough on-hand inventory to cover the configured days of coverage. The first part of the formula computes the days of coverage from the next review date until the end of days of coverage configured. The total covering period is *DOCP,S*​ for product *P* and site *S*. The second part of the formula computes the extra demand before the target review date (the first review date after delivery). The covering period starts from the expected deliver date and ends with the target review date. If the current on-hand inventory on the delivery date is able to cover demand of this period, the system reorders 0. The max function determines whether we must order extra.

## Calculating reorder quantity
<a name="purchase-order-requests"></a>

The input for the reorder quantity calculation is the target inventory level and the current inventory level. If the inventory level record is missing, the system generates plan exceptions for you to review.

![Calculation of reorder quantity](http://docs.aws.amazon.com/connect-decisions/legacy/userguide/images/roq_calculation.png)

The reorder quantity of product *P*, site *S*, and date *D* is the difference between the target inventory level and the current inventory level. If the current inventory level is higher than the target inventory level, the reorder quantity is 0.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Decisions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect-decisions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
