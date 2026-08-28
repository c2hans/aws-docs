---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeView.html
---

# DescribeView
<a name="API_DescribeView"></a>

Retrieves the view for the specified Connect Customer instance and view identifier.

The view identifier can be supplied as a ViewId or ARN.

 `$SAVED` needs to be supplied if a view is unpublished.

The view identifier can contain an optional qualifier, for example, `<view-id>:$SAVED`, which is either an actual version number or an Connect Customer managed qualifier `$SAVED | $LATEST`. If it is not supplied, then `$LATEST` is assumed for customer managed views and an error is returned if there is no published content available. Version 1 is assumed for AWS managed views.

## Request Syntax
<a name="API_DescribeView_RequestSyntax"></a>

```
GET /views/{{InstanceId}}/{{ViewId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeView_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_DescribeView_RequestSyntax) **   <a name="connect-DescribeView-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can find the instanceId in the ARN of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9\_\-:\/]+$`
Required: Yes

 ** [ViewId](#API_DescribeView_RequestSyntax) **   <a name="connect-DescribeView-request-uri-ViewId"></a>
The ViewId of the view. This must be an ARN for AWS managed views.
Length Constraints: Minimum length of 1. Maximum length of 500.
Pattern: `^[a-zA-Z0-9\_\-:\/$]+$`
Required: Yes

## Request Body
<a name="API_DescribeView_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeView_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "View": {
      "Arn": "string",
      "Content": {
         "Actions": [ "string" ],
         "InputSchema": "string",
         "Template": "string"
      },
      "CreatedTime": number,
      "Description": "string",
      "Id": "string",
      "LastModifiedTime": number,
      "Name": "string",
      "Status": "string",
      "Tags": {
         "string" : "string"
      },
      "Type": "string",
      "Version": number,
      "VersionDescription": "string",
      "ViewContentSha256": "string"
   }
}
```

## Response Elements
<a name="API_DescribeView_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [View](#API_DescribeView_ResponseSyntax) **   <a name="connect-DescribeView-response-View"></a>
All view data is contained within the View object.
Type: [View](API_View.md) object

## Errors
<a name="API_DescribeView_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidParameterException **
One or more of the specified parameters are not valid.
 ** Message **
The message about the parameters.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is not valid.
 ** Message **
The message about the request.
 ** Reason **
Reason why the request was invalid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** TooManyRequestsException **
Displayed when rate-related API limits are exceeded.
HTTP Status Code: 429

## See Also
<a name="API_DescribeView_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/DescribeView)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/DescribeView)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/DescribeView)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/DescribeView)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/DescribeView)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/DescribeView)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/DescribeView)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/DescribeView)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/DescribeView)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/DescribeView)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
