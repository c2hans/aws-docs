---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_ListUsageProfiles.html
---

# ListUsageProfiles
<a name="API_ListUsageProfiles"></a>

List all the AWS Glue usage profiles.

## Request Syntax
<a name="API_ListUsageProfiles_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListUsageProfiles_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListUsageProfiles_RequestSyntax) **   <a name="Glue-ListUsageProfiles-request-MaxResults"></a>
The maximum number of usage profiles to return in a single response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 200.
Required: No

 ** [NextToken](#API_ListUsageProfiles_RequestSyntax) **   <a name="Glue-ListUsageProfiles-request-NextToken"></a>
A continuation token, included if this is a continuation call.
Type: String
Length Constraints: Maximum length of 400000.
Required: No

## Response Syntax
<a name="API_ListUsageProfiles_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "Profiles": [
      {
         "CreatedOn": number,
         "Description": "string",
         "LastModifiedOn": number,
         "Name": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListUsageProfiles_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListUsageProfiles_ResponseSyntax) **   <a name="Glue-ListUsageProfiles-response-NextToken"></a>
A continuation token, present if the current list segment is not the last.
Type: String
Length Constraints: Maximum length of 400000.

 ** [Profiles](#API_ListUsageProfiles_ResponseSyntax) **   <a name="Glue-ListUsageProfiles-response-Profiles"></a>
A list of usage profile (`UsageProfileDefinition`) objects.
Type: Array of [UsageProfileDefinition](API_UsageProfileDefinition.md) objects

## Errors
<a name="API_ListUsageProfiles_Errors"></a>

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

 ** OperationNotSupportedException **
The operation is not available in the region.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** OperationTimeoutException **
The operation timed out.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_ListUsageProfiles_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/ListUsageProfiles)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/ListUsageProfiles)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/ListUsageProfiles)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/ListUsageProfiles)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/ListUsageProfiles)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/ListUsageProfiles)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/ListUsageProfiles)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/ListUsageProfiles)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/ListUsageProfiles)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/ListUsageProfiles)
