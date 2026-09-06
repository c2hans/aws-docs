---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ResourceStatus.html
---

# ResourceStatus
<a name="API_ResourceStatus"></a>

Contains information about the current status of a resource.

## Contents
<a name="API_ResourceStatus_Contents"></a>

 ** error **   <a name="iotsitewise-Type-ResourceStatus-error"></a>
Contains associated error information, if any.
Type: [ResourceError](API_ResourceError.md) object
Required: No

 ** state **   <a name="iotsitewise-Type-ResourceStatus-state"></a>
The current status of the resource.
Type: String
Valid Values: `CREATING | ACTIVE | UPDATING | DELETING | FAILED`
Required: No

## See Also
<a name="API_ResourceStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/ResourceStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/ResourceStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/ResourceStatus)
