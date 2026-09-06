---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetDelegationRequest.html
---

# GetDelegationRequest
<a name="API_GetDelegationRequest"></a>

Retrieves information about a specific delegation request.

 If a delegation request has no owner or owner account, `GetDelegationRequest` for that delegation request can be called by any account. If the owner account is assigned but there is no owner id, only identities within that owner account can call `GetDelegationRequest` for the delegation request. Once the delegation request is fully owned, the owner of the request gets a default permission to get that delegation request. For more details, see [ Managing Permissions for Delegation Requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies-temporary-delegation.html#temporary-delegation-managing-permissions).

## Request Parameters
<a name="API_GetDelegationRequest_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DelegationPermissionCheck **
Specifies whether to perform a permission check for the delegation request.
If set to true, the `GetDelegationRequest` API call will start a permission check process. This process calculates whether the caller has sufficient permissions to cover the asks from this delegation request.
Setting this parameter to true does not guarantee an answer in the response. See the `PermissionCheckStatus` and the `PermissionCheckResult` response attributes for further details.
Type: Boolean
Required: No

 ** DelegationRequestId **
The unique identifier of the delegation request to retrieve.
Type: String
Length Constraints: Minimum length of 16. Maximum length of 128.
Pattern: `[\w-]+`
Required: Yes

## Response Elements
<a name="API_GetDelegationRequest_ResponseElements"></a>

The following elements are returned by the service.

 ** DelegationRequest **
The delegation request object containing all details about the request.
Type: [DelegationRequest](API_DelegationRequest.md) object

 ** PermissionCheckResult **
The result of the permission check, indicating whether the caller has sufficient permissions to cover the requested permissions. This is an approximate result.
+  `ALLOWED` : The caller has sufficient permissions cover all the requested permissions.
+  `DENIED` : The caller does not have sufficient permissions to cover all the requested permissions.
+  `UNSURE` : It is not possible to determine whether the caller has all the permissions needed. This output is most likely for cases when the caller has permissions with conditions.
Type: String
Valid Values: `ALLOWED | DENIED | UNSURE`

 ** PermissionCheckStatus **
The status of the permission check for the delegation request.
This value indicates the status of the process to check whether the caller has sufficient permissions to cover the requested actions in the delegation request. Since this is an asynchronous process, there are three potential values:
+  `IN_PROGRESS` : The permission check process has started.
+  `COMPLETED` : The permission check process has completed. The `PermissionCheckResult` will include the result.
+  `FAILED` : The permission check process has failed.
Type: String
Valid Values: `COMPLETE | IN_PROGRESS | FAILED`

## Errors
<a name="API_GetDelegationRequest_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** NoSuchEntity **
The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
HTTP Status Code: 404

 ** ServiceFailure **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

## Examples
<a name="API_GetDelegationRequest_Examples"></a>

### Example
<a name="API_GetDelegationRequest_Example_1"></a>

This example illustrates one usage of GetDelegationRequest.

#### Sample Request
<a name="API_GetDelegationRequest_Example_1_Request"></a>

```
https://iam.amazonaws.com/?Action=GetDelegationRequest
&DelegationRequestId=e4bdcdae-4f66-11eD-ELEG-ATIONEXAMPLE
&Version=2010-05-08
&AUTHPARAMS
```

#### Sample Response
<a name="API_GetDelegationRequest_Example_1_Response"></a>

```
<GetDelegationRequestResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
  <GetDelegationRequestResult>
    <DelegationRequest>
      <UpdatedTime>2025-11-16T00:00:00.570Z</UpdatedTime>
        <DelegationRequestId>e4bdcdae-4f66-11eD-ELEG-ATIONEXAMPLE</DelegationRequestId>
          <Description>Example Request</Description>
          <SessionDuration>3600</SessionDuration>
          <RequestorId>112233445566</RequestorId>
          <OnlySendByOwner>false</OnlySendByOwner>
          <PermissionPolicy>
             {
                "Statement": [
                  {
                    "Sid": "IAMAll",
                    "Effect": "Allow",
                    "Action": [
                      "iam:*"
                    ],
                    "Resource": [
                      "*"
                    ]
                  }
                ]
              }
          </PermissionPolicy>
          <RolePermissionRestrictionArns/>
          <State>UNASSIGNED</State>
          <ExpirationTime>2025-11-17T00:00:00.570Z</ExpirationTime>
          <RequestorName>RequestorFriendlyName</RequestorName>
          <CreateDate>2025-11-16T00:00:00.570Z</CreateDate>
        </DelegationRequest>
    </GetDelegationRequestResult>
    <ResponseMetadata>
      <RequestId>e4bdcdae-4f66-11e4-aefa-bfd6aEXAMPLE</RequestId>
    </ResponseMetadata>
</GetDelegationRequestResponse>
```

## See Also
<a name="API_GetDelegationRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iam-2010-05-08/GetDelegationRequest)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iam-2010-05-08/GetDelegationRequest)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/GetDelegationRequest)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iam-2010-05-08/GetDelegationRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/GetDelegationRequest)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iam-2010-05-08/GetDelegationRequest)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iam-2010-05-08/GetDelegationRequest)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iam-2010-05-08/GetDelegationRequest)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iam-2010-05-08/GetDelegationRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/GetDelegationRequest)
