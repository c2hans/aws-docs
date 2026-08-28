---
source_url: https://docs.aws.amazon.com/solutions/latest/media2cloud-on-aws/using-aws-command-line-interface.html
---

# Using AWS Command Line Interface
<a name="using-aws-command-line-interface"></a>

 Determine whether the AWS Command Line Interface (AWS CLI) is available in your environment. For installation instructions, see [What Is the AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) in the *AWS CLI User Guide*. After confirming that the AWS CLI is available, run the following command.

```
      $ aws cloudformation delete-stack --stack-name
      <{{installation-stack-name}}>
```

 Replace {{<installation-stack-name}}{{>}} with the name of your CloudFormation stack.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Media2Cloud on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
