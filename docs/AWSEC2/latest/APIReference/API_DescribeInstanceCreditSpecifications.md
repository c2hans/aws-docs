---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeInstanceCreditSpecifications.html
---

# DescribeInstanceCreditSpecifications
<a name="API_DescribeInstanceCreditSpecifications"></a>

Describes the credit option for CPU usage of the specified burstable performance instances. The credit options are `standard` and `unlimited`.

If you do not specify an instance ID, Amazon EC2 returns burstable performance instances with the `unlimited` credit option, as well as instances that were previously configured as T2, T3, and T3a with the `unlimited` credit option. For example, if you resize a T2 instance, while it is configured as `unlimited`, to an M4 instance, Amazon EC2 returns the M4 instance.

If you specify one or more instance IDs, Amazon EC2 returns the credit option (`standard` or `unlimited`) of those instances. If you specify an instance ID that is not valid, such as an instance that is not a burstable performance instance, an error is returned.

Recently terminated instances might appear in the returned results. This interval is usually less than one hour.

If an Availability Zone is experiencing a service disruption and you specify instance IDs in the affected zone, or do not specify any instance IDs at all, the call fails. If you specify only instance IDs in an unaffected zone, the call works normally.

For more information, see [Burstable performance instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-performance-instances.html) in the *Amazon EC2 User Guide*.

## Request Parameters
<a name="API_DescribeInstanceCreditSpecifications_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Filter.N**
The filters.
+  `instance-id` - The ID of the instance.
Type: Array of [Filter](API_Filter.md) objects
Required: No

 **InstanceId.N**
The instance IDs.
Default: Describes all your instances.
Constraints: Maximum 1000 explicitly specified instance IDs.
Type: Array of strings
Required: No

 **MaxResults**
The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see [Pagination](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination).
You cannot specify this parameter and the instance IDs parameter in the same call.
Type: Integer
Valid Range: Minimum value of 5. Maximum value of 1000.
Required: No

 **NextToken**
The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.
Type: String
Required: No

## Response Elements
<a name="API_DescribeInstanceCreditSpecifications_ResponseElements"></a>

The following elements are returned by the service.

 **instanceCreditSpecificationSet**
Information about the credit option for CPU usage of an instance.
Type: Array of [InstanceCreditSpecification](API_InstanceCreditSpecification.md) objects

 **nextToken**
The token to include in another request to get the next page of items. This value is `null` when there are no more items to return.
Type: String

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_DescribeInstanceCreditSpecifications_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribeInstanceCreditSpecifications_Examples"></a>

### Example
<a name="API_DescribeInstanceCreditSpecifications_Example_1"></a>

This request describes the current credit option for CPU usage of the specified instance.

#### Sample Request
<a name="API_DescribeInstanceCreditSpecifications_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribeInstanceCreditSpecifications
&InstanceId.1=i-1234567890abcdef0
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeInstanceCreditSpecifications_Example_1_Response"></a>

```
<DescribeInstanceCreditSpecificationsResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>1b234b5c-d6ef-7gh8-90i1-j2345678901</requestId>
    <instanceCreditSpecificationSet>
        <item>
            <cpuCredits>unlimited</cpuCredits>
            <instanceId>i-1234567890abcdef0</instanceId>
        </item>
    </instanceCreditSpecificationSet>
</DescribeInstanceCreditSpecificationsResponse>
```

## See Also
<a name="API_DescribeInstanceCreditSpecifications_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribeInstanceCreditSpecifications)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribeInstanceCreditSpecifications)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribeInstanceCreditSpecifications)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribeInstanceCreditSpecifications)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribeInstanceCreditSpecifications)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribeInstanceCreditSpecifications)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribeInstanceCreditSpecifications)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribeInstanceCreditSpecifications)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribeInstanceCreditSpecifications)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribeInstanceCreditSpecifications)
