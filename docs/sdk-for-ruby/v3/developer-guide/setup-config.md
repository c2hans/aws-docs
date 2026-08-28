---
source_url: https://docs.aws.amazon.com/sdk-for-ruby/v3/developer-guide/setup-config.html
---

# Configuring AWS SDK for Ruby service clients in code
<a name="setup-config"></a>

When configuration is handled directly in code, the configuration scope is limited to the application that uses that code. Within that application, there are options for the global configuration of all service clients, the configuration to all clients of a certain AWS service type, or the configuration to a specific service client instance.

## `Aws.config`
<a name="config"></a>

To provide global configuration within your code for all AWS classes, use [`Aws.config`](https://github.com/aws/aws-sdk-ruby/blob/version-3/gems/aws-sdk-core/lib/aws-sdk-core/plugins/global_configuration.rb) that is available in the `aws-sdk-core` gem.

 `Aws.config` supports two syntaxes for different uses. Global settings can either be applied for all AWS services or for a specific service. For the complete list of supported settings, see the `Client` [`Options`](https://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/MachineLearning/Client.html#initialize-instance_method) in the *AWS SDK for Ruby API Reference*.

### Global settings through `Aws.config`
<a name="global-config"></a>

To set service-agnostic settings through `Aws.config`, use the following syntax:

```
Aws.config[:{{<global setting name>}}] = {{<value>}}
```

These settings are merged into any created service clients.

 Example of a global setting:

```
Aws.config[:{{region}}] = {{'us-west-2'}}
```

 If you try to use a setting name that is not globally supported, an error is raised when you attempt to create an instance of a type of service that doesn't support it. If this happens, use service-specific syntax instead.

### Service-specific settings through `Aws.config`
<a name="service-config"></a>

 To set service-specific settings through `Aws.config`, use the following syntax:

```
Aws.config[:{{<service identifier>}}] = { {{<global setting name>}}: {{<value>}} }
```

 These settings are merged into all created service clients of that service type.

 Example of a setting that only applies to Amazon S3:

```
 Aws.config[:{{s3}}] = { {{force_path_style}}: {{true}} }
```

 The `{{<service identifier>}}` can be identified by looking at the name of the corresponding [AWS SDK for Ruby gem name](https://github.com/aws/aws-sdk-ruby/tree/version-3/gems), and using the suffix that follows "`aws-sdk-`". For example:
+ For `aws-sdk-s3`, the service identifier string is "`s3`".
+ For `aws-sdk-ecs`, the service identifer string is "`ecs`".

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Ruby. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-ruby` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
