---
source_url: https://docs.aws.amazon.com/transfer/latest/userguide/test-sftp-connector.html
---

# Test an SFTP connector
<a name="test-sftp-connector"></a>

After you create an SFTP connector, we recommend that you test it before you attempt to transfer any files using your new connector.

**To test an SFTP connector**

1. Open the AWS Transfer Family console at [https://console.aws.amazon.com/transfer/](https://console.aws.amazon.com/transfer/).

1. In the left navigation pane, choose **SFTP Connectors**, and select a connector.

1. From the **Actions** menu, choose **Test connection**.
![The Transfer Family console, showing an SFTP connector selected, and the Test connectionTest connection action highlighted.](http://docs.aws.amazon.com/transfer/latest/userguide/images/connector-test-choose.png)

The system returns a message, indicating whether the test passes or fails. If the test fails, the system provides an error message based on the reason the test failed.

![The SFTP connector test connection panel, showing a successful test.](http://docs.aws.amazon.com/transfer/latest/userguide/images/connector-test-success.png)

![The SFTP connector test connection panel, showing a failed test: the error message indicates that the access role for the connector is incorrect.](http://docs.aws.amazon.com/transfer/latest/userguide/images/connector-test-fail-role.png)

**Note**
To use the API to test your connector, see the [TestConnection](https://docs.aws.amazon.com/transfer/latest/APIReference/API_TestConnection) API documentation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Transfer Family. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query transfer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
