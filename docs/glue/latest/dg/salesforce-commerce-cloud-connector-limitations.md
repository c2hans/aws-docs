---
source_url: https://docs.aws.amazon.com/glue/latest/dg/salesforce-commerce-cloud-connector-limitations.html
---

# Limitations
<a name="salesforce-commerce-cloud-connector-limitations"></a>

The following are limitations for the Salesforce Commerce Cloud connector:
+ The Contains filter is not working as expected when partitioning.
+ CDN Zones' entity doesn't support sandbox instances, and it supports only Development and production instance types. For more information, see [ https://help.salesforce.com/s/articleView?id=cc.b2c\_embedded\_cdn\_overview.htm ](https://help.salesforce.com/s/articleView?id=cc.b2c_embedded_cdn_overview.htm).
+ In Salesforce Commerce Cloud, there is no API endpoint to fetch Dynamic Metadata. As a result, there is no provision to support the custom fields in the Product and Category entity.
+ Site id is a mandatory query parameter. You must pass the Site Id value through the Custom Connector Setting. For more information, see [Base URL and Request Formation ](https://developer.salesforce.com/docs/commerce/commerce-api/guide/base-url.html).
+ You can apply filters on maximum two fields (excluding Levels if present) in single API request with the combination of different operators as mentioned in the below table:
<a name="salesforce-commerce-cloud-limitations-filters"></a>[See the AWS documentation website for more details](http://docs.aws.amazon.com/glue/latest/dg/salesforce-commerce-cloud-connector-limitations.html)
+ In some of the entities, the data type for the fields while retrieving is different from when it is used as searchable fields. As a result, there is no provision of filter feature for these fields. The following table provides the details about such fields.
<a name="salesforce-commerce-cloud-limitations-filters-provision"></a>[See the AWS documentation website for more details](http://docs.aws.amazon.com/glue/latest/dg/salesforce-commerce-cloud-connector-limitations.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
