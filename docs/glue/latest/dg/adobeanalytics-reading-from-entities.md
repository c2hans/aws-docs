---
source_url: https://docs.aws.amazon.com/glue/latest/dg/adobeanalytics-reading-from-entities.html
---

# Reading from Adobe Analytics entities
<a name="adobeanalytics-reading-from-entities"></a>

 **Prerequisites**

An Adobe Analytics Object you would like to read from. Refer the supported entities table below to check the available entities.

 **Supported entities**

| Entity | Can be Filtered | Supports Limit | Supports Order By | Supports Select \* | Supports Partitioning |
| --- | --- | --- | --- | --- | --- |
| Annotation | Yes | Yes | Yes | Yes | No |
| Calculated Metrics | Yes | Yes | Yes | Yes | No |
| Calculated Metrics Function | Yes | No | No | Yes | No |
| Component Metadata Shares | Yes | Yes | No | Yes | No |
| Date Ranges | Yes | Yes | No | Yes | No |
| Dimensions | Yes | No | No | Yes | No |
| Metrics | Yes | No | No | Yes | No |
| Projects | Yes | No | No | Yes | No |
| Reports Top Item | Yes | Yes | No | Yes | No |
| Segments | Yes | Yes | Yes | Yes | No |
| Usage Logs | Yes | Yes | No | Yes | No |

 **Example**

```
adobeAnalytics_read = glueContext.create_dynamic_frame.from_options(
     connection_type="adobeanalytics",
     connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "annotation/ex*****",
        "API_VERSION": "v2.0"
 })
```

 **Adobe Analytics entity and field details**
+ [Annotations](https://adobedocs.github.io/analytics-2.0-apis/#/Annotations)
+ [Calculated Metrics](https://adobedocs.github.io/analytics-2.0-apis/#/Calculated%20Metrics)
+ [Component Meta Data](https://adobedocs.github.io/analytics-2.0-apis/#/Component%20Meta%20Data)
+ [Date Ranges](https://adobedocs.github.io/analytics-2.0-apis/#/Date%20Ranges)
+ [Dimensions](https://adobedocs.github.io/analytics-2.0-apis/#/Dimensions)
+ [Metrics](https://adobedocs.github.io/analytics-2.0-apis/#/Metrics)
+ [Projects](https://adobedocs.github.io/analytics-2.0-apis/#/Projects)
+ [Reports](https://adobedocs.github.io/analytics-2.0-apis/#/Reports)
+ [Segments](https://adobedocs.github.io/analytics-2.0-apis/#/Segments)
+ [Users](https://adobedocs.github.io/analytics-2.0-apis/#/Users)
+ [Usage Logs](https://adobedocs.github.io/analytics-2.0-apis/#/Usage%20Logs)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
