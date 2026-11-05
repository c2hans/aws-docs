---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_ReportOverview.html
---

# ReportOverview
<a name="API_s3Buckets_ReportOverview"></a>

A report of a migration: the prefix it is written under and, once it is written, its key, its checksum and, for the compatibility reports, the number of blocking findings in each category.

## Contents
<a name="API_s3Buckets_ReportOverview_Contents"></a>

 ** checksumCRC64NVME **   <a name="AmazonS3-Type-s3Buckets_ReportOverview-checksumCRC64NVME"></a>
The Base64-encoded CRC64NVME checksum of the object that `key` names. For a report that has a manifest, the manifest lists the checksum of each report file. This value is returned after the migration writes the report.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[A-Za-z0-9+/]{11}=`
Required: No

 ** invalidFindings **   <a name="AmazonS3-Type-s3Buckets_ReportOverview-invalidFindings"></a>
For the compatibility reports, the number of blocking findings in each category. The object compatibility report counts each blocked object once, under its most severe finding. Categories with no blocking findings are left out.
Type: String to long map
Valid Keys: `access | metadata | data | internal`
Required: No

 ** key **   <a name="AmazonS3-Type-s3Buckets_ReportOverview-key"></a>
The key of the report object in the bucket. For the object compatibility and object migration reports, this is the report's manifest; for the table compatibility report, it is the report itself. This value is returned after the migration writes the report. A migration doesn't always write every report. For example, a migration that fails during planning doesn't write the object migration report.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** prefix **   <a name="AmazonS3-Type-s3Buckets_ReportOverview-prefix"></a>
The key prefix that the report is written under.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 512.
Required: No

## See Also
<a name="API_s3Buckets_ReportOverview_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/ReportOverview)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/ReportOverview)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/ReportOverview)
