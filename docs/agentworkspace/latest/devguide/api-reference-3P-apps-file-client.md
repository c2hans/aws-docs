---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/api-reference-3P-apps-file-client.html
---

# Connect Customer agent workspace File API
<a name="api-reference-3P-apps-file-client"></a>

The Amazon Connect SDK provides a `FileClient` which serves as an interface that you can use to make file requests to upload, retrieve, and delete attached files.

The `FileClient` accepts an optional constructor argument, ` ConnectClientConfig` which itself is defined as:

```
export type ConnectClientConfig = {
    context?: ModuleContext;
    provider?: AmazonConnectProvider;
};
```

If you do not provide a value for this config, then the client will default to using the ** AmazonConnectProvider** set in the global provider scope. You can also manually configure this using **setGlobalProvider**.

You can instantiate the agent client as follows:

```
import { FileClient } from "@amazon-connect/file";

const fileClient = new FileClient({ provider });
```

**Note**
You must first instantiate the [ AmazonConnectApp](getting-started-initialize-sdk.md) which initializes the default AmazonConnectProvider and returns ` { provider } `. This is the recommended option.

Alternatively, providing a constructor argument:

```
import { FileClient } from "@amazon-connect/file";

const fileClient = new FileClient({
    context: sampleContext,
    provider: sampleProvider
});
```

**Note**
Third-party applications must be configured with \* permission in order to utilize the FileClient APIs.

The following sections describe API calls for working with the File API.

**Topics**
+ [batchGetAttachedFileMetadata()](3P-apps-file-requests-batchgetattachedfilemetadata.md)
+ [completeAttachedFileUpload()](3P-apps-file-requests-completeattachedfileupload.md)
+ [deleteAttachedFile()](3P-apps-file-requests-deleteattachedfile.md)
+ [getAttachedFileUrl()](3P-apps-file-requests-getattachedfileurl.md)
+ [startAttachedFileUpload()](3P-apps-file-requests-startattachedfileupload.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
