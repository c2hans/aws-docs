---
source_url: https://docs.aws.amazon.com/iot-twinmaker/latest/guide/scenes-editing-add-tags.html
---

# Creating tags for your scenes
<a name="scenes-editing-add-tags"></a>

A tag is an annotation added to a specific `x,y,z` coordinate position of a scene. The tag uses an entity property to connect a scene part to the knowledge graph. You can use a tag to configure the behavior or visual appearance of an item in the scene, such as an alarm.

**Note**
To add functionality to tags, you apply visual rules to them.

Use the following procedure to add tags to your scene.

1. Select an object in the hierarchy, choose the **\+** button, and then choose **Add Tag**.

1. Name the tag. Then, to apply a visual rule, select a visual group Id.

1. In the dropdown lists, choose the EntityID, ComponentName, and PropertyName.

1. To populate the Data Path field, choose **Create DataFrameLabel**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT TwinMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-twinmaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
