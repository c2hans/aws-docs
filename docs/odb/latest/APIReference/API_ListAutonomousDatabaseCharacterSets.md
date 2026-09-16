---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_ListAutonomousDatabaseCharacterSets.html
---

# ListAutonomousDatabaseCharacterSets
<a name="API_ListAutonomousDatabaseCharacterSets"></a>

Lists the available character sets for Autonomous Databases.

## Request Syntax
<a name="API_ListAutonomousDatabaseCharacterSets_RequestSyntax"></a>

```
{
   "characterSetType": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListAutonomousDatabaseCharacterSets_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [characterSetType](#API_ListAutonomousDatabaseCharacterSets_RequestSyntax) **   <a name="odb-ListAutonomousDatabaseCharacterSets-request-characterSetType"></a>
The type of character set to return results for, either the database character set or the national character set.
Type: String
Valid Values: `DATABASE | NATIONAL`
Required: No

 ** [maxResults](#API_ListAutonomousDatabaseCharacterSets_RequestSyntax) **   <a name="odb-ListAutonomousDatabaseCharacterSets-request-maxResults"></a>
The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [nextToken](#API_ListAutonomousDatabaseCharacterSets_RequestSyntax) **   <a name="odb-ListAutonomousDatabaseCharacterSets-request-nextToken"></a>
The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Required: No

## Response Syntax
<a name="API_ListAutonomousDatabaseCharacterSets_ResponseSyntax"></a>

```
{
   "autonomousDatabaseCharacterSets": [
      {
         "characterSet": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListAutonomousDatabaseCharacterSets_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [autonomousDatabaseCharacterSets](#API_ListAutonomousDatabaseCharacterSets_ResponseSyntax) **   <a name="odb-ListAutonomousDatabaseCharacterSets-response-autonomousDatabaseCharacterSets"></a>
The list of available Autonomous Database character sets.
Type: Array of [AutonomousDatabaseCharacterSetSummary](API_AutonomousDatabaseCharacterSetSummary.md) objects

 ** [nextToken](#API_ListAutonomousDatabaseCharacterSets_ResponseSyntax) **   <a name="odb-ListAutonomousDatabaseCharacterSets-response-nextToken"></a>
The token to include in another request to get the next page of items. This value is `null` when there are no more items to return.
Type: String

## Errors
<a name="API_ListAutonomousDatabaseCharacterSets_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.
HTTP Status Code: 400

 ** InternalServerException **
Occurs when there is an internal failure in the Oracle Database@AWS service. Wait and try again.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request after an internal server error.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request after being throttled.
HTTP Status Code: 400

 ** ValidationException **
The request has failed validation because it is missing required fields or has invalid inputs.
 ** fieldList **
A list of fields that failed validation.
 ** reason **
The reason why the validation failed.
HTTP Status Code: 400

## See Also
<a name="API_ListAutonomousDatabaseCharacterSets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/odb-2024-08-20/ListAutonomousDatabaseCharacterSets)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/odb-2024-08-20/ListAutonomousDatabaseCharacterSets)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/ListAutonomousDatabaseCharacterSets)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/odb-2024-08-20/ListAutonomousDatabaseCharacterSets)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/ListAutonomousDatabaseCharacterSets)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/odb-2024-08-20/ListAutonomousDatabaseCharacterSets)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/odb-2024-08-20/ListAutonomousDatabaseCharacterSets)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/odb-2024-08-20/ListAutonomousDatabaseCharacterSets)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/odb-2024-08-20/ListAutonomousDatabaseCharacterSets)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/ListAutonomousDatabaseCharacterSets)
