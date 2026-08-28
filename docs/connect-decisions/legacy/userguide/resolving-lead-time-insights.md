---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/userguide/resolving-lead-time-insights.html
---

# Lead time insights
<a name="resolving-lead-time-insights"></a>

AWS Supply Chain provides insights on the lead time deviation for a vendor, product, and destination site level. The vendor lead time deviation insights also includes transportation mode, source locations, and identify lead time deviations at a more granular level. You can incorporate the recommended lead times in your planning cycle for enhanced planning accuracy and to avoid stock out risks.

For example, for supplier S, product P, destination site D, source site S, and transportation mode like Truck, Ship, and so on, the **Miss Frequency** displays the frequency of time the lead time was missed, compared to the planned lead time (that is, contractual lead times) shared in the vendor\_lead\_time entity. Therefore, Insights recommends to update the planned lead time for the same vendor, product, and site to avoid future lead time issues.

![Vendor lead time deviation](http://docs.aws.amazon.com/connect-decisions/legacy/userguide/images/insights_leadtime_deviation.png)

Choose **Export All Recommendations** to export the vendor lead time recommendations for the ingested product, site, or vendor combinations in a .csv file into your Amazon S3 bucket. Once the export is completed, you will receive an email and notification on the AWS Supply Chain web application with a link to the Amazon S3 bucket where the recommendations are exported.

When values for optional columns *source\_site\_id* and *trans\_mode* in the *vendor\_lead\_time* data entity are not available, Insights will use the master records for lead times. However, when transactional data for product, source site, destination site, vendor, and transportation mode is at a more granular level, that is, *inbound\_order\_line* and *inbound\_shipment*, it influences the recommendations and the planned lead time. When there are multiple planned lead time records in the master data file, Insights will use the highest planned lead time for calculation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Decisions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect-decisions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
