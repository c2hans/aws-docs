---
source_url: https://docs.aws.amazon.com/notifications/latest/APIReference/API_ManagedSourceEventMetadataSummary.html
---

# ManagedSourceEventMetadataSummary
<a name="API_ManagedSourceEventMetadataSummary"></a>

A short summary and metadata for a managed notification event.

## Contents
<a name="API_ManagedSourceEventMetadataSummary_Contents"></a>

 ** eventType **   <a name="Notifications-Type-ManagedSourceEventMetadataSummary-eventType"></a>
The event Type of the notification.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `([a-zA-Z0-9 \-\(\)])+`
Required: Yes

 ** source **   <a name="Notifications-Type-ManagedSourceEventMetadataSummary-source"></a>
The source service of the notification.
Must match one of the valid EventBridge sources. Only AWS service sourced events are supported. For example, `aws.ec2` and `aws.cloudwatch`. For more information, see [Event delivery from AWS services](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event.html#eb-service-event-delivery-level) in the *Amazon EventBridge User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Pattern: `aws.([a-z0-9\-])+`
Required: Yes

 ** eventOriginRegion **   <a name="Notifications-Type-ManagedSourceEventMetadataSummary-eventOriginRegion"></a>
The Region where the notification originated.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 32.
Pattern: `([a-z]{1,4})-([a-z]{1,15}-)+([0-9])`
Required: No

## See Also
<a name="API_ManagedSourceEventMetadataSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/notifications-2018-05-10/ManagedSourceEventMetadataSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/notifications-2018-05-10/ManagedSourceEventMetadataSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/notifications-2018-05-10/ManagedSourceEventMetadataSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS User Notifications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query notifications` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
