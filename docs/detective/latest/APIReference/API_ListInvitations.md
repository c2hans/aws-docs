---
source_url: https://docs.aws.amazon.com/detective/latest/APIReference/API_ListInvitations.html
---

# ListInvitations
<a name="API_ListInvitations"></a>

Retrieves the list of open and accepted behavior graph invitations for the member account. This operation can only be called by an invited member account.

Open invitations are invitations that the member account has not responded to.

The results do not include behavior graphs for which the member account declined the invitation. The results also do not include behavior graphs that the member account resigned from or was removed from.

## Request Syntax
<a name="API_ListInvitations_RequestSyntax"></a>

```
POST /invitations/list HTTP/1.1
Content-type: application/json

{
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListInvitations_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListInvitations_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListInvitations_RequestSyntax) **   <a name="detective-ListInvitations-request-MaxResults"></a>
The maximum number of behavior graph invitations to return in the response. The total must be less than the overall limit on the number of results to return, which is currently 200.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 200.
Required: No

 ** [NextToken](#API_ListInvitations_RequestSyntax) **   <a name="detective-ListInvitations-request-NextToken"></a>
For requests to retrieve the next page of results, the pagination token that was returned with the previous page of results. The initial request does not include a pagination token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## Response Syntax
<a name="API_ListInvitations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Invitations": [
      {
         "AccountId": "string",
         "AdministratorId": "string",
         "DatasourcePackageIngestStates": {
            "string" : "string"
         },
         "DisabledReason": "string",
         "EmailAddress": "string",
         "GraphArn": "string",
         "InvitationType": "string",
         "InvitedTime": "string",
         "MasterId": "string",
         "PercentOfGraphUtilization": number,
         "PercentOfGraphUtilizationUpdatedTime": "string",
         "Status": "string",
         "UpdatedTime": "string",
         "VolumeUsageByDatasourcePackage": {
            "string" : {
               "VolumeUsageInBytes": number,
               "VolumeUsageUpdateTime": "string"
            }
         },
         "VolumeUsageInBytes": number,
         "VolumeUsageUpdatedTime": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListInvitations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Invitations](#API_ListInvitations_ResponseSyntax) **   <a name="detective-ListInvitations-response-Invitations"></a>
The list of behavior graphs for which the member account has open or accepted invitations.
Type: Array of [MemberDetail](API_MemberDetail.md) objects

 ** [NextToken](#API_ListInvitations_ResponseSyntax) **   <a name="detective-ListInvitations-response-NextToken"></a>
If there are more behavior graphs remaining in the results, then this is the pagination token to use to request the next page of behavior graphs.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_ListInvitations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request issuer does not have permission to access this resource or perform this operation.
 ** ErrorCode **
The SDK default error code associated with the access denied exception.
 ** ErrorCodeReason **
The SDK default explanation of why access was denied.
 ** SubErrorCode **
The error code associated with the access denied exception.
 ** SubErrorCodeReason **
 An explanation of why access was denied.
HTTP Status Code: 403

 ** InternalServerException **
The request was valid but failed because of a problem with the service.
HTTP Status Code: 500

 ** ValidationException **
The request parameters are invalid.
 ** ErrorCode **
The error code associated with the validation failure.
 ** ErrorCodeReason **
 An explanation of why validation failed.
HTTP Status Code: 400

## Examples
<a name="API_ListInvitations_Examples"></a>

### Example
<a name="API_ListInvitations_Example_1"></a>

This example illustrates one usage of ListInvitations.

#### Sample Request
<a name="API_ListInvitations_Example_1_Request"></a>

```
POST /invitations/list HTTP/1.1
Host: api.detective.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 0
Authorization: AUTHPARAMS
X-Amz-Date: 20200124T193018Z
User-Agent: aws-cli/1.14.29 Python/2.7.9 Windows/8 botocore/1.8.33
```

### Example
<a name="API_ListInvitations_Example_2"></a>

This example illustrates one usage of ListInvitations.

#### Sample Response
<a name="API_ListInvitations_Example_2_Response"></a>

```
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 302
Date: Fri, 24 Jan 2020 23:07:46 GMT
x-amzn-RequestId: 397d0549-0092-11e8-a0ee-a7f9aa6e7572
Connection: Keep-alive

{
 "Invitations": [
 {
  "AccountId": "444455556666",
  "AdministratorId": "111122223333",
  "EmailAddress": "mmajor@example.com",
  "GraphArn": "arn:aws:detective:us-east-1:111122223333:graph:027c7c4610ea4aacaf0b883093cab899",
  "InvitedTime": "2020-01-24T12:35:0.1587Z",
  "MasterId": "111122223333",
  "Status": "INVITED",
  "UpdatedTime": "2020-01-24T12:35:0.1587Z"
 }
 ]
}
```

## See Also
<a name="API_ListInvitations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/detective-2018-10-26/ListInvitations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/detective-2018-10-26/ListInvitations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/detective-2018-10-26/ListInvitations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/detective-2018-10-26/ListInvitations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/detective-2018-10-26/ListInvitations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/detective-2018-10-26/ListInvitations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/detective-2018-10-26/ListInvitations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/detective-2018-10-26/ListInvitations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/detective-2018-10-26/ListInvitations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/detective-2018-10-26/ListInvitations)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Detective. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query detective` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
