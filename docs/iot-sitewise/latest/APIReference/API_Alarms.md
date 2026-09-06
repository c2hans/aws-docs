---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_Alarms.html
---

# Alarms
<a name="API_Alarms"></a>

Contains the configuration information of an alarm created in an AWS IoT SiteWise Monitor portal. You can use the alarm to monitor an asset property and get notified when the asset property value is outside a specified range. For more information, see [Monitoring with alarms](https://docs.aws.amazon.com/iot-sitewise/latest/appguide/monitor-alarms.html) in the * AWS IoT SiteWise Application Guide*.

## Contents
<a name="API_Alarms_Contents"></a>

 ** alarmRoleArn **   <a name="iotsitewise-Type-Alarms-alarmRoleArn"></a>
The [ARN](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the IAM role that allows the alarm to perform actions and access AWS resources and services, such as AWS IoT Events.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws(-cn|-us-gov)?:[a-zA-Z0-9-:\/_\.\+=,@]+$`
Required: Yes

 ** notificationLambdaArn **   <a name="iotsitewise-Type-Alarms-notificationLambdaArn"></a>
The [ARN](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the Lambda function that manages alarm notifications. For more information, see [Managing alarm notifications](https://docs.aws.amazon.com/iotevents/latest/developerguide/lambda-support.html) in the * AWS IoT Events Developer Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws(-cn|-us-gov)?:[a-zA-Z0-9-:\/_\.]+$`
Required: No

## See Also
<a name="API_Alarms_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/Alarms)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/Alarms)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/Alarms)
