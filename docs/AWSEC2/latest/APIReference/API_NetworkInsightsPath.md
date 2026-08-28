---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_NetworkInsightsPath.html
---

# NetworkInsightsPath
<a name="API_NetworkInsightsPath"></a>

Describes a path.

## Contents
<a name="API_NetworkInsightsPath_Contents"></a>

 ** createdDate **
The time stamp when the path was created.
Type: Timestamp
Required: No

 ** destination **
The ID of the destination.
Type: String
Required: No

 ** destinationArn **
The Amazon Resource Name (ARN) of the destination.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1283.
Required: No

 ** destinationIp **
The IP address of the destination.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 15.
Pattern: `^([0-9]{1,3}.){3}[0-9]{1,3}$`
Required: No

 ** destinationPort **
The destination port.
Type: Integer
Required: No

 ** filterAtDestination **
Scopes the analysis to network paths that match specific filters at the destination.
Type: [PathFilter](API_PathFilter.md) object
Required: No

 ** filterAtSource **
Scopes the analysis to network paths that match specific filters at the source.
Type: [PathFilter](API_PathFilter.md) object
Required: No

 ** networkInsightsPathArn **
The Amazon Resource Name (ARN) of the path.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1283.
Required: No

 ** networkInsightsPathId **
The ID of the path.
Type: String
Required: No

 ** protocol **
The protocol.
Type: String
Valid Values: `tcp | udp`
Required: No

 ** source **
The ID of the source.
Type: String
Required: No

 ** sourceArn **
The Amazon Resource Name (ARN) of the source.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1283.
Required: No

 ** sourceIp **
The IP address of the source.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 15.
Pattern: `^([0-9]{1,3}.){3}[0-9]{1,3}$`
Required: No

 ** TagSet.N **
The tags associated with the path.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## See Also
<a name="API_NetworkInsightsPath_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/NetworkInsightsPath)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/NetworkInsightsPath)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/NetworkInsightsPath)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
