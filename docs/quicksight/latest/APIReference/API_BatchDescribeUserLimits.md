---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_BatchDescribeUserLimits.html
---

# BatchDescribeUserLimits
<a name="API_BatchDescribeUserLimits"></a>

Describes the effective resource limits for one or more Amazon Quick Sight users, including the limits that apply to each user based on their profile assignments.

## Request Syntax
<a name="API_BatchDescribeUserLimits_RequestSyntax"></a>

```
POST /governance/limits/accounts/{{accountId}}/user-limits HTTP/1.1
Content-type: application/json

{
   "resourceTypes": [ "{{string}}" ],
   "users": [
      {
         "namespace": "{{string}}",
         "userName": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_BatchDescribeUserLimits_RequestParameters"></a>

The request uses the following URI parameters.

 ** [accountId](#API_BatchDescribeUserLimits_RequestSyntax) **   <a name="QS-BatchDescribeUserLimits-request-uri-accountId"></a>
The ID of the AWS account that contains the users.
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]{12}$`
Required: Yes

## Request Body
<a name="API_BatchDescribeUserLimits_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [resourceTypes](#API_BatchDescribeUserLimits_RequestSyntax) **   <a name="QS-BatchDescribeUserLimits-request-resourceTypes"></a>
An optional filter that limits the results to specific resource types. If you don't specify a value, the operation returns limits for all resource types.
Type: Array of strings
Valid Values: `INDEX_STORAGE | AGENT_HOURS`
Required: No

 ** [users](#API_BatchDescribeUserLimits_RequestSyntax) **   <a name="QS-BatchDescribeUserLimits-request-users"></a>
A list of users to describe limits for. Each entry contains a user name and namespace.
Type: Array of [UserLimitsEntry](API_UserLimitsEntry.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: No

## Response Syntax
<a name="API_BatchDescribeUserLimits_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "errors": [
      {
         "errorCode": "string",
         "message": "string",
         "namespace": "string",
         "userArn": "string",
         "userName": "string"
      }
   ],
   "userLimits": [
      {
         "effectiveLimits": [
            {
               "limitUnit": "string",
               "limitValue": number,
               "profileId": "string",
               "resourceType": "string",
               "source": "string"
            }
         ],
         "namespace": "string",
         "userName": "string"
      }
   ]
}
```

## Response Elements
<a name="API_BatchDescribeUserLimits_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [errors](#API_BatchDescribeUserLimits_ResponseSyntax) **   <a name="QS-BatchDescribeUserLimits-response-errors"></a>
A list of errors for users whose limits could not be described.
Type: Array of [BatchDescribeUserLimitsError](API_BatchDescribeUserLimitsError.md) objects

 ** [userLimits](#API_BatchDescribeUserLimits_ResponseSyntax) **   <a name="QS-BatchDescribeUserLimits-response-userLimits"></a>
A list of user limits results. Each entry contains the effective limits for a user.
Type: Array of [UserLimits](API_UserLimits.md) objects

## Errors
<a name="API_BatchDescribeUserLimits_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have access to this item. The provided credentials couldn't be validated. You might not be authorized to carry out the request. Make sure that your account is authorized to use the Amazon Quick Sight service, that your policies have the correct permissions, and that you are using the correct credentials.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 401

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

 ** ThrottlingException **
Access is throttled.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 429

## See Also
<a name="API_BatchDescribeUserLimits_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/BatchDescribeUserLimits)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/BatchDescribeUserLimits)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/BatchDescribeUserLimits)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/BatchDescribeUserLimits)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/BatchDescribeUserLimits)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/BatchDescribeUserLimits)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/BatchDescribeUserLimits)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/BatchDescribeUserLimits)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/BatchDescribeUserLimits)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/BatchDescribeUserLimits)
