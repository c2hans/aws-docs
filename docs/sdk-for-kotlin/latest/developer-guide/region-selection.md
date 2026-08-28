---
source_url: https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/region-selection.html
---

# AWS Region selection
<a name="region-selection"></a>

With AWS Regions, you can access AWS services that operate in a specific geographic area. This can be useful both for redundancy and to keep your data and applications running close to where you and your users will access them.

## Default Region provider chain
<a name="default-region-provider-chain"></a>

When loading a service client’s configuration [from the environment](creating-clients.md#loading-from-the-environment), the following lookup process is used:

1. Any explicit Region set on the builder.

1. The `aws.region` JVM system property is checked. If it’s set, that Region is used in the configuration of the client.

1. The `AWS_REGION` environment variable is checked. If it’s set, that Region is used in the configuration of the client.

   1.  **Note**: This environment variable is set by the Lambda container.

1. The SDK checks the AWS shared configuration file. If the `region` property is set for the active profile, the SDK uses it.

   1. The `AWS_CONFIG_FILE` environment variable can be used to customize the location of the shared config file.

   1. The `aws.profile` JVM system property or the `AWS_PROFILE` environment variable can be used to customize the profile that the SDK loads.

1. The SDK attempts to use the Amazon EC2 Instance Metadata Service to determine the Region of the currently running EC2 instance.

1. If the Region still isn’t resolved at this point, client creation fails with an exception.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Kotlin. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-kotlin` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
