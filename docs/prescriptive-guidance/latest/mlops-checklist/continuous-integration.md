---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/mlops-checklist/continuous-integration.html
---

# 5. Continuous integration
<a name="continuous-integration"></a>

The ML system runs tests to validate that the system works from end to end, checking for possible points of failure. Tests are run automatically on commit, and longer tests are run on a fixed schedule. Tests check traditional software engineering areas such as at the unit and system level. In addition, tests capture the particulars of ML by checking data, features, and the model.

|  |
| --- |
| 5.1 Local code checks | Before committing code into a centralized code repository, developers locally run checks such as basic unit tests and static analysis. Running these checks before committing increases overall code quality and catches problems before they enter version control. |
| --- |--- |
| **5.2 Static code analysis** | The central code repository has static code analysis tools that run on commit, quickly. This tooling should improve code style and formatting. It should also check for common security vulnerabilities within source and infrastructure code, common bugs, and other weaknesses in the code. |
| **5.3 Data quality tests** | Data quality tests should, at a bare minimum, check that the data has not violated a fixed schema. A more comprehensive approach is to compute data statistics at ingest, set constraints on the data, and run tests against these.<br />It's possible to set up data quality tests independently or as part of the pipeline. The statistics and constraints are reused for monitoring. |
| **5.4 Feature tests** | As part of a complete pipeline, feature importance is generated. Feature tests assert that the importance of features, or the model's way of attributing feature values, does not change. Feature tests can feed into monitoring because they can alert and track violations in a model's inputs. |
| **5.5 Unit tests** | Unit tests for all code—model, application, and infrastructure—run before commit and on commit. Each unit test provides a check on an important piece of code to confirm that it functions as expected. In the case of ML code, tests can run for algorithmic correctness. |
| **5.6 Integration tests** | An integration test verifies that the pipeline runs end to end successfully, including standing up the associated infrastructure for the pipeline. This test validates that the system is working and logging as expected. If deployment is separate, there should be an end-to-end test for this as well to make sure deployment works. |
| **5.7 Smoke tests** | The system has smoke tests that run in mini and rapid regression of each piece of functionality. Smoke tests are part of continuous integration, and can run in a containerized environment to mimic cloud functionality. |
| **5.8 Load testing** | On-demand load testing is in place. In addition to capturing how the ML system behaves under high and low loads, load tests provide statistics on system-wide throughput or latency. Data gathered through load tests provides information about resource sizes and scaling policies. |
| **5.9 Model functional tests** | Model outputs and inputs run through automated functional tests. To check a behavior within a capability, both outputs and inputs for the model are tested on real or fake data with basic examples. |
| **5.10 Model inference tests with extreme cases** | As part of the minimum functionality testing, model tests should check for extreme behavior given certain inputs before model promotion. This places an additional guardrail to help prevent unexpected behavior. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
