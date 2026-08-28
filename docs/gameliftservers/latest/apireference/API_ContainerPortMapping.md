---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_ContainerPortMapping.html
---

# ContainerPortMapping
<a name="API_ContainerPortMapping"></a>

Describes a mapping between a container port and a connection port on a fleet instance. You define container ports in a container group definition. Amazon GameLift Servers assigns connection ports when it deploys the container group to an instance.

 **Part of:** [ContainerGroupPortMapping](https://docs.aws.amazon.com/gamelift/latest/apireference/API_ContainerGroupPortMapping.html)

## Contents
<a name="API_ContainerPortMapping_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ConnectionPort **   <a name="gameliftservers-Type-ContainerPortMapping-ConnectionPort"></a>
The port number on the fleet instance that maps to the container port. Connection ports are assigned by Amazon GameLift Servers when the container group is deployed to an instance.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 60000.
Required: No

 ** ContainerPort **   <a name="gameliftservers-Type-ContainerPortMapping-ContainerPort"></a>
The port number on the container. This port is defined in the container group definition. Container port numbers must be unique within a container group definition.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 60000.
Required: No

 ** Protocol **   <a name="gameliftservers-Type-ContainerPortMapping-Protocol"></a>
The network protocol for the port mapping. Valid values are `TCP` or `UDP`.
Type: String
Valid Values: `TCP | UDP`
Required: No

## See Also
<a name="API_ContainerPortMapping_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/ContainerPortMapping)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/ContainerPortMapping)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/ContainerPortMapping)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
