---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_CreateCustomEntityType.html
---

# CreateCustomEntityType
<a name="API_CreateCustomEntityType"></a>

Creates a custom pattern that is used to detect sensitive data across the columns and rows of your structured data.

Each custom pattern you create specifies a regular expression and an optional list of context words. If no context words are passed only a regular expression is checked.

## Request Syntax
<a name="API_CreateCustomEntityType_RequestSyntax"></a>

```
{
   "ContextWords": [ "{{string}}" ],
   "Name": "{{string}}",
   "RegexString": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## Request Parameters
<a name="API_CreateCustomEntityType_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ContextWords](#API_CreateCustomEntityType_RequestSyntax) **   <a name="Glue-CreateCustomEntityType-request-ContextWords"></a>
A list of context words. If none of these context words are found within the vicinity of the regular expression the data will not be detected as sensitive data.
If no context words are passed only a regular expression is checked.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [Name](#API_CreateCustomEntityType_RequestSyntax) **   <a name="Glue-CreateCustomEntityType-request-Name"></a>
A name for the custom pattern that allows it to be retrieved or deleted later. This name must be unique per AWS account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** [RegexString](#API_CreateCustomEntityType_RequestSyntax) **   <a name="Glue-CreateCustomEntityType-request-RegexString"></a>
A regular expression string that is used for detecting sensitive data in a custom pattern.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** [Tags](#API_CreateCustomEntityType_RequestSyntax) **   <a name="Glue-CreateCustomEntityType-request-Tags"></a>
A list of tags applied to the custom entity type.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateCustomEntityType_ResponseSyntax"></a>

```
{
   "Name": "string"
}
```

## Response Elements
<a name="API_CreateCustomEntityType_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Name](#API_CreateCustomEntityType_ResponseSyntax) **   <a name="Glue-CreateCustomEntityType-response-Name"></a>
The name of the custom pattern you created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`

## Errors
<a name="API_CreateCustomEntityType_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to a resource was denied.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** AlreadyExistsException **
A resource to be created or added already exists.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** IdempotentParameterMismatchException **
The same unique identifier was associated with two different records.
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

 ** OperationTimeoutException **
The operation timed out.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** ResourceNumberLimitExceededException **
A resource numerical limit was exceeded.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_CreateCustomEntityType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/CreateCustomEntityType)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/CreateCustomEntityType)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/CreateCustomEntityType)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/CreateCustomEntityType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/CreateCustomEntityType)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/CreateCustomEntityType)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/CreateCustomEntityType)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/CreateCustomEntityType)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/CreateCustomEntityType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/CreateCustomEntityType)
