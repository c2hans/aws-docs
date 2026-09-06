---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_Filter.html
---

# Filter
<a name="API_Filter"></a>

A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as tags, attributes, or IDs.

If you specify multiple filters, the filters are joined with an `AND`, and the request returns only results that match all of the specified filters.

The filters supported by a describe operation are documented with the describe operation. For example:
+  [DescribeAvailabilityZones](API_DescribeAvailabilityZones.md)
+  [DescribeImages](API_DescribeImages.md)
+  [DescribeInstances](API_DescribeInstances.md)
+  [DescribeKeyPairs](API_DescribeKeyPairs.md)
+  [DescribeSecurityGroups](API_DescribeSecurityGroups.md)
+  [DescribeSnapshots](API_DescribeSnapshots.md)
+  [DescribeSubnets](API_DescribeSubnets.md)
+  [DescribeTags](API_DescribeTags.md)
+  [DescribeVolumes](API_DescribeVolumes.md)
+  [DescribeVpcs](API_DescribeVpcs.md)

For more information, see [List and filter using the CLI and API](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Filtering.html#Filtering_Resources_CLI) in the *Amazon EC2 User Guide*.

## Contents
<a name="API_Filter_Contents"></a>

 ** Name **
The name of the filter. Filter names are case-sensitive.
Type: String
Required: No

 ** Value.N **
The filter values. Filter values are case-sensitive. If you specify multiple values for a filter, the values are joined with an `OR`, and the request returns all results that match any of the specified values.
Type: Array of strings
Required: No

## See Also
<a name="API_Filter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/Filter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/Filter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/Filter)
