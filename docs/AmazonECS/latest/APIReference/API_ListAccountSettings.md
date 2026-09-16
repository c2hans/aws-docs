---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ListAccountSettings.html
---

# ListAccountSettings
<a name="API_ListAccountSettings"></a>

Lists the account settings for a specified principal.

## Request Syntax
<a name="API_ListAccountSettings_RequestSyntax"></a>

```
{
   "effectiveSettings": {{boolean}},
   "maxResults": {{number}},
   "name": "{{string}}",
   "nextToken": "{{string}}",
   "principalArn": "{{string}}",
   "value": "{{string}}"
}
```

## Request Parameters
<a name="API_ListAccountSettings_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [effectiveSettings](#API_ListAccountSettings_RequestSyntax) **   <a name="ECS-ListAccountSettings-request-effectiveSettings"></a>
Determines whether to return the effective settings. If `true`, the account settings for the root user or the default setting for the `principalArn` are returned. If `false`, the account settings for the `principalArn` are returned if they're set. Otherwise, no account settings are returned.
Type: Boolean
Required: No

 ** [maxResults](#API_ListAccountSettings_RequestSyntax) **   <a name="ECS-ListAccountSettings-request-maxResults"></a>
The maximum number of account setting results returned by `ListAccountSettings` in paginated output. When this parameter is used, `ListAccountSettings` only returns `maxResults` results in a single page along with a `nextToken` response element. The remaining results of the initial request can be seen by sending another `ListAccountSettings` request with the returned `nextToken` value. This value can be between 1 and 10. If this parameter isn't used, then `ListAccountSettings` returns up to 10 results and a `nextToken` value if applicable.
Type: Integer
Required: No

 ** [name](#API_ListAccountSettings_RequestSyntax) **   <a name="ECS-ListAccountSettings-request-name"></a>
The name of the account setting you want to list the settings for.
Type: String
Valid Values: `serviceLongArnFormat | taskLongArnFormat | containerInstanceLongArnFormat | awsvpcTrunking | containerInsights | fargateFIPSMode | tagResourceAuthorization | fargateTaskRetirementWaitPeriod | guardDutyActivate | defaultLogDriverMode | fargateEventWindows`
Required: No

 ** [nextToken](#API_ListAccountSettings_RequestSyntax) **   <a name="ECS-ListAccountSettings-request-nextToken"></a>
The `nextToken` value returned from a `ListAccountSettings` request indicating that more results are available to fulfill the request and further calls will be needed. If `maxResults` was provided, it's possible the number of results to be fewer than `maxResults`.
This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.
Type: String
Required: No

 ** [principalArn](#API_ListAccountSettings_RequestSyntax) **   <a name="ECS-ListAccountSettings-request-principalArn"></a>
The ARN of the principal, which can be a user, role, or the root user. If this field is omitted, the account settings are listed only for the authenticated user.
In order to use this parameter, you must be the root user, or the principal.
Federated users assume the account setting of the root user and can't have explicit account settings set for them.
Type: String
Required: No

 ** [value](#API_ListAccountSettings_RequestSyntax) **   <a name="ECS-ListAccountSettings-request-value"></a>
The value of the account settings to filter results with. You must also specify an account setting name to use this parameter.
Type: String
Required: No

## Response Syntax
<a name="API_ListAccountSettings_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "settings": [
      {
         "name": "string",
         "principalArn": "string",
         "type": "string",
         "value": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListAccountSettings_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListAccountSettings_ResponseSyntax) **   <a name="ECS-ListAccountSettings-response-nextToken"></a>
The `nextToken` value to include in a future `ListAccountSettings` request. When the results of a `ListAccountSettings` request exceed `maxResults`, this value can be used to retrieve the next page of results. This value is `null` when there are no more results to return.
Type: String

 ** [settings](#API_ListAccountSettings_ResponseSyntax) **   <a name="ECS-ListAccountSettings-response-settings"></a>
The account settings for the resource.
Type: Array of [Setting](API_Setting.md) objects

## Errors
<a name="API_ListAccountSettings_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have authorization to perform the requested action.
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 400

 ** ClientException **
These errors are usually caused by a client action. This client action might be using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Or, it might be specifying an identifier that isn't valid.
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 400

 ** InvalidParameterException **
The specified parameter isn't valid. Review the available parameters for the API request.
For more information about service event errors, see [Amazon ECS service event messages](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-event-messages-list.html).
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 400

 ** ServerException **
These errors are usually caused by a server issue.
 ** message **
 Message that describes the cause of the exception.
HTTP Status Code: 500

## See Also
<a name="API_ListAccountSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecs-2014-11-13/ListAccountSettings)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecs-2014-11-13/ListAccountSettings)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/ListAccountSettings)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecs-2014-11-13/ListAccountSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/ListAccountSettings)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecs-2014-11-13/ListAccountSettings)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecs-2014-11-13/ListAccountSettings)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecs-2014-11-13/ListAccountSettings)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ecs-2014-11-13/ListAccountSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/ListAccountSettings)
