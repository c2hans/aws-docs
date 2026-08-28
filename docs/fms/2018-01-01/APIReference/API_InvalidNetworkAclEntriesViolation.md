---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_InvalidNetworkAclEntriesViolation.html
---

# InvalidNetworkAclEntriesViolation
<a name="API_InvalidNetworkAclEntriesViolation"></a>

Violation detail for the entries in a network ACL resource.

## Contents
<a name="API_InvalidNetworkAclEntriesViolation_Contents"></a>

 ** CurrentAssociatedNetworkAcl **   <a name="fms-Type-InvalidNetworkAclEntriesViolation-CurrentAssociatedNetworkAcl"></a>
The network ACL containing the entry violations.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

 ** EntryViolations **   <a name="fms-Type-InvalidNetworkAclEntriesViolation-EntryViolations"></a>
Detailed information about the entry violations in the network ACL.
Type: Array of [EntryViolation](API_EntryViolation.md) objects
Required: No

 ** Subnet **   <a name="fms-Type-InvalidNetworkAclEntriesViolation-Subnet"></a>
The subnet that's associated with the network ACL.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

 ** SubnetAvailabilityZone **   <a name="fms-Type-InvalidNetworkAclEntriesViolation-SubnetAvailabilityZone"></a>
The Availability Zone where the network ACL is in use.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** Vpc **   <a name="fms-Type-InvalidNetworkAclEntriesViolation-Vpc"></a>
The VPC where the violation was found.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

## See Also
<a name="API_InvalidNetworkAclEntriesViolation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/InvalidNetworkAclEntriesViolation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/InvalidNetworkAclEntriesViolation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/InvalidNetworkAclEntriesViolation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for 1.0. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
