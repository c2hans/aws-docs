---
source_url: https://docs.aws.amazon.com/cloud-map/latest/api/API_ServiceAttributes.html
---

# ServiceAttributes
<a name="API_ServiceAttributes"></a>

A complex type that contains information about attributes associated with a specific service.

## Contents
<a name="API_ServiceAttributes_Contents"></a>

 ** Attributes **   <a name="cloudmap-Type-ServiceAttributes-Attributes"></a>
A string map that contains the following information for the service that you specify in `ServiceArn`:
+ The attributes that apply to the service.
+ For each attribute, the applicable value.
You can specify a total of 30 attributes.
Type: String to string map
Map Entries: Maximum number of 30 items.
Key Length Constraints: Maximum length of 255.
Value Length Constraints: Maximum length of 1024.
Required: No

 ** ResourceOwner **   <a name="cloudmap-Type-ServiceAttributes-ResourceOwner"></a>
The ID of the AWS account that created the namespace with which the service is associated. If this isn't your account ID, it is the ID of the account that shared the namespace with your account. For more information about shared namespaces, see [Cross-account AWS Cloud Map namespace sharing](https://docs.aws.amazon.com/cloud-map/latest/dg/sharing-namespaces.html) in the * AWS Cloud Map Developer Guide*.
Type: String
Length Constraints: Fixed length of 12.
Required: No

 ** ServiceArn **   <a name="cloudmap-Type-ServiceAttributes-ServiceArn"></a>
The ARN of the service that the attributes are associated with.
Type: String
Length Constraints: Maximum length of 255.
Required: No

## See Also
<a name="API_ServiceAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicediscovery-2017-03-14/ServiceAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicediscovery-2017-03-14/ServiceAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicediscovery-2017-03-14/ServiceAttributes)
