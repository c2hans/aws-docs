---
source_url: https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_ApplicationInfo.html
---

# ApplicationInfo
<a name="API_ApplicationInfo"></a>

Describes the status of the application.

## Contents
<a name="API_ApplicationInfo_Contents"></a>

 ** AccountId **   <a name="appinsights-Type-ApplicationInfo-AccountId"></a>
The AWS account ID for the owner of the application.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `^\d{12}$`
Required: No

 ** AttachMissingPermission **   <a name="appinsights-Type-ApplicationInfo-AttachMissingPermission"></a>
If set to true, the managed policies for SSM and CW will be attached to the instance roles if they are missing.
Type: Boolean
Required: No

 ** AutoConfigEnabled **   <a name="appinsights-Type-ApplicationInfo-AutoConfigEnabled"></a>
 Indicates whether auto-configuration is turned on for this application.
Type: Boolean
Required: No

 ** CWEMonitorEnabled **   <a name="appinsights-Type-ApplicationInfo-CWEMonitorEnabled"></a>
 Indicates whether Application Insights can listen to CloudWatch events for the application resources, such as `instance terminated`, `failed deployment`, and others.
Type: Boolean
Required: No

 ** DiscoveryType **   <a name="appinsights-Type-ApplicationInfo-DiscoveryType"></a>
 The method used by Application Insights to onboard your resources.
Type: String
Valid Values: `RESOURCE_GROUP_BASED | ACCOUNT_BASED`
Required: No

 ** LifeCycle **   <a name="appinsights-Type-ApplicationInfo-LifeCycle"></a>
The lifecycle of the application.
Type: String
Required: No

 ** OpsCenterEnabled **   <a name="appinsights-Type-ApplicationInfo-OpsCenterEnabled"></a>
 Indicates whether Application Insights will create opsItems for any problem detected by Application Insights for an application.
Type: Boolean
Required: No

 ** OpsItemSNSTopicArn **   <a name="appinsights-Type-ApplicationInfo-OpsItemSNSTopicArn"></a>
 The SNS topic provided to Application Insights that is associated to the created opsItems to receive SNS notifications for opsItem updates.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 300.
Pattern: `^arn:aws(-\w+)*:[\w\d-]+:([\w\d-]*)?:[\w\d_-]*([:/].+)*$`
Required: No

 ** Remarks **   <a name="appinsights-Type-ApplicationInfo-Remarks"></a>
The issues on the user side that block Application Insights from successfully monitoring an application. Example remarks include:
+ “Configuring application, detected 1 Errors, 3 Warnings”
+ “Configuring application, detected 1 Unconfigured Components”
Type: String
Required: No

 ** ResourceGroupName **   <a name="appinsights-Type-ApplicationInfo-ResourceGroupName"></a>
The name of the resource group used for the application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9\.\-_]*`
Required: No

 ** SNSNotificationArn **   <a name="appinsights-Type-ApplicationInfo-SNSNotificationArn"></a>
 The SNS topic ARN that is associated with SNS notifications for updates or issues.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 300.
Pattern: `^arn:aws(-\w+)*:[\w\d-]+:([\w\d-]*)?:[\w\d_-]*([:/].+)*$`
Required: No

## See Also
<a name="API_ApplicationInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-insights-2018-11-25/ApplicationInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-insights-2018-11-25/ApplicationInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-insights-2018-11-25/ApplicationInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Application Insights. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudwatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
