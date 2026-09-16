---
source_url: https://docs.aws.amazon.com/ram/latest/APIReference/API_GetResourceShareInvitations.html
---

# GetResourceShareInvitations
<a name="API_GetResourceShareInvitations"></a>

Retrieves details about invitations that you have received for resource shares.

**Note**
Always check the `NextToken` response parameter for a `null` value when calling a paginated operation. These operations can occasionally return an empty set of results even when there are more results available. The `NextToken` response parameter value is `null` *only* when there are no more results to display.

## Request Syntax
<a name="API_GetResourceShareInvitations_RequestSyntax"></a>

```
POST /getresourceshareinvitations HTTP/1.1
Content-type: application/json

{
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "resourceShareArns": [ "{{string}}" ],
   "resourceShareInvitationArns": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_GetResourceShareInvitations_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetResourceShareInvitations_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [maxResults](#API_GetResourceShareInvitations_RequestSyntax) **   <a name="ram-GetResourceShareInvitations-request-maxResults"></a>
Specifies the total number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items exist beyond the number you specify, the `NextToken` response element is returned with a value (not null). Include the specified value as the `NextToken` request parameter in the next call to the operation to get the next part of the results. Note that the service might return fewer results than the maximum even when there are more results available. You should check `NextToken` after every operation to ensure that you receive all of the results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 500.
Required: No

 ** [nextToken](#API_GetResourceShareInvitations_RequestSyntax) **   <a name="ram-GetResourceShareInvitations-request-nextToken"></a>
Specifies that you want to receive the next page of results. Valid only if you received a `NextToken` response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's `NextToken` response to request the next page of results.
Type: String
Required: No

 ** [resourceShareArns](#API_GetResourceShareInvitations_RequestSyntax) **   <a name="ram-GetResourceShareInvitations-request-resourceShareArns"></a>
Specifies that you want details about invitations only for the resource shares described by this list of [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html)
Type: Array of strings
Required: No

 ** [resourceShareInvitationArns](#API_GetResourceShareInvitations_RequestSyntax) **   <a name="ram-GetResourceShareInvitations-request-resourceShareInvitationArns"></a>
Specifies the [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the resource share invitations you want information about.
Type: Array of strings
Required: No

## Response Syntax
<a name="API_GetResourceShareInvitations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "resourceShareInvitations": [
      {
         "invitationTimestamp": number,
         "receiverAccountId": "string",
         "receiverArn": "string",
         "resourceShareArn": "string",
         "resourceShareAssociations": [
            {
               "associatedEntity": "string",
               "associationType": "string",
               "creationTime": number,
               "external": boolean,
               "lastUpdatedTime": number,
               "resourceShareArn": "string",
               "resourceShareName": "string",
               "status": "string",
               "statusMessage": "string"
            }
         ],
         "resourceShareInvitationArn": "string",
         "resourceShareName": "string",
         "senderAccountId": "string",
         "status": "string"
      }
   ]
}
```

## Response Elements
<a name="API_GetResourceShareInvitations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_GetResourceShareInvitations_ResponseSyntax) **   <a name="ram-GetResourceShareInvitations-response-nextToken"></a>
If present, this value indicates that more output is available than is included in the current response. Use this value in the `NextToken` request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the `NextToken` response element comes back as `null`. This indicates that this is the last page of results.
Type: String

 ** [resourceShareInvitations](#API_GetResourceShareInvitations_ResponseSyntax) **   <a name="ram-GetResourceShareInvitations-response-resourceShareInvitations"></a>
An array of objects that contain the details about the invitations.
Type: Array of [ResourceShareInvitation](API_ResourceShareInvitation.md) objects

## Errors
<a name="API_GetResourceShareInvitations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidMaxResultsException **
The operation failed because the specified value for `MaxResults` isn't valid.
HTTP Status Code: 400

 ** InvalidNextTokenException **
The operation failed because the specified value for `NextToken` isn't valid. You must specify a value you received in the `NextToken` response of a previous call to this operation.
HTTP Status Code: 400

 ** InvalidParameterException **
The operation failed because a parameter you specified isn't valid.
HTTP Status Code: 400

 ** MalformedArnException **
The operation failed because the specified [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) has a format that isn't valid.
HTTP Status Code: 400

 ** ResourceShareInvitationArnNotFoundException **
The operation failed because the specified [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) for an invitation was not found.
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

## Examples
<a name="API_GetResourceShareInvitations_Examples"></a>

**Note**
The examples show the JSON payloads of the request and response pretty printed with white spaces and line breaks for ease for ease of reading.

### Example
<a name="API_GetResourceShareInvitations_Example_1"></a>

The following example shows an AWS account 111111111111 retrieving a list of its currently available invitations in the `us-east-1` Region. The response includes one `PENDING` invitation from AWS account 999999999999.

#### Sample Request
<a name="API_GetResourceShareInvitations_Example_1_Request"></a>

```
POST /getresourceshareinvitations HTTP/1.1
Host: ram.us-east-1.amazonaws.com
Accept-Encoding: identity
User-Agent: <UserAgentString>
Content-Length: <PayloadSizeBytes>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>>
```

#### Sample Response
<a name="API_GetResourceShareInvitations_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Wed, 22 Sep 2021 21:11:46 GMT
Content-Type: application/json
Content-Length: <PayloadSizeBytes>

{
    "resourceShareInvitations": [
        {
            "invitationTimestamp": 1632342984.382,
            "receiverAccountId": "111111111111",
            "resourceShareArn": "arn:aws:ram:us-east-1:999999999999:resource-share/27d09b4b-5e12-41d1-a4f2-19ded10982e2",
            "resourceShareInvitationArn": "arn:aws:ram:us-east-1:999999999999:resource-share-invitation/1e3477be-4a95-46b4-bbe0-c400156cd8e6",
            "resourceShareName": "MyLicenseShare",
            "senderAccountId": "999999999999",
            "status": "PENDING"
        }
    ]
}
```

## See Also
<a name="API_GetResourceShareInvitations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ram-2018-01-04/GetResourceShareInvitations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ram-2018-01-04/GetResourceShareInvitations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ram-2018-01-04/GetResourceShareInvitations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ram-2018-01-04/GetResourceShareInvitations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ram-2018-01-04/GetResourceShareInvitations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ram-2018-01-04/GetResourceShareInvitations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ram-2018-01-04/GetResourceShareInvitations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ram-2018-01-04/GetResourceShareInvitations)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ram-2018-01-04/GetResourceShareInvitations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ram-2018-01-04/GetResourceShareInvitations)
