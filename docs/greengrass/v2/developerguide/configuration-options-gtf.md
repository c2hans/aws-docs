---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/configuration-options-gtf.html
---

# Greengrass Testing Framework configuration options
<a name="configuration-options-gtf"></a>

## GTF configuration options
<a name="configuration-options-gtf-options"></a>

Greengrass Testing Framework (GTF) enables you to configure certain parameters during the launch of the end-to-end testing process to orchestrate the test flow. You can specify these configuration options as CLI arguments for the GTF standalone JAR.

<a name="gtf_options"></a>GTF version 1.1.0 and later provides the following configuration options.
+ `additional-plugins` – (Optional) Additional Cucumber plugins
+ `aws-region` – Targets specific regional endpoints for AWS services. Defaults to what the AWS SDK discovers.
+ `credentials-path` – Optional AWS profile credentials path. Defaults to credentials discovered on host environment.
+ `credentials-path-rotation` – Optional rotation duration for AWS credentials. Defaults to 15 minutes or `PT15M`.
+ `csr-path` – The path for the CSR using which the device certificate will be generated.
+ `device-mode` – The target device under test. Defaults to local device.
+ `env-stage` – Targets the deployment environment of Greengrass. Defaults to production.
+ `existing-device-cert-arn` – The arn of an existing certificate that you want to use as a device certificate for Greengrass.
+ `feature-path` – File or directory containing additional feature files. Default is no additional feature files are used.
+ `gg-cli-version` – Overrides the version of the Greengrass CLI. Defaults to the value found in `ggc.version`.
+ `gg-component-bucket` – The name of an existing Amazon S3 bucket that houses Greengrass components.
+ `gg-component-overrides` – A list of Greengrass component overrides.
+ `gg-persist` – A list of test elements to persist after a test run. Default behavior is to persist nothing. Accepted values are: `aws.resources`, `installed.software`, and `generated.files`.
+ `gg-runtime` – A list of values to influence how the test interacts with testing resources. These values supersede the `gg.persist` parameter. If the default is empty, it assumes all testing resources are manged by test case, including the installed Greengrass runtime. Accepted values are: `aws.resources`, `installed.software`, and `generated.files`.
+ `ggc-archive` – The path to the archived Greengrass nucleus component.
+ `ggc-install-root` – Directory to install the Greengrass nucleus component. Defaults to test.temp.path and test run folder.
+ `ggc-log-level` – Set the Greengrass nucleus log level for the test run. Default is "INFO".
+ `ggc-tes-rolename` – The IAM role that AWS IoT Greengrass Core will assume to access AWS services. If a role with given name does not exist then one will be created and default access policy.
+ `ggc-trusted-plugins` – The comma separate list of the paths (on host) of the trusted plugins that need to added to Greengrass. To provide the path on the DUT itself, prefix the path with 'dut:'
+ `ggc-user-name` – The user:group posixUser value for the Greengrass nucleus. Defaults to the current username that is logged in.
+ `ggc-version` – Overrides the version of the running Greengrass nucleus component. Defaults to the value found in ggc.archive.
+ `log-level` – Log level of the test run. Defaults to "INFO".
+ `parallel-config` – Set of batch index and number of batches as a JSON String. Default value of batch index is 0 and number of batches is 1.
+ `proxy-url` – Configure all tests to route traffic through this URL.
+ `tags` – Only run feature tags. Can be intersected with '&'
+ `test-id-prefix` – A common prefix applied to all test specific resources including AWS resource names and tags. Default is a "gg" prefix.
+ `test-log-path` – Directory that will contain the results of the entire test run. Defaults to "testResults".
+ `test-results-json` – Flag to determine if a resulting Cucumber JSON report is generated written to disk. Defaults to true.
+ `test-results-log` – Flag to determine if the console output is generated written to disk. Defaults to false.
+ `test-results-xml` – Flag to determine if a resulting JUnit XML report is generated written to disk. Defaults to true.
+ `test-temp-path` – Directory to generate local test artifacts. Defaults to a random temp directory prefixed with gg-testing.
+ `timeout-multiplier` – Multiplier provided to all test timeouts. Default is 1.0.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
