---
source_url: https://docs.aws.amazon.com/glue/latest/dg/adobeanalytics-connector-limitations.html
---

# Limitations
<a name="adobeanalytics-connector-limitations"></a>

The following are limitations for the Adobe Analytics connector:
+ Adobe Analytics doesn’t support field based and record-based partitioning. Field based partitioning is not supported as you cannot query fields that you partition. Record based partitioning cannot be supported as there is no provision to get ‘offset’ for pagination.
+ In the `Report Top Item` entity, the `startDate` and `endDate` query parameters are not functioning as expected. The response is not being filtered based on these parameters, which is causing issues with the filter and incremental flow for this entity.
+ For the `Annotation`, `Calculated Metrics`, `Calculated Metrics Function`, `Date Ranges`, `Dimension`, `Metric`, `Project`, `Report Top Items`, and `Segment` entities, the `locale` query parameter specifies which language is to be used for localized sections of responses and does not filter the records. For example, `locale="ja_JP"` will display the data in Japanese.
+ `Report Top Item` entity – filter on `dateRange` and `lookupNoneValues` fields are currently not working.
+ `Segment` entity: with filter value `includeType=“templates”`, filters on other fields are not working.
+ `Date Range` entity – filter on `curatedRsid` field is not working.
+ `Metric entity` entity – filter on segmentable field with “false” value gives result for both true and false value.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
