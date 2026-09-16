---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateDashboardPublishedVersion.html
---

# UpdateDashboardPublishedVersion
<a name="API_UpdateDashboardPublishedVersion"></a>

Updates the published version of a dashboard.

## Request Syntax
<a name="API_UpdateDashboardPublishedVersion_RequestSyntax"></a>

```
PUT /accounts/{{AwsAccountId}}/dashboards/{{DashboardId}}/versions/{{VersionNumber}} HTTP/1.1
```

## URI Request Parameters
<a name="API_UpdateDashboardPublishedVersion_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_UpdateDashboardPublishedVersion_RequestSyntax) **   <a name="QS-UpdateDashboardPublishedVersion-request-uri-AwsAccountId"></a>
The ID of the AWS account that contains the dashboard that you're updating.
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]{12}$`
Required: Yes

 ** [DashboardId](#API_UpdateDashboardPublishedVersion_RequestSyntax) **   <a name="QS-UpdateDashboardPublishedVersion-request-uri-DashboardId"></a>
The ID for the dashboard.
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

 ** [VersionNumber](#API_UpdateDashboardPublishedVersion_RequestSyntax) **   <a name="QS-UpdateDashboardPublishedVersion-request-uri-VersionNumber"></a>
The version number of the dashboard.
Valid Range: Minimum value of 1.
Required: Yes

## Request Body
<a name="API_UpdateDashboardPublishedVersion_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_UpdateDashboardPublishedVersion_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "DashboardArn": "string",
   "DashboardId": "string",
   "RequestId": "string"
}
```

## Response Elements
<a name="API_UpdateDashboardPublishedVersion_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_UpdateDashboardPublishedVersion_ResponseSyntax) **   <a name="QS-UpdateDashboardPublishedVersion-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [DashboardArn](#API_UpdateDashboardPublishedVersion_ResponseSyntax) **   <a name="QS-UpdateDashboardPublishedVersion-response-DashboardArn"></a>
The Amazon Resource Name (ARN) of the dashboard.
Type: String

 ** [DashboardId](#API_UpdateDashboardPublishedVersion_ResponseSyntax) **   <a name="QS-UpdateDashboardPublishedVersion-response-DashboardId"></a>
The ID for the dashboard.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`

 ** [RequestId](#API_UpdateDashboardPublishedVersion_ResponseSyntax) **   <a name="QS-UpdateDashboardPublishedVersion-response-RequestId"></a>
The AWS request ID for this operation.
Type: String

## Errors
<a name="API_UpdateDashboardPublishedVersion_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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
<a name="API_UpdateDashboardPublishedVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/UpdateDashboardPublishedVersion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/UpdateDashboardPublishedVersion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/UpdateDashboardPublishedVersion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/UpdateDashboardPublishedVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/UpdateDashboardPublishedVersion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/UpdateDashboardPublishedVersion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/UpdateDashboardPublishedVersion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/UpdateDashboardPublishedVersion)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/UpdateDashboardPublishedVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/UpdateDashboardPublishedVersion)
