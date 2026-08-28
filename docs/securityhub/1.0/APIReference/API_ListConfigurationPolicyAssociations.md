---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_ListConfigurationPolicyAssociations.html
---

# ListConfigurationPolicyAssociations
<a name="API_ListConfigurationPolicyAssociations"></a>

 Provides information about the associations for your configuration policies and self-managed behavior. Only the AWS Security Hub CSPM delegated administrator can invoke this operation from the home Region.

## Request Syntax
<a name="API_ListConfigurationPolicyAssociations_RequestSyntax"></a>

```
POST /configurationPolicyAssociation/list HTTP/1.1
Content-type: application/json

{
   "Filters": {
      "AssociationStatus": "{{string}}",
      "AssociationType": "{{string}}",
      "ConfigurationPolicyId": "{{string}}"
   },
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListConfigurationPolicyAssociations_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListConfigurationPolicyAssociations_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Filters](#API_ListConfigurationPolicyAssociations_RequestSyntax) **   <a name="securityhub-ListConfigurationPolicyAssociations-request-Filters"></a>
 Options for filtering the `ListConfigurationPolicyAssociations` response. You can filter by the Amazon Resource Name (ARN) or universally unique identifier (UUID) of a configuration, `AssociationType`, or `AssociationStatus`.
Type: [AssociationFilters](API_AssociationFilters.md) object
Required: No

 ** [MaxResults](#API_ListConfigurationPolicyAssociations_RequestSyntax) **   <a name="securityhub-ListConfigurationPolicyAssociations-request-MaxResults"></a>
 The maximum number of results that's returned by `ListConfigurationPolicies` in each page of the response. When this parameter is used, `ListConfigurationPolicyAssociations` returns the specified number of results in a single page and a `NextToken` response element. You can see the remaining results of the initial request by sending another `ListConfigurationPolicyAssociations` request with the returned `NextToken` value. A valid range for `MaxResults` is between 1 and 100.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListConfigurationPolicyAssociations_RequestSyntax) **   <a name="securityhub-ListConfigurationPolicyAssociations-request-NextToken"></a>
 The `NextToken` value that's returned from a previous paginated `ListConfigurationPolicyAssociations` request where `MaxResults` was used but the results exceeded the value of that parameter. Pagination continues from the end of the previous response that returned the `NextToken` value. This value is `null` when there are no more results to return.
Type: String
Required: No

## Response Syntax
<a name="API_ListConfigurationPolicyAssociations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ConfigurationPolicyAssociationSummaries": [
      {
         "AssociationStatus": "string",
         "AssociationStatusMessage": "string",
         "AssociationType": "string",
         "ConfigurationPolicyId": "string",
         "TargetId": "string",
         "TargetType": "string",
         "UpdatedAt": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListConfigurationPolicyAssociations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ConfigurationPolicyAssociationSummaries](#API_ListConfigurationPolicyAssociations_ResponseSyntax) **   <a name="securityhub-ListConfigurationPolicyAssociations-response-ConfigurationPolicyAssociationSummaries"></a>
 An object that contains the details of each configuration policy association that’s returned in a `ListConfigurationPolicyAssociations` request.
Type: Array of [ConfigurationPolicyAssociationSummary](API_ConfigurationPolicyAssociationSummary.md) objects

 ** [NextToken](#API_ListConfigurationPolicyAssociations_ResponseSyntax) **   <a name="securityhub-ListConfigurationPolicyAssociations-response-NextToken"></a>
 The `NextToken` value to include in the next `ListConfigurationPolicyAssociations` request. When the results of a `ListConfigurationPolicyAssociations` request exceed `MaxResults`, this value can be used to retrieve the next page of results. This value is `null` when there are no more results to return.
Type: String

## Errors
<a name="API_ListConfigurationPolicyAssociations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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
<a name="API_ListConfigurationPolicyAssociations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityhub-2018-10-26/ListConfigurationPolicyAssociations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityhub-2018-10-26/ListConfigurationPolicyAssociations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/ListConfigurationPolicyAssociations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityhub-2018-10-26/ListConfigurationPolicyAssociations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/ListConfigurationPolicyAssociations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityhub-2018-10-26/ListConfigurationPolicyAssociations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityhub-2018-10-26/ListConfigurationPolicyAssociations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityhub-2018-10-26/ListConfigurationPolicyAssociations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/securityhub-2018-10-26/ListConfigurationPolicyAssociations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/ListConfigurationPolicyAssociations)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
