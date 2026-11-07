---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_ListGlossaries.html
---

# ListGlossaries
<a name="API_ListGlossaries"></a>

Lists business glossaries in AWS Glue Data Catalog.

## Request Syntax
<a name="API_ListGlossaries_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListGlossaries_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListGlossaries_RequestSyntax) **   <a name="Glue-ListGlossaries-request-MaxResults"></a>
The maximum number of results to return in the response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [NextToken](#API_ListGlossaries_RequestSyntax) **   <a name="Glue-ListGlossaries-request-NextToken"></a>
A continuation token, if this is a continuation call.
Type: String
Required: No

## Response Syntax
<a name="API_ListGlossaries_ResponseSyntax"></a>

```
{
   "Items": [
      {
         "Description": "string",
         "Id": "string",
         "Name": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListGlossaries_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Items](#API_ListGlossaries_ResponseSyntax) **   <a name="Glue-ListGlossaries-response-Items"></a>
The list of glossary items.
Type: Array of [GlossaryItem](API_GlossaryItem.md) objects

 ** [NextToken](#API_ListGlossaries_ResponseSyntax) **   <a name="Glue-ListGlossaries-response-NextToken"></a>
A continuation token, present if the current segment is not the last.
Type: String

## Errors
<a name="API_ListGlossaries_Errors"></a>

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

 ** InvalidInputException **
The input provided was not valid.
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** ThrottlingException **
The throttling threshhold was exceeded.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## Examples
<a name="API_ListGlossaries_Examples"></a>

### Example
<a name="API_ListGlossaries_Example_1"></a>

The following example lists the glossaries in the account.

```
aws glue list-glossaries --max-results 20

{
    "Items": [
        {
            "Id": "6n5f21s641nbjb",
            "Name": "Sales Terms",
            "Description": "Glossary of sales and revenue business terms"
        }
    ]
}
```

## See Also
<a name="API_ListGlossaries_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/ListGlossaries)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/ListGlossaries)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/ListGlossaries)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/ListGlossaries)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/ListGlossaries)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/ListGlossaries)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/ListGlossaries)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/ListGlossaries)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/ListGlossaries)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/ListGlossaries)
