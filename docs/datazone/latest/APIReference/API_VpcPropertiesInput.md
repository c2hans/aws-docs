---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_VpcPropertiesInput.html
---

# VpcPropertiesInput
<a name="API_VpcPropertiesInput"></a>

The VPC connection properties used when creating a connection.

## Contents
<a name="API_VpcPropertiesInput_Contents"></a>

 ** subnetIds **   <a name="datazone-Type-VpcPropertiesInput-subnetIds"></a>
The subnet IDs of the VPC connection. You can specify between 1 and 16 subnet IDs.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 16 items.
Length Constraints: Minimum length of 0. Maximum length of 32.
Pattern: `subnet-[a-z0-9]+`
Required: Yes

 ** vpcId **   <a name="datazone-Type-VpcPropertiesInput-vpcId"></a>
The identifier of the VPC. Must match the pattern `^vpc-[a-z0-9]+$`. Maximum length of 32.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 32.
Pattern: `vpc-[a-z0-9]+`
Required: Yes

 ** securityGroupId **   <a name="datazone-Type-VpcPropertiesInput-securityGroupId"></a>
The security group ID of the VPC connection. Must match the pattern `^sg-[a-z0-9]+$`. Maximum length of 32.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 32.
Pattern: `sg-[a-z0-9]+`
Required: No

## See Also
<a name="API_VpcPropertiesInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/VpcPropertiesInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/VpcPropertiesInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/VpcPropertiesInput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
