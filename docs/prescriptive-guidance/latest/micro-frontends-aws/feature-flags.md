---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/micro-frontends-aws/feature-flags.html
---

# Feature flags
<a name="feature-flags"></a>

You can implement feature flags in micro-frontends to help coordinate testing and releasing features in multiple environments. The feature flag technique centralizes decisions in a Boolean-based store and drives behavior based on those decisions. Teams often use it to propagate changes silently and keep them hidden until a specific time. This approach also unblocks releases of new features that would otherwise slow team velocity.

Consider the example of teams working on a micro-frontend feature that they will launch on a specific date. The feature is ready, but it needs to be released together with a change on another micro-frontend that is released independently. Blocking the release of both micro-frontends is an anti-pattern and increases deployment risk.

Instead, the teams can create a Boolean feature flag in a database that they both consume during render time (perhaps through an HTTP call to a shared Feature Flags API). The teams can even release the change in a test environment where the Boolean value is set to `True` to verify cross-project functional and nonfunctional requirements before launching to production.

Another example of feature flag use is implementing a mechanism to override the value of a flag by setting a specific value through the `QueryString` parameter or storing a particular test string in a cookie. Product owners can iterate on features without blocking the release of other features or bug fixes until the launch date. On the given date, changing the flag value in the database makes the change visible in production, without the need for cross-team coordinated releases. After a feature is released, the development teams clean up the code to remove the old behavior.

Other use cases include releasing a context-based feature flag system. For example, if a single website serves customers in multiple languages, a feature might be available only for visitors of a particular country. The feature flag system can be dependent on the consumer sending the country context (for example by making use of the `Accept-Language` HTTP header), and there can be a different behavior depending on that context.

While feature flags are a powerful tool for facilitating collaboration between developers and product owners, they rely on people's diligence to avoid a significant degradation of the code base. Keeping flags active on multiple features can increase complexity when troubleshooting issues, increase JavaScript bundle size, and ultimately accumulate technical debt. Common mitigation activities include the following:
+ Unit testing each feature behind a flag to reduce the probability of bugs, which can introduce longer feedback loops in the automated CI/CD pipelines that run the tests
+ Creating tools to measure bundle size increases during code changes, which can be mitigated during code reviews

AWS offers a range of solutions for optimizing A/B testing on the edge by using Amazon CloudFront functions or Lambda@Edge. These approaches help reduce the complexity of integrating a new solution, or an existing third-party product, to validate your hypotheses. For more information, see [A/B testing](https://aws.amazon.com/developer/application-security-performance/articles/a-b-testing/).
