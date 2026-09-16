---
source_url: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_CheckNoNewAccess.html
---

# CheckNoNewAccess
<a name="API_CheckNoNewAccess"></a>

Checks whether new access is allowed for an updated policy when compared to the existing policy.

You can find examples for reference policies and learn how to set up and run a custom policy check for new access in the [IAM Access Analyzer custom policy checks samples](https://github.com/aws-samples/iam-access-analyzer-custom-policy-check-samples) repository on GitHub. The reference policies in this repository are meant to be passed to the `existingPolicyDocument` request parameter.

## Request Syntax
<a name="API_CheckNoNewAccess_RequestSyntax"></a>

```
POST /policy/check-no-new-access HTTP/1.1
Content-type: application/json

{
   "existingPolicyDocument": "{{string}}",
   "newPolicyDocument": "{{string}}",
   "policyType": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CheckNoNewAccess_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CheckNoNewAccess_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [existingPolicyDocument](#API_CheckNoNewAccess_RequestSyntax) **   <a name="accessanalyzer-CheckNoNewAccess-request-existingPolicyDocument"></a>
The JSON policy document to use as the content for the existing policy.
Type: String
Required: Yes

 ** [newPolicyDocument](#API_CheckNoNewAccess_RequestSyntax) **   <a name="accessanalyzer-CheckNoNewAccess-request-newPolicyDocument"></a>
The JSON policy document to use as the content for the updated policy.
Type: String
Required: Yes

 ** [policyType](#API_CheckNoNewAccess_RequestSyntax) **   <a name="accessanalyzer-CheckNoNewAccess-request-policyType"></a>
The type of policy to compare. Identity policies grant permissions to IAM principals. Identity policies include managed and inline policies for IAM roles, users, and groups.
Resource policies grant permissions on AWS resources. Resource policies include trust policies for IAM roles and bucket policies for Amazon S3 buckets. You can provide a generic input such as identity policy or resource policy or a specific input such as managed policy or Amazon S3 bucket policy.
Type: String
Valid Values: `IDENTITY_POLICY | RESOURCE_POLICY`
Required: Yes

## Response Syntax
<a name="API_CheckNoNewAccess_ResponseSyntax"></a>

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
<a name="API_CheckNoNewAccess_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [message](#API_CheckNoNewAccess_ResponseSyntax) **   <a name="accessanalyzer-CheckNoNewAccess-response-message"></a>
The message indicating whether the updated policy allows new access.
Type: String

 ** [reasons](#API_CheckNoNewAccess_ResponseSyntax) **   <a name="accessanalyzer-CheckNoNewAccess-response-reasons"></a>
A description of the reasoning of the result.
Type: Array of [ReasonSummary](API_ReasonSummary.md) objects

 ** [result](#API_CheckNoNewAccess_ResponseSyntax) **   <a name="accessanalyzer-CheckNoNewAccess-response-result"></a>
The result of the check for new access. If the result is `PASS`, no new access is allowed by the updated policy. If the result is `FAIL`, the updated policy might allow new access.
Type: String
Valid Values: `PASS | FAIL`

## Errors
<a name="API_CheckNoNewAccess_Errors"></a>

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
<a name="API_CheckNoNewAccess_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/accessanalyzer-2019-11-01/CheckNoNewAccess)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/accessanalyzer-2019-11-01/CheckNoNewAccess)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/CheckNoNewAccess)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/accessanalyzer-2019-11-01/CheckNoNewAccess)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/CheckNoNewAccess)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/accessanalyzer-2019-11-01/CheckNoNewAccess)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/accessanalyzer-2019-11-01/CheckNoNewAccess)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/accessanalyzer-2019-11-01/CheckNoNewAccess)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/accessanalyzer-2019-11-01/CheckNoNewAccess)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/CheckNoNewAccess)
