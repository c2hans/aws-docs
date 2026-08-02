---
source_url: https://docs.aws.amazon.com/healthimaging/latest/APIReference/API_CopySourceImageSetProperties.html
---

# CopySourceImageSetProperties
<a name="API_CopySourceImageSetProperties"></a>

Copy source image set properties.

## Contents
<a name="API_CopySourceImageSetProperties_Contents"></a>

 ** imageSetId **   <a name="healthimaging-Type-CopySourceImageSetProperties-imageSetId"></a>
The image set identifier for the copied source image set.
Type: String
Pattern: `[0-9a-z]{32}`
Required: Yes

 ** latestVersionId **   <a name="healthimaging-Type-CopySourceImageSetProperties-latestVersionId"></a>
The latest version identifier for the copied source image set.
Type: String
Pattern: `\d+`
Required: Yes

 ** createdAt **   <a name="healthimaging-Type-CopySourceImageSetProperties-createdAt"></a>
The timestamp when the source image set properties were created.
Type: Timestamp
Required: No

 ** imageSetArn **   <a name="healthimaging-Type-CopySourceImageSetProperties-imageSetArn"></a>
The Amazon Resource Name (ARN) assigned to the source image set.
Type: String
Pattern: `arn:aws((-us-gov)|(-iso)|(-iso-b)|(-cn))?:medical-imaging:[a-z0-9-]+:[0-9]{12}:datastore/[0-9a-z]{32}(/imageset/[0-9a-z]{32})?`
Required: No

 ** imageSetState **   <a name="healthimaging-Type-CopySourceImageSetProperties-imageSetState"></a>
The image set state of the copied source image set.
Type: String
Valid Values: `ACTIVE | LOCKED | DELETED`
Required: No

 ** imageSetWorkflowStatus **   <a name="healthimaging-Type-CopySourceImageSetProperties-imageSetWorkflowStatus"></a>
The workflow status of the copied source image set.
Type: String
Valid Values: `CREATED | COPIED | COPYING | COPYING_WITH_READ_ONLY_ACCESS | COPY_FAILED | UPDATING | UPDATING_FOR_STUDY_CONSISTENCY | UPDATED | UPDATE_FAILED | DELETING | DELETED | IMPORTING | IMPORTED | IMPORT_FAILED`
Required: No

 ** updatedAt **   <a name="healthimaging-Type-CopySourceImageSetProperties-updatedAt"></a>
The timestamp when the source image set properties were updated.
Type: Timestamp
Required: No

## See Also
<a name="API_CopySourceImageSetProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/medical-imaging-2023-07-19/CopySourceImageSetProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/medical-imaging-2023-07-19/CopySourceImageSetProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/medical-imaging-2023-07-19/CopySourceImageSetProperties)
