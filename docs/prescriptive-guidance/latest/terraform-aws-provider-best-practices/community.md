---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/terraform-aws-provider-best-practices/community.html
---

# Best practices for community modules
<a name="community"></a>

Using modules effectively helps you manage complex Terraform configurations and promote reuse. This section covers recommended practices for community modules, dependencies, sources, abstraction, and contributions.

## Discover community modules
<a name="discovery"></a>

Search the [Terraform Registry](https://registry.terraform.io/namespaces/terraform-aws-modules), [GitHub](https://github.com/terraform-aws-modules), and other sources for existing AWS modules that might solve your use case before you build a new module. Look for modules that have recent updates and are actively maintained.

### Use variables for customization
<a name="use-variables-for-customization.b987b7a0-bb46-5544-9cb3-e7b0d3cb1459"></a>

When you use community modules, pass inputs through variables instead of forking or directly modifying the source code. Override defaults where required instead of changing the internals of the module.

Limit forking to contributing fixes or features back to the original module to benefit the broader community.

## Understand dependencies
<a name="dependencies"></a>

Before you use the module, review its source code and documentation to identify dependencies:
+ **Required providers**: Note the versions of AWS, Kubernetes, or other providers the module requires.
+ **Nested modules**: Check for other modules used internally that introduce cascading dependencies.
+ **External data sources**: Note the APIs, custom plugins, or infrastructure dependencies that the module relies on.

By mapping out the full tree of direct and indirect dependencies, you can prevent unexpected issues when you use the module.

## Use trusted sources
<a name="trusted-sources"></a>

Sourcing Terraform modules from unverified or unknown publishers introduces significant risk. Use modules only from sources that you trust, and review them like any other third-party code.
+ On the Terraform Registry, modules with the verified badge are published by HashiCorp partners. AWS publishes verified modules in the [aws-ia](https://registry.terraform.io/namespaces/aws-ia) namespace.
+ Widely used community namespaces, such as [terraform-aws-modules](https://registry.terraform.io/namespaces/terraform-aws-modules), aren't verified. Review their maintainers, release history, and open issues before you adopt them.
+ For custom modules, review publisher history, support levels, and usage reputation, even if the module is from your own organization.
+ Pin each module to an exact version, and review the changes before you upgrade. For tighter supply chain control, pin a commit SHA, as described in [Use recommended module sources](https://docs.aws.amazon.com/prescriptive-guidance/latest/terraform-aws-provider-best-practices/structure.html#module-sources).

Restricting modules to trusted, vetted sources reduces the risk of introducing vulnerabilities or maintenance issues into your code.

### Subscribe to notifications
<a name="subscribe-to-notifications.980b6f0e-caa1-5bee-9026-41a16cce4223"></a>

Subscribe to notifications for new module releases from trusted publishers:
+ Watch GitHub module repositories to get alerts on new versions of the module.
+ Monitor publisher blogs and changelogs for updates.
+ Get proactive notifications for new versions from verified, well-maintained sources instead of automatically receiving updates.

Consuming modules only from trusted sources and monitoring changes helps maintain stability and reduce security risk across your supply chain.

## Contribute to community modules
<a name="contribute-community"></a>

Submit fixes and enhancements for community modules that are hosted in GitHub:
+ Open pull requests on modules to address defects or limitations that you encounter in your usage.
+ Request new best practice configurations to be added to existing OSS modules by creating issues.

Contributing to community modules enhances reusable, codified patterns for all Terraform practitioners.
