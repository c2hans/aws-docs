---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/terraform-aws-provider-best-practices/community.html
---

# Best practices for community modules
<a name="community"></a>

Using modules effectively is key to managing complex Terraform configurations and promoting reuse. This section provides best practices around community modules, dependencies, sources, abstraction, and contributions.

## Discover community modules
<a name="discovery"></a>

Search the [Terraform Registry](https://registry.terraform.io/namespaces/terraform-aws-modules), [GitHub](https://github.com/terraform-aws-modules), and other sources for existing AWS modules that might solve your use case before you build a new module. Look for popular options that have recent updates and are actively maintained.

### Use variables for customization
<a name="use-variables-for-customization.91930afe-06fe-5186-a4d7-40b8a1fe8b5c"></a>

When you use community modules, pass inputs through variables instead of forking or directly modifying the source code. Override defaults where required instead of changing the internals of the module.

Forking should be limited to contributing fixes or features to the original module to benefit the broader community.

## Understand dependencies
<a name="dependencies"></a>

Before you use the module, review its source code and documentation to identify dependencies:
+ **Required providers**: Note the versions of AWS, Kubernetes, or other providers the module requires.
+ **Nested modules**: Check for other modules used internally that introduce cascading dependencies.
+ **External data sources**: Note the APIs, custom plugins, or infrastructure dependencies that the module relies on.

By mapping out the full tree of direct and indirect dependencies, you can avoid surprises when you use the module.

## Use trusted sources
<a name="trusted-sources"></a>

Sourcing Terraform modules from unverified or unknown publishers introduces significant risk. Use modules only from trusted sources.
+ Favor certified modules from the [Terraform Registry](https://registry.terraform.io/namespaces/terraform-aws-modules) that are published by verified creators such as AWS or HashiCorp partners.
+ For custom modules, review publisher history, support levels, and usage reputation, even if the module is from your own organization.

By not allowing modules from unknown or unvetted sources, you can reduce the risk of injecting vulnerabilities or maintenance issues into your code.

### Subscribe to notifications
<a name="subscribe-to-notifications.18e4fe26-5c3f-572c-8d32-45b1c40eda58"></a>

Subscribe to notifications for new module releases from trusted publishers:
+ Watch GitHub module repositories to get alerts on new versions of the module.
+ Monitor publisher blogs and changelogs for updates.
+ Get proactive notifications for new versions from verified, highly rated sources instead of implicitly pulling in updates.

Consuming modules only from trusted sources and monitoring changes provide stability and security. Vetted modules enhance productivity while minimizing supply chain risk.

## Contribute to community modules
<a name="contribute-community"></a>

Submit fixes and enhancements for community modules that are hosted in GitHub:
+ Open pull requests on modules to address defects or limitations that you encounter in your usage.
+ Request new best practice configurations to be added to existing OSS modules by creating issues.

Contributing to community modules enhances reusable, codified patterns for all Terraform practitioners.
