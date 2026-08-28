---
source_url: https://docs.aws.amazon.com/drs/latest/APIReference/API_SourceNetwork.html
---

# SourceNetwork
<a name="API_SourceNetwork"></a>

The ARN of the Source Network.

## Contents
<a name="API_SourceNetwork_Contents"></a>

 ** arn **   <a name="drs-Type-SourceNetwork-arn"></a>
The ARN of the Source Network.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:.{16,2044}`
Required: No

 ** cfnStackName **   <a name="drs-Type-SourceNetwork-cfnStackName"></a>
CloudFormation stack name that was deployed for recovering the Source Network.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z][-a-zA-Z0-9]*`
Required: No

 ** lastRecovery **   <a name="drs-Type-SourceNetwork-lastRecovery"></a>
An object containing information regarding the last recovery of the Source Network.
Type: [RecoveryLifeCycle](API_RecoveryLifeCycle.md) object
Required: No

 ** launchedVpcID **   <a name="drs-Type-SourceNetwork-launchedVpcID"></a>
ID of the recovered VPC following Source Network recovery.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 21.
Pattern: `vpc-[0-9a-fA-F]{8,}`
Required: No

 ** replicationStatus **   <a name="drs-Type-SourceNetwork-replicationStatus"></a>
Status of Source Network Replication. Possible values: (a) STOPPED - Source Network is not replicating. (b) IN\_PROGRESS - Source Network is being replicated. (c) PROTECTED - Source Network was replicated successfully and is being synchronized for changes. (d) ERROR - Source Network replication has failed
Type: String
Valid Values: `STOPPED | IN_PROGRESS | PROTECTED | ERROR`
Required: No

 ** replicationStatusDetails **   <a name="drs-Type-SourceNetwork-replicationStatusDetails"></a>
Error details in case Source Network replication status is ERROR.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** sourceAccountID **   <a name="drs-Type-SourceNetwork-sourceAccountID"></a>
Account ID containing the VPC protected by the Source Network.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `.*[0-9]{12,}.*`
Required: No

 ** sourceNetworkID **   <a name="drs-Type-SourceNetwork-sourceNetworkID"></a>
Source Network ID.
Type: String
Length Constraints: Fixed length of 20.
Pattern: `sn-[0-9a-zA-Z]{17}`
Required: No

 ** sourceRegion **   <a name="drs-Type-SourceNetwork-sourceRegion"></a>
Region containing the VPC protected by the Source Network.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `(us(-gov)?|ap|ca|cn|eu|eusc|sa|af|me|mx|il)-([a-z]{2}-)?(central|north|(north(?:east|west))|south|south(?:east|west)|east|west)-[0-9]`
Required: No

 ** sourceVpcID **   <a name="drs-Type-SourceNetwork-sourceVpcID"></a>
VPC ID protected by the Source Network.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 21.
Pattern: `vpc-[0-9a-fA-F]{8,}`
Required: No

 ** tags **   <a name="drs-Type-SourceNetwork-tags"></a>
A list of tags associated with the Source Network.
Type: String to string map
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## See Also
<a name="API_SourceNetwork_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/drs-2020-02-26/SourceNetwork)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/drs-2020-02-26/SourceNetwork)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/drs-2020-02-26/SourceNetwork)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Disaster Recovery. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query drs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
