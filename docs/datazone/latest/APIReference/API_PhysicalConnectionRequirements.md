---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_PhysicalConnectionRequirements.html
---

# PhysicalConnectionRequirements
<a name="API_PhysicalConnectionRequirements"></a>

Physical connection requirements of a connection.

## Contents
<a name="API_PhysicalConnectionRequirements_Contents"></a>

 ** availabilityZone **   <a name="datazone-Type-PhysicalConnectionRequirements-availabilityZone"></a>
The availability zone of the physical connection requirements of a connection.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** securityGroupIdList **   <a name="datazone-Type-PhysicalConnectionRequirements-securityGroupIdList"></a>
The group ID list of the physical connection requirements of a connection.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** subnetId **   <a name="datazone-Type-PhysicalConnectionRequirements-subnetId"></a>
The subnet ID of the physical connection requirements of a connection.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 32.
Pattern: `subnet-[a-z0-9]+`
Required: No

 ** subnetIdList **   <a name="datazone-Type-PhysicalConnectionRequirements-subnetIdList"></a>
The subnet ID list of the physical connection requirements of a connection.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Length Constraints: Minimum length of 0. Maximum length of 32.
Pattern: `subnet-[a-z0-9]+`
Required: No

## See Also
<a name="API_PhysicalConnectionRequirements_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/PhysicalConnectionRequirements)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/PhysicalConnectionRequirements)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/PhysicalConnectionRequirements)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
