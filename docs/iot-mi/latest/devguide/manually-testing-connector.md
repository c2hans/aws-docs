---
source_url: https://docs.aws.amazon.com/iot-mi/latest/devguide/manually-testing-connector.html
---

# Manually test your C2C connector
<a name="manually-testing-connector"></a>

To manually test your C2C connector end-to-end, you must simulate both the customer and the end user.

**You will need the following resources:**
+ An AWS Lambda ARN designating the connector you would like to test.
+ A testing OAuth 2.0 user account from your cloud platform.
+ A connector registered with managed integrations for AWS IoT Device Management. For more information, see [Use a C2C (Cloud-to-Cloud) connector](use-c2c-create-cloud-connector.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Managed integrations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-mi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
