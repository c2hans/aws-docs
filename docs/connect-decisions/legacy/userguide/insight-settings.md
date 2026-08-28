---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/userguide/insight-settings.html
---

# Insight settings
<a name="insight-settings"></a>

After creating an instance, follow the procedure below:

1. In the left navigation pane on the AWS Supply Chain dashboard, choose the **Settings** icon. Choose **Organization** and then choose **Insights**.

   The **Insight Settings** page appears.
![Updating Insights settings](http://docs.aws.amazon.com/connect-decisions/legacy/userguide/images/insights_setttings.png)

1. Under **Projection Period**, enter the inventory projection time horizon and the time buckets. You can see inventory projections upto a total of six months.
**Note**
You can group and analyze the inventory projections in daily, weekly, or monthly intervals. Choosing a daily interval will provide a daily projection and weekly and monthly intervals will provide a long-term projection in a single bucket. Insights supports up to 60 days, 8 weeks, and 3 months per projection bucket.

   The following example displays the projected inventory level for a portable air conditioner at the New York warehouse for 7 days, next 4 weeks, and 1 month beyond the weeks.
![Projection period example settings example](http://docs.aws.amazon.com/connect-decisions/legacy/userguide/images/Insishts_settings_example.png)

1. Under **Rebalancing Recommendations Options**, you can setup the radius surrounding the stocked out site to search for available stock for rebalance. You can setup the distance in miles or kilometers.

   You can configure the rebalance model to optimize inventory levels for both supplying and receiving sites. Insights supports up to a maximum of six weeks beyond the current date, and you can customize the time horizon by factoring your lead times to see the impact of the rebalance before and after transfers.

1. Under **Rebalancing Recommendations Score Weights**, use the **Up/down** arrow to enter the core weight values to determine how ranking is calculated for rebalance recommendations.

   Depending on the inventory risk resolved, distance, time horizon, available transportation modes from the ingested data (transportation\_lane.trans\_mode), and shipping costs (transportation\_lane.unit\_costs), Insights recommends one or more ways to resolve an inventory risk insight. Insights also provides a *Score* per recommendation which is derived based on the weights configured. The higher the score, the recommendation is ranked higher and is displayed at the top.
   + *Distance* – Distance between your current location and the location where you want to transfer inventory from.
   + *Emissions (CO2)* – CO2 emissions computed for the rebalance option.
   + *Risk Resolved* – Net improvement in inventory risk percentage when excess inventory is reduced at one location to help restock the current stocked out location.
   + *Shipping Cost* – Shipping cost to rebalance and transfer inventory from one location to another.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Decisions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect-decisions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
