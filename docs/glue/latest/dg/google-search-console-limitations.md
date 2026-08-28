---
source_url: https://docs.aws.amazon.com/glue/latest/dg/google-search-console-limitations.html
---

# Google Search Console limitations
<a name="google-search-console-limitations"></a>

The following are limitations or notes for Google Search Console:
+ Google Search Console enforces usage limits on the API. For more information, see [Usage Limits](https://developers.google.com/webmaster-tools/limits).
+ When no filter is passed for the `Search Analytics` entity, the API sums up all the clicks, impressions, CTR, and other data for your entire site within the specified default date range and presents it as a single record.
+ To breakdown the data into smaller segments, you need to introduce dimensions to your query. Dimensions tells the API how you want to segment your data.
  + For example, if you add `filterPredicate: dimensions="country"` you'll get one record for each country where your site received traffic during the specified period.
  + Example to pass multiple dimensions: `filterPredicate: dimensions="country" AND dimensions="device" AND dimensions="page"`. In this case you'll get one row in the response for each unique combination of these three dimensions.
+ Default values are set for the `start_end_date` and `dataState` fields.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/glue/latest/dg/google-search-console-limitations.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
