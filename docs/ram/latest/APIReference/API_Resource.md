---
source_url: https://docs.aws.amazon.com/ram/latest/APIReference/API_Resource.html
---

# Resource
<a name="API_Resource"></a>

Describes a resource associated with a resource share in AWS RAM.

## Contents
<a name="API_Resource_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** arn **   <a name="ram-Type-Resource-arn"></a>
The [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the resource.
Type: String
Required: No

 ** creationTime **   <a name="ram-Type-Resource-creationTime"></a>
The date and time when the resource was associated with the resource share.
Type: Timestamp
Required: No

 ** lastUpdatedTime **   <a name="ram-Type-Resource-lastUpdatedTime"></a>
The date an time when the association between the resource and the resource share was last updated.
Type: Timestamp
Required: No

 ** resourceGroupArn **   <a name="ram-Type-Resource-resourceGroupArn"></a>
The [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the resource group. This value is available only if the resource is part of a resource group.
Type: String
Required: No

 ** resourceRegionScope **   <a name="ram-Type-Resource-resourceRegionScope"></a>
Specifies the scope of visibility of this resource:
+  **REGIONAL** – The resource can be accessed only by using requests that target the AWS Region in which the resource exists.
+  **GLOBAL** – The resource can be accessed from any AWS Region.
Type: String
Valid Values: `REGIONAL | GLOBAL`
Required: No

 ** resourceShareArn **   <a name="ram-Type-Resource-resourceShareArn"></a>
The [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the resource share this resource is associated with.
Type: String
Required: No

 ** status **   <a name="ram-Type-Resource-status"></a>
The current status of the resource.
Type: String
Valid Values: `AVAILABLE | ZONAL_RESOURCE_INACCESSIBLE | LIMIT_EXCEEDED | UNAVAILABLE | PENDING`
Required: No

 ** statusMessage **   <a name="ram-Type-Resource-statusMessage"></a>
A message about the status of the resource.
Type: String
Required: No

 ** type **   <a name="ram-Type-Resource-type"></a>
The resource type. This takes the form of: `service-code`:`resource-code`, and is case-insensitive. For example, an Amazon EC2 Subnet would be represented by the string `ec2:subnet`.
Type: String
Required: No

## See Also
<a name="API_Resource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ram-2018-01-04/Resource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ram-2018-01-04/Resource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ram-2018-01-04/Resource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS RAM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ram` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
