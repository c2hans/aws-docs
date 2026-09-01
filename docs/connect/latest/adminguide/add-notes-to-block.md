---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/add-notes-to-block.html
---

# Add comments to a flow block in the flow designer in Connect Customer
<a name="add-notes-to-block"></a>

To add notes to a block, on the toolbar choose **Annotation**. Or, with your cursor on the flow designer canvas, use the shortcut keys: Ctrl \+ Alt \+N. A yellow box opens for you to type up to 1000 characters. With annotations, you can leave comments that others can view.

The following image shows the flow designer toolbar, the annotation box, and an annotation that is attached to a block.

![A block with annotations.](http://docs.aws.amazon.com/connect/latest/adminguide/images/flow-annotations.png)

The following GIF shows how to move notes around the flow designer and attach them to a block.

![Notes on the flow designer.](http://docs.aws.amazon.com/connect/latest/adminguide/images/flow-annotationsGIF.gif)

The following image shows the dropdown menu that you can use to view a list of all the notes in a flow. Choose a note to navigate to it. Use the search box to search notes across the flow.

![The list note menu item.](http://docs.aws.amazon.com/connect/latest/adminguide/images/flow-annotations2.png)

Note the following functionality:
+ Unicode and emojis are supported.
+ You can copy and paste, undo, and redo into the note box.
+ You can search notes across the flow.
+ When a block is deleted, the notes are deleted. When a block is restored, the notes are restored.

## Limits
<a name="note-limits"></a>

| Item | Limit |
| --- | --- |
| Character limit | 1000 characters per note |
| Attachment limit | 5 notes per block |
| Note limit | 100 notes per flow |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
