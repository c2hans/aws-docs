---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_DbServerPatchingDetails.html
---

# DbServerPatchingDetails
<a name="API_DbServerPatchingDetails"></a>

The scheduling details for the quarterly maintenance window. Patching and system updates take place during the maintenance window.

## Contents
<a name="API_DbServerPatchingDetails_Contents"></a>

 ** estimatedPatchDuration **   <a name="odb-Type-DbServerPatchingDetails-estimatedPatchDuration"></a>
Estimated time, in minutes, to patch one database server.
Type: Integer
Required: No

 ** patchingStatus **   <a name="odb-Type-DbServerPatchingDetails-patchingStatus"></a>
The status of the patching operation. Possible values are `SCHEDULED`, `MAINTENANCE_IN_PROGRESS`, `FAILED`, and `COMPLETE`.
Type: String
Valid Values: `COMPLETE | FAILED | MAINTENANCE_IN_PROGRESS | SCHEDULED`
Required: No

 ** timePatchingEnded **   <a name="odb-Type-DbServerPatchingDetails-timePatchingEnded"></a>
The time when the patching operation ended.
Type: String
Required: No

 ** timePatchingStarted **   <a name="odb-Type-DbServerPatchingDetails-timePatchingStarted"></a>
The time when the patching operation started.
Type: String
Required: No

## See Also
<a name="API_DbServerPatchingDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/DbServerPatchingDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/DbServerPatchingDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/DbServerPatchingDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Oracle Database@AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query odb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
