---
source_url: https://docs.aws.amazon.com/healthimaging/latest/devguide/modifying-image-sets.html
---

# Modifying image sets with AWS HealthImaging
<a name="modifying-image-sets"></a>

DICOM import jobs typically require you to modify your [image sets](getting-started-concepts.md#concept-image-set) for the following reasons:
+ Patient safety
+ Data consistency
+ Reduce storage costs

**Important**
During import, HealthImaging processes DICOM instance binaries (`.dcm` files) and transforms them into image sets. Use HealthImaging [cloud native actions](https://docs.aws.amazon.com/healthimaging/latest/APIReference/API_Operations.html) (APIs) to manage data stores and image sets. Use HealthImaging's [representation of DICOMweb services](using-dicomweb.md) to return DICOMweb responses.

HealthImaging provides several cloud native APIs to simplify the image set modification process. The following topics describe how to modify image sets using AWS CLI and AWS SDKs.

**Topics**
+ [Listing image set versions](list-image-set-versions.md)
+ [Updating image set metadata](update-image-set-metadata.md)
+ [Copying an image set](copy-image-set.md)
+ [Deleting an image set](delete-image-set.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthImaging. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query healthimaging` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
