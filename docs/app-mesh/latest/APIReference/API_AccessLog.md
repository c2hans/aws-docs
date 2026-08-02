---
source_url: https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_AccessLog.html
---

# AccessLog
<a name="API_AccessLog"></a>

An object that represents the access logging information for a virtual node.

## Contents
<a name="API_AccessLog_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** file **   <a name="appmesh-Type-AccessLog-file"></a>
The file object to send virtual node access logs to.
Type: [FileAccessLog](API_FileAccessLog.md) object
Required: No

## See Also
<a name="API_AccessLog_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/AccessLog)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/AccessLog)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/AccessLog)
