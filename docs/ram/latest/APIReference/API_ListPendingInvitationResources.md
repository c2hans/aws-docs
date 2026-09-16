---
source_url: https://docs.aws.amazon.com/ram/latest/APIReference/API_ListPendingInvitationResources.html
---

# ListPendingInvitationResources
<a name="API_ListPendingInvitationResources"></a>

Lists the resources in a resource share that is shared with you but for which the invitation is still `PENDING`. That means that you haven't accepted or rejected the invitation and the invitation hasn't expired.

**Note**
Always check the `NextToken` response parameter for a `null` value when calling a paginated operation. These operations can occasionally return an empty set of results even when there are more results available. The `NextToken` response parameter value is `null` *only* when there are no more results to display.

## Request Syntax
<a name="API_ListPendingInvitationResources_RequestSyntax"></a>

```
POST /listpendinginvitationresources HTTP/1.1
Content-type: application/json

{
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "resourceRegionScope": "{{string}}",
   "resourceShareInvitationArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListPendingInvitationResources_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListPendingInvitationResources_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [resourceShareInvitationArn](#API_ListPendingInvitationResources_RequestSyntax) **   <a name="ram-ListPendingInvitationResources-request-resourceShareInvitationArn"></a>
Specifies the [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the invitation. You can use [GetResourceShareInvitations](API_GetResourceShareInvitations.md) to find the ARN of the invitation.
Type: String
Required: Yes

 ** [maxResults](#API_ListPendingInvitationResources_RequestSyntax) **   <a name="ram-ListPendingInvitationResources-request-maxResults"></a>
Specifies the total number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items exist beyond the number you specify, the `NextToken` response element is returned with a value (not null). Include the specified value as the `NextToken` request parameter in the next call to the operation to get the next part of the results. Note that the service might return fewer results than the maximum even when there are more results available. You should check `NextToken` after every operation to ensure that you receive all of the results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 500.
Required: No

 ** [nextToken](#API_ListPendingInvitationResources_RequestSyntax) **   <a name="ram-ListPendingInvitationResources-request-nextToken"></a>
Specifies that you want to receive the next page of results. Valid only if you received a `NextToken` response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's `NextToken` response to request the next page of results.
Type: String
Required: No

 ** [resourceRegionScope](#API_ListPendingInvitationResources_RequestSyntax) **   <a name="ram-ListPendingInvitationResources-request-resourceRegionScope"></a>
Specifies that you want the results to include only resources that have the specified scope.
+  `ALL` – the results include both global and regional resources or resource types.
+  `GLOBAL` – the results include only global resources or resource types.
+  `REGIONAL` – the results include only regional resources or resource types.
The default value is `ALL`.
Type: String
Valid Values: `ALL | REGIONAL | GLOBAL`
Required: No

## Response Syntax
<a name="API_ListPendingInvitationResources_ResponseSyntax"></a>

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
<a name="API_ListPendingInvitationResources_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListPendingInvitationResources_ResponseSyntax) **   <a name="ram-ListPendingInvitationResources-response-nextToken"></a>
If present, this value indicates that more output is available than is included in the current response. Use this value in the `NextToken` request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the `NextToken` response element comes back as `null`. This indicates that this is the last page of results.
Type: String

 ** [resources](#API_ListPendingInvitationResources_ResponseSyntax) **   <a name="ram-ListPendingInvitationResources-response-resources"></a>
An array of objects that contain the information about the resources included the specified resource share.
Type: Array of [Resource](API_Resource.md) objects

## Errors
<a name="API_ListPendingInvitationResources_Errors"></a>

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

 ** MissingRequiredParameterException **
The operation failed because a required input parameter is missing.
HTTP Status Code: 400

 ** ResourceShareInvitationAlreadyRejectedException **
The operation failed because the specified invitation was already rejected.
HTTP Status Code: 400

 ** ResourceShareInvitationArnNotFoundException **
The operation failed because the specified [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) for an invitation was not found.
HTTP Status Code: 400

 ** ResourceShareInvitationExpiredException **
The operation failed because the specified invitation is past its expiration date and time.
HTTP Status Code: 400

 ** ServerInternalException **
The operation failed because the service could not respond to the request due to an internal problem. Try again later.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The operation failed because the service isn't available. Try again later.
HTTP Status Code: 503

## See Also
<a name="API_ListPendingInvitationResources_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ram-2018-01-04/ListPendingInvitationResources)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ram-2018-01-04/ListPendingInvitationResources)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ram-2018-01-04/ListPendingInvitationResources)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ram-2018-01-04/ListPendingInvitationResources)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ram-2018-01-04/ListPendingInvitationResources)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ram-2018-01-04/ListPendingInvitationResources)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ram-2018-01-04/ListPendingInvitationResources)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ram-2018-01-04/ListPendingInvitationResources)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ram-2018-01-04/ListPendingInvitationResources)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ram-2018-01-04/ListPendingInvitationResources)
