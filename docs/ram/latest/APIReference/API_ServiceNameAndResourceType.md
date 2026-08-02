---
source_url: https://docs.aws.amazon.com/ram/latest/APIReference/API_ServiceNameAndResourceType.html
---

# ServiceNameAndResourceType
<a name="API_ServiceNameAndResourceType"></a>

Information about a shareable resource type and the AWS service to which resources of that type belong.

## Contents
<a name="API_ServiceNameAndResourceType_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** resourceRegionScope **   <a name="ram-Type-ServiceNameAndResourceType-resourceRegionScope"></a>
Specifies the scope of visibility of resources of this type:
+  **REGIONAL** – The resource can be accessed only by using requests that target the AWS Region in which the resource exists.
+  **GLOBAL** – The resource can be accessed from any AWS Region.
Type: String
Valid Values: `REGIONAL | GLOBAL`
Required: No

 ** resourceType **   <a name="ram-Type-ServiceNameAndResourceType-resourceType"></a>
The type of the resource. This takes the form of: `service-code`:`resource-code`, and is case-insensitive. For example, an Amazon EC2 Subnet would be represented by the string `ec2:subnet`.
Type: String
Required: No

 ** serviceName **   <a name="ram-Type-ServiceNameAndResourceType-serviceName"></a>
The name of the AWS service to which resources of this type belong.
Type: String
Required: No

## See Also
<a name="API_ServiceNameAndResourceType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ram-2018-01-04/ServiceNameAndResourceType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ram-2018-01-04/ServiceNameAndResourceType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ram-2018-01-04/ServiceNameAndResourceType)
