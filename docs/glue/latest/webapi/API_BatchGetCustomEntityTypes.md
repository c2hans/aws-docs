---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_BatchGetCustomEntityTypes.html
---

# BatchGetCustomEntityTypes
<a name="API_BatchGetCustomEntityTypes"></a>

Retrieves the details for the custom patterns specified by a list of names.

## Request Syntax
<a name="API_BatchGetCustomEntityTypes_RequestSyntax"></a>

```
{
   "Names": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_BatchGetCustomEntityTypes_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Names](#API_BatchGetCustomEntityTypes_RequestSyntax) **   <a name="Glue-BatchGetCustomEntityTypes-request-Names"></a>
A list of names of the custom patterns that you want to retrieve.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

## Response Syntax
<a name="API_BatchGetCustomEntityTypes_ResponseSyntax"></a>

```
{
   "CustomEntityTypes": [
      {
         "ContextWords": [ "string" ],
         "Name": "string",
         "RegexString": "string"
      }
   ],
   "CustomEntityTypesNotFound": [ "string" ]
}
```

## Response Elements
<a name="API_BatchGetCustomEntityTypes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CustomEntityTypes](#API_BatchGetCustomEntityTypes_ResponseSyntax) **   <a name="Glue-BatchGetCustomEntityTypes-response-CustomEntityTypes"></a>
A list of `CustomEntityType` objects representing the custom patterns that have been created.
Type: Array of [CustomEntityType](API_CustomEntityType.md) objects

 ** [CustomEntityTypesNotFound](#API_BatchGetCustomEntityTypes_ResponseSyntax) **   <a name="Glue-BatchGetCustomEntityTypes-response-CustomEntityTypesNotFound"></a>
A list of the names of custom patterns that were not found.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`

## Errors
<a name="API_BatchGetCustomEntityTypes_Errors"></a>

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
<a name="API_BatchGetCustomEntityTypes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/BatchGetCustomEntityTypes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/BatchGetCustomEntityTypes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/BatchGetCustomEntityTypes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/BatchGetCustomEntityTypes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/BatchGetCustomEntityTypes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/BatchGetCustomEntityTypes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/BatchGetCustomEntityTypes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/BatchGetCustomEntityTypes)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/BatchGetCustomEntityTypes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/BatchGetCustomEntityTypes)
