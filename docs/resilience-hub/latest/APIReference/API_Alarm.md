---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_Alarm.html
---

# Alarm
<a name="API_Alarm"></a>

Indicates the Amazon CloudWatch alarm detected while running an assessment.

## Contents
<a name="API_Alarm_Contents"></a>

 ** alarmArn **   <a name="resiliencehub-Type-Alarm-alarmArn"></a>
Amazon Resource Name (ARN) of the Amazon CloudWatch alarm.
Type: String
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: No

 ** source **   <a name="resiliencehub-Type-Alarm-source"></a>
Indicates the source of the Amazon CloudWatch alarm. That is, it indicates if the alarm was created using AWS Resilience Hub recommendation (`AwsResilienceHub`), or if you had created the alarm in Amazon CloudWatch (`Customer`).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

## See Also
<a name="API_Alarm_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehub-2020-04-30/Alarm)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehub-2020-04-30/Alarm)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehub-2020-04-30/Alarm)
