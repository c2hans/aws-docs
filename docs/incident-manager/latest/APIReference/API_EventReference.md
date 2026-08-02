---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_EventReference.html
---

# EventReference
<a name="API_EventReference"></a>

An item referenced in a `TimelineEvent` that is involved in or somehow associated with an incident. You can specify an Amazon Resource Name (ARN) for an AWS resource or a `RelatedItem` ID.

## Contents
<a name="API_EventReference_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** relatedItemId **   <a name="IncidentManager-Type-EventReference-relatedItemId"></a>
The ID of a `RelatedItem` referenced in a `TimelineEvent`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 200.
Pattern: `related-item/(ANALYSIS|INCIDENT|METRIC|PARENT|ATTACHMENT|OTHER|AUTOMATION|INVOLVED_RESOURCE|TASK)/([0-9]|[A-F]){32}`
Required: No

 ** resource **   <a name="IncidentManager-Type-EventReference-resource"></a>
The Amazon Resource Name (ARN) of an AWS resource referenced in a `TimelineEvent`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Pattern: `arn:aws(-cn|-us-gov)?:[a-z0-9-]*:[a-z0-9-]*:([0-9]{12})?:.+`
Required: No

## See Also
<a name="API_EventReference_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-incidents-2018-05-10/EventReference)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-incidents-2018-05-10/EventReference)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-incidents-2018-05-10/EventReference)
