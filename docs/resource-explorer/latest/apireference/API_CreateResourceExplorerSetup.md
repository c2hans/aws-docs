---
source_url: https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_CreateResourceExplorerSetup.html
---

# CreateResourceExplorerSetup
<a name="API_CreateResourceExplorerSetup"></a>

Creates a Resource Explorer setup configuration across multiple AWS Regions. This operation sets up indexes and views in the specified Regions. This operation can also be used to set an aggregator Region for cross-Region resource search.

## Request Syntax
<a name="API_CreateResourceExplorerSetup_RequestSyntax"></a>

```
POST /CreateResourceExplorerSetup HTTP/1.1
Content-type: application/json

{
   "AggregatorRegions": [ "{{string}}" ],
   "RegionList": [ "{{string}}" ],
   "ViewName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateResourceExplorerSetup_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateResourceExplorerSetup_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [RegionList](#API_CreateResourceExplorerSetup_RequestSyntax) **   <a name="resourceexplorer-CreateResourceExplorerSetup-request-RegionList"></a>
A list of AWS Regions where Resource Explorer should be configured. Each Region in the list will have a user-owned index created.
Type: Array of strings
Array Members: Minimum number of 1 item.
Pattern: `[a-z-]+-[a-z]+-[0-9]`
Required: Yes

 ** [ViewName](#API_CreateResourceExplorerSetup_RequestSyntax) **   <a name="resourceexplorer-CreateResourceExplorerSetup-request-ViewName"></a>
The name for the view to be created as part of the Resource Explorer setup. The view name must be unique within the AWS account and Region.
Type: String
Pattern: `[a-zA-Z0-9-]{1,64}`
Required: Yes

 ** [AggregatorRegions](#API_CreateResourceExplorerSetup_RequestSyntax) **   <a name="resourceexplorer-CreateResourceExplorerSetup-request-AggregatorRegions"></a>
A list of AWS Regions that should be configured as aggregator Regions. Aggregator Regions receive replicated index information from all other Regions where there is a user-owned index.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Pattern: `[a-z-]+-[a-z]+-[0-9]`
Required: No

## Response Syntax
<a name="API_CreateResourceExplorerSetup_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "TaskId": "string"
}
```

## Response Elements
<a name="API_CreateResourceExplorerSetup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [TaskId](#API_CreateResourceExplorerSetup_ResponseSyntax) **   <a name="resourceexplorer-CreateResourceExplorerSetup-response-TaskId"></a>
The unique identifier for the setup task. Use this ID with `GetResourceExplorerSetup` to monitor the progress of the configuration operation.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`

## Errors
<a name="API_CreateResourceExplorerSetup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The credentials that you used to call this operation don't have the minimum required permissions.
HTTP Status Code: 403

 ** ConflictException **
If you attempted to create a view, then the request failed because either you specified parameters that didn’t match the original request, or you attempted to create a view with a name that already exists in this AWS Region.
If you attempted to create an index, then the request failed because either you specified parameters that didn't match the original request, or an index already exists in the current AWS Region.
If you attempted to update an index type to `AGGREGATOR`, then the request failed because you already have an `AGGREGATOR` index in a different AWS Region.
HTTP Status Code: 409

 ** InternalServerException **
The request failed because of internal service error. Try your request again later.
HTTP Status Code: 500

 ** ThrottlingException **
The request failed because you exceeded a rate limit for this operation. For more information, see [Quotas for Resource Explorer](https://docs.aws.amazon.com/resource-explorer/latest/userguide/quotas.html).
HTTP Status Code: 429

 ** ValidationException **
You provided an invalid value for one of the operation's parameters. Check the syntax for the operation, and try again.
 ** FieldList **
An array of the request fields that had validation errors.
HTTP Status Code: 400

## See Also
<a name="API_CreateResourceExplorerSetup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resource-explorer-2-2022-07-28/CreateResourceExplorerSetup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resource-explorer-2-2022-07-28/CreateResourceExplorerSetup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resource-explorer-2-2022-07-28/CreateResourceExplorerSetup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resource-explorer-2-2022-07-28/CreateResourceExplorerSetup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resource-explorer-2-2022-07-28/CreateResourceExplorerSetup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resource-explorer-2-2022-07-28/CreateResourceExplorerSetup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resource-explorer-2-2022-07-28/CreateResourceExplorerSetup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resource-explorer-2-2022-07-28/CreateResourceExplorerSetup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/resource-explorer-2-2022-07-28/CreateResourceExplorerSetup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resource-explorer-2-2022-07-28/CreateResourceExplorerSetup)
