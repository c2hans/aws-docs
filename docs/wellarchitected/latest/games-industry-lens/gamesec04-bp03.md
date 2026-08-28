---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gamesec04-bp03.html
---

# GAMESEC04-BP03 Implement geographic restrictions to limit unauthorized access
<a name="gamesec04-bp03"></a>

 When a player requests your content, Amazon CloudFront serves the requested content from the nearest edge location, regardless of where the player is located. However, there may be scenarios in which you need to restrict how your content is accessible by users in specific parts of the world. For example, you may have a rolling game deployment strategy that releases content in phases on a country-by-country basis, or you may have to abide by country-specific access controls.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance-26"></a>

 You can use [geographic restrictions](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/georestrictions.html), also known as geo blocking, to block players in specific geographic locations from accessing content that you're distributing through a CloudFront distribution. This feature lets you restrict access to files that are associated with a distribution and restrict access at the country level. Alternatively, you can use a third-party geo-location service to restrict access to a subset of the files that are associated with a distribution or to restrict access at a finer granularity than the country level.

 By using CloudFront geographic restrictions, you can allow your players to only access your content if they're in one of the countries that are on an allow list of approved countries. You can also block your players from accessing your content if they're in one of the countries that are on a deny list of banned countries. If a request is received from a blocked geographic location, CloudFront will return a 403 Forbidden HTTP status code to the player. It is important to note that this works well for non-sensitive content and should not be used as stand-alone protection for PII or sensitive game artifacts.

### Implementation steps
<a name="implementation-steps-26"></a>
+  Use CloudFront geographic restrictions to allow or deny content access based on country-level allow or deny lists.
+  Return a 403 Forbidden HTTP status code for requests originating from blocked geographic locations.
+  Avoid relying solely on geo restrictions for protecting sensitive content or PII

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
