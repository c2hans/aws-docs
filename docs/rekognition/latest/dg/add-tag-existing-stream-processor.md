---
source_url: https://docs.aws.amazon.com/rekognition/latest/dg/add-tag-existing-stream-processor.html
---

# Add tags to an existing stream processor
<a name="add-tag-existing-stream-processor"></a>

**Note**
Streaming Video and Bulk Image Analysis is no longer available to new customers. For more information, see [Amazon Rekognition feature availability changes](rekognition-availability-changes.md).
**This change does not impact the availability of other Amazon Rekognition features.**

You can identify, organize, search for, and filter Amazon Rekognition stream processors by using tags. Each tag is a label consisting of a user-defined key and value.

To add one or more tags to an existing stream processor, use the `TagResource` operation. Specify the stream processor's Amazon Resource Name (ARN) (`ResourceArn`) and the tags (`Tags`) that you want to add. The following example shows how to add two tags.

```
aws rekognition tag-resource --resource-arn resource-arn \
                --tags '{"key1":"value1","key2":"value2"}'
```

**Note**
If you do not know the stream processor's Amazon Resource Name, you can use the `DescribeStreamProcessor` operation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Rekognition. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rekognition` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
