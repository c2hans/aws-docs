---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/dss-choose-service.html
---

# Choosing among the AWS media services
<a name="dss-choose-service"></a>

If your preferred downstream system is another AWS media service, following are some useful tips for choosing the service to use:
+ If you need to choose between AWS Elemental MediaPackage or AWS Elemental MediaStore for HLS outputs, follow these guidelines:
  + Decide if you want to protect your content with a digital rights management (DRM) solution. DRM prevents unauthorized people from accessing the content.
  + Decide if you want to insert ads in your content.

  If you want either or both of these features, you should choose MediaPackage as the origin service because you will need to repackage the output.

  If you do not want any of these features, you could choose MediaPackage or AWS Elemental MediaStore. AWS Elemental MediaStore is generally a simpler solution as an origin service, but it lacks the repackaging features of MediaPackage.
+ If you have identified AWS Elemental MediaPackage as an origin service, see [Delivering to MediaPackage](delivering-to-mediapackage.md) for guidance on choosing the correct output group configuration.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
