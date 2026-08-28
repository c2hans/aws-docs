---
source_url: https://docs.aws.amazon.com/ram/latest/APIReference/API_ListReplacePermissionAssociationsWork.html
---

# ListReplacePermissionAssociationsWork
<a name="API_ListReplacePermissionAssociationsWork"></a>

Retrieves the current status of the asynchronous tasks performed by AWS RAM when you perform the [ReplacePermissionAssociationsWork](API_ReplacePermissionAssociationsWork.md) operation.

**Note**
Always check the `NextToken` response parameter for a `null` value when calling a paginated operation. These operations can occasionally return an empty set of results even when there are more results available. The `NextToken` response parameter value is `null` *only* when there are no more results to display.

## Request Syntax
<a name="API_ListReplacePermissionAssociationsWork_RequestSyntax"></a>

```
POST /listreplacepermissionassociationswork HTTP/1.1
Content-type: application/json

{
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "status": "{{string}}",
   "workIds": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_ListReplacePermissionAssociationsWork_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListReplacePermissionAssociationsWork_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListReplacePermissionAssociationsWork_RequestSyntax) **   <a name="ram-ListReplacePermissionAssociationsWork-request-maxResults"></a>
Specifies the total number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items exist beyond the number you specify, the `NextToken` response element is returned with a value (not null). Include the specified value as the `NextToken` request parameter in the next call to the operation to get the next part of the results. Note that the service might return fewer results than the maximum even when there are more results available. You should check `NextToken` after every operation to ensure that you receive all of the results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 500.
Required: No

 ** [nextToken](#API_ListReplacePermissionAssociationsWork_RequestSyntax) **   <a name="ram-ListReplacePermissionAssociationsWork-request-nextToken"></a>
Specifies that you want to receive the next page of results. Valid only if you received a `NextToken` response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's `NextToken` response to request the next page of results.
Type: String
Required: No

 ** [status](#API_ListReplacePermissionAssociationsWork_RequestSyntax) **   <a name="ram-ListReplacePermissionAssociationsWork-request-status"></a>
Specifies that you want to see only the details about requests with a status that matches this value.
Type: String
Valid Values: `IN_PROGRESS | COMPLETED | FAILED`
Required: No

 ** [workIds](#API_ListReplacePermissionAssociationsWork_RequestSyntax) **   <a name="ram-ListReplacePermissionAssociationsWork-request-workIds"></a>
A list of IDs. These values come from the `id`field of the `replacePermissionAssociationsWork`structure returned by the [ReplacePermissionAssociations](API_ReplacePermissionAssociations.md) operation.
Type: Array of strings
Required: No

## Response Syntax
<a name="API_ListReplacePermissionAssociationsWork_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "replacePermissionAssociationsWorks": [
      {
         "creationTime": number,
         "fromPermissionArn": "string",
         "fromPermissionVersion": "string",
         "id": "string",
         "lastUpdatedTime": number,
         "status": "string",
         "statusMessage": "string",
         "toPermissionArn": "string",
         "toPermissionVersion": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListReplacePermissionAssociationsWork_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListReplacePermissionAssociationsWork_ResponseSyntax) **   <a name="ram-ListReplacePermissionAssociationsWork-response-nextToken"></a>
If present, this value indicates that more output is available than is included in the current response. Use this value in the `NextToken` request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the `NextToken` response element comes back as `null`. This indicates that this is the last page of results.
Type: String

 ** [replacePermissionAssociationsWorks](#API_ListReplacePermissionAssociationsWork_ResponseSyntax) **   <a name="ram-ListReplacePermissionAssociationsWork-response-replacePermissionAssociationsWorks"></a>
An array of data structures that provide details of the matching work IDs.
Type: Array of [ReplacePermissionAssociationsWork](API_ReplacePermissionAssociationsWork.md) objects

## Errors
<a name="API_ListReplacePermissionAssociationsWork_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidNextTokenException **
The operation failed because the specified value for `NextToken` isn't valid. You must specify a value you received in the `NextToken` response of a previous call to this operation.
HTTP Status Code: 400

 ** InvalidParameterException **
The operation failed because a parameter you specified isn't valid.
HTTP Status Code: 400

 ** ServerInternalException **
The operation failed because the service could not respond to the request due to an internal problem. Try again later.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The operation failed because the service isn't available. Try again later.
HTTP Status Code: 503

## See Also
<a name="API_ListReplacePermissionAssociationsWork_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ram-2018-01-04/ListReplacePermissionAssociationsWork)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ram-2018-01-04/ListReplacePermissionAssociationsWork)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ram-2018-01-04/ListReplacePermissionAssociationsWork)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ram-2018-01-04/ListReplacePermissionAssociationsWork)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ram-2018-01-04/ListReplacePermissionAssociationsWork)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ram-2018-01-04/ListReplacePermissionAssociationsWork)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ram-2018-01-04/ListReplacePermissionAssociationsWork)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ram-2018-01-04/ListReplacePermissionAssociationsWork)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ram-2018-01-04/ListReplacePermissionAssociationsWork)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ram-2018-01-04/ListReplacePermissionAssociationsWork)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS RAM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ram` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
