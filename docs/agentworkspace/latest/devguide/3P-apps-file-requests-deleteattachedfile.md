---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-file-requests-deleteattachedfile.html
---

# Delete an attached file in Connect Customer agent workspace
<a name="3P-apps-file-requests-deleteattachedfile"></a>

Deletes an attached file along with the underlying S3 Object. The attached file is permanently deleted if S3 bucket versioning is not enabled. The request accepts an Attachment object, which has the following properties:
+ `associatedResourceArn: string`: Amazon Connect ARN of the resource that the file is attached to. Could be a Connect Email Contact ARN or a Connect Case ARN
+ `fileId: string`: ID in Connect's File record

 **Signature**

```
deleteAttachedFile(data: Attachment): Promise<void>
```

 **Usage**

```
await fileClient.deleteAttachedFile({
  associatedResourceArn: sampleAssociatedResourceArn, // Get this from the response from `startAttachedFileUpload`
  fileId: sampleFileId // Get this from the response from `startAttachedFileUpload`
});
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
