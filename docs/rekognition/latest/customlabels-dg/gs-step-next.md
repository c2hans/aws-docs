---
source_url: https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/gs-step-next.html
---

# Step 6: Next steps
<a name="gs-step-next"></a>

After you finished trying the examples projects, you can use your own images and datasets to create your own model. For more information, see [Understanding Amazon Rekognition Custom Labels](understanding-custom-labels.md).

Use the labeling information in the following table to train models similar to the example projects.

| Example | Training images | Test images |
| --- | --- | --- |
| Image classification (Rooms) | 1 Image-level label per image | 1 Image-level label per image  |
| Multi-label classification (Flowers) | Multiple image-level labels per image | Multiple image-level labels per image |
| Brand detection (Logos) | image level-labels (you can also use Labeled bounding boxes) | Labeled bounding boxes |
| Image localization (Circuit boards) | Labeled bounding boxes | Labeled bounding boxes |

The [Classifying images](tutorial-classification.md) shows you how to create a project, datasets, and models for an Image classification model.

For detailed information about creating datasets and training models, see [Creating an Amazon Rekognition Custom Labels model](creating-model.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Rekognition. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rekognition` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
