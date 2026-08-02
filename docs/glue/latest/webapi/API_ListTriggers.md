---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_ListTriggers.html
---

# ListTriggers
<a name="API_ListTriggers"></a>

Retrieves the names of all trigger resources in this AWS account, or the resources with the specified tag. This operation allows you to see which resources are available in your account, and their names.

This operation takes the optional `Tags` field, which you can use as a filter on the response so that tagged resources can be retrieved as a group. If you choose to use tags filtering, only resources with the tag are retrieved.

## Request Syntax
<a name="API_ListTriggers_RequestSyntax"></a>

```
{
   "DependentJobName": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## Request Parameters
<a name="API_ListTriggers_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DependentJobName](#API_ListTriggers_RequestSyntax) **   <a name="Glue-ListTriggers-request-DependentJobName"></a>
 The name of the job for which to retrieve triggers. The trigger that can start this job is returned. If there is no such trigger, all triggers are returned.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [MaxResults](#API_ListTriggers_RequestSyntax) **   <a name="Glue-ListTriggers-request-MaxResults"></a>
The maximum size of a list to return.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 200.
Required: No

 ** [NextToken](#API_ListTriggers_RequestSyntax) **   <a name="Glue-ListTriggers-request-NextToken"></a>
A continuation token, if this is a continuation request.
Type: String
Required: No

 ** [Tags](#API_ListTriggers_RequestSyntax) **   <a name="Glue-ListTriggers-request-Tags"></a>
Specifies to return only these tagged resources.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_ListTriggers_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "TriggerNames": [ "string" ]
}
```

## Response Elements
<a name="API_ListTriggers_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListTriggers_ResponseSyntax) **   <a name="Glue-ListTriggers-response-NextToken"></a>
A continuation token, if the returned list does not contain the last metric available.
Type: String

 ** [TriggerNames](#API_ListTriggers_ResponseSyntax) **   <a name="Glue-ListTriggers-response-TriggerNames"></a>
The names of all triggers in the account, or the triggers with the specified tags.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`

## Errors
<a name="API_ListTriggers_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** EntityNotFoundException **
A specified entity does not exist
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
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

## See Also
<a name="API_ListTriggers_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/ListTriggers)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/ListTriggers)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/ListTriggers)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/ListTriggers)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/ListTriggers)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/ListTriggers)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/ListTriggers)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/ListTriggers)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/ListTriggers)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/ListTriggers)
