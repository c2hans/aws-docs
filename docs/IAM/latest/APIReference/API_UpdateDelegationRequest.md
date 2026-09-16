---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_UpdateDelegationRequest.html
---

# UpdateDelegationRequest
<a name="API_UpdateDelegationRequest"></a>

Updates an existing delegation request with additional information. When the delegation request is updated, it reaches the `PENDING_APPROVAL` state.

Once a delegation request has an owner, that owner gets a default permission to update the delegation request. For more details, see [ Managing Permissions for Delegation Requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies-temporary-delegation.html#temporary-delegation-managing-permissions).

## Request Parameters
<a name="API_UpdateDelegationRequest_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DelegationRequestId **
The unique identifier of the delegation request to update.
Type: String
Length Constraints: Minimum length of 16. Maximum length of 128.
Pattern: `[\w-]+`
Required: Yes

 ** Notes **
Additional notes or comments to add to the delegation request.
Type: String
Length Constraints: Maximum length of 500.
Pattern: `[\u0009\u000A\u000D\u0020-\u007E\u00A1-\u00FF]*`
Required: No

## Errors
<a name="API_UpdateDelegationRequest_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConcurrentModification **
The request was rejected because multiple requests to change this object were submitted simultaneously. Wait a few minutes and submit your request again.
HTTP Status Code: 409

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
<a name="API_UpdateDelegationRequest_Examples"></a>

### Example
<a name="API_UpdateDelegationRequest_Example_1"></a>

This example illustrates one usage of UpdateDelegationRequest.

#### Sample Request
<a name="API_UpdateDelegationRequest_Example_1_Request"></a>

```
https://iam.amazonaws.com/?Action=UpdateDelegationRequest
&DelegationRequestId=e4bdcdae-4f66-11eD-ELEG-ATIONEXAMPLE
&Notes=Additional%20Details
&Version=2010-05-08
&AUTHPARAMS
```

#### Sample Response
<a name="API_UpdateDelegationRequest_Example_1_Response"></a>

```
<UpdateDelegationRequestResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
  <ResponseMetadata>
    <RequestId>2cdd0b0b-d879-4bb8-a617-b75570d37854</RequestId>
  </ResponseMetadata>
</UpdateDelegationRequestResponse>
```

## See Also
<a name="API_UpdateDelegationRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iam-2010-05-08/UpdateDelegationRequest)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iam-2010-05-08/UpdateDelegationRequest)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/UpdateDelegationRequest)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iam-2010-05-08/UpdateDelegationRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/UpdateDelegationRequest)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iam-2010-05-08/UpdateDelegationRequest)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iam-2010-05-08/UpdateDelegationRequest)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iam-2010-05-08/UpdateDelegationRequest)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iam-2010-05-08/UpdateDelegationRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/UpdateDelegationRequest)
