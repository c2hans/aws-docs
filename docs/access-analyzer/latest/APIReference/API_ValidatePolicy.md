---
source_url: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_ValidatePolicy.html
---

# ValidatePolicy
<a name="API_ValidatePolicy"></a>

Requests the validation of a policy and returns a list of findings. The findings help you identify issues and provide actionable recommendations to resolve the issue and enable you to author functional policies that meet security best practices.

## Request Syntax
<a name="API_ValidatePolicy_RequestSyntax"></a>

```
POST /policy/validation?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
Content-type: application/json

{
   "locale": "{{string}}",
   "policyDocument": "{{string}}",
   "policyType": "{{string}}",
   "validatePolicyResourceType": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ValidatePolicy_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ValidatePolicy_RequestSyntax) **   <a name="accessanalyzer-ValidatePolicy-request-uri-maxResults"></a>
The maximum number of results to return in the response.

 ** [nextToken](#API_ValidatePolicy_RequestSyntax) **   <a name="accessanalyzer-ValidatePolicy-request-uri-nextToken"></a>
A token used for pagination of results returned.

## Request Body
<a name="API_ValidatePolicy_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [locale](#API_ValidatePolicy_RequestSyntax) **   <a name="accessanalyzer-ValidatePolicy-request-locale"></a>
The locale to use for localizing the findings.
Type: String
Valid Values: `DE | EN | ES | FR | IT | JA | KO | PT_BR | ZH_CN | ZH_TW`
Required: No

 ** [policyDocument](#API_ValidatePolicy_RequestSyntax) **   <a name="accessanalyzer-ValidatePolicy-request-policyDocument"></a>
The JSON policy document to use as the content for the policy.
Type: String
Required: Yes

 ** [policyType](#API_ValidatePolicy_RequestSyntax) **   <a name="accessanalyzer-ValidatePolicy-request-policyType"></a>
The type of policy to validate. Identity policies grant permissions to IAM principals. Identity policies include managed and inline policies for IAM roles, users, and groups.
Resource policies grant permissions on AWS resources. Resource policies include trust policies for IAM roles and bucket policies for Amazon S3 buckets. You can provide a generic input such as identity policy or resource policy or a specific input such as managed policy or Amazon S3 bucket policy.
Service control policies (SCPs) are a type of organization policy attached to an AWS organization, organizational unit (OU), or an account.
Type: String
Valid Values: `IDENTITY_POLICY | RESOURCE_POLICY | SERVICE_CONTROL_POLICY | RESOURCE_CONTROL_POLICY`
Required: Yes

 ** [validatePolicyResourceType](#API_ValidatePolicy_RequestSyntax) **   <a name="accessanalyzer-ValidatePolicy-request-validatePolicyResourceType"></a>
The type of resource to attach to your resource policy. Specify a value for the policy validation resource type only if the policy type is `RESOURCE_POLICY`. For example, to validate a resource policy to attach to an Amazon S3 bucket, you can choose `AWS::S3::Bucket` for the policy validation resource type.
For resource types not supported as valid values, IAM Access Analyzer runs policy checks that apply to all resource policies. For example, to validate a resource policy to attach to a KMS key, do not specify a value for the policy validation resource type and IAM Access Analyzer will run policy checks that apply to all resource policies.
Type: String
Valid Values: `AWS::S3::Bucket | AWS::S3::AccessPoint | AWS::S3::MultiRegionAccessPoint | AWS::S3ObjectLambda::AccessPoint | AWS::IAM::AssumeRolePolicyDocument | AWS::DynamoDB::Table`
Required: No

## Response Syntax
<a name="API_ValidatePolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "findings": [
      {
         "findingDetails": "string",
         "findingType": "string",
         "issueCode": "string",
         "learnMoreLink": "string",
         "locations": [
            {
               "path": [
                  { ... }
               ],
               "span": {
                  "end": {
                     "column": number,
                     "line": number,
                     "offset": number
                  },
                  "start": {
                     "column": number,
                     "line": number,
                     "offset": number
                  }
               }
            }
         ]
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ValidatePolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [findings](#API_ValidatePolicy_ResponseSyntax) **   <a name="accessanalyzer-ValidatePolicy-response-findings"></a>
The list of findings in a policy returned by IAM Access Analyzer based on its suite of policy checks.
Type: Array of [ValidatePolicyFinding](API_ValidatePolicyFinding.md) objects

 ** [nextToken](#API_ValidatePolicy_ResponseSyntax) **   <a name="accessanalyzer-ValidatePolicy-response-nextToken"></a>
A token used for pagination of results returned.
Type: String

## Errors
<a name="API_ValidatePolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
Internal server error.
 ** retryAfterSeconds **
The seconds to wait to retry.
HTTP Status Code: 500

 ** ThrottlingException **
Throttling limit exceeded error.
 ** retryAfterSeconds **
The seconds to wait to retry.
HTTP Status Code: 429

 ** ValidationException **
Validation exception error.
 ** fieldList **
A list of fields that didn't validate.
 ** reason **
The reason for the exception.
HTTP Status Code: 400

## See Also
<a name="API_ValidatePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/accessanalyzer-2019-11-01/ValidatePolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/accessanalyzer-2019-11-01/ValidatePolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/ValidatePolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/accessanalyzer-2019-11-01/ValidatePolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/ValidatePolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/accessanalyzer-2019-11-01/ValidatePolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/accessanalyzer-2019-11-01/ValidatePolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/accessanalyzer-2019-11-01/ValidatePolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/accessanalyzer-2019-11-01/ValidatePolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/ValidatePolicy)
