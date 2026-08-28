---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_SearchEmailAddresses.html
---

# SearchEmailAddresses
<a name="API_SearchEmailAddresses"></a>

Searches email address in an instance, with optional filtering.

## Request Syntax
<a name="API_SearchEmailAddresses_RequestSyntax"></a>

```
POST /search-email-addresses HTTP/1.1
Content-type: application/json

{
   "InstanceId": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "SearchCriteria": {
      "AndConditions": [
         "EmailAddressSearchCriteria"
      ],
      "OrConditions": [
         "EmailAddressSearchCriteria"
      ],
      "StringCondition": {
         "ComparisonType": "{{string}}",
         "FieldName": "{{string}}",
         "Value": "{{string}}"
      }
   },
   "SearchFilter": {
      "TagFilter": {
         "AndConditions": [
            {
               "TagKey": "{{string}}",
               "TagValue": "{{string}}"
            }
         ],
         "OrConditions": [
            [
               {
                  "TagKey": "{{string}}",
                  "TagValue": "{{string}}"
               }
            ]
         ],
         "TagCondition": {
            "TagKey": "{{string}}",
            "TagValue": "{{string}}"
         }
      }
   }
}
```

## URI Request Parameters
<a name="API_SearchEmailAddresses_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_SearchEmailAddresses_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [InstanceId](#API_SearchEmailAddresses_RequestSyntax) **   <a name="connect-SearchEmailAddresses-request-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [MaxResults](#API_SearchEmailAddresses_RequestSyntax) **   <a name="connect-SearchEmailAddresses-request-MaxResults"></a>
The maximum number of results to return per page.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_SearchEmailAddresses_RequestSyntax) **   <a name="connect-SearchEmailAddresses-request-NextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2500.
Required: No

 ** [SearchCriteria](#API_SearchEmailAddresses_RequestSyntax) **   <a name="connect-SearchEmailAddresses-request-SearchCriteria"></a>
The search criteria to be used to return email addresses.
Type: [EmailAddressSearchCriteria](API_EmailAddressSearchCriteria.md) object
Required: No

 ** [SearchFilter](#API_SearchEmailAddresses_RequestSyntax) **   <a name="connect-SearchEmailAddresses-request-SearchFilter"></a>
Filters to be applied to search results.
Type: [EmailAddressSearchFilter](API_EmailAddressSearchFilter.md) object
Required: No

## Response Syntax
<a name="API_SearchEmailAddresses_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ApproximateTotalCount": number,
   "EmailAddresses": [
      {
         "AliasConfigurations": [
            {
               "EmailAddressId": "string"
            }
         ],
         "Description": "string",
         "DisplayName": "string",
         "EmailAddress": "string",
         "EmailAddressArn": "string",
         "EmailAddressId": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_SearchEmailAddresses_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ApproximateTotalCount](#API_SearchEmailAddresses_ResponseSyntax) **   <a name="connect-SearchEmailAddresses-response-ApproximateTotalCount"></a>
The total number of email addresses which matched your search query.
Type: Long

 ** [EmailAddresses](#API_SearchEmailAddresses_ResponseSyntax) **   <a name="connect-SearchEmailAddresses-response-EmailAddresses"></a>
List of email addresses matching SearchFilter and SearchCriteria
Type: Array of [EmailAddressMetadata](API_EmailAddressMetadata.md) objects

 ** [NextToken](#API_SearchEmailAddresses_ResponseSyntax) **   <a name="connect-SearchEmailAddresses-response-NextToken"></a>
If there are additional results, this is the token for the next set of results.
Type: String

## Errors
<a name="API_SearchEmailAddresses_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidParameterException **
One or more of the specified parameters are not valid.
 ** Message **
The message about the parameters.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is not valid.
 ** Message **
The message about the request.
 ** Reason **
Reason why the request was invalid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_SearchEmailAddresses_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/SearchEmailAddresses)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/SearchEmailAddresses)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/SearchEmailAddresses)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/SearchEmailAddresses)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/SearchEmailAddresses)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/SearchEmailAddresses)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/SearchEmailAddresses)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/SearchEmailAddresses)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/SearchEmailAddresses)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/SearchEmailAddresses)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
