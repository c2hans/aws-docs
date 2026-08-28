---
source_url: https://docs.aws.amazon.com/acm/latest/APIReference/API_ListAcmeEndpoints.html
---

# ListAcmeEndpoints
<a name="API_ListAcmeEndpoints"></a>

Retrieves a list of ACME endpoints in your account. Use this operation to view all configured ACME endpoints and their current status.

## Request Syntax
<a name="API_ListAcmeEndpoints_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListAcmeEndpoints_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [MaxResults](#API_ListAcmeEndpoints_RequestSyntax) **   <a name="ACM-ListAcmeEndpoints-request-MaxResults"></a>
The maximum number of results to return.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListAcmeEndpoints_RequestSyntax) **   <a name="ACM-ListAcmeEndpoints-request-NextToken"></a>
A token for pagination.
Type: String
Required: No

## Response Syntax
<a name="API_ListAcmeEndpoints_ResponseSyntax"></a>

```
{
   "AcmeEndpoints": [
      {
         "AcmeEndpointArn": "string",
         "AuthorizationBehavior": "string",
         "CertificateAuthority": { ... },
         "CertificateTags": [
            {
               "Key": "string",
               "Value": "string"
            }
         ],
         "Contact": "string",
         "CreatedAt": number,
         "EndpointUrl": "string",
         "FailureReason": "string",
         "Status": "string",
         "UpdatedAt": number
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListAcmeEndpoints_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AcmeEndpoints](#API_ListAcmeEndpoints_ResponseSyntax) **   <a name="ACM-ListAcmeEndpoints-response-AcmeEndpoints"></a>
The list of ACME endpoints.
Type: Array of [AcmeEndpointSummary](API_AcmeEndpointSummary.md) objects

 ** [NextToken](#API_ListAcmeEndpoints_ResponseSyntax) **   <a name="ACM-ListAcmeEndpoints-response-NextToken"></a>
A token for pagination.
Type: String

## Errors
<a name="API_ListAcmeEndpoints_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have access required to perform this action.
HTTP Status Code: 400

 ** InternalServerException **
The request processing has failed because of an unknown error, exception, or failure.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied because it exceeded a quota.
 ** throttlingReasons **
One or more reasons why the request was throttled.
HTTP Status Code: 400

 ** ValidationException **
The supplied input failed to satisfy constraints of an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_ListAcmeEndpoints_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/acm-2015-12-08/ListAcmeEndpoints)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/acm-2015-12-08/ListAcmeEndpoints)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-2015-12-08/ListAcmeEndpoints)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/acm-2015-12-08/ListAcmeEndpoints)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-2015-12-08/ListAcmeEndpoints)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/acm-2015-12-08/ListAcmeEndpoints)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/acm-2015-12-08/ListAcmeEndpoints)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/acm-2015-12-08/ListAcmeEndpoints)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/acm-2015-12-08/ListAcmeEndpoints)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-2015-12-08/ListAcmeEndpoints)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for ACM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query acm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
