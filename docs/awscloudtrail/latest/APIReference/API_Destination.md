---
source_url: https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_Destination.html
---

# Destination
<a name="API_Destination"></a>

Contains information about the destination receiving events.

## Contents
<a name="API_Destination_Contents"></a>

 ** Location **   <a name="awscloudtrail-Type-Destination-Location"></a>
 For channels used for a CloudTrail Lake integration, the location is the ARN of an event data store that receives events from a channel. For service-linked channels, the location is the name of the AWS service.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 1024.
Pattern: `^[a-zA-Z0-9._/\-:*]+$`
Required: Yes

 ** Type **   <a name="awscloudtrail-Type-Destination-Type"></a>
The type of destination for events arriving from a channel. For channels used for a CloudTrail Lake integration, the value is `EVENT_DATA_STORE`. For service-linked channels, the value is `AWS_SERVICE`.
Type: String
Valid Values: `EVENT_DATA_STORE | AWS_SERVICE`
Required: Yes

## See Also
<a name="API_Destination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/Destination)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/Destination)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/Destination)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudTrail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query awscloudtrail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
