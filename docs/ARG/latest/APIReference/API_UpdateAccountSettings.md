---
source_url: https://docs.aws.amazon.com/ARG/latest/APIReference/API_UpdateAccountSettings.html
---

# UpdateAccountSettings
<a name="API_UpdateAccountSettings"></a>

**Note**
 AWS Group Lifecycle Events (GLE) feature of AWS Resource Groups is no longer open to new customers. For capabilities similar to Group Lifecycle Events (GLE), see the recommended EventBridge-based alternative. For more information, see [Group Lifecycle Events feature of AWS Resource Groups availability change](https://docs.aws.amazon.com/ARG/latest/userguide/resource-groups-gle-availability-change.html).

Turns on or turns off optional features in Resource Groups.

The preceding example shows that the request to turn on group lifecycle events is `IN_PROGRESS`. You can call the [GetAccountSettings](API_GetAccountSettings.md) operation to check for completion by looking for `GroupLifecycleEventsStatus` to change to `ACTIVE`.

## Request Syntax
<a name="API_UpdateAccountSettings_RequestSyntax"></a>

```
POST /update-account-settings HTTP/1.1
Content-type: application/json

{
   "GroupLifecycleEventsDesiredStatus": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateAccountSettings_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateAccountSettings_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [GroupLifecycleEventsDesiredStatus](#API_UpdateAccountSettings_RequestSyntax) **   <a name="ARG-UpdateAccountSettings-request-GroupLifecycleEventsDesiredStatus"></a>
 AWS Group Lifecycle Events (GLE) feature of AWS Resource Groups is no longer open to new customers. For capabilities similar to Group Lifecycle Events (GLE), see the recommended EventBridge-based alternative. For more information, see [Group Lifecycle Events feature of AWS Resource Groups availability change](https://docs.aws.amazon.com/ARG/latest/userguide/resource-groups-gle-availability-change.html).
Specifies whether you want to turn [group lifecycle events](https://docs.aws.amazon.com/ARG/latest/userguide/monitor-groups.html) on or off.
You can't turn on group lifecycle events if your resource groups quota is greater than 2,000.
Type: String
Valid Values: `ACTIVE | INACTIVE`
Required: No

## Response Syntax
<a name="API_UpdateAccountSettings_ResponseSyntax"></a>

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
<a name="API_UpdateAccountSettings_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AccountSettings](#API_UpdateAccountSettings_ResponseSyntax) **   <a name="ARG-UpdateAccountSettings-response-AccountSettings"></a>
 AWS Group Lifecycle Events (GLE) feature of AWS Resource Groups is no longer open to new customers. For capabilities similar to Group Lifecycle Events (GLE), see the recommended EventBridge-based alternative. For more information, see [Group Lifecycle Events feature of AWS Resource Groups availability change](https://docs.aws.amazon.com/ARG/latest/userguide/resource-groups-gle-availability-change.html).
A structure that displays the status of the optional features in the account.
Type: [AccountSettings](API_AccountSettings.md) object

## Errors
<a name="API_UpdateAccountSettings_Errors"></a>

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
<a name="API_UpdateAccountSettings_Examples"></a>

### Example
<a name="API_UpdateAccountSettings_Example_1"></a>

The following example turns on the group lifecycle events setting for the calling AWS account:

#### Sample Request
<a name="API_UpdateAccountSettings_Example_1_Request"></a>

```
POST /update-account-settings HTTP/1.1
Host: resource-groups.us-east-1.amazonaws.com
Accept-Encoding: identity
User-Agent: <VARIES>
X-Amz-Date: 20221213T215349Z
X-Amz-Security-Token: <SECURITY-TOKEN>
Authorization: AWS4-HMAC-SHA256 Credential=<ACCESS-KEY>/20220113/us-west-2/resource-groups/aws4_request,SignedHeaders=host;x-amz-date;x-amz-security-token,Signature=<SIGV4-SIGNATURE>
Content-Length: 47

{
    "GroupLifecycleEventsDesiredStatus": "ACTIVE"
}
```

#### Sample Response
<a name="API_UpdateAccountSettings_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 13 Dec 2022 21:53:49 GMT
Content-Type: application/json
Content-Length: 109
x-amzn-RequestId: <VARIES>
x-amz-apigw-id: <VARIES>
X-Amzn-Trace-Id: Root=<VARIES>
Connection: keep-alive

{
    "AccountSettings": {
        "GroupLifecycleEventsDesiredStatus": "ACTIVE",
        "GroupLifecycleEventsStatus": "IN_PROGRESS"
    }
}
```

## See Also
<a name="API_UpdateAccountSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resource-groups-2017-11-27/UpdateAccountSettings)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resource-groups-2017-11-27/UpdateAccountSettings)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resource-groups-2017-11-27/UpdateAccountSettings)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resource-groups-2017-11-27/UpdateAccountSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resource-groups-2017-11-27/UpdateAccountSettings)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resource-groups-2017-11-27/UpdateAccountSettings)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resource-groups-2017-11-27/UpdateAccountSettings)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resource-groups-2017-11-27/UpdateAccountSettings)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/resource-groups-2017-11-27/UpdateAccountSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resource-groups-2017-11-27/UpdateAccountSettings)
