---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_PathFilter.html
---

# PathFilter
<a name="API_PathFilter"></a>

Describes a set of filters for a path analysis. Use path filters to scope the analysis when there can be multiple resulting paths.

## Contents
<a name="API_PathFilter_Contents"></a>

 ** destinationAddress **
The destination IPv4 address.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 15.
Pattern: `^([0-9]{1,3}.){3}[0-9]{1,3}$`
Required: No

 ** destinationPortRange **
The destination port range.
Type: [FilterPortRange](API_FilterPortRange.md) object
Required: No

 ** sourceAddress **
The source IPv4 address.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 15.
Pattern: `^([0-9]{1,3}.){3}[0-9]{1,3}$`
Required: No

 ** sourcePortRange **
The source port range.
Type: [FilterPortRange](API_FilterPortRange.md) object
Required: No

## See Also
<a name="API_PathFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/PathFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/PathFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/PathFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
