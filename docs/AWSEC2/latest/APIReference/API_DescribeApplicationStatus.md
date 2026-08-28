---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeApplicationStatus.html
---

# DescribeApplicationStatus
<a name="API_DescribeApplicationStatus"></a>

Describes the aggregated application health status for the specified instances. The following rules apply:
+ The instance-level status is derived from all application status checks with the aggregation setting set to `included`.
+ Use `DescribeApplicationStatusChecks` to view the configuration of individual checks.
+ Use `EnableApplicationStatusCheckSuppression` to temporarily suppress health check results from affecting the instance-level status.

## Request Parameters
<a name="API_DescribeApplicationStatus_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Filter.N**
The filters.
+  `availability-zone-id` – The ID of the Availability Zone.
+  `status` – The instance-level application status. For valid values and their meanings, see `ApplicationStatus`.
Type: Array of [Filter](API_Filter.md) objects
Required: No

 **InstanceId.N**
The IDs of the instances for which to describe application status.
Type: Array of strings
Required: No

 **MaxResults**
The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see [Pagination](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination).
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 **NextToken**
The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.
Type: String
Required: No

## Response Elements
<a name="API_DescribeApplicationStatus_ResponseElements"></a>

The following elements are returned by the service.

 **applicationStatusesResponseType**
The application statuses for the specified instances.
Type: [ApplicationStatusesResponseType](API_ApplicationStatusesResponseType.md) object

 **nextToken**
The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.
Type: String

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_DescribeApplicationStatus_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribeApplicationStatus_Examples"></a>

### To describe application status for instances
<a name="API_DescribeApplicationStatus_Example_1"></a>

This example describes the application status for the specified instance.

#### Sample Request
<a name="API_DescribeApplicationStatus_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribeApplicationStatus
&InstanceId.1=i-0123456789abcdef0
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeApplicationStatus_Example_1_Response"></a>

```
<DescribeApplicationStatusResult xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>59dbff89-35bd-4eac-99ed-be587EXAMPLE</requestId>
    <applicationStatusesResponseType>
        <instanceSet>
            <item>
                <instanceId>i-0123456789abcdef0</instanceId>
                <applicationStatus>
                    <status>ok</status>
                </applicationStatus>
            </item>
        </instanceSet>
    </applicationStatusesResponseType>
</DescribeApplicationStatusResult>
```

## See Also
<a name="API_DescribeApplicationStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribeApplicationStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribeApplicationStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribeApplicationStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribeApplicationStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribeApplicationStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribeApplicationStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribeApplicationStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribeApplicationStatus)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribeApplicationStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribeApplicationStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
