---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-10-03/framework/sec_appsec_automate_testing_throughout_lifecycle.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SEC11-BP02 Automate testing throughout the development and release lifecycle
<a name="sec_appsec_automate_testing_throughout_lifecycle"></a>

 Automate the testing for security properties throughout the development and release lifecycle. Automation makes it easier to consistently and repeatably identify potential issues in software prior to release, which reduces the risk of security issues in the software being provided.

**Desired outcome: ** The goal of automated testing is to provide a programmatic way of detecting potential issues early and often throughout the development lifecycle. When you automate regression testing, you can rerun functional and non-functional tests to verify that previously tested software still performs as expected after a change. When you define security unit tests to check for common misconfigurations, such as broken or missing authentication, you can identify and fix these issues early in the development process.

 Test automation uses purpose-built test cases for application validation, based on the application’s requirements and desired functionality. The result of the automated testing is based on comparing the generated test output to its respective expected output, which expedites the overall testing lifecycle. Testing methodologies such as regression testing and unit test suites are best suited for automation. Automating the testing of security properties allows builders to receive automated feedback without having to wait for a security review. Automated tests in the form of static or dynamic code analysis can increase code quality and help detect potential software issues early in the development lifecycle.

**Common anti-patterns: **
+  Not communicating the test cases and test results of the automated testing.
+  Performing the automated testing only immediately prior to a release.
+  Automating test cases with frequently changing requirements.
+  Failing to provide guidance on how to address the results of security tests.

**Benefits of establishing this best practice: **
+  Reduced dependency on people evaluating the security properties of systems.
+  Having consistent findings across multiple workstreams improves consistency.
+  Reduced likelihood of introducing security issues into production software.
+  Shorter window of time between detection and remediation due to catching software issues earlier.
+  Increased visibility of systemic or repeated behavior across multiple workstreams, which can be used to drive organization-wide improvements.

** Level of risk exposed if this best practice is not established: **Medium

## Implementation guidance
<a name="implementation-guidance"></a>

