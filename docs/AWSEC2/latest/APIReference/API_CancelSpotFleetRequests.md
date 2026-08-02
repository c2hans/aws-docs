---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CancelSpotFleetRequests.html
---

# CancelSpotFleetRequests
<a name="API_CancelSpotFleetRequests"></a>

Cancels the specified Spot Fleet requests.

After you cancel a Spot Fleet request, the Spot Fleet launches no new instances.

You must also specify whether a canceled Spot Fleet request should terminate its instances. If you choose to terminate the instances, the Spot Fleet request enters the `cancelled_terminating` state. Otherwise, the Spot Fleet request enters the `cancelled_running` state and the instances continue to run until they are interrupted or you terminate them manually.

**Important**
 **Terminating an instance is permanent and irreversible.**
After you terminate an instance, you can no longer connect to it, and it can't be recovered. All attached Amazon EBS volumes that are configured to be deleted on termination are also permanently deleted and can't be recovered. All data stored on instance store volumes is permanently lost. For more information, see [ How instance termination works](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/how-ec2-instance-termination-works.html).
Before you terminate an instance, ensure that you have backed up all data that you need to retain after the termination to persistent storage.

**Restrictions**
+ You can delete up to 100 fleets in a single request. If you exceed the specified number, no fleets are deleted.

## Request Parameters
<a name="API_CancelSpotFleetRequests_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **SpotFleetRequestId.N**
The IDs of the Spot Fleet requests.
Constraint: You can specify up to 100 IDs in a single request.
Type: Array of strings
Required: Yes

 **TerminateInstances**
Indicates whether to terminate the associated instances when the Spot Fleet request is canceled. The default is to terminate the instances.
To let the instances continue to run after the Spot Fleet request is canceled, specify `no-terminate-instances`.
Type: Boolean
Required: Yes

## Response Elements
<a name="API_CancelSpotFleetRequests_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **successfulFleetRequestSet**
Information about the Spot Fleet requests that are successfully canceled.
Type: Array of [CancelSpotFleetRequestsSuccessItem](API_CancelSpotFleetRequestsSuccessItem.md) objects

 **unsuccessfulFleetRequestSet**
Information about the Spot Fleet requests that are not successfully canceled.
Type: Array of [CancelSpotFleetRequestsErrorItem](API_CancelSpotFleetRequestsErrorItem.md) objects

## Errors
<a name="API_CancelSpotFleetRequests_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_CancelSpotFleetRequests_Examples"></a>

### Example
<a name="API_CancelSpotFleetRequests_Example_1"></a>

This example cancels Spot Fleet request sfr-123f8fc2-cb31-425e-abcd-example2710 and terminates all instances that were launched by the request.

#### Sample Request
<a name="API_CancelSpotFleetRequests_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=CancelSpotFleetRequests
&SpotFleetRequestId.1=sfr-123f8fc2-cb31-425e-abcd-example2710
&TerminateInstances=true
&AUTHPARAMS
```

#### Sample Response
<a name="API_CancelSpotFleetRequests_Example_1_Response"></a>

```
<CancelSpotFleetRequestsResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>e12d2fe5-6503-4b4b-911c-example</requestId>
    <unsuccessfulFleetRequestSet/>
    <successfulFleetRequestSet>
        <item>
            <spotFleetRequestId>sfr-123f8fc2-cb31-425e-abcd-example2710</spotFleetRequestId>
            <currentSpotFleetRequestState>cancelled_terminating</currentSpotFleetRequestState>
            <previousSpotFleetRequestState>active</previousSpotFleetRequestState>
        </item>
    </successfulFleetRequestSet>
</CancelSpotFleetRequestsResponse>
```

## See Also
<a name="API_CancelSpotFleetRequests_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/CancelSpotFleetRequests)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/CancelSpotFleetRequests)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CancelSpotFleetRequests)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/CancelSpotFleetRequests)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CancelSpotFleetRequests)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/CancelSpotFleetRequests)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/CancelSpotFleetRequests)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/CancelSpotFleetRequests)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/CancelSpotFleetRequests)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CancelSpotFleetRequests)
