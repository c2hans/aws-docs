---
source_url: https://docs.aws.amazon.com/freertos/latest/userguide/lts-configure-aws-credentials.html
---

# Configure AWS credentials to use the IDT UI
<a name="lts-configure-aws-credentials"></a>

You must configure your IAM user credentials for the AWS user you created in [Create an AWS account](lts-idt-dev-tester-prereqs.md#lts-config-aws-account). You can specify your credentials in one of two ways:
+ In a credentials file
+ As environment variables

## Configure AWS credentials with a credentials file
<a name="lts-config-cred-file"></a>

IDT uses the same credentials file as the AWS CLI. For more information, see [Configuration and credential files](https://docs.aws.amazon.com/cli/latest/userguide/cli-config-files.html).

The location of the credentials file varies based on the operating system you use:
+ **macOS and Linux** – `~/.aws/credentials`
+ **Windows** – `C:\Users\{{UserName}}\.aws\credentials`

Add your AWS credentials to the `credentials` file in the following format:

```
[default]
aws_access_key_id = {{your_access_key_id}}
aws_secret_access_key = {{your_secret_access_key}}
```

**Note**
If you don't use the `default` AWS profile, you must specify the profile name in the IDT for FreeRTOS UI. For more information about profiles, see [ Configuration and credential file settings](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html).

## Configure AWS credentials with environment variables
<a name="lts-config-env-vars"></a>

Environment variables are variables maintained by the operating system and used by system commands. They're not saved if you close the SSH session. The IDT for FreeRTOS UI uses the `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` environment variables to store your AWS credentials.

To set these variables on Linux, macOS, or Unix, use **export**:

```
export AWS_ACCESS_KEY_ID={{your_access_key_id}}
export AWS_SECRET_ACCESS_KEY={{your_secret_access_key}}
```

To set these variables on Windows, use **set**:

```
set AWS_ACCESS_KEY_ID={{your_access_key_id}}
set AWS_SECRET_ACCESS_KEY={{your_secret_access_key}}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for FreeRTOS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query freertos` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
