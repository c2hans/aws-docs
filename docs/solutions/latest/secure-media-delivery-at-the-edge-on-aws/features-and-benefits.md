---
source_url: https://docs.aws.amazon.com/solutions/latest/secure-media-delivery-at-the-edge-on-aws/features-and-benefits.html
---

# Features and benefits
<a name="features-and-benefits"></a>

 The solution provides the following features:

 **Ease of integration**

 Easily integrate this solution into your existing workflows or add to new ones in a few configuration steps. Implemented as an incremental component, the solution is ready to use without redesigning the CloudFront architecture.

 **Live and on demand workloads**

 The solution supports Live streaming and Video on Demand (VOD) workloads.

 **Widespread support across video clients**

 With a wide range of devices and streaming formats, the solution is designed to provide the best possible support coverage. The URL-based token works universally with the clients you use today, and the ones you might need to support tomorrow.

 **Flexible token structure**

 Presenting secure tokens in the widely-adopted JSON Web Token (JWT) format offers flexibility in construction. Combine multiple viewer attributes and geolocation details provided by CloudFront to restrict playback to only authorized clients. Viewer attributes are not exposed in the token or URL path, ensuring the privacy of your end-users.

 **Session revocation**

 Quickly identify playback sessions with irregular traffic patterns suggesting unauthorized distribution of your content. Block playback sessions by reporting corresponding session identifiers, or leverage the automatic workflow offered by the solution to detect and block suspicious sessions.

 **Scale and automation**

 The solution seamlessly scales to the highest traffic events via CloudFront Functions. You can depend on the automated workflows implemented by the solution to handle regular key rotation, and process traffic patterns to detect and block sessions with suspicious traffic patterns.

 **Integration with Service Catalog AppRegistry and Application Manager, a capability of AWS Systems Manager**

 This solution includes a [Service Catalog AppRegistry](https://docs.aws.amazon.com/servicecatalog/latest/arguide/intro-app-registry.html) resource to register the solution’s CloudFormation template and its underlying resources as an application in both Service Catalog AppRegistry and [Application Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/application-manager.html). With this integration, you can centrally manage the solution’s resources and enable application search, reporting, and management actions.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Secure Media Delivery at the Edge on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
