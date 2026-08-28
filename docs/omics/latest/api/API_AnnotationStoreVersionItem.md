---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_AnnotationStoreVersionItem.html
---

# AnnotationStoreVersionItem
<a name="API_AnnotationStoreVersionItem"></a>

 Annotation store versions.

## Contents
<a name="API_AnnotationStoreVersionItem_Contents"></a>

 ** creationTime **   <a name="omics-Type-AnnotationStoreVersionItem-creationTime"></a>
 The time stamp for when an annotation store version was created.
Type: Timestamp
Required: Yes

 ** description **   <a name="omics-Type-AnnotationStoreVersionItem-description"></a>
 The description of an annotation store version.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: Yes

 ** id **   <a name="omics-Type-AnnotationStoreVersionItem-id"></a>
 The annotation store version ID.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** name **   <a name="omics-Type-AnnotationStoreVersionItem-name"></a>
 A name given to an annotation store version to distinguish it from others.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Pattern: `([a-z]){1}([a-z0-9_]){2,254}`
Required: Yes

 ** status **   <a name="omics-Type-AnnotationStoreVersionItem-status"></a>
 The status of an annotation store version.
Type: String
Valid Values: `CREATING | UPDATING | DELETING | ACTIVE | FAILED`
Required: Yes

 ** statusMessage **   <a name="omics-Type-AnnotationStoreVersionItem-statusMessage"></a>
 The status of an annotation store version.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Required: Yes

 ** storeId **   <a name="omics-Type-AnnotationStoreVersionItem-storeId"></a>
 The store ID for an annotation store version.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** updateTime **   <a name="omics-Type-AnnotationStoreVersionItem-updateTime"></a>
 The time stamp for when an annotation store version was updated.
Type: Timestamp
Required: Yes

 ** versionArn **   <a name="omics-Type-AnnotationStoreVersionItem-versionArn"></a>
 The Arn for an annotation store version.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:([^: ]*):([^: ]*):([^: ]*):([0-9]{12}):([^: ]*)`
Required: Yes

 ** versionName **   <a name="omics-Type-AnnotationStoreVersionItem-versionName"></a>
 The name of an annotation store version.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Pattern: `([a-z]){1}([a-z0-9_]){2,254}`
Required: Yes

 ** versionSizeBytes **   <a name="omics-Type-AnnotationStoreVersionItem-versionSizeBytes"></a>
 The size of an annotation store version in Bytes.
Type: Long
Required: Yes

## See Also
<a name="API_AnnotationStoreVersionItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/AnnotationStoreVersionItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/AnnotationStoreVersionItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/AnnotationStoreVersionItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthOmics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query omics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
