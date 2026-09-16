---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_UpdateCapacityManagerOrganizationsAccess.html
---

# UpdateCapacityManagerOrganizationsAccess
<a name="API_UpdateCapacityManagerOrganizationsAccess"></a>

 Updates the Organizations access setting for EC2 Capacity Manager. This controls whether Capacity Manager can aggregate data from all accounts in your AWS Organization or only from the current account.

## Request Parameters
<a name="API_UpdateCapacityManagerOrganizationsAccess_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **ClientToken**
 Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
Type: String
Required: No

 **DryRun**
 Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **OrganizationsAccess**
 Specifies whether to enable or disable cross-account access for AWS Organizations. When enabled, Capacity Manager aggregates data from all accounts in your organization.
Type: Boolean
Required: Yes

## Response Elements
<a name="API_UpdateCapacityManagerOrganizationsAccess_ResponseElements"></a>

The following elements are returned by the service.

 **capacityManagerStatus**
 The current status of Capacity Manager after the update operation.
Type: String
Valid Values: `enabled | disabled`

 **organizationsAccess**
 The updated Organizations access setting indicating whether cross-account data aggregation is enabled.
Type: Boolean

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_UpdateCapacityManagerOrganizationsAccess_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_UpdateCapacityManagerOrganizationsAccess_Examples"></a>

### Example
<a name="API_UpdateCapacityManagerOrganizationsAccess_Example_1"></a>

This example enables Organizations access for cross-account data aggregation.

#### Sample Request
<a name="API_UpdateCapacityManagerOrganizationsAccess_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=UpdateCapacityManagerOrganizationsAccess
&OrganizationsAccess=true
&AUTHPARAMS
```

#### Sample Response
<a name="API_UpdateCapacityManagerOrganizationsAccess_Example_1_Response"></a>

```
<UpdateCapacityManagerOrganizationsAccessResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>d4904fd9-82c2-4ea5-adfe-a9cc3EXAMPLE</requestId>
    <capacityManagerStatus>enabled</capacityManagerStatus>
    <organizationsAccess>true</organizationsAccess>
</UpdateCapacityManagerOrganizationsAccessResponse>
```

## See Also
<a name="API_UpdateCapacityManagerOrganizationsAccess_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/UpdateCapacityManagerOrganizationsAccess)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/UpdateCapacityManagerOrganizationsAccess)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/UpdateCapacityManagerOrganizationsAccess)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/UpdateCapacityManagerOrganizationsAccess)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/UpdateCapacityManagerOrganizationsAccess)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/UpdateCapacityManagerOrganizationsAccess)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/UpdateCapacityManagerOrganizationsAccess)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/UpdateCapacityManagerOrganizationsAccess)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/UpdateCapacityManagerOrganizationsAccess)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/UpdateCapacityManagerOrganizationsAccess)
