---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/platforms-linux-extend.config-files.html
---

# Configuration files
<a name="platforms-linux-extend.config-files"></a>

You can add [configuration files](ebextensions.md) to the `.ebextensions` directory of your application's source code to configure various aspects of your Elastic Beanstalk environment. Among other things, configuration files let you customize software and other files on your environment's instances and run initialization commands on the instances. For more information, see [Customizing software on Linux servers](customize-containers-ec2.md).

You can also set [configuration options](command-options.md) using configuration files. Many of the options control platform behavior, and some of these options are [platform specific](command-options-specific.md).

For platforms based on Amazon Linux 2 and Amazon Linux 2023, we recommend using *Buildfile*, *Procfile*, and *platform hooks* to configure and run custom code on your environment instances during instance provisioning. These mechanisms are described in the previous sections on this page. You can still use commands and container commands in `.ebextensions` configuration files, but they aren't as easy to work with. For example, writing command scripts inside a YAML file can be challenging from a syntax standpoint. You still need to use `.ebextensions` configuration files for any script that needs a reference to a AWS CloudFormation resource.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Beanstalk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticbeanstalk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
