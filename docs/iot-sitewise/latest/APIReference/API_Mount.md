---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_Mount.html
---

# Mount
<a name="API_Mount"></a>

Attaches a data source to the container filesystem for a task at a customer-supplied relative path under the service-owned mount root.

## Contents
<a name="API_Mount_Contents"></a>

 ** name **   <a name="iotsitewise-Type-Mount-name"></a>
A unique name for the mount within the task.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** relativePath **   <a name="iotsitewise-Type-Mount-relativePath"></a>
The relative path under the service-owned mount root where this mount is attached inside the container.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `((?!.*(^|/)\.\.?(/|$))(?!.*//)[a-zA-Z0-9._-][a-zA-Z0-9._/-]*[a-zA-Z0-9._-]|[a-zA-Z0-9_-])`
Required: Yes

 ** source **   <a name="iotsitewise-Type-Mount-source"></a>
The data source for the mount.
Type: [MountSource](API_MountSource.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** storageType **   <a name="iotsitewise-Type-Mount-storageType"></a>
The type of storage used for the mount.
Type: String
Valid Values: `SHARED_STORAGE`
Required: Yes

## See Also
<a name="API_Mount_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/Mount)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/Mount)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/Mount)
