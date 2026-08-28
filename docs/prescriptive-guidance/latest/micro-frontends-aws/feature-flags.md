---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/micro-frontends-aws/feature-flags.html
---

# Feature flags
<a name="feature-flags"></a>

Feature flags can be implemented in micro-frontends to facilitate the coordination of testing and releasing features in multiple environments. The feature flag technique consists of centralizing decisions in a Boolean-based store, and driving behavior based on that. It's often used to silently propagate changes that can be kept hidden until a specific moment in time, while unlocking new releases for new features that would otherwise be blocked, reducing team velocity.

Consider the example of teams working on a micro-frontend feature that will be launched on a specific date. The feature is ready, but it needs to be released together with a change on another micro-frontend that is independently released. Blocking the release of both micro-frontends would be considered an anti-pattern and would increase risk when deployed.

Instead, the teams can create a Boolean feature flag in a database that they both consume during render time (perhaps through an HTTP call to a shared Feature Flags API). The teams can even release the change in a test environment where the Boolean value is set to `True` to verify cross-project functional and nonfunctional requirements before launching to production.

Another example of feature flag use is implementing a mechanism to override the value of a flag by setting a specific value through the `QueryString` parameter or storing a particular test string in a cookie. Product owners can iterate on features without blocking the release of other features or bug fixes until launch date. On the given date, changing the flag value on the database instantly makes the change visible in production, without the need for cross-team coordinated releases. After a feature is released, the development teams clean up the code to remove the old behavior.

Other use cases include releasing a context-based feature flag system. For example, if a single website serves customers in multiple languages, a feature might be available only for visitors of a particular country. The feature flag system can be dependent on the consumer sending the country context (for example by making use of the `Accept-Language` HTTP header), and there can be a different behavior depending on that context.

While feature flags are a powerful tool for facilitating collaboration between developers and product owners, they rely on people's diligence to avoid a significant degradation of the code base. Keeping flags active on multiple features can increase complexity when troubleshooting issues, increase JavaScript bundle size, and ultimately accumulate technical debt. Common mitigation activities include the following:
+ Unit testing each feature behind a flag to reduce the probability of bugs, which can introduce longer feedback loops in the automated CI/CD pipelines that run the tests
+ Creating tools to measure bundle size increases during code changes, which can be mitigated during code reviews

AWS offers a range of solutions for optimizing A/B testing on the edge by using Amazon CloudFront functions or Lambda@Edge. These approaches help to reduce the complexity of integrating a solution or the existing SaaS product that you are using to assert your assumptions. For more information, see [A/B testing](https://aws.amazon.com/developer/application-security-performance/articles/a-b-testing/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
