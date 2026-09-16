---
source_url: https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_CreateApplication.html
---

# CreateApplication
<a name="API_CreateApplication"></a>

Adds an application that is created from a resource group.

## Request Syntax
<a name="API_CreateApplication_RequestSyntax"></a>

```
{
   "AttachMissingPermission": {{boolean}},
   "AutoConfigEnabled": {{boolean}},
   "AutoCreate": {{boolean}},
   "CWEMonitorEnabled": {{boolean}},
   "GroupingType": "{{string}}",
   "OpsCenterEnabled": {{boolean}},
   "OpsItemSNSTopicArn": "{{string}}",
   "ResourceGroupName": "{{string}}",
   "SNSNotificationArn": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateApplication_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AttachMissingPermission](#API_CreateApplication_RequestSyntax) **   <a name="appinsights-CreateApplication-request-AttachMissingPermission"></a>
If set to true, the managed policies for SSM and CW will be attached to the instance roles if they are missing.
Type: Boolean
Required: No

 ** [AutoConfigEnabled](#API_CreateApplication_RequestSyntax) **   <a name="appinsights-CreateApplication-request-AutoConfigEnabled"></a>
 Indicates whether Application Insights automatically configures unmonitored resources in the resource group.
Type: Boolean
Required: No

 ** [AutoCreate](#API_CreateApplication_RequestSyntax) **   <a name="appinsights-CreateApplication-request-AutoCreate"></a>
 Configures all of the resources in the resource group by applying the recommended configurations.
Type: Boolean
Required: No

 ** [CWEMonitorEnabled](#API_CreateApplication_RequestSyntax) **   <a name="appinsights-CreateApplication-request-CWEMonitorEnabled"></a>
 Indicates whether Application Insights can listen to CloudWatch events for the application resources, such as `instance terminated`, `failed deployment`, and others.
Type: Boolean
Required: No

 ** [GroupingType](#API_CreateApplication_RequestSyntax) **   <a name="appinsights-CreateApplication-request-GroupingType"></a>
Application Insights can create applications based on a resource group or on an account. To create an account-based application using all of the resources in the account, set this parameter to `ACCOUNT_BASED`.
Type: String
Valid Values: `ACCOUNT_BASED`
Required: No

 ** [OpsCenterEnabled](#API_CreateApplication_RequestSyntax) **   <a name="appinsights-CreateApplication-request-OpsCenterEnabled"></a>
 When set to `true`, creates opsItems for any problems detected on an application.
Type: Boolean
Required: No

 ** [OpsItemSNSTopicArn](#API_CreateApplication_RequestSyntax) **   <a name="appinsights-CreateApplication-request-OpsItemSNSTopicArn"></a>
 The SNS topic provided to Application Insights that is associated to the created opsItem. Allows you to receive notifications for updates to the opsItem.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 300.
Pattern: `^arn:aws(-\w+)*:[\w\d-]+:([\w\d-]*)?:[\w\d_-]*([:/].+)*$`
Required: No

 ** [ResourceGroupName](#API_CreateApplication_RequestSyntax) **   <a name="appinsights-CreateApplication-request-ResourceGroupName"></a>
The name of the resource group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9\.\-_]*`
Required: No

 ** [SNSNotificationArn](#API_CreateApplication_RequestSyntax) **   <a name="appinsights-CreateApplication-request-SNSNotificationArn"></a>
 The SNS notification topic ARN.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 300.
Pattern: `^arn:aws(-\w+)*:[\w\d-]+:([\w\d-]*)?:[\w\d_-]*([:/].+)*$`
Required: No

 ** [Tags](#API_CreateApplication_RequestSyntax) **   <a name="appinsights-CreateApplication-request-Tags"></a>
List of tags to add to the application. tag key (`Key`) and an associated tag value (`Value`). The maximum length of a tag key is 128 characters. The maximum length of a tag value is 256 characters.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

## Response Syntax
<a name="API_CreateApplication_ResponseSyntax"></a>

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
<a name="API_CreateApplication_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ApplicationInfo](#API_CreateApplication_ResponseSyntax) **   <a name="appinsights-CreateApplication-response-ApplicationInfo"></a>
Information about the application.
Type: [ApplicationInfo](API_ApplicationInfo.md) object

## Errors
<a name="API_CreateApplication_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 User does not have permissions to perform this action.
HTTP Status Code: 400

 ** InternalServerException **
The server encountered an internal error and is unable to complete the request.
HTTP Status Code: 400

 ** ResourceInUseException **
The resource is already created or in use.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The resource does not exist in the customer account.
HTTP Status Code: 400

 ** TagsAlreadyExistException **
Tags are already registered for the specified application ARN.
HTTP Status Code: 400

 ** ValidationException **
The parameter is not valid.
HTTP Status Code: 400

## See Also
<a name="API_CreateApplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/application-insights-2018-11-25/CreateApplication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/application-insights-2018-11-25/CreateApplication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-insights-2018-11-25/CreateApplication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/application-insights-2018-11-25/CreateApplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-insights-2018-11-25/CreateApplication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/application-insights-2018-11-25/CreateApplication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/application-insights-2018-11-25/CreateApplication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/application-insights-2018-11-25/CreateApplication)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/application-insights-2018-11-25/CreateApplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-insights-2018-11-25/CreateApplication)
