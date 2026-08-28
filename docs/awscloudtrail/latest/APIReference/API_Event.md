---
source_url: https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_Event.html
---

# Event
<a name="API_Event"></a>

Contains information about an event that was returned by a lookup request. The result includes a representation of a CloudTrail event.

## Contents
<a name="API_Event_Contents"></a>

 ** AccessKeyId **   <a name="awscloudtrail-Type-Event-AccessKeyId"></a>
The AWS access key ID that was used to sign the request. If the request was made with temporary security credentials, this is the access key ID of the temporary credentials.
Type: String
Required: No

 ** CloudTrailEvent **   <a name="awscloudtrail-Type-Event-CloudTrailEvent"></a>
A JSON string that contains a representation of the event returned.
Type: String
Required: No

 ** EventId **   <a name="awscloudtrail-Type-Event-EventId"></a>
The CloudTrail ID of the event returned.
Type: String
Required: No

 ** EventName **   <a name="awscloudtrail-Type-Event-EventName"></a>
The name of the event returned.
Type: String
Required: No

 ** EventSource **   <a name="awscloudtrail-Type-Event-EventSource"></a>
The AWS service to which the request was made.
Type: String
Required: No

 ** EventTime **   <a name="awscloudtrail-Type-Event-EventTime"></a>
The date and time of the event returned.
Type: Timestamp
Required: No

 ** ReadOnly **   <a name="awscloudtrail-Type-Event-ReadOnly"></a>
Information about whether the event is a write event or a read event.
Type: String
Required: No

 ** Resources **   <a name="awscloudtrail-Type-Event-Resources"></a>
A list of resources referenced by the event returned.
Type: Array of [Resource](API_Resource.md) objects
Required: No

 ** Username **   <a name="awscloudtrail-Type-Event-Username"></a>
A user name or role name of the requester that called the API in the event returned.
Type: String
Required: No

## See Also
<a name="API_Event_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/Event)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/Event)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/Event)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudTrail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query awscloudtrail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
