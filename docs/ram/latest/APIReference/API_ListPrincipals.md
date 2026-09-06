---
source_url: https://docs.aws.amazon.com/ram/latest/APIReference/API_ListPrincipals.html
---

# ListPrincipals
<a name="API_ListPrincipals"></a>

Lists the principals that you are sharing resources with or that are sharing resources with you.

**Note**
Always check the `NextToken` response parameter for a `null` value when calling a paginated operation. These operations can occasionally return an empty set of results even when there are more results available. The `NextToken` response parameter value is `null` *only* when there are no more results to display.

## Request Syntax
<a name="API_ListPrincipals_RequestSyntax"></a>

```
POST /listprincipals HTTP/1.1
Content-type: application/json

{
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "principals": [ "{{string}}" ],
   "resourceArn": "{{string}}",
   "resourceOwner": "{{string}}",
   "resourceShareArns": [ "{{string}}" ],
   "resourceType": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListPrincipals_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListPrincipals_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [resourceOwner](#API_ListPrincipals_RequestSyntax) **   <a name="ram-ListPrincipals-request-resourceOwner"></a>
Specifies that you want to list information for only resource shares that match the following:
+  ** `SELF` ** – principals that your account is sharing resources with
+  ** `OTHER-ACCOUNTS` ** – principals that are sharing resources with your account
Type: String
Valid Values: `SELF | OTHER-ACCOUNTS`
Required: Yes

 ** [maxResults](#API_ListPrincipals_RequestSyntax) **   <a name="ram-ListPrincipals-request-maxResults"></a>
Specifies the total number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items exist beyond the number you specify, the `NextToken` response element is returned with a value (not null). Include the specified value as the `NextToken` request parameter in the next call to the operation to get the next part of the results. Note that the service might return fewer results than the maximum even when there are more results available. You should check `NextToken` after every operation to ensure that you receive all of the results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 500.
Required: No

 ** [nextToken](#API_ListPrincipals_RequestSyntax) **   <a name="ram-ListPrincipals-request-nextToken"></a>
Specifies that you want to receive the next page of results. Valid only if you received a `NextToken` response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's `NextToken` response to request the next page of results.
Type: String
Required: No

 ** [principals](#API_ListPrincipals_RequestSyntax) **   <a name="ram-ListPrincipals-request-principals"></a>
Specifies that you want to list information for only the listed principals.
You can include the following values:
+ An AWS account ID, for example: `123456789012`
+ An [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of an organization in AWS Organizations, for example: `arn:aws:organizations::123456789012:organization/o-exampleorgid`
+ An ARN of an organizational unit (OU) in AWS Organizations, for example: `arn:aws:organizations::123456789012:ou/o-exampleorgid/ou-examplerootid-exampleouid123`
+ An ARN of an IAM role, for example: `arn:aws:iam::123456789012:role/rolename`
+ An ARN of an IAM user, for example: `arn:aws:iam::123456789012user/username`
+ A service principal name, for example: `service-id.amazonaws.com`
Not all resource types can be shared with IAM roles and users. For more information, see [Sharing with IAM roles and users](https://docs.aws.amazon.com/ram/latest/userguide/permissions.html#permissions-rbp-supported-resource-types) in the * AWS Resource Access Manager User Guide*.
Type: Array of strings
Required: No

 ** [resourceArn](#API_ListPrincipals_RequestSyntax) **   <a name="ram-ListPrincipals-request-resourceArn"></a>
Specifies that you want to list principal information for the resource share with the specified [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html).
Type: String
Required: No

 ** [resourceShareArns](#API_ListPrincipals_RequestSyntax) **   <a name="ram-ListPrincipals-request-resourceShareArns"></a>
Specifies that you want to list information for only principals associated with the resource shares specified by a list the [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html).
Type: Array of strings
Required: No

 ** [resourceType](#API_ListPrincipals_RequestSyntax) **   <a name="ram-ListPrincipals-request-resourceType"></a>
Specifies that you want to list information for only principals associated with resource shares that include the specified resource type.
For a list of valid values, query the [ListResourceTypes](API_ListResourceTypes.md) operation.
Type: String
Required: No

## Response Syntax
<a name="API_ListPrincipals_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "principals": [
      {
         "creationTime": number,
         "external": boolean,
         "id": "string",
         "lastUpdatedTime": number,
         "resourceShareArn": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListPrincipals_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListPrincipals_ResponseSyntax) **   <a name="ram-ListPrincipals-response-nextToken"></a>
If present, this value indicates that more output is available than is included in the current response. Use this value in the `NextToken` request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the `NextToken` response element comes back as `null`. This indicates that this is the last page of results.
Type: String

 ** [principals](#API_ListPrincipals_ResponseSyntax) **   <a name="ram-ListPrincipals-response-principals"></a>
An array of objects that contain the details about the principals.
Type: Array of [Principal](API_Principal.md) objects

## Errors
<a name="API_ListPrincipals_Errors"></a>

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
<a name="API_ListPrincipals_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ram-2018-01-04/ListPrincipals)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ram-2018-01-04/ListPrincipals)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ram-2018-01-04/ListPrincipals)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ram-2018-01-04/ListPrincipals)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ram-2018-01-04/ListPrincipals)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ram-2018-01-04/ListPrincipals)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ram-2018-01-04/ListPrincipals)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ram-2018-01-04/ListPrincipals)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ram-2018-01-04/ListPrincipals)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ram-2018-01-04/ListPrincipals)
