---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-10-03/framework/sec_appsec_manual_code_reviews.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SEC11-BP04 Manual code reviews
<a name="sec_appsec_manual_code_reviews"></a>

Perform a manual code review of the software that you produce. This process helps verify that the person who wrote the code is not the only one checking the code quality.

**Desired outcome:** Including a manual code review step during development increases the quality of the software being written, helps upskill less experienced members of the team, and provides an opportunity to identify places where automation can be used. Manual code reviews can be supported by automated tools and testing.

**Common anti-patterns:**
+  Not performing reviews of code before deployment.
+  Having the same person write and review the code.
+  Not using automation to assist or orchestrate code reviews.
+  Not training builders on application security before they review code.

**Benefits of establishing this best practice:**
+  Increased code quality.
+  Increased consistency of code development through reuse of common approaches.
+  Reduction in the number of issues discovered during penetration testing and later stages.
+  Improved knowledge transfer within the team.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>

 The review step should be implemented as part of the overall code management flow. The specifics depend on the approach used for branching, pull-requests, and merging. You might be using AWS CodeCommit or third-party solutions such as GitHub, GitLab, or Bitbucket. Whatever method you use, it’s important to verify that your processes require the review of code before it’s deployed in a production environment. Using tools such as [Amazon CodeGuru Reviewer](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/welcome.html) can make it easier to orchestrate the code review process.

### Implementation steps
<a name="implementation-steps-required-field"></a>
+  Implement a manual review step as part of your code management flow and perform this review before proceeding.
+  Consider [Amazon CodeGuru Reviewer](https://aws.amazon.com/codeguru/) for managing and assisting in code reviews.
+  Implement an approval flow that requires a code review being completed before code can progress to the next stage.
+  Verify there is a process to identify issues being found during manual code reviews that could be detected automatically.
+  Integrate the manual code review step in a way that aligns with your code development practices.

## Resources
<a name="resources-required-field"></a>

 **Related best practices:**
+  [SEC11-BP02 Automate testing throughout the development and release lifecycle](sec_appsec_automate_testing_throughout_lifecycle.md)

 **Related documents:**
+  [Working with pull requests in AWS CodeCommit repositories](https://docs.aws.amazon.com/codecommit/latest/userguide/pull-requests.html)
+  [Working with approval rule templates in AWS CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/approval-rule-templates.html)
+  [About pull requests in GitHub](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests)
+  [Automate code reviews with Amazon CodeGuru Reviewer](https://aws.amazon.com/blogs/devops/automate-code-reviews-with-amazon-codeguru-reviewer/)
+  [Automating detection of security vulnerabilities and bugs in CI/CD pipelines using Amazon CodeGuru Reviewer CLI](https://aws.amazon.com/blogs/devops/automating-detection-of-security-vulnerabilities-and-bugs-in-ci-cd-pipelines-using-amazon-codeguru-reviewer-cli/)

 **Related videos:**
+  [Continuous improvement of code quality with Amazon CodeGuru](https://www.youtube.com/watch?v=iX1i35H1OVw)

 **Related examples:**
+  [Security for Developers workshop](https://catalog.workshops.aws/sec4devs)
