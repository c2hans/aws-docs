---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_SearchContactFlowModules.html
---

# SearchContactFlowModules
<a name="API_SearchContactFlowModules"></a>

Searches the flow modules in an Connect Customer instance, with optional filtering.

## Request Syntax
<a name="API_SearchContactFlowModules_RequestSyntax"></a>

```
POST /search-contact-flow-modules HTTP/1.1
Content-type: application/json

{
   "InstanceId": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "SearchCriteria": {
      "AndConditions": [
         "ContactFlowModuleSearchCriteria"
      ],
      "OrConditions": [
         "ContactFlowModuleSearchCriteria"
      ],
      "StateCondition": "{{string}}",
      "StatusCondition": "{{string}}",
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
<a name="API_SearchContactFlowModules_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_SearchContactFlowModules_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [InstanceId](#API_SearchContactFlowModules_RequestSyntax) **   <a name="connect-SearchContactFlowModules-request-InstanceId"></a>
The identifier of the Connect Customer instance. You can find the instance ID in the Amazon Resource Name (ARN) of the instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [MaxResults](#API_SearchContactFlowModules_RequestSyntax) **   <a name="connect-SearchContactFlowModules-request-MaxResults"></a>
The maximum number of results to return per page.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_SearchContactFlowModules_RequestSyntax) **   <a name="connect-SearchContactFlowModules-request-NextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2500.
Required: No

 ** [SearchCriteria](#API_SearchContactFlowModules_RequestSyntax) **   <a name="connect-SearchContactFlowModules-request-SearchCriteria"></a>
The search criteria to be used to return flow modules.
The `name` and `description` fields support "contains" queries with a minimum of 2 characters and a maximum of 25 characters. Any queries with character lengths outside of this range will result in invalid results.
Type: [ContactFlowModuleSearchCriteria](API_ContactFlowModuleSearchCriteria.md) object
Required: No

 ** [SearchFilter](#API_SearchContactFlowModules_RequestSyntax) **   <a name="connect-SearchContactFlowModules-request-SearchFilter"></a>
Filters to be applied to search results.
Type: [ContactFlowModuleSearchFilter](API_ContactFlowModuleSearchFilter.md) object
Required: No

## Response Syntax
<a name="API_SearchContactFlowModules_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ApproximateTotalCount": number,
   "ContactFlowModules": [
      {
         "Arn": "string",
         "Content": "string",
         "Description": "string",
         "ExternalInvocationConfiguration": {
            "Enabled": boolean
         },
         "FlowModuleContentSha256": "string",
         "Id": "string",
         "Name": "string",
         "Settings": "string",
         "State": "string",
         "Status": "string",
         "Tags": {
            "string" : "string"
         },
         "Version": number,
         "VersionDescription": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_SearchContactFlowModules_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ApproximateTotalCount](#API_SearchContactFlowModules_ResponseSyntax) **   <a name="connect-SearchContactFlowModules-response-ApproximateTotalCount"></a>
The total number of flows which matched your search query.
Type: Long

 ** [ContactFlowModules](#API_SearchContactFlowModules_ResponseSyntax) **   <a name="connect-SearchContactFlowModules-response-ContactFlowModules"></a>
The search criteria to be used to return flow modules.
Type: Array of [ContactFlowModule](API_ContactFlowModule.md) objects

 ** [NextToken](#API_SearchContactFlowModules_ResponseSyntax) **   <a name="connect-SearchContactFlowModules-response-NextToken"></a>
If there are additional results, this is the token for the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2500.

## Errors
<a name="API_SearchContactFlowModules_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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
<a name="API_SearchContactFlowModules_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/SearchContactFlowModules)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/SearchContactFlowModules)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/SearchContactFlowModules)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/SearchContactFlowModules)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/SearchContactFlowModules)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/SearchContactFlowModules)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/SearchContactFlowModules)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/SearchContactFlowModules)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/SearchContactFlowModules)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/SearchContactFlowModules)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
