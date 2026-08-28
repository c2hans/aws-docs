---
source_url: https://docs.aws.amazon.com/healthimaging/latest/devguide/getting-started-tutorial.html
---

# AWS HealthImaging tutorial
<a name="getting-started-tutorial"></a>

**Objective**
The objective of this tutorial is to import DICOM P10 binaries (`.dcm` files) into an AWS HealthImaging [data store](getting-started-concepts.md#concept-data-store) and transform them into [image sets](getting-started-concepts.md#concept-image-set) comprised of [ metadata](getting-started-concepts.md#concept-metadata) and [image frames](getting-started-concepts.md#concept-image-frame) (pixel data). After importing the DICOM data, you use HealthImaging cloud native actions to access the image sets, metadata, and image frames based on your [access preference](what-is.md#what-is-accessing).

**Prerequisites**
All procedures listed in [Setting up](getting-started-setting-up.md) are required to complete this tutorial.

**Tutorial steps**

1. [Start import job](start-dicom-import-job.md)

1. [Get import job properties](get-dicom-import-job.md)

1. [Search image sets](search-image-sets.md)

1. [Get image set properties](get-image-set-properties.md)

1. [Get image set metadata](get-image-set-metadata.md)

1. [Get image set pixel data](get-image-frame.md)

1. [Delete data store](delete-data-store.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthImaging. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query healthimaging` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
