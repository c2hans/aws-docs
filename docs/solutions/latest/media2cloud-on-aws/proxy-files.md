---
source_url: https://docs.aws.amazon.com/solutions/latest/media2cloud-on-aws/proxy-files.html
---

# Proxy files
<a name="proxy-files"></a>

 When a new video is uploaded to Amazon S3, the Media2Cloud on AWS solution automatically converts the video to MP4 format and creates a compressed version of the video known as a proxy file. For this solution, proxy files are used to allow users to upload videos of various sizing and formatting, without being subject to Amazon Rekognition and Amazon Transcribe quotas. Additionally, the proxy files can be used as reference proxies in a Media Asset Manager (MAM) for search, discovery, and [proxy editing](https://en.wikipedia.org/wiki/Offline_editing). The solution also generates compressed proxies for audio, images, and documents after extracting technical data from these file types during the ingestion process.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Media2Cloud on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
