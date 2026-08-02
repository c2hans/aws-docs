---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_DeltaTarget.html
---

# DeltaTarget
<a name="API_DeltaTarget"></a>

Specifies a Delta data store to crawl one or more Delta tables.

## Contents
<a name="API_DeltaTarget_Contents"></a>

 ** ConnectionName **   <a name="Glue-Type-DeltaTarget-ConnectionName"></a>
The name of the connection to use to connect to the Delta table target.
Type: String
Required: No

 ** CreateNativeDeltaTable **   <a name="Glue-Type-DeltaTarget-CreateNativeDeltaTable"></a>
Specifies whether the crawler will create native tables, to allow integration with query engines that support querying of the Delta transaction log directly.
Type: Boolean
Required: No

 ** DeltaTables **   <a name="Glue-Type-DeltaTarget-DeltaTables"></a>
A list of the Amazon S3 paths to the Delta tables.
Type: Array of strings
Required: No

 ** WriteManifest **   <a name="Glue-Type-DeltaTarget-WriteManifest"></a>
Specifies whether to write the manifest files to the Delta table path.
Type: Boolean
Required: No

## See Also
<a name="API_DeltaTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/DeltaTarget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/DeltaTarget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/DeltaTarget)
