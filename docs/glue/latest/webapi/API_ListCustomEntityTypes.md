---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_ListCustomEntityTypes.html
---

# ListCustomEntityTypes
<a name="API_ListCustomEntityTypes"></a>

Lists all the custom patterns that have been created.

## Request Syntax
<a name="API_ListCustomEntityTypes_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## Request Parameters
<a name="API_ListCustomEntityTypes_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListCustomEntityTypes_RequestSyntax) **   <a name="Glue-ListCustomEntityTypes-request-MaxResults"></a>
The maximum number of results to return.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [NextToken](#API_ListCustomEntityTypes_RequestSyntax) **   <a name="Glue-ListCustomEntityTypes-request-NextToken"></a>
A paginated token to offset the results.
Type: String
Required: No

 ** [Tags](#API_ListCustomEntityTypes_RequestSyntax) **   <a name="Glue-ListCustomEntityTypes-request-Tags"></a>
A list of key-value pair tags.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_ListCustomEntityTypes_ResponseSyntax"></a>

```
{
   "CustomEntityTypes": [
      {
         "ContextWords": [ "string" ],
         "Name": "string",
         "RegexString": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListCustomEntityTypes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CustomEntityTypes](#API_ListCustomEntityTypes_ResponseSyntax) **   <a name="Glue-ListCustomEntityTypes-response-CustomEntityTypes"></a>
A list of `CustomEntityType` objects representing custom patterns.
Type: Array of [CustomEntityType](API_CustomEntityType.md) objects

 ** [NextToken](#API_ListCustomEntityTypes_ResponseSyntax) **   <a name="Glue-ListCustomEntityTypes-response-NextToken"></a>
A pagination token, if more results are available.
Type: String

## Errors
<a name="API_ListCustomEntityTypes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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
<a name="API_ListCustomEntityTypes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/ListCustomEntityTypes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/ListCustomEntityTypes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/ListCustomEntityTypes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/ListCustomEntityTypes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/ListCustomEntityTypes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/ListCustomEntityTypes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/ListCustomEntityTypes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/ListCustomEntityTypes)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/ListCustomEntityTypes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/ListCustomEntityTypes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
