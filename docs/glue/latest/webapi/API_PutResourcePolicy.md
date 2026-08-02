---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_PutResourcePolicy.html
---

# PutResourcePolicy
<a name="API_PutResourcePolicy"></a>

Sets the Data Catalog resource policy for access control.

## Request Syntax
<a name="API_PutResourcePolicy_RequestSyntax"></a>

```
{
   "EnableHybrid": "{{string}}",
   "PolicyExistsCondition": "{{string}}",
   "PolicyHashCondition": "{{string}}",
   "PolicyInJson": "{{string}}",
   "ResourceArn": "{{string}}"
}
```

## Request Parameters
<a name="API_PutResourcePolicy_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [EnableHybrid](#API_PutResourcePolicy_RequestSyntax) **   <a name="Glue-PutResourcePolicy-request-EnableHybrid"></a>
If `'TRUE'`, indicates that you are using both methods to grant cross-account access to Data Catalog resources:
+ By directly updating the resource policy with `PutResourePolicy`
+ By using the **Grant permissions** command on the AWS Management Console.
Must be set to `'TRUE'` if you have already used the Management Console to grant cross-account access, otherwise the call fails. Default is 'FALSE'.
Type: String
Valid Values: `TRUE | FALSE`
Required: No

 ** [PolicyExistsCondition](#API_PutResourcePolicy_RequestSyntax) **   <a name="Glue-PutResourcePolicy-request-PolicyExistsCondition"></a>
A value of `MUST_EXIST` is used to update a policy. A value of `NOT_EXIST` is used to create a new policy. If a value of `NONE` or a null value is used, the call does not depend on the existence of a policy.
Type: String
Valid Values: `MUST_EXIST | NOT_EXIST | NONE`
Required: No

 ** [PolicyHashCondition](#API_PutResourcePolicy_RequestSyntax) **   <a name="Glue-PutResourcePolicy-request-PolicyHashCondition"></a>
The hash value returned when the previous policy was set using `PutResourcePolicy`. Its purpose is to prevent concurrent modifications of a policy. Do not use this parameter if no previous policy has been set.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [PolicyInJson](#API_PutResourcePolicy_RequestSyntax) **   <a name="Glue-PutResourcePolicy-request-PolicyInJson"></a>
Contains the policy document to set, in JSON format.
Type: String
Length Constraints: Minimum length of 2.
Required: Yes

 ** [ResourceArn](#API_PutResourcePolicy_RequestSyntax) **   <a name="Glue-PutResourcePolicy-request-ResourceArn"></a>
Do not use. For internal use only.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10240.
Pattern: `arn:aws(-(cn|us-gov|iso(-[bef])?))?:glue:.*`
Required: No

## Response Syntax
<a name="API_PutResourcePolicy_ResponseSyntax"></a>

```
{
   "PolicyHash": "string"
}
```

## Response Elements
<a name="API_PutResourcePolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [PolicyHash](#API_PutResourcePolicy_ResponseSyntax) **   <a name="Glue-PutResourcePolicy-response-PolicyHash"></a>
A hash of the policy that has just been set. This must be included in a subsequent call that overwrites or updates this policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`

## Errors
<a name="API_PutResourcePolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConditionCheckFailureException **
A specified condition was not satisfied.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** EntityNotFoundException **
A specified entity does not exist
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** InternalServiceException **
An internal service error occurred.
 ** Message **
A message describing the problem.
HTTP Status Code: 500

 ** InvalidInputException **
The input provided was not valid.
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** OperationTimeoutException **
The operation timed out.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_PutResourcePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/PutResourcePolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/PutResourcePolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/PutResourcePolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/PutResourcePolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/PutResourcePolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/PutResourcePolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/PutResourcePolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/PutResourcePolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/PutResourcePolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/PutResourcePolicy)
