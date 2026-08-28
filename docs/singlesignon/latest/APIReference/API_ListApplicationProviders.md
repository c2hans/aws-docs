---
source_url: https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListApplicationProviders.html
---

# ListApplicationProviders
<a name="API_ListApplicationProviders"></a>

Lists the application providers configured in the IAM Identity Center identity store.

## Request Syntax
<a name="API_ListApplicationProviders_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListApplicationProviders_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListApplicationProviders_RequestSyntax) **   <a name="singlesignon-ListApplicationProviders-request-MaxResults"></a>
Specifies the total number of results that you want included in each response. If additional items exist beyond the number you specify, the `NextToken` response element is returned with a value (not null). Include the specified value as the `NextToken` request parameter in the next call to the operation to get the next set of results. Note that the service might return fewer results than the maximum even when there are more results available. You should check `NextToken` after every operation to ensure that you receive all of the results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListApplicationProviders_RequestSyntax) **   <a name="singlesignon-ListApplicationProviders-request-NextToken"></a>
Specifies that you want to receive the next page of results. Valid only if you received a `NextToken` response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's `NextToken` response to request the next page of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[-a-zA-Z0-9+=/_]*`
Required: No

## Response Syntax
<a name="API_ListApplicationProviders_ResponseSyntax"></a>

```
{
   "ApplicationProviders": [
      {
         "ApplicationProviderArn": "string",
         "DisplayData": {
            "Description": "string",
            "DisplayName": "string",
            "IconUrl": "string"
         },
         "FederationProtocol": "string",
         "ResourceServerConfig": {
            "Scopes": {
               "string" : {
                  "DetailedTitle": "string",
                  "LongDescription": "string"
               }
            }
         }
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListApplicationProviders_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ApplicationProviders](#API_ListApplicationProviders_ResponseSyntax) **   <a name="singlesignon-ListApplicationProviders-response-ApplicationProviders"></a>
An array list of structures that describe application providers.
Type: Array of [ApplicationProvider](API_ApplicationProvider.md) objects

 ** [NextToken](#API_ListApplicationProviders_ResponseSyntax) **   <a name="singlesignon-ListApplicationProviders-response-NextToken"></a>
If present, this value indicates that more output is available than is included in the current response. Use this value in the `NextToken` request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the `NextToken` response element comes back as `null`. This indicates that this is the last page of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[-a-zA-Z0-9+=/_]*`

## Errors
<a name="API_ListApplicationProviders_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
 ** Reason **
The reason for the access denied exception.
HTTP Status Code: 400

 ** InternalServerException **
The request processing has failed because of an unknown error, exception, or failure with an internal server.
HTTP Status Code: 500

 ** ThrottlingException **
Indicates that the principal has crossed the throttling limits of the API operations.
 ** Reason **
The reason for the throttling exception.
HTTP Status Code: 400

 ** ValidationException **
The request failed because it contains a syntax error.
 ** Reason **
The reason for the validation exception.
HTTP Status Code: 400

## See Also
<a name="API_ListApplicationProviders_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sso-admin-2020-07-20/ListApplicationProviders)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sso-admin-2020-07-20/ListApplicationProviders)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sso-admin-2020-07-20/ListApplicationProviders)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sso-admin-2020-07-20/ListApplicationProviders)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sso-admin-2020-07-20/ListApplicationProviders)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sso-admin-2020-07-20/ListApplicationProviders)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sso-admin-2020-07-20/ListApplicationProviders)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sso-admin-2020-07-20/ListApplicationProviders)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sso-admin-2020-07-20/ListApplicationProviders)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sso-admin-2020-07-20/ListApplicationProviders)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for IAM Identity Center API Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query singlesignon` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
