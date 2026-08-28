---
source_url: https://docs.aws.amazon.com/drs/latest/APIReference/API_SourceNetworkData.html
---

# SourceNetworkData
<a name="API_SourceNetworkData"></a>

Properties of Source Network related to a job event.

## Contents
<a name="API_SourceNetworkData_Contents"></a>

 ** sourceNetworkID **   <a name="drs-Type-SourceNetworkData-sourceNetworkID"></a>
Source Network ID.
Type: String
Length Constraints: Fixed length of 20.
Pattern: `sn-[0-9a-zA-Z]{17}`
Required: No

 ** sourceVpc **   <a name="drs-Type-SourceNetworkData-sourceVpc"></a>
VPC ID protected by the Source Network.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 21.
Pattern: `vpc-[0-9a-fA-F]{8,}`
Required: No

 ** stackName **   <a name="drs-Type-SourceNetworkData-stackName"></a>
CloudFormation stack name that was deployed for recovering the Source Network.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 65536.
Required: No

 ** targetVpc **   <a name="drs-Type-SourceNetworkData-targetVpc"></a>
ID of the recovered VPC following Source Network recovery.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 21.
Pattern: `vpc-[0-9a-fA-F]{8,}`
Required: No

## See Also
<a name="API_SourceNetworkData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/drs-2020-02-26/SourceNetworkData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/drs-2020-02-26/SourceNetworkData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/drs-2020-02-26/SourceNetworkData)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Disaster Recovery. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query drs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
