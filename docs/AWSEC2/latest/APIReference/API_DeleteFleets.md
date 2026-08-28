---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteFleets.html
---

# DeleteFleets
<a name="API_DeleteFleets"></a>

Deletes the specified EC2 Fleet request.

After you delete an EC2 Fleet request, it launches no new instances.

You must also specify whether a deleted EC2 Fleet request should terminate its instances. If you choose to terminate the instances, the EC2 Fleet request enters the `deleted_terminating` state. Otherwise, it enters the `deleted_running` state, and the instances continue to run until they are interrupted or you terminate them manually.

A deleted `instant` fleet with running instances is not supported. When you delete an `instant` fleet, Amazon EC2 automatically terminates all its instances. For fleets with more than 1000 instances, the deletion request might fail. If your fleet has more than 1000 instances, first terminate most of the instances manually, leaving 1000 or fewer. Then delete the fleet, and the remaining instances will be terminated automatically.

**Important**
 **Terminating an instance is permanent and irreversible.**
After you terminate an instance, you can no longer connect to it, and it can't be recovered. All attached Amazon EBS volumes that are configured to be deleted on termination are also permanently deleted and can't be recovered. All data stored on instance store volumes is permanently lost. For more information, see [ How instance termination works](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/how-ec2-instance-termination-works.html).
Before you terminate an instance, ensure that you have backed up all data that you need to retain after the termination to persistent storage.

**Restrictions**
+ You can delete up to 25 fleets of type `instant` in a single request.
+ You can delete up to 100 fleets of type `maintain` or `request` in a single request.
+ You can delete up to 125 fleets in a single request, provided you do not exceed the quota for each fleet type, as specified above.
+ If you exceed the specified number of fleets to delete, no fleets are deleted.

For more information, see [Delete an EC2 Fleet request and the instances in the fleet](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/delete-fleet.html) in the *Amazon EC2 User Guide*.

## Request Parameters
<a name="API_DeleteFleets_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **FleetId.N**
The IDs of the EC2 Fleets.
Constraints: In a single request, you can specify up to 25 `instant` fleet IDs and up to 100 `maintain` or `request` fleet IDs.
Type: Array of strings
Required: Yes

 **TerminateInstances**
Indicates whether to terminate the associated instances when the EC2 Fleet is deleted. The default is to terminate the instances.
To let the instances continue to run after the EC2 Fleet is deleted, specify `no-terminate-instances`. Supported only for fleets of type `maintain` and `request`.
For `instant` fleets, you cannot specify `NoTerminateInstances`. A deleted `instant` fleet with running instances is not supported.
Type: Boolean
Required: Yes

## Response Elements
<a name="API_DeleteFleets_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **successfulFleetDeletionSet**
Information about the EC2 Fleets that are successfully deleted.
Type: Array of [DeleteFleetSuccessItem](API_DeleteFleetSuccessItem.md) objects

 **unsuccessfulFleetDeletionSet**
Information about the EC2 Fleets that are not successfully deleted.
Type: Array of [DeleteFleetErrorItem](API_DeleteFleetErrorItem.md) objects

## Errors
<a name="API_DeleteFleets_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_DeleteFleets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DeleteFleets)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DeleteFleets)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DeleteFleets)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DeleteFleets)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DeleteFleets)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DeleteFleets)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DeleteFleets)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DeleteFleets)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DeleteFleets)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DeleteFleets)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
