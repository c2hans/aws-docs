---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_BatchGetSecurityControls.html
---

# BatchGetSecurityControls
<a name="API_BatchGetSecurityControls"></a>

 Provides details about a batch of security controls for the current AWS account and AWS Region.

## Request Syntax
<a name="API_BatchGetSecurityControls_RequestSyntax"></a>

```
POST /securityControls/batchGet HTTP/1.1
Content-type: application/json

{
   "SecurityControlIds": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_BatchGetSecurityControls_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_BatchGetSecurityControls_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [SecurityControlIds](#API_BatchGetSecurityControls_RequestSyntax) **   <a name="securityhub-BatchGetSecurityControls-request-SecurityControlIds"></a>
 A list of security controls (identified with `SecurityControlId`, `SecurityControlArn`, or a mix of both parameters). The security control ID or Amazon Resource Name (ARN) is the same across standards.
Type: Array of strings
Pattern: `.*\S.*`
Required: Yes

## Response Syntax
<a name="API_BatchGetSecurityControls_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "SecurityControls": [
      {
         "Description": "string",
         "LastUpdateReason": "string",
         "Parameters": {
            "string" : {
               "Value": { ... },
               "ValueType": "string"
            }
         },
         "Provider": "string",
         "RemediationUrl": "string",
         "SecurityControlArn": "string",
         "SecurityControlId": "string",
         "SecurityControlStatus": "string",
         "SeverityRating": "string",
         "Title": "string",
         "UpdateStatus": "string"
      }
   ],
   "UnprocessedIds": [
      {
         "ErrorCode": "string",
         "ErrorReason": "string",
         "SecurityControlId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_BatchGetSecurityControls_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [SecurityControls](#API_BatchGetSecurityControls_ResponseSyntax) **   <a name="securityhub-BatchGetSecurityControls-response-SecurityControls"></a>
 An array that returns the identifier, Amazon Resource Name (ARN), and other details about a security control. The same information is returned whether the request includes `SecurityControlId` or `SecurityControlArn`.
Type: Array of [SecurityControl](API_SecurityControl.md) objects

 ** [UnprocessedIds](#API_BatchGetSecurityControls_ResponseSyntax) **   <a name="securityhub-BatchGetSecurityControls-response-UnprocessedIds"></a>
 A security control (identified with `SecurityControlId`, `SecurityControlArn`, or a mix of both parameters) for which details cannot be returned.
Type: Array of [UnprocessedSecurityControl](API_UnprocessedSecurityControl.md) objects

## Errors
<a name="API_BatchGetSecurityControls_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalException **
Internal server error.
HTTP Status Code: 500

 ** InvalidAccessException **
The account doesn't have permission to perform this action.
HTTP Status Code: 401

 ** InvalidInputException **
The request was rejected because you supplied an invalid or out-of-range value for an input parameter.
HTTP Status Code: 400

 ** LimitExceededException **
The request was rejected because it attempted to create resources beyond the current AWS account or throttling limits. The error code describes the limit exceeded.
HTTP Status Code: 429

## See Also
<a name="API_BatchGetSecurityControls_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityhub-2018-10-26/BatchGetSecurityControls)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityhub-2018-10-26/BatchGetSecurityControls)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/BatchGetSecurityControls)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityhub-2018-10-26/BatchGetSecurityControls)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/BatchGetSecurityControls)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityhub-2018-10-26/BatchGetSecurityControls)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityhub-2018-10-26/BatchGetSecurityControls)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityhub-2018-10-26/BatchGetSecurityControls)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/securityhub-2018-10-26/BatchGetSecurityControls)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/BatchGetSecurityControls)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
