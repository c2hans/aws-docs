---
source_url: https://docs.aws.amazon.com/solutions/latest/media2cloud-on-aws/web-interface.html
---

# Web interface
<a name="web-interface"></a>

 This solution deploys a web interface that allows you to upload, browse, search video and image files, extract metadata, and search and discover content metadata. The web interface leverages Amazon Cognito for user authentication and is powered by web assets [hosted](https://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteHosting.html) in the web Amazon S3 bucket. Amazon CloudFront provides public access to the solution’s website bucket contents. An [Amazon API Gateway RESTful API](https://docs.aws.amazon.com/apigateway/api-reference/) is used for searching results stored in the Amazon OpenSearch Service cluster, and AWS IoT Core is used as a publish/subscribe message broker to periodically update workflow progress to connected web clients.

 The web interface also provides a human-in-the-loop feature that allows customers to remediate cases where Amazon Rekognition cannot detect individuals in a video or cannot provide logical groupings of related individuals based on the customer’s specific use case, for example, Olympic athletes for a specific year. Using the web interface, customers can create face collections and index people in the video to that face collection.

![Media2Cloud on AWS web interface architecture diagram](http://docs.aws.amazon.com/solutions/latest/media2cloud-on-aws/images/media2cloud-web-interface.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Media2Cloud on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
