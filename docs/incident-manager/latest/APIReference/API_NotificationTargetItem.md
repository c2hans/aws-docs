---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_NotificationTargetItem.html
---

# NotificationTargetItem
<a name="API_NotificationTargetItem"></a>

The SNS targets that are notified when updates are made to an incident.

## Contents
<a name="API_NotificationTargetItem_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** snsTopicArn **   <a name="IncidentManager-Type-NotificationTargetItem-snsTopicArn"></a>
The Amazon Resource Name (ARN) of the SNS topic.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Pattern: `arn:aws(-cn|-us-gov)?:[a-z0-9-]*:[a-z0-9-]*:([0-9]{12})?:.+`
Required: No

## See Also
<a name="API_NotificationTargetItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-incidents-2018-05-10/NotificationTargetItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-incidents-2018-05-10/NotificationTargetItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-incidents-2018-05-10/NotificationTargetItem)
