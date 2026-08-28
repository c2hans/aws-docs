---
source_url: https://docs.aws.amazon.com/mediatailor/latest/ug/variables-domains.html
---

# MediaTailor domain variables for multiple content sources
<a name="variables-domains"></a>

AWS Elemental MediaTailor dynamic domain variables allow you to use multiple domains, such as the **my-ads-server.com** part of the URL http://my-ads-server.com, with the player parameters in your configuration. This makes it possible for you to use more than one content source or ad decision server (ADS) in a single configuration.

 You can use domain variables with any parameter that contains a URI:
+ `AdDecisionServerUrl`
+ `AdSegmentUrlPrefix`
+ `ContentSegmentUrlPrefix`
+ `LivePreroll.AdDecisionServerUrl`
+ `VideoContentSourceUrl`

 Domain variables are used alongside *configuration aliases* to perform dynamic variable replacement. Configuration aliases map a set of aliases and values to the player parameters that are used for dynamic domain configuration. For setup procedures, see [Creating and using configuration aliases with MediaTailor](creating-configuration-aliases.md). For detailed reference information, see [MediaTailor configuration aliases overview](configuration-aliases-overview.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaTailor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediatailor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
