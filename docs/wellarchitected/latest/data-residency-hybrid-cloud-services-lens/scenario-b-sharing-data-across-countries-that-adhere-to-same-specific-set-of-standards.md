---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/data-residency-hybrid-cloud-services-lens/scenario-b-sharing-data-across-countries-that-adhere-to-same-specific-set-of-standards.html
---

# Scenario B: Sharing data across countries that adhere to same specific set of standards
<a name="scenario-b-sharing-data-across-countries-that-adhere-to-same-specific-set-of-standards"></a>

 Transfer of in-scope data may be allowed to countries that adhere to the same specific set of standards (or higher) than the originating country with permissions or notification to the regulators.

![Scenario diagram covering sharing data across countries that adhere to the same specific standards](http://docs.aws.amazon.com/wellarchitected/latest/data-residency-hybrid-cloud-services-lens/images/scenario-B.png)

 This diagram shows the process of selecting a Region to store data based on its origin country:
+  Organization A retrieves the origin country of the data from Individuals X.
+  Organization A checks available Regions for different countries that potentially have similar or higher data protection standards compared to the origin country.
+  When Region Y meets the requirements, the data is stored in that Region.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
