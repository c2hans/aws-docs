---
source_url: https://docs.aws.amazon.com/whitepapers/latest/practicing-continuous-integration-continuous-delivery/summary-of-best-practices.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Summary of best practices
<a name="summary-of-best-practices"></a>

The following are some best practices for CI/CD.

**Do:**
+  Treat your infrastructure as code:
  +  Use version control for your infrastructure code.
  +  Make use of bug tracking/ticketing systems.
  +  Have peers review changes before applying them.
  +  Establish infrastructure code patterns/designs.
  +  Test infrastructure changes like code changes.
+  Put developers into integrated teams of no more than 12 self-sustaining members.
+  Have all developers commit code to the main branch frequently, with no long-running feature branches.
+  Consistently adopt a build system such as Maven or Gradle across your organization and standardize builds.
+  Bake security into your code pipeline.
+  Have developers build unit tests toward 100% coverage of the code base.
+  Ensure that unit tests are 70% of the overall testing in duration, number, and scope.
+  Ensure that unit tests are up-to-date and not neglected. Unit test failures should be fixed, not bypassed.
+  Treat your continuous delivery configuration as code.
+  Establish role-based security controls (that is, who can do what and when):
  +  Monitor/track every resource possible.
  +  Alert on services, availability, and response times.
  +  Capture, learn, and improve.
  +  Share access with everyone on the team.
  +  Plan metrics and monitoring into the lifecycle.
+  Keep and track standard metrics:
  +  Number of builds.
  +  Number of deployments.
  +  Average time for changes to reach production.
  +  Average time from first pipeline stage to each stage.
  +  Number of changes reaching production.
  +  Average build time.
+  Use multiple distinct pipelines for each branch and team.

 **Don’t:**
+  Have long-running branches with large complicated merges.
+  Have manual tests.
+  Have manual approval processes, gates, code reviews, and security reviews.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
