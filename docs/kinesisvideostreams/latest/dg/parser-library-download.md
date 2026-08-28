---
source_url: https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/parser-library-download.html
---

# Download the code
<a name="parser-library-download"></a>

In this section, you download the Java library and test code, and import the project into your Java IDE.

For prerequisites and other details about this procedure, see [Watch output from cameras using parser library](parser-library.md).

1. Create a directory and clone the library source code from the GitHub repository ([https://github.com/aws/amazon-kinesis-video-streams-parser-library](https://github.com/aws/amazon-kinesis-video-streams-parser-library)).

   ```
   git clone https://github.com/aws/amazon-kinesis-video-streams-parser-library
   ```

1. Open the Java IDE that you're using (for example, [Eclipse](https://www.eclipse.org/) or [IntelliJ IDEA](https://www.jetbrains.com/idea/)) and import the Apache Maven project that you downloaded:
   + **In Eclipse:** Choose **File**, **Import**, **Maven**, **Existing Maven Projects**, and navigate to the `kinesis-video-streams-parser-lib` folder.
   + **In IntelliJ Idea: ** Choose **Import**. Navigate to the **pom.xml** file in the root of the downloaded package.

    For more information, see the related IDE documentation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kinesis Video Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kinesisvideostreams` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
