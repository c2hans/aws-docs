---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeElasticGpus.html
---

# DescribeElasticGpus
<a name="API_DescribeElasticGpus"></a>

**Note**
Amazon Elastic Graphics reached end of life on January 8, 2024.

Describes the Elastic Graphics accelerator associated with your instances.

## Request Parameters
<a name="API_DescribeElasticGpus_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **ElasticGpuId.N**
The Elastic Graphics accelerator IDs.
Type: Array of strings
Required: No

 **Filter.N**
The filters.
+  `availability-zone` - The Availability Zone in which the Elastic Graphics accelerator resides.
+  `elastic-gpu-health` - The status of the Elastic Graphics accelerator (`OK` \| `IMPAIRED`).
+  `elastic-gpu-state` - The state of the Elastic Graphics accelerator (`ATTACHED`).
+  `elastic-gpu-type` - The type of Elastic Graphics accelerator; for example, `eg1.medium`.
+  `instance-id` - The ID of the instance to which the Elastic Graphics accelerator is associated.
Type: Array of [Filter](API_Filter.md) objects
Required: No

 **MaxResults**
The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned `NextToken` value. This value can be between 5 and 1000.
Type: Integer
Valid Range: Minimum value of 10. Maximum value of 1000.
Required: No

 **NextToken**
The token to request the next page of results.
Type: String
Required: No

## Response Elements
<a name="API_DescribeElasticGpus_ResponseElements"></a>

The following elements are returned by the service.

 **elasticGpuSet**
Information about the Elastic Graphics accelerators.
Type: Array of [ElasticGpus](API_ElasticGpus.md) objects

 **maxResults**
The total number of items to return. If the total number of items available is more than the value specified in max-items then a Next-Token will be provided in the output that you can use to resume pagination.
Type: Integer

 **nextToken**
The token to use to retrieve the next page of results. This value is `null` when there are no more results to return.
Type: String

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_DescribeElasticGpus_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribeElasticGpus_Examples"></a>

### Example
<a name="API_DescribeElasticGpus_Example_1"></a>

This example describes all of the Elastic Graphics accelerators associated with your instances.

#### Sample Request
<a name="API_DescribeElasticGpus_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribeElasticGpus
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeElasticGpus_Example_1_Response"></a>

```
<DescribeElasticGpusResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
<requestId>450268ba-0e1d-4401-958e-9a3example</requestId>
  <elasticGpuSet>
     <item>
        <elasticGpuId>egpu-0833fd743e7227123</elasticGpuId>
        <availabilityZone>us-east-1a</availabilityZone>
        <elasticGpuType>eg1.small</elasticGpuType>
        <elasticGpuHealth>OK</elasticGpuHealth>
        <elasticGpuState>ATTACHED</elasticGpuState>
        <instanceId>i-1234567890abc1234</instanceId>
      </item>
  </elasticGpuSet>
</DescribeElasticGpusResponse>
```

## See Also
<a name="API_DescribeElasticGpus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribeElasticGpus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribeElasticGpus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribeElasticGpus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribeElasticGpus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribeElasticGpus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribeElasticGpus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribeElasticGpus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribeElasticGpus)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribeElasticGpus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribeElasticGpus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
