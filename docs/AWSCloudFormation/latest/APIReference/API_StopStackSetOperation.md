---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_StopStackSetOperation.html
---

# StopStackSetOperation
<a name="API_StopStackSetOperation"></a>

Stops an in-progress operation on a StackSet and its associated stack instances. StackSets will cancel all the unstarted stack instance deployments and wait for those are in-progress to complete.

## Request Parameters
<a name="API_StopStackSetOperation_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** CallAs **
Specifies whether you are acting as an account administrator in the organization's management account or as a delegated administrator in a member account. Valid only if the StackSet uses service-managed permissions.
By default, `SELF` is specified. Use `SELF` for StackSets with self-managed permissions.
+ If you are signed in to the management account, specify `SELF`.
+ If you are signed in to a delegated administrator account, specify `DELEGATED_ADMIN`.

  Your AWS account must be registered as a delegated administrator in the management account. For more information, see [Register a delegated administrator](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html) in the * AWS CloudFormation User Guide*.
Type: String
Valid Values: `SELF | DELEGATED_ADMIN`
Required: No

 ** OperationId **
The ID of the stack operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9][-a-zA-Z0-9]*`
Required: Yes

 ** StackSetName **
The name or unique ID of the StackSet that you want to stop the operation for.
Type: String
Required: Yes

## Errors
<a name="API_StopStackSetOperation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidOperation **
The specified operation isn't valid.
HTTP Status Code: 400

 ** OperationNotFound **
The specified ID refers to an operation that doesn't exist.
HTTP Status Code: 404

 ** StackSetNotFound **
The specified StackSet doesn't exist.
HTTP Status Code: 404

## Examples
<a name="API_StopStackSetOperation_Examples"></a>

### StopStackSetOperation
<a name="API_StopStackSetOperation_Example_1"></a>

This example illustrates one usage of StopStackSetOperation.

#### Sample Request
<a name="API_StopStackSetOperation_Example_1_Request"></a>

```
https://cloudformation.us-east-1.amazonaws.com/
 ?Action=StopStackSetOperation
 &Version=2010-05-15
 &StackSetName=stack-set-example
 &OperationId=61806005-bde9-46f1-949d-6791example
 &X-Amz-Algorithm=AWS4-HMAC-SHA256
 &X-Amz-Credential=[Access key ID and scope]
 &X-Amz-Date=20170810T233349Z
 &X-Amz-SignedHeaders=content-type;host
 &X-Amz-Signature=[Signature]
```

#### Sample Response
<a name="API_StopStackSetOperation_Example_1_Response"></a>

```
<StopStackSetOperationResponse xmlns="http://internal.amazon.com/coral/com.amazonaws.maestro.service.v20160713/">
  <StopStackSetOperationResult/>
  <ResponseMetadata>
    <RequestId>dded5cd7-8140-11e7-bc66-f9191example</RequestId>
  </ResponseMetadata>
</StopStackSetOperationResponse>
```

## See Also
<a name="API_StopStackSetOperation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/StopStackSetOperation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudformation-2010-05-15/StopStackSetOperation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/StopStackSetOperation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/StopStackSetOperation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/StopStackSetOperation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/StopStackSetOperation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/StopStackSetOperation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/StopStackSetOperation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/StopStackSetOperation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/StopStackSetOperation)
