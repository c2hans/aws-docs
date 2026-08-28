---
source_url: https://docs.aws.amazon.com/rekognition/latest/dg/creating-and-using-adapters.html
---

# Creating and using adapters
<a name="creating-and-using-adapters"></a>

Adapters are modular components that can be added to the existing Rekognition deep learning model, extending its capabilities for the tasks it’s trained on. By training a deep learning model with adapters, you can achieve better accuracy for image analysis tasks related to your specific use case.

To create and use an adapter, you must provide training and testing data to Rekognition. You can accomplish this in one of two different ways:
+ Bulk analysis and verification - You can create a training dataset by bulk analyzing images that Rekognition will analyze and assign labels to. You can then review the generated annotations for your images and verify or correct the predictions. For more information on how the Bulk analysis of images works, see [Bulk analysis](https://docs.aws.amazon.com/rekognition/latest/dg/bulk-analysis.html).
+ Manual annotation - With this approach you create your training data by uploading and annotating images. You create your test data by either uploading and annotating images or by auto-splitting.

Choose one of the following topics to learn more:

**Topics**
+ [Bulk analysis and verification](adapters-bulk-analysis.md)
+ [Manual annotation](adapters-manual-annotation.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Rekognition. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rekognition` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
