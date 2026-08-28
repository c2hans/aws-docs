---
source_url: https://docs.aws.amazon.com/healthimaging/latest/devguide/reference-dicom.html
---

# DICOM support for AWS HealthImaging
<a name="reference-dicom"></a>

AWS HealthImaging supports specific DICOM elements and transfer syntaxes. Familiarize yourself with the supported Patient, Study, and Series level DICOM data elements, as HealthImaging metadata keys are based on them. Before you start an import, verify that your medical imaging data is compliant with HealthImaging's supported transfer syntaxes and DICOM element constraints.

**Note**
AWS HealthImaging does not currently support Binary Segmentation Images or Icon Image Sequence pixel data.

**Topics**
+ [Supported SOP classes](supported-sop-classes.md)
+ [Metadata normalization](metadata-normalization.md)
+ [Supported transfer syntaxes](supported-transfer-syntaxes.md)
+ [DICOM element constraints](dicom-element-constraints.md)
+ [DICOM metadata constraints](dicom-metadata-constraints.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthImaging. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query healthimaging` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
