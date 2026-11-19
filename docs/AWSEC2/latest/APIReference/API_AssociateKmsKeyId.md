---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AssociateKmsKeyId.html
---

# AssociateKmsKeyId

Associates an additional AWS KMS key with an encrypted Amazon EBS snapshot. With the associated key, you have a second, independent way to access the snapshot's data, in addition to the key the snapshot is already encrypted under. Associating a key doesn't re-encrypt the snapshot or grant access to its original key.

For more information, see [Associated KMS keys](https://docs.aws.amazon.com/ebs/latest/userguide/associated-kms-keys.html) in the *Amazon EBS User Guide*.

## Request Parameters
<a name="API_AssociateKmsKeyId_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **KmsKeyId**
The ID, alias, or ARN of the AWS KMS key to associate with the snapshot. You can specify a key ID, key alias, key ARN, or alias ARN.
Type: String
Required: Yes

 **SnapshotId**
The ID of the Amazon EBS snapshot.
Type: String
Required: No

## Response Elements
<a name="API_AssociateKmsKeyId_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **return**
Returns `true` if the request succeeds; otherwise, it returns an error.
Type: Boolean

## Errors
<a name="API_AssociateKmsKeyId_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_AssociateKmsKeyId_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/AssociateKmsKeyId)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/AssociateKmsKeyId)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/AssociateKmsKeyId)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/AssociateKmsKeyId)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/AssociateKmsKeyId)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/AssociateKmsKeyId)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/AssociateKmsKeyId)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/AssociateKmsKeyId)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/AssociateKmsKeyId)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/AssociateKmsKeyId)
