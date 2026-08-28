---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_ContainerAttribute.html
---

# ContainerAttribute
<a name="API_ContainerAttribute"></a>

A unique identifier for a container in a container fleet compute.

 **Returned by:** [DescribeCompute](https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeCompute.html)

## Contents
<a name="API_ContainerAttribute_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ContainerName **   <a name="gameliftservers-Type-ContainerAttribute-ContainerName"></a>
The identifier for a container that's running in a compute.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[a-zA-Z0-9\-]+$`
Required: No

 ** ContainerRuntimeId **   <a name="gameliftservers-Type-ContainerAttribute-ContainerRuntimeId"></a>
The runtime ID for the container that's running in a compute. This value is unique within the compute.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## See Also
<a name="API_ContainerAttribute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/ContainerAttribute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/ContainerAttribute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/ContainerAttribute)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
