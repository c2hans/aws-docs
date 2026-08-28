---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_AutoSnapshotDetails.html
---

# AutoSnapshotDetails
<a name="API_AutoSnapshotDetails"></a>

Describes an automatic snapshot.

## Contents
<a name="API_AutoSnapshotDetails_Contents"></a>

 ** createdAt **   <a name="Lightsail-Type-AutoSnapshotDetails-createdAt"></a>
The timestamp when the automatic snapshot was created.
Type: Timestamp
Required: No

 ** date **   <a name="Lightsail-Type-AutoSnapshotDetails-date"></a>
The date of the automatic snapshot in `YYYY-MM-DD` format.
Type: String
Required: No

 ** fromAttachedDisks **   <a name="Lightsail-Type-AutoSnapshotDetails-fromAttachedDisks"></a>
An array of objects that describe the block storage disks attached to the instance when the automatic snapshot was created.
Type: Array of [AttachedDisk](API_AttachedDisk.md) objects
Required: No

 ** status **   <a name="Lightsail-Type-AutoSnapshotDetails-status"></a>
The status of the automatic snapshot.
Type: String
Valid Values: `Success | Failed | InProgress | NotFound`
Required: No

## See Also
<a name="API_AutoSnapshotDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/AutoSnapshotDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/AutoSnapshotDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/AutoSnapshotDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lightsail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lightsail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
