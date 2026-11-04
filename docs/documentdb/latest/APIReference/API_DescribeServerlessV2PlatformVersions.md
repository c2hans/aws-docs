---
source_url: https://docs.aws.amazon.com/documentdb/latest/APIReference/API_DescribeServerlessV2PlatformVersions.html
---

# DescribeServerlessV2PlatformVersions
<a name="API_DescribeServerlessV2PlatformVersions"></a>

Describes the properties of specific platform versions for Amazon DocumentDB Serverless v2.

## Request Parameters
<a name="API_DescribeServerlessV2PlatformVersions_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DefaultOnly **
Specifies whether to return only the default platform versions for each engine. The default platform version is the version used for new DB clusters.
Type: Boolean
Required: No

 ** Engine **
The database engine to return platform version details for.
Type: String
Required: No

 **Filters.Filter.N**
This parameter isn't currently supported.
Type: Array of [Filter](API_Filter.md) objects
Required: No

 ** IncludeAll **
Specifies whether to also include platform versions that are no longer in use. If you don't specify a value, the response includes only active platform versions.
Type: Boolean
Required: No

 ** Marker **
An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.
Type: String
Required: No

 ** MaxRecords **
 The maximum number of records to include in the response. If more records exist than the specified `MaxRecords` value, a pagination token (marker) is included in the response so that the remaining results can be retrieved.
Default: 100
Constraints: Minimum 20, maximum 100.
Type: Integer
Required: No

 ** ServerlessV2PlatformVersion **
A specific platform version to return details for.
Example: `3`
Type: String
Required: No

## Response Elements
<a name="API_DescribeServerlessV2PlatformVersions_ResponseElements"></a>

The following elements are returned by the service.

 ** Marker **
An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.
Type: String

 **ServerlessV2PlatformVersions.ServerlessV2PlatformVersionInfo.N**
A list of `ServerlessV2PlatformVersionInfo` elements.
Type: Array of [ServerlessV2PlatformVersionInfo](API_ServerlessV2PlatformVersionInfo.md) objects

## Errors
<a name="API_DescribeServerlessV2PlatformVersions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_DescribeServerlessV2PlatformVersions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/docdb-2014-10-31/DescribeServerlessV2PlatformVersions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/docdb-2014-10-31/DescribeServerlessV2PlatformVersions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/docdb-2014-10-31/DescribeServerlessV2PlatformVersions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/docdb-2014-10-31/DescribeServerlessV2PlatformVersions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/docdb-2014-10-31/DescribeServerlessV2PlatformVersions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/docdb-2014-10-31/DescribeServerlessV2PlatformVersions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/docdb-2014-10-31/DescribeServerlessV2PlatformVersions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/docdb-2014-10-31/DescribeServerlessV2PlatformVersions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/docdb-2014-10-31/DescribeServerlessV2PlatformVersions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/docdb-2014-10-31/DescribeServerlessV2PlatformVersions)
