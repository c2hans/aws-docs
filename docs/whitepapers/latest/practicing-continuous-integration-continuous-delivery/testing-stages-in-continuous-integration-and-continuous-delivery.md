---
source_url: https://docs.aws.amazon.com/whitepapers/latest/practicing-continuous-integration-continuous-delivery/testing-stages-in-continuous-integration-and-continuous-delivery.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Testing stages in continuous integration and continuous delivery
<a name="testing-stages-in-continuous-integration-and-continuous-delivery"></a>

 The three CI/CD teams should incorporate testing into the software development lifecycle at the different stages of the CI/CD pipeline. Overall, testing should start as early as possible. The following testing pyramid is a concept provided by Mike Cohn in *Succeeding with Agile*. It shows the various software tests in relation to their cost and speed at which they run.

![Diagram showing CI/CD testing pyramid](http://docs.aws.amazon.com/whitepapers/latest/practicing-continuous-integration-continuous-delivery/images/ci-cd-testing-pyramid.png)

 Unit tests are on the bottom of the pyramid. They are both the fastest to run and the least expensive. Therefore, unit tests should make up the bulk of your testing strategy. A good rule of thumb is about 70 percent. Unit tests should have near-complete code coverage because bugs caught in this phase can be fixed quickly and cheaply.

 Service, component, and integration tests are above unit tests on the pyramid. These tests require detailed environments and therefore, are more costly in infrastructure requirements and slower to run. Performance and compliance tests are the next level. They require production-quality environments and are more expensive yet. UI and user acceptance tests are at the top of the pyramid and require production-quality environments as well.

 All of these tests are part of a complete strategy to assure high-quality software. However, for speed of development, emphasis is on the number of tests and the coverage in the bottom half of the pyramid.

 The following sections discuss the CI/CD stages.

## Setting up the source
<a name="setting-up-the-source"></a>

 At the beginning of the project, it’s essential to set up a source where you can store your raw code and configuration and schema changes. In the source stage, choose a source code repository such as one hosted in GitHub, Amazon CodeCatalyst, or AWS CodeCommit.

## Setting up and running builds
<a name="setting-up-and-running-builds"></a>

 Build automation is essential to the CI process. When setting up build automation, the first task is to choose the right build tool. There are many build tools, such as:
+  Ant, Maven, and Gradle for Java and Kotlin
+  esbuild, Rollup, Webpack, and Vite for JavaScript and TypeScript
+  Cargo for Rust
+  Make for C/C\+\+
+  Go Build for Go
+  Rake for Ruby

 The build tool that will work best for you depends on the programming language of your project and the skill set of your team. After you choose the build tool, all the dependencies need to be clearly defined in the build scripts, along with the build steps. It’s also a best practice to version the final build artifacts, which makes it easier to deploy and to keep track of issues.

## Building
<a name="building"></a>

In the build stage, the build tools will take any change to the source code repository as input, build the software, and run the following types of tests:

 **Unit Testing** – Tests a specific section of code to ensure the code does what it is expected to do. The unit testing is performed by software developers during the development phase. At this stage, a static code analysis, data flow analysis, code coverage, and other software verification processes can be applied.

 **Static Code Analysis** – This test is performed without actually running the application after the build and unit testing. This analysis can help to find coding errors and security holes, and it also can ensure conformance to coding guidelines.

 **Static Application Security Testing (SAST)** – This test is used to analyze code against security violations such as [XML External Entity Processing](https://owasp.org/www-community/vulnerabilities/XML_External_Entity_(XXE)_Processing) ,[SQL Injection](https://owasp.org/www-community/attacks/SQL_Injection) and [Cross Site Scripting](https://owasp.org/www-community/attacks/xss/). As soon as violations are detected, the build will fail and any progress will be blocked in the pipeline. For further details, see [Security in every stage of CI/CD pipeline](security-in-every-stage-of-cicd-pipeline.md).

 **Secrets Detection** – This check is used to identify secrets such as usernames, passwords, and access keys in code. As soon as secrets are discovered, the build will fail immediately. For further details, see [Security in every stage of CI/CD pipeline](security-in-every-stage-of-cicd-pipeline.md).

 **Software Composition Analysis (SCA)** – SCA tools enable users to manage and analyze the open-source components in their applications. They also verify licensing and assess security vulnerabilities. SCA tools can launch workflows to fix these vulnerabilities. Any findings that exceed the configured threshold will immediately fail the build and stop any forward progress in the pipeline. These tools also require a software bill of materials (SBOM) existence. For further details, see [Security in every stage of CI/CD pipeline](security-in-every-stage-of-cicd-pipeline.md).

 **Software Bill of Materials (SBOM)** – SBOM is a reporting mechanism to detail all the components and dependencies involved in the development and delivery of an application. This will allow visibility of product components, assure file integrity, leverage licensing governance, and robust vulnerability scanning. For further details, see [Security in every stage of CI/CD pipeline](security-in-every-stage-of-cicd-pipeline.md).

## Staging
<a name="staging"></a>

 In the staging phase, full environments are created that mirror the eventual production environment. The following tests are performed:

 **Integration testing** – Verifies the interfaces between components against software design. Integration testing is an iterative process and facilitates building robust interfaces and system integrity.

 **Component testing** – Tests message passing between various components and their outcomes. A key goal of this testing could be idempotency in component testing. Tests can include extremely large data volumes, or edge situations and abnormal inputs.

 **System testing** – Tests the system end-to-end and verifies if the software satisfies the business requirement. This might include testing the user interface (UI), API, backend logic, and end state.

 **Performance testing** – Determines the responsiveness and stability of a system as it performs under a particular workload. Performance testing also is used to investigate, measure, validate, or verify other quality attributes of the system, such as scalability, reliability, and resource usage. Types of performance tests might include load tests, stress tests, and spike tests. Performance tests are used for benchmarking against predefined criteria.

 **Compliance testing** – Checks whether the code change complies with the requirements of a nonfunctional specification and/or regulations. It determines if you are implementing and meeting the defined standards.

 **User acceptance testing** – Validates the end-to-end business flow. This testing is performed by an end user in a staging environment and confirms whether the system meets the requirements of the requirement specification. Typically, customers employ alpha and beta testing methodologies at this stage.

 **Dynamic Application Security Testing (DAST)** - This type of testing is used to check for security problems in an application while it is running. DAST tools evaluate the application by attacking like a malicious user would from outside. For further details, see [Security in every stage of CI/CD pipeline](security-in-every-stage-of-cicd-pipeline.md).

## Production
<a name="production"></a>

 Finally, after passing the previous tests, the staging phase is repeated in a production environment. In this phase, a final Canary test can be completed by deploying the new code only on a small subset of servers or even one server, or one AWS Region before deploying code to the entire production environment. Specifics on how to safely deploy to production are covered in [Deployment methods](deployment-methods.md).

 The next section discusses building the pipeline to incorporate these stages and tests

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
