---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_VpcPropertiesPatch.html
---

# VpcPropertiesPatch
<a name="API_VpcPropertiesPatch"></a>

The VPC connection properties used when updating a connection.

## Contents
<a name="API_VpcPropertiesPatch_Contents"></a>

 ** securityGroupId **   <a name="datazone-Type-VpcPropertiesPatch-securityGroupId"></a>
The security group ID of the VPC connection.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 32.
Pattern: `sg-[a-z0-9]+`
Required: No

 ** subnetIds **   <a name="datazone-Type-VpcPropertiesPatch-subnetIds"></a>
The subnet IDs of the VPC connection.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 16 items.
Length Constraints: Minimum length of 0. Maximum length of 32.
Pattern: `subnet-[a-z0-9]+`
Required: No

 ** vpcId **   <a name="datazone-Type-VpcPropertiesPatch-vpcId"></a>
The identifier of the VPC.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 32.
Pattern: `vpc-[a-z0-9]+`
Required: No

## See Also
<a name="API_VpcPropertiesPatch_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/VpcPropertiesPatch)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/VpcPropertiesPatch)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/VpcPropertiesPatch)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
