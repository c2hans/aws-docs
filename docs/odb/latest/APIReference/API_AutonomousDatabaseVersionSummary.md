---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_AutonomousDatabaseVersionSummary.html
---

# AutonomousDatabaseVersionSummary
<a name="API_AutonomousDatabaseVersionSummary"></a>

A summary of an available Oracle Database software version for Autonomous Databases.

## Contents
<a name="API_AutonomousDatabaseVersionSummary_Contents"></a>

 ** dbWorkload **   <a name="odb-Type-AutonomousDatabaseVersionSummary-dbWorkload"></a>
The intended use of the Autonomous Database that the version supports, such as transaction processing, data warehouse, JSON database, or APEX.
Type: String
Valid Values: `OLTP | AJD | APEX | LH`
Required: No

 ** details **   <a name="odb-Type-AutonomousDatabaseVersionSummary-details"></a>
Additional details about the Autonomous Database software version.
Type: String
Required: No

 ** version **   <a name="odb-Type-AutonomousDatabaseVersionSummary-version"></a>
The Oracle Database software version.
Type: String
Required: No

## See Also
<a name="API_AutonomousDatabaseVersionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/AutonomousDatabaseVersionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/AutonomousDatabaseVersionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/AutonomousDatabaseVersionSummary)
