---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_ListConfigurationPolicies.html
---

# ListConfigurationPolicies
<a name="API_ListConfigurationPolicies"></a>

 Lists the configuration policies that the AWS Security Hub CSPM delegated administrator has created for your organization. Only the delegated administrator can invoke this operation from the home Region.

## Request Syntax
<a name="API_ListConfigurationPolicies_RequestSyntax"></a>

```
GET /configurationPolicy/list?MaxResults={{MaxResults}}&NextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListConfigurationPolicies_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_ListConfigurationPolicies_RequestSyntax) **   <a name="securityhub-ListConfigurationPolicies-request-uri-MaxResults"></a>
 The maximum number of results that's returned by `ListConfigurationPolicies` in each page of the response. When this parameter is used, `ListConfigurationPolicies` returns the specified number of results in a single page and a `NextToken` response element. You can see the remaining results of the initial request by sending another `ListConfigurationPolicies` request with the returned `NextToken` value. A valid range for `MaxResults` is between 1 and 100.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_ListConfigurationPolicies_RequestSyntax) **   <a name="securityhub-ListConfigurationPolicies-request-uri-NextToken"></a>
 The NextToken value that's returned from a previous paginated `ListConfigurationPolicies` request where `MaxResults` was used but the results exceeded the value of that parameter. Pagination continues from the `MaxResults` was used but the results exceeded the value of that parameter. Pagination continues from the end of the previous response that returned the `NextToken` value. This value is `null` when there are no more results to return.

## Request Body
<a name="API_ListConfigurationPolicies_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListConfigurationPolicies_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ConfigurationPolicySummaries": [
      {
         "Arn": "string",
         "Description": "string",
         "Id": "string",
         "Name": "string",
         "ServiceEnabled": boolean,
         "UpdatedAt": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListConfigurationPolicies_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ConfigurationPolicySummaries](#API_ListConfigurationPolicies_ResponseSyntax) **   <a name="securityhub-ListConfigurationPolicies-response-ConfigurationPolicySummaries"></a>
 Provides metadata for each of your configuration policies.
Type: Array of [ConfigurationPolicySummary](API_ConfigurationPolicySummary.md) objects

 ** [NextToken](#API_ListConfigurationPolicies_ResponseSyntax) **   <a name="securityhub-ListConfigurationPolicies-response-NextToken"></a>
 The `NextToken` value to include in the next `ListConfigurationPolicies` request. When the results of a `ListConfigurationPolicies` request exceed `MaxResults`, this value can be used to retrieve the next page of results. This value is `null` when there are no more results to return.
Type: String

## Errors
<a name="API_ListConfigurationPolicies_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permission to perform the action specified in the request.
HTTP Status Code: 403

 ** AccessDeniedException **
You don't have permission to perform the action specified in the request.
HTTP Status Code: 403

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
<a name="API_ListConfigurationPolicies_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityhub-2018-10-26/ListConfigurationPolicies)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityhub-2018-10-26/ListConfigurationPolicies)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/ListConfigurationPolicies)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityhub-2018-10-26/ListConfigurationPolicies)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/ListConfigurationPolicies)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityhub-2018-10-26/ListConfigurationPolicies)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityhub-2018-10-26/ListConfigurationPolicies)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityhub-2018-10-26/ListConfigurationPolicies)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/securityhub-2018-10-26/ListConfigurationPolicies)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/ListConfigurationPolicies)
