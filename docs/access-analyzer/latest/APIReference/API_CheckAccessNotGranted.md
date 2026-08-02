---
source_url: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_CheckAccessNotGranted.html
---

# CheckAccessNotGranted
<a name="API_CheckAccessNotGranted"></a>

Checks whether the specified access isn't allowed by a policy.

## Request Syntax
<a name="API_CheckAccessNotGranted_RequestSyntax"></a>

```
POST /policy/check-access-not-granted HTTP/1.1
Content-type: application/json

{
   "access": [
      {
         "actions": [ "{{string}}" ],
         "resources": [ "{{string}}" ]
      }
   ],
   "policyDocument": "{{string}}",
   "policyType": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CheckAccessNotGranted_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CheckAccessNotGranted_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [access](#API_CheckAccessNotGranted_RequestSyntax) **   <a name="accessanalyzer-CheckAccessNotGranted-request-access"></a>
An access object containing the permissions that shouldn't be granted by the specified policy. If only actions are specified, IAM Access Analyzer checks for access to peform at least one of the actions on any resource in the policy. If only resources are specified, then IAM Access Analyzer checks for access to perform any action on at least one of the resources. If both actions and resources are specified, IAM Access Analyzer checks for access to perform at least one of the specified actions on at least one of the specified resources.
Type: Array of [Access](API_Access.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Required: Yes

 ** [policyDocument](#API_CheckAccessNotGranted_RequestSyntax) **   <a name="accessanalyzer-CheckAccessNotGranted-request-policyDocument"></a>
The JSON policy document to use as the content for the policy.
Type: String
Required: Yes

 ** [policyType](#API_CheckAccessNotGranted_RequestSyntax) **   <a name="accessanalyzer-CheckAccessNotGranted-request-policyType"></a>
The type of policy. Identity policies grant permissions to IAM principals. Identity policies include managed and inline policies for IAM roles, users, and groups.
Resource policies grant permissions on AWS resources. Resource policies include trust policies for IAM roles and bucket policies for Amazon S3 buckets.
Type: String
Valid Values: `IDENTITY_POLICY | RESOURCE_POLICY`
Required: Yes

## Response Syntax
<a name="API_CheckAccessNotGranted_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "message": "string",
   "reasons": [
      {
         "description": "string",
         "statementId": "string",
         "statementIndex": number
      }
   ],
   "result": "string"
}
```

## Response Elements
<a name="API_CheckAccessNotGranted_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [message](#API_CheckAccessNotGranted_ResponseSyntax) **   <a name="accessanalyzer-CheckAccessNotGranted-response-message"></a>
The message indicating whether the specified access is allowed.
Type: String

 ** [reasons](#API_CheckAccessNotGranted_ResponseSyntax) **   <a name="accessanalyzer-CheckAccessNotGranted-response-reasons"></a>
A description of the reasoning of the result.
Type: Array of [ReasonSummary](API_ReasonSummary.md) objects

 ** [result](#API_CheckAccessNotGranted_ResponseSyntax) **   <a name="accessanalyzer-CheckAccessNotGranted-response-result"></a>
The result of the check for whether the access is allowed. If the result is `PASS`, the specified policy doesn't allow any of the specified permissions in the access object. If the result is `FAIL`, the specified policy might allow some or all of the permissions in the access object.
Type: String
Valid Values: `PASS | FAIL`

## Errors
<a name="API_CheckAccessNotGranted_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
Internal server error.
 ** retryAfterSeconds **
The seconds to wait to retry.
HTTP Status Code: 500

 ** InvalidParameterException **
The specified parameter is invalid.
HTTP Status Code: 400

 ** ThrottlingException **
Throttling limit exceeded error.
 ** retryAfterSeconds **
The seconds to wait to retry.
HTTP Status Code: 429

 ** UnprocessableEntityException **
The specified entity could not be processed.
HTTP Status Code: 422

 ** ValidationException **
Validation exception error.
 ** fieldList **
A list of fields that didn't validate.
 ** reason **
The reason for the exception.
HTTP Status Code: 400

## See Also
<a name="API_CheckAccessNotGranted_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/accessanalyzer-2019-11-01/CheckAccessNotGranted)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/accessanalyzer-2019-11-01/CheckAccessNotGranted)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/CheckAccessNotGranted)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/accessanalyzer-2019-11-01/CheckAccessNotGranted)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/CheckAccessNotGranted)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/accessanalyzer-2019-11-01/CheckAccessNotGranted)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/accessanalyzer-2019-11-01/CheckAccessNotGranted)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/accessanalyzer-2019-11-01/CheckAccessNotGranted)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/accessanalyzer-2019-11-01/CheckAccessNotGranted)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/CheckAccessNotGranted)
