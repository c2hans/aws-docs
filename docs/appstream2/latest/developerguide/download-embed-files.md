---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/download-embed-files.html
---

# Step 3: Download the Embedded Amazon WorkSpaces Applications Files
<a name="download-embed-files"></a>

To host embedded WorkSpaces Applications streaming sessions, you must download and configure the provided WorkSpaces Applications API JavaScript file.

1. On the [Embedding WorkSpaces Applications in Your Website](https://clients.amazonappstream.com/embed.html) webpage, choose the link in step 1 to download the WorkSpaces Applications Embed Kit .zip file, **appstream\_embed\_<version>.zip**.

1. Navigate to the location where you downloaded the .zip file, and extract the contents of the file.

1. The extracted contents of the file comprise one folder, **appstream-embed**. In addition to the **COPYRIGHT.txt** and **THIRD\_PARTY\_NOTICES.txt **file, this folder contains the following two files:
   + **appstream-embed.js** — Provides the embedded WorkSpaces Applications API. This JavaScript file includes the functions and API actions for configuring and controlling your embedded WorkSpaces Applications streaming session.
   + **embed-sample.html** — Describes how to use the embedded WorkSpaces Applications API to initialize a streaming session, call functions, and listen for events. This sample file expands on the information in this topic, to provide an example use case for developers.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
