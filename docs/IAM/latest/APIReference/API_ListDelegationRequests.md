---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListDelegationRequests.html
---

# ListDelegationRequests
<a name="API_ListDelegationRequests"></a>

Lists delegation requests based on the specified criteria.

If a delegation request has no owner, even if it is assigned to a specific account, it will not be part of the `ListDelegationRequests` output for that account.

 For more details, see [ Managing Permissions for Delegation Requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies-temporary-delegation.html#temporary-delegation-managing-permissions).

## Request Parameters
<a name="API_ListDelegationRequests_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** Marker **
Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the `Marker` element in the response that you received to indicate where the next call should start.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 320.
Pattern: `[\u0020-\u00FF]+`
Required: No

 ** MaxItems **
Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the `IsTruncated` response element is `true`.
If you do not include this parameter, the number of items defaults to 100. Note that IAM may return fewer results, even when there are more results available. In that case, the `IsTruncated` response element returns `true`, and `Marker` contains a value to include in the subsequent call that tells the service where to continue from.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** OwnerId **
The owner ID to filter delegation requests by.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^[a-zA-Z0-9:/+=,.@_-]+$`
Required: No

## Response Elements
<a name="API_ListDelegationRequests_ResponseElements"></a>

The following elements are returned by the service.

 **DelegationRequests.member.N**
A list of delegation requests that match the specified criteria.
Type: Array of [DelegationRequest](API_DelegationRequest.md) objects

 ** isTruncated **
A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent pagination request using the `Marker` request parameter to retrieve more items.
Type: Boolean

 ** Marker **
When `isTruncated` is `true`, this element is present and contains the value to use for the `Marker` parameter in a subsequent pagination request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 320.
Pattern: `[\u0020-\u00FF]+`

## Errors
<a name="API_ListDelegationRequests_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInput **
The request was rejected because an invalid or out-of-range value was supplied for an input parameter.
HTTP Status Code: 400

 ** NoSuchEntity **
The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
HTTP Status Code: 404

 ** ServiceFailure **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

## Examples
<a name="API_ListDelegationRequests_Examples"></a>

### Example
<a name="API_ListDelegationRequests_Example_1"></a>

This example illustrates one usage of ListDelegationRequests.

#### Sample Request
<a name="API_ListDelegationRequests_Example_1_Request"></a>

```
https://iam.amazonaws.com/?Action=ListDelegationRequests
&Version=2010-05-08
&AUTHPARAMS
```

#### Sample Response
<a name="API_ListDelegationRequests_Example_1_Response"></a>

```
<ListDelegationRequestsResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
  <ListDelegationRequestsResult>
    <isTruncated>false</isTruncated>
    <DelegationRequests>
      <member>
        <UpdatedTime>2025-11-16T00:00:00.00Z</UpdatedTime>
        <DelegationRequestId>e4bdcdae-4f66-11eD-ELEG-ATIONEXAMPLE</DelegationRequestId>
        <ApproverId>arn:aws:iam::112233445566:user/Admin</ApproverId>
        <Description>Example Request</Description>
        <OwnerId>arn:aws:iam::112233445566:user/Alice</OwnerId>
        <SessionDuration>3600</SessionDuration>
        <RequestorId>665544332211</RequestorId>
        <OwnerAccountId>112233445566</OwnerAccountId>
        <OnlySendByOwner>false</OnlySendByOwner>
        <State>REJECTED</State>
        <CreateDate>2025-11-16T01:00:00.00Z</CreateDate>
      </member>
    </DelegationRequests>
  </ListDelegationRequestsResult>
  <ResponseMetadata>
    <RequestId>e4bdcdae-4f66-11e4-aefa-bfd6aEXAMPLE</RequestId>
  </ResponseMetadata>
</ListDelegationRequestsResponse>
```

## See Also
<a name="API_ListDelegationRequests_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iam-2010-05-08/ListDelegationRequests)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iam-2010-05-08/ListDelegationRequests)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/ListDelegationRequests)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iam-2010-05-08/ListDelegationRequests)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/ListDelegationRequests)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iam-2010-05-08/ListDelegationRequests)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iam-2010-05-08/ListDelegationRequests)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iam-2010-05-08/ListDelegationRequests)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iam-2010-05-08/ListDelegationRequests)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/ListDelegationRequests)
