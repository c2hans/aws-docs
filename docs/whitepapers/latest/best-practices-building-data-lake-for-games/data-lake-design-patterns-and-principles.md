---
source_url: https://docs.aws.amazon.com/whitepapers/latest/best-practices-building-data-lake-for-games/data-lake-design-patterns-and-principles.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Data lake design patterns and principles
<a name="data-lake-design-patterns-and-principles"></a>

## Framework
<a name="framework"></a>

 Following is a high-level framework for building a data lake on AWS.

### 10,000 foot view
<a name="ft-view"></a>

![This is a 10,000 foot (high level) view of how analytics systems work with source and destination systems.](http://docs.aws.amazon.com/whitepapers/latest/best-practices-building-data-lake-for-games/images/ten-thousand-foot.png)

### 5000 foot view
<a name="ft-view-1"></a>

![This is a 5,000 foot (mid-level) view of how analytics systems work with source and destination systems.](http://docs.aws.amazon.com/whitepapers/latest/best-practices-building-data-lake-for-games/images/five-thousand-foot.png)

 Diving deeper into the framework, there are data streamers, data collectors, data aggregators, and data transformers that collect the data from the data producers (sources). Depending on the use-case, data is then consumed for analysis or downstream consumers and cataloged into a data lake for governed access.

### 1000 foot view
<a name="ft-view-2"></a>

![This is a 1,000 foot (detailed) view of how analytics systems work with source and destination systems.](http://docs.aws.amazon.com/whitepapers/latest/best-practices-building-data-lake-for-games/images/one-thousand-foot.png)

 Diving deeper in the framework, Some AWS services are added as an example to show data flow. This layout is a common pattern AWS observed with its customers.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
