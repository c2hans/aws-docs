---
source_url: https://docs.aws.amazon.com/solutions/latest/media2cloud-on-aws/revisions.html
---

# Revisions
<a name="revisions"></a>

|  Date  |  Change  |
| --- | --- |
|  January 2019  |  Initial release  |
|  March 2019  |  Modified JSON file descriptions.  |
|  November 2019  |  Updated the analysis workflow engine and added support for ingesting and analyzing images.  |
|  January 2021  |  Updated the list of AWS Partners.  |
|  February 2022  |  Release v3.0.0: New web user interface enhancing the user experience. New analysis features included Amazon Rekognition Custom Labels model, Amazon Rekognition Segment Detection, Amazon Transcribe Custom Vocabulary and Custom Language Model, Amazon Comprehend Custom Entity Recognizer. New Amazon OpenSearch Service provided deeper search results that allow customers to find search terms with the timestamps from the archived files. Frame based analysis feature allowing customers to define the time interval (rate) of running the detections on the video content by using Amazon Rekognition Image based API instead of Video based API. For more information, refer to the [CHANGELOG.md](https://github.com/aws-solutions/media2cloud-on-aws/blob/main/CHANGELOG.md) file in the GitHub repository.  |
|  February 2023  |  Release v3.1.0: Added a Service Catalog AppRegistry resource to register the CloudFormation template and underlying resources as an application in both [Service Catalog AppRegistry](https://docs.aws.amazon.com/servicecatalog/latest/arguide/intro-app-registry.html) and [AWS Systems Manager Application Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/application-manager.html). You can now manage costs, view logs, implement patching, and run automation runbooks for this solution from a central location. For more information, refer to the [CHANGELOG.md](https://github.com/aws-solutions/media2cloud-on-aws/blob/main/CHANGELOG.md) file in the GitHub repository.  |
|  April 2023  |  Release v3.1.1: Added package-lock.json files to all Lambda state machine functions to snapshot the dependency tree used. For more information, refer to the [CHANGELOG.md](https://github.com/aws-solutions/media2cloud-on-aws/blob/main/CHANGELOG.md) file in the GitHub repository.  |
|  April 2023  |  Release v3.1.2: Mitigated impact caused by new default settings for S3 Object Ownership (ACLs disabled) for all new S3 buckets. Updated object ownership configuration on the S3 buckets. Updated security patching. For more information, refer to the [CHANGELOG.md](https://github.com/aws-solutions/media2cloud-on-aws/blob/main/CHANGELOG.md) file in the GitHub repository.  |
|  August 2023  |  Release v3.1.3: Fixed an issue where media analysis result is not visible in the web application. For more information, refer to the [CHANGELOG.md](https://github.com/aws-solutions/media2cloud-on-aws/blob/main/CHANGELOG.md) file in the GitHub repository.  |
|  September 2023  |  Release v3.1.4: Updated Lambda nodes to Node.js 16. Added unit tests for document ingestion, information about stack update support, and default values to stack parameters. Updated parameter names for consistency. Added fix to allow PDF conversion to PNG files for previously unsupported font types and other bug fixes. For more information, refer to the [CHANGELOG.md](https://github.com/aws-solutions/media2cloud-on-aws/blob/main/CHANGELOG.md) file in the GitHub repository.  |
|  November 2023  |  Release v3.1.5: Updated package versions to resolve security vulnerabilities. For more information, refer to the [CHANGELOG.md](https://github.com/aws-solutions/media2cloud-on-aws/blob/main/CHANGELOG.md) file in the GitHub repository.  |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Media2Cloud on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
