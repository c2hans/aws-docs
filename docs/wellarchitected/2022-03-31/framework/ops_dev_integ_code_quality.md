---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/ops_dev_integ_code_quality.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# OPS05-BP07 Implement practices to improve code quality
<a name="ops_dev_integ_code_quality"></a>

 Implement practices to improve code quality and minimize defects. Some examples include test-driven development, code reviews, and standards adoption.

 On AWS, you can integrate services such as [Amazon CodeGuru](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/welcome.html) with your pipeline to automatically [identify potential code and security issues](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/how-codeguru-reviewer-works.html) using program analysis and machine learning. CodeGuru provides recommendations on how to implement the AWS best practices to address these issues.

 **Common anti-patterns:**
+  To be able to test your feature sooner, you have decided to not integrate your standard input sanitization library. After testing, you commit your code without remembering to complete incorporation of the library.
+  You have minimal experience with the dataset you are processing and are unaware that there are a series of edge cases that can exist in your dataset. Those edge cases are not compatible with the code that you have implemented.

 **Benefits of establishing this best practice:** By adopting practices to improve code quality, you can help minimize issues introduced to production.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>
+  Implement practices to improve code quality: Implement practices to improve code quality to minimize defects and the risk of their being deployed. For example, test-driven development, pair programming, code reviews, and standards adoption.
  +  [Amazon CodeGuru](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/welcome.html)

## Resources
<a name="resources"></a>

 **Related documents:**
+  [Amazon CodeGuru](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/welcome.html)
