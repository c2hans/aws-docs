---
source_url: https://docs.aws.amazon.com/wellarchitected/2024-06-27/framework/sec_appsec_centralize_services_for_packages_and_dependencies.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SEC11-BP05 Centralize services for packages and dependencies
<a name="sec_appsec_centralize_services_for_packages_and_dependencies"></a>

Provide centralized services for builder teams to obtain software packages and other dependencies. This allows the validation of packages before they are included in the software that you write, and provides a source of data for the analysis of the software being used in your organization.

**Desired outcome:** Software is comprised of a set of other software packages in addition to the code that is being written. This makes it simple to consume implementations of functionality that are repeatedly used, such as a JSON parser or an encryption library. Logically centralizing the sources for these packages and dependencies provides a mechanism for security teams to validate the properties of the packages before they are used. This approach also reduces the risk of an unexpected issue being caused by a change in an existing package, or by builder teams including arbitrary packages directly from the internet. Use this approach in conjunction with the manual and automated testing flows to increase the confidence in the quality of the software that is being developed.

**Common anti-patterns:**
+  Pulling packages from arbitrary repositories on the internet.
+  Not testing new packages before making them available to builders.

**Benefits of establishing this best practice:**
+  Better understanding of what packages are being used in the software being built.
+  Being able to notify workload teams when a package needs to be updated based on the understanding of who is using what.
+  Reducing the risk of a package with issues being included in your software.

 **Level of risk exposed if this best practice is not established: **Medium

## Implementation guidance
<a name="implementation-guidance"></a>

 Provide centralized services for packages and dependencies in a way that is simple for builders to consume. Centralized services can be logically central rather than implemented as a monolithic system. This approach allows you to provide services in a way that meets the needs of your builders. You should implement an efficient way of adding packages to the repository when updates happen or new requirements emerge. AWS services such as [AWS CodeArtifact](https://aws.amazon.com/codeartifact/) or similar AWS partner solutions provide a way of delivering this capability.

### Implementation steps:
<a name="implementation-steps"></a>
+ Implement a logically centralized repository service that is available in all of the environments where software is developed.
+ Include access to the repository as part of the AWS account vending process.
+ Build automation to test packages before they are published in a repository.
+ Maintain metrics of the most commonly used packages, languages, and teams with the highest amount of change.
+  Provide an automated mechanism for builder teams to request new packages and provide feedback.
+  Regularly scan packages in your repository to identify the potential impact of newly discovered issues.

## Resources
<a name="resources"></a>

 **Related best practices:**
+  [SEC11-BP02 Automate testing throughout the development and release lifecycle](sec_appsec_automate_testing_throughout_lifecycle.md)

 **Related documents:**
+  [Accelerate deployments on AWS with effective governance](https://aws.amazon.com/blogs/architecture/accelerate-deployments-on-aws-with-effective-governance/)
+  [Tighten your package security with CodeArtifact Package Origin Control toolkit](https://aws.amazon.com/blogs/devops/tighten-your-package-security-with-codeartifact-package-origin-control-toolkit/)
+  [Detecting security issues in logging with Amazon CodeGuru Reviewer](https://aws.amazon.com/blogs/devops/detecting-security-issues-in-logging-with-amazon-codeguru-reviewer/)
+  [Supply chain Levels for Software Artifacts (SLSA)](https://slsa.dev/)

 **Related videos:**
+  [Proactive security: Considerations and approaches](https://www.youtube.com/watch?v=CBrUE6Qwfag)
+  [The AWS Philosophy of Security (re:Invent 2017)](https://www.youtube.com/watch?v=KJiCfPXOW-U)
+  [When security, safety, and urgency all matter: Handling Log4Shell](https://www.youtube.com/watch?v=pkPkm7W6rGg)

 **Related examples:**
+  [Multi Region Package Publishing Pipeline](https://github.com/aws-samples/multi-region-python-package-publishing-pipeline) (GitHub)
+  [Publishing Node.js Modules on AWS CodeArtifact using AWS CodePipeline](https://github.com/aws-samples/aws-codepipeline-publish-nodejs-modules) (GitHub)
+  [AWS CDK Java CodeArtifact Pipeline Sample](https://github.com/aws-samples/aws-cdk-codeartifact-pipeline-sample) (GitHub)
+  [Distribute private .NET NuGet packages with AWS CodeArtifact](https://github.com/aws-samples/aws-codeartifact-nuget-dotnet-pipelines) (GitHub)