As you build your software, adopt various mechanisms for software testing to ensure that you are testing your application for both functional requirements, based on your application’s business logic, and non-functional requirements, which are focused on application reliability, performance, and security.

 Static application security testing (SAST) analyzes your source code for anomalous security patterns, and provides indications for defect prone code. SAST relies on static inputs, such as documentation (requirements specification, design documentation, and design specifications) and application source code to test for a range of known security issues. Static code analyzers can help expedite the analysis of large volumes of code. The [NIST Quality Group](https://www.nist.gov/itl/ssd/software-quality-group) provides a comparison of [Source Code Security Analyzers](https://www.nist.gov/itl/ssd/software-quality-group/source-code-security-analyzers), which includes open source tools for [Byte Code Scanners](https://samate.nist.gov/index.php/Byte_Code_Scanners.html) and [Binary Code Scanners](https://samate.nist.gov/index.php/Binary_Code_Scanners.html).

 Complement your static testing with dynamic analysis security testing (DAST) methodologies, which performs tests against the running application to identify potentially unexpected behavior. Dynamic testing can be used to detect potential issues that are not detectable via static analysis. Testing at the code repository, build, and pipeline stages allows you to check for different types of potential issues from entering into your code. [Amazon CodeWhisperer](https://aws.amazon.com/codewhisperer/) provides code recommendations, including security scanning, in the builder’s IDE. [Amazon CodeGuru Reviewer](https://aws.amazon.com/codeguru/) can identify critical issues, security issues, and hard-to-find bugs during application development, and provides recommendations to improve code quality.

 The [Security for Developers workshop](https://catalog.workshops.aws/sec4devs) uses AWS developer tools, such as [AWS CodeBuild](https://aws.amazon.com/codebuild/), [AWS CodeCommit](https://aws.amazon.com/codecommit/), and [AWS CodePipeline](https://aws.amazon.com/codepipeline/), for release pipeline automation that includes SAST and DAST testing methodologies.

 As you progress through your SDLC, establish an iterative process that includes periodic application reviews with your security team. Feedback gathered from these security reviews should be addressed and validated as part of your release readiness review. These reviews establish a robust application security posture, and provide builders with actionable feedback to address potential issues.

### Implementation steps
<a name="implementation-steps"></a>
+  Implement consistent IDE, code review, and CI/CD tools that include security testing.
+  Consider where in the SDLC it is appropriate to block pipelines instead of just notifying builders that issues need to be remediated.
+  The [Security for Developers workshop](https://catalog.workshops.aws/sec4devs) provides an example of integrating static and dynamic testing into a release pipeline.
+  Performing testing or code analysis using automated tools, such as [Amazon CodeWhisperer](https://aws.amazon.com/codewhisperer/) integrated with developer IDEs, and [Amazon CodeGuru Reviewer](https://aws.amazon.com/codeguru/) for scanning code on commit, helps builders get feedback at the right time.
+  When building using AWS Lambda, you can use [Amazon Inspector](https://aws.amazon.com/about-aws/whats-new/2023/02/code-scans-lambda-functions-amazon-inspector-preview/) to scan the application code in your functions.
+  When automated testing is included in CI/CD pipelines, you should use a ticketing system to track the notification and remediation of software issues.
+  For security tests that might generate findings, linking to guidance for remediation helps builders improve code quality.
+  Regularly analyze the findings from automated tools to prioritize the next automation, builder training, or awareness campaign.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [Continuous Delivery and Continuous Deployment](https://aws.amazon.com/devops/continuous-delivery/)
+  [AWS DevOps Competency Partners](https://aws.amazon.com/devops/partner-solutions/?blog-posts-cards.sort-by=item.additionalFields.createdDate&blog-posts-cards.sort-order=desc&partner-solutions-cards.sort-by=item.additionalFields.partnerNameLower&partner-solutions-cards.sort-order=asc&awsf.partner-solutions-filter-partner-type=partner-type%23technology&awsf.Filter%20Name%3A%20partner-solutions-filter-partner-location=*all&awsf.partner-solutions-filter-partner-location=*all&partner-case-studies-cards.sort-by=item.additionalFields.sortDate&partner-case-studies-cards.sort-order=desc&awsm.page-partner-solutions-cards=1)
+  [AWS Security Competency Partners](https://aws.amazon.com/security/partner-solutions/?blog-posts-cards.sort-by=item.additionalFields.createdDate&blog-posts-cards.sort-order=desc&partner-solutions-cards.sort-by=item.additionalFields.partnerNameLower&partner-solutions-cards.sort-order=asc&awsf.partner-solutions-filter-partner-type=*all&awsf.Filter%20Name%3A%20partner-solutions-filter-partner-categories=use-case%23app-security&awsf.partner-solutions-filter-partner-location=*all&partner-case-studies-cards.sort-by=item.additionalFields.sortDate&partner-case-studies-cards.sort-order=desc&events-master-partner-webinars.sort-by=item.additionalFields.startDateTime&events-master-partner-webinars.sort-order=asc) for Application Security
+  [Choosing a Well-Architected CI/CD approach](https://aws.amazon.com/blogs/devops/choosing-well-architected-ci-cd-open-source-software-aws-services/)
+  [Monitoring CodeCommit events in Amazon EventBridge and Amazon CloudWatch Events](https://docs.aws.amazon.com/codecommit/latest/userguide/monitoring-events.html)
+  [Secrets detection in Amazon CodeGuru Review](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/recommendations.html#secrets-detection)
+  [Accelerate deployments on AWS with effective governance](https://aws.amazon.com/blogs/architecture/accelerate-deployments-on-aws-with-effective-governance/)
+  [How AWS approaches automating safe, hands-off deployments](https://aws.amazon.com/builders-library/automating-safe-hands-off-deployments/)

 **Related videos:**
+  [Hands-off: Automating continuous delivery pipelines at Amazon](https://www.youtube.com/watch?v=ngnMj1zbMPY)
+  [Automating cross-account CI/CD pipelines](https://www.youtube.com/watch?v=AF-pSRSGNks)

 **Related examples:**
+  [Industry awareness for developers](https://owasp.org/www-project-top-ten/)
+  [AWS CodePipeline Governance](https://github.com/awslabs/aws-codepipeline-governance) (GitHub)
+  [Security for Developers workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/66275888-6bab-4872-8c6e-ed2fe132a362/en-US)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
