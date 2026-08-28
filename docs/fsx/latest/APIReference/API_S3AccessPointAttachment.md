---
source_url: https://docs.aws.amazon.com/fsx/latest/APIReference/API_S3AccessPointAttachment.html
---

# S3AccessPointAttachment
<a name="API_S3AccessPointAttachment"></a>

An S3 access point attached to an Amazon FSx volume.

## Contents
<a name="API_S3AccessPointAttachment_Contents"></a>

 ** CreationTime **   <a name="FSx-Type-S3AccessPointAttachment-CreationTime"></a>
The time that the resource was created, in seconds (since 1970-01-01T00:00:00Z), also known as Unix time.
Type: Timestamp
Required: No

 ** Lifecycle **   <a name="FSx-Type-S3AccessPointAttachment-Lifecycle"></a>
The lifecycle status of the S3 access point attachment. The lifecycle can have the following values:
+ AVAILABLE - the S3 access point attachment is available for use
+ CREATING - Amazon FSx is creating the S3 access point and attachment
+ DELETING - Amazon FSx is deleting the S3 access point and attachment
+ FAILED - The S3 access point attachment is in a failed state. Delete and detach the S3 access point attachment, and create a new one.
+ MISCONFIGURED - The S3 access point attachment has a configuration issue that prevents it from serving requests. Amazon FSx periodically checks for this condition and automatically returns the access point to AVAILABLE when the issue is resolved.
+ UPDATING - Amazon FSx is updating the S3 access point attachment
Type: String
Valid Values: `AVAILABLE | CREATING | DELETING | UPDATING | FAILED | MISCONFIGURED`
Required: No

 ** LifecycleTransitionReason **   <a name="FSx-Type-S3AccessPointAttachment-LifecycleTransitionReason"></a>
Describes why a resource lifecycle state changed.
Type: [LifecycleTransitionReason](API_LifecycleTransitionReason.md) object
Required: No

 ** Name **   <a name="FSx-Type-S3AccessPointAttachment-Name"></a>
The name of the S3 access point attachment; also used for the name of the S3 access point.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 50.
Pattern: `^(?=[a-z0-9])[a-z0-9-]{1,48}[a-z0-9]$`
Required: No

 ** OntapConfiguration **   <a name="FSx-Type-S3AccessPointAttachment-OntapConfiguration"></a>
The ONTAP configuration of the S3 access point attachment.
Type: [S3AccessPointOntapConfiguration](API_S3AccessPointOntapConfiguration.md) object
Required: No

 ** OpenZFSConfiguration **   <a name="FSx-Type-S3AccessPointAttachment-OpenZFSConfiguration"></a>
The OpenZFSConfiguration of the S3 access point attachment.
Type: [S3AccessPointOpenZFSConfiguration](API_S3AccessPointOpenZFSConfiguration.md) object
Required: No

 ** S3AccessPoint **   <a name="FSx-Type-S3AccessPointAttachment-S3AccessPoint"></a>
The S3 access point configuration of the S3 access point attachment.
Type: [S3AccessPoint](API_S3AccessPoint.md) object
Required: No

 ** Type **   <a name="FSx-Type-S3AccessPointAttachment-Type"></a>
The type of Amazon FSx volume that the S3 access point is attached to.
Type: String
Valid Values: `OPENZFS | ONTAP`
Required: No

## See Also
<a name="API_S3AccessPointAttachment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/S3AccessPointAttachment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/S3AccessPointAttachment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/S3AccessPointAttachment)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon FSx. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fsx` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
