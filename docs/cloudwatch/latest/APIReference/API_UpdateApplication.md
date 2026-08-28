---
source_url: https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_UpdateApplication.html
---

# UpdateApplication
<a name="API_UpdateApplication"></a>

Updates the application.

## Request Syntax
<a name="API_UpdateApplication_RequestSyntax"></a>

```
{
   "AttachMissingPermission": {{boolean}},
   "AutoConfigEnabled": {{boolean}},
   "CWEMonitorEnabled": {{boolean}},
   "OpsCenterEnabled": {{boolean}},
   "OpsItemSNSTopicArn": "{{string}}",
   "RemoveSNSTopic": {{boolean}},
   "ResourceGroupName": "{{string}}",
   "SNSNotificationArn": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateApplication_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AttachMissingPermission](#API_UpdateApplication_RequestSyntax) **   <a name="appinsights-UpdateApplication-request-AttachMissingPermission"></a>
If set to true, the managed policies for SSM and CW will be attached to the instance roles if they are missing.
Type: Boolean
Required: No

 ** [AutoConfigEnabled](#API_UpdateApplication_RequestSyntax) **   <a name="appinsights-UpdateApplication-request-AutoConfigEnabled"></a>
 Turns auto-configuration on or off.
Type: Boolean
Required: No

 ** [CWEMonitorEnabled](#API_UpdateApplication_RequestSyntax) **   <a name="appinsights-UpdateApplication-request-CWEMonitorEnabled"></a>
 Indicates whether Application Insights can listen to CloudWatch events for the application resources, such as `instance terminated`, `failed deployment`, and others.
Type: Boolean
Required: No

 ** [OpsCenterEnabled](#API_UpdateApplication_RequestSyntax) **   <a name="appinsights-UpdateApplication-request-OpsCenterEnabled"></a>
 When set to `true`, creates opsItems for any problems detected on an application.
Type: Boolean
Required: No

 ** [OpsItemSNSTopicArn](#API_UpdateApplication_RequestSyntax) **   <a name="appinsights-UpdateApplication-request-OpsItemSNSTopicArn"></a>
 The SNS topic provided to Application Insights that is associated to the created opsItem. Allows you to receive notifications for updates to the opsItem.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 300.
Pattern: `^arn:aws(-\w+)*:[\w\d-]+:([\w\d-]*)?:[\w\d_-]*([:/].+)*$`
Required: No

 ** [RemoveSNSTopic](#API_UpdateApplication_RequestSyntax) **   <a name="appinsights-UpdateApplication-request-RemoveSNSTopic"></a>
 Disassociates the SNS topic from the opsItem created for detected problems.
Type: Boolean
Required: No

 ** [ResourceGroupName](#API_UpdateApplication_RequestSyntax) **   <a name="appinsights-UpdateApplication-request-ResourceGroupName"></a>
The name of the resource group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9\.\-_]*`
Required: Yes

 ** [SNSNotificationArn](#API_UpdateApplication_RequestSyntax) **   <a name="appinsights-UpdateApplication-request-SNSNotificationArn"></a>
 The SNS topic ARN. Allows you to receive SNS notifications for updates and issues with an application.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 300.
Pattern: `^arn:aws(-\w+)*:[\w\d-]+:([\w\d-]*)?:[\w\d_-]*([:/].+)*$`
Required: No

## Response Syntax
<a name="API_UpdateApplication_ResponseSyntax"></a>

```
{
   "ApplicationInfo": {
      "AccountId": "string",
      "AttachMissingPermission": boolean,
      "AutoConfigEnabled": boolean,
      "CWEMonitorEnabled": boolean,
      "DiscoveryType": "string",
      "LifeCycle": "string",
      "OpsCenterEnabled": boolean,
      "OpsItemSNSTopicArn": "string",
      "Remarks": "string",
      "ResourceGroupName": "string",
      "SNSNotificationArn": "string"
   }
}
```

## Response Elements
<a name="API_UpdateApplication_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ApplicationInfo](#API_UpdateApplication_ResponseSyntax) **   <a name="appinsights-UpdateApplication-response-ApplicationInfo"></a>
Information about the application.
Type: [ApplicationInfo](API_ApplicationInfo.md) object

## Errors
<a name="API_UpdateApplication_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
The server encountered an internal error and is unable to complete the request.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The resource does not exist in the customer account.
HTTP Status Code: 400

 ** ValidationException **
The parameter is not valid.
HTTP Status Code: 400

## See Also
<a name="API_UpdateApplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/application-insights-2018-11-25/UpdateApplication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/application-insights-2018-11-25/UpdateApplication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-insights-2018-11-25/UpdateApplication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/application-insights-2018-11-25/UpdateApplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-insights-2018-11-25/UpdateApplication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/application-insights-2018-11-25/UpdateApplication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/application-insights-2018-11-25/UpdateApplication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/application-insights-2018-11-25/UpdateApplication)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/application-insights-2018-11-25/UpdateApplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-insights-2018-11-25/UpdateApplication)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Application Insights. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudwatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
