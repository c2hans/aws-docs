---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_HostEntry.html
---

# HostEntry
<a name="API_HostEntry"></a>

Hostnames and IP address entries that are added to the `/etc/hosts` file of a container via the `extraHosts` parameter of its [ContainerDefinition](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ContainerDefinition.html).

## Contents
<a name="API_HostEntry_Contents"></a>

 ** hostname **   <a name="ECS-Type-HostEntry-hostname"></a>
The hostname to use in the `/etc/hosts` entry.
Type: String
Required: Yes

 ** ipAddress **   <a name="ECS-Type-HostEntry-ipAddress"></a>
The IP address to use in the `/etc/hosts` entry.
Type: String
Required: Yes

## See Also
<a name="API_HostEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/HostEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/HostEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/HostEntry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic Container Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
