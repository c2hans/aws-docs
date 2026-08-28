---
source_url: https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_GetAutoManagementConfiguration.html
---

# GetAutoManagementConfiguration
<a name="API_GetAutoManagementConfiguration"></a>

Retrieves information about your [Service Quotas Automatic Management](https://docs.aws.amazon.com/servicequotas/latest/userguide/automatic-management.html) configuration. Automatic Management monitors your Service Quotas utilization and notifies you before you run out of your allocated quotas.

## Response Syntax
<a name="API_GetAutoManagementConfiguration_ResponseSyntax"></a>

```
{
   "ExclusionList": {
      "string" : [
         {
            "QuotaCode": "string",
            "QuotaName": "string"
         }
      ]
   },
   "NotificationArn": "string",
   "OptInLevel": "string",
   "OptInStatus": "string",
   "OptInType": "string"
}
```

## Response Elements
<a name="API_GetAutoManagementConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ExclusionList](#API_GetAutoManagementConfiguration_ResponseSyntax) **   <a name="servicequotas-GetAutoManagementConfiguration-response-ExclusionList"></a>
List of AWS services excluded from Automatic Management. You won't be notified of Service Quotas utilization for AWS services added to the Automatic Management exclusion list.
Type: String to array of [QuotaInfo](API_QuotaInfo.md) objects map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[A-Za-z0-9-_ /]{1,128}`

 ** [NotificationArn](#API_GetAutoManagementConfiguration_ResponseSyntax) **   <a name="servicequotas-GetAutoManagementConfiguration-response-NotificationArn"></a>
The [AWS User Notifications](https://docs.aws.amazon.com/notifications/latest/userguide/resource-level-permissions.html#rlp-table) Amazon Resource Name (ARN) for Automatic Management notifications.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:aws(-[\w]+)*:*:.+:[0-9]{12}:.+`

 ** [OptInLevel](#API_GetAutoManagementConfiguration_ResponseSyntax) **   <a name="servicequotas-GetAutoManagementConfiguration-response-OptInLevel"></a>
Information on the opt-in level for Automatic Management. Only AWS account level is supported.
Type: String
Valid Values: `ACCOUNT`

 ** [OptInStatus](#API_GetAutoManagementConfiguration_ResponseSyntax) **   <a name="servicequotas-GetAutoManagementConfiguration-response-OptInStatus"></a>
Status on whether Automatic Management is started or stopped.
Type: String
Valid Values: `ENABLED | DISABLED`

 ** [OptInType](#API_GetAutoManagementConfiguration_ResponseSyntax) **   <a name="servicequotas-GetAutoManagementConfiguration-response-OptInType"></a>
Information on the opt-in type for Automatic Management. There are two modes: Notify only and Notify and Auto-Adjust. Currently, only NotifyOnly is available.
Type: String
Valid Values: `NotifyOnly | NotifyAndAdjust`

## Errors
<a name="API_GetAutoManagementConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permission to perform this action.
HTTP Status Code: 400

 ** IllegalArgumentException **
Invalid input was provided.
HTTP Status Code: 400

 ** NoSuchResourceException **
The specified resource does not exist.
HTTP Status Code: 400

 ** ServiceException **
Something went wrong.
HTTP Status Code: 500

 ** TooManyRequestsException **
Due to throttling, the request was denied. Slow down the rate of request calls, or request an increase for this quota.
HTTP Status Code: 400

## See Also
<a name="API_GetAutoManagementConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/service-quotas-2019-06-24/GetAutoManagementConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/service-quotas-2019-06-24/GetAutoManagementConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/service-quotas-2019-06-24/GetAutoManagementConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/service-quotas-2019-06-24/GetAutoManagementConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/service-quotas-2019-06-24/GetAutoManagementConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/service-quotas-2019-06-24/GetAutoManagementConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/service-quotas-2019-06-24/GetAutoManagementConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/service-quotas-2019-06-24/GetAutoManagementConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/service-quotas-2019-06-24/GetAutoManagementConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/service-quotas-2019-06-24/GetAutoManagementConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Service Quotas. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query servicequotas` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
