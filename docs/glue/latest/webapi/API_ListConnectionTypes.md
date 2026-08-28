---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_ListConnectionTypes.html
---

# ListConnectionTypes
<a name="API_ListConnectionTypes"></a>

The `ListConnectionTypes` API provides a discovery mechanism to learn available connection types in AWS Glue. The response contains a list of connection types with high-level details of what is supported for each connection type, including both built-in connection types and custom connection types registered via `RegisterConnectionType`. The connection types listed are the set of supported options for the `ConnectionType` value in the `CreateConnection` API.

See also: `DescribeConnectionType`, `RegisterConnectionType`, `DeleteConnectionType`

## Request Syntax
<a name="API_ListConnectionTypes_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListConnectionTypes_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListConnectionTypes_RequestSyntax) **   <a name="Glue-ListConnectionTypes-request-MaxResults"></a>
The maximum number of results to return.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListConnectionTypes_RequestSyntax) **   <a name="Glue-ListConnectionTypes-request-NextToken"></a>
A continuation token, if this is a continuation call.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[-a-zA-Z0-9+=/:_]*`
Required: No

## Response Syntax
<a name="API_ListConnectionTypes_ResponseSyntax"></a>

```
{
   "ConnectionTypes": [
      {
         "Capabilities": {
            "SupportedAuthenticationTypes": [ "string" ],
            "SupportedComputeEnvironments": [ "string" ],
            "SupportedDataOperations": [ "string" ]
         },
         "Categories": [ "string" ],
         "ConnectionType": "string",
         "ConnectionTypeVariants": [
            {
               "ConnectionTypeVariantName": "string",
               "Description": "string",
               "DisplayName": "string",
               "LogoUrl": "string"
            }
         ],
         "Description": "string",
         "DisplayName": "string",
         "LogoUrl": "string",
         "Vendor": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListConnectionTypes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ConnectionTypes](#API_ListConnectionTypes_ResponseSyntax) **   <a name="Glue-ListConnectionTypes-response-ConnectionTypes"></a>
A list of `ConnectionTypeBrief` objects containing brief information about the supported connection types.
Type: Array of [ConnectionTypeBrief](API_ConnectionTypeBrief.md) objects

 ** [NextToken](#API_ListConnectionTypes_ResponseSyntax) **   <a name="Glue-ListConnectionTypes-response-NextToken"></a>
A continuation token, if the current list segment is not the last.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[-a-zA-Z0-9+=/:_]*`

## Errors
<a name="API_ListConnectionTypes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to a resource was denied.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** InternalServiceException **
An internal service error occurred.
 ** Message **
A message describing the problem.
HTTP Status Code: 500

## See Also
<a name="API_ListConnectionTypes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/ListConnectionTypes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/ListConnectionTypes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/ListConnectionTypes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/ListConnectionTypes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/ListConnectionTypes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/ListConnectionTypes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/ListConnectionTypes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/ListConnectionTypes)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/ListConnectionTypes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/ListConnectionTypes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
