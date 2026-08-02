---
source_url: https://docs.aws.amazon.com/solutions/latest/workload-discovery-on-aws/web-ui-and-storage-management.html
---

# Web UI and storage management
<a name="web-ui-and-storage-management"></a>

We developed the web UI using [React](https://reactjs.org/). The web UI provides a frontend console to allow users to interact with Workload Discovery on AWS.

 [Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html) is configured to append secure headers to every HTTP request to the web UI. This provides an additional layer of security, protecting against attacks such as [cross-site scripting](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-type-xss-match.html) (XSS).

 **Workload Discovery on AWS web UI and storage management components**

![workload discovery webui storage management](http://docs.aws.amazon.com/solutions/latest/workload-discovery-on-aws/images/workload-discovery-webui-storage-management.png)

The web UI resources are hosted in the `WebUIBucket` Amazon S3 bucket and distributed by Amazon CloudFront. AWS Amplify provides an abstraction layer to simplify the integrations to AWS AppSync and Amazon S3.

This solution uses AWS AppSync to facilitate interaction with various configurations available to Workload Discovery on AWS, including managing imported Regions. AWS AppSync utilizes the `Settings` AWS Lambda function to handle requests such as importing a new account or Region.
