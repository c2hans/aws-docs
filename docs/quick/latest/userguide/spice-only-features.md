---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/spice-only-features.html
---

# SPICE-only features
<a name="spice-only-features"></a>

Amazon Quick Sight's SPICE (Super-fast, Parallel, In-memory Calculation Engine) enables certain computationally intensive data preparation features. These transformations are materialized in SPICE for optimal performance, rather than being executed at query time.

**SPICE-only features**

| Steps | Other capabilities |
| --- | --- |
|  + Append<br />+ Aggregate<br />+ Pivot<br />+ Unpivot  |  + Divergence  |

**Features available in both SPICE and DirectQuery**

| Steps | Other capabilities |
| --- | --- |
|  + Input<br />+ Add Calculated Columns<br />+ Change Data Type<br />+ Rename Columns<br />+ Select Columns<br />+ Filter<br />+ Join  |  + Composite Datasets  |

**Best practices**
+ Use SPICE for workflows requiring SPICE-only features.
+ Choose SPICE to optimize performance for complex transformations and large datasets.
+ Consider DirectQuery for real-time data needs when SPICE-only features are not required.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quick` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
