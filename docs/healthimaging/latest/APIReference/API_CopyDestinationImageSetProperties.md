---
source_url: https://docs.aws.amazon.com/healthimaging/latest/APIReference/API_CopyDestinationImageSetProperties.html
---

# CopyDestinationImageSetProperties
<a name="API_CopyDestinationImageSetProperties"></a>

Copy the image set properties of the destination image set.

## Contents
<a name="API_CopyDestinationImageSetProperties_Contents"></a>

 ** imageSetId **   <a name="healthimaging-Type-CopyDestinationImageSetProperties-imageSetId"></a>
The image set identifier of the copied image set properties.
Type: String
Pattern: `[0-9a-z]{32}`
Required: Yes

 ** latestVersionId **   <a name="healthimaging-Type-CopyDestinationImageSetProperties-latestVersionId"></a>
The latest version identifier for the destination image set properties.
Type: String
Pattern: `\d+`
Required: Yes

 ** createdAt **   <a name="healthimaging-Type-CopyDestinationImageSetProperties-createdAt"></a>
The timestamp when the destination image set properties were created.
Type: Timestamp
Required: No

 ** imageSetArn **   <a name="healthimaging-Type-CopyDestinationImageSetProperties-imageSetArn"></a>
The Amazon Resource Name (ARN) assigned to the destination image set.
Type: String
Pattern: `arn:aws((-us-gov)|(-iso)|(-iso-b)|(-cn))?:medical-imaging:[a-z0-9-]+:[0-9]{12}:datastore/[0-9a-z]{32}(/imageset/[0-9a-z]{32})?`
Required: No

 ** imageSetState **   <a name="healthimaging-Type-CopyDestinationImageSetProperties-imageSetState"></a>
The image set state of the destination image set properties.
Type: String
Valid Values: `ACTIVE | LOCKED | DELETED`
Required: No

 ** imageSetWorkflowStatus **   <a name="healthimaging-Type-CopyDestinationImageSetProperties-imageSetWorkflowStatus"></a>
The image set workflow status of the destination image set properties.
Type: String
Valid Values: `CREATED | COPIED | COPYING | COPYING_WITH_READ_ONLY_ACCESS | COPY_FAILED | UPDATING | UPDATING_FOR_STUDY_CONSISTENCY | UPDATED | UPDATE_FAILED | DELETING | DELETED | IMPORTING | IMPORTED | IMPORT_FAILED`
Required: No

 ** updatedAt **   <a name="healthimaging-Type-CopyDestinationImageSetProperties-updatedAt"></a>
The timestamp when the destination image set properties were last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_CopyDestinationImageSetProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/medical-imaging-2023-07-19/CopyDestinationImageSetProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/medical-imaging-2023-07-19/CopyDestinationImageSetProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/medical-imaging-2023-07-19/CopyDestinationImageSetProperties)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthImaging. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query healthimaging` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
