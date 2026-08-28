---
source_url: https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_ListStreamingAccessForServices.html
---

# ListStreamingAccessForServices
<a name="API_ListStreamingAccessForServices"></a>

Returns a list of AWS services that have been granted streaming access to your Resource Explorer data. Streaming access allows AWS services to receive real-time updates about your resources as they are indexed by Resource Explorer.

 **Minimum permissions**

To call this operation, you must have the following permissions:
+  **Action**: `resource-explorer-2:ListStreamingAccessForServices`

   **Resource**: No specific resource (\*).

 **Related operations**
+ To search for resources, use [Search](API_Search.md).
+ To list available views, use [ListViews](API_ListViews.md).

## Request Syntax
<a name="API_ListStreamingAccessForServices_RequestSyntax"></a>

```
POST /ListStreamingAccessForServices HTTP/1.1
Content-type: application/json

{
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListStreamingAccessForServices_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListStreamingAccessForServices_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListStreamingAccessForServices_RequestSyntax) **   <a name="resourceexplorer-ListStreamingAccessForServices-request-MaxResults"></a>
The maximum number of streaming access entries to return in the response. If there are more results available, the response includes a NextToken value that you can use in a subsequent call to get the next set of results. The value must be between 1 and 50. If you don't specify a value, the default is 50.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [NextToken](#API_ListStreamingAccessForServices_RequestSyntax) **   <a name="resourceexplorer-ListStreamingAccessForServices-request-NextToken"></a>
The parameter for receiving additional results if you receive a `NextToken` response in a previous request. A `NextToken` response indicates that more output is available. Set this parameter to the value of the previous call's `NextToken` response to indicate where the output should continue from. The pagination tokens expire after 24 hours.
Type: String
Required: No

## Response Syntax
<a name="API_ListStreamingAccessForServices_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "StreamingAccessForServices": [
      {
         "CreatedAt": "string",
         "ServicePrincipal": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListStreamingAccessForServices_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [StreamingAccessForServices](#API_ListStreamingAccessForServices_ResponseSyntax) **   <a name="resourceexplorer-ListStreamingAccessForServices-response-StreamingAccessForServices"></a>
A list of AWS services that have streaming access to your Resource Explorer data, including details about when the access was granted.
Type: Array of [StreamingAccessDetails](API_StreamingAccessDetails.md) objects

 ** [NextToken](#API_ListStreamingAccessForServices_ResponseSyntax) **   <a name="resourceexplorer-ListStreamingAccessForServices-response-NextToken"></a>
If present, indicates that more output is available than is included in the current response. Use this value in the `NextToken` request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the `NextToken` response element comes back as `null`. The pagination tokens expire after 24 hours.
Type: String

## Errors
<a name="API_ListStreamingAccessForServices_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The credentials that you used to call this operation don't have the minimum required permissions.
HTTP Status Code: 403

 ** InternalServerException **
The request failed because of internal service error. Try your request again later.
HTTP Status Code: 500

 ** ValidationException **
You provided an invalid value for one of the operation's parameters. Check the syntax for the operation, and try again.
 ** FieldList **
An array of the request fields that had validation errors.
HTTP Status Code: 400

## See Also
<a name="API_ListStreamingAccessForServices_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resource-explorer-2-2022-07-28/ListStreamingAccessForServices)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resource-explorer-2-2022-07-28/ListStreamingAccessForServices)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resource-explorer-2-2022-07-28/ListStreamingAccessForServices)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resource-explorer-2-2022-07-28/ListStreamingAccessForServices)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resource-explorer-2-2022-07-28/ListStreamingAccessForServices)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resource-explorer-2-2022-07-28/ListStreamingAccessForServices)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resource-explorer-2-2022-07-28/ListStreamingAccessForServices)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resource-explorer-2-2022-07-28/ListStreamingAccessForServices)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/resource-explorer-2-2022-07-28/ListStreamingAccessForServices)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resource-explorer-2-2022-07-28/ListStreamingAccessForServices)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resource Explorer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resource-explorer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
