---
source_url: https://docs.aws.amazon.com/ram/latest/APIReference/API_GetResourceShares.html
---

# GetResourceShares
<a name="API_GetResourceShares"></a>

Retrieves details about the resource shares that you own or that are shared with you.

**Note**
Always check the `NextToken` response parameter for a `null` value when calling a paginated operation. These operations can occasionally return an empty set of results even when there are more results available. The `NextToken` response parameter value is `null` *only* when there are no more results to display.

## Request Syntax
<a name="API_GetResourceShares_RequestSyntax"></a>

```
POST /getresourceshares HTTP/1.1
Content-type: application/json

{
   "maxResults": {{number}},
   "name": "{{string}}",
   "nextToken": "{{string}}",
   "permissionArn": "{{string}}",
   "permissionVersion": {{number}},
   "resourceOwner": "{{string}}",
   "resourceShareArns": [ "{{string}}" ],
   "resourceShareStatus": "{{string}}",
   "tagFilters": [
      {
         "tagKey": "{{string}}",
         "tagValues": [ "{{string}}" ]
      }
   ]
}
```

## URI Request Parameters
<a name="API_GetResourceShares_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetResourceShares_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [resourceOwner](#API_GetResourceShares_RequestSyntax) **   <a name="ram-GetResourceShares-request-resourceOwner"></a>
Specifies that you want to retrieve details of only those resource shares that match the following:
+  ** `SELF` ** – resource shares that your account shares with other accounts
+  ** `OTHER-ACCOUNTS` ** – resource shares that other accounts share with your account
Type: String
Valid Values: `SELF | OTHER-ACCOUNTS`
Required: Yes

 ** [maxResults](#API_GetResourceShares_RequestSyntax) **   <a name="ram-GetResourceShares-request-maxResults"></a>
Specifies the total number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items exist beyond the number you specify, the `NextToken` response element is returned with a value (not null). Include the specified value as the `NextToken` request parameter in the next call to the operation to get the next part of the results. Note that the service might return fewer results than the maximum even when there are more results available. You should check `NextToken` after every operation to ensure that you receive all of the results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 500.
Required: No

 ** [name](#API_GetResourceShares_RequestSyntax) **   <a name="ram-GetResourceShares-request-name"></a>
Specifies the name of an individual resource share that you want to retrieve details about.
Type: String
Required: No

 ** [nextToken](#API_GetResourceShares_RequestSyntax) **   <a name="ram-GetResourceShares-request-nextToken"></a>
Specifies that you want to receive the next page of results. Valid only if you received a `NextToken` response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's `NextToken` response to request the next page of results.
Type: String
Required: No

 ** [permissionArn](#API_GetResourceShares_RequestSyntax) **   <a name="ram-GetResourceShares-request-permissionArn"></a>
Specifies that you want to retrieve details of only those resource shares that use the managed permission with this [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html).
Type: String
Required: No

 ** [permissionVersion](#API_GetResourceShares_RequestSyntax) **   <a name="ram-GetResourceShares-request-permissionVersion"></a>
Specifies that you want to retrieve details for only those resource shares that use the specified version of the managed permission.
Type: Integer
Required: No

 ** [resourceShareArns](#API_GetResourceShares_RequestSyntax) **   <a name="ram-GetResourceShares-request-resourceShareArns"></a>
Specifies the [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of individual resource shares that you want information about.
Type: Array of strings
Required: No

 ** [resourceShareStatus](#API_GetResourceShares_RequestSyntax) **   <a name="ram-GetResourceShares-request-resourceShareStatus"></a>
Specifies that you want to retrieve details of only those resource shares that have this status.
Type: String
Valid Values: `PENDING | ACTIVE | FAILED | DELETING | DELETED`
Required: No

 ** [tagFilters](#API_GetResourceShares_RequestSyntax) **   <a name="ram-GetResourceShares-request-tagFilters"></a>
Specifies that you want to retrieve details of only those resource shares that match the specified tag keys and values.
Type: Array of [TagFilter](API_TagFilter.md) objects
Required: No

## Response Syntax
<a name="API_GetResourceShares_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "resourceShares": [
      {
         "allowExternalPrincipals": boolean,
         "creationTime": number,
         "featureSet": "string",
         "lastUpdatedTime": number,
         "name": "string",
         "owningAccountId": "string",
         "resourceShareArn": "string",
         "resourceShareConfiguration": {
            "retainSharingOnAccountLeaveOrganization": boolean
         },
         "status": "string",
         "statusMessage": "string",
         "tags": [
            {
               "key": "string",
               "value": "string"
            }
         ]
      }
   ]
}
```

## Response Elements
<a name="API_GetResourceShares_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_GetResourceShares_ResponseSyntax) **   <a name="ram-GetResourceShares-response-nextToken"></a>
If present, this value indicates that more output is available than is included in the current response. Use this value in the `NextToken` request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the `NextToken` response element comes back as `null`. This indicates that this is the last page of results.
Type: String

 ** [resourceShares](#API_GetResourceShares_ResponseSyntax) **   <a name="ram-GetResourceShares-response-resourceShares"></a>
An array of objects that contain the information about the resource shares.
Type: Array of [ResourceShare](API_ResourceShare.md) objects

## Errors
<a name="API_GetResourceShares_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidNextTokenException **
The operation failed because the specified value for `NextToken` isn't valid. You must specify a value you received in the `NextToken` response of a previous call to this operation.
HTTP Status Code: 400

 ** InvalidParameterException **
The operation failed because a parameter you specified isn't valid.
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
<a name="API_GetResourceShares_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ram-2018-01-04/GetResourceShares)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ram-2018-01-04/GetResourceShares)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ram-2018-01-04/GetResourceShares)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ram-2018-01-04/GetResourceShares)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ram-2018-01-04/GetResourceShares)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ram-2018-01-04/GetResourceShares)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ram-2018-01-04/GetResourceShares)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ram-2018-01-04/GetResourceShares)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ram-2018-01-04/GetResourceShares)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ram-2018-01-04/GetResourceShares)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS RAM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ram` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
