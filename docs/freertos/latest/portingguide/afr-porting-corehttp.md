---
source_url: https://docs.aws.amazon.com/freertos/latest/portingguide/afr-porting-corehttp.html
---

# Configuring the coreHTTP library
<a name="afr-porting-corehttp"></a>

Devices on the edge can use the HTTP protocol to communicate with the AWS Cloud. AWS IoT services host an HTTP server that sends and receives messages to and from connected devices at the edge.

## Testing
<a name="testing-corehttp"></a>

Follow the steps below for testing:
+ Setup the PKI for TLS mutual authentication with AWS or an HTTP server.
+ Run CoreHTTP integration tests.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for FreeRTOS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query freertos` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
