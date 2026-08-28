---
source_url: https://docs.aws.amazon.com/solutions/latest/security-automations-for-aws-waf/use-lambda-log-parser-json-file.html
---

# Use Lambda log parser JSON file
<a name="use-lambda-log-parser-json-file"></a>

## Use Lambda log parser JSON file for HTTP Flood protection
<a name="use-lambda-log-parser-json-file-for-http-flood-protection"></a>

If you chose `Yes - AWS Lambda log parser` for the **Activate HTTP Flood Protection** template parameter, this solution creates a configuration file named ` <stack_name>-waf_log_conf.json` and uploads it to the Amazon S3 bucket used to store the AWS WAF log files. To find the bucket name, refer to the **WafLogBucket** variable in the CloudFormation output. The following figure shows an example.

 **Screenshot depicting a screen labeled AWSWAFSecurityAutomations and listing four outputs**

![stack outputs](http://docs.aws.amazon.com/solutions/latest/security-automations-for-aws-waf/images/stack-outputs.png)

If you edit and overwrite the ` <stack_name>-waf_log_conf.json` file on Amazon S3, the `Log Parser` Lambda function considers the new values when processing new AWS WAF log files. The following is a sample configuration file:

 **Screenshot of a sample configuration file**

![http flood config](http://docs.aws.amazon.com/solutions/latest/security-automations-for-aws-waf/images/http-flood-config.png)

Parameters include the following:
+ General:
  +  **Request threshold (required)** - The maximum acceptable requests per five minutes, per IP address. This solution uses the value you define when provisioning or updating the CloudFormation stack.
  +  **Block period (required)** - The period (in minutes) to block applicable IP addresses. This solution uses the value you define when provisioning or updating the CloudFormation stack.
  +  **Ignored suffixes** - Requests accessing this type of resource don’t count to request threshold. By default, this list is empty.
+  **URI list** - Uuse this to define a custom request threshold and block period for specifics URLs. By default, this list is empty.

When WAF logs arrive in the **WafLogBucket**, they will be processed by Lambda log parser function using the configurations in your configuration file. The solution writes the result to an output file named ` <stack_name>-waf_log_out.json` in the same bucket. If the output file contains a list of the IP addresses identified as attackers, the solution adds them to the WAF IP set for **HTTP Flood**, and they’re blocked from accessing your application. If the output files have no IP addresses, check if your configuration file is valid or if the rate limit has exceeded according to the configuration file.

## Use Lambda log parser JSON file for scanner and probe protection
<a name="use-lambda-log-parser-json-file-for-scanner-and-probe-protection"></a>

If you chose `Yes - AWS Lambda log parser` for the **Activate Scanner & Probe Protection** template parameter, this solution creates a configuration file named ` <stack_name>-app_log_conf.json` and uploads it to the defined Amazon S3 bucket used to store CloudFront or Application Load Balancer log files.

If you edit and overwrite on the ` <stack_name>-app_log_conf.json` on Amazon S3, the `Log Parser` Lambda function considers the new values when processing new AWS WAF log files. The following is a sample configuration file:

 **Screenshot of configuration file**

![scanner probes config file](http://docs.aws.amazon.com/solutions/latest/security-automations-for-aws-waf/images/scanner-probes-config-file.png)

Parameters include the following:
+ General:
  +  **Error threshold (required)** - The maximum acceptable bad requests per minute, per IP address. This solution uses the value you defined when provisioning or updating the CloudFormation stack.
  +  **Block period (required)** - The period (in minutes) to block applicable IP addresses. This solution uses the value you defined when provisioning or updating the CloudFormation stack.
  +  **Error codes** - Return status code considered errors. By default, the list considers the following HTTP status codes as errors: `400 (Bad Request)`, `401 (Unauthorized)`, `403 (Forbidden)`, `404 (Not Found)`, and `405 (Method Not Allowed)`.
+  **URI list** - Use this to define a custom request threshold and block period for specifics URLs. By default, this list is empty.

When application access logs arrive in the **AppAccessLogBucket**, the `Log Parser` Lambda function processes them using the configurations in your configuration file. The solution writes the result to an output file named ` <stack_name>``-app\_log\_out.json` in the same bucket. If the output file contains a list of the IP addresses identified as attackers, the solution adds them to the WAF IP set for **Scanner & Probe** and blocks them from accessing your application. If the output files have no IP addresses, check if your configuration file is valid or if the rate limit has been exceeded according to the configuration file.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Security Automations for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
