---
source_url: https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_GetResourceExplorerSetup.html
---

# GetResourceExplorerSetup
<a name="API_GetResourceExplorerSetup"></a>

Retrieves the status and details of a Resource Explorer setup operation. This operation returns information about the progress of creating or deleting Resource Explorer configurations across Regions.

## Request Syntax
<a name="API_GetResourceExplorerSetup_RequestSyntax"></a>

```
POST /GetResourceExplorerSetup HTTP/1.1
Content-type: application/json

{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "TaskId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetResourceExplorerSetup_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetResourceExplorerSetup_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [TaskId](#API_GetResourceExplorerSetup_RequestSyntax) **   <a name="resourceexplorer-GetResourceExplorerSetup-request-TaskId"></a>
The unique identifier of the setup task to retrieve status information for. This ID is returned by `CreateResourceExplorerSetup` or `DeleteResourceExplorerSetup` operations.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** [MaxResults](#API_GetResourceExplorerSetup_RequestSyntax) **   <a name="resourceexplorer-GetResourceExplorerSetup-request-MaxResults"></a>
The maximum number of Region status results to return in a single response. Valid values are between `1` and `100`.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_GetResourceExplorerSetup_RequestSyntax) **   <a name="resourceexplorer-GetResourceExplorerSetup-request-NextToken"></a>
The pagination token from a previous `GetResourceExplorerSetup` response. Use this token to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## Response Syntax
<a name="API_GetResourceExplorerSetup_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "Regions": [
      {
         "Index": {
            "ErrorDetails": {
               "Code": "string",
               "Message": "string"
            },
            "Index": {
               "Arn": "string",
               "Region": "string",
               "Type": "string"
            },
            "Status": "string"
         },
         "Region": "string",
         "View": {
            "ErrorDetails": {
               "Code": "string",
               "Message": "string"
            },
            "Status": "string",
            "View": {
               "Filters": {
                  "FilterString": "string"
               },
               "IncludedProperties": [
                  {
                     "Name": "string"
                  }
               ],
               "LastUpdatedAt": "string",
               "Owner": "string",
               "Scope": "string",
               "ViewArn": "string"
            }
         }
      }
   ]
}
```

## Response Elements
<a name="API_GetResourceExplorerSetup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_GetResourceExplorerSetup_ResponseSyntax) **   <a name="resourceexplorer-GetResourceExplorerSetup-response-NextToken"></a>
The pagination token to use in a subsequent `GetResourceExplorerSetup` request to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [Regions](#API_GetResourceExplorerSetup_ResponseSyntax) **   <a name="resourceexplorer-GetResourceExplorerSetup-response-Regions"></a>
A list of Region status objects that describe the current state of Resource Explorer configuration in each Region.
Type: Array of [RegionStatus](API_RegionStatus.md) objects

## Errors
<a name="API_GetResourceExplorerSetup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The credentials that you used to call this operation don't have the minimum required permissions.
HTTP Status Code: 403

 ** InternalServerException **
The request failed because of internal service error. Try your request again later.
HTTP Status Code: 500

 ** ResourceNotFoundException **
You specified a resource that doesn't exist. Check the ID or ARN that you used to identity the resource, and try again.
HTTP Status Code: 404

 ** ThrottlingException **
The request failed because you exceeded a rate limit for this operation. For more information, see [Quotas for Resource Explorer](https://docs.aws.amazon.com/resource-explorer/latest/userguide/quotas.html).
HTTP Status Code: 429

 ** ValidationException **
You provided an invalid value for one of the operation's parameters. Check the syntax for the operation, and try again.
 ** FieldList **
An array of the request fields that had validation errors.
HTTP Status Code: 400

## See Also
<a name="API_GetResourceExplorerSetup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resource-explorer-2-2022-07-28/GetResourceExplorerSetup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resource-explorer-2-2022-07-28/GetResourceExplorerSetup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resource-explorer-2-2022-07-28/GetResourceExplorerSetup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resource-explorer-2-2022-07-28/GetResourceExplorerSetup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resource-explorer-2-2022-07-28/GetResourceExplorerSetup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resource-explorer-2-2022-07-28/GetResourceExplorerSetup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resource-explorer-2-2022-07-28/GetResourceExplorerSetup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resource-explorer-2-2022-07-28/GetResourceExplorerSetup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/resource-explorer-2-2022-07-28/GetResourceExplorerSetup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resource-explorer-2-2022-07-28/GetResourceExplorerSetup)
