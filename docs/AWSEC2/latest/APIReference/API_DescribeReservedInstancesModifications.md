---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeReservedInstancesModifications.html
---

# DescribeReservedInstancesModifications
<a name="API_DescribeReservedInstancesModifications"></a>

Describes the modifications made to your Reserved Instances. If no parameter is specified, information about all your Reserved Instances modification requests is returned. If a modification ID is specified, only information about the specific modification is returned.

For more information, see [Modify Reserved Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ri-modifying.html) in the *Amazon EC2 User Guide*.

**Note**
The order of the elements in the response, including those within nested structures, might vary. Applications should not assume the elements appear in a particular order.

## Request Parameters
<a name="API_DescribeReservedInstancesModifications_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **Filter.N**
One or more filters.
+  `client-token` - The idempotency token for the modification request.
+  `create-date` - The time when the modification request was created.
+  `effective-date` - The time when the modification becomes effective.
+  `modification-result.reserved-instances-id` - The ID for the Reserved Instances created as part of the modification request. This ID is only available when the status of the modification is `fulfilled`.
+  `modification-result.target-configuration.availability-zone` - The Availability Zone for the new Reserved Instances.
+  `modification-result.target-configuration.availability-zone-id` - The ID of the Availability Zone for the new Reserved Instances.
+  `modification-result.target-configuration.instance-count ` - The number of new Reserved Instances.
+  `modification-result.target-configuration.instance-type` - The instance type of the new Reserved Instances.
+  `reserved-instances-id` - The ID of the Reserved Instances modified.
+  `reserved-instances-modification-id` - The ID of the modification request.
+  `status` - The status of the Reserved Instances modification request (`processing` \| `fulfilled` \| `failed`).
+  `status-message` - The reason for the status.
+  `update-date` - The time when the modification request was last updated.
Type: Array of [Filter](API_Filter.md) objects
Required: No

 **NextToken**
The token to retrieve the next page of results.
Type: String
Required: No

 **ReservedInstancesModificationId.N**
IDs for the submitted modification request.
Type: Array of strings
Required: No

## Response Elements
<a name="API_DescribeReservedInstancesModifications_ResponseElements"></a>

The following elements are returned by the service.

 **nextToken**
The token to use to retrieve the next page of results. This value is `null` when there are no more results to return.
Type: String

 **requestId**
The ID of the request.
Type: String

 **reservedInstancesModificationsSet**
The Reserved Instance modification information.
Type: Array of [ReservedInstancesModification](API_ReservedInstancesModification.md) objects

## Errors
<a name="API_DescribeReservedInstancesModifications_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribeReservedInstancesModifications_Examples"></a>

### Example 1
<a name="API_DescribeReservedInstancesModifications_Example_1"></a>

This example illustrates one usage of DescribeReservedInstancesModifications.

#### Sample Request
<a name="API_DescribeReservedInstancesModifications_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribeReservedInstancesModifications
&AUTHPARAMS
```

### Example 2
<a name="API_DescribeReservedInstancesModifications_Example_2"></a>

This example filters the response to include only Reserved Instances modification requests with status `processing`.

#### Sample Request
<a name="API_DescribeReservedInstancesModifications_Example_2_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribeReservedInstancesModifications
&Filter.1.Name=status
&Filter.1.Value.1=processing
&AUTHPARAMS
```

## See Also
<a name="API_DescribeReservedInstancesModifications_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribeReservedInstancesModifications)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribeReservedInstancesModifications)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribeReservedInstancesModifications)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribeReservedInstancesModifications)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribeReservedInstancesModifications)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribeReservedInstancesModifications)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribeReservedInstancesModifications)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribeReservedInstancesModifications)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribeReservedInstancesModifications)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribeReservedInstancesModifications)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
