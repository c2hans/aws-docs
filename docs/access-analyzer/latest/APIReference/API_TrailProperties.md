---
source_url: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_TrailProperties.html
---

# TrailProperties
<a name="API_TrailProperties"></a>

Contains details about the CloudTrail trail being analyzed to generate a policy.

## Contents
<a name="API_TrailProperties_Contents"></a>

 ** cloudTrailArn **   <a name="accessanalyzer-Type-TrailProperties-cloudTrailArn"></a>
Specifies the ARN of the trail. The format of a trail ARN is `arn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail`.
Type: String
Pattern: `arn:[^:]*:cloudtrail:[^:]*:[^:]*:trail/.{1,576}`
Required: Yes

 ** allRegions **   <a name="accessanalyzer-Type-TrailProperties-allRegions"></a>
Possible values are `true` or `false`. If set to `true`, IAM Access Analyzer retrieves CloudTrail data from all regions to analyze and generate a policy.
Type: Boolean
Required: No

 ** regions **   <a name="accessanalyzer-Type-TrailProperties-regions"></a>
A list of regions to get CloudTrail data from and analyze to generate a policy.
Type: Array of strings
Required: No

## See Also
<a name="API_TrailProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/TrailProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/TrailProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/TrailProperties)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IAM Access Analyzer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query access-analyzer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
