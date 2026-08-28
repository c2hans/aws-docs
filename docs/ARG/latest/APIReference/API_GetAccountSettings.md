---
source_url: https://docs.aws.amazon.com/ARG/latest/APIReference/API_GetAccountSettings.html
---

# GetAccountSettings
<a name="API_GetAccountSettings"></a>

Retrieves the current status of optional features in Resource Groups.

## Request Syntax
<a name="API_GetAccountSettings_RequestSyntax"></a>

```
POST /get-account-settings HTTP/1.1
```

## URI Request Parameters
<a name="API_GetAccountSettings_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetAccountSettings_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetAccountSettings_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AccountSettings": {
      "GroupLifecycleEventsDesiredStatus": "string",
      "GroupLifecycleEventsStatus": "string",
      "GroupLifecycleEventsStatusMessage": "string"
   }
}
```

## Response Elements
<a name="API_GetAccountSettings_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AccountSettings](#API_GetAccountSettings_ResponseSyntax) **   <a name="ARG-GetAccountSettings-response-AccountSettings"></a>
The current settings for the optional features in Resource Groups.
Type: [AccountSettings](API_AccountSettings.md) object

## Errors
<a name="API_GetAccountSettings_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
The request includes one or more parameters that violate validation rules.
HTTP Status Code: 400

 ** ForbiddenException **
The caller isn't authorized to make the request. Check permissions.
HTTP Status Code: 403

 ** InternalServerErrorException **
An internal error occurred while processing the request. Try again later.
HTTP Status Code: 500

 ** MethodNotAllowedException **
The request uses an HTTP method that isn't allowed for the specified resource.
HTTP Status Code: 405

 ** TooManyRequestsException **
You've exceeded throttling limits by making too many requests in a period of time.
HTTP Status Code: 429

## Examples
<a name="API_GetAccountSettings_Examples"></a>

### Example
<a name="API_GetAccountSettings_Example_1"></a>

The following example retrieves the current Resource Groups account settings for the calling AWS account:

#### Sample Request
<a name="API_GetAccountSettings_Example_1_Request"></a>

```
POST /get-account-settings HTTP/1.1
Host: resource-groups.us-east-1.amazonaws.com
Accept-Encoding: identity
User-Agent: <VARIES>
X-Amz-Date: 20221213T214448Z
X-Amz-Security-Token: <SECURITY-TOKEN>
Authorization: AWS4-HMAC-SHA256 Credential=<ACCESS-KEY>/20220113/us-west-2/resource-groups/aws4_request,SignedHeaders=host;x-amz-date;x-amz-security-token,Signature=<SIGV4-SIGNATURE>
```

#### Sample Response
<a name="API_GetAccountSettings_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 13 Dec 2022 21:44:48 GMT
Content-Type: application/json
Content-Length: 61
x-amzn-RequestId: <VARIES>
x-amz-apigw-id: <VARIES>
X-Amzn-Trace-Id: Root=<VARIES>
Connection: keep-alive

{
    "AccountSettings": {
        "GroupLifecycleEventsStatus": "INACTIVE"
    }
}
```

## See Also
<a name="API_GetAccountSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resource-groups-2017-11-27/GetAccountSettings)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resource-groups-2017-11-27/GetAccountSettings)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resource-groups-2017-11-27/GetAccountSettings)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resource-groups-2017-11-27/GetAccountSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resource-groups-2017-11-27/GetAccountSettings)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resource-groups-2017-11-27/GetAccountSettings)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resource-groups-2017-11-27/GetAccountSettings)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resource-groups-2017-11-27/GetAccountSettings)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/resource-groups-2017-11-27/GetAccountSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resource-groups-2017-11-27/GetAccountSettings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Resource Groups & Tagging. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ARG` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
