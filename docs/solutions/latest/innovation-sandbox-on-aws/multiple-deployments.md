---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/multiple-deployments.html
---

# Multiple deployments with different namespaces
<a name="multiple-deployments"></a>

You can deploy multiple independent instances of Innovation Sandbox within the same AWS Organization by using a different namespace for each deployment. The **Namespace** parameter, which you set on each stack, prefixes all resources that the solution creates. As a result, deployments with different namespaces are fully isolated and do not interfere with one another.

Use cases for multiple deployments include:
+ Separate instances for different teams or business units (for example, `devisb` for a development team and `secisb` for a security team)
+ A non-production instance for testing solution upgrades before applying them to the production instance
+ Distinct governance configurations (allowed services, budget limits, or managed Regions) for different populations of users

Each deployment requires its own set of four stacks (AccountPool, IDC, Data, Compute) with the same namespace value across all member stacks. All stacks for a given namespace must be deployed in the same Region. Each namespace also requires its own SAML 2.0 application in IAM Identity Center and its own set of user groups.

The namespace must be 3–8 alphanumeric characters (for example, `myisb`, `team2`, `prodisb`).

When running multiple deployments in the same Organization, keep in mind that all instances share the same underlying AWS Organizations API quotas, IAM Identity Center instance, and service quotas in the management and Hub accounts. High-volume operations in one deployment (such as bulk account moves or large-scale lease approvals) can consume shared API capacity that affects the other deployments.
