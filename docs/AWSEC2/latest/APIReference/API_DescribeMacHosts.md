---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeMacHosts.html
---

# DescribeMacHosts
<a name="API_DescribeMacHosts"></a>

Describes the specified EC2 Mac Dedicated Host or all of your EC2 Mac Dedicated Hosts.

## Request Parameters
<a name="API_DescribeMacHosts_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **Filter.N**
The filters.
+  `availability-zone` - The Availability Zone of the EC2 Mac Dedicated Host.
+  `instance-type` - The instance type size that the EC2 Mac Dedicated Host is configured to support.
Type: Array of [Filter](API_Filter.md) objects
Required: No

 **HostId.N**
 The IDs of the EC2 Mac Dedicated Hosts.
Type: Array of strings
Required: No

 **MaxResults**
The maximum number of results to return for the request in a single page. The remaining results can be seen by sending another request with the returned `nextToken` value. This value can be between 5 and 500. If `maxResults` is given a larger value than 500, you receive an error.
Type: Integer
Valid Range: Minimum value of 5. Maximum value of 500.
Required: No

 **NextToken**
The token to use to retrieve the next page of results.
Type: String
Required: No

## Response Elements
<a name="API_DescribeMacHosts_ResponseElements"></a>

The following elements are returned by the service.

 **macHostSet**
 Information about the EC2 Mac Dedicated Hosts.
Type: Array of [MacHost](API_MacHost.md) objects

 **nextToken**
The token to use to retrieve the next page of results.
Type: String

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_DescribeMacHosts_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_DescribeMacHosts_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribeMacHosts)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribeMacHosts)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribeMacHosts)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribeMacHosts)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribeMacHosts)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribeMacHosts)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribeMacHosts)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribeMacHosts)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribeMacHosts)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribeMacHosts)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
