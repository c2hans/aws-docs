---
source_url: https://docs.aws.amazon.com/acm/latest/APIReference/API_ListAcmeExternalAccountBindings.html
---

# ListAcmeExternalAccountBindings
<a name="API_ListAcmeExternalAccountBindings"></a>

Retrieves a list of external account bindings for the specified ACME endpoint.

## Request Syntax
<a name="API_ListAcmeExternalAccountBindings_RequestSyntax"></a>

```
{
   "AcmeEndpointArn": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListAcmeExternalAccountBindings_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [AcmeEndpointArn](#API_ListAcmeExternalAccountBindings_RequestSyntax) **   <a name="ACM-ListAcmeExternalAccountBindings-request-AcmeEndpointArn"></a>
The Amazon Resource Name (ARN) of the ACME endpoint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `arn:aws[a-z-]*:acm:[a-z0-9-]+:[0-9]{12}:acme-endpoint/[a-zA-Z0-9-]+`
Required: Yes

 ** [MaxResults](#API_ListAcmeExternalAccountBindings_RequestSyntax) **   <a name="ACM-ListAcmeExternalAccountBindings-request-MaxResults"></a>
The maximum number of results to return.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListAcmeExternalAccountBindings_RequestSyntax) **   <a name="ACM-ListAcmeExternalAccountBindings-request-NextToken"></a>
A token for pagination.
Type: String
Required: No

## Response Syntax
<a name="API_ListAcmeExternalAccountBindings_ResponseSyntax"></a>

```
{
   "ExternalAccountBindings": [
      {
         "AcmeEndpointArn": "string",
         "AcmeExternalAccountBindingArn": "string",
         "CreatedAt": number,
         "ExpiresAt": number,
         "LastUsedAt": number,
         "RevokedAt": number,
         "RoleArn": "string",
         "UpdatedAt": number
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListAcmeExternalAccountBindings_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ExternalAccountBindings](#API_ListAcmeExternalAccountBindings_ResponseSyntax) **   <a name="ACM-ListAcmeExternalAccountBindings-response-ExternalAccountBindings"></a>
The list of external account bindings.
Type: Array of [AcmeExternalAccountBindingSummary](API_AcmeExternalAccountBindingSummary.md) objects

 ** [NextToken](#API_ListAcmeExternalAccountBindings_ResponseSyntax) **   <a name="ACM-ListAcmeExternalAccountBindings-response-NextToken"></a>
A token for pagination.
Type: String

## Errors
<a name="API_ListAcmeExternalAccountBindings_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have access required to perform this action.
HTTP Status Code: 400

 ** InternalServerException **
The request processing has failed because of an unknown error, exception, or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified certificate cannot be found in the caller's account or the caller's account cannot be found.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied because it exceeded a quota.
 ** throttlingReasons **
One or more reasons why the request was throttled.
HTTP Status Code: 400

 ** ValidationException **
The supplied input failed to satisfy constraints of an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_ListAcmeExternalAccountBindings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/acm-2015-12-08/ListAcmeExternalAccountBindings)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/acm-2015-12-08/ListAcmeExternalAccountBindings)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-2015-12-08/ListAcmeExternalAccountBindings)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/acm-2015-12-08/ListAcmeExternalAccountBindings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-2015-12-08/ListAcmeExternalAccountBindings)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/acm-2015-12-08/ListAcmeExternalAccountBindings)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/acm-2015-12-08/ListAcmeExternalAccountBindings)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/acm-2015-12-08/ListAcmeExternalAccountBindings)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/acm-2015-12-08/ListAcmeExternalAccountBindings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-2015-12-08/ListAcmeExternalAccountBindings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for ACM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query acm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
