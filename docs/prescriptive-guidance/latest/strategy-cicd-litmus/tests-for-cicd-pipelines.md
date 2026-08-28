---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-cicd-litmus/tests-for-cicd-pipelines.html
---

# Tests for CI/CD pipelines
<a name="tests-for-cicd-pipelines"></a>

The two types of automated tests that are commonly referred to in deployment pipelines are *unit tests* and *integration tests*. However, there are many types of tests that you can run on a code base and the development environment. The [AWS Deployment Pipeline Reference Architecture](https://pipelines.devops.aws.dev/application-pipeline/) defines the following types of tests:
+ **Unit test** – These tests build and run application code to verify that it is performing according to expectations. They simulate all external dependencies that are used in the code base. Examples of unit test tools include [JUnit](https://junit.org/), [Jest](https://jestjs.io/), and [pytest](https://docs.pytest.org/en/stable/).
+ **Integration test** – These tests verify that the application satisfies technical requirements by testing against a provisioned test environment. Examples of integration test tools include [Cucumber](https://cucumber.io/), [vRest NG](https://vrest.io/), and [integ-tests](https://docs.aws.amazon.com/cdk/api/v2/docs/integ-tests-alpha-readme.html) (for AWS CDK).
+ **Acceptance test** – These tests verify that the application satisfies user requirements by testing against a provisioned test environment. Examples of acceptance test tools include [Cypress](https://cypress.io/) and [Selenium](https://selenium.dev/).
+ **Synthetic test** – These tests run continuously in the background to generate traffic and verify that the system is healthy. Examples of synthetic test tools include [Amazon CloudWatch Synthetics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html) and [Dynatrace Synthetic Monitoring](https://www.dynatrace.com/monitoring/platform/synthetic-monitoring/).
+ **Performance test** – These tests simulate production capacity. They determine if the application meets performance requirements and compare metrics to past performance. Examples of performance test tools include [Apache JMeter](https://jmeter.apache.org/), [Locust](https://locust.io/), and [Gatling](https://gatling.io/).
+ **Resilience test** – Also known as *chaos testing*, these tests inject failures into environments in order to identify risk areas. Periods when the failures are injected are then compared to periods without the failures. Examples of resilience test tools include [AWS Fault Injection Service](https://aws.amazon.com/fis/) and [Gremlin](https://www.gremlin.com/).
+ **Static application security test (SAST)** – These tests analyze code for security violations, such as [SQL injection](https://owasp.org/www-community/attacks/SQL_Injection) or [cross-site scripting (XSS)](https://owasp.org/www-community/attacks/xss/). Examples of SAST tools include [Amazon CodeGuru](https://aws.amazon.com/codeguru/), [SonarQube](https://www.sonarqube.org/), and [Checkmarx](https://checkmarx.com/).
+ **Dynamic application security test (DAST)** – These tests are also known as *penetration testing* or *pen testing*. They identify vulnerabilities, such as SQL injection or XSS in a provisioned test environment. Examples of DAST tools include [Zed Attack Proxy (ZAP)](https://www.zaproxy.org/) and [HCL AppScan](https://www.hcltechsw.com/appscan). For more information, see [Penetration Testing](https://aws.amazon.com/security/penetration-testing/).

Not all fully CI/CD pipelines run all of these tests. However, at a minimum, a pipeline should run unit tests and SAST tests on the code base as well as integration and acceptance tests on a test environment.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
