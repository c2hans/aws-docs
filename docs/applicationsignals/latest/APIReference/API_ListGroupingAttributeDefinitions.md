---
source_url: https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ListGroupingAttributeDefinitions.html
---

# ListGroupingAttributeDefinitions
<a name="API_ListGroupingAttributeDefinitions"></a>

Returns the current grouping configuration for this account, including all custom grouping attribute definitions that have been configured. These definitions determine how services are logically grouped based on telemetry attributes, AWS tags, or predefined mappings.

## Request Syntax
<a name="API_ListGroupingAttributeDefinitions_RequestSyntax"></a>

```
POST /grouping-attribute-definitions?AwsAccountId={{AwsAccountId}}&IncludeLinkedAccounts={{IncludeLinkedAccounts}}&NextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListGroupingAttributeDefinitions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_ListGroupingAttributeDefinitions_RequestSyntax) **   <a name="applicationsignals-ListGroupingAttributeDefinitions-request-uri-AwsAccountId"></a>
The AWS account ID to retrieve grouping attribute definitions for. Use this when accessing grouping configurations from a different account in cross-account monitoring scenarios.
Pattern: `[0-9]{12}`

 ** [IncludeLinkedAccounts](#API_ListGroupingAttributeDefinitions_RequestSyntax) **   <a name="applicationsignals-ListGroupingAttributeDefinitions-request-uri-IncludeLinkedAccounts"></a>
If you are using this operation in a monitoring account, specify `true` to include grouping attributes from source accounts in the returned data.

 ** [NextToken](#API_ListGroupingAttributeDefinitions_RequestSyntax) **   <a name="applicationsignals-ListGroupingAttributeDefinitions-request-uri-NextToken"></a>
Include this value, if it was returned by the previous operation, to get the next set of grouping attribute definitions.

## Request Body
<a name="API_ListGroupingAttributeDefinitions_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListGroupingAttributeDefinitions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "GroupingAttributeDefinitions": [
      {
         "DefaultGroupingValue": "string",
         "GroupingName": "string",
         "GroupingSourceKeys": [ "string" ]
      }
   ],
   "NextToken": "string",
   "UpdatedAt": number
}
```

## Response Elements
<a name="API_ListGroupingAttributeDefinitions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [GroupingAttributeDefinitions](#API_ListGroupingAttributeDefinitions_ResponseSyntax) **   <a name="applicationsignals-ListGroupingAttributeDefinitions-response-GroupingAttributeDefinitions"></a>
An array of structures, where each structure contains information about one grouping attribute definition, including the grouping name, source keys, and default values.
Type: Array of [GroupingAttributeDefinition](API_GroupingAttributeDefinition.md) objects

 ** [NextToken](#API_ListGroupingAttributeDefinitions_ResponseSyntax) **   <a name="applicationsignals-ListGroupingAttributeDefinitions-response-NextToken"></a>
Include this value in your next use of this API to get the next set of grouping attribute definitions.
Type: String

 ** [UpdatedAt](#API_ListGroupingAttributeDefinitions_ResponseSyntax) **   <a name="applicationsignals-ListGroupingAttributeDefinitions-response-UpdatedAt"></a>
The timestamp when the grouping configuration was last updated. When used in a raw HTTP Query API, it is formatted as epoch time in seconds.
Type: Timestamp

## Errors
<a name="API_ListGroupingAttributeDefinitions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** ThrottlingException **
The request was throttled because of quota limits.
HTTP Status Code: 429

 ** ValidationException **
The resource is not valid.
HTTP Status Code: 400

## See Also
<a name="API_ListGroupingAttributeDefinitions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/application-signals-2024-04-15/ListGroupingAttributeDefinitions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/application-signals-2024-04-15/ListGroupingAttributeDefinitions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-signals-2024-04-15/ListGroupingAttributeDefinitions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/application-signals-2024-04-15/ListGroupingAttributeDefinitions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-signals-2024-04-15/ListGroupingAttributeDefinitions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/application-signals-2024-04-15/ListGroupingAttributeDefinitions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/application-signals-2024-04-15/ListGroupingAttributeDefinitions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/application-signals-2024-04-15/ListGroupingAttributeDefinitions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/application-signals-2024-04-15/ListGroupingAttributeDefinitions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-signals-2024-04-15/ListGroupingAttributeDefinitions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Application Signals. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query applicationsignals` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
