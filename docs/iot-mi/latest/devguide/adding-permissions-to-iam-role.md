---
source_url: https://docs.aws.amazon.com/iot-mi/latest/devguide/adding-permissions-to-iam-role.html
---

# Add permissions to your IAM Role
<a name="adding-permissions-to-iam-role"></a>

All Managed Integrations APIs require AWS sigV4 authentication to invoke. SigV4 is signing protocol to authenticate AWS API requests using your AWS account credentials. The IAM role you use to invoke the Managed Integrations APIs must have the following permissions to be able to successfully invoke the APIs:

```
 	"Version": "2012-10-17",
 	"Statement": [
 	{
 		"Sid": "Statement1",
 		"Effect": "Allow",
 		"Action": [
 			"iotmanagedintegrations:{{Your-Required-Actions}}"
 		],
 		"Resource": [
 			"{{Your-Resource}}"
 		]
 	}]
}
```

For additional information on adding these permissions, contact Support.

**Additional resources**
To register your C2C connector, you will need the following:
+ The Lambda ARN designating the connector you would like to register.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Managed integrations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-mi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
