---
source_url: https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_DescribeOrganizationOverview.html
---

# DescribeOrganizationOverview
<a name="API_DescribeOrganizationOverview"></a>

**Note**
End of support notice: On September 30, 2027, AWS will end support for Amazon DevOps Guru. After September 30, 2027, you will no longer be able to access the Amazon DevOps Guru console or Amazon DevOps Guru resources. For more information, see [Amazon DevOps Guru end of support](https://docs.aws.amazon.com/devops-guru/latest/userguide/devops-guru-end-of-support.html).

Returns an overview of your organization's history based on the specified time range. The overview includes the total reactive and proactive insights.

## Request Syntax
<a name="API_DescribeOrganizationOverview_RequestSyntax"></a>

```
POST /organization/overview HTTP/1.1
Content-type: application/json

{
   "AccountIds": [ "{{string}}" ],
   "FromTime": {{number}},
   "OrganizationalUnitIds": [ "{{string}}" ],
   "ToTime": {{number}}
}
```

## URI Request Parameters
<a name="API_DescribeOrganizationOverview_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DescribeOrganizationOverview_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AccountIds](#API_DescribeOrganizationOverview_RequestSyntax) **   <a name="DevOpsGuru-DescribeOrganizationOverview-request-AccountIds"></a>
The ID of the AWS account.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Length Constraints: Fixed length of 12.
Pattern: `^\d{12}$`
Required: No

 ** [FromTime](#API_DescribeOrganizationOverview_RequestSyntax) **   <a name="DevOpsGuru-DescribeOrganizationOverview-request-FromTime"></a>
 The start of the time range passed in. The start time granularity is at the day level. The floor of the start time is used. Returned information occurred after this day.
Type: Timestamp
Required: Yes

 ** [OrganizationalUnitIds](#API_DescribeOrganizationOverview_RequestSyntax) **   <a name="DevOpsGuru-DescribeOrganizationOverview-request-OrganizationalUnitIds"></a>
The ID of the organizational unit.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Length Constraints: Maximum length of 68.
Pattern: `^ou-[0-9a-z]{4,32}-[a-z0-9]{8,32}$`
Required: No

 ** [ToTime](#API_DescribeOrganizationOverview_RequestSyntax) **   <a name="DevOpsGuru-DescribeOrganizationOverview-request-ToTime"></a>
 The end of the time range passed in. The start time granularity is at the day level. The floor of the start time is used. Returned information occurred before this day. If this is not specified, then the current day is used.
Type: Timestamp
Required: No

## Response Syntax
<a name="API_DescribeOrganizationOverview_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ProactiveInsights": number,
   "ReactiveInsights": number
}
```

## Response Elements
<a name="API_DescribeOrganizationOverview_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ProactiveInsights](#API_DescribeOrganizationOverview_ResponseSyntax) **   <a name="DevOpsGuru-DescribeOrganizationOverview-response-ProactiveInsights"></a>
An integer that specifies the number of open proactive insights in your AWS account.
Type: Integer

 ** [ReactiveInsights](#API_DescribeOrganizationOverview_ResponseSyntax) **   <a name="DevOpsGuru-DescribeOrganizationOverview-response-ReactiveInsights"></a>
An integer that specifies the number of open reactive insights in your AWS account.
Type: Integer

## Errors
<a name="API_DescribeOrganizationOverview_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 You don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see [Access Management](https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html) in the *IAM User Guide*.
HTTP Status Code: 403

 ** InternalServerException **
An internal failure in an Amazon service occurred.
 ** RetryAfterSeconds **
 The number of seconds after which the action that caused the internal server exception can be retried.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to a request throttling.
 ** QuotaCode **
 The code of the quota that was exceeded, causing the throttling exception.
 ** RetryAfterSeconds **
 The number of seconds after which the action that caused the throttling exception can be retried.
 ** ServiceCode **
 The code of the service that caused the throttling exception.
HTTP Status Code: 429

 ** ValidationException **
 Contains information about data passed in to a field during a request that is not valid.
 ** Fields **
 An array of fields that are associated with the validation exception.
 ** Message **
 A message that describes the validation exception.
 ** Reason **
 The reason the validation exception was thrown.
HTTP Status Code: 400

## See Also
<a name="API_DescribeOrganizationOverview_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/devops-guru-2020-12-01/DescribeOrganizationOverview)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/devops-guru-2020-12-01/DescribeOrganizationOverview)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-guru-2020-12-01/DescribeOrganizationOverview)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/devops-guru-2020-12-01/DescribeOrganizationOverview)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-guru-2020-12-01/DescribeOrganizationOverview)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/devops-guru-2020-12-01/DescribeOrganizationOverview)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/devops-guru-2020-12-01/DescribeOrganizationOverview)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/devops-guru-2020-12-01/DescribeOrganizationOverview)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/devops-guru-2020-12-01/DescribeOrganizationOverview)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-guru-2020-12-01/DescribeOrganizationOverview)
