---
source_url: https://docs.aws.amazon.com/apprunner/latest/dg/config-file.html
---

AWS App Runner is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS App Runner availability change](https://docs.aws.amazon.com/apprunner/latest/dg/apprunner-availability-change.html).

# Setting App Runner service options using a configuration file
<a name="config-file"></a>

**Note**
Configuration files are applicable only to [services that are based on source code](service-source-code.md). You can't use configuration files with [image-based services](service-source-image.md).

When you create an AWS App Runner service using a source code repository, AWS App Runner requires information about building and starting your service. You can provide this information each time you create a service using the App Runner console or API. Alternatively, you can set service options by using a *configuration file*. The options that you specify in a file become part of your source repository, and any changes to these options are tracked similarly to how changes to the source code are tracked. You can use the App Runner configuration file to specify more options than the API supports. You don't need to provide a configuration file if you only need the basic options that the API supports.

The App Runner configuration file is a YAML file that's named `apprunner.yaml` in the [source directory](service-source-code.md#service-source-code.source-directory) of your application’s repository. It provides build and runtime options for your service. Values in this file instruct App Runner how to build and start your service, and provide runtime context such as network settings and environment variables.

The App Runner configuration file doesn’t include operational settings, such as CPU and memory.

For examples of App Runner configuration files, see [App Runner configuration file examples](config-file-examples.md). For a complete reference guide, see [App Runner configuration file reference](config-file-ref.md).

**Topics**
+ [App Runner configuration file examples](config-file-examples.md)
+ [App Runner configuration file reference](config-file-ref.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for App Runner. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apprunner` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
