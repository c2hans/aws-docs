---
source_url: https://docs.aws.amazon.com/whitepapers/latest/device-manufacturing-provisioning/conclusion.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Conclusion
<a name="conclusion"></a>

 Moving an IoT project from proof of concept to a large-scale deployment is a complex challenge. Device makers and service operators must make multiple decisions that fundamentally impact the device’s capabilities, level of security, bill of materials, and product and operational cost. Production and deployment decisions must be considered early on in the development process because they will impact manufacturing and deployment costs.

 Device makers must consider the following when creating IoT devices:
+  Who will maintain the public key infrastructure for their project?
+  What capabilities should they build into their device?
+  What capabilities do their contract manufacturer have to provide customization at manufacturing times?

   Service operators must also consider similar questions when considering which devices to use:
+  How are devices trusted to connect to the service platform?
+  How and when will devices onboard to the service platform from a manufacturer?
+  Will the IoT service require multi-Region or multi-account device deployments?

 This whitepaper has outlined the options that AWS IoT provides for device makers and service operators as they answer these questions. No matter the capabilities of the device and manufacturing process, the level of trust in the manufacturing supply chain or security requirements, AWS IoT provides options to onboard and trust devices at scale in a secure way.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
