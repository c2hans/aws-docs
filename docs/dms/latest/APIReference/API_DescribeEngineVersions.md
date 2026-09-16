---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeEngineVersions.html
---

# DescribeEngineVersions
<a name="API_DescribeEngineVersions"></a>

Returns information about the replication instance versions used in the project.

## Request Syntax
<a name="API_DescribeEngineVersions_RequestSyntax"></a>

```
{
   "Marker": "{{string}}",
   "MaxRecords": {{number}}
}
```

## Request Parameters
<a name="API_DescribeEngineVersions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Marker](#API_DescribeEngineVersions_RequestSyntax) **   <a name="DMS-DescribeEngineVersions-request-Marker"></a>
An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.
Type: String
Required: No

 ** [MaxRecords](#API_DescribeEngineVersions_RequestSyntax) **   <a name="DMS-DescribeEngineVersions-request-MaxRecords"></a>
The maximum number of records to include in the response. If more records exist than the specified `MaxRecords` value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.
Type: Integer
Required: No

## Response Syntax
<a name="API_DescribeEngineVersions_ResponseSyntax"></a>

```
{
   "EngineVersions": [
      {
         "AutoUpgradeDate": number,
         "AvailableUpgrades": [ "string" ],
         "DeprecationDate": number,
         "ForceUpgradeDate": number,
         "LaunchDate": number,
         "Lifecycle": "string",
         "ReleaseStatus": "string",
         "Version": "string"
      }
   ],
   "Marker": "string"
}
```

## Response Elements
<a name="API_DescribeEngineVersions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EngineVersions](#API_DescribeEngineVersions_ResponseSyntax) **   <a name="DMS-DescribeEngineVersions-response-EngineVersions"></a>
Returned `EngineVersion` objects that describe the replication instance engine versions used in the project.
Type: Array of [EngineVersion](API_EngineVersion.md) objects

 ** [Marker](#API_DescribeEngineVersions_ResponseSyntax) **   <a name="DMS-DescribeEngineVersions-response-Marker"></a>
An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.
Type: String

## Errors
<a name="API_DescribeEngineVersions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_DescribeEngineVersions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dms-2016-01-01/DescribeEngineVersions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dms-2016-01-01/DescribeEngineVersions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/DescribeEngineVersions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dms-2016-01-01/DescribeEngineVersions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/DescribeEngineVersions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dms-2016-01-01/DescribeEngineVersions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dms-2016-01-01/DescribeEngineVersions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dms-2016-01-01/DescribeEngineVersions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/dms-2016-01-01/DescribeEngineVersions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/DescribeEngineVersions)
