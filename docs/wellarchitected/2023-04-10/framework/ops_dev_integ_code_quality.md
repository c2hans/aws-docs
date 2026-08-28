---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/ops_dev_integ_code_quality.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# OPS05-BP07 Implement practices to improve code quality
<a name="ops_dev_integ_code_quality"></a>

Implement practices to improve code quality and minimize defects. Some examples include test-driven development, code reviews, standards adoption, and pair programming. Incorporate these practices into your continuous integration and delivery process.

 **Desired outcome:**
+  Your organization uses best practices like code reviews or pair programming to improve code quality.
+  Developers and operators adopt code quality best practices as part of the software development lifecycle.

 **Common anti-patterns:**
+ You commit code to the main branch of your application without a code review. The change automatically deploys to production and causes an outage.
+  A new application is developed without any unit, end-to-end, or integration tests. There is no way to test the application before deployment.
+  Your teams make manual changes in production to address defects. Changes do not go through testing or code reviews and are not captured or logged through continuous integration and delivery processes.

 **Benefits of establishing this best practice:**
+  By adopting practices to improve code quality, you can help minimize issues introduced to production.
+  Code quality increases using best practices like pair programming and code reviews.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>

 Implement practices to improve code quality to minimize defects before they are deployed. Use practices like test-driven development, code reviews, and pair programming to increase the quality of your development.

 **Customer example**

 AnyCompany Retail adopts several practices to improve code quality. They have adopted test-driven development as the standard for writing applications. For some new features, they will have developers pair program together during a sprint. Every pull request goes through a code review by a senior developer before being integrated and deployed.

 **Implementation steps**

1.  Adopt code quality practices like test-driven development, code reviews, and pair programming into your continuous integration and delivery process. Use these techniques to improve software quality.

   1.  [Amazon CodeGuru Reviewer](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/welcome.html) can provide programming recommendations for Java and Python code using machine learning.

   1.  You can create shared development environments with [AWS Cloud9](https://docs.aws.amazon.com/cloud9/latest/user-guide/welcome.html) where you can collaborate on developing code.

 **Level of effort for the implementation plan:** Medium. There are many ways of implementing this best practice, but getting organizational adoption may be challenging.

## Resources
<a name="resources"></a>

 **Related best practices:**
+  [OPS05-BP06 Share design standards](ops_dev_integ_share_design_stds.md) - You can share design standards as part of your code quality practice.

 **Related documents:**
+ [ Agile Software Guide ](https://martinfowler.com/agile.html)
+ [My CI/CD pipeline is my release captain](https://aws.amazon.com/builders-library/cicd-pipeline/)
+ [ Automate code reviews with Amazon CodeGuru Reviewer ](https://aws.amazon.com/blogs/devops/automate-code-reviews-with-amazon-codeguru-reviewer/)
+ [ Adopt a test-driven development approach ](https://docs.aws.amazon.com/prescriptive-guidance/latest/best-practices-cdk-typescript-iac/development-best-practices.html)
+ [ How DevFactory builds better applications with Amazon CodeGuru ](https://aws.amazon.com/blogs/machine-learning/how-devfactory-builds-better-applications-with-amazon-codeguru/)
+ [ On Pair Programming ](https://martinfowler.com/articles/on-pair-programming.html)
+ [ RENGA Inc. automates code reviews with Amazon CodeGuru ](https://aws.amazon.com/blogs/machine-learning/renga-inc-automates-code-reviews-with-amazon-codeguru/)
+ [ The Art of Agile Development: Test-Driven Development ](http://www.jamesshore.com/v2/books/aoad1/test_driven_development)
+ [ Why code reviews matter (and actually save time\!) ](https://www.atlassian.com/agile/software-development/code-reviews)

 **Related videos:**
+ [AWS re:Invent 2020: Continuous improvement of code quality with Amazon CodeGuru ](https://www.youtube.com/watch?v=iX1i35H1OVw)
+ [AWS Summit ANZ 2021 - Driving a test-first strategy with CDK and test driven development ](https://www.youtube.com/watch?v=1R7G_wcyd3s)

 **Related services:**
+ [Amazon CodeGuru Reviewer](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/welcome.html)
+ [ Amazon CodeGuru Profiler ](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/what-is-codeguru-profiler.html)
+  [AWS Cloud9](https://docs.aws.amazon.com/cloud9/latest/user-guide/welcome.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
