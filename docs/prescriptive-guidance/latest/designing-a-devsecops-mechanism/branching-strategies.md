---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/designing-a-devsecops-mechanism/branching-strategies.html
---

# Branching strategies for IaC
<a name="branching-strategies"></a>

Typical Git methodology uses a primary trunk base (such as `main`) branch for production, a development branch, and feature branches. Many organizations instantly adopt this same design for infrastructure as code (IaC). However, Git methodology is not directly compatible with common infrastructure design patterns. Consider the following points:
+ Applications have several environments.
  + Environment examples include sandbox, development, staging, and production.
+ Environments are not tightly coupled.
  + Production is often tightly coupled with successful staging deployments.
  + Production and staging are typically decoupled entirely from the development environment.
  + Development is typically decoupled entirely from the sandbox environment.
+ Each application has its own set of environments standards.
  + Many applications don't use a sandbox environment.
  + Some applications don't require a staging environment but instead use a blue/green deployment strategy.

Imagine a scenario in which an application repository delivers three environments that use a trunk-based methodology. The development environment is tied to the `develop` branch, staging to the `staging` branch, and production to the `main` branch. For this application, a new feature is required to connect a transit gateway in the solution, which is managed by another team and repository. A developer writes the infrastructure code in a feature branch, and merges it to the `develop` branch when ready. All appears well.

However, a challenge arises. Another developer has a separate user story for a separate feature, writes it in a feature branch, and merges it to the `develop` branch. The second feature is now ready for merge into staging and production. However, the original transit gateway feature isn't ready because of a risk criterion in the organization. Now all features are blocked from promotion to production, and the application code is effectively frozen or broken.

In this scenario, consider the following potential solutions:
+ *Most common solution:* Increase code repetition (reduce [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself)) at targeted code structure locations by setting separate `./environments` folders in the repository. This allows the environments' code to be in the same repository, but decoupled.
+ Set up a CI/CD process with complex variable management.
+ Separate environments into separate repositories.
+ *Least common solution:* Use multiple trunk branches.
