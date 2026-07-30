---
source_url: https://docs.aws.amazon.com/ARG/latest/APIReference/API_ResourceStatus.html
---

# ResourceStatus
<a name="API_ResourceStatus"></a>

A structure that identifies the current group membership status for a resource. Adding a resource to a resource group is performed asynchronously as a background task. A `PENDING` status indicates, for this resource, that the process isn't completed yet.

## Contents
<a name="API_ResourceStatus_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Name **   <a name="ARG-Type-ResourceStatus-Name"></a>
The current status.
Type: String
Valid Values: `PENDING`
Required: No

## See Also
<a name="API_ResourceStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resource-groups-2017-11-27/ResourceStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resource-groups-2017-11-27/ResourceStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resource-groups-2017-11-27/ResourceStatus)
