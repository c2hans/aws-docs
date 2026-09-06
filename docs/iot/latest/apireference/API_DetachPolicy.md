---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_DetachPolicy.html
---

# DetachPolicy
<a name="API_DetachPolicy"></a>

Detaches a policy from the specified target.

**Note**
Because of the distributed nature of AWS, it can take up to five minutes after a policy is detached before it's ready to be deleted.

Requires permission to access the [DetachPolicy](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_DetachPolicy_RequestSyntax"></a>

```
POST /target-policies/{{policyName}} HTTP/1.1
Content-type: application/json

{
   "target": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DetachPolicy_RequestParameters"></a>

The request uses the following URI parameters.

 ** [policyName](#API_DetachPolicy_RequestSyntax) **   <a name="iot-DetachPolicy-request-uri-policyName"></a>
The policy to detach.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w+=,.@-]+`
Required: Yes

## Request Body
<a name="API_DetachPolicy_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [target](#API_DetachPolicy_RequestSyntax) **   <a name="iot-DetachPolicy-request-target"></a>
The target from which the policy will be detached.
Type: String
Required: Yes

## Response Syntax
<a name="API_DetachPolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DetachPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DetachPolicy_Errors"></a>

 ** InternalFailureException **
An unexpected error has occurred.
 ** message **
The message for the exception.
HTTP Status Code: 500

 ** InvalidRequestException **
The request is not valid.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** LimitExceededException **
A limit has been exceeded.
 ** message **
The message for the exception.
HTTP Status Code: 410

 ** ServiceUnavailableException **
The service is temporarily unavailable.
 ** message **
The message for the exception.
HTTP Status Code: 503

 ** ThrottlingException **
The rate exceeds the limit.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** UnauthorizedException **
You are not authorized to perform this operation.
 ** message **
The message for the exception.
HTTP Status Code: 401

## See Also
<a name="API_DetachPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/DetachPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/DetachPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/DetachPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/DetachPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/DetachPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/DetachPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/DetachPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/DetachPolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/DetachPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/DetachPolicy)
