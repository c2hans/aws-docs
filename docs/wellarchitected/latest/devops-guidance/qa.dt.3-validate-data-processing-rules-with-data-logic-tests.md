---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/qa.dt.3-validate-data-processing-rules-with-data-logic-tests.html
---

# [QA.DT.3] Validate data processing rules with data logic tests
<a name="qa.dt.3-validate-data-processing-rules-with-data-logic-tests"></a>

 **Category:** OPTIONAL

 Data logic tests verify the accuracy and reliability of data processing and transformation within your application, ensuring that it functions as intended.

 Establish test cases for data processing workflows and transformation functions, confirming that expected outcomes are achieved. Use version control systems to track changes in data logic and collaborate effectively with team members. Implement automated data logic tests in development and staging environments, which can be triggered by code commits or scheduled intervals, to proactively identify and fix issues before they reach production environments.

**Related information:**
+  [Test data quality at scale with Deequ](https://aws.amazon.com/blogs/big-data/test-data-quality-at-scale-with-deequ/)
+  [Deequ automatic suggestion of constraints](https://github.com/awslabs/deequ/blob/master/src/main/scala/com/amazon/deequ/examples/constraint_suggestion_example.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
