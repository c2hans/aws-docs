---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DisableSnapshotBlockPublicAccess.html
---

# DisableSnapshotBlockPublicAccess
<a name="API_DisableSnapshotBlockPublicAccess"></a>

Disables the *block public access for snapshots* setting at the account level for the specified AWS Region. After you disable block public access for snapshots in a Region, users can publicly share snapshots in that Region.

**Important**
Enabling block public access for snapshots in *block-all-sharing* mode does not change the permissions for snapshots that are already publicly shared. Instead, it prevents these snapshots from be publicly visible and publicly accessible. Therefore, the attributes for these snapshots still indicate that they are publicly shared, even though they are not publicly available.
If you disable block public access , these snapshots will become publicly available again.

For more information, see [ Block public access for snapshots](https://docs.aws.amazon.com/ebs/latest/userguide/block-public-access-snapshots.html) in the *Amazon EBS User Guide* .

## Request Parameters
<a name="API_DisableSnapshotBlockPublicAccess_RequestParameters"></a>

For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

## Response Elements
<a name="API_DisableSnapshotBlockPublicAccess_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **state**
Returns `unblocked` if the request succeeds.
Type: String
Valid Values: `block-all-sharing | block-new-sharing | unblocked`

## Errors
<a name="API_DisableSnapshotBlockPublicAccess_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_DisableSnapshotBlockPublicAccess_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DisableSnapshotBlockPublicAccess)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DisableSnapshotBlockPublicAccess)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DisableSnapshotBlockPublicAccess)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DisableSnapshotBlockPublicAccess)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DisableSnapshotBlockPublicAccess)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DisableSnapshotBlockPublicAccess)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DisableSnapshotBlockPublicAccess)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DisableSnapshotBlockPublicAccess)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DisableSnapshotBlockPublicAccess)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DisableSnapshotBlockPublicAccess)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
