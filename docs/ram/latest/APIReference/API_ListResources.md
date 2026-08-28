---
source_url: https://docs.aws.amazon.com/ram/latest/APIReference/API_ListResources.html
---

# ListResources
<a name="API_ListResources"></a>

Lists the resources that you added to a resource share or the resources that are shared with you.

**Note**
Always check the `NextToken` response parameter for a `null` value when calling a paginated operation. These operations can occasionally return an empty set of results even when there are more results available. The `NextToken` response parameter value is `null` *only* when there are no more results to display.

## Request Syntax
<a name="API_ListResources_RequestSyntax"></a>

```
POST /listresources HTTP/1.1
Content-type: application/json

{
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "principal": "{{string}}",
   "resourceArns": [ "{{string}}" ],
   "resourceOwner": "{{string}}",
   "resourceRegionScope": "{{string}}",
   "resourceShareArns": [ "{{string}}" ],
   "resourceType": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListResources_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListResources_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [resourceOwner](#API_ListResources_RequestSyntax) **   <a name="ram-ListResources-request-resourceOwner"></a>
Specifies that you want to list only the resource shares that match the following:
+  ** `SELF` ** – resources that your account shares with other accounts
+  ** `OTHER-ACCOUNTS` ** – resources that other accounts share with your account
Type: String
Valid Values: `SELF | OTHER-ACCOUNTS`
Required: Yes

 ** [maxResults](#API_ListResources_RequestSyntax) **   <a name="ram-ListResources-request-maxResults"></a>
Specifies the total number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items exist beyond the number you specify, the `NextToken` response element is returned with a value (not null). Include the specified value as the `NextToken` request parameter in the next call to the operation to get the next part of the results. Note that the service might return fewer results than the maximum even when there are more results available. You should check `NextToken` after every operation to ensure that you receive all of the results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 500.
Required: No

 ** [nextToken](#API_ListResources_RequestSyntax) **   <a name="ram-ListResources-request-nextToken"></a>
Specifies that you want to receive the next page of results. Valid only if you received a `NextToken` response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's `NextToken` response to request the next page of results.
Type: String
Required: No

 ** [principal](#API_ListResources_RequestSyntax) **   <a name="ram-ListResources-request-principal"></a>
Specifies that you want to list only the resource shares that are associated with the specified principal.
Type: String
Required: No

 ** [resourceArns](#API_ListResources_RequestSyntax) **   <a name="ram-ListResources-request-resourceArns"></a>
Specifies that you want to list only the resource shares that include resources with the specified [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html).
Type: Array of strings
Required: No

 ** [resourceRegionScope](#API_ListResources_RequestSyntax) **   <a name="ram-ListResources-request-resourceRegionScope"></a>
Specifies that you want the results to include only resources that have the specified scope.
+  `ALL` – the results include both global and regional resources or resource types.
+  `GLOBAL` – the results include only global resources or resource types.
+  `REGIONAL` – the results include only regional resources or resource types.
The default value is `ALL`.
Type: String
Valid Values: `ALL | REGIONAL | GLOBAL`
Required: No

 ** [resourceShareArns](#API_ListResources_RequestSyntax) **   <a name="ram-ListResources-request-resourceShareArns"></a>
Specifies that you want to list only resources in the resource shares identified by the specified [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html).
Type: Array of strings
Required: No

 ** [resourceType](#API_ListResources_RequestSyntax) **   <a name="ram-ListResources-request-resourceType"></a>
Specifies that you want to list only the resource shares that include resources of the specified resource type.
For valid values, query the [ListResourceTypes](API_ListResourceTypes.md) operation.
Type: String
Required: No

## Response Syntax
<a name="API_ListResources_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "resources": [
      {
         "arn": "string",
         "creationTime": number,
         "lastUpdatedTime": number,
         "resourceGroupArn": "string",
         "resourceRegionScope": "string",
         "resourceShareArn": "string",
         "status": "string",
         "statusMessage": "string",
         "type": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListResources_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListResources_ResponseSyntax) **   <a name="ram-ListResources-response-nextToken"></a>
If present, this value indicates that more output is available than is included in the current response. Use this value in the `NextToken` request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the `NextToken` response element comes back as `null`. This indicates that this is the last page of results.
Type: String

 ** [resources](#API_ListResources_ResponseSyntax) **   <a name="ram-ListResources-response-resources"></a>
An array of objects that contain information about the resources.
Type: Array of [Resource](API_Resource.md) objects

## Errors
<a name="API_ListResources_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidNextTokenException **
The operation failed because the specified value for `NextToken` isn't valid. You must specify a value you received in the `NextToken` response of a previous call to this operation.
HTTP Status Code: 400

 ** InvalidParameterException **
The operation failed because a parameter you specified isn't valid.
HTTP Status Code: 400

 ** InvalidResourceTypeException **
The operation failed because the specified resource type isn't valid.
HTTP Status Code: 400

 ** MalformedArnException **
The operation failed because the specified [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) has a format that isn't valid.
HTTP Status Code: 400

 ** ServerInternalException **
The operation failed because the service could not respond to the request due to an internal problem. Try again later.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The operation failed because the service isn't available. Try again later.
HTTP Status Code: 503

 ** UnknownResourceException **
The operation failed because a specified resource couldn't be found.
HTTP Status Code: 400

## See Also
<a name="API_ListResources_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ram-2018-01-04/ListResources)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ram-2018-01-04/ListResources)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ram-2018-01-04/ListResources)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ram-2018-01-04/ListResources)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ram-2018-01-04/ListResources)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ram-2018-01-04/ListResources)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ram-2018-01-04/ListResources)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ram-2018-01-04/ListResources)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ram-2018-01-04/ListResources)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ram-2018-01-04/ListResources)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS RAM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ram` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
