---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateDashboardLinks.html
---

# UpdateDashboardLinks
<a name="API_UpdateDashboardLinks"></a>

Updates the linked analyses on a dashboard.

## Request Syntax
<a name="API_UpdateDashboardLinks_RequestSyntax"></a>

```
PUT /accounts/{{AwsAccountId}}/dashboards/{{DashboardId}}/linked-entities HTTP/1.1
Content-type: application/json

{
   "LinkEntities": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_UpdateDashboardLinks_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_UpdateDashboardLinks_RequestSyntax) **   <a name="QS-UpdateDashboardLinks-request-uri-AwsAccountId"></a>
The ID of the AWS account that contains the dashboard whose links you want to update.
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]{12}$`
Required: Yes

 ** [DashboardId](#API_UpdateDashboardLinks_RequestSyntax) **   <a name="QS-UpdateDashboardLinks-request-uri-DashboardId"></a>
The ID for the dashboard.
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

## Request Body
<a name="API_UpdateDashboardLinks_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [LinkEntities](#API_UpdateDashboardLinks_RequestSyntax) **   <a name="QS-UpdateDashboardLinks-request-LinkEntities"></a>
 list of analysis Amazon Resource Names (ARNs) to be linked to the dashboard.
Type: Array of strings
Array Members: Maximum number of 5 items.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^arn:aws[\w\-]*:quicksight:[\w\-]+:\d+:analysis/[\w\-]{1,512}`
Required: Yes

## Response Syntax
<a name="API_UpdateDashboardLinks_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "DashboardArn": "string",
   "LinkEntities": [ "string" ],
   "RequestId": "string"
}
```

## Response Elements
<a name="API_UpdateDashboardLinks_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_UpdateDashboardLinks_ResponseSyntax) **   <a name="QS-UpdateDashboardLinks-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [DashboardArn](#API_UpdateDashboardLinks_ResponseSyntax) **   <a name="QS-UpdateDashboardLinks-response-DashboardArn"></a>
The Amazon Resource Name (ARN) of the dashboard.
Type: String

 ** [LinkEntities](#API_UpdateDashboardLinks_ResponseSyntax) **   <a name="QS-UpdateDashboardLinks-response-LinkEntities"></a>
A list of analysis Amazon Resource Names (ARNs) to be linked to the dashboard.
Type: Array of strings
Array Members: Maximum number of 5 items.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^arn:aws[\w\-]*:quicksight:[\w\-]+:\d+:analysis/[\w\-]{1,512}`

 ** [RequestId](#API_UpdateDashboardLinks_ResponseSyntax) **   <a name="QS-UpdateDashboardLinks-response-RequestId"></a>
The AWS request ID for this operation.
Type: String

## Errors
<a name="API_UpdateDashboardLinks_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have access to this item. The provided credentials couldn't be validated. You might not be authorized to carry out the request. Make sure that your account is authorized to use the Amazon Quick Sight service, that your policies have the correct permissions, and that you are using the correct credentials.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 401

 ** ConflictException **
Updating or deleting a resource can cause an inconsistent state.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 409

 ** InternalFailureException **
An internal failure occurred.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 500

 ** InvalidParameterValueException **
One or more parameters has a value that isn't valid.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 400

 ** ResourceNotFoundException **
One or more resources can't be found.
 ** RequestId **
The AWS request ID for this request.
 ** ResourceType **
The resource type for this request.
HTTP Status Code: 404

 ** ThrottlingException **
Access is throttled.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 429

 ** UnsupportedUserEditionException **
This error indicates that you are calling an operation on an Amazon Quick Suite subscription where the edition doesn't include support for that operation. Amazon Quick Suite currently has Standard Edition and Enterprise Edition. Not every operation and capability is available in every edition.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 403

## See Also
<a name="API_UpdateDashboardLinks_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/UpdateDashboardLinks)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/UpdateDashboardLinks)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/UpdateDashboardLinks)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/UpdateDashboardLinks)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/UpdateDashboardLinks)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/UpdateDashboardLinks)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/UpdateDashboardLinks)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/UpdateDashboardLinks)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/UpdateDashboardLinks)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/UpdateDashboardLinks)
