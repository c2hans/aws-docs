---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/polly_example_polly_LipSync_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Create a lip-sync application with Amazon Polly using an AWS SDK
<a name="polly_example_polly_LipSync_section"></a>

The following code example shows how to create a lip-sync application with Amazon Polly.

------
#### [ Python ]

**SDK for Python (Boto3)**
 Shows how to use Amazon Polly and Tkinter to create a lip-sync application that displays an animated face speaking along with the speech synthesized by Amazon Polly. Lip-sync is accomplished by requesting a list of visemes from Amazon Polly that match up with the synthesized speech.
+ Get voice metadata from Amazon Polly and display it in a Tkinter application.
+ Get synthesized speech audio and matching viseme speech marks from Amazon Polly.
+ Play the audio with synchronized mouth movements in an animated face.
+ Submit asynchronous synthesis tasks for long texts and retrieve the output from an Amazon Simple Storage Service (Amazon S3) bucket.
 For complete source code and instructions on how to set up and run, see the full example on [GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/polly#code-examples).

**Services used in this example**
+ Amazon Polly

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
