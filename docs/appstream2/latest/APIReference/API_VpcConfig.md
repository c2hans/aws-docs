---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_VpcConfig.html
---

# VpcConfig
<a name="API_VpcConfig"></a>

Describes VPC configuration information for fleets and image builders.

## Contents
<a name="API_VpcConfig_Contents"></a>

 ** SecurityGroupIds **   <a name="WorkSpacesApplications-Type-VpcConfig-SecurityGroupIds"></a>
The identifiers of the security groups for the fleet or image builder.
Type: Array of strings
Array Members: Maximum number of 5 items.
Length Constraints: Minimum length of 1.
Required: No

 ** SubnetIds **   <a name="WorkSpacesApplications-Type-VpcConfig-SubnetIds"></a>
The identifiers of the subnets to which a network interface is attached from the fleet instance or image builder instance. Fleet instances use one or more subnets. Image builder instances use one subnet.
Type: Array of strings
Length Constraints: Minimum length of 1.
Required: No

## See Also
<a name="API_VpcConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/VpcConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/VpcConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/VpcConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
