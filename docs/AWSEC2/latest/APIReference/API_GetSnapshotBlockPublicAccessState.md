---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetSnapshotBlockPublicAccessState.html
---

# GetSnapshotBlockPublicAccessState
<a name="API_GetSnapshotBlockPublicAccessState"></a>

Gets the current state of *block public access for snapshots* setting for the account and Region.

For more information, see [ Block public access for snapshots](https://docs.aws.amazon.com/ebs/latest/userguide/block-public-access-snapshots.html) in the *Amazon EBS User Guide*.

## Request Parameters
<a name="API_GetSnapshotBlockPublicAccessState_RequestParameters"></a>

For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

## Response Elements
<a name="API_GetSnapshotBlockPublicAccessState_ResponseElements"></a>

The following elements are returned by the service.

 **managedBy**
The entity that manages the state for block public access for snapshots. Possible values include:
+  `account` - The state is managed by the account.
+  `declarative-policy` - The state is managed by a declarative policy and can't be modified by the account.
Type: String
Valid Values: `account | declarative-policy`

 **requestId**
The ID of the request.
Type: String

 **state**
The current state of block public access for snapshots. Possible values include:
+  `block-all-sharing` - All public sharing of snapshots is blocked. Users in the account can't request new public sharing. Additionally, snapshots that were already publicly shared are treated as private and are not publicly available.
+  `block-new-sharing` - Only new public sharing of snapshots is blocked. Users in the account can't request new public sharing. However, snapshots that were already publicly shared, remain publicly available.
+  `unblocked` - Public sharing is not blocked. Users can publicly share snapshots.
Type: String
Valid Values: `block-all-sharing | block-new-sharing | unblocked`

## Errors
<a name="API_GetSnapshotBlockPublicAccessState_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_GetSnapshotBlockPublicAccessState_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/GetSnapshotBlockPublicAccessState)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/GetSnapshotBlockPublicAccessState)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/GetSnapshotBlockPublicAccessState)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/GetSnapshotBlockPublicAccessState)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/GetSnapshotBlockPublicAccessState)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/GetSnapshotBlockPublicAccessState)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/GetSnapshotBlockPublicAccessState)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/GetSnapshotBlockPublicAccessState)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/GetSnapshotBlockPublicAccessState)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/GetSnapshotBlockPublicAccessState)
